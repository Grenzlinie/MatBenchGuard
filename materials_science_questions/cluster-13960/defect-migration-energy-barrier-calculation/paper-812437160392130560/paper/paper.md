# Calculation of defect migration rates by molecular dynamics simulation

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1987 J. Phys. C: Solid State Phys. 20 2331

(http://iopscience.iop.org/0022-3719/20/16/009)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 141.161.91.14
This content was downloaded on 17/08/2015 at 10:44

Please note that terms and conditions apply.

# Calculation of defect migration rates by molecular dynamics simulation

M J Gillan, J H Harding and R-J Tarento†
Theoretical Physics Division, AERE Harwell, Oxfordshire, UK

Received 20 October 1986

Abstract. The migration of point defects is usually treated using Vineyard's theory, but recent work has shown that this is inadequate for some important materials. We discuss techniques based on molecular dynamics simulation which do not rely on the approximations of this theory. We have made calculations for a rigid-ion model of cobalt oxide that demonstrate the practical effectiveness of the molecular dynamics techniques. Our results indicate that for this particular model the Vineyard theory is qualitatively reliable.

## 1. Introduction

Much experimental and theoretical work on point defects in solids has the ultimate aim of determining and interpreting atomic diffusion coefficients. These can usually be expressed as the product of three factors, (i) the defect concentration, (ii) the defect diffusion coefficient and (iii) a correlation factor. The third factor, which depends on the particular defect mechanism, can be derived from purely geometrical considerations in the simple case of tracer diffusion. It is generally satisfactory to calculate the formation energies and entropies which determine defect concentrations on the basis of quasi-harmonic theory (Catlow and Mackrodt 1982, Gillan and Jacobs 1983, Harding 1985a, b). The calculation of defect diffusion coefficients is, however, not quite so straightforward. The diffusion coefficient of a defect can be written as

$$
D=z a^{2} \Gamma \tag{1}
$$

where $z$ is a geometrical factor, $a$ is the jump distance and $\Gamma$ is the hopping rate, i.e. the rate at which the defect hops from a given site to a particular neighbour. The standard theory for the hopping rate is that of Vineyard (1957) (see also Vineyard and Krumhansl 1985), according to which

$$
\Gamma=\bar{\nu} \exp \left(-\Delta E / k_{\mathrm{B}} T\right) \tag{2}
$$

where $\Delta E$ is the migration energy and $\bar{\nu}$ is the effective frequency. $\bar{\nu}$ can be written in terms of the two sets of normal-mode frequencies $\{\nu_i\}$ and $\{\nu_i'\}$ of the system with the defect in its stable site and at the saddle point, respectively, as $\bar{\nu}=(\Pi_i \nu_i)/(\Pi_i' \nu_i')$, where the product over $\nu_i'$ excludes the unstable model at the saddle point. There are two crucial assumptions in the Vineyard theory: (i) that it is sufficient to expand the potential energy to quadratic order about the saddle point (and so define the saddle point

† Present address: Laboratoire de Physique des Matériaux, CNRS, 92195 Meudon, France

frequencies $\nu_{i}^{\prime}$) and (ii) that every crossing of the saddle plane represents a successful defect jump.

The unreliability of the quadratic assumption has recently been emphasised by the calculations of Sangster and Stoneham (1984) and Harding (1985a), which show that in some simple but important cases the assumption may break down entirely. However, this problem may be tackled within the spirit of the Vineyard method by integrating along the energy surface numerically, rather than by assuming a Taylor expansion.

The second assumption is of much greater interest. It expresses the fact that Vineyard's theory is a thermodynamic theory, and derives the hopping rate as the ratio of the partition functions at the saddle hypersurface and in the ground state. Such a theory can say nothing about the details of the dynamics of the hopping event. This leads us to look to the technique of molecular dynamics if we wish to investigate the adequacy or otherwise of Vineyard's assumption.

One of the first people to think in detail about this was Bennett (1975), who discussed the problems that arise in trying to use molecular dynamics in this way, and described how these problems could be overcome. (Earlier work by McCombie and Sachdev (1975) had already shown that the methods he used were feasible for one-dimensional systems.) In principle, the most direct way of using molecular dynamics to calculate a diffusion coefficient would be simply to simulate the system in thermal equilibrium, and determine the rate at which the defect hops from site to site. The problem with this method is that the activation energy $\Delta E$ is usually much greater than $k_{\mathrm{B}} T$, so that the hopping rate is much smaller than typical vibrational frequencies, often by many orders of magnitude. Almost all the time in such a direct simulation would thus be spent in the uninteresting vibrational motion, and only a tiny fraction in the hopping process itself— it is only this hopping process that is relevant to a calculation of the diffusion coefficient. Bennett (1975) showed that this process can be studied by molecular dynamics simulation by generating trajectories which start at the saddle plane, instead of arriving there by chance after many vibrations, and he gave the statistical mechanical arguments which justify this procedure. The method we shall describe later in the paper is in fact an adaptation of Bennett's work. The hopping rate can be expressed as a product of two factors: (i) the probability of finding the system at the saddle plane and (ii) the fraction of saddle-plane crossings that correspond to a successful jump. Bennett illustrated his techniques by applying them to the case of a vacancy in a Lennard-Jonesium crystal.

An alternative approach to the whole problem is seen in the work of Flynn and Jacucci (1982) (see also Jacucci 1984, Jacucci et al 1984). They used the work of Bennett and of Da Fano and Jacucci (1977) to make a distinction between the short-time dynam- ical correlation of jumps and a long-time regime where randomisation is complete and rate theory is applicable. However, they then address the problem of correcting rate theories such as Vineyard's by analysing the geometrical properties of the saddle hyper- surface. The Vineyard method defines a saddle hyperplane spanned by the eigenvectors of the saddle plane modes $\xi_{i}$. These authors then define the curved watershed saddle surface obtained by passing from the saddle point up the maximum gradient. This may be specified in terms of displacements $\zeta$ of the saddle surface normal to the saddle plane, i.e.

$$
\zeta=\zeta\left(\xi_{i}\right). \tag{3}
$$

The saddle surface and saddle plane coincide at the saddle point but not in general elsewhere. Their method then consists of evaluating the radii of curvature of the saddle surface and comparing them with the radii of curvature of possible trajectories. They

only consider U-shaped return jumps (i.e. only two cuts of the saddle surface, ignoring the possibility of three or more cuts per trajectory). They conclude that, for a simple vacancy jump in a metal, only about 5% of jumps are return jumps and so rate theory will be applicable. It should be noted that this figure of 5% applies to the *saddle surface* and not the saddle plane defined by Vineyard theory. As we shall see, the number of return jumps with respect to the latter divider can be much larger.

We believe it should be possible to use these methods to make convincing calculations for (some) real materials. However, our aim in the present work is limited to making calculations for a simple ionic model in order to show the feasibility of the molecular dynamics approach for ionic systems. The model we have used is intended to serve as a fairly realistic representation of cobalt oxide, this material being chosen because of the current interests of two of the authors.

The plan of this Paper is as follows. We first (§ 2) recall some of the ideas that are essential for the consideration of defect hopping rates. Then (§ 3) we outline some of the techniques that can be used for turning these ideas into a practical calculation. We report in § 4 the trial calculations we have done in order to try out these techniques on our model of CoO. Our conclusions are summarised in § 5.

## 2. Theoretical ideas

In spite of the importance of Bennett's work, his methods have not been widely used in defect calculations, perhaps because of a feeling that inter-atomic potentials were not well enough understood for accurate calculations of migration rates to be worthwhile. Our understanding of inter-atomic potentials, particularly in ionic materials, has greatly improved since Bennett's work was done, and it seemed to us timely to re-examine the use of molecular dynamics methods for this kind of calculation.

### 2.1. The reaction coordinate

When considering the transition of a defect between two neighbouring sites, it is con- venient to define a reaction coordinate $\xi$, which depends on the positions of the hopping atom itself and some of its neighbours. In the molecular dynamics context, it is essential that $\xi$ should depend only on the *relative* positions of the atoms (i.e. it should be unaffected by overall translations), for reasons discussed by Bennett. This means that we cannot, for example, just take $\xi$ to be the position of the hopping atom itself. It should be emphasised that the choice of $\xi$ is not unique—it is mainly a matter of convenience; the final results should be independent of this choice. In our general discussion, we shall assume $\xi$ to be of the form

$$
\xi = \sum_{i} \boldsymbol{\alpha}_{i} \cdot \boldsymbol{r}_{i} \tag{4}
$$

and it will be convenient to assume also that the vector coefficients $\boldsymbol{\alpha}_{i}$ are normalised so that

$$
\sum_{i} |\boldsymbol{\alpha}_{i}|^{2} = 1. \tag{5}
$$

Equation (4) implies that the surfaces of constant $\xi$ are planes in configuration space.

To illustrate this, let us take the hopping of vacancy in the rock-salt lattice (figure 1). Here, it is most natural to choose as the particles involved in $\xi$ the hopping ion itself

![](./images/812437160392130560_1.jpg)

Figure 1. Hopping geometry of the anion vacancy in the rock-salt lattice, showing the three ions involved in the reaction coordinate of equation (4).

together with the two ions between which it passes. We label these ions 1, 2 and 3 respectively. Then the reaction coordinate is

$$
\xi=\left(\frac{2}{3}\right)^{1 / 2}\left(\boldsymbol{r}_{1}-\frac{1}{2}\left(\boldsymbol{r}_{2}+\boldsymbol{r}_{3}\right)\right) \cdot \boldsymbol{n} \tag{6}
$$

where $\boldsymbol{n}$ is the unit vector in the hopping direction.

### 2.2. The total crossing rate

Consider the hopping of the defect between two neighbouring sites—we assume that we have for the moment introduced barriers which prevent it hopping to any other site. If we observe the system in thermal equilibrium, we shall set the defect spontaneously hopping back and forth between the sites, so that the behaviour of $\xi$ will be somewhat as shown in figure 2. Every time $\xi$ passes through the value $\xi=0$, we shall say the system makes a saddle-plane crossing. Suppose now that at some arbitrary instant $t$ we know that the system is on the left of the saddle plane: $\xi<0$. Let the probability that there is a left $\rightarrow$ right saddle-plane crossing in the ensuing interval $(t, t+\delta t)$ be called $\Gamma_{0} \delta t$. We call $\Gamma_{0}$ the total crossing rate. It should be noted that $\Gamma_{0}$ will depend on the definition adopted for $\xi$.

![](./images/812437160392130560_2.jpg)

Figure 2. Typical behaviour of the reaction coordinate in thermal equilibrium, when the defect is confined to a pair of neighbouring sites. The event at A is an unsuccessful jump.

Elementary statistical mechanics gives us an exact formula for $\Gamma_0$. Let us suppose the velocity of the reaction coordinate is $\dot{\xi}$; in order for a left $\rightarrow$ right crossing to occur, we must have $\dot{\xi} > 0$. If the crossing is to occur within a small time interval $\delta t$, we must also have, at the beginning of the interval

$$-\dot{\xi} \delta t < \xi < 0. \tag{7}$$

In full thermal equilibrium, when the system is equally likely to be on either side of the saddle plane, let the probability distribution of $\xi$ be $P(\xi)$. In this situation, the probability of finding $\xi$ in the small interval $-\delta \xi < \xi < 0$ would be $P(\xi = 0)\delta \xi$. If we know that $\dot{\xi} < 0$, then the probability is just twice this, so that from equation (7) the crossing rate is $2P(0)\dot{\xi}$. In order to get $\Gamma_0$ we have simply to replace $\dot{\xi}$ by its average $\langle \dot{\xi} \rangle$ (given that $\dot{\xi} > 0$). We are justified in doing this, since $\xi$ and $\dot{\xi}$ are uncorrelated in thermal equilibrium. It is important to stress that we are invoking an exact result here, and not making any special assumptions about 'thermalisation' during the crossing process. The probability distribution $M(\dot{\xi})$ of $\dot{\xi}$ is Maxwellian:

$$M(\dot{\xi}) = (\mu / 2\pi k_{\text{B}} T)^{1/2} \exp(-\mu \dot{\xi}^2 / 2k_{\text{B}} T) \tag{8}$$

where $\mu$ is the mass associated with the reaction coordinate (see below). Hence

$$\langle \dot{\xi} \rangle = (\mu / 2\pi k_{\text{B}} T)^{1/2} \int_{0}^{\infty} \mathrm{d} \dot{\xi} \, \dot{\xi} \exp(-\mu \dot{\xi}^2 / 2k_{\text{B}} T) = (k_{\text{B}} T / 2\pi \mu)^{1/2} \tag{9}$$

so that $\Gamma_0$ is given by

$$\Gamma_0 = 2(k_{\text{B}} T / 2\pi \mu)^{1/2} P(0). \tag{10}$$

The identity of the mass $\mu$ can be discovered by noting that the mean square value of $\dot{\xi}$ is

$$\langle \dot{\xi}^2 \rangle = k_{\text{B}} T / \mu = \sum_{ij} \langle \boldsymbol{\alpha}_i \cdot \boldsymbol{v}_i \, \boldsymbol{\alpha}_j \cdot \boldsymbol{v}_j \rangle = \sum_{i} \langle (\boldsymbol{\alpha}_i \cdot \boldsymbol{v}_i)^2 \rangle = k_{\text{B}} T \sum_{i} |\boldsymbol{\alpha}_i|^2 / m_i \tag{11}$$

so that

$$1/\mu = \sum_{i} |\boldsymbol{\alpha}_i|^2 / m_i \tag{12}$$

where $m_i$ is the mass of ion $i$; we have used the fact that the velocities of different particles are uncorrelated in thermal equilibrium.

### 2.3. The effective crossing rate

A saddle-plane crossing, as we have defined it above, is not the same thing as a jump between sites: in some cases, a crossing will be immediately followed by a reverse crossing, and the return of the defect to its original site, as we have illustrated at A in figure 2. The 'effective' crossing rate $\Gamma$, i.e. the number of *successful* jumps per unit time is therefore less than the total crossing rate $\Gamma_0$ by a factor $\langle S \rangle$ which we shall refer to as the transmission coefficient (Bennett 1975, Flynn and Jacucci 1982, Chandler 1978):

$$\Gamma = \langle S \rangle \Gamma_0. \tag{13}$$

What we have just said provides only a very loose definition of $\langle S \rangle$. One might ask, for example, how soon a reverse crossing has to occur for the jump to counted as unsuccessful. The question of giving a precise meaning to the transmission coefficient for the

case of the double-well potential has been discussed in detail by Chandler (1978), who shows that it is a characteristic property of a certain well defined correlation function. We can express his result for $\langle S\rangle$ in simple terms as follows. Take at random a left $\to$ right saddle-plane crossing. Now define a random variable $\psi(t)$, which is equal to +1 if $\xi>0$ at time $t$ after the instant of crossing and -1 if $\xi<0$. Repeating this many times, we construct the average quantity $\bar{\psi}(t)$. For $t$ infinitesimally greater than zero, $\bar{\psi}(t)$ is exactly unity, but thereafter, because of return crossings, it decays to some almost constant plateau value. The time $\tau$ it takes to decay is a measure of the time needed to complete the jump. The plateau value is only 'almost constant' because as $t$ becomes much longer than the residence time $\Gamma^{-1}$ we must have $\bar{\psi}(t) \to 0$ (in the end, the system is equally likely to be in either well). The transmission coefficient is equal to the plateau value of $\bar{\psi}(t)$:

$$
\langle S\rangle=\bar{\psi}(t) \quad \tau \ll t \ll \Gamma^{-1}. \tag{14}
$$

This formulation makes precise one's intuitive notion of successful and unsuccessful jumps: $\psi=+1$ characterises a successful jump and $\psi=-1$ an unsuccessful one.

It may be worth remarking that Chandler's formulation is not really broad enough to do full justice to the lattice defect problem, because it does not allow for the possibility of multiple jumps-correlated sequences of jumps involving more than two sites-which are known to be significant in some situations (Da Fano and Jacucci 1977, Flynn and Jacucci 1982). The formulation is clearly capable of the required extension, but we shall not need to consider this here.

## 3. Techniques

According to what we have said above, the diffusion coefficient contains two non-trivial factors, namely the saddle-plane probability $P(0)$ and the transmission coefficient $\langle S\rangle$. We now summarise the techniques we have used to calculate $P(0)$ and to estimate the significance of $\langle S\rangle$.

### 3.1. The saddle-plane probability

The difficulty with $P(0)$ is that it is exceedingly small in most cases. If this were not so, the direct calculation of the diffusion coefficient by molecular dynamics simulation would be feasible. Various approaches to the calculation of $P(0)$, in the context of solid state diffusion and in other contexts, have been suggested. One approach is based on the notion that if we write $P(\xi)$ as $\lambda^{-1} \exp \left(-f(\xi) / k_{\mathrm{B}} T\right)$, where $\lambda$ is a constant having the dimensions of $\xi$, then $f(\xi)$ plays the role of a position-dependent free energy (a potential of mean force) and can therefore be interpreted in terms of the reversible work done by external forces. From this point of view, $k_{\mathrm{B}} T \ln P(0)$ can be expressed in terms of the work needed to bring the system from the regular-site configuration to the saddle-point configuration. This work could be evaluated from a sequence of simulations with the system in external potentials of different strengths. In a second approach, described by Bennett, one obtains $P(0)$ from the distribution of $\xi$ in a sequence of systems in which $\xi$ is confined by infinite walls $\left(-\xi_{0}<\xi<\xi_{0}\right)$ of variable separation $\xi_{0}$.

We have used a third technique, which is simpler than either of the other two, in that it does not require the use of sequences of intermediate systems. This is based on the 'umbrella-sampling' method (Valleau and Whittington 1977) which has been successfully

applied to a number of problems, including the isomerisation of molecules in solution (Rebertus *et al* 1979, Berne 1985), The idea is that instead of calculating $P(0)$ directly, one calculates the related probability distribution $P'(\xi)$ for the system in an external potential, which is chosen so that $P'(\xi)$ has reasonable values in the region of $\xi = 0$. If we apply an external potential $V_{\text{ext}}(\xi)$, which depends only on $\xi$, then it is easily shown (Valleau and Whittington 1977) that the new probability distribution for $\xi$ is given by

$$
P'(\xi) = A \exp(-V_{\text{ext}}(\xi)/k_{\text{B}} T)P(\xi) \tag{15}
$$

where $A$ is a constant which is determined by the condition that the integral of $P'(\xi)$ should be equal to unity (in fact, $k_{\text{B}} T \ln A$ is the change in free energy associated with the introduction of the external potential). If we can find a $V_{\text{ext}}(\xi)$ such that $P'(\xi)$ has reasonably large values in both the saddle-plane region and the regular lattice region, then we shall be able to calculate $P'(\xi)$ by simulation and hence determine $P(\xi)$, and in particular the value $P(0)$ that we need.

How do we find a suitable $V_{\text{ext}}(\xi)$? Consider for a moment the system when it is relaxed to the configuration of minimum energy under the constraint that $\xi$ has some fixed value. Let this minimum energy be $\Delta E(\xi)$, the energy zero being chosen so that $\Delta E = 0$ for the regular site of the defect; clearly, $\Delta E(0)$ is the migration energy calculated by the usual static-relaxation method. Now think of the system in thermal equilibrium but at a low temperature. If we find the system in a configuration with a particular value of $\xi$, then, because fluctuations are small, this configuration will be very close to the minimum-energy configuration associated with that value of $\xi$. The potential of mean force $f(\xi)$ mentioned above will thus become equal to $\Delta E(\xi)$ as $T \to 0$. This means that a good choice for $V_{\text{ext}}(\xi)$ will be

$$
V_{\text{ext}}(\xi) = -\Delta E(\xi). \tag{16}
$$

It will be appreciated that this choice does not guarantee that $P'(\xi)$ will be reasonably uniform in the interesting region of $\xi$, because the $\xi$-dependent entropy associated with $f(\xi)$ might be large. Nevertheless, it seems the most sensible first guess.

### 3.2. The transmission coefficient

In order to estimate the transmission coefficient, we have to generate a set of statistically representative trajectories for the system as it crosses the barrier. Bennett and others have discussed ways of avoiding the necessity of waiting for such crossings to occur spontaneously. In the technique advocated by Bennett, one first confines the system so that $\xi$ is only allowed to vary over a narrow range about the saddle plane, namely $-\xi_{0} < \xi < \xi_{0}$. One allows the system to evolve according to the usual equations of motion, but with rigid reflecting walls representing this constraint. As usual in molecular dynamics, one allows the system to evolve for a certain time so that it settles into thermal equilibrium. Points on the trajectory can then be used as initial conditions for hopping trajectories, the walls being removed and the system being allowed to evolve without constraint. The ensemble of trajectories generated in this way is identical to the ensemble of trajectories that cross the saddle plane spontaneously in thermal equilibrium. We can therefore calculate the transmission coefficient $\langle S \rangle$ by averaging over these trajectories (14).

Bennett's method appears to work perfectly well, but is slightly more cumbersome than it really needs to be. The method we have adopted amounts essentially to shrinking the separation of the walls to zero: instead of confining the system between walls, we

constrain it to move exactly within the saddle plane $\xi=0$. This method has been described before in the literature (Chandler 1978, Rosenberg *et al* 1980) and in fact has been used by one of the present authors in calculations on thermotransport in solids (Gillan 1977, 1983). Actually, there is one important qualitative difference from Bennett's method. With the constraint $\xi=0$, the velocity of the reaction coordinate $\dot{\xi}$ is always exactly zero. This means that, in order to construct the initial conditions for the hopping trajectory, we must give $\dot{\xi}$ a random value drawn from the distribution $\tilde{M}(\dot{\xi})$ which $\dot{\xi}$ has in spontaneous crossings. This probability distribution for the value of $\dot{\xi}$ at the instant when the crossing occurs, for trajectories which spontaneously cross the saddle plane from left to right, is

$$
\tilde{M}(\dot{\xi})=\left(\mu / k_{\mathrm{B}} T\right) \dot{\xi} \exp \left(-\mu \dot{\xi}^{2} / 2 k_{\mathrm{B}} T\right)
\tag{17}
$$

(see also Bennett 1975).

The procedure is thus as follows. We allow the system to settle into thermal equilibrium with the constraint $\xi=0$. With the constraint still in operation, we then let the time evolution continue, so that we generate a constrained trajectory typical of thermal equilibrium. A sequence of configurations on this trajectory will be used as the initial conditions for unconstrained evolution, with the modification that for each initial condition $\dot{\xi}$ is given a random value drawn from the distribution $\tilde{M}(\dot{\xi})$. The set of hopping trajectories so generated is used to estimate $\langle S\rangle$.

### 3.3. Constrained molecular dynamics

In order to perform the constrained dynamical simulation just discussed, we need to modify the normal equations of motion. We can think of the constraint as being implemented by a reaction force $\boldsymbol{F}_{i}^{\text {reac }}$ acting on the particles, so that the equation of motion is

$$
m_{i} \ddot{\boldsymbol{r}}_{i}=\boldsymbol{F}_{i}=\boldsymbol{F}_{i}^{0}+\boldsymbol{F}_{i}^{\text {reac }}
\tag{18}
$$

where $\boldsymbol{F}_{i}^{0}$ is the force on particle $i$ due to the interactions with the other particles. The reaction forces, considered as a vector in configuration space, must be normal to the plane of constant $\xi$, i.e. they must be of the form

$$
\boldsymbol{F}_{i}^{\text {reac }}=f^{\text {reac }} \boldsymbol{\alpha}_{i}.
\tag{19}
$$

The multiplier $f^{\text {reac }}$ is determined by the condition that the acceleration $\ddot{\xi}$ should vanish:

$$
0=\ddot{\xi}=\sum_{i} \boldsymbol{\alpha}_{i} \cdot \ddot{\boldsymbol{r}}_{i}=\sum_{i}\left(\boldsymbol{\alpha}_{i} \cdot \boldsymbol{F}_{i}^{0}+\boldsymbol{\alpha}_{i} \boldsymbol{F}_{i}^{\text {reac }}\right) / m_{i}.
\tag{20}
$$

It follows that the reaction force for any configuration is given by

$$
f^{\text {reac }}=-\left(\sum_{i} \boldsymbol{\alpha}_{i} \cdot \boldsymbol{F}_{i}^{0} / m_{i}\right)\left(\sum_{i}\left|\boldsymbol{\alpha}_{i}\right|^{2} / m_{i}\right)^{-1}=-\mu \sum_{i} \boldsymbol{\alpha}_{i} \cdot \boldsymbol{F}_{i}^{0} / m_{i}.
\tag{21}
$$

Since the reaction force is perpendicular to the plane of motion, the energy is, of course, still conserved with this modified equation of motion, and the constrained simulation employed in constructing the saddle-plane ensemble described above is in every qualitative way the same as conventional molecular dynamics.

The usual way of initiating a molecular dynamics calculation involves giving all the particles random velocities. This will mean that the velocity $\dot{\xi}$ is not in general zero, as we must require it to be for the constrained simulation. In order to ensure that it *is* zero,

we add to the random velocities $\boldsymbol{v}_{i}$ a set of changes $\Delta \boldsymbol{v}_{i}$, which, considered as a vector in configuration space, will be taken perpendicular to the plane of constant $\xi$:

$$
\Delta \boldsymbol{v}_{i}=\Delta v \boldsymbol{\alpha}_{i}. \tag{22}
$$

Then the modified value of $\dot{\xi}$, which we wish to be zero, is

$$
0=\dot{\xi}=\sum_{i}\left(\boldsymbol{\alpha}_{i} \cdot \boldsymbol{v}_{i}+\boldsymbol{\alpha}_{i} \cdot \Delta \boldsymbol{v}_{i}\right) \tag{23}
$$

from which it follows that we must take $\Delta v$ to be equal to

$$
\Delta v=-\sum_{i} \boldsymbol{\alpha}_{i} \cdot \boldsymbol{v}_{i} \tag{24}
$$

where we have used the normalisation condition (4) on the $\boldsymbol{\alpha}_{i}$.

We note here also a point concerning the assignment of random velocities when we construct the initial conditions for the hopping trajectory. These random velocities $\Delta \boldsymbol{v}_{i}^{\text {rand }}$ must be perpendicular to the constant-$\xi$ plane:

$$
\Delta \boldsymbol{v}_{i}^{\text {rand }}=\Delta v^{\text {rand }} \boldsymbol{\alpha}_{i}. \tag{25}
$$

The value of $\Delta v^{\text {rand }}$ must, in fact, be equal to the velocity of the reaction coordinate:

$$
\dot{\xi}=\sum_{i} \boldsymbol{\alpha}_{i} \cdot \Delta \boldsymbol{v}_{i}^{\text {rand }}=\Delta v^{\text {rand }}. \tag{26}
$$

This means that, having drawn the random value of $\dot{\xi}$ from the distribution $\tilde{M}(\dot{\xi})$, we then modify the velocities by setting

$$
\boldsymbol{v}_{i} \rightarrow \boldsymbol{v}_{i}+\dot{\xi} \boldsymbol{\alpha}_{i}. \tag{27}
$$

Finally, we note that the constrained equation of motion (18) can also be used, in a damped form, to determine the $\xi$-dependent migration energy $\Delta E(\xi)$. If the system evolves according to the constrained equation of motion, but with a damping force acting on the velocities so that kinetic energy is continually extracted, it will tend to the configuration of minimum energy for the given value of $\xi$, and its energy will tend to $\Delta E(\xi)$. In practice, the damping is introduced by the well known method (Beeler and Kulcinski 1972) by which, at each time step, we calculate the scalar product $\boldsymbol{F}_{i} \cdot \boldsymbol{v}_{i}$ for each particle and, if this is negative, we set the velocity $\boldsymbol{v}_{i}$ equal to zero. This way of finding minimum-energy configurations is, of course, far less efficient than the techniques based on the Newton-Raphson method that are used in modern relaxation schemes for defect systems. It does, however, have the advantage of giving results that are uniform with the rest of the molecular-dynamics calculation.

## 4. Vacancy migration in cobalt oxide

### 4.1. The model

The simulations we have performed were made with a rigid-ion model for CoO con- taining a single anion vacancy. This rigid-ion model was derived from the shell model recently developed for this material by Stoneham and Sangster (1985). Cobalt oxide has the rock-salt structure and the hopping geometry is therefore as shown in figure 1. The inter-ionic potentials have the conventional Born-Mayer-Huggins form:

$$
V_{\alpha \beta}(r)=z_{\alpha} z_{\beta} e^{2} / r+A_{\alpha \beta} \exp \left(-r / \rho_{\alpha \beta}\right)-C_{\alpha \beta} / r^{6} \tag{28}
$$

in the usual notation, and the parameters are given in table 1.

The migration energy for the oxygen vacancy, calculated from these potentials using the HADES program (Norgett 1972, 1974a, b, Catlow and Mackrodt 1982) is 1.62 eV. This is to be compared with the value of 2.16 given by the shell model. It is of interest to examine the form of the potential energy surface in the region of the saddle point. We can do this by using HADES to calculate the fully relaxed energy $E(r)$ of the system with

<table>
<caption>Table 1. Parameters of rigid-ion potential for CoO. The parameters $A_{++}$, $C_{++}$ and $C_{--}$ are equal to zero.</caption>
<tbody>
<tr>
<td>$z_{\pm}$</td>
<td>$\pm 2$</td>
</tr>
<tr>
<td>$A_{+-}$</td>
<td>825.5 eV</td>
</tr>
<tr>
<td>$A_{--}$</td>
<td>22764.0 eV</td>
</tr>
<tr>
<td>$\rho_{+-}$</td>
<td>$0.3262\ \mathring{A}$</td>
</tr>
<tr>
<td>$\rho_{--}$</td>
<td>$0.149\ \mathring{A}$</td>
</tr>
<tr>
<td>$C_{--}$</td>
<td>$20.37\ \text{eV}\ \mathring{A}^6$</td>
</tr>
</tbody>
</table>

the hopping ion held fixed at various positions $r$ relative to the saddle point. The energy $E(r)$ along the hopping path, and in the two perpendicular directions, is shown in figure 3. It has the typical saddle-point behaviour envisaged in Vineyard theory, and there is every indication that this theory should yield a reasonable prediction of the hopping rate. This situation should be contrasted with the non-Vineyard-like behaviour found by Sangster and Stoneham (1984) for cation diffusion in MgO.

![](./images/812437160392130560_3.jpg)

Figure 3. The relaxed energy $E(r)$ for the oxygen vacancy in CoO when the hopping anion is fixed at position $r$, measured in units of the cation-anion distance, relative to the saddle point. The hopping direction is $\langle 110\rangle$. A, $\langle 1\overline{1}0\rangle$; B, $\langle 001\rangle$; C, $\langle 110\rangle$.

Our molecular dynamics simulations have all been made for a system of 32 cations and 31 anions in the normal periodically repeating geometry with a cubic repeat unit. Recent studies on the calculation of defect entropies (Gillan and Jacobs 1983, Harding 1985b) suggest that the system may not be large enough to give accurate results; however, it should certainly be large enough for testing techniques, which is out present concern. The reaction coordinate $\xi$ used in the calculations is defined as in equation (6).

### 4.2. Energy along the migration path

Our first test of the molecular dynamics method was to calculate the relaxed energy for a fixed reaction coordinate, using the constrained equation of motion with damping described in $\S$ 3.3. The calculation of $\Delta E(\xi)$ for fixed $\xi$ should give the same result as that of $E(\boldsymbol{r})$ for fixed $\boldsymbol{r}$, provided, of course, that we make the appropriate correspondence between $\xi$ and $\boldsymbol{r}$ (the HADES minimisation for fixed $\boldsymbol{r}$ along the hopping path yields a certain value of $\xi$). We show the comparison of the molecular dynamics and HADES

![](./images/812437160392130560_4.jpg)

Figure 4. The relaxed energy $\Delta E(\xi)$ along the migration path calculated for the rigid-ion model of CoO by HADES (full curve) and by damped molecular dynamics (broken curve).

results for $\Delta E(\xi)$ in figure 4. The agreement between the two not only confirms the correctness of the molecular dynamics technique, but indicates that our system of 63 ions is at least giving the *energetics* of the migration correctly.

### 4.3. The total crossing rate

We have used unconstrained molecular dynamics with an external potential $V_{\text{ext}}(\xi)$ to evaluate the saddle-plane probability and hence the total crossing rate, as described in $\S\S$ 2.2 and 3.1. We have set $V_{\text{ext}}(\xi)$ equal to $-\Delta E(\xi)$, using for this the numerical results from the molecular dynamics relaxation we have just described. In order to provide a simple representation for $\Delta E(\xi)$, we have specified it on a mesh of points spanning the range between the stable sites, and we have used linear interpolation between each pair of points. This entails discontinuities in the external force, but these do not appear to have a detrimental effect on the simulation.

In order to obtain the probability distribution $P'(\xi)$ for the system in the external potential, we divide the range over which $\xi$ varies into a uniform grid and at each time step determine the segment in which $\xi$ falls; this enables us to accumulate a histogram for the distribution of $\xi$. Since we know that $P'(\xi)$ is an even function of $\xi$, we can improve the statistics by taking the average of $P'(\xi)$ and $P'(-\xi)$.

![](./images/812437160392130560_5.jpg)

Figure 5. Results for the probability distributions $P'(\xi)$ and $P(\xi)$ for the system with and without the external potential at the temperaure 1368 K.

Calculations of $P'(\xi)$, and hence $P(\xi)$, have been made at four temperatures spanning the range 995-1760 K. We present in figure 5 numerical results for $P'(\xi)$ obtained from a run of 1500 steps (time step $=5 \times 10^{-15} \mathrm{~s}$) at the temperature $1368 \mathrm{~K}$, and the resulting distribution $P(\xi)$ for the system in the absence of $V_{\text {ext }}$ calculated according to equation (15). From this, we get a numerical estimate for the saddle-plane probability, which for this temperature is $P(0)=1.6 \times 10^{-6} \AA^{-1}$. Table 2 shows the results for $P(0)$ for the four temperatures examined.

Table 2. Simulation results for the saddle-plane probability $P(0)$, the transmission coefficient $\langle S\rangle$ (numbers of successful and unsuccessful crossings $n_{+}$and $n_{-}$), the effective crossing rate $\Gamma$ and the frequency prefactor $\bar{\nu}$ at four temperatures.

<table>
<thead>
<tr>
<th>$T(\mathrm{~K})$</th>
<th>$P(0)\left(\AA^{-1}\right)$</th>
<th>$n_{+}$</th>
<th>$n_{-}$</th>
<th>$\langle S\rangle$</th>
<th>$\Gamma\left(\mathrm{s}^{-1}\right)$</th>
<th>$\bar{\nu}\left(10^{12} \mathrm{~s}^{-1}\right)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>995</td>
<td>$9.6 × 10^{-9}$</td>
<td>52</td>
<td>24</td>
<td>0.37</td>
<td>$1.8 × 10^{4}$</td>
<td>5.2</td>
</tr>
<tr>
<td>1368</td>
<td>$1.6 × 10^{-6}$</td>
<td>52</td>
<td>27</td>
<td>0.32</td>
<td>$3.0 × 10^{6}$</td>
<td>4.2</td>
</tr>
<tr>
<td>1520</td>
<td>$7.8 × 10^{-6}$</td>
<td>60</td>
<td>18</td>
<td>0.54</td>
<td>$2.6 × 10^{7}$</td>
<td>8.8</td>
</tr>
<tr>
<td>1760</td>
<td>$2.3 × 10^{-5}$</td>
<td>48</td>
<td>24</td>
<td>0.33</td>
<td>$5.0 × 10^{7}$</td>
<td>3.0</td>
</tr>
</tbody>
</table>

### 4.4. The transmission coefficient

To get an estimate for $\langle S\rangle$, we have generated a series of hopping trajectories for each of the four temperatures, using the method outlined in $\S 3.2$. The time evolution of $\xi$ on a selection of these trajectories for $T=1368 \mathrm{~K}$ is shown in figure 6. We see that most of

![](./images/812437160392130560_6.jpg)

Figure 6. Time evolution of the reaction coordinate $\xi$ for a selection of the hopping trajectories at $1368 \mathrm{~K}$; the broken lines show the values of $\xi$ for the equilibrium positions of the vacancy.

the saddle-plane crossings do represent successful jumps. However, there are three cases here in which the velocity $\xi$ is reversed and the system recrosses the saddle plane; in addition, there is a more complicated jump, which appears to be successful after two crossings. Table 2 gives the numbers of successful and unsuccessful crossings and the estimated value of $\langle S\rangle$ for the four temperatures, together with the results for the effective crossing rate $\Gamma$. For the purpose of comparing with the Vineyard theory, it is convenient to express $\Gamma$ in terms of the frequency prefactor $\bar{\nu}$ using (2). Our results for $\bar{\nu}$ obtained using the value for $\Delta E_{m}$ given by molecular dynamics relaxation are listed in table 2. There is no consistent variation of these results with temperature, and the spread of values must be ascribed to inadequate statistics, mainly in the calculation of $\langle S\rangle$.

### 4.5. Comparison with Vineyard theory
The theory of Vineyard gives the expression for the prefactor $\bar{\nu}$ discussed in $\S 1$. Calculations with the SHEOL program developed by one of the present authors (Harding 1985a, b) show that, with the CoO model we are using, there is only a single unstable mode at the saddle point, so that there is no difficulty in evaluating this expression. We have made SHEOL calculations of $\bar{\nu}$ using our rigid-ion potential, which yield the numerical result $\bar{\nu}=1.4 \times 10^{13} \mathrm{~s}^{-1}$, in qualitative agreement with the value we obtained from the molecular dynamics simulation.

## 5. Discussion
The calculations we have described show that it is possible to calculate defect migration rates for models of important real materials without making the approximations of the usual Vineyard theory. For the particular model we have studied, the results we have described suggest that the Vineyard theory is qualitatively correct, though it appears to overestimate the migration rate by about a factor of three. In the way we have presented the calculation, it seems that the main reason for this is that a substantial number of saddle-plane crossings represent unsuccessful jumps. Indeed, our total crossing rate $\Gamma_{0}$, is numerically very close to the Vineyard crossing rate. However, it should be borne in mind that $\Gamma_{0}$ and the transmission coefficient $\langle S\rangle$ individually depend on the definition of the reaction coordinate $\xi$, though their product $\Gamma$ does not. It might be, then, that with a different $\xi$ the fraction of successful crossings would be much closer to unity, and the total crossing rate would be lower than the Vineyard value.

Recent work of DeLorenzi and Jacucci (1986) has compared a lattice dynamics calculation of the hopping rate in a Lennard-Jones solid with the molecular dynamics results of Bennett (1975). They used a periodic repeating-cell method to calculate the prefactor rather than the large crystallite method used in the SHEOL program. They conclude from their work that the lattice dynamics result may be too low by a factor of 2-15. This factor is in the opposite sense to that reported here. Further, the result is counterintuitive since, if the lattice dynamics calculation overcounts the hopping events by counting return jumps, one might expect the lattice dynamics results to be too high, as we have found. However, matters are not quite so simple. A molecular dynamics calculation not only describes the hopping trajectories correctly, but also includes anharmonic effects that a lattice dynamics calculation ignores. Before accepting this explanation, however, one should ask whether the calculations of Bennett and DeLorenzi and Jacucci are strictly comparable. The calculations of Bennet where done

using a 255-atom repeating cell whereas the larger cell size used by DeLorenzi and Jacucci was 108 sites. They claim that the dependence of the result on the number of sites used is small, but our experience (Gillan and Jacobs 1983, Harding 1985b, Leslie 1985) shows that the calculated values of the prefactors can depend strongly on the number of sites considered for all methods of calculation (Green function, large crys- tallite and periodic cell). We are therefore cautious about accepting claims (or indeed claiming ourselves) that it has been conclusively shown that the lattice dynamics method gives an overestimate or an underestimate of the true hopping rate. What is important, and what both our calculations and those of DeLorenzi and Jacucci show, is that for important systems the rate theory may be expected to be an acceptable method of predicting absolute diffusion rates to within an order of magnitude. It is in any case doubtful whether such methods are capable of doing better than that owing to the problems of obtaining adequate inter-ionic potentials and adequate convergence of the calculation (especially of the energy calculation).

In this paper we have only considered calculations at the level of the harmonic approximation. The methods discussed here could be applied to check the quasi-har- monic calculations of diffusion rates that have been performed. Here DeLorenzi and Jacucci have done some work on Lennard-Jones solids. The investigation of the approxi- mation for ionic solids would be of considerable interest.

© 1987 UKAEA.

## References

Beeler J R Jr and Kulcinski G L 1972 *Interatomic Potentials and Simulation of Lattice Defects* ed. P C Gehlen and J R Beeler (New York: Plenum)

Bennett C H 1975 *Diffusion in Solids: Recent Developments* ed. J J Burton and A S Nowick (New York: Academic)

Berne B J 1985 in *Multiple Time Scales* ed. J U Brackbill and B I Cohen (New York: Academic)

Catlow C R A and Mackrodt W C 1982 *Computer Simulation of Solids* ed. C R A Catlow and W C Mackrodt (New York: Springer)

Chandler D 1978 *J. Chem. Phys.* **68** 2959

Da Fano A and Jacucci G 1977 *Phys. Rev. Lett.* **39** 950

DeLorenzi G and Jacucci G 1986 *Phys. Rev.* **B33** 1993

Flynn C P and Jacucci G 1982 *Phys. Rev.* **B25** 6225

Gillan M J 1977 *J. Phys. C: Solid State Phys.* **10** 1641
—— 1983 *Proc. Nato Advanced Study Institute Mass Transport in Solids (Lannion) 1981* (New York: Plenum)

Gillan M J and Jacobs P W M 1983 *Phys. Rev.* **B28** 759

Harding J H 1985a *Physica B* **131** 13
—— 1985b *Phys. Rev.* **B32** 6861

Jacucci G 1984 *Diffusion in Crystalline Solids* ed. G E Murch and A S Nowick (New York: Academic)

Jacucci G, Toller M, DeLorenzi G and Flynn C P 1984 *Mater. Sci. Forum* **1** 187

Leslie M 1985 unpublished

McCombie C W and Sachdev M 1975 *J. Phys. C: Solid State Phys.* **8** L413

Norgett M J 1972 *Harwell Report* R 7015
—— 1974a *Harwell Report* R 7650
—— 1974b *Harwell Report* R 7780

Rebertus D, Berne B J and Chandler D 1979 *J. Chem. Phys.* **70** 3395

Rosenberg R O, Berne B J and Chandler D 1980 *Chem. Phys. Lett.* **75** 162

Sangster M J L and Stoneham A M 1984 *J. Phys. C: Solid State Phys.* **17** 6093

Stoneham A M and Sangster M J L 1985 *Phil. Mag.* B **52** 717

Valleau J P and Whittington S G 1977 *Statistical Mechanics Part A*, ed. B J Berne (New York: Plenum) p 137

Vineyard G H 1957 *J. Phys. Chem. Solids* **3** 121

Vineyard G H and Krumhansl J A 1985 *Phys. Rev.* B **31** 4929