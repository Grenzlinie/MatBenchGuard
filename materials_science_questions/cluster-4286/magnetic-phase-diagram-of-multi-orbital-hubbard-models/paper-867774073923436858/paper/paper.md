# Competition of Spinon Fermi Surface and Heavy Fermi Liquids states from the Periodic Anderson to the Hubbard model

Chuan Chen, $^{1}$ Inti Sodemann, $^{1, *}$ and Patrick A. Lee $^{2, \dagger}$

$^{1}$ Max-Planck Institute for the Physics of Complex Systems, 01187 Dresden, Germany
$^{2}$ Department of Physics, Massachusetts Institute of Technology, Cambridge Massachusetts 02139, USA

(Dated: February 25, 2021)

We study a model of correlated electrons coupled by tunnelling to a layer of itinerant metallic electrons, which allows to interpolate from a frustrated limit favorable to spin liquid states to a Kondo-lattice limit favorable to interlayer coherent heavy metallic states. We study the competition of the spinon fermi surface state and the interlayer coherent heavy Kondo metal that appears with increasing tunnelling. Employing a slave rotor mean-field approach, we obtain a phase diagram and describe two regimes where the spin liquid state is destroyed by weak interlayer tunnelling, (i) the Kondo limit in which the correlated electrons can be viewed as localized spin moments and (ii) near the Mott metal-insulator-transition where the spinon Fermi surface transitions continuously into a Fermi liquid. We study the shape of LDOS spectra of the putative spin liquid layer in the heavy Fermi liquid phase and describe the temperature dependence of its width arising from quasiparticle interactions and disorder effects throughout this phase diagram, in an effort to understand recent STM experiments of the candidate spin liquid 1T-TaSe₂ residing on metallic 1H-TaSe₂. Comparison of the shape and temperature dependence of the theoretical LDOS suggest that this system is either close to the localized Kondo limit, or in an intermediate coupling regime where the Kondo coupling and the Heisenberg exchange interaction are comparable.

## I. INTRODUCTION

Since the pioneering proposal by Anderson [1–3], there has been an extensive quest to find quantum spin liquids (QSL) in materials [4–6]. Recently, it has been suggested that certain layered transition metal dichalcogenide compounds might harbour a QSL state [7, 8]. In particular, 1T-TaS₂, a material that undergoes a commensurate charge density wave transition around 200 K into a $\sqrt{13} \times \sqrt{13}$ star of David structure [9, 10], remains insulating to the lowest temperatures in spite of having an odd number of electrons per star of David supercell, and yet shows no sign of any further conventional ordering phase transition such as antiferromagnetism that would double the unit cell, to the lowest measurable temperatures [11]. A possible connection to Anderson’s proposal of a spin liquid was actually made from the very beginning [12], but somehow forgotten. The magnetic susceptibility of this compound remains nearly constant at low temperatures [13] and the material displays a finite linear in temperature specific heat coefficient [14] indicative of a finite density of states at low energies. Earlier experiments found no linear in temperature heat conductivity [15], which was taken as evidence against itinerant carriers. However, more recent experiments have shown a delicate sensitivity of heat transport to impurities [16], finding a finite linear in temperature heat conductivity in the cleanest samples. This indicates the presence of a finite density of states of itinerant carriers, as expected for the spinon Fermi surface state. Moreover, band structure analysis [17] showed that a single narrow band crosses the Fermi energy and is separated from other bands, making it very likely that the low energy electronic behaviour can be described by a single band Hubbard model.

A closely related compound, 1T-TaSe₂, which also undergoes a commensurate charge density wave transition into the star of David structure, is expected to display similar phenomenology. While bulk 1T-TaSe₂ is metallic [18] , monolayer 1T-TaSe₂ was studied by STM and found to be a Mott insulator [19]. Recently Crommie and co-workers [20] extended their study by placing a monolayer of 1T-TaSe₂ on top of a 1H-TaSe₂ monolayer, which is metallic. Surprinsingly their experiment has found that a Kondo-like resonance peak near the Fermi energy develops in the tunnelling density of states. It is important to emphasize that in these experiments the tunnelling tip is coupled primarily to the originally insulating top layer of 1T-TaSe₂. Therefore, taken at face value, the appearance of a tunnelling density of states peak near zero bias may imply the destruction of the presumed spin liquid that would exist for 1T-TaSe₂ in isolation and the formation of a coherent metallic state by the coupling with the substrate metallic 1H-TaSe₂, as it would be expected the classic problem of Kondo heavy metal formation.

These experimental findings motivate us to consider a model consisting of a layer of correlated electrons coupled to a layer of non-interacting itinerant electrons via tunnelling to study the competition of spinon Fermi surface states and the heavy Kondo metals. There are two questions that we would like to address. First, the experimentalists found an excellent fit of the lineshape and its temperature dependence with that expected for the Kondo resonance of a single impurity Kondo problem [20]. On the other hand, the actual system consists of a periodic array of local moments. Even if these are in the Kondo

* Correspondence to: sodemann@pks.mpg.de
† Correspondence to: palee@mit.edu

limit, the low temperature state is expected to be a heavy Fermion metal. Would the formation of a narrow coher- ent band lead to observable changes in the local density of states (LDOS)? Second, how does the Heisenberg ex- change coupling $J_H$ between the local moments compete with the Kondo coupling $J_K$ that operates between the local moments and the conducting substrate? This prob- lem was considered by Doniach [21] for the case when the Heisenberg coupling leads to an antiferromagnetic state. His conclusion is that the two relevant competing energy scales are the Kondo temperature $T_K$ and the Heisen- berg exchange scale $J_H$. Note that at weak coupling $T_K$ is exponential small in terms of the Kondo coupling $J_K$. This would suggest that a very weak $J_H$ is sufficient to destroy the Kondo effect. If the experiment was inter- preted as being in the Kondo limit, this places a rather small upper bound on $J_H$ of about 50K, since the scale $T_K$ is estimated to be about 50K from the experimental fit [20]. With such a small Heisenberg coupling, the in- terpretation of the monolayer 1T-TaSe₂ as a spin liquid is brought into question. We note that the situation may change when the coupling becomes strong, and it may also change in frustrated spin models where the spin liq- uid state may be favored over the anti-ferromagnet. No- tice that in the resonating valence bond (RVB) picture, the quantum spin liquid is viewed as the superposition of singlet formed between local moment pairs, while the Kondo phenomenon arises from the singlet formation be- tween the local moment and the conduction electron spin. The competition between different ways of forming sin- glets may well be different from the competition with an anti-ferromagnet considered by Doniach. With this in mind, we will consider a model that is sufficently gen- eral to include the Hubbard interaction $(U)$ for the cor related electrons that reside in the putative spin liquid layer, which hop with an amplitude $(t_d)$ within this layer, and a tunnelling amplitude $(V)$ to the itinerant electrons residing in the putative metallic layer, which hop with an amplitude $(t_c)$ within their own layer, as dipicted in Fig. 1. This model therefore interpolates naturally be- tween the periodic Anderson model $(t_d \to 0)$ where it would capture the physics of the formation of the inter- layer coherent heavy Kondo metal [22, 23] and the pure Hubbard limit $(V \to 0)$ where it would capture the tra ditional scenario for the appearance of the spinon Fermi surface state near the Mott transition [24–26]. We note in passing that this model has been recently employed to understand ARPES spectra in PdCrO₂ [27], however, in this material the insulating layers are believed to be strong Mott insulators with $120^\circ$ spin anti-ferromagnetic order.

One of the central quantities of our interest will be the LDOS of the putative spin liquid layer, which is what has been measured in the aforementioned STM experi- ments. We are particularly interested in understanding the temperature dependence of the width of the LDOS peak, which can be used to try to learn about the mi- croscopic parameters of the putative spin liquid and its coupling to the metal, and can guide us in determining where the system is likely to lie in the parameter space of our Hubbard-Anderson periodic model. Although an unambiguous quantitative description of the temperature dependence is challenging because it is controlled by the interplay of intrinsic quasi-particle lifetimes and extrin- sic effects such as disorder induced broadening, we believe that our modelling is consistent with the system to be ei- ther close to the periodic Anderson model limit or in an intermediate coupling regime where the Kondo coupling and the Heisenberg exchange interaction are comparable, as we will discuss in detail. In the latter case, we cannot extract a tight bound on $J_H$ based on the experimental data.

Our paper is organized as follows: Section II sets up the model and describes the mean-field slave rotor ap- proach that we employ to tackle it. Section III presents the solution of this mean field under a wide range of pa- rameters, including not only the interplay between spinon Fermi surface and heavy metal but also the possibility of competing with Kondo insulating states. Section IV is devoted to a detailed analysis of the LDOS spectra and temperature dependence of the LDOS width and the comparison with STM experiments. Section V summa- rizes and further discusses our main findings. We have relegated some of the technical details of the mean-field treatment to Appendix A. In Appendix B we revisit the classic result of the temperature dependence of the sin- gle impurity Anderson model and give a more thorough derivation of the width of the Kondo resonance.

## II. MODEL AND SLAVE ROTOR APPROACH

We consider a model of two-species of fermions residing in a triangular lattice that interpolates naturally between the Hubbard model and the periodic Anderson model. The microscopic Hamiltonian of the system has the form:

$$
\begin{aligned}
H= & -t_{d} \sum_{\langle i, j\rangle, \sigma} d_{i, \sigma}^{\dagger} d_{j, \sigma}+\sum_{i} n_{d, i}\left(\epsilon_{d}^{(0)}-\mu_{F}\right) \\
& -t_{c} \sum_{\langle i, j\rangle, \sigma} c_{i, \sigma}^{\dagger} c_{j, \sigma}+\sum_{i} n_{c, i}\left(\epsilon_{c}^{(0)}-\mu_{F}\right) \\
& +\frac{U}{2} \sum_{i}\left(n_{d, i}-1\right)^{2}-V \sum_{i, \sigma}\left(c_{i, \sigma}^{\dagger} d_{i, \sigma}+h. c.\right).
\end{aligned} \quad (1)
$$

Here the electrons created by $c^{\dagger}$ are viewed as the "itin erant", and those created by $d^{\dagger}$ as the correlated ones. A schematic of the system is shown in Fig. 1. In the limit in which the correlated electrons are localized, $t_d=0$, this model reduces to the Periodic Anderson model, and in the limit in which the two specifies are decoupled, $V=0$, the Hamiltonian for the correlated electrons reduces to the Hubbard model. We would like to employ a formal- ism capable of handling the various regimes of this model, and in particular the single occupancy constraints that appear in the large $U$ limit. For this purpose we resort to the slave rotor mean-field approach. According to the

![](./images/867774073923436858_1.jpg)

FIG. 1. Schematic of the model. The electrons in the top layer (blue) are correlated, with nearest neighbour hopping $t_d$ and an on-site Hubbard interaction $U$. The bottom layer (red) hosts itinerant electrons with nearest neighbour hopping $t_c$. There is also an inter-layer tunneling $V$.

slave rotor method [24, 28], the $d$-electron can be represented by a bosonic rotor, $\theta_i$, and a fermionic spinon $f_{i,\sigma}$ degrees of freedom: $d_{i,\sigma}\equiv e^{i\theta_i}f_{i,\sigma}$, with the constrain $n_{\theta,i}+n_{f,i}=1$. The Hamiltonian can be then written in terms of these partons as follows:

$$
\begin{aligned}
H= & -t_{d} \sum_{\langle i, j\rangle, \sigma} e^{-i \theta_{i}} e^{i \theta_{j}} f_{i, \sigma}^{\dagger} f_{j, \sigma}+\sum_{i} n_{f, i}\left(\epsilon_{d}^{(0)}-\mu_{F}\right) \\
& -t_{c} \sum_{\langle i, j\rangle, \sigma} c_{i, \sigma}^{\dagger} c_{j, \sigma}+\sum_{i} n_{c, i}\left(\epsilon_{c}^{(0)}-\mu_{F}\right) \\
& +\frac{U}{2} \sum_{i} n_{\theta, i}^{2}-V \sum_{i, \sigma}\left(e^{i \theta_{i}} c_{i, \sigma}^{\dagger} f_{i, \sigma}+h . c .\right).
\end{aligned}
\tag{2}
$$

### A. Mean-field theory

In the spirit of a mean-field theory we approximate the ground state of Eq. (2) by a direct product of a rotor state and a spinon state. The constrain on the rotor and spinon occupation is satisfied on average:

$$
\left\langle n_{\theta, i}\right\rangle+\left\langle n_{f, i}\right\rangle=1.
\tag{3}
$$

Since the rotor and spinon degrees of freedom are assumed to be disentangled, we write the mean-field Hamiltonian as the sum of a rotor part and a fermionic part, i.e., $H_{\mathrm{mf}}=H_{f}+H_{\theta}$, with

$$
\begin{aligned}
H_{f}= & -T_{f} \sum_{\langle i, j\rangle, \sigma} f_{i, \sigma}^{\dagger} f_{j, \sigma}+\sum_{i} n_{f, i}\left(\epsilon_{d}^{(0)}+\lambda-\mu_{F}\right) \\
& -t_{c} \sum_{\langle i, j\rangle, \sigma} c_{i, \sigma}^{\dagger} c_{j, \sigma}+\sum_{i} n_{c, i}\left(\epsilon_{c}^{(0)}-\mu_{F}\right) \\
& -V_{f} \sum_{i, \sigma} c_{i, \sigma}^{\dagger} f_{i, \sigma}+h . c .,
\end{aligned}
\tag{4a}
$$

$$
H_{\theta}=-2 \sum_{\langle i, j\rangle} T_{\theta} e^{-i \theta_{i}} e^{i \theta_{j}}+\sum_{i} \frac{U}{2} n_{\theta, i}^{2}+\lambda n_{\theta, i}-4 V_{\theta} \cos \left(\theta_{i}\right),
\tag{4b}
$$

$$
T_{f}=t_{d}\left\langle e^{-i \theta_{i}} e^{i \theta_{j}}\right\rangle_{\theta},
\tag{4c}
$$

$$
V_{f}=V\left\langle e^{i \theta_{i}}\right\rangle_{\theta},
\tag{4d}
$$

$$
T_{\theta}=t_{d}\left\langle f_{i, \sigma}^{\dagger} f_{j, \sigma}\right\rangle_{f},
\tag{4e}
$$

$$
V_{\theta}=V\left\langle c_{i, \sigma}^{\dagger} f_{i, \sigma}\right\rangle_{f},
\tag{4f}
$$

here a Lagrange multiplier $\lambda$ is introduced to maintain the constrain Eq. (3). The quasiparticle residue of correlated $d$ electron is $\langle e^{i \theta_{i}}\rangle \equiv \Phi$. This can be regarded as the order parameter for the metallic phase: when it is non-zero there will be a coherent tunnelling between the spinon and itinerant electrons. In this work, we will concentrate on the competition of this correlated metallic state and a more exotic state, known as the spinon Fermi surface state, that arises when $\Phi=0$ and the spinon, $f$, has a Fermi surface.

We expect that the essence of the competition between these phases does not depend substantially on the details of the fermion dispersions, and therefore, in order to simplify analytical treatment, we will approximate the band structure for spinons $(f)$ and itinerant electrons $(c)$ by simple parabolic bands:

$$
\begin{aligned}
H_{f}=\sum_{k, \sigma} f_{k, \sigma}^{\dagger} f_{k, \sigma} \epsilon_{f, k}+c_{k, \sigma}^{\dagger} c_{k, \sigma} \epsilon_{c, k}-V_{f}\left(c_{k, \sigma}^{\dagger} f_{k, \sigma}+h . c .\right),
\end{aligned}
\tag{5a}
$$

$$
\epsilon_{f, k}=\frac{3}{2} T_{f}\left(k^{2}-\frac{\Lambda^{2}}{2}\right)+\lambda-\mu_{F},
\tag{5b}
$$

$$
\epsilon_{c, k}=\frac{3}{2} t_{c}\left(k^{2}-\xi \frac{\Lambda^{2}}{2}\right)-\mu_{F},
\tag{5c}
$$

here $\Lambda$ is a cut-off on $k$-space intended to mimic the finite size of the Brillouin zone which can be determined by equalling $\pi \Lambda^{2}$ to the area of triangular lattice's Brillouin zone, the lattice constant $a_{0}$ is taken to be 1. The dimensionless parameter $\xi$ in $\epsilon_{c, k}$ reflects the occupancy of $c$ electrons when $c$ and $f$ fermions are decoupled (since in such case $\lambda=0$ and $\mu_{F}=0$, see discussions in the following section): the number of $c$ electron per site is $\xi$ when the dispersion $\epsilon_{c, k}$ is particle $(t_{c}>0)$, and $2-\xi$ with hole like dispersion $(t_{c}<0)$. See Fig. 2 for a schematic illustration.

### B. Expectation values of the rotor operators

Notice that even after the mean field decoupling, the rotor Hamiltonian $H_\theta$ is still essentially a $2D$ quantum XY model with a transverse field which is not amenable to analytic treatment. Therefore, one has to make further approximations.

We are interested in solutions that respect time- reversal and translational symmetry and that have no flux per unit cell. Therefore we seek for self-consistent solutions where $\Phi$ is uniform and real. To do so, we perform an additional self-consistent mean-field treatment of $H_\theta$ by introducing an effective single-site rotor Hamiltonian:
$$
H_{\theta}^{(1)}=-K_{\theta}\left(e^{i \theta}+e^{-i \theta}\right)+\frac{U}{2} n_{\theta}^{2}+\lambda n_{\theta}, \tag{6a}
$$
$$
K_{\theta}=2 z T_{\theta} \Phi+2 V_{\theta}, \tag{6b}
$$
with $z$ being the lattice coordination ($z=6$ for triangular lattice). To lowest order in perturbation theory in $K_\theta/U$ ($\lambda=0$ since we are interested in half-filled spinon and the constrain Eq. (3) leads to $\langle n_{\theta,i}\rangle=0$) we have $\Phi = 4K_\theta/U$. On the other hand, in the opposite limit in which $K_\theta/U \gg 1$, we have $\theta \approx 0$ and thus $\Phi=\langle e^{i\theta}\rangle=1$. Moreover, since $\Phi=\langle e^{i\theta}\rangle$ is never greater than one, we introduce the following natural interpolation between these limits:
$$
\Phi=\frac{K_{\theta}}{\sqrt{(U / 4)^{2}+K_{\theta}^{2}}}, \tag{7}
$$
or equivalently,
$$
K_{\theta}=\frac{U}{4} \frac{\left\langle e^{i \theta}\right\rangle}{\sqrt{1-\left\langle e^{i \theta}\right\rangle^{2}}}, \tag{8}
$$

Although the above mean field treatment captures well the behavior of the residue $\Phi$, it ignores completely the nearest neighbour rotor correlations, which are essential in order to obtain a dispersion for the spinon. To capture these, and since $V_\theta$ is small near the metal to insulator phase transition, we will approximate their value by performing a perturbative calculation directly with the more complete rotor Hamiltonian $H_\theta$ from Eq. (4b), which contains the $U$ and $T_\theta$ terms only,
$$
\tilde{H}_{\theta}=\frac{U}{2} \sum_{i} n_{\theta, i}^{2}-2 T_{\theta} \sum_{\langle i, j\rangle} e^{-i \theta_{i}} e^{i \theta_{j}}, \tag{9}
$$
which leads to the following nearest neighbor rotor correlations:
$$
\left\langle e^{-i \theta_{i}} e^{i \theta_{j}}\right\rangle \approx \frac{4 T_{\theta}}{U}, \tag{10}
$$
it should be noted that these nearest-neighbor rotor correlations from Eq. (10) are needed to reproduce the spinon bandwidth which is expected to be given by the Heisenberg exchange coupling scale $J_H=4t_d^2/U$. The expressions above are all zero temperature results. The finite temperature version of these formulae are discussed in Appendix A.

### C. Expectation values of the fermion operators

The fermionic mean-field Hamiltonian is free from interactions and can be diagonalized exactly. Because we are already accounting for spinon hopping in the spin liquid phase at $V=0$, the correlator $\langle f_{i,\sigma}^{\dagger} f_{j,\sigma}\rangle$ is not expected to change much during the spin-liquid to heavy-metal phase transition, so we will simply approximate its value when $c$ and $f$ fermions are decoupled from each other ($V_f=0$ in the insulating phase):
$$
\left\langle f_{i, \sigma}^{\dagger} f_{j, \sigma}\right\rangle=\frac{1}{N} \sum_{k} e^{i \vec{k} \cdot \vec{\delta}} n_{F}\left(\epsilon_{f, k}\right) \equiv \chi_{0}, \tag{11}
$$
with $n_F$ being the Fermi-Dirac distribution function: $n_F(x)=1/(e^{\beta x}+1)$, $\delta$ is the distance between sites $i$ and $j$, and $N$ is the total number of lattice sites in Eq. (11). thus $T_{\theta}=t_{d} \chi_{0}$. As for the hybridization between the itinerant electrons and spinons, one obtains:
$$
\left\langle c_{i, \sigma}^{\dagger} f_{i, \sigma}\right\rangle=V_{f} \chi_{c f}, \tag{12a}
$$
$$
\chi_{c f}=-\frac{1}{2 N} \sum_{k} \frac{n_{F}\left(E_{1, k}\right)-n_{F}\left(E_{2, k}\right)}{\sqrt{\left(\frac{\epsilon_{f, k}-\epsilon_{c, k}}{2}\right)^{2}+V_{f}^{2}}}. \tag{12b}
$$

It should be noted that Eq. (12a) is an exact result of solving the free fermionic Hamiltonian $H_f$, although in the $V_f \to 0$ limit, the $\chi_{cf}$ reduces to the $c$-$f$ hybridization susceptibility of the $c$-$f$ decoupled Hamiltonian. The quasi-particle energy dispersions read (see Fig. 2):
$$
E_{1 / 2, k}=\frac{\epsilon_{f, k}+\epsilon_{c, k}}{2} \pm \sqrt{\left(\frac{\epsilon_{f, k}-\epsilon_{c, k}}{2}\right)^{2}+V_{f}^{2}}, \tag{13}
$$
and the occupancy of spinon reads:
$$
\left\langle f_{i, \sigma}^{\dagger} f_{i, \sigma}\right\rangle=\frac{1}{N} \sum_{k} \cos ^{2}\left(\alpha_{k}\right) n_{F}\left(E_{1, k}\right)+\sin ^{2}\left(\alpha_{k}\right) n_{F}\left(E_{2, k}\right), \tag{14a}
$$
$$
\cos \left(2 \alpha_{k}\right)=\frac{\epsilon_{f, k}-\epsilon_{c, k}}{2} / \sqrt{\left(\frac{\epsilon_{f, k}-\epsilon_{c, k}}{2}\right)^{2}+V_{f}^{2}}, \tag{14b}
$$

### D. Self-consistent equations

Once the expressions for the expectation values of the rotor and fermions are obtained, the self-consistent equations for the order parameter $\Phi$ can be derived, from Eqs. (6b), (8) and (12a), one can show that:
$$
\frac{\Phi}{8}\left(\frac{1}{\sqrt{1-\Phi^{2}}}-8 z \frac{t_{d}}{U} \chi_{0}\right)=\Phi \frac{V^{2}}{U} \chi_{c f}. \tag{15}
$$

Therefore, one needs to solve Eq. (15) along with the constrain Eq. (3) and $\langle n_{f,i}\rangle=1$. Eq. (15) always has a trivial solution $\Phi=\langle e^{i\theta_i}\rangle=0$, and the non-trivial solution of $\langle e^{i\theta_i}\rangle$ satisfies:
$$
\frac{1}{8}\left(\frac{1}{\sqrt{1-\Phi^{2}}}-8 z \frac{t_{d}}{U} \chi_{0}\right)=\frac{V^{2}}{U} \chi_{c f}. \tag{16}
$$

![](./images/867774073923436858_2.jpg)

FIG. 2. Schematic of the band dispersion. (a) Particle- particle dispersion (with $\xi>1$). Blue solid lines indicate the $\epsilon_{f, k}$ and $\epsilon_{c, k}$ in the spin liquid phase; green dashed lines stand for the $E_{1, k}$ and $E_{2, k}$ for small $V_{f}$ , where both bands cross the Fermi level and there are two Fermi surfaces; the orange dashed lines are when $V_{f}$ is large such, so that the $E_{2, k}$ band is fully occupied and $E_{1, k}$ is partly occupied to maintain the half filling of the spinon. (b) Particle-hole dispersion $(\xi<1)$ . For small $V_{f}$ (green dashed line) only $E_{1, k}$ crosses the Fermi level and has two Fermi surfaces while the $E_{2, k}$ is fully occupied; when $V_{f}$ is large enough (orange dashed lines) there is only one Fermi surface.

It should be noted that the "susceptibility" $\chi_{c f}$ also depends on $\Phi$ , through its dependence on $V_{f}$ in Eq. (12b), which in turn depends on $\Phi$ via Eq. (4d).

## III. MEAN-FIELD PHASE DIAGRAM AND MEAN-FIELD PROPERTIES.

To explore the phase transition between the spin liquid and heavy metal phases, it is important to distinguish the cases with the band dispersions of the $d$-electron and itinerant electrons being particle-particle like $(t_{d}>0$ and $t_{c}>0)$ and particle-hole like $(t_{d}>0$ and $t_{c}<0)$ . Here we discuss in detail the behavior when the itinerantfermion has higher density (larger Fermi surface area) than the spinon, which is most relevant to the recent ex- periments $1 ~T-TaS_{2}$ and $1 ~T-TaSe_{2}$ . Namely we will take the paramter $\xi$ , that controls the density of the itiner ant electrons in Eq. (5c), to have a range of $1 \leq \xi<2$ for the particle-particle case and $0 \leq \xi<1$ for the particle-hole case (this leads to $n_{c} \geq n_{f}$ in the insulating phase), see Fig. 2 for an illustration.

### A. Particle-particle dispersion

In this section we discuss the situation for particle- particle like dispersions. As mentioned before, there are two competing phases in our phase diagram: the spin liq- uid phase and the heavy metal phase (see Fig. 5 for an ex- ample of the phase diagram). The phases are determined by whether order parameter $\Phi$ is finite (heavy metal) or zero (spin liquid). When $t_{d} \sim 0$ , the model reduces to a periodic Anderson model and the transition from spin liquid to heavy metal is of the form of a weak coupling instability. On the other hand, for larger $t_{d} / U \sim 1 / 8$ and V =0, the system exhibits a metal-insulator (Mott) tran- sition, as one expects from a Hubbard model. The goal of next section is to determine how the phase boundary evolves between these two regimes.

### 1. Phase boundary

The phase boundary is obtained when $\Phi=0$ is a solution of Eq. (16). According to the constraint from Eq. (3) and $\langle n_{f, i}\rangle=1$ , we have that $\langle n_{\theta, i}\rangle=0$ . This leads to a value $\lambda=0$ for the Lagrange multiplier in Eq. (4b). Thus one just needs to self-consistently adjust the chemical potential $\mu_{F}$ such that the spinon is half-filled. Along the phase boundary, since $c$ and $f$ fermions are de coupled, this can be satisfied by setting $\mu_{F}=0$ , which leads to $n_{f, i}=1$ and $n_{c, i}=\xi$ , which corresponds to two Fermi surfaces from the two bands with Fermi momen- tum $k_{F, f}=\Lambda / \sqrt{2}$ and $k_{F, c}=\Lambda \sqrt{\xi / 2}$ . In this case the susceptibility of $c-f$ coupling from Eq. (12b), reduces to:

$$
\begin{aligned}
\chi_{c f}^{(0)} & =-\frac{1}{N} \sum_{k} \frac{n_{F}\left(\epsilon_{f, k}\right)-n_{F}\left(\epsilon_{c, k}\right)}{\epsilon_{f, k}-\epsilon_{c, k}} \\
& =\frac{1}{\Lambda^{2}} \frac{2}{3} \frac{1}{T_{f}-t_{c}} \ln \left(\frac{T_{f}}{t_{c}}\right).
\end{aligned}\quad (17)
$$

It is interesting to notice that the $\chi_{c f}^{(0)}$ is independent of $\xi$ ; in other words, the density of itinerant electrons. This implies that the phase boundary is insensitive to the $c$ electron's density within the parabolic band approxima- tion. The critical value at which the residue $\Phi$ and the hibridization between the itinerant and correlated elec-tron, $V_{f}$ , become simultaneously non-zero is given by:

$$
\frac{V_{c}^{2}}{U t_{c}}=\frac{1}{8}\left(1-8 z \frac{t_{d}}{U} \chi_{0}\right)\left(\frac{4 t_{d}^{2} \chi_{0}}{U t_{c}}-1\right) \frac{\frac{3}{2} \Lambda^{2}}{\ln \left(\frac{4 t_{d}^{2} \chi_{0}}{t_{c} U}\right)}.\quad (18)
$$

A plot of the phase boundary in this case can be found in Fig. 3(a). As it approaches the Anderson $(t_{d} \to 0)$ limit, the critical $V_{c}^{2} / U$ has a logarithmic dependence on $t_{d} / U$ . This means that in the local moment limit, the heavy Fermi liquid phase is destabilized by a weak Heisen- berg coupling, $J_{H} \sim t_{d}^{2} / U$ , comparable to the Kondo scale, $T_{K} \sim \rho^{-1} e^{-1 / J_{K} \rho}$ (with $J_{K} \sim V^{2} / U$ and $\rho^{-1} \sim t_{c}$ ). This is responsible for the sharp narrowing of the region of the Heavy Fermi liquid phase in the local moment limit $V^{2} \ll t_{c} U$ , and $t_{d} \ll U$ , as shown in Fig. 3(a). Around the axis $V=0$ we recover the physics of the spin-liquid to metal (Mott transition) in the conventional Hub- bard model with the spin-liquid to metal transition (see Ref. [24]) occurring at $t_{d} / U=1 /(8 z \chi_{0})$ , which in the case of the triangular lattice corresponds to $t_{d} / U \sim 1 / 8$ and is in line with previous cluster mean-field calculation [28].

![](./images/867774073923436858_3.jpg)

FIG. 3. (a) Phase boundary between spin liquid (below blue curve) and heavy metal with particle-particle dispersion and $\xi$=1.2. As $t_d \to 0$, the critical coupling $V_c^2/U$ is suppressed logarithmically with $t_d/U$; when $V$=0 (horizontal axis), the metal-insulator transition occurs at $t_d/U$ ~ 1/8. Near this critical point, the $V_c^2/U$ has a linear dependence on $t_d/U$. (b) Plot of the $\chi_{cf}$ with $T_f$=0.1$t_c$. $\chi_{cf}$ saturates at small $V_f$, while for $V_f > V_f^*$, it is a decreasing function of $V_f$.

### 2. Turning on of the heavy fermion phase

As one enters the heavy fermion metallic phase ($\Phi$ becomes finite), both the $E_{1,k}$ and $E_{2,k}$ bands cross the Fermi level (as indicated by the green dashed lines in Fig. 2(a)). According to Eq. (14a), the spinon density in this case is:
$$
\langle f_{i,\sigma}^{\dagger} f_{i,\sigma} \rangle = \frac{k_{F1}^2 + k_{F2}^2}{2\Lambda^2} + \frac{\sum_{\alpha=c,f} \epsilon_{\alpha,k_{F1}} + \epsilon_{\alpha,k_{F2}}}{3\Lambda^2(t_c - T_f)}, \tag{19}
$$

$$
\langle f_{i,\sigma}^{\dagger} f_{i,\sigma} \rangle = \frac{k_{F1}^2 + \Lambda^2}{2\Lambda^2} + \frac{\epsilon_{f,k_{F1}} + \epsilon_{c,k_{F1}} + \sqrt{(\epsilon_{f,\Lambda} - \epsilon_{c,\Lambda})^2 + 4V_f^2}}{3\Lambda^2(t_c - T_f)}, \tag{21}
$$

and the $\mu_F$ can be determined by requiring $\langle f_{i,\sigma}^{\dagger} f_{i,\sigma} \rangle =1/2$. In this case the susceptibility $\chi_{cf}$ is no longer independent of $V_f$ (we do not show the explicit expression here since it is too lengthy). Fig. 3(b) shows a plot the $\chi_{cf}$ as a function of $V_f$ for a specific parameterization. As mentioned before, a finite $t_d$ sets a "cut-off" to the $\chi_{cf}$, moreover, the critical $V_f^*$ will also decrease as $t_d$ decreases. This role of $t_d$ as a cutoff of the $\chi_{cf}$ susceptibility leads to an increasing value of the critical $V$ as $t_d$ increases at extremely small values of $t_d$, as shown in Fig. 3(a). In other words, the larger the value of $t_d$ the smaller the susceptibility to induce the mixing between the itinerant and correlated fermions.

However, the physical role of $t_d$ is not exclusively to cutoff $\chi_{cf}$. It is clear from the Fig. 3(a) that at sufficiently large $t_d$ the critical $V$ starts to decrease as $t_d$ increases. The other physical role of $t_d$ can be understood from the self-consistent equation for the residue $\Phi$, by requiring this to be 1/2, one can obtain $\mu_F$=0 (with $\lambda$=0). It can be shown that in this case, the susceptibility is simply a constant:
$$
\chi_{cf} = \frac{2}{3} \frac{1}{t_c \Lambda^2} \frac{1}{\frac{4t_d^2 \chi_0}{U t_c} - 1} \ln\left( \frac{4t_d^2 \chi_0}{U t_c} \right). \tag{20}
$$

Notice that $\chi_{cf}$ is independent of $V_f$ (or $\Phi$), which is a consequence of the parabolic model. Physically $\chi_{cf}$ should be a monotonically decreasing function of $V_f$ for a general band dispersion, but we conclude from the above that it is weakly dependent on these parameters whenever the bands can be approximated by parabolas. Nevertheless, Eq. (20) still unveils an important effect of the correlated fermion hopping $t_d$, which is to set a "cut-off" to $\chi_{cf}$, as depicted in Fig. 3(b). Such cut-off would otherwise be absent in the pure periodic Anderson model ($t_d \to 0$) and we would have that $\chi_{cf} \to \infty$ as $V_f \to 0$. This divergence is responsible for the weak-coupling (Kondo) instability of the periodic Anderson model that leads to the formation of the heavy Fermi liquid state.

On the other hand, there is a further phase transition that appears within the heavy Fermi liquid state, associated with the disappearance of one of the Fermi surfaces while preserving the net Luttinger volume, at large $V_f$. This occurs when $V_f$ is larger than some critical value $V_f^* = \frac{3}{2} \frac{\Lambda^2}{2} \sqrt{T_f t_c (2 - \xi)}$, for which we have that $E_{2,\Lambda} <0$, so the $E_{2,k}$ band is fully occupied and there is only one Fermi surface associated with the band $E_{1,k}$ (see yellow dashed lines in Fig. 2(a))). In this case, the density of spinon reads:

Eq. (16), where we see that the hopping of correlated electrons $t_d$ appears not only inside $\chi_{cf}$, but also on the left hand side of the equation, arising from the coupling between nearest neighbour rotors in $H_\theta$ ($t_d e^{-i\theta_i} e^{i\theta_j}$). This term competes with the interaction part ($\sim U n_{\theta,i}^2$) and tends to "lock" the angles of nearby rotors, therefore, in this second role, $t_d$ tends to enhance the appearance of a residue and therefore favors the destruction of the spin liquid in favor of the appearance of the finite $\Phi$ leading to a metallic state.

To illustrate more concretely these contrasting roles of $t_d$ we compare the solution of $\Phi$ as a function of $V^2/U$ for different types of *modified* self-consistent equations. As shown by the dashed curves in Fig. 4, when the susceptibility $\chi_{cf}$ is replaced by one which diverges logarithmically at small $V_f$ (dashed lines), there is always a weak-coupling instability to the heavy fermion phase, while for the exact $\chi_{cf}$ (solid lines), one has to reach a

finite critical value of $V$ for the occurrence of the heavy metal phase. Moreover, when the linear $t_d$ terms from the left hand side of Eq. (16) is removed (blue lines), the heavy metal phase is also suppressed and one needs a larger $V$ to get a non-zero $\Phi$.

From the analysis above, one can see that either a very large $t_d$ (nearby rotors lock strongly) or a very small $t_d$ (susceptibility of the $c$-$f$ coupling diverges) will en- hance the tendency towards heavy Fermi liquid order and suppress the tendency towards the spin-liquid insulating phase. This conclusion is further confirmed by the (zero temperature) phase diagram Fig. 5 obtained by explic- itly solving the self-consistent equation (the boundary in this phase diagram is the same previously shown in Fig. 3(a)). As can be seen from Fig. 5, the insulating spin liquid phase has a dome shape in the phase dia- gram, which will be suppressed by very small or large $t_d$. The gray dashed line indicates the critical value of $V$, above which $E_2$ band is fully occupied and the metal- lic phase has a single Fermi surface. The orange dashed line marks the boundary where the two heavy fermion bands start to develop an indirect gap, which occurs for parameters above such orange line (see further discussion in Section IV).

### B. Particle-hole dispersion
In this section we discuss the results for the case where itinerant electrons are hole-like which can be accounted for by simply changing $t_c \rightarrow -t_c$ in their energy dispersion (Eq. (5c)).

![](./images/867774073923436858_4.jpg)

FIG. 4. Solution of $\Phi$ for different types of self-consistent equations. The orange lines stand for the self-consistent equa- tion with the linear $t_d$ (nearest neighbour coupling) term while the blue lines are for the case without the linear $t_d$ term. The solid lines are for the case with exact form of $\chi_{cf}$ with a cut-off while the dashed curves stand for the case with a (log- arithmically) diverging $\chi_{cf}$ at small $V_f$. The logarithmically diverging $\chi_{cf}$ always support a weak-coupling instability to the heavy metal phase while for the exact $\chi_{cf}$, there is a threshold of $V$ for the onset metallic phase. The linear $t_d$ term in the left hand side of the self-consistent equation will also help boost the heavy fermion phase, as expected.

![](./images/867774073923436858_5.jpg)

FIG. 5. Phase diagram with $\xi=1.2$ (density plot of $\Phi$). The vertical scale is proportional to the Kondo coupling scale $J_K \sim V^2/U$ while the horizontal scale is proportional to the hopping between the correlated electrons. The dark blue re- gion is the spin liquid with $\Phi=0$ and the light blue and red re- gion stand for the heavy metal phase. The gray dashed curve is the critical value of $V$ where the number of Fermi surfaces of the system changes from two (below) to one (above) and the $\chi_{cf}$ changes from a constant plateau to a monotonically decreasing function of $V_f$ (see Fig. 3(b)). The orange dashed curve indicates where the two heavy quasiparticle bands de- velop an indirect band gap. Dotted lines and symbols indicate where detailed LDOS spectra are calculated as a guiding ref- erence for subsequent Figs. 11 – 14.

### 1. Phase-boundary
When the metallic electron's band structure is hole- like, the susceptibility $\chi_{cf}$ will have a stronger $\xi$ depen- dence compared to the particle-particle case. It can be shown that within the spin liquid phase ($V_f=0$), it is given by:

$$
\chi_{c f}^{(0)}=\frac{2}{3 \Lambda^{2}\left(T_{f}+t_{c}\right)} \ln \left(\frac{\left(T_{f} / t_{c}+\xi\right)\left(T_{f} / t_{c}+2-\xi\right)}{T_{f} / t_{c}(1-\xi)^{2}}\right).
\tag{22}
$$

Thus for $\xi=1$, i.e., when both the itinerant electrons and spinons are at half-filing, the two bands are per- fectly *nested*, the band structure leads to a divergent susceptibility $\chi_{c f}$ for all values of $t_d$, which indicates that the spin liquid is unstable against a transition into the Kondo insulating phase at arbitrarily small $V$. Fig- ure 6(a) shows the phase boundary between the spin liq- uid and the heavy fermion metallic phase. Similar to the particle-particle case, as $t_d \to 0$, the critical value of $J_K \sim V^2/U$ decreases logarithmically with $t_d$. Moreover, for the particle-hole case, the phase boundary now also has a $\xi$-dependence, as expected from the $\xi$-dependence of $\chi_{c f}^{(0)}$. As $\xi \to 1$, the spin liquid phase is suppressed and

![](./images/867774073923436858_6.jpg)

FIG. 6. (a) Phase boundary for particle-hole dispersion at various filling of the metallic electrons. As $\xi \to 1$, the spin liquid phase gets suppressed and at exactly half-filling of the metal, it can exist only within the $V$=0 line. (b) $\chi_{cf}$ as a function of $V_f$ for the particle-hole dispersion with $\xi$=0.6, $T_f$=0.1$t_c$. Similar to the particle-particle case, $\chi_{cf}$ is a decreasing function of $V_f$.

when $\xi$=1, it only exists along the $V$=0 line Fig. 6(a). It should be noted that at $V$=0, the critical $t_d/U$ for the Mott transition is always the same "universal" value around 1/8, this is because the $d$ and $c$ electrons are decoupled in this case and the problem reduces to the metal to insulator transition for the triangular lattice Hubbard model.

### 2. Turning on of the heavy fermion phase

For the case with $\xi$<1, weakly inside the heavy-fermion metallic phase, where the quasi-particles' energy dispersion $E_{1,k}$ and $E_{2,k}$ has the Mexican-hat shape, it turns out that in order to maintain the half-filling constraint of the spinon, we find that $E_{2,k}$ band is fully filled while the $E_{1,k}$ band is partially occupied and features two Fermi surfaces, as shown by the green dashed lines in Fig. 2(b). The $\mu_F$ can be solved from $\langle f_{i,\sigma}^{\dagger}f_{i,\sigma} \rangle$=1/2 and the $\chi_{cf}$ as a function of $V_f$ can be obtained accordingly. Similar to the particle-particle case, at finite $t_d$, $\chi_{cf}$ tends to saturate as $V_f \to 0$ and it is diverging in the atomic limit ($t_d \to 0$). For rather large $V_f$, $E_{1,\Lambda}$ becomes smaller than 0 and there is only one Fermi surface for the system (see the orange dashed lines in Fig. 2(b)). A plot of $\chi_{cf}$ at $\xi$=0.6 is shown in Fig. 6(b), as expected, it is a decreasing function of $V_f$. The phase diagram for this case is shown in Fig. 7.

As for the special case when $\xi$=1, as explained before, because the spinon and the itinerant electron bands are nested in this case, the susceptibility $\chi_{cf}$ diverges as $V_f \to$ 0. As a result, one expects a weak coupling instability from the spin liquid state to that with heavy electrons. Notice however that this state is not a metal but a Kondo insulator, since the Fermi surfaces are completely gapped out by the hibridization due to the perfect nesting. As can be seen from Fig. 8, the Kondo insulating phase turns on more rapidly for larger $t_d/U$. The phase diagram for this case is shown in Fig. 9.

![](./images/867774073923436858_7.jpg)

FIG. 7. Phase diagram for the particle-hole case with $\xi$=0.6. The spin liquid phase has a dome shape and the phase boundary has qualitatively the same behaviour as the particle-particle case.

![](./images/867774073923436858_8.jpg)

FIG. 8. $\Phi$ as a function of $V^2/U$ for $\xi$=1 at different value of $t_d/U$. As expected, the metallic phase turns on in the form of a weak coupling instability with $V$.

## IV. TUNNELLING DOS

In the recent experiment by Ruan et al. [20], a monolayer 1T-TaSe$_2$, which is originally an insulator, is placed on top of a metallic monolayer 1H-TaSe$_2$. The system was studied by STM, where the tip is primarily coupled to the top layer (1T-TaSe$_2$). Surprisingly, a narrow peak around zero bias was found. It was found that this coherent peak can be broadened by increasing temperature and the temperature dependence of its width can be fitted to a form (see Eq. (28)) which describes the Kondo resonance for the single impurity Kondo problem

![](./images/867774073923436858_9.jpg)

FIG. 9. Phase diagram for the particle-hole case with perfect nesting ($\xi=1$). The system is in Kondo insulating at any finite $V$ since the Fermi surface of the heavy electrons are fully gapped out, and the spin liquid phase exists strictly only at the $V=0$ line.

(as shown in the Fig. 2(c) of Ref. [20]). This observation was then taken as an indication of the existence of the local magnetic moment in the $1\text{T-TaSe}_2$ layer, which couples to the metallic substrate (the $1\text{H}$ layer). Combining this with the further observation of a real space modulation of the electronic structure, it was suggested that the pristine $1\text{T-TaSe}_2$ monolayer is likely to host the QSL phase.

This motivates us to study if this behaviour could also appear in our theoretical model, e.g., in certain regimes of the heavy metal phase. In this section, we discuss the behaviour of the LDOS of the correlated $d$ electrons in the metallic phase, which is the quantity reflected by the STM $dI/dV$ curve. The thermal Green function of the $d$ electron can be written as:

$$
\begin{aligned}
G_{d}(\tau, \mathbf{r}) & =-\left\langle T_{\tau} d_{\mathbf{R}+\mathbf{r}}(\tau) d_{\mathbf{R}}^{\dagger}(0)\right\rangle \\
& =G_{f}(\tau, \mathbf{r}) G_{\theta}(\tau, \mathbf{r}),
\end{aligned}
\tag{23}
$$

where $G_{f}(\tau, \mathbf{r})$ and $G_{\theta}(\tau, \mathbf{r})$ are Green functions of the spinon and rotor, with the definition:

$$
G_{f}(\tau, \mathbf{r})=-\left\langle T_{\tau} f_{\mathbf{R}+\mathbf{r}}(\tau) f_{\mathbf{R}}^{\dagger}(0)\right\rangle,
\tag{24a}
$$

$$
G_{\theta}(\tau, \mathbf{r})=\left\langle T_{\tau} e^{i \theta_{\mathbf{R}+\mathbf{r}}(\tau)} e^{-i \theta_{\mathbf{R}}(0)}\right\rangle.
\tag{24b}
$$

As pointed out from previous studies [24, 28], the Matsubara Green function of $d$ electrons can be separated into a *coherent* part and an *incoherent* part:

$$
G_{d}\left(i \omega_{n}, \mathbf{r}\right)=G_{d}^{c o h}\left(i \omega_{n}, \mathbf{r}\right)+G_{d}^{i n c}\left(i \omega_{n}, \mathbf{r}\right),
\tag{25a}
$$

$$
G_{d}^{c o h}\left(i \omega_{n}, \mathbf{r}\right)=\Phi^{2} G_{f}\left(i \omega_{n}, \mathbf{r}\right).
\tag{25b}
$$

The coherent part is mainly peaked at $\omega \sim 0$ while the incoherent part captures features at larger energy scales $\omega \sim U$. In this work, we are mainly interested in the feature of LDOS near $\omega=0$ and we will focus on the coherent part. From the slave rotor mean-field theory, since the fermionic part of the Hamiltonian is non-interacting, it can be shown that the Matsubara Green function of spinon has the form:

$$
G_{f}\left(i \omega_{n}, k\right)=\cos ^{2}\left(\alpha_{k}\right) G_{1}\left(i \omega_{n}, k\right)+\sin ^{2}\left(\alpha_{k}\right) G_{2}\left(i \omega_{n}, k\right),
\tag{26}
$$

where $G_{1 / 2}\left(i \omega_{n}, k\right)=1 /\left(i \omega_{n}-E_{1 / 2, k}\right)$ are the Green function of the self-consistent band-diagonal quasiparticles that result from the coherent mixing of the correlated and the itinerant electron. By analytical continuation, the spectral function of the spinons can be obtained:

$$
\begin{aligned}
A_{f}(\omega, k) & =-\frac{1}{\pi} \operatorname{Im} G_{f}\left(\omega+i 0_{+}, k\right) \\
& =\cos ^{2}\left(\alpha_{k}\right) \delta\left(\omega-E_{1, k}\right)+\sin ^{2}\left(\alpha_{k}\right) \delta\left(\omega-E_{2, k}\right),
\end{aligned}
\tag{27}
$$

and the LDOS for the spinon $\rho_{f}(\omega)=\frac{1}{N} \sum_{k} A_{f}(\omega, k)$ can be obtained accordingly.

### A. Zero temperature mean-field LDOS

We are particularly interested in understanding the tunnelling density of states for experiments in $1\text{T-TaSe}_2$ where the dispersion of itinerant electron is likely to be particle like. Here we explored in detail the particle-particle case and we take the bare band filling of the itinerant electrons to be $\xi=1.2$ (this value is taken arbitrarily as the physics should not be very sensitive to the detailed value of $\xi$). We are mainly focused on three regimes: i) Anderson limit with $t_d=0$, ii) moderate $t_d$ along the orange dashed line in Fig. 5, iii) large $t_d$ near the metal-insulator transition of Hubbard model.

Fig. 10 shows the zero temperature mean-field LDOS of correlated $d$ electrons at different regimes of the phase diagram, as indicated by the black dotted lines in Fig. 5. In the Anderson limit (see Fig. 10(a)), the mean-field LDOS opens a coherent band gap enhanced by increasing the Kondo coupling $J_K$, which is the expected behaviour for the periodic Anderson model. When $t_d/U$ is finite (see Figs. 10(b), (c) and (d)), the spinon acquires a band dispersion. Consequently, when $\Phi$ is small at small $J_K$, the quasiparticle bands are still overlapping with each other in energy (see green dashed line in Fig. 2(a)) and the LDOS shows a plateau-like peak near $\omega \sim 0$. The width of the plateau is given mainly by the spinon bandwidth. As $J_K$ becomes larger, the overlap between the two bands decreases and the width of the flat peak is reduced. At some intermediate scale marked by the orange dashed line in Fig. 5, the Kondo coupling and the Heisenberg exchange interaction compete, resulting in a narrow peak whose width is much less than $J_K$ or $J_H$ inidividually. Finally, when $J_K$ is greater than

a critical value indicated by the orange dashed line in Fig. 5, the two quasiparticle bands become fully sepa- rated and the LDOS behaves similarly to the Anderson limit with a finite gap sandwiched by two peaks. As can be seen clearly, near the the metal-insulator transition of the Hubbard model, the LDOS peak is much broader than in the small $t_d/U$ limit. It should be noted that the perfect flatness of the peak is an artefact of parabolic band dispersion adopted in our study, and a more real- istic tight-binding model would give rise to a dispersive peak. Below we will describe how these LDOS features are broadened by temperature and by extrinsic disorder effects.

## B. Broadening due to finite temperature and disorder
At finite temperature the tunneling conductance is given by the LDOS convolved with the thermal broad- ening due to the thermal distribution of electrons in the lead. This effect has been removed in the experiment [29] and we also do not include it in our theory. After removing this, it is notable that the experiment shows a single peak which can be fitted with a Lorentzian with a temperature dependent half maximum half width:
$$
\Gamma_{exp}=\sqrt{2 T_{K}^{2}+\pi^{2} T^{2}},\qquad(28)
$$

This form of the width was found in an earlier experiment that detected the Kondo peak in a single impurity and has been considered a signature of the single impurity Kondo problem [29]. The low temperature width there- fore allows to extract $T_K$ from experiments. Further- more, at large temperatures compared to $T_K$ the width scales approximately as $\pi T$, which places a constraint on the theory. We have re-examined the theoretical ba- sis of Eq. (28) and came to the conclusion that while the derivation given in [29] is not well justified and there is a small correction to the width from Eq. (28) at low tem- peratures, it does provide a correct value of the slope of $\Gamma$-$T$ curve at high temperatures, which is $\pi$. Details are given in the Appendix B. In this work we do not fit the experimental data to the single impurity Kondo problem, but rather to the periodic Anderson-Hubbard model. As we shall see below, by introducing a Fermi liquid type quasiparticle life-time together with a disorder induced width, it is possible to fit the data in certain parameter ranges.

As it is well known from the theory of single Kondo impurity and Kondo lattice problems [30-33], the fluc- tuations around the mean-field configuration which give rise to quasi-particle interactions, lead to a characteris- tic temperature and frequency dependent quasi-particle lifetime. In order to account for these effects, we add the following semi-phenomenological imaginary part to the quasi-particle self-energy [34]:
$$
\Sigma_{F L}(\omega, T)=-i \frac{1}{2 \pi E_{0}}\left(\omega^{2}+\left(\pi k_{B} T\right)^{2}\right).\qquad(29)
$$

In addition to this intrinsic quasi-particle interaction life- time, disorder is another important agent in broadening the density of states in experiments, and we account for this by adding a constant impurity scattering rate $\gamma_0$ into the imaginary part of the self-energy, as follows:
$$
G_{1 / 2}\left(\omega+i 0_{+}, k\right)=\frac{1}{\omega-E_{1 / 2, k}-\Sigma(\omega, T)}\qquad(30a)
$$

$$
\Sigma(\omega, T)=-i \gamma_{0}+\Sigma_{F L}(\omega, T).\qquad(30b)
$$

It should be noted that the energy scale $E_0$ controlling the quasi-particle interaction effects in Eq. (29), is usu- ally of the order of the bandwidth for a normal Fermi liquid (large $t_d$), while for a Kondo lattice ($t_d=0$), it is of the order of the Kondo temperature $T_K \sim 2V_f^2/D_c$ with $D_c$ being the half bandwidth of itinerant electrons. In order to capture both regimes, we use a phenomenologi- cal expression of $E_0$ that interpolates between these two limits, as follows:
$$
E_{0}=\sqrt{T_{K}^{2}+W_{s p}^{2}},\qquad(31)
$$
with $W_{sp}$ being the spinon bandwidth.

As mentioned above, in the Anderson limit, the mean- field LDOS will have two peaks separated by the gap. However, once the self-energy is included, the mean- field spectral function will be broadened and it is pos- sible to obtain a single-peak behaviour. This can be seen clearly from Fig. 11, which shows the case of $t_d/U=0$, $V^2/U=0.5t_c$ (as indicated by the $\blacksquare$ in Fig. 5). By including only the $\Sigma_{FL}$ (see Fig. 11(a)), at very low temperatures, the LDOS has two peaks separated by a band gap. When a finite impurity scattering rate (here we take $\gamma_0=0.05t_c$) is taken into account, the LDOS is broadened into a single-peak, as shown in Fig. 11(b). We further calculated the half maximum half width of LDOS at different temperatures and compare it with the experimental results. We fit our theoretical data with a function of the form
$$
\Gamma=\sqrt{\left(\Gamma_{0}\right)^{2}+a \pi^{2}\left(k_{B} T\right)^{2}},\qquad(32)
$$
which is expected for the single-impurity Anderson model [35, 36]. Previous theoretical works find that the ex- perimental data can be well fitted with $a \approx 1$. Accord- ing to our theoretical calculation, for the case with $V^2/U=0.5t_c$ and $\gamma_0=0.05t_c$, the data can be well fit- ted with $a \approx 0.85$, as can be seen from Fig. 11(c), where all quantities are presented in unit of $t_c$. Nevertheless, once we take $t_c=105$meV so that the lowest tempera- ture width matches with the experimental one, we also find quantitatively good fit to the experimental result. In other words, the experimental data can be described by a periodic Anderson model with a finite impurity scat- tering rate.

When $t_d$ is finite, as shown in the mean-field results above, one expects to see either a plateau-like peak (with small $J_K$) or a finite gap sandwiched by two peaks (rather

![](./images/867774073923436858_10.jpg)

FIG. 10. Mean-field LDOS without disorder and quasiparticle life-time broadening effects for the case of (a) $t_d/U=0$, (b) $t_d/U=0.04$, (c) $t_d/U=0.08$ and (d) $t_d/U=0.1$. Within each case, the Kondo coupling $J_K \sim V^2/U$ is increased gradually (along the black dotted lines in Fig. 5). In the Anderson limit, it is clear that within the heavy metal phase, there is a coherent gap opened below the Fermi level. On the other hand, when $t_d/U$ is finite, the spinon band is dispersive with a finite bandwidth. So for small $J_K$, the band dispersion of heavy quasiparticles are still overlapping with each other (see the green dashed lines in Fig. 2(a)), and leads to a plateau like LDOS at small $\omega$. When $J_K$ is large and above the orange dashed line in the phase diagram (see Fig. 5), the two heavy quasiparticle bands are fully separated in energy and the LDOS exhibits a gap between the two peaks.

large $J_K$) in the LDOS. In any case, the inclusion of a finite imaginary self-energy can broaden the curve. Along the orange line, since the two mean-field bands of heavy quasiparticles are about to separate, the LDOS of spinon should have only a single peak around $\omega \sim 0$. Figs. 12(a)-(c) and 13(a)-(c) show two points close to the line: $t_d/U=0.04, V^2/U=0.35 t_c$ and $t_d/U=0.08, V^2/U=0.65 t_c$ (indicated by $\star$ and $\star$ respectively in Fig. 5), it is clear that the LDOS has only a single peak at $\omega \sim 0$. We find that the width as a function of temperature can also be relatively well fitted by Eq. (32). To compare with the experimental data, as we did for the Anderson limit, one can tune $t_c$ so that at the lowest temperatures the width is consistent with the experimental one. Fig. 12(c) and Fig. 13(c) show the comparison of the width between the theoretical and experimental results. $t_c$ is taken to be 120 meV and 75 meV separately. We can see that the small spinon hopping case $t_d/U=0.04$ can give rise to a good fit to the experimental data. For the larger $t_d$ case ($t_d/U=0.08$) the fit deteriorates because the coefficient $a$ is becoming too small.

![](./images/867774073923436858_11.jpg)

FIG. 11. LDOS for the particle-particle case ($\xi=1.2$) with $t_d/U=0, V^2/U=0.5 t_c$ (indicated by $\blacksquare$ in Fig. 5). (a) LDOS with the self-energy being $\Sigma_{FL}(\omega,T)$ only. It is clear that in the low temperature limit, the spectral function has the two-peak behaviour at $\omega \sim 0$, which is due to the opening of a band gap in the dispersion of heavy quasiparticles. This is the signature of a coherent heavy Fermion band in the kondo lattice problem. At higher temperature, there is only a single peak around $\omega \sim 0$ due to the broadening effects in $\Sigma_{FL}(\omega,T)$. (b) LDOS for self-energy from Eq. (30b) with $\gamma_0=0.05 t_c$. In this case the disorder effect ($\gamma_0$ term) is able to broaden the LDOS and changes it into a single-peak. (c) Width in unit of $t_c$. (d) Fitting to experimental data (extracted from Ref. [20]) with $t_c=105$ meV. The experimental data can be well fitted by the theoretical result.

We also checked cases with moderate $t_d/U$ but being farther away from the orange dashed line: $t_d/U=0.04$, $V^2/U=0.8$ and $t_d/U=0.08$, $V^2/U=0.3$ (indicated by $\diamond$ and $\bullet$ respectively in Fig. 5). Figs. 12 (d) and (e) show the LDOS for the first case without and with $\gamma_0$ included in the self-energy, and the LDOS for the latter case (without and with $\gamma_0$ in the self-energy) are presented in Figs. 13(d) and (e). The first case is

$$t_d/U=0.04$$

![](./images/867774073923436858_12.jpg)

![](./images/867774073923436858_13.jpg)

![](./images/867774073923436858_14.jpg)

![](./images/867774073923436858_15.jpg)

![](./images/867774073923436858_16.jpg)

![](./images/867774073923436858_17.jpg)

FIG. 12. LDOS at $t_d/U=0.04$. (a)-(c) With $V^2/U=0.35t_c$ (indicated by $\star$ in Fig. 5). (a)-(b) LDOS without/with $\gamma_0$ in the self-energy. (c) Width fitted to the experiment with $t_c=120$ meV. The experimental data can be relatively well fitted by this case. (d)-(f) With $V^2/U=0.8t_c$ (indicated by $\diamond$ in Fig. 5). (d)-(e) LDOS without/with impurity scattering in the self-energy. (f) Fitting of the width to experiment with $t_c=60$ meV. This case is much above the orange dashed line in Fig. 5 and the two quasiparticle bands are separated form each other.

above the orange dashed line in Fig. 5 with a large $J_K$, and the two quasiparticle bands are separated in energy. So the LDOS (Fig. 12(d)) has a gap sandwiched by two peaks. In the later case, which is below the orange dashed line, the two quasiparticle bands overlap with each other and there is a flat peak in LDOS (see Fig. 13(d)). Once $\gamma_0$ is introduced for both cases, the LDOS changes into a single peak behaviour for both cases (Fig. 12(e) and Fig. 13(e)). The fitting of LDOS width to the experimental data for these two cases are shown in Fig. 12(f) and Fig. 13(f). One can see that while the parameter $a$ for $t_d/U=0.04$ still gives a reasonable fit, the value of $a$ for $t_d/U=0.08$, $V^2/U=0.3$ is too small and the width cannot be well fitted by Eq. (32). We conclude that as $t_d/U$ increases, the fit deteriorates, especially away from the orange dashed line.

Finally, for large $t_d/U$ (here we take $t_d/U=0.11$) close to the critical value for the metal-insulator transition in the isolated Hubbard model, the LDOS for $V^2/U=0.1t_c$ and $V^2/U=0.3t_c$ (indicated by $\blacktriangle$ and $\triangle$ separately in Fig. 5) are shown in Fig. 14(a)-(c) and (d)-(f). As expected, the LDOS has a flat top near $\omega\sim0$ without the inclusion of $\gamma_0$ in the self-energy (Fig. 14(a) and Fig. 14(d)), and will be broadened once $\gamma_0$ is introduced (Fig. 14(b) and Fig. 14(e)). Fig. 14(c) and Fig. 14(f) show the width for these cases and we see that the experimental data cannot be fitted by the theoretical results in this regime because the theoretical slope is too small.

To summarize, by including a Fermi liquid type of (imaginary) self-energy into heavy quasiparticles' Green function, it is possible to obtain a single-peak behaviour for the LDOS even in the Anderson limit. By modifying the value of $\gamma_0$, the width of LDOS can be well fitted by Eq. (32), which is the formula for a single impurity Kondo problem, as illustrated in Fig. 11(d). Moreover, adjusting $t_c$ to fit the experimental width value at the lowest temperature, our theory suggests that the experimental situation may be in or close to the Anderson limit of the model. On the other hand, for intermediate $t_d/U$ a reasonable fit can be obtained when the Kondo scale $J_K$ and the Heisenberg scale $J_H$ compete, resulting in a low temperature width which is smaller than $J_K$ or $J_H$, as illustrated in Fig. 12(c). In addition, our theory predicts $a\sim0.3$ if the hopping of the $d$ electrons is close to the critical value of for the metal-insulator transition in isolated Hubbard model, a value which does not fit the experimental data.

$$t_d/U=0.08$$

![](./images/867774073923436858_18.jpg)

![](./images/867774073923436858_19.jpg)

![](./images/867774073923436858_20.jpg)

![](./images/867774073923436858_21.jpg)

![](./images/867774073923436858_22.jpg)

![](./images/867774073923436858_23.jpg)

FIG. 13. LDOS at $t_d/U=0.08$. (a)-(c) With $V^2/U=0.65t_c$ (indicated by $\star$ in Fig. 5). (a)-(b) LDOS without/with $\gamma_0$ in the self-energy. (c) Fitting of the width to experiment with $t_c=75$meV. In this case the theory lies below the data because the slope $a$ is becoming too small. (d)-(f) With $V^2/U=0.3t_c$ (indicated by $\bullet$ in Fig. 5). (d)-(e) LDOS without/with impurity scattering in the self-energy. (f) Fitting of the width to experiment with with $t_c=110$meV. This case is below the orange dashed line and the two quasiparticle bands overlaps.

## V. SUMMARY AND DISCUSSIONS

We have studied a model of coupled correlated and itinerant electrons which naturally interpolates between the periodic Anderson model and the Hubbard model. Using a slave rotor mean-field approach we have obtained a phase diagram that summarizes the competition between a spinon Fermi surface state weakly coupled to a metal and an interlayer coherent heavy Fermi liquid metallic state (illustrated in Figs. 5, 6 and 8). In the localized or atomic limit where our model reduces to the periodic Anderson model, the Kondo coupling needed to destroy the spin liquid in favor of the metal, $J_K \sim V^2/U$, has a logarithmic dependence on the hopping of the correlated electrons in the putative spin liquid layer $t_d/U$, reflecting that the emergent scales determining the competition are the Kondo temperature $T_K \sim \rho^{-1}e^{-1/J_K \rho}$ ($\rho \sim t_c^{-1}$) and Heisenberg coupling $J_H \sim t_d^2/U$. Therefore, although technically in such limit the spin liquid is destabilized via a weak coupling instability, the critical Kondo coupling needed to destabilize the spin liquid grows rather fast with the Heisenberg coupling, giving rise to the rapid rise of the boundary between the spin liquid and the heavy metal at small $t_d/U$ seen in Figs. 5, 6 and 8. In this limit one can use the measured saturation width $T_K$ to place an upper bound on the Heisenberg coupling $J_H$, resulting in a rather small bound of about 5 meV from the experiments of Ref. [20]. On the other hand, at larger values of $t_d/U \sim 0.1$ when the spin liquid has a sizable bandwidth, the critical $J_K$ is comparable to $t_d/U$, and near the Mott transition the critical Kondo coupling needed to destabilize the spin liquid vanishes linearly with the distance of $t_d/U$ away from the critical value associated with the Mott metal-insulator-transition, at mean field level. However, we find that generically the peak width is dominated by the spinon bandwidth, leading to a width that is too broad and with too weak a temperature dependence to explain the data. The exception is when the system happens to fall near the crossover line indicated in orange in Fig. 5, where a reasonable fit to the data can also be obtained. In this case, the Kondo scale $J_K$ and the Heisenberg scale $J_H$ compete, giving rise to a narrow peak with a width which is smaller than either scale at low temperature. As a result, in this case the low temperature width cannot be used as a bound for either scale, and it is possible that $J_H$ is much larger than the 5 meV bound mentioned previously.

The above conclusion was reached by studying the LDOS of the heavy metal throughout this phase diagram, which can be directly accessed via STM experiments [20]. In the local moment periodic Anderson limit of the model the coherent hybridization of correlated and

![](./images/867774073923436858_24.jpg)

FIG. 14. LDOS at $t_d/U=0.11$. (a)-(c) With $V^2/U=0.1t_c$ (indicated by $\blacktriangle$ in Fig. 5). (a)-(b) LDOS without/with impurity scattering in the self-energy. (c) Fitting of the width to experiment with $t_c=90$meV. The slope of the theoretical data is too small to fit the experimental data. (d)-(f) With $V^2/U=0.3t_c$ (indicated by $\bigtriangleup$ in Fig. 5). (d)-(e) LDOS without/with impurity scattering in the self-energy. (f) Fitting of the width to experiment with with $t_c=90$meV. Similar to the previous case, the slope of the theoretical data is too small to fit the experimental data.

itinerant electrons in the heavy metal leads to the bare LDOS acquiring a two-peak structure due to the opening of a direct optical band gap. On the other hand, near the Mott-metal-insulator transition the LDOS features a rather flat shape due to a relatively large spinon band width. The measured LDOS is however further broadened by the intrinsic lifetime of the heavy quasi-particles arising from their interactions and also by disorder, leading to a smearing of the double-peak structure in the periodic Anderson model limit. We have argued that including these effects renders the double peak structure effectively into a single peak, and we have found good agreement with the shape and temperature dependence of the peak reported in recent STM experiments [20], as illustrated in Fig. 11(d). We also find reasonable fit to the data at intermediate $t_d/U$ in the vicinity of the orange line in Fig. 5, as illustrated in Fig. 12(c).

We note that in the localized limit of small $t_d/U$ the Hubbard model in the triangular lattice is expected not to form a spinon Fermi surface state, but to order into a conventional $120^\circ$ AFM phase. This piece of physics is not captured in our slave rotor mean-field theory, which favors spin disordered ground states. Therefore, our results pose a challenge for the interpretation of the behavior of the stand-alone putative 1T-TaSe$_2$ as a quantum spin liquid: if indeed the system is near the Anderson limit, this raises the possibility that it could be instead comprised of localized moments that are rather weakly coupled and might ultimately weakly order at yet lower temperatures in cleaner samples. We however caution that we cannot definitely rule out that the putative spin liquid layer is at an intermediate coupling strength $t_d/U$ that brings the system closer to the Mott transition, where also a small interlayer tunnelling can destabilize the spin liquid. An additional consideration is that the actual 1T-TaSe$_2$ system involves multiple bands and is probably not described by a single band Mott-Hubbard model. While the spin liquid is stabilized only near the Mott transition in a single band model [25], it is possible that a multi-band description can extend the spin liquid to lower effective $t_d$.

Additionally, to reiterate the potential uncertainties, we wish to note that the parameter $a$ in Eq. (32) that we used near the Mott transition has a Fermi liquid form but it can be changed by tuning the value of $\gamma_0$ and $E_0$, which are respectively controlled by disorder and quansiparticle interactions, and hence are inherently difficult scales to estimate accurately.

We want also to point out that in our calculation, we considered the metallic electrons to have the same lattice constant and Brillouin zone as the correlated electrons. In doing so, we are imagining that in a more

microscopic description one would be folding the Bril- louin of the metallic 1H-TaSe₂, which does match with the smaller Brillouin zone of the star of David structure of 1T-TaSe₂, and that after this one is only including one of the folded bands of itinerant electrons. However, the hybridization with electrons at higher energy scales (coming from other folded bands) could also play an im- portant role in determining the phase boundary and the form of LDOS, but such details lie beyond the scope of the considerations that we have explored in the present work.

## ACKNOWLEDGMENTS

We thank Michael F. Crommie, Wei Ruan and Yi Chen for sharing their data and discussions. We also thank Peng Rao for fruitful discussions. PAL acknowledges support by DOE office of Basic Sciences grant number DE-FG02-03ER46076.

### Appendix A: Finite Temperature Rotor Mean Field Approach

As mentioned in the main text, for the order parame- ter of metallic phase, $\Phi=\langle e^{i\theta}\rangle$, we estimate its value by taking the average with respect to a single site Hamilto- nian:
$$
\begin{aligned}
H_{\theta}^{(1)} & =-K_{\theta}\left(e^{i \theta}+e^{-i \theta}\right)+\frac{U}{2} n_{\theta}^{2} & & \text { (A1) } \\
& =H_{K}+H_{U}, & & \text { (A2) }
\end{aligned}
$$
where $H_{K}=-K_{\theta}(e^{i \theta}+e^{-i \theta})$ and $H_{U}=\frac{U}{2} n_{\theta}^{2}$. We have taken $\lambda=0$ to fulfil the constrain Eq. (3) and the half filling of the spinon. Because we are interested in the large $U$ limit of the model $(t_{d}/U\lesssim 1/8)$, it is reasonable to use a first-order perturbation (in $H_{K}$) to estimate the expectation value:
$$
\begin{aligned}
\left\langle e^{i \theta}\right\rangle= & \frac{\operatorname{Tr}\left(e^{-\beta\left(H_{U}+H_{K}\right)} e^{i \theta}\right)}{\operatorname{Tr}\left(e^{-\beta\left(H_{U}+H_{K}\right)}\right)} \\
\approx & -\int_{0}^{\beta} d \tau \operatorname{Tr}\left(e^{-\beta H_{U}} e^{\tau H_{U}} H_{K} e^{-\tau H_{U}} e^{i \theta}\right) / \operatorname{Tr}\left(e^{-\beta H_{U}}\right), \\
& (\mathrm{A} 3)
\end{aligned}
$$
one can take the trace with the eigenbasis of angular momentum $n_{\theta}$: $\{|n\rangle\}$, which satisfies: $n_{\theta}|m\rangle=m|m\rangle$ and $e^{i \theta}|n\rangle=|n+1\rangle$, and we will denote the eigenvalue of $H_{U}$ by $E_{n}=\frac{U}{2} n^{2}$. It is straightforward to obtain:
$$
\begin{aligned}
& -\int_{0}^{\beta} d \tau \operatorname{Tr}\left(e^{-\beta H_{U}} e^{\tau H_{U}} H_{K} e^{-\tau H_{U}} e^{i \theta}\right) \\
= & K_{\theta} \sum_{n} \int_{0}^{\beta} d \tau e^{-\beta E_{n}} e^{-\beta E_{n}} e^{\tau\left(E_{n}-E_{n+1}\right)} \\
= & K_{\theta} \sum_{n} \frac{e^{-\beta E_{n+1}}-e^{-\beta E_{n}}}{E_{n}-E_{n+1}},
\end{aligned}
$$

$$
\operatorname{Tr}\left(e^{-\beta H_{U}}\right)=\sum_{n} e^{-\beta E_{n}}, \quad \text { (A4b) }
$$
so one finally arrives at:
$$
\left\langle e^{i \theta}\right\rangle \approx \chi_{\theta, 1} K_{\theta}, \quad \text { (A5) }
$$

$$
\chi_{\theta, 1}=\sum_{n} \frac{e^{-\beta E_{n+1}}-e^{-\beta E_{n}}}{E_{n}-E_{n+1}} / \sum_{n} e^{-\beta E_{n}}. \quad \text { (A6) }
$$

By Taking the zero temperature limit, one can recover the zero temperature result given by:
$$
\lim _{\beta \rightarrow \infty} \chi_{\theta, 1}(\beta)=4 / U. \quad \text { (A7) }
$$

Next, we extrapolate the expression above, which is valid only for small $K_{\theta}$, with the phenomenological formula:
$$
\left\langle e^{i \theta}\right\rangle=\frac{K_{\theta}}{\sqrt{\chi_{\theta, 1}^{-2}+K_{\theta}^{2}}}, \quad \text { (A8) }
$$
which recovers the behavior from Eq. (A5) at small $K_{\theta}$ and also the approach of $\langle e^{i\theta}\rangle\to 1$, which is expected at large $K_{\theta}$ (and it is also consistent with the constraint that $\langle e^{i\theta}\rangle\leq 1$).

For $\langle e^{-i \theta_{i}} e^{i \theta_{j}}\rangle$, one can perform same kind of calcula- tion. We estimate it by taking the expectation value with respect to the Hamiltonian:
$$
\tilde{H}_{\theta}=\frac{U}{2} \sum_{i} n_{\theta, i}^{2}-2 T_{\theta} \sum_{\langle i, j\rangle}\left(e^{-i \theta_{i}} e^{i \theta_{j}}+h. c.\right), \quad \text { (A9) }
$$
taking $T_{\theta}$-term as a perturbation, after some algebra, one obtains that:
$$
\left\langle e^{-i \theta_{i}} e^{i \theta_{j}}\right\rangle \approx \chi_{\theta, 2} T_{\theta}, \quad \text { (A10) }
$$

$$
\begin{aligned}
\chi_{\theta, 2}= & 2\left(\sum_{n_{i} \neq n_{j}+1} \frac{e^{-\beta\left(E_{n_{i}-1}+E_{n_{j}+1}\right)}-e^{-\beta\left(E_{n_{i}}+E_{n_{j}}\right)}}{E_{n_{i}}+E_{n_{j}}-\left(E_{n_{i}-1}+E_{n_{j}+1}\right)}\right. \\
& \left.+\sum_{n} \beta e^{-\beta\left(E_{n}+E_{n-1}\right)}\right) /\left(\sum_{n} e^{-\beta E_{n}}\right)^{2},
\end{aligned}
$$
and for the zero temperature limit, one recovers the value $\chi_{\theta, 2}=4 / U$. Because we are interested in small $t_{d}$ limit (remember that $T_{\theta}=t_{d} \chi_{0}$), we simply use Eq. (A10) throughout our calculations.

It should be noted that the current mean-field would predicts an artificial second order phase transition for any low temperature phase with finite $\langle e^{i\theta}\rangle$ to a high temper- ature phase with $\langle e^{i\theta}\rangle=0$, similar to the case of slave bo- son descriptions at mean-field level [32]. In reality, there is no such phase transition as a function of temperature but only a crossover [37, 38], and the expectation value of $\langle e^{i\theta}\rangle$ is always finite at non-zero temperatures. However, the zero temperature transitions which are the focus of the main manuscript are allowed to be sharp second order phase transitions in principle [39, 40].

### Appendix B: Tunnelling DOS of the single impurity Anderson Model

In this section, we briefly review the theory of tunnelling DOS for a single impurity Anderson model and give a more thorough derivation on the fitting of STM results expanding on the previous studies by Nagaoka et al. [29].

For a single impurity Anderson model, one can calculate the tunnelling DOS of the local electron using perturbation theory since there is *no* phase transition as the on-site interaction $U$ increases [23]. Early theoretical calculations [35, 36] showed that the (retarded) Green function of the local electron for the particle-hole symmetric case reads (valid at small $\omega$ and $T$):

$$
\begin{aligned}
G_{d}(\omega, T) &= \frac{1}{\omega-\epsilon_{d}-\operatorname{Re} \Sigma(\omega)+i \Delta-i \operatorname{Im} \Sigma(\omega, T)} \\
&=\frac{Z}{\omega-\tilde{\epsilon}_{d}+i Z(\Delta-\operatorname{Im} \Sigma(\omega, T))},
\end{aligned} \tag{B1}
$$

where
$$
\tilde{\epsilon}_{d}=\epsilon_{d}+\operatorname{Re} \Sigma(0) \approx 0, \tag{B2a}
$$
$$
\operatorname{Im} \Sigma(\omega, T)=-\frac{\Delta}{2} \alpha^{2}\left[\left(\frac{\omega}{T_{K}}\right)^{2}+\pi^{2}\left(\frac{T}{T_{K}}\right)^{2}\right], \tag{B2b}
$$

where $\alpha$ is a number of order unity and equals $\pi /4$. In the second line of Eq. (B1) we follow standard practice and expand $\operatorname{Re} \Sigma(\omega)$ to linear order in $\omega$ near the pole with
$$
Z=\frac{1}{1-\left.\partial_{\omega} \operatorname{Re} \Sigma(\omega)\right|_{\omega=0}}=\frac{T_{K}}{\alpha \Delta}, \tag{B3}
$$

Then it is straightforward to obtain the spectral function:

$$
\begin{aligned}
\rho_{d}(\omega) &=\frac{Z^{2}}{\pi} \frac{(\Delta-\operatorname{Im} \Sigma(\omega))}{\omega^{2}+Z^{2}(\Delta-\operatorname{Im} \Sigma(\omega))^{2}} \\
&=\frac{Z^{2} \Delta}{\pi} \frac{1+\frac{1}{2} \alpha^{2}\left(\frac{\omega^{2}}{T_{K}^{2}}+\frac{\pi^{2} T^{2}}{T_{K}^{2}}\right)}{\omega^{2}+Z^{2} \Delta^{2}\left(1+\frac{1}{2} \alpha^{2}\left(\frac{\omega^{2}}{T_{K}^{2}}+\frac{\pi^{2} T^{2}}{T_{K}^{2}}\right)\right)^{2}} \\
&=\frac{1}{\pi \Delta} \frac{1}{\frac{\omega^{2} /(Z \Delta)^{2}}{1+\frac{1}{2} \alpha^{2}\left(\frac{\omega^{2}}{T_{K}^{2}}+\frac{\pi^{2} T^{2}}{T_{K}^{2}}\right)}+1+\frac{1}{2} \alpha^{2}\left(\frac{\omega^{2}}{T_{K}^{2}}+\frac{\pi^{2} T^{2}}{T_{K}^{2}}\right)} \\
&=\frac{1}{\pi \Delta} \frac{1}{\frac{\alpha^{2} \omega^{2} / T_{K}^{2}}{1+\frac{1}{2} \alpha^{2}\left(\frac{\omega^{2}}{T_{K}^{2}}+\frac{\pi^{2} T^{2}}{T_{K}^{2}}\right)}+1+\frac{1}{2} \alpha^{2}\left(\frac{\omega^{2}}{T_{K}^{2}}+\frac{\pi^{2} T^{2}}{T_{K}^{2}}\right)}.
\end{aligned} \tag{B4}
$$

In the previous work by Nagaoka et al.[29], they did not include the expansion near the pole, which amounts to setting $Z=1$. With this and setting $\alpha=1$, they argued that the $\omega$ term in the denominator of Eq. (B1) can be dropped and they arrive at the incorrect result that $\rho_{d} \propto 1/\operatorname{Im} \Sigma(\omega, T)$, i.e.:
$$
\rho_{d}(\omega)=\frac{1}{\pi \Delta} \frac{1}{1+\frac{1}{2}\left(\frac{\omega^{2}}{T_{K}^{2}}+\frac{\pi^{2} T^{2}}{T_{K}^{2}}\right)} \tag{B5}
$$

with the prediction that the width reads:
$$
\Gamma_{exp}=\sqrt{2 T_{K}^{2}+\pi^{2} T^{2}}, \tag{B6}
$$
which suggests the slope of $\Gamma$ with respect to $T$ is approximately $\pi$ for $T \gg T_{K}$

However, as we can see from the second line in Eq. (B1), due to the fact that $Z \approx T_{K}/\Delta \ll 1$, $\omega$ cannot be dropped. This is seen explicitly in Eq. (B4), where the first term in the denominator dropped by Nagaoka et al.[29] is clearly of the same order as the rest and should be kept. Nevertheless, we shall show below that conclusion that the slope of $\Gamma$ with respect to $T$ is approximately $\pi$ at relatively high temperature is actually valid. The more complete Eq. (B4) implies that the lineshape is not a simple Lorentzian. Instead, we calculate the half-width at half height by requiring $\Gamma$ to satisfy $\rho_{d}(\Gamma)=\rho_{d}(0)/2$, which leads to:

$$
\alpha^{2}\left(\frac{\Gamma}{T_{K}}\right)^{2}=\left(1+\frac{1}{2} \alpha^{2}\left(\frac{\pi T}{T_{K}}\right)^{2}\right)^{2}-\left(\frac{1}{2} \alpha^{2}\left(\frac{\Gamma}{T_{K}}\right)^{2}\right)^{2}, \tag{B7}
$$

after some algebra, one can show that
$$
\Gamma=\frac{\sqrt{2}}{\alpha}\left(\sqrt{T_{K}^{4}+\left(T_{K}^{2}+\frac{1}{2} \alpha^{2} \pi^{2} T^{2}\right)^{2}}-T_{K}^{2}\right)^{1 / 2}. \tag{B8}
$$

In the low temperature limit, the width can be approximated as
$$
\Gamma \approx \sqrt{\frac{2(\sqrt{2}-1)}{\alpha^{2}} T_{K}^{2}+\frac{1}{\sqrt{2}} \pi^{2} T^{2}}, \tag{B9}
$$

on the other hand, for large $T$ such that $T \gg T_{K}$, $\Gamma$ can be approximated as
$$
\Gamma \approx \pi T. \tag{B10}
$$

Going back to Eq. (B4), we see that in large $T$ limit the first term in the denominator becomes a *nonzero* constant. It affects the effective definition of the zero temperature width in terms of $T_{K}$, but does not affect the high temperature limit of the line-width. Although the low temperature expansion Eq. (B9) seems to suggest that the slope of $\Gamma$-$T$ curve would saturate to $\pi /2^{1/4}$ at relatively large temperatures (see the orange dashed line in Fig. 15), the slope derived from Eq. (B8) actually saturates to $\pi$ at higher temperatures, as indicated by the blue line in Fig. 15.

According to Eq. (B8), the zero temperature width should be $\Gamma(T=0)=[2(\sqrt{2}-1)]^{\frac{1}{2}}/\alpha \approx 1.16 T_{K}$, while Eq. (B6) predicts $\Gamma_{exp}(T=0)=\sqrt{2} T_{K}$. Therefore, with a given set of experimental data of $\Gamma$ versus $T$, the extracted $T_{K}$ using Eq. (B6) would be slightly smaller than the one predicted from Eq. (B8). On the other hand, both expressions suggest that $\Gamma$ has an approximately linear dependence on $T$ for $T \sim T_{K}$ with a $\pi$ slope.

![](./images/867774073923436858_25.jpg)

FIG. 15. Plot of the LDOS width $\Gamma$ with respect to the temperature $T$ based on Fermi liquid theory. The blue solid line stands for the exact result Eq. (B8), the orange dashed line indicates the low temperature expanded form Eq. (B9) and the red dashed line shows the high temperature approximated form Eq. (B10).

Finally, comparing the Fermi liquid theory presented above and the more exact numerical renormalization group (NRG) calculation, one can see that both theories imply that the LDOS is not a simple Lorentzian form. The fermi liquid theory suggests $\Gamma(T=0) \approx 1.16T_K$ while the NRG suggests $\Gamma(T=0)=T_K$. The NRG LDOS curve can be quantitatively well fitted by a phenomenological expression suggested by Frota and Oliveira [41, 42]:

$$
\begin{aligned}
\rho_{f}(\omega) & =\frac{2}{\pi \Gamma_{A}} \operatorname{Re}\left[\left(\frac{\omega+i \Gamma_{K}}{i \Gamma_{K}}\right)^{-1 / 2}\right] \\
& =\frac{2}{\pi \Gamma_{A}}\left(\frac{1+\sqrt{1+\left(\omega / \Gamma_{K}\right)^{2}}}{2\left(1+\left(\omega / \Gamma_{K}\right)^{2}\right)}\right)^{1 / 2},
\end{aligned} \quad \text { (B11) }
$$

with $\Gamma_{A}$ and $\Gamma_{K}$ being fitting parameters. However, it should be noted that this formula is a phenomenological parameterization of the model and is not able to predict the temperature dependence of LDOS and its width [42].

[1] P. Anderson, MRS Bull. 8, 153 (1973).
[2] P. Fazekas and P. W. Anderson, Philosophical Magazine 30, 423 (1974).
[3] P. W. Anderson, Science 235, 1196 (1987).
[4] C. Broholm, R. J. Cava, S. A. Kivelson, D. G. Nocera, M. R. Norman, and T. Senthil, Science 367, eaay0668 (2020).
[5] L. Savary and L. Balents, Rep. Prog. Phys. 80, 016502 (2016).
[6] Y. Zhou, K. Kanoda, and T.-K. Ng, Rev. Mod. Phys. 89, 025003 (2017).
[7] K. T. Law and P. A. Lee, Proc. Natl. Acad. Sci. U.S.A. 114, 6996 (2017).
[8] W.-Y. He, X. Y. Xu, G. Chen, K. T. Law, and P. A. Lee, Phys. Rev. Lett. 121, 046401 (2018).
[9] K. Rossnagel, J. Phys. Condens. Matter 23, 213001 (2011).
[10] M. Kratochvilova, A. D. Hillier, A. R. Wildes, L. Wang, S.-W. Cheong, and J.-G. Park, npj Quantum Materials 2, 42 (2017).
[11] M. Klanjšek, A. Zorko, R. Žitko, J. Mravlje, Z. Jagličić, P. K. Biswas, P. Prelovšek, D. Mihailovic, and D. Arčon, Nat. Phys. 13, 1130 (2017).
[12] TOSATTI, E. and FAZEKAS, P., J. Phys. Colloques 37, C4 (1976).
[13] J. Wilson, F. D. Salvo, and S. Mahajan, Adv. Phys. 24, 117 (1975).
[14] A. Ribak, I. Silber, C. Baines, K. Chashka, Z. Salman, Y. Dagan, and A. Kanigel, Phys. Rev. B 96, 195131 (2017).
[15] Y. J. Yu, Y. Xu, L. P. He, M. Kratochvilova, Y. Y. Huang, J. M. Ni, L. Wang, S.-W. Cheong, J.-G. Park, and S. Y. Li, Phys. Rev. B 96, 081111 (2017).
[16] H. Murayama, Y. Sato, T. Taniguchi, R. Kurihara, X. Z. Xing, W. Huang, S. Kasahara, Y. Kasahara, I. Kim- chi, M. Yoshida, Y. Iwasa, Y. Mizukami, T. Shibauchi, M. Konczykowski, and Y. Matsuda, Phys. Rev. Research 2, 013099 (2020).
[17] K. Rossnagel and N. V. Smith, Phys. Rev. B 73, 073106 (2006).
[18] F. Di Salvo, R. Maines, J. Waszczak, and R. Schwall, Solid State Commun. 14, 497 (1974).
[19] Y. Chen, W. Ruan, M. Wu, S. Tang, H. Ryu, H.-Z. Tsai, R. Lee, S. Kahn, F. Liou, C. Jia, O. R. Albertini, H. Xiong, T. Jia, Z. Liu, J. A. Sobota, A. Y. Liu, J. E. Moore, Z.-X. Shen, S. G. Louie, S.-K. Mo, and M. F. Crommie, Nat. Phys. 16, 218 (2020).
[20] W. Ruan, Y. Chen, S. Tang, J. Hwang, H.-Z. Tsai, R. Lee, M. Wu, H. Ryu, S. Kahn, F. Liou, C. Jia, A. Aikawa, C. Hwang, F. Wang, Y. Choi, S. G. Louie, P. A. Lee, Z.-X. Shen, S.-K. Mo, and M. F. Crommie, arXiv e-prints , arXiv:2009.07379 (2020), arXiv:2009.07379 [cond-mat.str-el].
[21] S. Doniach, Physica B+C 91, 231 (1977).
[22] A. C. Hewson, The Kondo Problem to Heavy Fermions, Cambridge Studies in Magnetism (Cambridge University Press, 1993).
[23] P. Coleman, Introduction to Many-Body Physics (Cam- bridge University Press, 2015).
[24] S. Florens and A. Georges, Phys. Rev. B 70, 035114 (2004).
[25] S.-S. Lee and P. A. Lee, Phys. Rev. Lett. 95, 036403 (2005).
[26] O. I. Motrunich, Phys. Rev. B 72, 045105 (2005).
[27] V. Sunko, F. Mazzola, S. Kitamura, S. Khim, P. Kush- waha, O. J. Clark, M. D. Watson, I. Marković, D. Biswas, L. Pourovskii, T. K. Kim, T.-L. Lee, P. K. Thakur, H. Rosner, A. Georges, R. Moessner, T. Oka, A. P. Mackenzie, and P. D. C. King, Science Advances 6, 10.1126/sciadv.aaz0611 (2020).
[28] E. Zhao and A. Paramekanti, Phys. Rev. B 76, 195101 (2007).
[29] K. Nagaoka, T. Janneala, M. Grobis, and M. F. Crom- mie, Phys. Rev. Lett. 88, 077205 (2002).

[30] N. Read and D. M. Newns, *Journal of Physics C: Solid State Physics* **16**, 3273 (1983).

[31] N. Read and D. M. Newns, *Journal of Physics C: Solid State Physics* **16**, L1055 (1983).

[32] P. Coleman, *Phys. Rev. B* **29**, 3035 (1984).

[33] A. Auerbach and K. Levin, *Phys. Rev. B* **34**, 3524 (1986).

[34] L. Zheng and S. Das Sarma, *Phys. Rev. B* **53**, 9964 (1996).

[35] K. Yamada, *Prog. Theor. Exp. Phys.* **53**, 970 (1975).

[36] T. A. Costi, A. C. Hewson, and V. Zlatic, *J. Phys. Condens. Matter* **6**, 2519 (1994), 9310032.

[37] P. Coleman, *Journal of Magnetism and Magnetic Materials* **47-48**, 323 (1985).

[38] R. Franco, M. S. Figueira, and M. E. Foglio, *Phys. Rev. B* **66**, 045112 (2002).

[39] T. Senthil, M. Vojta, and S. Sachdev, *Phys. Rev. B* **69**, 035111 (2004).

[40] T. Senthil, *Phys. Rev. B* **78**, 045109 (2008).

[41] H. O. Frota and L. N. Oliveira, *Phys. Rev. B* **33**, 7871 (1986).

[42] H. O. Frota, *Phys. Rev. B* **45**, 1096 (1992).