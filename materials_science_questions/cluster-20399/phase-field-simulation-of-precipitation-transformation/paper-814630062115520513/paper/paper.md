![](./images/814630062115520513_1.jpg)
![](./images/814630062115520513_2.jpg)

Available online at www.sciencedirect.com

# Large scale phase-field simulations of directional ternary eutectic solidification

Johannes Hötzer, $^{a,b,*}$ Marcus Jainta, $^{a}$ Philipp Steinmetz, $^{a}$ Britta Nestler, $^{a,b}$ Anne Dennstedt, $^{d}$
Amber Genau, $^{e}$ Martin Bauer, $^{c}$ Harald Köstler $^{c}$ and Ulrich Rüde $^{c}$

$^{a}$ Institute for Applied Materials - Computational Materials Science (IAM-CMS), Karlsruhe Institute of Technology (KIT), Haid-und-Neu-Str. 7, 76131 Karlsruhe, Germany
$^{b}$ Institute of Materials and Processes, Karlsruhe University of Applied Sciences, Moltkestrasse 30, D 76133 Karlsruhe, Germany
$^{c}$ Lehrstuhl für Informatik 10 (Systemsimulation), Universität Erlangen-Nürnberg, Martensstraße 5a, 91058 Erlangen, Germany
$^{d}$ Deutsches Zentrum für Luft- und Raumfahrt e.V. (DLR), Institut für Materialphysik im Weltraum, Linder Höhe, 51170 Köln, Germany
$^{e}$ Dept. of Materials Science and Engineering, University of Alabama at Birmingham, 1720 2nd Ave. S, Birmingham, AL 35294, USA

Received 16 February 2015; revised 27 March 2015; accepted 28 March 2015

**Abstract**—Pattern formation in ternary eutectic microstructures is difficult to predict because of the complex interactions between diffusion and surface energies, as well as the large number of possible configurations which three phases can assume. The silver-aluminum-copper (Ag-Al-Cu) ternary eutectic is of particular interest to researchers, but its study is complicated by an unusually large solubility change. Due to this change, it is difficult to observe the patterns that form during the solid-liquid phase transition experimentally. This causes significant differences between the structure that forms during solidification and what is observed after traditional directional solidification processing. In order to model the solidification behavior and pattern formation in representative volume elements, large scale phase-field simulations are employed. Two different parameter sets are used. The first set uses the phase fractions and compositions of the as-solidified structure. The other used phase fractions found at lower temperatures in order to be comparable to experimental microstructures available in the literature. The second set of simulation results is compared quantitatively to experimental micrographs and found to be in good agreement. The predicted three-dimensional microstructures for the as-solidified structure are presented.

© 2015 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

**Keywords**: Phase-field simulation; Directional solidification; Eutectic structure; Al-Ag-Cu; Pattern formation

---

## 1. Introduction

The manipulation of metal alloys to change the properties of the resulting material is a technique that has been practiced for thousands of years. This article helps to improve our understanding of the underlying processes, in order to control the behavior and properties of alloys at the levels required for modern engineering applications. In industrial production, metal casting remains one of the primary means of production, where the properties of the material are in large part determined by the microstructure that forms while the alloy is solidifying. Advances in fields like chemistry, materials science, and computer science, now allow for accurate modeling of increasingly complex solidification behavior. The composition of the alloys and the process conditions themselves have a significant influence on the developing microstructures, whose patterns in turn affect the material properties. Alloys which exhibit a ternary eutectic point are one particular class of alloys in which there is growing interest, in part because their adjustable properties show promise in a variety of industrial applications. They are currently used in a number of lead-free solders [1]. From a scientific point of view they are of interest due to the complex interplay between diffusion, undercooling and surface energies at the solid/liquid interface, they produce a wide variety of microstructural patterns. The observed patterns can be classified by five theoretical patterns that were predicted by Ruggiero et al. [2] based on geometrical considerations for ternary systems, which were later depicted graphically by Lewis et al. [3].

---

*Corresponding author at: Institute for Applied Materials-Computational Materials Science (IAM-CMS), Karlsruhe Institute of Technology (KIT), Haid-und-Neu-Str. 7, 76131 Karlsruhe, Germany. Tel.: +49 721 608 45315; fax: +49 721 608 44364.; e-mail addresses: johannes.hoetzer@kit.edu; marcus.jainta@kit.edu; philipp.steinmetz@kit.edu; britta.nestler@kit.edu; anne.dennstedt@dlr.de; genau@uab.edu; martin.bauer@fau.de; harald.koestler@fau.de; ulrich.ruede@fau.de

http://dx.doi.org/10.1016/j.actamat.2015.03.051
1359-6462/© 2015 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

![](./images/814630062115520513_3.jpg)

The focus of the work is the pattern formation during the solidification of the system silver-aluminum-copper (Ag-Al-Cu) around the ternary eutectic point. The system is favored due to a relatively low eutectic temperature (773.6 K) and a roughly equal amount of each solid phase. First experimental observations of ternary eutectic systems, including Ag-Al-Cu, were conducted by Cooksey and Hellawell [4] in 1967. It should be considered that the undercooling velocity was orders of magnitudes larger compared to current experimental studies and the composition of the samples is off-eutectic. The influence of different velocities and compositions was systematically studied by McCartney et al. [5]. Analysis and modeling of the Ag- Al-Cu system is also supported by a detailed thermody- namic description developed by Hecht and Witusiewicz et al. [6-8]. The liquidus projection and the ternary eutectic point $E_{cal}$ , shown in Fig. 1, are based on these thermodynamic results.

One difficulty in analyzing structures in the Ag-Al-Cu system is a result of the unusually large change in solubility of Ag in the Al-phase. The solubility falls by more than $50\%$ (from $16.9\%$ to around $8\%$) over the 20 K directly below the eutectic temperature [9]. This leads to significant solid state evolution of the microstructure, particularly in directional solidification experiments at the low velocities necessary to maintain coupled growth and a planar interface. As a result, both phase fractions and composition of the Al-phase in directionally solidified samples deviate significantly from equilibrium eutectic values [9-11]. However, experimental results do show that the ratio of experimentally measured phase fractions to each other always corresponds to the equilibrium fractions predicted by the phase diagram in a small range below the eutectic temperature. The original solidification microstructure can only be obtained via quenching experiments, and observation of the sample directly behind the quenched interface. The authors are not aware of such microstructural images currently available in the literature.

The goal of this work is to investigate the pattern formation during solidification of (Ag-Al-Cu) ternary eutectics using phase field modeling. For this we simulate three-dimensional microstructures for comparison with experimental micrographs and analyze the influence of different parameters. In last years, the phase-field method has been established as a powerful tool to simulate free boundary problems, such as solidification [12,13]. The coupling to different physical phenomena enables a broad range of applications. In order to account for both the actual solidification behavior of the material and to compare the results with published experimental microstructures from the system, two different parameter sets were used. For the first, the actual ternary eutectic composition was used, as indicated by $E_{cal}$ in Fig. 1. To model the microstructure after solid state diffusion without the need to simulate the shift in solubility, a second parameter set was compiled. For this set, an off-eutectic composition is selected that produce the phase fractions comparable to those reported experimentally. This composition is depicted in Fig. 1 as $E_{exp}$.

This article is structured as follows: First we introduce the phase-field model and the evolution of the chemical potential. Then the applied framework and the implementation are introduced. The setup section describes the two parameter sets: the thermodynamic Calphad-database set and the experimental set. In the result section the patterns and their evolution during the simulations are presented. The simulations and an experimental micrograph are then compared, using nearest neighbor statistics. We conclude our paper by a short discussion of the results and the implications for further studies.

### 2. Model

To study the solidification process of a ternary eutectic system, we use a general thermodynamically consistent phase-field model, based on the work of [14-17].

#### 2.1. Order parameter

For the model we consider the domain $\Omega \subset \mathbb{R}^{d}$ with $d \in \{ 1,2,3\}$, which is divided in $N \in \mathbb{N}$ subdomains $\Omega_{\alpha} \subseteq \Omega$, where each $\Omega_{\alpha}$ is an order-parameter and represents a phase $\alpha$, which is described by the positive part of the $\alpha$ phase-field, $\phi_{\alpha}:\Omega \times \mathbb{R} \to [0,1]$, describing the local phase fractions at the position $\boldsymbol{x} \in \Omega$ and the time $t \in \mathbb{R}$. The function $\phi_{\alpha}(\boldsymbol{x},t)$ is twice continuously differentiable. These phase-fields are defined as a vector on a simplex, $\boldsymbol{\phi} \in \Lambda^{N}, \forall \boldsymbol{x},t$ which is written as $\Lambda^{N} = \left\{ \boldsymbol{v} \in [0,1]^{N} \mid \sum_{\alpha=1}^{N} v_{\alpha} = 1 \right\}$, and represents the thermodynamic state of the phase.

#### 2.2. The phase-field model

In order to model the total energy, we use the grand potential functional $\Psi$ of the form

$$
\Psi(\boldsymbol{\phi}, \boldsymbol{\mu}, T)=\int_{\Omega}\left(\varepsilon a(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})+\frac{1}{\varepsilon} \omega(\boldsymbol{\phi})\right)+\psi(\boldsymbol{\phi}, \boldsymbol{\mu}, T) d \Omega
\tag{1}
$$

that consists of the gradient energy density $\varepsilon a(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})$, the potential energy density $\omega(\boldsymbol{\phi})$ and the driving force $\psi(\boldsymbol{\phi}, \boldsymbol{\mu}, T)$. The functional depends on the order parameter $\boldsymbol{\phi}$, the chemical potential $\boldsymbol{\mu}(\boldsymbol{c}, T)$ and the temperature $T$.

![](./images/814630062115520513_4.jpg)

Fig. 1. Liquidus projection of the Ag-Al-Cu system based on the Calphad dataset. The thermodynamic ternary eutectic point is labeled as $E_{cal}$. The point $E_{exp}$ was used to produce a simulation with phase fractions comparable to experiments [9-11].

The small length scale parameter $\varepsilon$ is related to the interface thickness. The concentration vector $\boldsymbol{c} \in \Delta^{K}$ with $K$ components is defined on a simplex $\Delta^{K}$, similar to the order-parameters. In order to model a defined diffuse transition between two or more phases, a potential energy and an isotropic gradient energy density of the form

$$
a(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})=\sum_{\substack{\alpha, \beta=1 \\(\alpha<\beta)}}^{N, N} \gamma_{\alpha \beta}\left|\vec{q}_{\alpha \beta}\right|^{2}
\tag{2}
$$

is used. Here, the surface energy density is represented by $\gamma_{\alpha \beta}$ and the generalized gradient vector by $\vec{q}_{\alpha \beta}=\phi_{\alpha} \nabla \phi_{\beta}-$ $\phi_{\beta} \nabla \phi_{\alpha}$. The generalized potential energy density of obstacle type is formulated as

$$
\omega(\boldsymbol{\phi})=
\begin{cases}
\frac{16}{\pi^{2}} \sum_{\substack{\alpha, \beta=1 \\(\alpha<\beta)}}^{N, N} \gamma_{\alpha \beta} \phi_{\alpha} \phi_{\beta}+\sum_{\substack{\alpha, \beta, \delta=1 \\(\alpha<\beta<\delta)}}^{N, N, N} \gamma_{\alpha \beta \delta} \phi_{\alpha} \phi_{\beta} \phi_{\delta} &, \boldsymbol{\phi} \in \Delta^{N} \\
\infty &, \boldsymbol{\phi} \notin \Delta^{N}
\end{cases}.
\tag{3}
$$

The higher order term $\gamma_{\alpha \beta \delta}$ in (3) suppresses spurious contributions of third phases in the binary interfaces.

The driving force $\psi(\boldsymbol{\phi}, \boldsymbol{\mu}, T)$ can be derived from free energies, which are known from experiments and are reported in the literature [17,7,8]. Assuming that the volume of the system and the pressure are constant, the free energies and the Gibbs energies differ by a constant and therefore their concentration derivatives are equal. So, both energies can be used for the calculation. To facilitate the calculations, a parabolic fitting approach, written as

$$
f_{\alpha}(\boldsymbol{c}, T)=\left\langle\boldsymbol{c}, \boldsymbol{\Xi}_{\alpha}(T) \boldsymbol{c}\right\rangle+\left\langle\boldsymbol{c}, \boldsymbol{\xi}_{\alpha}(T)\right\rangle+X_{\alpha}(T)
\tag{4}
$$

is used. The matrix $\boldsymbol{\Xi}_{\alpha}(T)$, the vector $\boldsymbol{\xi}_{\alpha}(T)$ and the scalar $X_{\alpha}(T)$ are calculated from the free energies. By exploiting the conservation of mass for each element, the concentration vector, and therefore the whole formulation, can be reduced by one component, so that $c_{K}=1-\sum_{i=1}^{K-1} c_{i}$. In the neighborhood of the considered concentration, this is a suitable approximation. The chemical potentials $\boldsymbol{\mu}_{\alpha}(\boldsymbol{c}, T)=\frac{\partial f_{\alpha}(\boldsymbol{c})}{\partial \boldsymbol{c}}=2 \boldsymbol{\Xi}_{\alpha} \boldsymbol{c}+\boldsymbol{\xi}_{\alpha}$ and the specific concentration $\boldsymbol{c}_{\alpha}(\boldsymbol{\mu}, T)=\frac{1}{2} \boldsymbol{\Xi}_{\alpha}^{-1}\left(\boldsymbol{\mu}-\boldsymbol{\xi}_{\alpha}\right)$ can easily be derived from the free energies. The driving force of the system is caused by the differences of the grand potentials which are derived from the free energies. This force is written as

$$
\psi(\boldsymbol{\phi}, \boldsymbol{\mu}, T)=\sum_{\alpha=1}^{N}\left(\left\langle\boldsymbol{\mu}, \boldsymbol{\Upsilon}_{\alpha}(T) \boldsymbol{\mu}+\boldsymbol{v}_{\alpha}(T)\right\rangle+Y_{\alpha}(T)\right) h_{\alpha}(\boldsymbol{\phi})
\tag{5}
$$

with $\boldsymbol{\Upsilon}_{\alpha}(T)=-\frac{1}{4} \boldsymbol{\Xi}_{\alpha}^{-1}(T)$, $\boldsymbol{v}_{\alpha}(T)=\frac{1}{2} \boldsymbol{\Xi}_{\alpha}^{-1}(T) \boldsymbol{\xi}_{\alpha}(T)$ and $Y_{\alpha}(T)=-\frac{1}{2}\left\langle\boldsymbol{v}_{\alpha}(T), \boldsymbol{\xi}_{\alpha}(T)\right\rangle+X_{\alpha}(T)$.

As an interpolation function for driving forces, a formulation introduced by Moelans in [18] of the form $h_{\alpha}(\boldsymbol{\phi})=\phi_{\alpha}^{2}\left(\sum_{\beta=1}^{N} \phi_{\beta}^{2}\right)^{-1}$ is applied. For the minimization of the grand potential functional (1), we use a variational derivative to obtain the evolution equation

$$
\begin{aligned}
& \tau_{\alpha} \epsilon \frac{\partial \phi_{\alpha}}{\partial t} \\
& \quad=-\epsilon T \underbrace{\left(\frac{\partial a(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})}{\partial \phi_{\alpha}}+\nabla \cdot \frac{\partial a(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})}{\partial \nabla \phi_{\alpha}}\right)-\frac{1}{\epsilon} T \frac{\partial \omega(\boldsymbol{\phi})}{\partial \phi_{\alpha}}-\frac{\partial \psi(\boldsymbol{\phi}, \boldsymbol{\mu}, T)}{\partial \phi_{\alpha}}}_{=: r h s_{\alpha}}+\lambda
\end{aligned}
$$

of Allen-Cahn type, with $\tau_{\alpha}$ as a kinetic coefficient and the Lagrange multiplier $\lambda=\frac{1}{N} \sum_{\alpha=1}^{N} r h s_{\alpha}$ to ensure the constraint $\sum_{\alpha}^{N} \phi_{\alpha}=1$ from the simplex. The kinetic coefficient $\tau_{\alpha}$ is defined as $\tau_{\alpha}=\sum_{\substack{\beta=1 \\(\alpha<\beta)}}^{N} \tau_{\alpha \beta} \phi_{\alpha} \phi_{\beta}$ where $\tau_{\alpha \beta}$ is related to the inverse of the mobilities in the binary interface. To solve the evolution equation, finite differences and an explicit Euler-scheme for the time discretization are used.

### 2.3. The concentration model

The driving force (5) does not only depend on the order parameter, but also on the chemical potential and the temperature. First, we want to address the evolution of the chemical potentials, starting from the mass diffusion equation

$$
\begin{aligned}
\frac{\partial \boldsymbol{c}}{\partial t} & =\left(\frac{\partial \boldsymbol{c}}{\partial \boldsymbol{\mu}}\right)_{T, \boldsymbol{\phi}} \frac{\partial \boldsymbol{\mu}}{\partial t}+\left(\frac{\partial \boldsymbol{c}}{\partial \boldsymbol{\phi}}\right)_{T, \boldsymbol{\mu}} \frac{\partial \boldsymbol{\phi}}{\partial t}+\left(\frac{\partial \boldsymbol{c}}{\partial T}\right)_{\boldsymbol{\mu}, \boldsymbol{\phi}} \frac{\partial T}{\partial t} \\
& =\nabla \cdot(\boldsymbol{M}(\boldsymbol{\phi}, T) \nabla \boldsymbol{\mu}).
\end{aligned}
\tag{6}
$$

Using the chemical potentials for the driving force, we directly solve for the time derivative of the chemical potential from (6) and obtain the evolution equation:

$$
\begin{aligned}
\frac{\partial \boldsymbol{\mu}}{\partial t}= & {\left[\left(\frac{\partial \boldsymbol{c}}{\partial \boldsymbol{\mu}}\right)_{T, \boldsymbol{\phi}}\right]^{-1}\left(\nabla \cdot(\boldsymbol{M}(\boldsymbol{\phi}, T) \nabla \boldsymbol{\mu})-\left(\frac{\partial \boldsymbol{c}}{\partial \boldsymbol{\phi}}\right)_{T, \boldsymbol{\mu}} \frac{\partial \boldsymbol{\phi}}{\partial t}\right.} \\
& \left.-\left(\frac{\partial \boldsymbol{c}}{\partial T}\right)_{\boldsymbol{\mu}, \boldsymbol{\phi}} \frac{\partial T}{\partial t}\right).
\end{aligned}
\tag{7}
$$

The concentration is defined as the sum of the specific concentration for each order parameter $\boldsymbol{c}(\boldsymbol{\phi}, \boldsymbol{\mu}, T)=\sum_{\alpha=1}^{N} \boldsymbol{c}_{\alpha}(\boldsymbol{\mu}, T) h_{\alpha}(\boldsymbol{\phi})$ which can be derived from the parabolic free energies. As the fluxes in the interface of the phase-fields differ from the sharp interface limit, we need to introduce an additional "anti-trapping-current" $\boldsymbol{J}_{a t}$ into (7) which is derived in [15,16]. The "anti-trapping-current" is defined as

$$
\begin{aligned}
\boldsymbol{J}_{a t}= & \frac{\pi \epsilon}{4} \sum_{\substack{\alpha=1 \\(\alpha \neq l)}}^{N} \frac{g_{\alpha}(\boldsymbol{\phi}) h_{l}(\boldsymbol{\phi})}{\sqrt{\phi_{\alpha} \phi_{l}}} \frac{\partial \phi_{\alpha}}{\partial t}\left(\frac{\nabla \phi_{\alpha}}{\left|\nabla \phi_{\alpha}\right|} \cdot \frac{\nabla \phi_{\ell}}{\left|\nabla \phi_{\ell}\right|}\right) \\
& \left(\left(\boldsymbol{c}^{l}(\boldsymbol{\mu})-\boldsymbol{c}^{\alpha}(\boldsymbol{\mu})\right) \otimes \frac{\nabla \phi_{\alpha}}{\left|\nabla \phi_{\alpha}\right|}\right)
\end{aligned}
\tag{8}
$$

with the liquid phase $\phi_{l}$. Starting with (7) and the consideration above, the evolution equation of the chemical potentials can be written as:

$$
\begin{aligned}
\frac{\partial \boldsymbol{\mu}}{\partial t}= & {\left[\sum_{\alpha=1}^{N} h_{\alpha}(\boldsymbol{\phi})\left(\frac{\partial \boldsymbol{c}^{\alpha}(\boldsymbol{\mu}, T)}{\partial \boldsymbol{\mu}}\right)\right]^{-1} } \\
& -\left(\nabla \cdot(\boldsymbol{M}(\boldsymbol{\phi}, \boldsymbol{\mu}, T) \nabla \boldsymbol{\mu}-\boldsymbol{J}_{a t}(\boldsymbol{\phi}, \boldsymbol{\mu}, T))\right) \\
& -\sum_{\alpha=1}^{N} \boldsymbol{c}_{\alpha}(\boldsymbol{\mu}, T) \frac{\partial h_{\alpha}(\boldsymbol{\phi})}{\partial t}-\sum_{\alpha=1}^{N} h_{\alpha}(\boldsymbol{\phi})\left(\frac{\partial \boldsymbol{c}_{\alpha}(\boldsymbol{\mu}, T)}{\partial T}\right) \frac{\partial T}{\partial t}
\end{aligned}.
\tag{9}
$$

The first part of (9) can be interpreted as the susceptibility. The flux of $\boldsymbol{\mu}$ depends on the mobility as well as the "anti-trapping-current" correction term. The last two parts describe the change of the potential depending on the phase-fields and the temperature, respectively. These last

terms can be derived from the parabolic free energies. The mobility is defined as $\boldsymbol{M}(\boldsymbol{\phi}, \boldsymbol{\mu}, T)=\sum_{\alpha=1}^{N} \boldsymbol{D}_{\alpha} \frac{\partial c_{\alpha}(\boldsymbol{\mu}, T)}{\partial \boldsymbol{\mu}} g_{\alpha}(\boldsymbol{\phi})$ with $\boldsymbol{D}_{\alpha}$ as the diffusion matrix and $g_{\alpha}$ as the interpolation function which can be the same as $h_{\alpha}$.

### 2.4. Analytical temperature gradient

The diffusion coefficient for the temperature is much larger than the mass diffusion coefficient. Therefore, we assume that the temperature gradient for the setting of directional solidification can be calculated analytically. This is an usual approach for the directional solidification, called the "frozen temperature approximation" [19]. The temperature depends on the gradient $G$ and the velocity $v$ at a given time $t$ and position $x$ in the growing direction, as $T(x, t)=T_{0}+G(x-v t)$. $T_{0}$ is the temperature in the solid, which is below the melting point (temperature $T_{E}$ ) at the eutectic concentration $E_{c a l}$.

### 3. Walberla framework

The phase-field method described above is implemented in the waLBerla software package [20]. Starting as a framework for massively-parallel simulations using the Lattice Boltzmann method, it evolved over the years into a general framework for implementing parallel algorithms on block-structured grids that scale on various kinds of large HPC clusters [21-23]. Therefore, it offers datastructures and algorithms for load balancing, efficient input and output of simulation data as well as helper functions to implement stencil based schemes. waLBerla has two primary design goals: being efficient and scalable on current supercomputers, while at the same time being flexible and modular enough to support a wide range of applications. This modularity made it possible to implement a phase-field type model using the framework. The phase-field module contains highly optimized numerical kernels and uses the vector registers, to compute the evolution of the phase and concentration field. We make use of a 3D domain partitioning into blocks, which are distributed to processes depending on their computational load. This techniques are crucial to simulate the required domain size up to $2420 \times 2420 \times 1474$ cells.

### 4. Simulation setting

In order to study directional solidification of a melt in experiments $[9,10,24]$, an imposed temperature gradient can be used to control the solidification direction and the velocity. For the simulations, a setting (Fig. 2) related to the experimental conditions, with a solidification front growing in one direction, is applied. The front is driven by an analytical temperature gradient with a predefined velocity and slope.

To create the initial conditions, the nuclei are set as a random distribution through a Voronoi tessellation in the lower part of the simulation domain. The ratio of the phases for the Voronoi tessellation is based on the fractions given by the phase diagram of the system. At the solidified end of the domain, a Neumann boundary condition is used, because the diffusion coefficient in the solid is several orders of magnitude lower than in the liquid and hence the phase transition is neglected. On the liquid side, a Dirichlet boundary condition is used to model an infinite reservoir of melt. For the boundaries perpendicular to the solidification front, periodic boundary conditions are imposed to model a representative volume element. With respect to the defined solidification direction, the infinite flux of mass and neglecting the evolution of the solid phases, only the region around the solidification front needs to be simulated. This is achieved by a moving window technique [25], which is controlled by the solidification front height. The moving window technique enables us to simulate only the region around the moving interface so that we can resolve that region of interest with a very high resolution.

![](./images/814630062115520513_5.jpg)

Fig. 2. Simulation setting for the directional solidification of a ternary eutectic system including the boundary conditions. Below, the analytical temperature gradient $G$ with the velocity $v$ and its direction is shown.

The simulations were conducted with up to 84700 cores on the cluster systems Hermit and Hornet at the High Performance Computing Center Stuttgart (HLRS) [26]. Domain sizes with up to $2420 \times 2420 \times 1474$ cells were used.

### 5. Simulation parameters

In this part we describe the physical and numerical parameters of the simulations, including the different physical parameters used to model a eutectic microstructure with the phase fractions it has when solidifying, and with the phase fractions reported in the literature. This difference results from the considered temperatures of the solid as well as the solidification process. These two points are shown in the liquidus projection in Fig. 1 and described in the following.

#### 5.1. Calphad predicted parameters

The ternary eutectic point for the system $\mathrm{Ag}-\mathrm{Al}-\mathrm{Cu}$ is located at the mole fraction of $0.18 \mathrm{Ag}, 0.69 \mathrm{Al}$ and 0.13 $\mathrm{Cu}$ and at the temperature of $773.6 \mathrm{~K}$ (Fig. 1). Directly below this point, the solubility of $\mathrm{Ag}$ decreases in the order of $9 \%$ points over $20 \mathrm{~K}$ in the $\mathrm{Al}$ phase, which leads to different phase fractions $[10,11,9]$. The Calphad database describes the equilibrium concentrations and phase fractions at the ternary eutectic point as defined by the Calphad database and Witusiewicz et al. [7,8]. To preserve these phase fractions, subsequent quenching of the samples after solidification is modeled in our simulations. Quenching experiments are reported for this system

<table>
<caption>Table 1. Summary of the common parameters used in both settings.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Simulation value</th>
<th>Physical value</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><i>Numerical parameters</i></td>
</tr>
<tr>
<td>dx</td>
<td>1.0</td>
<td>$3.89*10^{-7}$ m</td>
</tr>
<tr>
<td>dt</td>
<td>0.032</td>
<td>$3.2*10^{-7}$ s</td>
</tr>
<tr>
<td>$\tau$</td>
<td>phase
$\begin{array}{c c c c}
\alpha & \beta & \gamma & liquid \\
\alpha \\
\beta \\
\gamma \\
liquid
\end{array}
\left[\begin{array}{c c c c}
- & 1.68 & 1.18 & 1.26 \\
1.68 & - & 0.29 & 0.58 \\
1.18 & 0.29 & - & 1.06 \\
1.26 & 0.58 & 1.06 & -
\end{array}\right]$</td>
<td>based on [17]</td>
</tr>
<tr>
<td>$\epsilon$</td>
<td>4.0</td>
<td>$1.56*10^{-6}$ m</td>
</tr>
<tr>
<td colspan="3"><i>Physical parameters</i></td>
</tr>
<tr>
<td>$\gamma$</td>
<td>phase
$\begin{array}{c c c c}
Al & Ag_2Al & Al_2Cu & liquid \\
Al \\
Ag_2Al \\
Al_2Cu \\
liquid
\end{array}
\left[\begin{array}{c c c c}
- & 0.6 & 0.4 & 0.2 \\
0.6 & - & 0.4 & 0.4 \\
0.4 & 0.4 & - & 0.4 \\
0.2 & 0.4 & 0.4 & -
\end{array}\right]$</td>
<td>Scaling factor for physical values: $0.175\frac{J}{m^2}$, based on [27–30]</td>
</tr>
<tr>
<td>D</td>
<td>5.0</td>
<td>$2.4*10^{-8}\frac{m^2}{s}$</td>
</tr>
<tr>
<td colspan="3"><i>Parabolic free energies of the solids</i></td>
</tr>
<tr>
<td>$\boldsymbol{\Xi}_\alpha, \boldsymbol{\xi}_\alpha, X_\alpha$</td>
<td>$\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$, $\begin{bmatrix} -2.25 \\ -3.486 \end{bmatrix}$, $1.561866$</td>
<td>Based on [7,8]</td>
</tr>
<tr>
<td>$\boldsymbol{\Xi}_\beta, \boldsymbol{\xi}_\beta, X_\beta$</td>
<td>$\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$, $\begin{bmatrix} -3.104 \\ -2.710 \end{bmatrix}$, $1.427846$</td>
<td>Based on [7,8]</td>
</tr>
<tr>
<td>$\boldsymbol{\Xi}_\gamma, \boldsymbol{\xi}_\gamma, X_\gamma$</td>
<td>$\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$, $\begin{bmatrix} -1.395 \\ -2.709 \end{bmatrix}$, $0.9176$</td>
<td>Based on [7,8]</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2. Summary of the parameters used in the CAL and the EXP setting.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Simulation value</th>
<th>Physical value resp. source</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><i>Parameters only used in the CAL setting</i></td>
</tr>
<tr>
<td>$\mathbf{c}_{liquid}$</td>
<td>0.18, 0.69, 0.13 (Ag, Al, Cu)</td>
<td>0.18, 0.69, 0.13 mol-% (Ag, Al, Cu)</td>
</tr>
<tr>
<td>Phase fractions</td>
<td>0.54, 0.3, 0.16</td>
<td>0.54, 0.3, 0.16</td>
</tr>
<tr>
<td>$\boldsymbol{\Xi}_{liq}, \boldsymbol{\xi}_{liq}, X_{liq}$</td>
<td>$\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$, $\begin{bmatrix} -2.140 \\ -3.140 \end{bmatrix}$, $3.9532-2.\bar{6}T$</td>
<td>Based on [7,8]</td>
</tr>
<tr>
<td colspan="3"><i>Parameters only used in the EXP setting</i></td>
</tr>
<tr>
<td>$\mathbf{c}_{liquid}$</td>
<td>0.237, 0.622, 0.141 (Ag, Al, Cu)</td>
<td>0.237, 0.622, 0.141 mol-% (Ag, Al, Cu)</td>
</tr>
<tr>
<td>Phase fractions</td>
<td>0.334, 0.309, 0.355</td>
<td>0.334, 0.309, 0.355</td>
</tr>
<tr>
<td>$\boldsymbol{\Xi}_{liq}, \boldsymbol{\xi}_{liq}, X_{liq}$</td>
<td>$\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$, $\begin{bmatrix} -2.220 \\ -2.980 \end{bmatrix}$, $3.8655-2.\bar{6}T$</td>
<td>Based on [7,8]</td>
</tr>
</tbody>
</table>

[9,24], but no micrographs are included in the publications. The values of the setting CAL (Tables 1 and 2) describe the thermodynamic state at the eutectic temperature. This state exists experimentally for only a short time after the solidification in a short distance behind the solid/liquid interface. Due to the quenching, all solubility changes and change of the phase fractions are neglected. The slopes of the parabolic free energies are changed to achieve a higher time step width and faster coupled growth. The surface energies are derived from [27–30].

### 5.2. Experimentally predicted parameters

The EXP setting (Tables 1 and 2) was selected to mimic the phase fractions observed in experimental samples after solid state changed due to changing solubilities. These phase fractions are reported by several authors [4,9,24,10,11]. Using these low temperature phase fractions, the reported concentrations in the solid phases and neglecting the solubility change, an adjusted phase diagram can be calculated which shifts the ternary eutectic point to a new composition $E_{exp}$. The phase fractions are averaged from the experiments and the concentration for $\boldsymbol{c}_{liquid}$ is calculated from this new point.

## 6. Results

This section describes the influence of each parameter set on the pattern formation of the ternary eutectic microstructure. Quantitative analysis is carried out on cross section of each structure using nearest neighbor statistics. The nearest neighbor statistics of the simulations based on the setting EXP are compared to an experimental micrograph. For the cross sections from the simulations, the phases are colored to match the micrograph, such that Al is black, $Al_2Cu$ is gray and $Ag_2Al$ is white. To increase the contrast, the 3D figures from the simulations show Al as red, $Al_2Cu$ as blue and $Ag_2Al$ as green. All results are shown in a state of equilibrium, where the velocity of the solidification front is constant.

The model was validated by comparing it to the analytical Jackson Hunt approach [31] using 2D domains. This was done by comparing the undercooling calculated from the velocity of the temperature gradient and the periodic length. In addition, we conducted convergence studies for the growth velocity, based on the interface thickness, related to $\varepsilon$ [17]. Both approaches show a good agreement with the simulation results.

A micrograph for the system Ag-Al-Cu from A. Dennstedt is shown in Fig. 4. In this micrograph a so-called chained brick-like structure is shown, with a strong association between the $Al_2Cu$ and $Ag_2Al$ phases. Multiple types of features, Fig. 4(a)-(f), can be found in the image. The features in (a), (d) and (f) show bricks with convex and concave $Ag_2Al$ links. In (b) the chains branch, in (c) a ring-like structure is shown and (e) contains a short chain. In (d) an irregularity can be seen in the bricks.

### 6.1. Results from the experimentally derived data set EXP

To study the data set EXP, two simulations with total domain sizes of $800 \times 800 \times 4256$ and $2420 \times 2420 \times 1474$ cells were conducted. The simulation with the domain sizes of $800 \times 800 \times 4256$ run on 13,600 cores in 16 h at the Hermit cluster. The other simulation was conducted on 84700 in 7 h at the Hornet. Figs. 3(a) and 4 show cross-sections through the solid, close to solidification front at the end of the simulation. Compared to the experimental micrograph, the basic features are reproduced with the phase-field model and the parameters used. In order to see the arrangement of the phases in 3D, the two final structures are shown in Figs. 3(b) and 5. The two phases $Al_2Cu$ and $Ag_2Al$ are exempted separately.

In the simulations, patterns formed which appeared as the chained brick-like structures in the cross section. Six distinct features can be found, comparable to the structures in the micrograph. The order of the displayed features of the simulation in Fig. 4(A)-(F), is the same as in the micrograph (a)-(f). Besides the overall good agreement, some differences in the characteristics are evident. The relative number of separated chains in the simulations is higher. The average phase at the tail of the chains in the simulations differs from the micrograph. This results in a different ordering of the phases in the display details (E). The width of the chains varies, in contrast to the experimental micrograph, where it is nearly constant. Despite similar phase fractions of the $Al_2Cu$ and $Ag_2Al$ phases, the width of the chain links differs approximately by a factor of two. The high aspect ratio of these phases in the simulated structure gives them a quasi-lamellar appearance. Like in the micrograph, most of the interfaces from $Ag_2Al$ to $Al_2Cu$ are concave (see details Fig. 4(a) and (A)). Depending on the $Al_2Cu$ and $Ag_2Al$ interface length in the simulations, Fig. 4(F), as well as in the experiment (f), the sign of the curvature differs along the interface. The interface between $Ag_2Al$ and $Al$ bulges into the matrix phase. This effect is more distinct in the simulations than in the experiment.

In addition to the patterns in the cross sections, further information on the microstructure evolution can be obtained by studying how individual phases change with growth distance. Fig. 3(b) is divided in three parts. In the back all solid phases are illustrated. In the front ($Ag_2Al$) and at the top ($Al_2Cu$) some lamellae of the phases are exempted. This is done to highlight details of the 3D microstructures and the development of the initial Voronoi filling to the steady state. During the regular coupled growth process, multiple splitting events, overgrowth of lamellae and merging can be observed in the simulations. These events can be seen in the side view of the exempted lamellae in Fig. 3(c) and (d). From the exempted structures, the steady state growth at the end of the simulation is obvious.

To compare the simulated cross-sections with experiments, quantitative nearest neighbor statistics are used. The nearest neighbor statistics for both base sizes of the

![](./images/814630062115520513_6.jpg)
(a) cross section

![](./images/814630062115520513_7.jpg)
(b) total structure in 3D

![](./images/814630062115520513_8.jpg)
(c) $Ag_2Al$ lamellae in 3D

![](./images/814630062115520513_9.jpg)
(d) $Al_2Cu$ lamellae in 3D

Fig. 3. Simulation result with $800^2$ cells base size and the dataset EXP. (a) shows a cross-section below the solidification front at the end of the simulation and (b) shows the solid phases in 3D at the end of the process. On the left and top, the $Al_2Cu$ as well as the $Ag_2Al$ phase are exempted. In (c) and (d) the exemptions are depicted from the side to show the split and merge events during the coupled growth.

![](./images/814630062115520513_10.jpg)

Fig. 4. Experimental micrograph (top) and simulation (bottom) of directionally solidified Ag-Al-Cu ternary eutectic where Al is black, Al₂Cu is gray and Ag₂Al is white. Both micrographs show chained brick-like structure, also called cobblestone structure. The velocity of the temperature gradient (2.2 K/mm) in this experiment was 0.08 µm/s.

![](./images/814630062115520513_11.jpg)

Fig. 5. Simulation result with the 2420² cells base size and the dataset EXP. The figure shows the all solid phases at the end of the solidification process. In the left (Ag₂Al) and in the right (Al₂Cu) the phases are exempted.

setting EXP are presented in Fig. 6, along with the same values taken from the experimental structure. The statistics indicates fairly good agreement among number of neighbors for the phases Ag₂Al and Al₂Cu. Due to a nearly continuous matrix phase Al, the number of Al regions around Ag₂Al and Al₂Cu is mostly one; this parameter is therefore not reported. In all data sets, the graphs indicate a predominance of phases with two nearest neighbors, as expected for such a chain-like structure. The graphs in Fig. 6 show
a noticeable difference between the behavior of the structures related to branching and chain termination. For these statistics, a single neighbor can be interpreted as a tail of a chain, while more than two neighbors indicate branching of a chain. The peaks at two neighbors are higher for the experiments than for the simulations, indicating slightly more regularity and continuity of the chains in the experimental structure. The branching is observed in the experimental structure more often at a Ag₂Al, while the

![](./images/814630062115520513_12.jpg)

(a) nearest neighbors of $Ag_2Al$

![](./images/814630062115520513_13.jpg)

(b) nearest neighbors of $Al_2Cu$

Fig. 6. Nearest-neighbors statistics for the phases $Ag_2Al$ and $Al_2Cu$ for both simulations of the EXP dataset compared to the experimental structure.

![](./images/814630062115520513_14.jpg)

(a) cross-section

![](./images/814630062115520513_15.jpg)

(b) total structure in 3D

![](./images/814630062115520513_16.jpg)

(c) $Ag_2Al$ lamellae in 3D

![](./images/814630062115520513_17.jpg)

(d) $Al_2Cu$ lamellae in 3D

Fig. 7. Simulation result with a base size of $800^2$ cells and the data set CAL. (a) shows a cross section below the solidification front at the end of the simulation and (b) shows the all solid phases at the end of the process. On the left and at the top, the $Al_2Cu$ phase as well as the $Ag_2Al$ phase are exempted. In (c) and (d) the exemptions are depicted from the side to show the split events during regular coupled growth of the lamellae.

branching in the simulated structures occurs almost exclu- sively from the $Al_2Cu$ phase. For the experiment, most of the chain tails consist of the phase $Al_2Cu$ (Fig. 6(b)), whereas in the simulations, the chains end mostly in the phase $Ag_2Al$ (Fig. 6(a)). Overall, the number of tails in the simulations is significantly higher, corresponding to shorter chains in the cross-sections. The non-zero value of nearest neighbors equal to four in Fig. 6(b) also indicates more complex branching in the simulations, resulting in a higher variance of neighbors, compared to the experiment.

### 6.2. Comparison of the database-derived dataset CAL with the dataset EXP

A simulation using the dataset CAL with a domain size of $800 × 800 × 3930$ cells is shown in Fig. 7. The simulation runs on 13,600 cores in 6 h at the Hornet cluster. The dif- ference in composition results in a significantly different pattern development. Instead of continuous chains, multi- ple independent clusters of the two phases form, appearing as islands engulfed in a continuous Al-matrix. The arrangements are related to paw and brick-like structures. The fibers of the $Ag_2Al$ and the $Al_2Cu$ phase are more rounded, instead of elongated.

The maximum number of "links" observed in any chain in this simulation is seven. For the CAL dataset, there are some instances where the $Ag_2Al$-phase is surrounded partly or completely by the $Al_2Cu$-phase instead of the matrix. This is also observed in experiments [32]. The fibers of the $Ag_2Al$ and the $Al_2Cu$ phase are also more rounded, instead of elongated into a quasi-lamellar arrangement as seen in EXP. Another difference, noticeable in Fig. 7(b), is that the arrangement of the patterns continues to change over the entire length of the simulation. This is despite the fact that the simulation has ostensibly reached steady state, as indicated by the constant volume fractions and constant growth velocity.

Similar to the microstructure evolution in the setting EXP, splitting and overgrowth can be observed in the exempted lamellae in Fig. 7(c) and (d).

The nearest neighbor statistic in Fig. 8 counts the mutual number of neighbors for the phases $Al_2Cu$ and

![](./images/814630062115520513_18.jpg)

(a) nearest neighbors of Ag₂Al

![](./images/814630062115520513_19.jpg)

(b) nearest neighbors of Al₂Cu

Fig. 8. Nearest-neighbors statistics for the CAL and EXP dataset for the phases Ag₂Al and Al₂Cu with respect to each other.

Ag₂Al. In these graphs, the simulations of dataset CAL and EXP with equal base size are compared. As in the former section, the statistics of the Al-phase are neglected. The interpretation of the statistics is ambiguous, due to the var- ious patterns which appear in the CAL dataset. The number of neighbors is not directly related to any pattern, e.g., a single neighbor can indicate an embedded phase as well as the end of a chain. The number of neighbors around Al₂Cu (Fig. 8(b)) has its maximum at two neighbors, but the peak is not as distinct as for the EXP set, with a large number of regions also having one or three neighbors. For the number of neighbors around Ag₂Al (Fig. 7(a)) the peak of the dataset CAL is at one and for EXP it is at two neighbors.

### 7. Discussion

With the model presented here, we have shown that it is possible to simulate the directional solidification of ternary eutectic microstructures in three dimensions. The growth velocity of $79.35\ \mu$m/s in both simulations was higher than in the experiments ($0.08$–$6.0\ \mu$m/s), to increase the effective growth height. Despite that, there is a good visual accor- dance of the simulations to the experimental micrographs, and the length scale of the observed features is in the same range. This is due to the small Peclet numbers (experiment: $6.2\cdot 10^{-4}$, simulation: $8.2\cdot 10^{-2}$) where the diffusion is much larger than the advection and the scaled surface ener- gies to get the same ratio between driving forces through undercooling and surface energies like in the experiments.

Although there is qualitative agreement between experi- ment and the simulated EXP structure, a number of differ- ences are noted. In the simulation, the width of the lamellae fluctuates along the chains and the shape of the chain links differs. One possible reason could be that the state of the simulation is still changing. However, due to the constant phase fractions and a comparison of cross sections at a late state of the simulation, we rule out this possibility. Therefore, we assume that the differences are caused by dif- ferences in the surface energies. The surface energies for the considered temperature range are difficult to measure and have not been reported for all interfaces in this system. We propose to investigate the influence of this parameter in further studies. There is also a deviation between the experimental and simulated structure in the nearest neigh- bor statistics related to the specific patterns that form. It should be noted that the experimental microstructure shown in Fig. 4 is only one of many patterns which have been observed experimentally [9–11]. It appears that the factors influencing pattern formation are complex and sen- sitive, as different patterns have been found even in a single sample processed under uniform conditions. In the future, additional methods will be used to further quantify the dif- ference between micrographs and simulations, including e.g., 3D graph representation or principal component analysis.

There are particularly marked differences between the simulated patterns for the EXP and the CAL data sets. Most notably, the length of the Ag₂Al/Al₂Cu chains is shorter and sometimes the Ag₂Al phase is embedded in the Al₂Cu phase for the dataset CAL. The variance in the patterns of the two datasets is resulting from the different phase fractions. The $Al$ fraction is larger for the dataset CAL, which results in a more pronounced matrix phase. A larger matrix phase can appear in a wider interval between the chains or in shorter chains which is observed in our simulations. Although no comparable experimental results for the CAL simulations have been published, the authors are working with experimentalists to obtain micro- graphs of the ternary eutectic structure directly behind a quenched interface for comparison. In addition, future work will focus on relaxing the assumption of no solid state diffusion in order to simulate the total cooling path, although this will require significantly larger computational effort. Justified by the good visual accordance between the EXP simulations and the micrograph, we propose phase- field simulations as a method to predict high temperature patterns of the system Ag–Al–Cu.

Some of the two and three fiber patterns in the CAL data set started to rotate in an intertwined way. No stable spiral growth could be observed in the presented simulations, but further investigations will be carried out on this topic, as this growth pattern was observed experimentally [9].

### 8. Conclusion

In the current work, we presented simulations of direc- tional solidification of the ternary eutectic system Ag–Al– Cu at the three phase invariant point. For this, we applied the phase-field method, based on a Grand-Potential approach. Using state of the art supercomputing allows us the study of realistic domain sizes, in which multiple fea- tures could be observed, similar to the experiments.

Two different datasets were under consideration. The first parameter set (EXP) was derived from experimental micrographs [10,11,9], and used the phase fractions found

after some amount of solid state diffusion driven by solubil-
ity changes. The second set (CAL) was compiled from ther-
modynamic Calphad data [7,8] and corresponds to the
compositions and phase fractions expected at the ternary
eutectic temperature.

Our primary conclusions are as follows:

A good visual agreement of the EXP simulations with
the micrographs was achieved. Similarly chained brick-like
structures were observed in cross-sections of both
structures.

The differences in the simulated patterns are due to the
difference in the composition. In contrast to the long
strands of chains for the EXP dataset, short chains and
islands appeared in the cross-sections of the CAL data set.

All simulations reached a steady state, as defined by con-
stant phase fractions, but only the EXP simulations pro-
duced stable patterns. We assume that the non-stationary
steady state is a prerequisite for the spiral growth observed
in experiments [9]. The study of this special morphology is a
topic for further investigations.

Large three-dimensional simulations allow to study the
continuous patterns of the evolving microstructure.
Therefore, it is possible to investigate additional correla-
tions, depending on the parameters, and to visualize the
occurring microstructures. In order to quantify the influ-
ence of certain parameters, it will be useful to improve
the applied statistics with additional methods of
characterization.

## Acknowledgements

We thank Sebastian Schulz, Marco Berghoff, Michael Selzer,
Michael Kellner and Oleg Tschukin for the fruitful discussions
and support. We also thank the High Performance Computing
Center Stuttgart (HLRS) for provision of supercomputing time
and access to special purpose queues at the systems Hermit and
Hornet. PS and AD thank for financial support through the
German Research Foundation within the project NE 822/14-2.
JH, MJ and BN acknowledge the funding of the cooperative grad-
uate school "Gefügeanalyse und Prozessbewertung" by the min-
istry of Baden-Wuerttemberg.

## References

[1] S. Kang, D.-Y. Shih, D. Leonard, D. Henderson, T. Gosselin,
S.-I. Cho, J. Yu, W. Choi, Controlling $Ag_{3}Sn$ plate formation
in near-ternary-eutectic Sn-Ag-Cu solder by minor Zn
alloying, JOM 56 (2004) 34-38.

[2] M.A. Ruggiero, J.W. Rutter, Origin of microstructure in the
332 K eutectic of the Bi-In-Sn system, Mater. Sci. Tech. 13
(1997) 5-11.

[3] D. Lewis, S. Allen, M. Notis, A. Scotch, Determination of the
eutectic structure in the Ag-Cu-Sn system, J. Electron.
Mater. 31 (2002) 161-167.

[4] D. Cooksey, A. Hellawell, The microstructures of ternary
eutectic alloys in the systems Cd-Sn-(Pb, In, Tl), Al-Cu-(Mg,
Zn, Ag) and Zn-Sn-Pb, J. Inst. Met. 95 (1967) 183-187.

[5] D. McCartney, R. Jordan, J. Hunt, The structures expected in
a simple ternary eutectic system: part II. The Al-Ag-Cu
ternary system, Metall. Trans. A 11 (1980) 1251-1257.

[6] U. Hecht, L. Gránásy, T. Pusztai, B. Böttger, M. Apel, V.
Witusiewicz, L. Ratke, J. De Wilde, L. Froyen, D. Camel,
et al., Multiphase solidification in multicomponent alloys,
Mater. Sci. Eng.: R: Rep. 46 (2004) 1-49.

[7] V. Witusiewicz, U. Hecht, S. Fries, S. Rex, The Ag-Al-Cu
system: part I: reassessment of the constituent binaries on the
basis of new experimental data, J. Alloys Compd. 385 (2004)
133-143.

[8] V. Witusiewicz, U. Hecht, S. Fries, S. Rex, The Ag-Al-Cu
system: part II: a thermodynamic evaluation of the ternary
system, J. Alloys Compd. 387 (2005) 217-227.

[9] A. Genau, L. Ratke, Morphological characterization of the
Al-Ag-Cu ternary eutectic, Int. J. Mater. Res. 103 (2012)
469-475.

[10] A. Dennstedt, L. Ratke, Microstructures of directionally
solidified Al-Ag-Cu ternary eutectics, Trans. Indian Inst.
Met. 65 (2012) 777-782.

[11] A. Dennstedt, L. Ratke, A. Choudhury, B. Nestler, New
metallographic method for estimation of ordering and lattice
parameter in ternary eutectic systems, Metall. Microstruct.
Anal. 2 (2013) 140-147.

[12] B. Nestler, A. Choudhury, Phase-field modeling of multi-
component systems, Curr. Opin. Solid State Mater. Sci. 15
(2011) 93-105.

[13] N. Moelans, B. Blanpain, P. Wollants, An introduction to
phase-field modeling of microstructure evolution, Calphad 32
(2008) 268-294.

[14] B. Nestler, H. Garcke, B. Stinner, Multicomponent alloy
solidification: phase-field modeling and simulations, Phys.
Rev. E 71 (2005) 041609.

[15] M. Plapp, Unified derivation of phase-field models for alloy
solidification from a grand-potential functional, Phys. Rev. E
84 (2011) 031601.

[16] A. Choudhury, B. Nestler, Grand-potential formulation for
multicomponent phase transformations combined with thin-
interface asymptotics of the double-obstacle potential, Phys.
Rev. E 85 (2012) 021602.

[17] A. Choudhury, Quantitative phase-field model for phase
transformations in multi-component alloys (Schriftenreihe
des Instituts für Angewandte Materialien Karlsruher Institut
fuer Technologie), KIT Scientific Publishing, 2013.

[18] N. Moelans, A quantitative and thermodynamically consis-
tent phase-field interpolation function for multi-phase sys-
tems, Acta Mater. 59 (2011) 1077-1086.

[19] W.J. Boettinger, J.A. Warren, Simulation of the cell to plane
front transition during directional solidification at high
velocity, J. Cryst. Growth 200 (1999) 583-591.

[20] C. Feichtinger, S. Donath, H. Köstler, J. Götz, U. Rüde,
WaLBerla: HPC software design for computational engineer-
ing simulations, J. Comput. Sci. 2 (2011) 105-112.

[21] C. Godenschwager, F. Schornbaum, M. Bauer, H. Köstler,
U. Rüde, A framework for hybrid parallel flow simulations
with a trillion cells in complex geometries, in: Proceedings of
SC13: International Conference for High Performance
Computing, Networking, Storage and Analysis, ACM,
2013, p. 35.

[22] C. Feichtinger, J. Habich, H. Köstler, U. Rüde, T. Aoki,
Performance modeling and analysis of heterogeneous lattice
Boltzmann simulations on CPU-GPU clusters, Parallel
Comput. (2014).

[23] H. Köstler, C. Feichtinger, U. Rüde, T. Aoki, A geometric
multigrid solver on tsubame 2.0, in: Efficient Algorithms for
Global Optimization Methods in Computer Vision, Springer,
2014, pp. 155-173.

[24] U. Böyük, N. Marasli, H. Kaya, E. Cadirli, K. Keslioglu,
Directional solidification of Al-Cu-Ag alloy, Appl. Phys. A
95 (2009) 923-932.

[25] A. Vondrous, M. Selzer, J. Hötzer, B. Nestler, Parallel
computing for phase-field models, Int. J. High Perform.
Comput. Appl. 28 (2014) 61-72.

[26] A. Bode, T. Lippert, M.M. Resch, inside, 2014.

[27] A. Bulla, C. Carreno-Bodensiek, B. Pustal, R. Berger, A.
Bührig-Polaczek, A. Ludwig, Determination of the solid-
liquid interface energy in the Al-Cu-Ag system, Metall.
Mater. Trans. A 38 (2007) 1956-1964.

[28] R. Kirchheim, D.M. Herlach, Phase Transformations in
Multicomponent Melts, John Wiley & Sons, 2009.

[29] T. Himemiya, T. Umeda, Three-phase planar eutectic growth models for a ternary eutectic system, Materials Transactions- JIM 40 (1999) 665-674.

[30] K.B. Kim, J. Liu, N. Marasli, J.D. Hunt, The effect of different atomic volumes in the three phases during lamellar eutectic growth. A comparison of experiment and theory in the $Al-Al_2Cu$ system, Acta Metall. Mater. 43 (1995) 2143.

[31] K. Jackson, J. Hunt, Lamellar and rod eutectic growth, AIME Met. Soc. Trans. 236 (1966) 1129-1142.

[32] A. Dennstedt, A. Choudhury, L. Ratke, B. Nesler, Microstructures in a ternary eutectic alloy, 2014.