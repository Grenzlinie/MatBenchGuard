# Mesoscopic Multi-particle Collision Model for Fluid Flow and Molecular Dynamics

Anatoly Malevanets¹ and Raymond Kapral²

¹ Flow Software Technologies 3070 Jefferson Blvd., Windsor, ON N8T 3G9, Canada
² Chemical Physics Theory Group, Department of Chemistry, University of Toronto, Toronto, ON M5S 3H6, Canada

**Abstract.** Several aspects of modeling dynamics at the mesoscale level are discussed: (1) The construction of a mesoscopic description of fluid dynamics. The mesoscale dynamics consists of free streaming interrupted by multi-particle collisions. The multi-particle collisions are carried out by performing random rotations of particle velocities in predetermined cells in a manner that conserves mass, momentum and energy. The algorithmic implementation of the method is described and its theoretical basis is justified. Examples of simulation results on hydrodynamic flows are presented. (2) A hybrid molecular dynamics (MD)-Mesoscale Solvent model is described next. In this method full MD of solute particles is combined with the mesoscale dynamics of the surrounding fluid. The method is illustrated by considering the diffusive dynamics and hydrodynamic interactions among solute particles and clusters in the mesoscale solvent. (3) Finally, extensions of such schemes are outlined. In particular, generalizations to molecular solvents are presented and examples of solute dynamics in mesoscale water are given; also extensions to reactive flows are described.

## 1 Introduction

It is well known that the hydrodynamic equations of motion are a macroscopic manifestation of the microscopic conservation laws of mass, momentum and energy. This observation has prompted the construction of mesoscopic models whose dynamics may be simplistic in comparison to that of real fluids but which preserve these conservation laws and lead to the hydrodynamic equations on macroscopic distance and time scales. Perhaps the best known models of this class are lattice gas automata and lattice Boltzmann equations. Lattice gas automata for hydrodynamics often suffer from lattice artifacts that have limited their use, but they have proven their utility for the simulations of complex fluids or fluid flows in complex geometries [1,2]. Lattice Boltzmann methods [3] have been developed extensively and have been used to investigate a variety of problems ranging from hydrodynamic flows to fluid flows in complex geometries and complex systems [4–6].

In this chapter we discuss a particle-based mesoscopic model for the description of hydrodynamic fluid flow and solute molecular dynamics [7,8]. The fictitious particles of the model are not restricted to the sites of a lattice and thus particle positions and velocities can take on continuous values. The dynamics consists of free streaming interrupted by multi-particle collisions that change the particle velocities. Formally, the multi-particle collision dynamics is constructed as a superposition of propagators

A. Malevanets and R. Kapral, Mesoscopic Multi-particle Collision Model for Fluid Flow and Molecular Dynamics, Lect. Notes Phys. **640**, 116–149 (2004)
http://www.springerlink.com/
© Springer-Verlag Berlin Heidelberg 2004

corresponding to these processes which act in position-momentum space and conserve momenta, energy and phase space volume. As a result, one may demonstrate that the exact full set of hydrodynamic equations is obtained in the macroscopic limit. We focus our attention on two specific types of propagator: Free-streaming propagator, arising from integration of the equations of motion for non-interacting molecules, and collision propagator, exchanging momenta among particles in a collision cell. The model differs from lattice Boltzmann models in that it is not a discrete simulation of a Boltzmann equation for a single particle distribution function, rather, it is a mesoscopic molecular dynamics which possesses the stability properties of particle-based methods. It is akin to Direct Simulation Monte Carlo (DSMC) methods [9] with a more efficient multi-particle collision dynamics.

The model should prove especially useful for applications to the dynamics of complex fluids and complex systems. Because of its particle nature, a hybrid version of the model that combines mesoscopic multi-particle collision dynamics with full molecular dynamics of embedded molecules or particles is easily constructed. Detailed features of the intermolecular forces between the mesoscopic solvent particles and the solute molecules are naturally taken into account. This permits potential applications of the model to large biomolecule or polymer dynamics in solution or to the dynamics of colloidal suspensions. For these systems the fluctuations intrinsic in the mesoscopic particle dynamics are an advantageous feature. Consequently, the model should see applications to a number of problems in biophysics and the rheology of complex systems.

The outline of the chapter is as follows: In Sect. 2 we describe the construction of the model and outline some of its main properties. Section 3 demonstrates how the hydrodynamic equations of motion can be deduced from the dynamics by the application of projection operator methods. In this section discrete Green–Kubo expressions for the transport properties are derived. Some illustrations of the utility of the scheme for simulations of fluid flow are described in Sect. 4. The hybrid scheme for molecular dynamics in the mesoscopic solvent is formulated in Sect. 5 while applications are discussed in Sect. 6. The conclusions are given in Sect. 7.

## 2 Multi-particle Collision Model for Fluid Flow

A simplified version of molecular collision dynamics in a fluid that yields the correct hydrodynamic equations on long distance and time scales can be constructed in the following way. We adopt a mesoscopic view of the fluid which involves discrete time updating of continuous particle positions and velocities through both free streaming and collisions. The dynamics is constructed so that the conservation laws of mass, momentum and energy are satisfied, an essential feature in any dynamical scheme.

Consider a system comprising $N$ particles, each with mass $m$. $^{1}$ The particle positions and velocities are denoted by $\mathbf{X}^{(N)} = \{\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_N\}$ and $\mathbf{V}^{(N)} = \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_N\}$, respectively. The dynamics consists of free streaming,

$$
\mathbf{x}_i(t+\tau) = \mathbf{x}_i(t) + \mathbf{v}_i(t)\tau \, \tag{1}
$$

$^{1}$ The mesoscopic collision dynamics is easily generalized to systems where the particles have different masses.

![](./images/813331739265990657_1.jpg)

Fig. 1. Schematic representation of the division of a system into cells for the application of the multi-particle collision rule. The particle positions are continuous variables and are not confined to the cell centers. The velocities are also continuous and are denoted by lines in the figure

interspersed by multi-particle collisions at discrete time intervals $\tau$. The post-collision velocities after multi-particle collisions [10] are determined by first dividing the system into cells as shown schematically in Fig. 1. At each time interval rotation operators $\hat{\omega}_{\xi}$ are chosen at random from a set $\Omega$ of rotation operators and assigned to the cells. Let $\mathrm{V}_{\xi}$ be the center of mass velocity of the particles in cell $\xi$,

$$
\mathrm{V}_{\xi}=\frac{1}{n_{\xi}} \sum_{i | \mathbf{x} \in \mathcal{V}} \mathbf{v}_{i}^{\prime},
$$

where $n_{\xi}$ is the number of particles in the cell with volume $\mathcal{V}$ and $\mathbf{v}_{i}^{\prime}$ is the pre-collision value of the velocity. The post-collision velocity $\mathbf{v}_{i}$ of every particle $i$ in cell $\xi$ is given by

$$
\mathbf{v}_{i}=\mathrm{V}_{\xi}+\hat{\omega}_{\xi}\left(\mathbf{v}_{i}^{\prime}-\mathrm{V}_{\xi}\right). \tag{2}
$$

The same rotation operator is applied to every particle in the cell but it differs from cell to cell. This simple collision rule changes both the directions and magnitudes of the particle velocities in the cell as can be seen from the two-dimensional example for two particle velocities shown in Fig. 2. The collision rule conserves mass, momentum and energy within each cell. This can be seen by summing the post-collision momenta and energies in each cell. For the momentum and energy we have, respectively,

$$
\sum_{i | \mathbf{x} \in \mathcal{V}} m \mathbf{v}_{i} \quad=\sum_{i | \mathbf{x} \in \mathcal{V}} m\left(\mathrm{~V}+\hat{\omega}\left[\mathbf{v}_{i}^{\prime}-\mathrm{V}\right]\right)=\sum_{i | \mathbf{x} \in \mathcal{V}} m \mathbf{v}_{i}^{\prime}, \tag{3}
$$

$$
\sum_{i | \mathbf{x} \in \mathcal{V}} \frac{m}{2}\left\|\mathbf{v}_{i}\right\|^{2}=\sum_{i | \mathbf{x} \in \mathcal{V}} \frac{m}{2}\left\|\mathrm{~V}+\hat{\omega}\left[\mathbf{v}_{i}^{\prime}-\mathrm{V}\right]\right\|^{2}=\sum_{i | \mathbf{x} \in \mathcal{V}} \frac{m}{2}\left\|\mathbf{v}_{i}^{\prime}\right\|^{2}. \tag{4}
$$

In addition, one may show that the dynamics preserves phase space volumes [7].

As discussed above, in order to apply the multi-particle collision rule the system must be divided into cells where the collisions occur. The choice of cell size is dictated

![](./images/813331739265990657_2.jpg)

Fig. 2. Multi-particle collision rule applied to two particles in two dimensions for a rotation by $\pi/2$. The dark arrows labelled $v_1'$ and $v_2'$ denote the pre-collision velocities. The upper panel also shows the center of mass velocity and the pre-collision velocities relative to the center of mass before and after rotation by $\pi/2$. The lower panel shows the result of adding back the center of mass velocity to yield the post-collision velocities. Both the velocity directions and magnitudes are changed as a result of the collision

by the particle density and the mean velocity of the particles in the system. The particle density determines the mean number of particles per cell and thus affects the number of particles involved in a multi-particle collision event. The mean velocity determines, on average, how far particles travel between collision events. Multi-particle collisions will be efficient if large numbers of particles participate in each collision event. In order to avoid correlations between collisions, particles should travel on the order of a cell length between collisions. Consideration of these factors provides rough guides for the appropriate choice of the collision cell size.

Once the system has been partitioned into cells of suitable size, a specific form for the particle velocity rotation operators must be chosen. This choice will also influence the magnitudes of the transport properties of the fluid. Consider a three-dimensional system. It is convenient to take rotations about a randomly chosen direction, $\hat{\mathbf{n}}$, by an angle $\Phi$ chosen from a set of angles. For this choice, the contribution to the post-collision velocity $\mathbf{v}_i$ of particle $i$ in cell $\boldsymbol{\xi}$, $\mathbf{v}_i = \mathrm{V}_\xi + \hat{\omega}_\xi(\mathbf{v}_i' - \mathrm{V}_\xi)$, arising from the rotation is given explicitly by

$$
\hat{\omega}_{\xi}(\mathbf{v}_{i}^{\prime}-\mathrm{V}_{\xi})=\hat{\mathbf{n}} \hat{\mathbf{n}} \cdot\left(\mathbf{v}_{i}^{\prime}-\mathrm{V}_{\xi}\right)+(\mathbf{I}-\hat{\mathbf{n}} \hat{\mathbf{n}}) \cdot\left(\mathbf{v}_{i}^{\prime}-\mathrm{V}_{\xi}\right) \cos \Phi-\hat{\mathbf{n}} \times\left(\mathbf{v}_{i}^{\prime}-\mathrm{V}_{\xi}\right) \sin \Phi. \tag{5}
$$

The unit vector $\hat{\mathbf{n}}$ may be sampled uniformly from the surface of a sphere, while the angles $\Phi$ may be chosen in any convenient way. For example, convenient choices are to select $\Phi$ randomly from the set $\{\pi/2, -\pi/2\}$, or from the set of all angles $0 \leq \Phi \leq \pi$.

A more elegant way to implement the collision rule is to represent a rotation matrix as a unit quaternion $\hat{\omega}_{\xi}$, and a velocity vector as a pure quaternion $\tilde{\mathbf{v}} = (0, v_x, v_y, v_z)$. For this choice, the contribution to the post-collision velocity $\mathbf{v}_i$ of particle $i$ in cell $\xi$, with slight abuse of notation, is written as $\mathbf{v}_i = \mathrm{V}_{\xi} + Ad_{\hat{\omega}_{\xi}} \cdot (\mathbf{v}_i' - \mathrm{V}_{\xi})$, where the conjugation operation is defined as

$$
Ad_x \cdot y = x y x^* .
$$

One can verify that the conjugation operation preserves the structure of the rotation group $SO(3)$ and transforms the vector space of pure quaternions into itself. A unit quaternion $\hat{\omega}_{\xi}$ can be generated by sampling vectors uniformly from unit ball $B \in R^4$ and subsequent scaling of the resulting vector.

### 2.1 Evolution Equation

In order to carry out a detailed analysis of the model, one may write the dynamics of the system in terms of an evolution equation for the phase space probability density, $\mathrm{P}(\mathbf{V}^{(N)}, \mathbf{X}^{(N)}, t)$, which takes the form,

$$
\mathrm{P}(\mathbf{V}^{(N)}, \mathbf{X}^{(N)} + \mathbf{V}^{(N)} \tau, t + \tau) = \hat{\mathcal{C}} \mathrm{P}(\mathbf{V}^{(N)}, \mathbf{X}^{(N)}, t) . \tag{6}
$$

The displaced position on the left hand side reflects the free streaming between collisions while the collision operator $\hat{\mathcal{C}}$ on the right hand side is defined by

$$
\begin{aligned}
\hat{\mathcal{C}} \mathrm{P}(\mathbf{V}^{(N)}, \mathbf{X}^{(N)}, t) &= \frac{1}{\|\Omega\|^L} \sum_{\Omega^L} \int \mathrm{d} \mathbf{V}'^{(N)} \mathrm{P}(\mathbf{V}'^{(N)}, \mathbf{X}^{(N)}, t) \\
& \quad \times \prod_{i=1}^N \delta\left(\mathbf{v}_i - \mathrm{V}_{\boldsymbol{\xi}} - \hat{\omega}_{\boldsymbol{\xi}}[\mathbf{v}_i' - \mathrm{V}_{\boldsymbol{\xi}}]\right) .
\end{aligned}
$$

Here $L$ is the number of cells and $\|\Omega\|^L$ is the number of rotation operators in the set.
Introducing the free streaming Liouville operator,

$$
\mathrm{i} \mathcal{L}_0 = \mathbf{V}^{(N)} \cdot \nabla_{\mathbf{X}^{(N)}} , \tag{7}
$$

we may write (6) in the alternative form,

$$
\mathrm{e}^{\mathrm{i} \mathcal{L}_0 \tau} \mathrm{P}(\mathbf{V}^{(N)}, \mathbf{X}^{(N)}, t + \tau) = \hat{\mathcal{C}} \mathrm{P}(\mathbf{V}^{(N)}, \mathbf{X}^{(N)}, t) . \tag{8}
$$

Using this expression it is instructive to write the evolution equation in continuous time with a delta function collision term,

$$
\frac{\partial}{\partial t} P(\mathbf{X}^{(N)}, \mathbf{V}^{(N)}, t) = \left( -\mathrm{i} \mathcal{L}_0 + \tilde{\mathcal{C}} \right) P(\mathbf{X}^{(N)}, \mathbf{V}^N), t) , \tag{9}
$$

where the collision operator $\tilde{\mathcal{C}}$ acts at discrete time intervals on the velocities of the particles and is defined as

$$
\tilde{\mathcal{C}} P\left(\mathbf{X}^{(N)}, \mathbf{V}^{(N)}, t\right)=\sum_{m=0}^{\infty} \delta(t-m \tau)(\hat{\mathcal{C}}-1) P\left(\mathbf{X}^{(N)}, \mathbf{V}^{(N)}, t\right). \tag{10}
$$

The reduction of the evolution equation (9) to the discrete form (8) can be carried out by integrating (9) from $t=m \tau+\epsilon$ to $t+\tau$ where $\epsilon$ is an infinitesimal number.

The evolution equation (6) can be written in a more compact form by letting $\Gamma=$ $(\mathbf{V}^{(N)}, \mathbf{X}^{(N)})$ denote a phase point and defining a transition operator $\mathcal{W}(\Gamma' \to \Gamma)$ that accounts for the streaming and collision steps. The discrete-time evolution equation may then be written as

$$
\mathrm{P}(\Gamma, t+\tau)=\int \mathrm{d} \Gamma' \mathcal{W}\left(\Gamma' \to \Gamma\right) \mathrm{P}\left(\Gamma', t\right) \equiv \hat{\mathcal{W}} \mathrm{P}(t), \tag{11}
$$

where the integral implies summation over any preimages of the state $\Gamma$. More explicitly, the transition operator has the definition,

$$
\begin{aligned}
& \int \mathrm{d} \Gamma' \mathcal{W}\left(\Gamma' \to \Gamma\right) \mathrm{P}\left(\Gamma', t\right)=\frac{1}{\|\Omega\|^{L}} \sum_{\Omega^{L}} \int \mathrm{d} \mathbf{V}^{\prime(N)} \mathrm{d} \mathbf{X}^{\prime(N)} \times \\
& \times \prod_{i=1}^{N} \delta\left(\mathbf{v}_{i}-\mathrm{V}_{\boldsymbol{\xi}}-\hat{\omega}_{\boldsymbol{\xi}}\left[\mathbf{v}_{i}^{\prime}-\mathrm{V}_{\boldsymbol{\xi}}\right]\right) \delta\left(\mathbf{x}_{i}^{\prime}-\left(\mathbf{x}_{i}+\mathbf{v}_{i} \tau\right)\right) \mathrm{P}\left(\mathbf{V}^{\prime(N)}, \mathbf{X}^{\prime(N)}, t\right).
\end{aligned}
$$

The distribution of this Markov chain is denoted by $P_{0}(\Gamma)=P_{0}(\mathbf{V}^{(N)}, \mathbf{X}^{(N)})$ in equilibrium. Assuming the system is ergodic, in view of the conservation laws obeyed by the dynamics, the stationary distribution is given by the microcanonical ensemble expression,

$$
P_{0}(\Gamma)=\mathcal{N} \delta\left(\frac{1}{N} \sum_{i=1}^{N} \frac{m}{2}\left\|\mathbf{v}_{i}\right\|^{2}-\frac{d}{2 \beta}\right) \delta\left(\sum_{i=1}^{N}\left[\mathbf{v}_{i}-\mathbf{u}\right]\right), \tag{12}
$$

where $\mathbf{u}$ is the mean velocity of the system and $\mathcal{N}$ is a normalization constant. If (12) is integrated over the coordinates and velocities of particles with labels $i=2, \ldots, N$, the Maxwell distribution,

$$
P_{\mathrm{m}}\left(\mathbf{v}_{1}, \mathbf{x}_{1}\right)=\frac{1}{V}\left(\frac{m \beta}{2 \pi}\right)^{d / 2} \exp \left(-\beta m\left\|\mathbf{v}_{1}-\mathbf{u}\right\|^{2} / 2\right), \tag{13}
$$

is obtained in the limit of large $N$. Here $\beta=\left(k_{\mathrm{B}} T\right)^{-1}$, $V$ is the system volume and $d$ is the dimension.

### 2.2 H-Theorem

While the above arguments indicate that the equilibrium one-particle distribution function is Maxwellian, it is instructive to establish an H-theorem for relaxation to equilibrium

for the multi-particle collision dynamics [7]. In the Boltzmann approximation where the full phase space probability distribution function P is a product of identical one-particle probability distributions,

$$
\mathrm{P}\left(\mathbf{V}^{(N)}, \mathbf{X}^{(N)}, t\right)=\prod_{i=1}^{N} P_{1}\left(\mathbf{v}_{i}, \mathbf{x}_{i}, t\right), \tag{14}
$$

it is possible to derive such a relation as we now show.

Letting $\mathrm{f}(\mathbf{v}, \mathbf{x}, t)=N P_{1}(\mathbf{v}, \mathbf{x}, t)$, the H-functional is defined in terms of the reduced one-particle distribution function as,

$$
\begin{aligned}
H(t) &=\int \mathrm{d} \mathbf{v} \mathrm{d} \mathbf{x} \mathrm{f}(\mathbf{v}, \mathbf{x}, t) \ln \mathrm{f}(\mathbf{v}, \mathbf{x}, t) \\
&=\sum_{\xi, n \in \mathbf{N}} \frac{\mathrm{e}^{-\rho \xi}}{n!} \int_{\mathcal{V}^{n}} \mathrm{d} \mathbf{V}^{(n)} \mathrm{d} \mathbf{X}^{(n)} \prod_{i=1}^{n} \mathrm{f}\left(\mathbf{v}_{i}, \mathbf{x}_{i}, t\right) \ln \prod_{i=1}^{n} \mathrm{f}\left(\mathbf{v}_{i}, \mathbf{x}_{i}, t\right), \quad(15)
\end{aligned}
$$

where the second equality follows from the representation of the system in terms of phase space cells and makes use of the resolution of identity $1=\sum_{n \geq 0} \frac{\mathrm{e}^{-x} x^{n}}{n!}$. That $H(t)$ decreases on each discrete evolution step may be proved using the convexity inequality,

$$
\sum_{s} A(s) B(s) \ln B(s) \geq\left(\sum_{s} A(s) B(s)\right) \ln \left(\sum_{s} A(s) B(s)\right), \tag{16}
$$

where $A$ is normalized so that $\sum_{s} A(s)=1$. We define $R^{(n)}$ by

$$
R^{(n)}\left(\mathbf{V}^{(n)}, \mathbf{V}^{\prime(n)}\right)=\frac{1}{\|\Omega\|} \sum_{\hat{\omega} \in \Omega} \prod_{i=1}^{n} \delta\left(\mathbf{v}_{i}-\mathrm{V}+\hat{\omega}\left[\mathrm{V}-\mathbf{v}_{i}^{\prime}\right]\right), \tag{17}
$$

whose integral over $\mathbf{V}^{\prime(n)}$ is unity. Making use of $R^{(n)}$, we may write (15) in the form

$$
\begin{aligned}
H(t)= & \sum_{\xi, n \in \mathbf{N}} \frac{\mathrm{e}^{-\rho \xi}}{n!} \int_{\mathcal{V}^{n}} \mathrm{d} \mathbf{V}^{(n)} \mathrm{d} \mathbf{X}^{(n)} \prod_{i=1}^{n} \mathrm{f}\left(\mathbf{v}_{i}, \mathbf{x}_{i}, t\right) \\
& \times \ln \prod_{i=1}^{n} \mathrm{f}\left(\mathbf{v}_{i}, \mathbf{x}_{i}, t\right) \int \mathrm{d} \mathbf{V}^{\prime(n)} R^{(n)}\left(\mathbf{V}^{n}, \mathbf{V}^{\prime(n)}\right). \tag{18}
\end{aligned}
$$

Next, we exchange the order of the $\mathbf{V}^{\prime(n)}$ and $\mathbf{V}^{(n)}$ integrations in each term in the sum and use (16) to write

$$
\begin{aligned}
& \int \mathrm{d} \mathbf{V}^{(n)} R^{(n)}\left(\mathbf{V}^{(n)}, \mathbf{V}^{\prime(n)}\right) \prod_{i=1}^{n} \mathrm{f}\left(\mathbf{v}_{i}, \mathbf{x}_{i}, t\right) \ln \prod_{i=1}^{n} \mathrm{f}\left(\mathbf{v}_{i}, \mathbf{x}_{i}, t\right) \\
& \quad \geq \tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right) \ln \tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right), \tag{19}
\end{aligned}
$$

where

$$
\tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right)=\int \mathrm{d} \mathbf{V}^{n} R^{(n)}\left(\mathbf{V}^{(n)}, \mathbf{V}^{\prime(n)}\right) \prod_{i=1}^{n} \mathrm{f}\left(\mathbf{v}_{i}, \mathbf{x}_{i}, t\right).
$$

As a result of these manipulations we obtain,

$$
H(t) \geq \sum_{\xi, n \in \mathbf{N}} \frac{\mathrm{e}^{-\rho \xi}}{n!} \int_{\mathcal{V}^{n}} \mathrm{~d} \mathbf{V}^{\prime(n)} \mathrm{d} \mathbf{X}^{(n)} \tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right) \ln \tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right). \quad (20)
$$

To simplify this expression, we let

$$
A=\prod_{i=1}^{n} \hat{\mathrm{f}}_{i}^{(n)}, \quad B=\frac{\tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{n}, t\right)}{Z \prod_{i=1}^{n} \hat{\mathrm{f}}_{i}^{(n)}},
$$

where $Z$ and $\hat{\mathrm{f}}^{(n)}$ are defined as

$$
Z=\int_{\mathcal{V}^{n}} \mathrm{~d} \mathbf{V}^{\prime(n)} \mathrm{d} \mathbf{X}^{(n)} \tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right)=\rho_{\xi}^{n}, \tag{21}
$$

$$
\hat{\mathrm{f}}_{i}^{(n)}\left(\mathbf{v}^{\prime}{ }_{i}, \mathbf{x}_{i}, t\right)=\frac{1}{Z} \int_{\mathcal{V}^{[n-1]}} \mathrm{d} \mathbf{v}^{\prime}{ }_{1} \mathrm{d} \mathbf{x}_{1} \cdots \mathrm{d} \hat{\mathbf{v}}_{i}^{\prime} d \hat{\mathbf{x}}_{i} \cdots \mathrm{d} \mathbf{v}^{\prime}{ }_{n} \mathrm{d} \mathbf{x}_{n} \tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right), \quad (22)
$$

where integrations over variables with a hat in (22) are omitted. Substituting $A$ and $B$ into (16) we find

$$
\begin{gathered}
\frac{1}{Z} \int_{\mathcal{V}^{n}} \mathrm{~d} \mathbf{V}^{\prime(n)} \mathrm{d} \mathbf{X}^{n} \tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right) \ln \frac{\tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right)}{Z \prod_{i=1}^{n} \hat{\mathrm{f}}_{i}^{(n)}} \geq \\
\int_{\mathcal{V}^{n}} \mathrm{~d} \mathbf{V}^{\prime(n)} \mathrm{d} \mathbf{X}^{(n)} \frac{\tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right)}{Z} \ln \int_{\mathcal{V}^{n}} \mathrm{~d} \mathbf{V}^{\prime(n)} \mathrm{d} \mathbf{X}^{(n)} \frac{\tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right)}{Z}=0. \quad(23)
\end{gathered}
$$

Since the argument of the logarithm is unity given the definition of $Z$, the last term in (23) is equal to zero. From (23) it follows that

$$
\begin{gathered}
\int_{\mathcal{V}^{n}} \mathrm{~d} \mathbf{V}^{\prime(n)} \mathrm{d} \mathbf{X}^{(n)} \tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right) \ln \tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right) \\
\geq \int_{\mathcal{V}^{n}} \mathrm{~d} \mathbf{V}^{\prime(n)} \mathrm{d} \mathbf{X}^{(n)} \tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right) \ln Z \prod_{i=1}^{n} \hat{\mathrm{f}}_{i}^{(n)}.
\end{gathered}
$$

Finally, using the identity,

$$
\begin{gathered}
\sum_{i=1}^{n} \int_{\mathcal{V}^{n}} \mathrm{~d} \mathbf{v}^{\prime}{ }_{i} \mathbf{x}_{i} Z \hat{\mathrm{f}}_{i}^{(n)}\left(\mathbf{v}^{\prime}{ }_{i}, \mathbf{x}_{i}, t\right) \ln Z^{1 / n} \hat{\mathrm{f}}_{i}^{(n)}\left(\mathbf{v}^{\prime}{ }_{i}, \mathbf{x}_{i}, t\right)= \\
=\int_{\mathcal{V}^{n}} \mathrm{~d} \mathbf{V}^{\prime(n)} \mathrm{d} \mathbf{X}^{(n)} \tilde{\mathrm{f}}^{(n)}\left(\mathbf{V}^{\prime(n)}, \mathbf{X}^{(n)}, t\right) \ln Z \prod_{i=1}^{n} \hat{\mathrm{f}}_{i}^{(n)}\left(\mathbf{v}^{\prime}{ }_{i}, \mathbf{x}_{i}, t\right),
\end{gathered}
$$

in (20) we have,

$$
\begin{aligned}
H(t) & \geq \sum_{i, \xi, n \in \mathbf{N} 1} \frac{\mathrm{e}^{-\rho \xi} \rho_{\xi}^{n-1}}{n!} \int_{\mathcal{V}} \mathrm{d} \mathbf{v}^{\prime} \mathrm{d} \mathbf{x} Z^{1 / n} \hat{\mathrm{f}}_{i}^{(n)}\left(\mathbf{v}^{\prime}, \mathbf{x}, t\right) \ln Z^{1 / n} \hat{\mathrm{f}}_{i}^{(n)}\left(\mathbf{v}^{\prime}, \mathbf{x}, t\right) \\
& \geq \int \mathrm{d} \mathbf{v}^{\prime} \mathrm{d} \mathbf{x} \mathcal{C}(\mathrm{f}) \ln \mathcal{C}(\mathrm{f})=\int \mathrm{d} \mathbf{v}^{\prime} \mathrm{d} \mathbf{x} \mathrm{f}\left(\mathbf{v}^{\prime}, \mathbf{x}, t+1\right) \ln \mathrm{f}\left(\mathbf{v}^{\prime}, \mathbf{x}, t+1\right).
\end{aligned}
$$

The second inequality follows from the application of (16) with $A$ given by the Poisson distribution $A(n)=\left(\mathrm{e}^{-\rho \xi} \rho_{\xi}^{n-1}\right) /[(n-1)!]$, and the last equality follows from the invariance of the integral with respect to translations by the streaming transformation. Therefore, the value of the H functional at time $t+\tau$ does not exceed its value at time $t$ so that

$$
H(t) \geq \int \mathrm{d} \mathbf{v}^{\prime} \mathrm{d} \mathbf{x} \mathrm{f}\left(\mathbf{v}^{\prime}, \mathbf{x}, t+\tau\right) \ln \mathrm{f}\left(\mathbf{v}^{\prime}, \mathbf{x}, t+\tau\right). \tag{24}
$$

System Thermalization. In order to confirm these predictions, we study the thermal- ization of a system obeying multi-particle collision dynamics. We consider a three- dimensional system with density $\rho=2$ in a box of length $L=40$ with periodic boundary conditions which is partitioned into $40 \times 40 \times 40$ cells of unit length. The tem perature in reduced units ( $m=1, \tau=1$, and unit cell length) is taken to be $k_{\mathrm{B}} T=4 / 3$. We study the equilibration of a system initialized by $f(\mathbf{v})=\frac{1}{2} \delta\left(\mathbf{v}+\mathbf{v}_{0}\right)+\frac{1}{2} \delta\left(\mathbf{v}-\mathbf{v}_{0}\right)$, where $\mathbf{v}_{0}=(2,0,0)$. The results of such a simulation after relaxation to equilibrium are shown as a histogram of the $x$-component of the velocity in Fig. 3. One can see that a Boltzmann distribution of velocities is obtained.

It is instructive to examine the relaxation to equilibrium of the multi-particle colli- sion dynamics in more detail. For this purpose, it is convenient to rewrite one-particle probability distribution as a sum of Hermite polynomials ,

$$
f\left(v_{x}\right)=\zeta^{-1} \mathrm{e}^{-\left(v_{x} / \zeta\right)^{2}} \sum \alpha_{i} H_{i}\left(v_{x} / \zeta\right), \tag{25}
$$

where $\zeta=\sqrt{2 k_{\mathrm{B}} T / m}$. The expansion coefficients are easily obtained from the expec- tation values of Hermite polynomials,

$$
(-1)^{n} n! 2^{n} \sqrt{\pi} \alpha_{n}=\left\langle H_{n}\left(v_{x} / \zeta\right)\right\rangle. \tag{26}
$$

The expansion coefficients are less sensitive to fluctuations than histograms (Fig. 3) and demonstrate fast convergence to local equilibrium.

In Fig. 4 we plot the values of the expansion coefficients as a function of time. Using the above expansion and assuming the system is spatially homogeneous, we may write for velocity component of the one-particle probability distribution

$$
-H_{\mathrm{v}}=\int \mathrm{d} \mathbf{v} f(\mathbf{v}) \ln f(\mathbf{v})=\langle\ln f(\mathbf{v})\rangle. \tag{27}
$$

Approximating $f(\mathbf{v})$ by the Hermite polynomial expansion to obtain the results, we plot values of the $H$-function in a non-equilibrium run. As expected from the theoretical analysis, the functional increases monotonously with time and rapidly converges to the equilibrium value.

![](./images/813331739265990657_3.jpg)

Fig.3. Histogram of the velocity distribution in the system at equilibrium. The system has $N=5.1\times10^6$ particles, $k_{\rm B}T=4/3$ and $\rho=2.0$. The solid line is the calculated distribution based on an expansion of the distribution function using ten Hermite polynomials (see text)

![](./images/813331739265990657_4.jpg)

Fig.4. Dynamics of the coefficients of the Hermite polynomials of a system relaxing to equilibrium. Coefficients of $H_2(v_x)$-(solid line), $H_4(v_x)$-(dotted line) and $H_6(v_x)$-(dotted line) are plotted. Odd coefficients vanish due to symmetry and the coefficient of $H_0$ is equal to one by definition

![](./images/813331739265990657_5.jpg)

Fig. 5. Evolution of the velocity component of the $H$-function from non-equilibrium initial conditions. Details are given in the text

## 3 Hydrodynamic Equations and Transport Properties

The dynamics described above is very simple, both in its conception and in its implementation. However, it is essential to provide a theoretical underpinning for the mesoscale dynamics to be able to assess its properties and to demonstrate that it yields the correct hydrodynamic equations. In this section we use projection operator methods to reduce the multi-particle collision dynamics to hydrodynamic equations for the conserved fields. As a by-product of this derivation we also obtain correlation function expressions for the transport properties of the system that can be used for their calculation.

### 3.1 Evolution Equations for Mean Dynamical Variables

The projection operator methods we use are based on methods developed for continuous-time deterministic systems [11,12]. Modifications of the projection operator techniques must be made to account for the intrinsic stochasticity and discrete-time dynamics of the mesoscopic dynamics [13]. We first present the derivation of a general set of projected equations and then specialize the projection operator to one that depends on the conserved fields.

In order to derive a set of evolution equations for the mean values of a set of dynamical variables $\mathbf{a}$, we introduce a projection operator $\mathcal{P}$ by,

$$
(\mathcal{P} \mathbf{h})(\Gamma)=\mathbf{a}^{\dagger}(\Gamma) P_{0}(\Gamma)\left\langle\mathbf{a a}^{\dagger}\right\rangle^{-1} \int \mathrm{d} \Gamma^{\prime} \mathbf{a}\left(\Gamma^{\prime}\right) \mathbf{h}\left(\Gamma^{\prime}\right),
$$

where $\mathbf{h}(\Gamma)$ is any function of the phase space variables. The dagger denotes the adjoint and the angular brackets symbolize an average over the equilibrium distribution, i.e.,

$$
\langle\cdots\rangle=\int \mathrm{d} \Gamma \cdots P_{0}(\Gamma).
$$

The complementary operator $\mathcal{Q}$ is defined by $\mathcal{Q}=1-\mathcal{P}$. Applying the projection operators $\mathcal{P}$ and $\mathcal{Q}$ to (11) we obtain a system of two equations,

$$
\mathrm{P}_{\mathcal{P}}(t+\tau)=\mathcal{P} \hat{\mathcal{W}} \mathrm{P}_{\mathcal{P}}(t)+\mathcal{P}(\hat{\mathcal{W}}-1) \mathrm{P}_{\mathcal{Q}}(t),\qquad(28)
$$

$$
\mathrm{P}_{\mathcal{Q}}(t+\tau)=\mathcal{Q}(\hat{\mathcal{W}}-1) \mathrm{P}_{\mathcal{P}}(t)+\mathcal{Q} \hat{\mathcal{W}} \mathrm{P}_{\mathcal{Q}}(t),\qquad(29)
$$

where $\mathrm{P}_{\mathcal{P}}(t)=\mathcal{P} \mathrm{P}(t)$ and $\mathrm{P}_{\mathcal{Q}}(t)=\mathcal{Q} \mathrm{P}(t)$. To facilitate some of the calculations presented below, we have replaced $\hat{\mathcal{W}}$ by $\hat{\mathcal{W}}-1$ in certain terms where this replacement has no effect because $\mathcal{P} \mathcal{Q}=0$. Solving (29) by iteration leads to

$$
\mathrm{P}_{\mathcal{Q}}(t)=[\mathcal{Q} \hat{\mathcal{W}}]^{t} \mathrm{P}_{\mathcal{Q}}(0)+\sum_{\ell=1}^{n}[\mathcal{Q} \hat{\mathcal{W}}]^{\ell-1} \mathcal{Q}(\hat{\mathcal{W}}-1) \mathrm{P}_{\mathcal{P}}(t-\ell \tau),\qquad(30)
$$

where $t=n \tau$. Substitution of this result into (28) gives

$$
\mathrm{P}_{\mathcal{P}}(t+\tau)=\mathcal{P} \hat{\mathcal{W}} \mathrm{P}_{\mathcal{P}}(t)+\sum_{\ell=1}^{n} \mathcal{K}(\ell-1) \mathrm{P}_{\mathcal{P}}(t-\ell \tau),\qquad(31)
$$

where the memory kernel is defined by

$$
\mathcal{K}(\ell)=\mathcal{P}(\hat{\mathcal{W}}-1)[\mathcal{Q} \hat{\mathcal{W}}]^{\ell} \mathcal{Q}(\hat{\mathcal{W}}-1) \mathcal{P}.\qquad(32)
$$

The first term on right hand side of (30) was eliminated by the use of a specially prepared ensemble of initial conditions where deviations from equilibrium occur only in the dynamical variables in the set $\mathbf{a}$ so that $\mathrm{P}_{\mathcal{Q}}(0)=0$.

From (31) we can easily derive a set of equations for the average values of the dynamical variables,

$$
\overline{\mathbf{a}}(t)=\int \mathrm{d} \Gamma \mathbf{a}(\Gamma) \mathrm{P}(\Gamma, t),\qquad(33)
$$

by multiplying this equation from the left by $\mathbf{a}$ and integrating over the phase space variables to obtain,

$$
\overline{\mathbf{a}}(t+\tau)-\overline{\mathbf{a}}(t)=\left\langle\mathbf{a}(\hat{\mathcal{W}}-1) \mathbf{a}^{\dagger}\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1} \overline{\mathbf{a}}(t)+\sum_{\ell=1}^{t} \mathbf{K}(\ell-1) \overline{\mathbf{a}}(t-\ell \tau),(34)
$$

where

$$
\mathbf{K}(\ell)=\left\langle\mathbf{a}(\hat{\mathcal{W}}-1)[\mathcal{Q} \hat{\mathcal{W}}]^{\ell} \mathcal{Q}(\hat{\mathcal{W}}-1) \mathbf{a}^{\dagger}\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}.
$$

For slowly decaying dynamical variables, which are our main concern, $\overline{\mathbf{a}}(t-\ell\tau)$ can be replaced by $\overline{\mathbf{a}}(t)$ and the upper limit on the sum can be replaced by infinity. In this approximation (34) becomes the kinetic equation

$$
\overline{\mathbf{a}}(t+\tau)-\overline{\mathbf{a}}(t)=\left(\boldsymbol{\Omega}+\boldsymbol{\Phi}\right)\overline{\mathbf{a}}(t),\tag{35}
$$

where the matrices $\boldsymbol{\Omega}$ and $\boldsymbol{\Phi}$ are given by

$$
\boldsymbol{\Omega}=\left\langle\mathbf{a}(\hat{\mathcal{W}}-1)\mathbf{a}^{\dagger}\right\rangle\left\langle\mathbf{a}\mathbf{a}^{\dagger}\right\rangle^{-1},\tag{36}
$$

$$
\boldsymbol{\Phi}=\sum_{\ell=1}^{\infty}\mathbf{K}(\ell-1).
$$

We now analyze the structure of (35) for the specific choice of conserved dynamical variables.

### 3.2 Kinetic Equations for Conserved Variables

The hydrodynamic equations describe the dynamics of the conserved mass, momentum and energy density fields. The microscopic fields corresponding to these variables, which are relevant for the multi-particle collision dynamics, are the particle density along with momentum (or, equivalently, velocity for equal mass particles) and energy densities in a cell,

$$
\rho(\mathbf{x})=\sum_{i=1}^{N}\delta(\mathbf{x}_{i}-\mathbf{x}),\tag{37}
$$

$$
\boldsymbol{\mu}(\boldsymbol{\xi})=\sum_{i=1}^{N}\mathbf{v}_{i}\theta(1/2-|\mathbf{x}_{i}-\boldsymbol{\xi}|),\tag{38}
$$

$$
\varepsilon(\boldsymbol{\xi})=\sum_{i=1}^{N}\frac{m}{2}v_{i}^{2}\theta(1/2-|\mathbf{x}_{i}-\boldsymbol{\xi}|).
$$

Here $\theta$ is the Heaviside function. Since the hydrodynamic equations are valid on distance and time scales which are long compared to molecular scales, it is convenient to work with the Fourier transforms of these fields and then consider the small $k$ limit. The Fourier transforms of these variables are given by,

$$
\rho_{\mathbf{k}}=\int\mathrm{d}\mathbf{x}\,\mathrm{e}^{\mathrm{i}\mathbf{k}\cdot\mathbf{x}}\rho(\mathbf{x})=\sum_{i=1}^{N}\mathrm{e}^{\mathrm{i}\mathbf{k}\cdot\mathbf{x}_{i}},\tag{39}
$$

$$
\boldsymbol{\mu}_{\mathbf{k}}=\sum_{\boldsymbol{\xi}}\mathrm{e}^{\mathrm{i}\mathbf{k}\cdot\boldsymbol{\xi}}\boldsymbol{\mu}(\boldsymbol{\xi})=\sum_{i=1}^{N}\mathbf{v}_{i}\sum_{\boldsymbol{\xi}}\mathrm{e}^{\mathrm{i}\mathbf{k}\cdot\boldsymbol{\xi}}\theta(1/2-|\mathbf{x}_{i}-\boldsymbol{\xi}|),\tag{40}
$$

$$
\varepsilon_{\mathbf{k}}=\sum_{\boldsymbol{\xi}}\mathrm{e}^{\mathrm{i}\mathbf{k}\cdot\boldsymbol{\xi}}\varepsilon(\boldsymbol{\xi})=\sum_{i=1}^{N}\frac{m}{2}v_{i}^{2}\sum_{\boldsymbol{\xi}}\mathrm{e}^{\mathrm{i}\mathbf{k}\cdot\boldsymbol{\xi}}\theta(1/2-|\mathbf{x}_{i}-\boldsymbol{\xi}|).
$$

Rather than dealing with this set of variables directly, it is useful to define an orthogonal set of dynamical variables, $\mathbf{a}_{\mathbf{k}} = \{\rho_{\mathbf{k}}, \boldsymbol{\mu}_{\mathbf{k}}, s_{\mathbf{k}}\}$, where the entropy density is defined as $s_{\mathbf{k}} = \varepsilon_{\mathbf{k}} - C_{\mathrm{v}} T \rho_{\mathbf{k}}$ with $C_{\mathrm{v}}$ the specific heat. In terms of this set of variables the matrix $\langle \mathbf{a}_{\mathbf{k}} \mathbf{a}_{\mathbf{k}}^{\dagger} \rangle$ is diagonal and given by

$$
\left\langle\mathbf{a}_{\mathbf{k}} \mathbf{a}_{\mathbf{k}}^{\dagger}\right\rangle=N\left(\begin{array}{ccc}
1 & \mathbf{0} & 0 \\
\mathbf{0} & \left(k_{\mathrm{B}} T / m\right) \mathbf{1} & \mathbf{0} \\
0 & \mathbf{0} & C_{\mathrm{v}} k_{\mathrm{B}} T^{2}
\end{array}\right),
\tag{41}
$$

where $C_{\mathrm{v}}=3 k_{\mathrm{B}} / 2$ in three dimensions. Using this statistically independent set of variables simplifies the algebraic manipulations. When confusion is unlikely to arise, we shall simplify the notation and drop the subscripts $\mathbf{k}$ on the vectors of dynamical variables. In view of the fact that one is primarily interested in the evolution of the conserved variable fields, we specialize the general kinetic equation (35) to this case and, in particular, we determine the forms of the $\boldsymbol{\Omega}$ and $\boldsymbol{\Phi}$ matrices.

Structure of the $\boldsymbol{\Omega}$ Matrix. We first construct the form of the matrix $\boldsymbol{\Omega}$ to $\mathcal{O}(\mathbf{k}^{2})$ for conserved fields. For this purpose it is convenient to introduce an operator $\mathcal{S}(\Gamma, t)$ which relates the state $\Gamma$ at the initial time to the set of states at time $t$, weighted with the probability of transition to the corresponding state. In terms of this notation, equilibrium averages may be written as

$$
\int \mathrm{d} \Gamma \int \mathrm{d} \Gamma^{\prime} \mathbf{a}(\Gamma) \mathcal{W}\left(\Gamma^{\prime} \rightarrow \Gamma\right) \mathbf{h}^{\dagger}\left(\Gamma^{\prime}\right) P_{0}\left(\Gamma^{\prime}\right)=\left\langle\mathbf{a}(\mathcal{S}(\Gamma, \tau)) \mathbf{h}^{\dagger}(\Gamma)\right\rangle,
$$

where summation over states is implied. Similarly, if we consider the equilibrium average of a set of dynamical variables, using the stationarity of the equilibrium distribution, $P_{0}(\Gamma)=\hat{\mathcal{W}} P_{0}(\Gamma)$, we may write,

$$
\begin{aligned}
\int \mathrm{d} \Gamma \mathbf{h}^{\dagger}(\Gamma) P_{0}(\Gamma) &=\int \mathrm{d} \Gamma \mathbf{h}^{\dagger}(\Gamma) \hat{\mathcal{W}} P_{0}(\Gamma)=\int \mathrm{d} \Gamma \mathbf{h}^{\dagger}(\Gamma) \int \mathrm{d} \Gamma^{\prime} \mathcal{W}\left(\Gamma^{\prime} \rightarrow \Gamma\right) P_{0}\left(\Gamma^{\prime}\right) \\
&=\int \mathrm{d} \Gamma^{\prime}\left[\int \mathrm{d} \Gamma \mathbf{h}^{\dagger}(\Gamma) \mathcal{W}\left(\Gamma^{\prime} \rightarrow \Gamma\right)\right] P_{0}\left(\Gamma^{\prime}\right), \\
& \equiv \int \mathrm{d} \Gamma^{\prime} \mathbf{h}^{\dagger}\left(\mathcal{S}\left(\Gamma^{\prime}, \tau\right)\right) P_{0}\left(\Gamma^{\prime}\right).
\end{aligned}
$$

From this result we may establish that

$$
\left\langle\mathbf{a}(\mathcal{S}(\Gamma, \tau)) \mathbf{a}^{\dagger}(\mathcal{S}(\Gamma, \tau))\right\rangle=\left\langle\mathbf{a}(\Gamma) \mathbf{a}^{\dagger}(\Gamma)\right\rangle.
$$

Letting $\mathbf{b}(\Gamma)=\mathbf{a}(\mathcal{S}(\Gamma, \tau))-\mathbf{a}(\Gamma)$ we may write $\boldsymbol{\Omega}$ as

$$
\boldsymbol{\Omega}=\left\langle\mathbf{b} \mathbf{a}^{\dagger}\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}.
$$

The elements of the $\mathbf{b}$ variable vector are given by

$$
b_{\mathbf{k}}^{\rho}=\mathrm{i} \mathbf{k} \cdot \sum_{i=1}^{N} \tau \mathbf{v}_{i}+o(\mathbf{k}), \tag{42}
$$

$$
b_{\mathbf{k}}^{\mu}=\mathrm{i} \mathbf{k} \cdot \sum_{i=1}^{N} \Delta \boldsymbol{\xi}_{i} \mathbf{v}_{i}+o(\mathbf{k}), \tag{43}
$$

$$
b_{\mathbf{k}}^{\epsilon}=\mathrm{i} \mathbf{k} \cdot \sum_{i=1}^{N} \Delta \boldsymbol{\xi}_{i} \frac{m}{2} v_{i}^{2}+o(\mathbf{k}),
$$

where we introduced notation $\Delta \boldsymbol{\xi}_{i}(t)=\boldsymbol{\xi}_{i}(t+\tau)-\boldsymbol{\xi}_{i}(t)$ with $\boldsymbol{\xi}_{i}(t)$ the coordinate of the cell in which particle $i$ is located at time $t$. One can see that these elements are $\mathcal{O}(\mathbf{k})$.

It is useful to rewrite the numerator of $\boldsymbol{\Omega}$ as a sum of symmetric and antisymmetric terms; thus, we have

$$
\boldsymbol{\Omega}=\mathcal{A}-\frac{1}{2}\left\langle\mathbf{b} \mathbf{b}^{\dagger}\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}, \tag{44}
$$

where we defined $\mathcal{A}$ as

$$
\mathcal{A}=\frac{1}{2}\left\langle\mathbf{a}(\mathcal{S}(\Gamma, \tau)) \mathbf{a}^{\dagger}(\Gamma)-\mathbf{a}(\Gamma) \mathbf{a}^{\dagger}(\mathcal{S}(\Gamma, \tau))\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}.
$$

Using the explicit forms of the conserved mass, momentum and energy density fields, $\mathcal{A}$ may be computed to give,

$$
\mathcal{A}=N \tau \frac{k_{\mathrm{B}} T}{m}\left(\begin{array}{ccc}
0 & \mathrm{i} \mathbf{k} & 0 \\
\mathrm{i} \mathbf{k}^{T} & \mathbf{0} & \mathrm{i} \mathbf{k}^{T} k_{\mathrm{B}} T \\
0 & \mathrm{i} \mathbf{k} k_{\mathrm{B}} T & 0
\end{array}\right)\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}. \tag{45}
$$

In order to write $\left\langle\mathbf{b} \mathbf{b}^{\dagger}\right\rangle$ in the second term of (44) in an alternative form, we introduce a projection operator onto a dynamical variable as

$$
P \mathbf{h}=\left\langle\mathbf{h} \mathbf{a}^{\dagger}\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1} \mathbf{a}. \tag{46}
$$

In terms of this new projection operator we have

$$
\frac{1}{2}\left\langle\mathbf{b} \mathbf{b}^{\dagger}\right\rangle=\frac{1}{2}\left\langle\mathbf{b} Q \mathbf{b}^{\dagger}\right\rangle+\frac{1}{2}\left\langle\mathbf{b} P \mathbf{b}^{\dagger}\right\rangle=\frac{1}{2}\left\langle\mathbf{f}(0) \mathbf{f}^{\dagger}(0)\right\rangle+\frac{1}{2}\left\langle\mathbf{b} P \mathbf{b}^{\dagger}\right\rangle, \tag{47}
$$

where we have defined the random forces,

$$
\mathbf{f}(0)=\mathbf{b}-\left\langle\mathbf{b} \mathbf{a}^{\dagger}\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1} \mathbf{a}=\mathbf{a}(\mathcal{S}(\Gamma, \tau))-\left\langle\mathbf{a}(\mathcal{S}(\Gamma, \tau)) \mathbf{a}^{\dagger}\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1} \mathbf{a}. \tag{48}
$$

The explicit expressions for the random forces corresponding to the conserved variable fields are, to lowest order in $\mathbf{k}$,

$$
f_{\mathbf{k}}^{\rho}(t)=0+o(\mathbf{k}), \tag{49}
$$

$$
f_{\mathbf{k}}^{\boldsymbol{\mu}}(t)=\tau \sum_{i}\left(\mathbf{v}_{i}(t)\left[\mathrm{i} \mathbf{k} \cdot \frac{\Delta \boldsymbol{\xi}_{i}(t)}{\tau}\right]-\frac{1}{d} \mathrm{i} \mathbf{k} v_{i}(t)^{2}\right)+o(\mathbf{k}), \tag{50}
$$

$$
f_{\mathbf{k}}^{\epsilon}(t)=\tau \mathrm{i} \mathbf{k} \cdot \sum_{i}\left[\frac{\Delta \boldsymbol{\xi}_{i}(t)}{\tau}\left(\frac{m}{2} v_{i}(t)^{2}-C_{\mathrm{v}} T\right)-\mathbf{v}_{i}(t)\left(C_{\mathrm{p}}-C_{\mathrm{v}}\right) T\right]+o(\mathbf{k}).
$$

The term $\langle \mathbf{b}P\mathbf{b}^\dagger \rangle \langle \mathbf{a}\mathbf{a}^\dagger \rangle^{-1}$ may be expressed as

$$
\langle \mathbf{b}P\mathbf{b}^\dagger \rangle \langle \mathbf{a}\mathbf{a}^\dagger \rangle^{-1} = \langle \mathbf{b}\mathbf{a}^\dagger \rangle \langle \mathbf{a}\mathbf{a}^\dagger \rangle^{-1} \langle \mathbf{a}\mathbf{b}^\dagger \rangle \langle \mathbf{a}\mathbf{a}^\dagger \rangle^{-1} .
$$

From (44) we have,

$$
\langle \mathbf{b}\mathbf{a}^\dagger \rangle \langle \mathbf{a}\mathbf{a}^\dagger \rangle^{-1} = \mathcal{A} + o(\mathbf{k}) , \quad \langle \mathbf{a}\mathbf{b}^\dagger \rangle \langle \mathbf{a}\mathbf{a}^\dagger \rangle^{-1} = -\mathcal{A} + o(\mathbf{k}).
$$

Consequently, it follows that

$$
\langle \mathbf{b}P\mathbf{b}^\dagger \rangle \langle \mathbf{a}\mathbf{a}^\dagger \rangle^{-1} = -\mathcal{A}^2 + o(\mathbf{k}^2).
$$

Assembling all of these results, the net effect of these manipulations is that the $\boldsymbol{\Omega}$ matrix may be written as

$$
\boldsymbol{\Omega} = \mathcal{A} + \frac{1}{2}\mathcal{A}^2 - \frac{1}{2} \langle \mathbf{f}(0)\mathbf{f}^\dagger(0) \rangle \langle \mathbf{a}\mathbf{a}^\dagger \rangle^{-1} + o(\mathbf{k}^2).
$$

Structure of the $\Phi$ Matrix. In order to write the $\Phi$ matrix in a convenient form, we first show that the projected dynamics can be replaced by ordinary dynamics in the small k limit for conserved variables. If the dynamics is given by a composition of streaming and collision operators in that order, we may write,

$$
a_{\mathbf{k}} = \sum_i a_i(t)\mathrm{e}^{\mathrm{i}\mathbf{k}\cdot \mathbf{x}_i(t)} = \sum_i a_i(t-\tau)\mathrm{e}^{\mathrm{i}\mathbf{k}\cdot \mathbf{x}_i(t)}, \tag{51}
$$

where $a_i$ is a conserved variable. This result follows from the conservation of the quantities a under collisions at time $t-\tau$. Using the identity (51) and expanding a in powers of $\mathbf{k}$, we may write $\mathcal{P}[\hat{\mathcal{W}} - 1]\mathbf{h}^\dagger$, where $\mathbf{h}^\dagger$ is an arbitrary function, as

$$
\begin{aligned}
(\mathcal{P}[\hat{\mathcal{W}} - 1]\mathbf{h}^\dagger)(\Gamma) &= \mathbf{a}^\dagger P_0(\Gamma) \langle \mathbf{a}\mathbf{a}^\dagger \rangle^{-1} \int \mathrm{d}\Gamma'\mathbf{b}(\Gamma')\mathbf{h}^\dagger(\Gamma') \\
&= \mathbf{a}^\dagger P_0(\Gamma) \langle \mathbf{a}\mathbf{a}^\dagger \rangle^{-1} \iint \Gamma' \bigg[ \mathbf{h}^\dagger(\Gamma') \\
&\quad \sum_i (\mathrm{i}\mathbf{k} \cdot [\mathbf{x}_i'(t+\tau) - \mathbf{x}_i'(t)] a_i'(t) + o(\mathbf{k})) \bigg]. \tag{52}
\end{aligned}
$$

Similarly, one may show that $[\hat{\mathcal{W}} - 1]\mathcal{P} = \mathcal{O}(\mathbf{k})$.

Using these results we may prove by induction that

$$
[\mathcal{Q}\hat{\mathcal{W}}]^\ell \mathcal{Q} = \mathcal{Q}\mathcal{W}^\ell \mathcal{Q} + \mathcal{O}(\mathbf{k}). \tag{53}
$$

For $\ell = 0$ relation (53) holds; we assume that it holds for $\ell$ and prove the relation for $\ell+1$. We write $[\mathcal{Q}\hat{\mathcal{W}}]^{\ell+1}\mathcal{Q} = [\mathcal{Q}\hat{\mathcal{W}}]^\ell \mathcal{Q}\hat{\mathcal{W}}\mathcal{Q}$. Then

$$
\begin{aligned}
[\mathcal{Q}\hat{\mathcal{W}}]^{\ell+1}\mathcal{Q} &= [\mathcal{Q}\mathcal{W}]^\ell \mathcal{Q}\hat{\mathcal{W}}\mathcal{Q} = \mathcal{Q}\hat{\mathcal{W}}^\ell \mathcal{Q}\hat{\mathcal{W}}\mathcal{Q} + \mathcal{O}(\mathbf{k}) \\
&= \mathcal{Q}\mathcal{W}^\ell [\mathcal{Q} + (\hat{\mathcal{W}} - 1) + \mathcal{O}(\mathbf{k})] \mathcal{Q} + \mathcal{O}(\mathbf{k}) \\
&= \mathcal{Q}\hat{\mathcal{W}}^{\ell+1}\mathcal{Q} + \mathcal{O}(\mathbf{k}),
\end{aligned}
$$

where we expressed $Q\hat{\mathcal{W}}$ in the equivalent form

$$
\mathcal{Q}\hat{\mathcal{W}}=\mathcal{Q}+(\hat{\mathcal{W}}-1)-\mathcal{P}(\hat{\mathcal{W}}-1)=\mathcal{Q}+(\hat{\mathcal{W}}-1)+\mathcal{O}(\mathbf{k}).\tag{54}
$$

This proves the assertion of the recursion relation and, thus, the validity of (53).

The correlation function in the definition of the $\boldsymbol{\Phi}$ matrix can now be written as

$$
\mathbf{K}(\ell-1)\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle=\left\langle\mathbf{a}(\hat{\mathcal{W}}-1) \mathcal{Q} \hat{\mathcal{W}}^{\ell-1} \mathcal{Q}(\hat{\mathcal{W}}-1) \mathbf{a}^{\dagger}\right\rangle=\left\langle\mathbf{f}(\ell) \tilde{\mathbf{f}}(0)\right\rangle,\tag{55}
$$

with

$$
\mathbf{f}(\ell)=\mathbf{a}(\mathcal{S}(\Gamma,(\ell+1) \tau))-\left\langle\mathbf{a}(\mathcal{S}(\Gamma, \tau)) \mathbf{a}^{\dagger}\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1} \mathbf{a}(\mathcal{S}(\Gamma, \ell \tau)),\tag{56}
$$

and

$$
\tilde{\mathbf{f}}(0)=\mathbf{a}^{\dagger}-\mathbf{a}^{\dagger}(\mathcal{S}(\Gamma, \tau))\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}\left\langle\mathbf{a}(\mathcal{S}(\Gamma, \tau)) \mathbf{a}^{\dagger}\right\rangle.
$$

The last step in the analysis of $\boldsymbol{\Phi}$ is to rewrite the expression for $\tilde{\mathbf{f}}(0)$ for conserved variables fields for small $\mathbf{k}$. We may write,

$$
\begin{aligned}
\mathbf{f}^{\dagger}(0)+\tilde{\mathbf{f}}(0) & =-\mathbf{b}^{\dagger}\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1} \mathcal{A}\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle+\frac{1}{2}\left(\mathbf{a}^{\dagger}+\mathbf{a}^{\dagger}(\mathcal{S}(\Gamma, \tau))\right)\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}\left\langle\mathbf{b} \mathbf{b}^{\dagger}\right\rangle \\
& =\mathcal{O}\left(\mathbf{k}^{2}\right).
\end{aligned}
$$

Making use of this result, the $\boldsymbol{\Phi}$ matrix to order $\mathcal{O}(\mathbf{k}^{2})$ takes the form,

$$
\boldsymbol{\Phi}=-\sum_{\ell=1}^{\infty}\left\langle\mathbf{f}(\ell) \mathbf{f}^{\dagger}(0)\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}.
$$

### 3.3 General Form of the Kinetic Equation

In order to use these results to write the kinetic equations in the form of the hydrodynamic equations, we consider the passage from discrete-time to continuous-time dynamics. From the analysis presented above, the sum of the $\boldsymbol{\Omega}$ and $\boldsymbol{\Phi}$ matrices may be written in terms of contributions of $\mathcal{O}(\mathbf{k})$ and $\mathcal{O}(\mathbf{k}^{2})$, respectively, as

$$
\boldsymbol{\Omega}+\boldsymbol{\Phi}=\mathcal{A}-\mathcal{B},
$$

where

$$
\mathcal{B}=-\frac{1}{2} \mathcal{A}^{2}+\frac{1}{2}\left\langle\mathbf{f}(0) \mathbf{f}^{\dagger}(0)\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}-\boldsymbol{\Phi}.
$$

The matrices $\mathcal{A}$ and $\mathcal{B}$ are of the first and second orders in $\mathbf{k}$, respectively. The evolution equation (35) can be written as

$$
\overline{\mathbf{a}}(t+\tau)=\mathrm{e}^{\tau \frac{\partial}{\partial t}} \overline{\mathbf{a}}(t)=(1+\mathcal{A}-\mathcal{B}) \bar{a}(t),
$$

so that we have the operator identity

$$
\mathrm{e}^{\tau \frac{\partial}{\partial t}}=1+\mathcal{A}-\mathcal{B}.
$$

Taking the logarithm of this operator identity and expanding the logarithm in a Taylor series up to second order in k we obtain

$$
\begin{aligned}
\tau \frac{\partial}{\partial t} &=\mathcal{A}-\frac{1}{2} \mathcal{A}^{2}-\mathcal{B}, \\
&=\mathcal{A}-\frac{1}{2}\left\langle\mathbf{f}(0) \mathbf{f}^{\dagger}(0)\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}-\sum_{\ell=1}^{\infty}\left\langle\mathbf{f}(\ell) \mathbf{f}^{\dagger}(0)\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}.
\end{aligned}\tag{57}
$$

Using this relation, the continuous-time limit of (35) is given by

$$
\tau \partial_{t} \overline{\mathbf{a}}=\mathcal{A} \overline{\mathbf{a}}-\left[\lim _{\mathrm{T} \rightarrow \infty} \frac{1}{2 \mathrm{~T}} \sum_{\ell, \ell^{\prime \prime}<\mathrm{T}}\left\langle\mathbf{f}(\ell) \mathbf{f}^{\dagger}\left(\ell^{\prime}\right)\right\rangle\left\langle\mathbf{a} \mathbf{a}^{\dagger}\right\rangle^{-1}\right] \overline{\mathbf{a}}.\tag{58}
$$

The second term on the right hand side provides expressions for the transport coefficients in terms of discrete-time sums of autocorrelation functions. In writing this equation we used the notation,

$$
\lim _{\mathrm{T} \rightarrow \infty} \frac{1}{2 \mathrm{~T}} \sum_{\ell, \ell^{\prime}<\mathrm{T}}\left\langle\mathbf{f}(\ell) \mathbf{f}^{\dagger}\left(\ell^{\prime}\right)\right\rangle=\frac{1}{2}\left\langle\mathbf{f}(0) \mathbf{f}^{\dagger}(0)\right\rangle+\sum_{\ell=1}^{\infty}\left\langle\mathbf{f}(\ell) \mathbf{f}^{\dagger}(0)\right\rangle.\tag{59}
$$

### 3.4 Hydrodynamic Equations

All that remains in the derivation is to substitute the explicit forms of the conserved fields to obtain the hydrodynamic equations. To separate the shear and bulk viscosity contributions one may write the momentum random force as a sum terms which are parallel and perpendicular to $\mathbf{k}$,

$$
f_{\mathbf{k}}^{\boldsymbol{\mu}}(t)=\tau \sum_{i}\left(\mathrm{v}_{i}^{\perp}(t) \mathrm{i} \mathbf{k} \cdot \frac{\Delta \boldsymbol{\xi}^{\perp}{ }_{i}(t)}{\tau}+\mathrm{i} \mathbf{k}\left[\mathrm{v}_{i}^{\|}(t) \frac{\Delta \boldsymbol{\xi}^{\|}{ }_{i}(t)}{\tau}-\frac{1}{d} v_{i}(t)^{2}\right]\right)+o(\mathbf{k}),
$$

where $\mathrm{v}_{i}^{\|}$and $\mathrm{v}_{i}^{\perp}$ are the parallel and perpendicular components of the velocity, respectively. Then, using this decomposition of the random force and the explicit expression for the $\mathcal{A}$ matrix, we find that the linearized hydrodynamic equations take the form,

$$
\partial_{t} \rho_{\mathbf{k}}=\mathrm{i} \mathbf{k} \cdot \boldsymbol{\mu}_{\mathbf{k}},\tag{60}
$$

$$
\partial_{t} \boldsymbol{\mu}_{\mathbf{k}}=\mathrm{i} \mathbf{k} \cdot\left[k_{\mathrm{B}} T \rho_{\mathbf{k}}+\frac{s_{\mathbf{k}}}{c_{\mathrm{v}}}\right]-\frac{\eta}{m \rho}\left[\mathbf{k} \mathbf{k}-\frac{1}{d} k^{2} \mathbf{1}\right]: \boldsymbol{\mu}_{\mathbf{k}}-\frac{\eta_{b}}{m \rho} \mathbf{k} \mathbf{k}: \boldsymbol{\mu}_{\mathbf{k}}\tag{61}
$$

$$
\partial_{t} s_{\mathbf{k}}=k_{\mathrm{B}} T \mathrm{i} \mathbf{k} \cdot \boldsymbol{\mu}_{\mathbf{k}}-\frac{\lambda}{m \rho} k^{2} s_{\mathbf{k}}.
$$

The viscosity coefficient is obtained from the auto-correlation of the transverse component of $f_{\mathbf{k}}^{\boldsymbol{\mu}}(t)$:

$$
\eta=\lim _{\mathrm{T} \rightarrow \infty} \frac{m^{2} \rho}{2 k_{\mathrm{B}} T N \mathrm{~T} \tau} \sum_{\ell, \ell^{\prime}<\mathrm{T}} \sum_{i, j} \mathrm{v}_{x i}(\ell \tau) \Delta \xi_{y i}(\ell \tau) \mathrm{v}_{x j}\left(\ell^{\prime} \tau\right) \Delta \xi_{y j}\left(\ell^{\prime} \tau\right).\tag{62}
$$

![](./images/813331739265990657_6.jpg)

Fig. 6. Shear viscosity and stress autocorrelation function as a function of time. The circles on the solid line show computed values of the stress autocorrelation function. The filled diamonds on the dotted line are the results of the partial summation of the autocorrelation function. The parameter values are $\rho=10.0$ and $k_{\mathrm{B}} T=1 / 3$

Similarly, the bulk viscosity $\eta_{b}$ and heat conductivity $\lambda$ transport coefficients are given by the correlation function expressions,

$$
\begin{aligned}
\eta_{b}= & \lim _{\tau \rightarrow \infty} \frac{\tau m \rho}{2 k_{\mathrm{B}} T N \tau} \sum_{\ell, \ell^{\prime}<\tau} \sum_{i, j}\left[\mathbf{v}_{i}^{\|}(\ell \tau) \frac{\Delta \boldsymbol{\xi}^{\|}{ }_{i}(\ell \tau)}{\tau}-\frac{1}{d} v_{i}(\ell \tau)^{2}\right] \\
& \times\left[\mathbf{v}_{j}^{\|}\left(\ell^{\prime} \tau\right) \frac{\Delta \boldsymbol{\xi}^{\|}{ }_{j}\left(\ell^{\prime} \tau\right)}{\tau}-\frac{1}{d} v_{j}\left(\ell^{\prime} \tau\right)^{2}\right],
\end{aligned}
$$

$$
\lambda=\lim _{\tau \rightarrow \infty} \frac{m \rho}{4 C_{\mathrm{v}} k_{\mathrm{B}} T^{2} N \tau} \sum_{\ell, \ell^{\prime}<\tau} f_{\mathbf{k}}^{\varepsilon}(\ell \tau) f_{\mathbf{k}}^{\varepsilon}\left(\ell^{\prime} \tau\right).
$$

This rather detailed calculation has served to establish that the mesoscopic multiparticle collision model does lead to the correct full set of hydrodynamic equations on long distance and time scales. Furthermore, we have derived expressions for the transport properties of the fluid in terms of discrete-time autocorrelation function expressions that can serve as the starting points for computing these properties from simulations of the dynamics.

As an illustration of the calculation of a transport property using the discrete Green- Kubo expression, in Fig. 6 we present the results of numerical simulations of the stress- stress autocorrelation function and shear viscosity. A scattering rule was used where the velocity was rotated by $\pi / 2$ in random directions. The simulations were carried out on a three-dimensional system of size $32 \times 32 \times 32$ lattice cells. The figure shows both the stress-stress autocorrelation function and its time integral, whose asymptotic value

is the solvent viscosity. We note that the stress autocorrelation decays to zero in about two discrete time units, setting the time scale for solvent relaxation.

## 4 Simulations of Fluid Flow

While the demonstration of the properties of the mesoscopic multi-particle collision model and the derivation of the hydrodynamic equations are rather involved, the dynam- ics may be simulated in a simple and efficient manner. Below we give some examples of the simulations of fluid flow in order to demonstrate the utility of the model for investigations of hydrodynamic flows.

We first show the results of simulations of three-dimensional flow past a cylinder. A solid cylinder of radius $2R=100$ parallel to the $z$ axis was created by imposing bounce- back conditions on particles colliding with the cylinder. Periodic boundary conditions were imposed on the system. The system was initialized by assigning velocities from Maxwell distribution

$$
\sqrt{\frac{m}{2\pi k_{\mathrm{B}} T}} \exp \left(-m u^{2} /\left(2 k_{\mathrm{B}} T\right)\right).
$$

The flow along the $x$-direction was established by assigning velocities from a Maxwell distribution with the velocity shifted $u_x$ in the domain $x<5$. One may demonstrate that the system relaxes to a uniform steady flow in the absence of dissipation.

After approximately 2000 time steps the flow past the cylinder stabilizes and a periodically oscillating pattern is established. In Fig. 7 a snapshot of the flow pattern is plotted. The length of an arrow at each position is proportional to the flow velocity at this point and we have color coded the direction of the flow with varying hues. We note that spatiotemporal averaging obscures fine details of flow. In Fig. 7 the fine structure of flow pattern supporting the two large vortexes is not visible.

![](./images/813331739265990657_7.jpg)

Fig.7. Simulation of fluid flow past a cylinder showing the development of vortices. The cylinder diameter, system size and density are $D=2R=100$, $500\times600\times5$ and $\rho=4.0$, respectively. The temperature and velocity at the origin are $T=1.0$ and $u_x=0.3$. The corresponding kinematic viscosity and Reynolds number are $\nu=0.58$ and $\text{Re}=52.0$

![](./images/813331739265990657_8.jpg)

Fig. 8. Development of the boundary layer at the rear of a disc suddenly set in motion

As another illustration of the method, in Fig. 8 we show the results of simulations of stages in the development of the boundary layer at the rear of a disk suddenly set in motion. The system size is $400 \times 400$ cells of unit length and the disc diameter $2R = 100$. The flow velocity at $x=0$, the density of the system and the Reynolds number are $u_x=0.4$, $\rho=20.0$ and $\text{Re}=1520$, respectively. Periodic boundary conditions are imposed on the system and bounce-back conditions on the disc. The initially symmetric flow separates from the disk and a backflow at the far end of the disk develops. At the contact line between the normal flow and the oppositely-directed backflow, a system of vortices appears which later expands into the full-scale boundary layer [14].

A series of more detailed studies of the properties of hydrodynamic flows and fluid flow around obstacles of different shapes using the mesoscopic multi-particle collision model were carried out by Ihle and Kroll [15] and Lamura et al. [16,17]. These studies provide further evidence of the utility of the method for the investigation of problems in hydrodynamics.

## 5 Mesoscopic Model for Solute Molecular Dynamics

In this section we show how one may study the dynamics of molecules and other types of molecular aggregates or particles embedded in a mesoscopic solvent. There are many circumstances when such an approximate treatment of solvent dynamics is appropriate or necessary. This is the case if one's primary interest is in the properties of the solute molecules; then the details of the solvent molecule motions need not be analyzed except in so far as they influence solute molecule dynamics. This view of solvent dynamics underlies all Langevin and generalized Langevin approximations to condensed phase systems where the solvent is not explicitly included in the description of the system. Rather than adopting such a extreme reduction of description, we show how one may construct a hybrid molecular dynamics-mesoscopic solvent scheme that eliminates the need for some of the restrictive assumptions in more phenomenological models.

The system we now consider comprises $N$ solvent or bath molecules (labelled $b$) with phase space coordinates $(\mathbf{V}^{(N)}, \mathbf{X}^{(N)})$ introduced earlier, which will be described at the mesoscopic level, and $M$ solute molecules (labelled $s$) with phase space coordinates $\mathbf{X}^{(M)} = (\mathbf{x}_{N+1}, \mathbf{x}_{N+2}, \dots, \mathbf{x}_{N+M})$ and $\mathbf{V}^{(M)} = (\mathbf{v}_{N+1}, \mathbf{v}_{N+2}, \dots, \mathbf{v}_{N+M})$, which will be described microscopically. The system is demonstrated schematically in Fig. 9. We assume the solute molecules interact through the intermolecular potential $V_{\text{ss}}(\mathbf{X}^{(M)})$, while the solute-solvent interactions are governed by the potential energy $V_{\text{sb}}(\mathbf{X}^{(M)}, \mathbf{X}^{(N)})$. Since the solvent will be treated at the mesoscopic level using multi-particle collision dynamics, solvent-solvent interactions are set to zero.

![](./images/813331739265990657_9.jpg)

Fig.9. Schematic representation of a system following hybrid mesoscopic-molecular dynamics.
The small particles are treated at the mesoscopic level while the large particles are treated by full
molecular dynamics that includes solute-solute and solute-solvent interactions

If we let $(\mathbf{X}^{(K)}, \mathbf{V}^{(K)}) = (\mathbf{X}^{(N)}, \mathbf{X}^{(M)}, \mathbf{V}^{(N)} \mathbf{V}^{(M)})$ for the $K=N+M$ particles,
we can define the classical evolution operator for streaming in the potential energy
function, $V(\mathbf{X})=V_{\mathrm{ss}}(\mathbf{X}^{(M)})+V_{\mathrm{sb}}(\mathbf{X})$ as

$$
\mathrm{i} \mathcal{L}=\mathbf{V}^{(K)} \cdot \nabla_{\mathbf{X}^{(K)}}+\mathbf{F} \cdot \mathbf{M}^{-1} \cdot \nabla_{\mathbf{V}^{(K)}},
$$

where $\mathbf{F}=-\nabla_{\mathbf{X}^{(K)}} V(\mathbf{X}^{(K)})$ is the force and $\mathbf{M}$ is a diagonal matrix of masses. The
equation for the evolution of the $N+M$ particle phase space density in the hybrid
molecular-mesoscopic dynamics is easily written using this classical evolution operator
and the collision operator $\mathcal{C}$ introduced earlier. We have

$$
\frac{\partial}{\partial t} \mathrm{P}\left(\mathbf{X}^{(K)}, \mathbf{V}^{(K)}, t\right)=\left(-\mathrm{i} \mathcal{L}+\tilde{\mathcal{C}}\right) \mathrm{P}\left(\mathbf{X}^{(K)}, \mathbf{V}^{K)}, t\right),
$$

where the collision operator $\tilde{\mathcal{C}}$ was defined in (10). If we integrate this equation from
$t_{0}=m \tau+\epsilon=t$ to $t+\tau$ we obtain

$$
\mathrm{e}^{\mathrm{i} \mathcal{L} \tau} \mathrm{P}\left(\mathbf{X}^{(K)}, \mathbf{V}^{(K)}, t+\tau\right)=\hat{\mathcal{C}} \mathrm{P}\left(\mathbf{X}^{(K)}, \mathbf{V}^{(K)}, t\right). \tag{65}
$$

If the solute molecules are not present, the potential contribution to the evolution operator
$\mathrm{i} \mathcal{L}$ is zero, and the evolution operator describes free streaming. In this limit (65) reduces
to (6).

To implement the dynamics described by (65), we imagine that the phase space
trajectory of the entire system is partitioned into time segments of length $\tau$ within which
one evolves the system by Newton's equations of motion,

$$
\begin{aligned}
\dot{\mathbf{x}}_{i} & =\mathbf{v}_{i} \\
m_{i} \dot{\mathbf{v}}_{i} & =-\frac{\partial V}{\partial \mathbf{x}_{i}}=\mathbf{F}_{i},
\end{aligned}
$$

where $m_{i}$ is the mass of particle $i$. Such a partitioned phase space trajectory is depicted
schematically in Fig. 10. During this Newtonian portion of the evolution the solvent-
solvent intermolecular potential is zero; thus, solvent molecules undergo free streaming
in the solute-solvent intermolecular potential (assuming they are within range of this

![](./images/813331739265990657_10.jpg)

Fig. 10. Schematic representation of a system trajectory showing the division into MD and seg- ments separated by multi-particle solvent molecule collisions

potential) but do not interact with each other. At discrete time intervals $\tau$ the solvent molecules are assumed to undergo multi-particle collisions as discussed in Sect. 2 which change the velocities of the solvent molecules. These multi-particle collisions replace the full solvent-solvent interactions. Since there are no solvent-solvent interactions this molecular dynamics evolution may be carried out efficiently since it scales with $M \times$ $(N+M)$ rather than $(M+N)^{2}$. Since typically $N \gg M$ this will lead to short simulation times compared to full molecular dynamics.

## 6 Simulations of Hybrid Dynamics

In this section we give some simple illustrations of the implementation of the hybrid mesoscopic-molecular dynamics algorithm. In order to carry out such simulations, one must select a values for the molecular dynamics and multi-particle collision time steps, $\Delta t$ and $\tau$, respectively. During the molecular dynamics segments $\Delta t$ for the integration of Newton's equations of motion must be chosen to resolve motion in all the forces, including solvent-solute forces. In addition, since the multi-particle collision rule pro- duces momentum jumps in the solvent momenta, an integration scheme must be selected that involves the velocities of the molecules, such as the velocity Verlet or leap-frog al- gorithms [18]. The time $\tau$ for multi-particle collisions is dictated by several factors. From the perspective of the solvent molecules, $\tau$ must be sufficiently large that solvent molecules stream on the order of a cell length in order to ensure sufficient dynami- cal changes in multi-particle collisions. Furthermore, $\tau$ should be sufficiently small to incorporate correctly the effect of solvent dynamics on the solute molecules. In such applications, typically we are interested in both microscopic (mesoscopic) and collec- tive effects on the solute dynamics. We now show how this hybrid model can be used to study some familiar problems in condensed matter physics.

### 6.1 Brownian Motion

The classical theory of Brownian motion is perhaps one of the best known models of solute motion in a solvent whose dynamics is treated approximately [19]. In this theory the Langevin equation for a Brownian particle takes the form [20,21]

$$
M \frac{\mathrm{d} \mathbf{u}(t)}{\mathrm{d} t}=-\zeta \mathbf{u}(t)+\mathbf{f}(t), \tag{66}
$$

where $\mathbf{r}$ and $\mathbf{u}$ are the position and velocity of the Brownian particle with mass $M$, $\zeta$ is the friction coefficient and $\mathbf{f}$ is a random force which is usually taken to be a Gaussian random process with white noise spectrum,

$$\langle \mathbf{f}(t)\rangle = 0 \quad \text{and} \quad \langle \mathbf{f}(t)\mathbf{f}(t')\rangle = 2k_{\mathrm{B}}T\zeta\delta(t-t').$$

In this mesoscopic description all information about solute-solvent interactions is con- tained in the friction coefficient which must be evaluated by other means; it is a parameter in phenomenological Brownian motion theory. In general, the friction coefficient con- tains both microscopic and macroscopic (hydrodynamic) contributions whose relative magnitudes depend on the relative sizes of the Brownian and solvent molecules. Thus, the Langevin approach is not complete unless the friction coefficient and stochastic prop- erties of the random force are determined from the molecular dynamics of the solute and solvent molecules.

In order to study Brownian motion in the mesoscopic solvent, we consider the dif- fusion of solute particles that interact with the mesoscopic solvent molecules through continuous intermolecular forces. The Hamiltonian that governs the molecular dynamics segments is

$$\mathcal{H} = \frac{1}{2}M\mathbf{u}^2 + \sum_{i=1}^{N} \frac{1}{2}m\mathbf{v}_i^2 + \sum_{i=1}^{N} V_{\mathrm{sb}}(|\mathbf{x}_i - \mathbf{r}|). \tag{67}$$

For the simulation results presented below, the Brownian particle-solvent interactions, $V_{\mathrm{sb}}$, are given by truncated LJ potentials,

$$V_{\mathrm{sb}}(r) =
\begin{cases}
4\epsilon \left[ \frac{\sigma^{12}}{r^{12}} - \frac{\sigma^6}{r^6} + \frac{1}{4} \right], & r < 2^{1/6}\sigma \\
0, & r > 2^{1/6}\sigma
\end{cases}, \tag{68}$$

with $\sigma = 3.0$ and $\epsilon = 1.0$. In the Newtonian trajectory segments the equations of motion were integrated using the velocity Verlet algorithm [18] with a time step of $\Delta t = 0.02\tau$, which is sufficient to resolve the intermolecular forces. The mass of the Brownian particle was taken to be $M = 250$ while the solvent particle mass was $m = 1$. The solvent density was $\rho = 10$ and reduced temperature was $k_{\mathrm{B}}T = 1/3$. For these conditions, both the mass density ratio, $m/M = 0.004$ and the mass density ratio, $m\rho/(M/V_{\mathrm{B}}) = 0.45$, where the volume of the Brownian particle is $V_{\mathrm{B}} = 4\pi\sigma^3/3$, are small so that one expects simple dynamics [22]. The multi-particle collision dynamics was carried out using random rotations by $\pm\pi/2$ about randomly chosen axes as discussed earlier.

The velocity autocorrelation function of the Brownian particle is defined as

$$C_u(t) = \frac{1}{3} \langle \mathbf{u}(t) \cdot \mathbf{u} \rangle.$$

The phenomenological theory of Brownian motion based on the Langevin equation (66) predicts exponential decay, $C_u(t) = (k_{\mathrm{B}}T/M)\exp -\zeta t/M$, for all times. For systems with continuous forces, the $C_u(t)$ must have an initial slope of zero and behave as

$$C_u(t) \sim \frac{k_{\mathrm{B}}T}{M} - \frac{\langle F^2\rangle}{3M^2} \frac{t^2}{2},$$

for short times. Simulation results using the hybrid mesoscopic model confirm this short time behavior. It is more interesting to study the long time behavior of the velocity correlation function. While a simple Langevin model predicts exponential decay for all times, it is known from both full molecular dynamics simulations [23], kinetic theory [24] and mode coupling theories [25] that the $C_{u}(t) \sim t^{-3 / 2}$ for long times in three dimensions. The long time tail arises from the coupling between the Brownian particle density field and the viscous modes of the solvent. Such an effect can also be captured in a generalized Langevin model,

$$
M \frac{\mathrm{d} \mathbf{u}(t)}{\mathrm{d} t}=-\int_{0}^{t} \mathrm{~d} t^{\prime} \zeta\left(t-t^{\prime}\right) \mathbf{u}\left(t^{\prime}\right)+\mathbf{f}(t),
$$

where the time dependent friction is evaluated using hydrodynamics [26]. In particular, using the expression for the friction coefficient for a macroscopic particle oscillating with frequency $\omega$ in an incompressible continuum fluid, [27]

$$
\zeta(\omega)=\zeta_{h}\left[\frac{(1+\alpha \sigma)}{(1+\alpha \sigma / 3)}+\frac{1}{6}(\alpha \sigma)^{2}\right],
$$

where the hydrodynamic friction coefficient is $\zeta_{h}=4 \pi \eta \sigma$ for slip boundary conditions appropriate for our central our system with central forces. The Brownian particle radius has been set equal to the Lennard-Jones $\sigma$ parameter for Brownian particle-solvent particle interactions. Here $\alpha^{2}=-\mathrm{i} \omega \rho M / \eta$. The time-dependent diffusion coefficient $D(t)$ is defined by the finite time integral of the velocity correlation function,

$$
D(t)=\int_{0}^{t} \mathrm{~d} t^{\prime} C_{u}\left(t^{\prime}\right).
$$

Using (69) with (70), the long time behavior of $D(t)$ is given by

$$
D(t) \approx D-\frac{\alpha_{1}}{\sqrt{t}}, \text { where } \alpha_{1}=\frac{2}{3}(4 \pi \eta)^{-3 / 2} \sqrt{M \rho}.
$$

This result is valid for either slip or stick boundary conditions. The coefficient of $t^{-1 / 2}$ depends only on the Brownian particle mass and the solvent density and viscosity. Figure 11 plots the hybrid mesoscopic model simulation results for $D(t)$ versus $t^{-1 / 2}$. One can see from this figure that $D(t)$ does indeed possess a $t^{-1 / 2}$ long time tail. Furthermore, the coefficient of this long time decay is in agreement with the predictions of hydrodynamics: The predicted hydrodynamic value using the mesoscopic solvent viscosity is $\alpha_{1}=0.0114$ while the simulation value is approximately 0.0104 . These results show that the mesoscopic multi-particle collision dynamics correctly captures the collective hydrodynamic component of the Brownian particle diffusion coefficient.

It is also of interest to compare the magnitude of the diffusion coefficient obtained from the simulation with that predicted by simple theories that account for both microscopic and hydrodynamic contributions to this transport coefficient. One can view the environment of the Brownian particle as being composed of two parts: A boundary layer of microscopic dimensions where details of the intermolecular forces and collision dynamics are essential and an outer region where a continuum hydrodynamic description

![](./images/813331739265990657_11.jpg)

Fig. 11. Long time behavior of the time dependent diffusion coefficient

![](./images/813331739265990657_12.jpg)

Fig. 12. Boundary layer around a microscopic particle

of the solvent is appropriate. (See Fig. 12 for a schematic picture of this decomposition of the environment.) Using a generalized boundary condition in conjunction with a kinetic theory description of the boundary layer one may derive an approximate expression for the diffusion coefficient of the form, [28]

$$
D = D_0 + D_h \ , \tag{71}
$$

where $D_0$ is a microscopic contribution arising from binary collision events whose approximate from can be estimated from kinetic theory,

$$
D_0 = \frac{3}{8\rho\sigma^2} \left( \frac{k_{\rm B}T}{2\pi M} \right)^{1/2} \ ,
$$

and a hydrodynamic contribution $D_h = k_{\rm B}T/\zeta_h$. The estimates of these quantities are: $D_0 = 1.0 \times 10^{-3}$ and $D_h = 4.5 \times 10^{-3}$ giving $D = 5.5 \times 10^{-3}$. The hydrodynamic component dominates the microscopic component for a large Brownian particle. The value of the diffusion coefficient determined from an extrapolation of the simulation data is $D = 4.9 \times 10^{-3}$ which is close to that from the approximate theory.

From these results we conclude that the hybrid mesoscopic dynamics is able capture important microscopic and hydrodynamic contributions to the velocity correlation func- tion and diffusion coefficient. It provides a description of the dynamics that goes beyond that of simple or even generalized Langevin models with approximate expressions for the time dependent friction.

## 6.2 Cluster Dynamics

As a somewhat more complicated example we study the dynamics and equilibrium structure of an aggregate or cluster of microscopic particles in the mesoscopic solvent. Clusters are interesting systems that have been studied extensively both experimentally and theoretically [29,30]. They have attracted attention since clusters with nanoscale dimensions lie in a regime which is intermediate between the microscopic and macro- scopic domains and exhibit unusual properties as a result of the strong competition between bulk and surface forces. Clusters of Lennard-Jones (LJ) particles with parame- ters that model argon atoms have been studied in vacuum using full molecular dynamics [31-33]. Studies of the properties of such LJ clusters in the mesoscopic solvent provide information on how such clusters are influenced by a thermalizing environment [34].

More specifically, we consider a system comprising a cluster whose particles have mass $m_s$ and interact through attractive LJ forces,

$$
V_{\mathrm{ss}}=4 \epsilon_{\mathrm{ss}}\left[\frac{\sigma_{\mathrm{ss}}^{12}}{r^{12}}-\frac{\sigma_{\mathrm{ss}}^{6}}{r^{6}}\right],
$$

embedded in the mesoscopic solvent whose particles have mass $m$. The system Hamil- tonian is

$$
\begin{aligned}
\mathcal{H} & =\sum_{i=N+1}^{K} \frac{1}{2} m_{s} \mathbf{u}_{i}^{2}+\sum_{i<i^{\prime}=N+1}^{K} V_{\mathrm{ss}}\left(\left|\mathbf{r}_{i}-\mathbf{r}_{i^{\prime}}\right|\right)+\sum_{i=N+1}^{K} \sum_{j=1}^{N} V_{\mathrm{sb}}\left(\left|\mathbf{r}_{i}-\mathbf{x}_{j}\right|\right)+\sum_{j=1}^{N} \frac{1}{2} m \mathbf{v}_{j}^{2} \\
& \equiv \mathcal{H}_{\mathrm{s}}+V_{\mathrm{sb}}+\mathcal{H}_{\mathrm{b}},
\end{aligned}
$$

where $\mathcal{H}_{\mathrm{s}}$ is the cluster Hamiltonian, $\mathcal{H}_{\mathrm{b}}$ is the bath Hamiltonian which only has a kinetic energy contribution since solvent-solvent forces are zero, and $V_{\mathrm{sb}}$ is again the cluster particle-solvent interaction potential which is taken to be a truncated LJ potential (68). The cluster particle interaction parameters are are taken to mimic argon: $\sigma_{\mathrm{ss}}=0.34 \mathrm{~nm}$ and $\epsilon_{\mathrm{ss}}=1.00604 \mathrm{~kJ} / \mathrm{mol}$ and the values for the cluster particle-solvent molecule interactions are $\epsilon_{\mathrm{sb}}=1.00604$ with $\sigma_{\mathrm{sb}}$ taking either of two values, $\sigma_{\mathrm{sb}}=0.17 \mathrm{~nm}$ or $\sigma_{\mathrm{sb}}=0.221 \mathrm{~nm}$. The masses of the cluster particles are $m_{s}=39.948 \mathrm{~g} / \mathrm{mol}$ and the solvent molecules have masses $m=3.9948 \mathrm{~g} / \mathrm{mol}$.

The cubic simulation box had length $L=5.44 \mathrm{~nm}$ with periodic boundary conditions and contained $N=327680$ solvent molecules with number density $\rho_{s}=2035.42 \mathrm{~nm}^{-3}$ and a cluster with either $M=25$ or 123 particles. The molecular dynamics time step for the velocity Verlet integrator was $\Delta t=0.002 \mathrm{ps}$. The system was divided into $32 \times 32 \times 32$ cells for the multi-particle collision dynamics and $\tau=0.1 \mathrm{ps}$. The same random rotation rule as that described for Brownian motion was employed. In Fig. 13 we show a picture of a cluster with 123 particles at temperature $T=48.4$.

![](./images/813331739265990657_13.jpg)

Fig. 13. Picture of a $M=123$ atom cluster in the mesoscopic solvent. The cluster particles are depicted as large atoms while the solvent atoms are small. Only solvent molecules close to the cluster surface are shown in the figure for clarity

The cluster structure can be described by the radial distribution function for cluster and solvent molecules relative to the center of mass of the cluster,

$$
g_{\mathrm{CM}-\alpha}(r)=\frac{1}{4 \pi r^{2} \rho_{\alpha}}\left\langle\sum_{i}^{N_{\alpha}} \delta\left(\left|\mathbf{x}_{i}-\mathbf{R}_{\mathrm{CM}}\right|-r\right)\right\rangle,
$$

where $\alpha=s$ or $b$ designates a cluster or solvent molecule, $\mathbf{R}_{\mathrm{CM}}$ is the center of mass of the cluster and $\rho_{\alpha}$ is the number density of cluster or solvent molecules. Here $\rho_{s}=\sigma_{\mathrm{ss}}^{-3}=25.44 \mathrm{~nm}^{-3}$.

For clusters in vacuum $g_{\mathrm{CM}-\mathrm{c}}(r)$ shows liquid-like distributions of cluster particles and structural ordering within the clusters [32,33]. The cluster structure is modified when it is embedded in the mesoscopic solvent and the modifications depend on the cluster-solvent interactions. We fix $\epsilon_{\mathrm{sb}}=\epsilon_{\mathrm{ss}}$ and vary $\sigma_{\mathrm{sb}}$. The $M=25$ cluster radial distribution functions are shown in Fig. 14 (left) and (right) for $\sigma_{\mathrm{sb}}=0.17$ and $\sigma_{\mathrm{sb}}=$ 0.221 , respectively. The radial distribution functions $g_{\mathrm{CM}-\mathrm{s}}(r)$ for the solvent molecules relative to the cluster center of mass are also shown in the figure. The structures of the radial distribution functions are similar in vacuum and in the mesoscopic solvent for $\sigma_{\mathrm{sb}}=0.17 \mathrm{~nm}$ but are quite different for $\sigma_{\mathrm{sb}}=0.221 \mathrm{~nm}$ where the cluster is compressed and adopts a solid-like configuration.

This difference is signalled in the structure of the solvent molecule-cluster particle distributions. For $\sigma_{\mathrm{sb}}=0.17$ the solvent molecules are able to penetrate into the cluster. For $\sigma_{\mathrm{sb}}=0.221$ they are not able to do so and the solvent provides a larger external force on the cluster which compresses it and induces a solid-like structural configuration.

The center of mass diffusion coefficients of the clusters can be analyzed using the approximate formula (71) presented in the previous subsection. Since the cluster is a composite object we can determine its effective radius $R$ from the radial distribution function. For the $M=25$ cluster with $\sigma_{\mathrm{sb}}=0.17$ we find $R \approx 2.25$. Furthermore, the central LJ forces now act on the individual cluster atoms so for macroscopic sizes the cluster will appear to have stick boundary conditions. Given these facts, we may estimate $D$ for the cluster and compare the value with that obtained from the simulation of the

![](./images/813331739265990657_14.jpg)

Fig. 14. Radial distribution function $g_{\mathrm{CM}-\mathrm{c}}(r)$ versus $r^{*}$ for $\sigma_{\mathrm{sb}}=0.221 \mathrm{~nm}$ (left) and $\sigma_{\mathrm{sb}}=$ $0.17 \mathrm{~nm}$ (right) for $M=25$ ($T=40.33$) clusters in the mesoscale solvent (solid lines); vacuum cluster (dotted lines). Also shown is the solvent radial distribution function $g_{\mathrm{CM}-\mathrm{s}}(r)$ (dashed lines)

mean square displacement of the cluster. We find, in units of $\mathrm{cm}^{2} / \mathrm{s}, D_{0}=2.8 \times 10^{-7}$, $D_{h}=7.8 \times 10^{-7}$, so that $D($ theory $) \approx 1.1 \times 10^{-6}$. The simulation result is $D(\mathrm{sim})=$ $9.6 \times 10^{-7}$.

## 6.3 Polymer Dynamics

The dynamics of a long polymer chain in solution is determined by macroscopic prop- erties of the solvent [35] rather than the microscopic details of the chain-solvent in- teractions. Indeed, time scale separation between the microscopic collision processes and hydrodynamic flows that define the long time evolution of a polymer chain makes direct simulations of polymer dynamics a challenging task. Therefore, in simulations, it is suitable to replace molecular solvents with mesoscale models [36-38].

Multi-particle collision dynamics can be adapted to model polymer flows [38]. In one version of the model the system is extended to include a polymer chain and "inert" solvent. The polymer chain itself is modelled using standard molecular dynamics. The architecture of the chain and the interactions within it can be varied. The free-streaming propagation step is modified to include evolution of the chain by integrating the chain equations of motion on the time interval $\tau$,

$$
\left(\mathbf{X}^{(M)}(t+\tau), \mathbf{V}^{(M)}(t+\tau)\right)=\mathrm{e}^{\mathrm{i} \mathcal{L} \tau}\left(\mathbf{X}^{(M)}(t), \mathbf{V}^{(M)}(t)\right). \tag{73}
$$

Here $(\mathbf{X}^{(M)}(t), \mathbf{V}^{(M)}(t))$ denotes a set velocities and coordinates of a polymer chain with $M$ monomers and $\mathrm{i}\mathcal{L}$ is defined by the relation $\mathrm{i}\mathcal{L}u=\{\mathcal{H}, u\}$ for any dynamical variable $u$. The Hamiltonian $\mathcal{H}$ of the system is given by

$$
\mathcal{H}=\sum_{i \in \text { solvent }} \frac{1}{2} m_{i} \mathbf{v}_{i}^{2}+\sum_{i \in \text { chain }} \frac{1}{2} M_{i} \mathbf{V}_{i}^{2}+\sum_{i \leq j \in \text { chain }} U_{i j}\left(\mathbf{R}_{i}, \mathbf{R}_{j}\right). \tag{74}
$$

During the propagation step the system evolves according to Newton's equation of motion. For chain atoms (73) is solved by integration of the equation of motions of a

![](./images/813331739265990657_15.jpg)

Fig. 15. Snapshot of a chain configuration showing a few of the surrounding mesoscopic solvent molecules

free chain using the Verlet algorithm

$$
\begin{aligned}
\mathbf{R}_{i}(t+\Delta t) & =\mathbf{R}_{i}(t)+\Delta t \mathbf{V}_{i}(t)+\frac{(\Delta t)^{2}}{2 m_{i}} \mathbf{F}_{i}\left(\mathbf{R}_{i}(t)\right), \\
\mathbf{V}_{i}(t+\Delta t) & =\mathbf{V}_{i}(t)+\frac{\Delta t}{2 M_{i}}\left[\mathbf{F}_{i}\left(\mathbf{R}_{i}(t)\right)+\mathbf{F}_{i}\left(\mathbf{R}_{i}(t+\Delta t)\right)\right],
\end{aligned}\tag{75}
$$

with a time step of $\Delta t$ to evolve the positions and velocities in the MD step. As no force is exerted on the solvent between collision steps we propagate solvent particles with a time step $\Delta t=1$.

To capture hydrodynamic interactions between molecules comprising the chain it is necessary to add chain-solvent interactions. This can done within the multi-particle collision scheme approach without destroying the conservation laws. To this end, during the collision step an additional collision step (2) exchanging momenta and energies of the polymer beads and solvent particles in the same cell is performed. By choosing a suitable class of rotation matrices $\hat{\omega}$ one may tune the bead-solvent friction coefficient. A snapshot of a polymer configuration in the mesoscopic solvent is shown in Fig. 15.

The numerical results of simulations were shown to agree well with an equation of motion for a chain which assumed a linear coupling to the velocity of the surround- ing fluid via viscous friction [38]. Simulations demonstrated that the velocity-velocity correlation function comprises two contributions; an initial exponential decay result- ing from Brownian collisions of monomers with uncorrelated solvent molecules and, at longer times, a hydrodynamic contribution as monomers interact via hydrodynamic modes propagated through the solvent. Analysis of chain diffusion coefficient given by the integral of the velocity-velocity correlation function demonstrated Zimm scaling $D \sim R_{G}^{-1}$ for the hydrodynamic contribution to the diffusion constant.

## 6.4 Complex Fluids

The multi-particle collision model has been extended to the treatment of binary immiscible fluids with a conserved order parameter [39]. The extension is based on the Rothman–Keller model [40] for immiscible lattice gases. The original Rothman–Keller model considers two kinds of particle, called *red* and *blue*, and introduces two fields related to the colors of the particles: A color flux and a color field. The immiscible lattice-gas model is constructed to account for cohesion in real fluids arising from short range attractive intermolecular forces by allowing particles in neighboring sites to influence the configuration of particles at a chosen site. This is accomplished by constructing collision rules where the "work" performed by the color flux against the color field is a minimum.

This idea can be transcribed to the multi-particle collision rule by altering the nature of the rotation operator that effects the collisions in a cell [39]. Again, we let $\boldsymbol{\xi}_\nu$ denote the coordinate of the center of cell $\nu$, and introduce a characteristic function $H_i(\boldsymbol{\xi}_\nu)$ for particle $i$ in cell $\nu$ which takes the value +1 if the particle is red and -1 if the particle is blue. Using this notation the color flux is defined as

$$
\mathbf{q}_\nu = \sum_{i=1}^{n(\xi_\nu)} H_i(\boldsymbol{\xi}_\nu)(\mathbf{v}_i' - \mathrm{V}_{\xi_\nu}) ,
\tag{76}
$$

where $n(\xi_\nu)$ is the number of particles in cell $\nu$. This is the color-weighted relative velocity of the particles in cell $\nu$. The color field is a color gradient arising from the color differences in neighboring cells,

$$
\mathbf{f}_\nu = \sum_{\nu' \in \mathcal{N}(\nu)} \mathrm{w}_{\nu\nu'} \hat{\boldsymbol{\xi}}_{\nu\nu'} \sum_{i=1}^{n(\xi_{\nu'})} H_i(\boldsymbol{\xi}_{\nu'}) ,
\tag{77}
$$

where $\hat{\boldsymbol{\xi}}_{\nu\nu'}$ is a unit vector along the relative separation between cells $\nu$ and $\nu'$, that is $\hat{\boldsymbol{\xi}}_{\nu\nu'} = (\boldsymbol{\xi}_\nu - \boldsymbol{\xi}_{\nu'})/|\boldsymbol{\xi}_\nu - \boldsymbol{\xi}_{\nu'}|$, and $\mathcal{N}(\nu)$ denotes the cells neighboring cell $\nu$. The weight function $\mathrm{w}_{\nu\nu'}$ is taken to be $\mathrm{w}_{\nu\nu'} = |\boldsymbol{\xi}_\nu - \boldsymbol{\xi}_{\nu'}|^{-1}$.

Given these definitions, the rotation matrix, $\hat{\omega}_\nu^c$, for multi-particle collisions in a cell with coordinates $\boldsymbol{\xi}_\nu$ is constructed so that the rotated color flux lies along the color field, $\hat{\mathbf{f}}_\nu = \hat{\omega}_\nu^c \hat{\mathbf{q}}_\nu$. If we let $\hat{\mathbf{h}}_\nu = \hat{\mathbf{f}}_\nu \times \hat{\mathbf{q}}_\nu$, which is normal to both the color flux and color field vectors, the rotation operator effects a rotation of $\hat{\mathbf{q}}_\nu$ by an angle $\theta$ about $\hat{\mathbf{h}}_\nu$, where $\theta$ is the angle between $\hat{\mathbf{q}}_\nu$ and $\hat{\mathbf{f}}_\nu$, $\cos\theta = \hat{\mathbf{f}}_\nu \cdot \hat{\mathbf{q}}_\nu$. The multi-particle collision rule again takes the form, $\mathbf{v}_i = \mathrm{V}_\xi + \hat{\omega}^c(\mathbf{v}_i' - \mathrm{V}_\xi)$, where now, from (5),

$$
\hat{\omega}^c(\mathbf{v}_i' - \mathrm{V}_\xi) = \hat{\mathbf{h}}\hat{\mathbf{h}} \cdot (\mathbf{v}_i' - \mathrm{V}_\xi) + (\mathbf{I} - \hat{\mathbf{h}}\hat{\mathbf{h}}) \cdot (\mathbf{v}_i' - \mathrm{V}_\xi) \cos\theta - \hat{\mathbf{h}} \times (\mathbf{v}_i' - \mathrm{V}_\xi) \sin\theta .
\tag{78}
$$

This rule has been used to simulate phase segregation in binary fluids in two and three dimensions [39]. Simulations on the model have shown that Laplace's law for the pressure difference inside and outside a droplet of radius $R$, $\Delta p = 2\sigma/R$, where $\sigma$ is the surface tension, is satisfied and that this generalization of the collision rule reproduces the main

features of phase segregation dynamics. However, we note that this generalization no longer preserves phase space volumes and is not time reversible. As a result the equi- librium distribution is not Maxwellian. The model has also been extended to include surfactant molecules so that microemulsions may be simulated using such dynamics [41,42].

## 7 Conclusion and Perspectives

The multi-particle collision model provides a simple way to simulate the dynamics of fluids at the mesoscopic level. We have demonstrated that it possesses some basic ingre- dients which are desirable in such models: Mass, momentum and energy are conserved, the equilibrium distribution is Maxwellian, an H-theorem exists and the full set of hy- drodynamic equations are obtained on long distance and time scales. Consequently, the model should find applications to problems in fluid flow and turbulence, especially in complex geometries where solutions of the Navier–Stokes equation are difficult. In this case it may provide an approach that complements DSMC, lattice-gas or lattice Boltzmann methods.

The hybrid mesoscopic multi-particle collision model marries full molecular dynam- ics of embedded particles (solutes) with a mesoscopic treatment of the solvent. We have shown that this hybrid scheme is able to capture essential features of both microscopic and hydrodynamic contributions arising from coupling between the solute and solvent degrees of freedom. The model is flexible enough to allow one to model large colloidal particles by using bounce-back [8] and other suitable generalizations of the collision rule to account for solid objects [39,43] or molecular degrees of freedom using explicit solute-solvent intermolecular potentials. The simple applications presented above have demonstrated the utility of this approach for the Brownian motion of molecules, molec- ular aggregates and polymer molecules in solution. This hybrid approach is likely to provide a promising route to investigate the dynamics of large biopolymers in solution where both specific details of solute-solvent forces and hydrodynamic solvent effects play important roles.

The development of the multi-particle collision model is still at an early stage. Fur- ther generalizations of the model to more complex situations; for example, molecular fluids, chemically reacting flows and more complex systems are possible. The model should not only provide a means to simulate efficiently complex systems and help bridge microscopic and macroscopic time scales but should also permit one to understand some of the important features of solute-solvent dynamics without recourse to full molecular dynamics of very large systems.

## Acknowledgements

This work was supported in part by a grant from the Natural Sciences and Engineering Research Council of Canada.

## References

1.  D.H. Rothman, S. Zaleski: *Lattice-Gas Cellular Automata: Simple Models of Complex Hydrodynamics* (Cambridge University Press, Cambridge 1997)

2.  J.-P. Rivet, J.-P. Boon: *Lattice Gas Hydrodynamics* (Cambridge University Press, Cambridge 2001)

3.  I. Pagonabarraga: Lattice Boltzmann Modeling of Complex Fluids: Colloidal Suspensions and Fluid Mixtures, Lect. Notes Phys. **640**, 275 (2004)

4.  For a review, see, S. Chen, G. Doolen: Ann. Rev. Fluid Mech. **30**, 329 (1998)

5.  L. S. Luo: Phys. Rev. E **62**, 4982 (2000)

6.  S. Succi: *The Lattice Boltzmann Equation – For Fluid Dynamics and Beyond* (Clarendon Press, Oxford 2001)

7.  A. Malevanets, R. Kapral: J. Chem. Phys. **110**, 8605 (1999)

8.  A. Malevanets, R. Kapral: J. Chem. Phys. **112**, 7260 (2000)

9.  G. A. Bird: *Molecular Gas Dynamics* (Clarendon Press, Oxford 1976); G. A. Bird: Comp. & Math. with Appl. **35**, 1 (1998)

10. The multi-particle collision rule was first introduced in the context of a lattice model with a stochastic streaming rule in: A. Malevanets, R. Kapral: Europhys. Lett. **44**, 552 (1998)

11. R. Zwanzig: J. Chem. Phys. **33**, 1338 (1960)

12. H. Mori: Prog. Theor. Phys. **33**, 423 (1965)

13. Related derivations for lattice-gas automata have been carried out in D. d'Humières, B. Has- slacher, P. Lallemand, Y. Pomeau, J.-P. Rivet: Complex systems **1**, 839, (1987); M. H. Ernst. In: *Microscopic Simulations of Complex Hydrodynamics Phenomena*, ed. by M. Mareschal, B. Holian (Plenum Press, New York 1992) p. 153

14. G. K. Batchelor: J. Fluid Mech. **74**, 1 (1976)

15. T. Ihle, D. M. Kroll: Phys. Rev. E **63**, 020201 (2001)

16. A. Lamura, G. Gompper, T. Ihle, D. M. Kroll: Europhys. Lett. **56**, 768 (2001)

17. A. Lamura, G. Gompper, T. Ihle, D. M. Kroll: Europhys. Lett. **56**, 319 (2001)

18. W. C. Swope, H. C. Andersen, P. H. Berens, K. R. Wilson: J. Chem. Phys. **76**, 673 (1982); M. Tuckerman, B. J. Berne, G. J. Martyna: J. Chem. Phys. **97**, 1990 (1992)

19. A. Einstein: *Investigations on the Theory of Brownian Movement*, ed. by R. Fürth (Dover, New York 1956)

20. S. Chandrasekhar: Rev. Mod. Phys. **15**, 1 (1943)

21. R. Kubo: The Fluctuation-Dissipation Theorem. In: *Many-Body Problems*, ed. by W. E. Parry et al. (W. A. Benjamin, New York 1969), p. 235

22. M. Tokuyama, I. Oppenheim: Physica A **94**, 501 (1978)

23. B. J. Alder, T. E. Wainwright: Phys. Rev. Lett. **18**, 988 (1967)

24. J. R. Dorfman, E. G. D. Cohen: Phys. Rev. Lett. **25**, 1257 (1970)

25. K. Kawasaki: Prog. Theor. Phys. **45**, 1691 (1971)

26. R. Zwanzig, M. Bixon: Phys. Rev. A **2**, 2005 (1970)

27. L. D. Landau, E. M. Lifshitz: *Fluid Mechanics* (Pergamon Press, New York 1959)

28. J. T. Hynes, R. Kapral, M. Weinberg: J. Chem. Phys. **70** 1456 (1979)

29. A. W. Castleman, Jr., R. G. Keese: Chem. Rev. **86**, 589 (1986); Annu. Rev. Phys. Chem. **37**, 525 (1986); Science **241**, 36 (1988); A. W. Castleman, Jr., S. Wei: Ann. Rev. Phys. Chem. **45**, 685 (1994)

30. R. S. Berry, T. L. Beck, H. I. Davis, J. Jellinek: Adv. Chem. Phys. **70**, 75 (1988); M. Y. Hahn, R. L. Whetten: Phys. Rev. Lett. **61**, 1190 (1988); H.-P. Cheng, X. Li, R. L. Whetten, R. S. Berry: Phys. Rev. A **46**, 791 (1992)

31. J. D. Honeycutt, H. C. Andersen: J. Phys. Chem. **91**, 4950 (1987)

32. B. G. Moore, A. A. Al-Quraishi: Chem. Phys. **252**, 337 (2000)

33. A. S. Clarke, R. Kapral, B. Moore, G. Patey, X.-G. Wu: Phys. Rev. Lett. **70**, 3283 (1993); A. S. Clarke, R. Kapral, G. Patey: J. Chem. Phys. **101**, 2432 (1994)

34. S.-H. Lee, R. Kapral: Physica A **298**, 56 (2001)

35. M. Doi: *Introduction to Polymer Physics* (Clarendon Press, Oxford 1996)

36. P. Ahlrichs, B. Dünweg: J. Chem. Phys. **111**, 8225 (1999)

37. Y. Kong, C. W. Manke, W. G. Madden, A. G. Schlijper: J. Chem. Phys. **107**, 592 (1997)

38. A. Malevanets, J. M. Yeomans: Europhys. Lett. **52**, 231 (2000)

39. Y. Hashimoto, Y. Chen, H. Ohashi: Comput. Phys. Commun. **129**, 56 (2000)

40. D. H. Rothman, J. M. Keller: J. Stat. Phys.**52**, 1119 (1988)

41. Y. Inoue, Y. Chen, H. Ohashi: Colloids and Surfaces A **201**, 297 (2002)

42. T. Sakai, Y. Chen, H. Ohashi: Phys. Rev. E **65**, 031503 (2002)

43. T. Sakai, Y. Chen, H. Ohashi: J. Stat. Phys. **107**, 85 (2002)