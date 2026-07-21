# Formation of finger-like step patterns on a Si(111) vicinal face

Masahide Sato $^{a, *}$, Shinji Kondo $^{b}$, Makio Uwaha $^{b}$

$^{a}$ Information Media Center, Kanazawa University, Kakuma-cho, Kanazawa 920-1192, Japan
$^{b}$ Department of Physics, Nagoya University, Chikusa-ku, Nagoya 464-8602, Japan

---

## A R T I C L E  I N F O

Available online 26 October 2010

**Keywords:**
A1. Crystal morphology
A1. Growth model
A1. Surfaces

---

## A B S T R A C T

During deposition of Ga atoms, the structure of a Si(111) vicinal face is transformed from the $\sqrt{3} \times \sqrt{3}$ structure to the $6.3 \times 6.3$ structure. The transformation occurs preferentially from the lower side of steps. Since the density of Si atoms needed to form the $6.3 \times 6.3$ structure is lower than that to form the $\sqrt{3} \times \sqrt{3}$ structure, Si atoms are supplied onto the surface during the structural transition. The steps advance by incorporating the extra adatoms, and show a finger-like wandering pattern (H. Hibino, H. Kageshima, M. Uwaha, Surf. Sci. 602 (2008) 2421). To study the formation of the finger-like pattern, we carry out Monte Carlo simulations. When atoms are supplied immediately in front of a straight step, the step becomes unstable. Step wandering occurs and a step shows a finger-like pattern. The characteristic period of the fingers is consistent with the linear stability analysis and proportional to $(\tilde{\beta}/V)^{1/2}$, where $\tilde{\beta}$ is the step stiffness and $V$ is the step velocity (deposition rate).

© 2010 Elsevier B.V. All rights reserved.

---

## 1. Introduction

In equilibrium, steps on a crystal surface are straight with small thermal fluctuation along the step, but during growth, the straight steps sometimes become unstable and wander. It is called step wandering. The step wandering is caused by an asymmetry of the surface diffusion field. One of the causes to induce the asymmetry is the Erlich-Schwoebel (ES) effect [1–6]. If a large potential barrier is present at the step edge, adatoms attach to the step from the lower side terrace more easily than from the upper side. Owing to the asymmetry of the step kinetics, the surface diffusion field becomes asymmetric, and wandering of the advancing steps occurs. The ES effect is believed to induce the step wandering on $Cu(1,1,17)$ during homoepitaxial growth [7].

When Ga atoms are deposited on a Si(111) vicinal face at $580\ ^{\circ}\text{C}$, the $7 \times 7$ structure is first transformed to the $\sqrt{3} \times \sqrt{3}$ structure. With more deposition of Ga atoms, the structural transition from the $\sqrt{3} \times \sqrt{3}$ structure to the $6.3 \times 6.3$ structure occurs [8–11]. Since the density of Si atoms in the top layer to form the $\sqrt{3} \times \sqrt{3}$ structure is higher than that to form the $6.3 \times 6.3$ structure, Si atoms are released onto the surface during the structural transition. The released atoms are incorporated into steps and the steps advance. Since the transition from the $\sqrt{3} \times \sqrt{3}$ structure to the $6.3 \times 6.3$ structure mainly occurs immediately in front of steps. The incorporation of Si atoms from the lower side of a step is more than that from the upper side. The asymmetry causes wandering of advancing steps, and a step shows a finger-like pattern [11].

The finger-like wandering pattern is very different from that predicted in previous studies [4–6,12,13]. When evaporation of adatoms is present, the motion of a wandering step is described by the Kuramoto–Sivashinsky equation. The amplitude of step wandering is saturated, and the wandering step shows a chaotic behavior [4,5,12]. When evaporation of atoms is neglected, the motion of steps is described by another type of nonlinear equation whose solution shows a regular pattern [6,13]. When the wavelength of the step pattern is longer than the terrace width, grooves perpendicular to the steps are formed. The formation of the grooves is observed on some vicinal faces [7,14–16]. In the case of step wandering on a Si(111)vicinal face during Ga deposition [11], the wandering pattern is regular. The typical width of the finger-like branches is, however, much smaller than the terrace width and grooves are not formed. In the previous study [11], the formation of finger-like branches is attributed to the phase boundary immediately in front of the step, but this hypothesis has not been confirmed yet.

In this paper, to study step wandering on a Si(111) vicinal face during deposition of Ga atoms, we perform Monte Carlo simulation. In Section 2, we introduce a lattice model for Monte Carlo simulation. In the simulation, we confirm the formation of branches and find an effect of the crystal anisotropy of steps. In Section 3, we carry out a linear stability analysis to determine the characteristic length of the pattern and compare the results with the simulation. In Section 4, we give a brief summary.

## 2. Model of simulation

For simplicity, we use a square lattice to investigate the motion of a single step. We take the lattice constant $a$ as the length unit in

---

* Corresponding author.
E-mail address: sato@cs.s.kanazawa-u.ac.jp (M. Sato).

0022-0248/$- see front matter © 2010 Elsevier B.V. All rights reserved.
doi:10.1016/j.jcrysgro.2010.10.093

the simulation. Initially, the step is straight. It is parallel to the x-direction and advances to the y-direction. The periodic boundary condition is used in the x-direction. Since the phase boundary between the $6.3 \times 6.3$ and the $\sqrt{3} \times \sqrt{3}$ structures, which acts as the source of adatoms, is located immediately in front of the step [11], incorporation of atoms to the step mainly occurs from the lower side. Thus, we place a linear source of adatoms in front of the step. Diffusion of adatoms from the phase boundary will induce a wandering instability.

In our simulation, active atoms are adatoms and solid atoms at the step edge, which we call step atoms. In a Monte Carlo trial, we choose one of the active atoms. When a chosen atom is an adatom, a diffusion trial is carried out. We choose one of the nearest neighbor sites with the probability 1/4. When the chosen site is empty, the adatom moves to the site. The increase of time for a diffusion trial is set as $\Delta t=1/(4N_{\mathrm{g}})$, where $N_{\mathrm{g}}$ is the number of adatoms, to make the diffusion coefficient unity. If the adatom is attached to a step atom after the diffusion trial, a solidification trial is successively carried out.

When a chosen atom is a step atom, a melting trial is carried out. The solidification probability $p_{+}$ and the melting probability $p_{-}$ are given by [5]

$$
p_{\pm}=\left[1+\exp\left(\frac{\Delta E \mp \phi}{k_{\mathrm{B}} T}\right)\right]^{-1}, \tag{1}
$$

where $\phi$ is the chemical potential gain by solidification and $\Delta E=\epsilon \times$ (increment of step perimeter) is the increment of step energy by solidification. The equilibrium adatom density $c_{\mathrm{eq}}^{0}$ is given by

$$
c_{\mathrm{eq}}^{0}=\exp\left(-\frac{\phi}{k_{\mathrm{B}} T}\right). \tag{2}
$$

In the experiment [11], during the formation of finger-like branches, the phase boundary seems straight and the top of the intruding step appears to follow the phase boundary. Thus, to mimic this behavior, we keep the distance between the top of intruding part and the straight phase boundary constant at the value $l$ by shifting the position of the straight phase boundary every several diffusion trials. In the simulation, the phase boundary is represented by a thin buffer layer of a constant adatom density $c_{0}$.

We use two types of steps, a [01] step and a [11] step in the simulation. The step stiffness of the [01] step, $\tilde{\beta}_{[01]}$ and that of the [11] step, $\tilde{\beta}_{[11]}$ are given by [5]

$$
\tilde{\beta}_{[01]}=\frac{2k_{\mathrm{B}} T}{a}\sinh^{2}\frac{\epsilon}{2k_{\mathrm{B}} T}, \tag{3}
$$

$$
\tilde{\beta}_{[11]}=\frac{\sqrt{2}k_{\mathrm{B}} T}{a}\left[1+\cosh^{2}\frac{\epsilon}{k_{\mathrm{B}} T}\right]^{-1}\sinh^{2}\frac{\epsilon}{k_{\mathrm{B}} T}. \tag{4}
$$

![](./images/811709311771213826_1.jpg)

Fig. 1. Snapshots of (a) a [01] step and (b) a [11] step.

Fig. 1 shows snapshots of finger-like branches. The system size in the $x$ direction, $L_{x}$, is 1024 (Note that we put $a=1$ in the simulation). The size in the $y$-direction is expanded with growth of branches. The initial step position is $y=10$. We use $\phi/k_{\mathrm{B}} T=3.0$ so that $c_{\mathrm{eq}}^{0}$ is $4.98 \times 10^{-2}$. The distance $l$ is 3 and the adatom density in the buffer layer $c_{0}$ is 0.15. The blue area, the red lines and the green dots represent solid atoms, step edge atoms and adatoms, respectively. The adatom density is high around the top of branches and approaches the equilibrium value around the lower part.

Many branches appear in an initial stage. Tall branches obtain many adatoms and grow faster than short branches. Since the short branches can hardly grow, the distance between branches increases during growth. In Fig. 1, the bonding energy $\epsilon/k_{\mathrm{B}} T$ is 2.0, and the step stiffnesses $\tilde{\beta}_{[01]}/k_{\mathrm{B}} T$ and $\tilde{\beta}_{[11]}/k_{\mathrm{B}} T$ are estimated to be 2.76 and 1.23, respectively. Since a bump of a step grows more easily into the direction of a small stiffness, branches tend to grow into $<11>$ directions. As a result, a branch in [11] direction has few side branches, and a branch in [01] direction develops many branching in the tilted directions.

## 3. Linear stability analysis and initial branch formation

To study the characteristic length of wandering, we perform a linear stability analysis. We consider a straight step moving steadily at the velocity $V_{0}$. In the frame of reference moving with the step, the diffusion equation of adatom density is given by

$$
\frac{\partial c(\boldsymbol{r})}{\partial t}-V_{0}\frac{\partial c(\boldsymbol{r})}{\partial y}=D_{\mathrm{s}}\nabla^{2}c(\boldsymbol{r}), \tag{5}
$$

where $D_{\mathrm{s}}$ is the diffusion coefficient. We assume that solidification and melting of atoms at the step is so fast that the adatom density is in equilibrium with the steps:

$$
c|_{y=\zeta(x,t)-V_{0}t}=c_{\mathrm{eq}}, \tag{6}
$$

where $\zeta(x,t)$ represents the step position in the frame of the crystal. The equilibrium adatom density $c_{\mathrm{eq}}$ is expressed as

$$
c_{\mathrm{eq}}=c_{\mathrm{eq}}^{0}\left(1+\frac{\Omega \tilde{\beta}}{k_{\mathrm{B}} T}\kappa\right), \tag{7}
$$

where $\Omega$ is the atomic area ($\Omega=a^{2}=1$ in the simulation), $\tilde{\beta}$ is the stiffness and $\kappa$ is the curvature of the step. In the simulation, the diffusion field exists in $0 \leq y \leq l$, but, for simplicity, we consider the diffusion field in the region $0 \leq y$. To realize the steady state of the straight step, the boundary condition at $y \to \infty$ should satisfy

$$
c|_{y \to \infty} \to \Omega^{-1}. \tag{8}
$$

By solving the diffusion equation, Eq. (5) with boundary conditions, Eqs. (6) and (8), we obtain the step velocity $V_{\mathrm{n}}$ as
$$
\left(\Omega^{-1}-c_{\mathrm{eq}}\right) \Omega V_{\mathrm{n}}=\left.\hat{\boldsymbol{n}} \cdot \Omega D_{\mathrm{s}} \nabla c\right|_{y=\zeta(x, t)-V_{0} t},\qquad(9)
$$
where $\hat{\boldsymbol{n}}$ is the unit vector normal to the step. When the step moves at the velocity $V_{0}$, the distribution of adatom density $c^{(0)}(y)$ is given by
$$
c^{(0)}(y)=-\left(\Omega^{-1}-c_{\mathrm{eq}}^{0}\right) \mathrm{e}^{-V_{0} y / D_{\mathrm{s}}}+\Omega^{-1}.\qquad(10)
$$

In our simulation, the adatom density at $y=-l$ is kept constant, $c(l)=c_{0}$. Then, the step velocity $V_{0}$ and the diffusion length $l_{\mathrm{D}}$ are related to $c_{0}$ and $l$ as
$$
V_{0} \equiv \frac{D_{\mathrm{s}}}{l_{\mathrm{D}}}=-\frac{D_{\mathrm{s}}}{l} \ln \frac{1-\Omega c_{0}}{1-\Omega c_{\mathrm{eq}}^{0}}.\qquad(11)
$$

We give a small perturbation to the steady solution. The step position and the distribution of adatom density are expressed as
$$
\zeta(x, t)=V_{0} t+\delta \zeta \mathrm{e}^{\mathrm{i} q x+\omega_{q} t},\qquad(12)
$$

$$
c(x, y, t)=c^{(0)}(y)+\delta c_{1} \mathrm{e}^{\mathrm{i} q x-\Lambda_{q} y+\omega_{q} t},\qquad(13)
$$
where $q$ and $\Lambda_{q}$ are the wavenumbers parallel and perpendicular to the step, and $\omega_{q}$ is the amplification rate of the perturbation. By solving the diffusion equation with the boundary conditions, the adatom density is determined and the amplification rate $\omega_{q}$ is obtained as
$$
\frac{\omega_{q}}{D_{\mathrm{s}}}=\left(\frac{V_{0}}{D_{\mathrm{s}}}-\frac{\Gamma q^{2}}{\Omega^{-1}-c_{\mathrm{eq}}^{0}}\right)\left[|q| \sqrt{1+\frac{1}{4}\left(\frac{\Gamma q}{\Omega^{-1}-c_{\mathrm{eq}}^{0}}\right)^{2}}-\frac{1}{2} \frac{\Gamma q^{2}}{\Omega^{-1}-c_{\mathrm{eq}}^{0}}\right],\qquad(14)
$$
where $\Gamma=c_{\mathrm{eq}}^{0} \Omega \tilde{\beta} / k_{\mathrm{B}} T$. The second factor of the amplification rate (14) is positive, and the first factor determines the sign. With a small $q$, the amplification rate $\omega_{q}$ is positive and the step is unstable with the fluctuation. For long wavelength modes $(\Omega \Gamma q \ll 1)$, the amplification rate is approximated as
$$
\frac{\omega_{q}}{D_{\mathrm{s}}}=|q|\left(\frac{V_{0}}{D_{\mathrm{s}}}-\frac{\Gamma q^{2}}{\Omega^{-1}-c_{\mathrm{eq}}^{0}}\right).\qquad(15)
$$

The wavelength $\lambda_{\max }$ of the most unstable mode, in which $\omega_{q}$ becomes the largest, is given by
$$
\lambda_{\max }=2 \pi \sqrt{\frac{3 \Omega^{2} \tilde{\beta} c_{\mathrm{eq}}^{0} l_{\mathrm{D}}}{k_{\mathrm{B}} T\left(1-\Omega c_{\mathrm{eq}}^{0}\right)}}.\qquad(16)
$$

In Eq. (16), the factor $l_{\mathrm{D}} /\left(1-\Omega c_{\mathrm{eq}}^{0}\right)$ may be approximated by $l / \Omega\left(c_{0}-c_{\mathrm{eq}}^{0}\right)$ in terms of the parameters used in the simulation.

If the formation of branches is controlled by the linear instability scenario, the characteristic wavelength in the initial stage of the formation of branches should be given by the wavelength of the most unstable mode, Eq. (16). Thus, we need to investigate the initial stage of simulation in more detail. In an early stage, fluctuation in the position of the top of branches is too large in the present algorithm, and we modify the model to obtain the data as follows. We keep the distance between the average height of the step, instead of the top height, and the phase boundary constant. The initial adatom distribution is adjusted to satisfy the steady state solution.

Fig. 2 shows snapshots of a [01] step in an early stage. The blue line shows the system size in the $y$-direction. The pink line represents the position of average height. The adatom density between the blue line and the red line is kept $c_{0}$. We count the number $N$ of branches which cross the pink line at $y=30$, and estimate the characteristic wavelength $\lambda^{*}$ as $\lambda^{*}=L_{x} / N$. The number $N$ is 33 in (a), 27 in (b) and 29 in (c), giving $\lambda^{*}=31$ and 38, and 35. The three conditions in Fig. 2 all correspond to $l_{\mathrm{D}}=90$, and $\lambda_{\max }$ calculated from Eq. (16) is 39. The observed wavelengths $\lambda^{*}$ are slightly shorter than $\lambda_{\max }$.

We carry out simulation with various parameters and compare the data with the linear stability analysis. Fig. 3 shows the dependence of $\lambda^{*}$ on $\tilde{\beta}$ with various values of $c_{0}$ and $l$, which correspond to $l_{\mathrm{D}}=269$ or $V_{0}=3.71 \times 10^{-3}$. The changed parameters of the simulation are $\epsilon, c_{0}$ and $l$, while $\phi$ and $T$ are kept constant. The data in an early stage are measured when the average height $y$ is 30 or 50, and averaged over 50 runs. The characteristic

![](./images/811709311771213826_2.jpg)

Fig. 2. Formation of branches in an early stage with a [01] step. The adatom density in the buffer layer and the distance $l$ are (a) $c_{0}=0.24$ and $l=20$, (b) $c_{0}=0.32$ and $l=30$ and (c) $c_{0}=0.46$ and $l=50$. Other parameters are the same as those in Fig. 1.

![](./images/811709311771213826_3.jpg)

Fig. 3. The dependence of $\lambda^{*}$ on $\tilde{\beta}$ with various values of $c_{0}$ and $l$. The data in the initial stage with $c_{0}=0.15,0.24,0.32,0.39$ and 0.46 are plotted with red circles, blue squares, green triangles, circles with dot and diamonds, respectively. The data in the late stage with $c_{0}=0.15,0.24,0.32$ are plotted with open circles, open squares and open triangles, respectively. The dotted lines are $\lambda \propto \tilde{\beta}^{1 / 2}$ (The red dotted line shows $\lambda_{\max }$ given by Eq. (16)). The system size $l$ is so chosen that $l_{\mathrm{D}}=269$. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](./images/811709311771213826_4.jpg)

Fig. 4. Dependence of $\lambda^{*}$ on $V_{0}$. The marks are the same as those in Fig. 3. The step stiffness is $\tilde{\beta}/k_{B}T=2.76$.

wavelength $\lambda^{*}$ in the initial stage is slightly shorter than $\lambda_{\text{max}}$ given by Eq. (16) as $\lambda^{*}=0.9\lambda_{\text{max}}$. The $\lambda^{*}$ in a late stage, where the finger-like pattern appears, is measured at $y = 700, 750, ..., 1000$, and the minimum value is adopted for each sample. The data are averaged over 10 runs. The change of $\lambda^{*}$ with large stiffness seems consistent with $\lambda^{*} \propto \tilde{\beta}^{1/2}$, but the value is about 2.5 times larger than $\lambda_{\text{max}}$ of the linear stability analysis. With small stiffness, $\lambda^{*}$ in the late stage appears independent of $\tilde{\beta}$.

Fig. 4 shows the dependence of $\lambda^{*}$ on $V_{0}$. For a given $V_{0}$, we use various values of $c_{0}$ and $l$, and the step stiffness is kept constant. All data show that the result does not depend on $c_{0}$ and $l$, and the relevant quantity is only the diffusion length $l_{D}$ in this parameter range. The characteristic wavelength $\lambda^{*}$ in both early and late stages decreases with the velocity as $\lambda^{*} \propto V_{0}^{-1/2}$, in agreement with the linear instability analysis. The characteristic wavelength $\lambda^{*}$ is slightly shorter than $\lambda_{\text{max}}$ in the early stage ($\lambda^{*}=0.9\lambda_{\text{max}}$), but about 2.5 times larger in the late stage.

## 4. Summary and discussion

In order to study the step wandering of a Ga-deposited Si(111) vicinal face, we carried out Monte Carlo simulation using a lattice model with a step and a straight phase boundary. When the straight source of adatoms in front of the step moves with the top of the step, finger-like branches are formed. The shape of branches changes as the anisotropy of a step. The main branch of a [11] step is straighter than that of a [01] step. More side branches are formed in the [01] step than in the [11] step. In the experiment [11], the branches are straight and have few side branches. They are similar to the [11] step in the simulation.

In our simulation, the characteristic wavelength $\lambda^{*}$ is proportional to $\lambda_{\text{max}}$ and depends on $\tilde{\beta}$ and $V_{0}$ as $\lambda^{*} \sim (\tilde{\beta}/V_{0})^{1/2}$. In an early stage, $\lambda^{*} \approx \lambda_{\text{max}}$, and the step behavior is controlled by linear instability. In the late stage, tall branches get more adatoms and move faster than short ones. The short branches stop growing and vanish by thermal relaxation. Thus, the distance between branches becomes longer as they grow. In the experiment [11], the wavelength is proportional to $V^{-1/2}$, in agreement with our results.

In our simulation, we have assumed that the phase boundary moves at the same velocity as the top of branches. The velocity of the top determines the velocity of the phase boundary. In the experiment [11], however, motion of the phase boundary must be determined by the Ga deposition rate and the velocity of phase boundary is the controlling parameter. Now we have made a new model with a steadily moving source. Since there is not any steady solution with a straight step in the new model, the linear stability analysis is not possible. Careful study of the relation to the present model is under way.

## Acknowledgment

This work is supported by Grants-in-Aid for Scientific Research from Japan Society for the Promotion of Science.

## References

[1] G. Ehrlich, F.G. Hudda, J. Chem. Phys. 44 (1966) 1039.
[2] R.L. Schwoebel, E.J. Shipsey, J. Appl. Phys. 37 (1966) 3682.
[3] G.S. Bales, A. Zangwill, Phys. Rev. B 41 (1990) 5500.
[4] I. Bena, C. Misbah, A. Valance, Phys. Rev. B 47 (1993) 7408.
[5] Y. Saito, M. Uwaha, Phys. Rev. B 49 (1994) 10677.
[6] O. Pierre-Louis, C. Misbah, Y. Saito, J. Krug, P. Politi, Phys. Rev. Lett. 80 (1998) 4221.
[7] T. Maroutian, L. Douillard, H.-J. Ernst, Phys. Rev. Lett. 83 (1999) 4353.
[8] J. Zegenhagen, M.S. Hybertsen, P.E. Freeland, J.R. Patel, Phys. Rev. B 38 (1998) 7885.
[9] D.M. Chen, J.A. Golovchenko, P. Bedrossian, K. Mortensen, Phys. Rev. Lett. 61 (1988) 2867.
[10] J.R. Patel, J. Zegenhagen, P.E. Freeland, M.S. Hybertsen, J.A. Golovchenko, D.M. Chen, J. Vac. Sci. Technol. B 7 (1989) 894.
[11] H. Hibino, H. Kageshima, M. Uwaha, Surf. Sci. 602 (2008) 2421.
[12] M. Sato, M. Uwaha, J. Phys. Soc. Jpn. 65 (1996) 2146.
[13] M. Sato, M. Uwaha, Y. Saito, Y. Hirose, Phys. Rev. B 67 (2003) 125408.
[14] M. Degawa, H. Nishimura, Y. Tanishiro, H. Minoda, K. Yagi, Jpn. J. Appl. Phys. 38 (1999) L308.
[15] J.-F. Nielsen, M.S. Pettersen, J.P. Pelz, Surf. Sci. 480 (2001) 84.
[16] H. Hibino, Y. Homma, M. Uwaha, T. Ogino, Surf. Sci. 527 (2003) L222.