# Finite-temperature properties of the generalized Falicov-Kimball model

S. El Shawish, $^{1}$ J. Bonča, $^{1,2}$ and C. D. Batista $^{3}$

$^{1}$J. Stefan Institute, SI-1000 Ljubljana, Slovenia
$^{2}$Faculty of Mathematics and Physics, University of Ljubljana, SI-1000 Ljubljana, Slovenia
$^{3}$Theoretical Division, Los Alamos National Laboratory, Los Alamos, New Mexico 87545, USA

(Received 4 July 2003; published 18 November 2003)

The thermodynamic properties of the extended Falicov-Kimball model (FKM) for spinless fermions are studied as a function of temperature, doping, and interlevel spacing on the two-dimensional lattice. Thermodynamic quantities are calculated using the finite-temperature Lanczos method with additional phase averaging for a system of $4×4$ sites. Changes of the thermodynamic properties are studied as the system evolves from its symmetric limit represented by the original Hubbard model to the other limiting case, which corresponds to the original FKM for spinless fermions. Our results indicate that valence transition exists in the extended Falicov-Kimball model.

DOI: 10.1103/PhysRevB.68.195112
PACS number(s): 71.27.+a, 71.10.Fd

## I. INTRODUCTION

The Falicov-Kimball model (FKM) was originally proposed to explain a metal-insulator transition that occurs in transition-metals and rare-earth compounds. In its original version, $^{1}$ the FKM consists of localized $f$ orbitals which interact with a dispersive band of $d$ orbitals through an on-site Coulomb repulsion. There is no hybridization between the two bands. The FKM has also been extensively used to describe valence transitions in intermediate valence compounds. A renewed interest in this model started when Portengen et al. $^{2}$ suggested that the FKM might lead to the formation of a Bose-Einstein condensate of $d$-$f$ excitons. Such a state has a built in macroscopic electric polarization. This suggestion was later supported by the exact solution of the FKM in infinite dimensions. $^{3}$

Recently, one of us showed that electronically driven ferroelectricity exists in the strong coupling regime of an extended FKM (Ref. 4) with no extra hybridization between the $f$ and $d$ orbitals. The existence of this new mechanism opens the door to new technological applications due to the strong coupling between the orbital and the spin degrees of freedom of each electron: $^{4}$ for instance, a magnetic field can be used as a switch for the ferroelectric state.

The spontaneous ferroelectric state that exists in the mixed-valence regime of the extended FKM is the consequence of a coherent spontaneous hybridization between two atomic orbitals with opposite parity under spatial inversion ($f$ and $d$ in our case). $^{4}$ This state competes with an orbitally ordered (chessboardlike) state that is also realized in the mixed valence regime. The most important ingredients necessary for the realization of the electrically polarized state are (a) the system has to be in the mixed valence regime, (b) the two orbitals which are involved must have opposite parity under spatial inversion, (c) a finite Coulomb repulsion $U^{fd}$ between electrons occupying different bands is required, (d) it is better if both bands have similar bandwidths, and (e) hybridization between bands is not necessary although it plays an important role in defining the nature of the low energy spectrum of the ferroelectric state. $^{4}$

For simplicity, we will consider an extended FKM for spinless fermions. Although the spin degrees of freedom can play an important role due to the coupling with the orbital flavor, $^{4}$ the philosophy of the present work is to isolate the orbital degrees of freedom, which are responsible for the ferroelectricity, in order to simplify the study of its thermodynamic properties. The Hamiltonian defined on a square lattice is given by

$$
\begin{aligned}
H= & \epsilon_{d} \sum_{\mathbf{i}} n_{\mathbf{i}}^{d}+\epsilon_{f} \sum_{\mathbf{i}} n_{\mathbf{i}}^{f}-t_{d} \sum_{\langle\mathbf{i j}\rangle} d_{\mathbf{i}}^{\dagger} d_{\mathbf{j}}+U^{f d} \sum_{\mathbf{i}} n_{\mathbf{i}}^{d} n_{\mathbf{i}}^{f} \\
& +t_{f} \sum_{\langle\mathbf{i j}\rangle} f_{\mathbf{i}}^{\dagger} f_{\mathbf{j}},
\end{aligned}
$$

where $n_{\mathbf{i}}^{f}=f_{\mathbf{i}}^{\dagger} f_{\mathbf{i}}$ and $n_{\mathbf{i}}^{d}=d_{\mathbf{i}}^{\dagger} d_{\mathbf{i}}$ are the $f$- and $d$-orbital occupation numbers on site $\mathbf{i}$. The sum $\langle\mathbf{i j}\rangle$ runs over pairs of nearest-neighbor sites. For historical reasons we have named the orbitals $d$ and $f$, but these two labels can represent any pair of orbitals with opposite parity under a spatial inversion.

While the original FKM can be viewed as a single-particle problem at zero temperature, this is not the case for the extended model given by Eq. (1). This model can be exactly mapped into an asymmetric Hubbard model (AHM). $^{4}$ After this mapping, the orbital flavor is replaced by a pseudo spin variable: $c_{\mathbf{i} \uparrow}=f_{\mathbf{i}}$ and $c_{\mathbf{i} \downarrow}=d_{\mathbf{i}}$. Replacing these expressions in Eq. (1), we get the desired expression for $H$:

$$
\begin{aligned}
H= & \epsilon \sum_{\mathbf{i}, \sigma} n_{\mathbf{i} \sigma}-\sum_{\langle\mathbf{i j}\rangle, \sigma} t_{\sigma}\left(c_{\mathbf{i} \sigma}^{\dagger} c_{\mathbf{j} \sigma}+c_{\mathbf{j} \sigma}^{\dagger} c_{\mathbf{i} \sigma}\right)+U^{f d} \sum_{\mathbf{i}} n_{\mathbf{i} \uparrow} n_{\mathbf{i} \downarrow} \\
& +B_{z} \sum_{\mathbf{i}} \tau_{\mathbf{i}}^{z},
\end{aligned}
$$

where $\epsilon=(\epsilon_{d}+\epsilon_{f})/2$ and $B_{z}=\epsilon_{f}-\epsilon_{d}$ and $\tau_{\mathbf{i}}^{z}=(n_{\mathbf{i}}^{f}-n_{\mathbf{i}}^{d})/2$. Without any loss of generality we set $\epsilon=0$ since a finite $\epsilon$ merely represents a shift of the chemical potential. When the original bands have the same dispersion, i.e., $t_{f}=t_{d}=t_{\sigma}$, $H$ is reduced to the original Hubbard model with additional Zeeman coupling to an external magnetic field. For the general case, the SU(2) symmetry of the original Hubbard model is reduced to a U(1) symmetry due to the presence of the

Zeeman term and the different hopping amplitudes for each spin polarization ($t_\uparrow \neq t_\downarrow$). The generator of this U(1) symmetry is $\tau^z=\sum_{\mathbf{i}} \tau_{\mathbf{i}}^z$, and the associated conserved quantity is the difference between the total number of particles in each band. We use these conservation laws in building our numerical method. It is also important to note that in the new version of our original model, the $z$ component of the total magnetization couples to the difference between the populations of both bands. Therefore, in the new language the valence instabilities are described as metamagnetic or spin-flop (finite jump in the magnetization) transitions. In a real system, the value of $B_z$ is varied by applying pressure or by alloying. In addition, the orbitally ordered state (chessboard-like) and the Bose-Einstein condensation of excitons are represented by longitudinal (along to the $z$ axis) and transverse (xy-like) spin density waves, respectively. $^{4}$

In our finite-temperature study we will focus on the investigation of the thermodynamic properties of the AHM [Eq. (2)] as a function of temperature, doping and external magnetic field. Note that the external magnetic field corresponds to the energy difference between the centers of both bands in our original version of the extended FKM [see Eq. (1)]. There are two main goals of our investigation. First, we want to gain a deeper physical understanding of the AHM by studying its thermodynamic properties. The motivation of such investigation is primarily coming from the recently established electronically driven spontaneous polarization. $^{4}$ Second, we want to study how the valence instabilities are affected by the inclusion of a realistic hopping integral for the lower band.

## II. METHOD

We study numerically the asymmetric Hubbard model on a square lattice using the finite temperature Lanczos method (FTLM) (Refs. 5 and 6) with the additional phase averaging explained in detail in Refs. 7 and 8. In short, the method is based on the Lanczos procedure of exact diagonalization with a random sampling over initial wave functions and phases representing the effect of a uniform vector potential. $^{7,8}$ There are many advantages of this method in comparison to more standard methods as are the hightemperature expansion techniques and quantum Monte Carlo calculations. The method connects continuously the highand low- temperature regimes. There is no minus-sign problem, and the method applies well almost independently of the Hubbard coupling strength $U^{f d}$; nevertheless the best results are achieved in the intermediate to strong coupling regime. The main limitation to the validity of the results comes from finite-size effects which appear at $T<T_{f s}$. The $T_{f s}$ strongly depends on the physical properties of the system. For gapless systems, a criterion for $T_{f s}$ defined through the thermodynamic sum $\bar{Z}(T)=\operatorname{Tr} \exp \left(-\left(H-E_{0}\right) / T\right)$ calculated in a given system at fixed particle number $N_{e}$ can be used together with the requirement $\bar{Z}\left(T_{f s}\right)=Z^{*} \geqslant 1 .{ }^{6}$ If there is a gap in the excitation spectrum, as is the case for $t_{\uparrow} \neq t_{\downarrow}$, this criterion can be relaxed $\left(Z^{*} \geq 1\right)$ leading to substantially lower $T_{f s}$.

The calculation of the thermodynamic properties for the original FKM $(t_{\uparrow}=0)$ does not require a solution of a manybody problem, since in this case, the spin-up local occupation number is a good quantum number with two possible values: $w_{i}=1$ or $w_{i}=0 .^{9-12}$ Therefore, for a given spin-up electron configuration $w=\{w_{1}, w_{2}, \ldots, w_{L}\}$, the model Hamiltonian [Eq. (2)] represents a noninteracting problem for spin-down electrons moving in a fixed potential created by spin-up electrons. The ground state energy of such system is just the sum over the number of spin-down lowest singleparticle energies. The thermodynamic properties are obtained by a summation over all possible configurations of spin-up electrons $w=\{w_{1}, w_{2}, \ldots, w_{L}\}$ on small square clusters with $L$ sites $(L=16,20)$. In order to compensate for the small size of the clusters, the thermal properties of the system are investigated via the grand canonical ensemble and averaged over different boundary conditions as in the case of the Hubbard model. In this way the results are considerably improved in general and more specifically for the largest dopings $n \sim 0.6-0.8$. It is also important to note that the FTLM could as well be used to compute thermodynamic properties of the FKM (on $4 \times 4$ lattice), however with a significantly larger computational effort. We will show that the results obtained for the original FKM summing over all the possible configurations of the spin-up electrons are very similar to the ones obtained with the FTLM for $t_{\uparrow} / t_{\downarrow}=0.1$. This provides an additional test for both methods.

## III. RESULTS

### A. Entropy and specific heat

Using the FTLM with additional phase averaging on 4 $\times 4$ lattice for $t_{\uparrow} / t_{\downarrow} \neq 0$ and sampling over all possible noninteracting states for the case of $t_{\uparrow}=0$ we evaluate the entropy density $s$:

$$
s=\ln \Omega / N+\left(\langle H\rangle-\mu\left\langle N_{e}\right\rangle\right) / N T, \quad \text { (3) }
$$

where $N_{e}$ is the total electron-number operator connected to electron-density through $n=n_{\uparrow}+n_{\downarrow}=\left\langle N_{e}\right\rangle / N$. From $s$ we also evaluate the specific heat $C_{V}=T(\partial s / \partial T)_{n}$.

In Fig. 1 we present $C_{V}(T)$ for $U^{f d}=8$, different ratios of $t_{\uparrow} / t_{\downarrow}=1.0,0.3,0.1$, and 0.0 , and $B_{z}=0$. We first comment on results calculated at half-filling, i.e., $n=1$. The case $t_{\uparrow} / t_{\downarrow}$ $=1$ corresponds to the original SU(2) invariant Hubbard model. The low energy peak at $n=1$ is associated with spin excitations. In terms of our original model, these spin excitations represent the Goldstone modes of the orbital ordering and the Bose-Einstein condensation of excitons which are degenerate at the SU(2) invariant point. In the large $U^{f d}$ limit, $U^{f d}>W=4(t_{\uparrow}+t_{\downarrow})$, this peak is approximately located at $T / t_{\downarrow}=8 t_{\downarrow} / 3 U^{f d} \cdot{ }^{7,13}$ In this limit, the low energy physics of the Hubbard model for $n=1$ can be mapped into a Heisenberg model. The broad high-energy peak located around $T \sim U^{f d} / 4.8$ is associated with charge excitations. $^{13}$ Decreasing the ratio $t_{\uparrow} / t_{\downarrow}$, the low-energy peak becomes substantially sharper and moves towards lower temperatures.


![](./images/812376854441754624_1.jpg)

FIG. 1. (Color online) Specific heat $C_V$ (per unit cell) vs $T$ for $U^{fd}=8$, $B_z=0$, various electron densities $n$, and different ratios of $t_\uparrow/t_\downarrow$. Tiny dashed lines represent $C_V$ for the $S=1/2$ $XXZ$ model (also see the text).

At $t_\uparrow=0$, i.e., for the original version of the FKM, our calculations qualitatively agree with the results of Farkašovský. $^{11}$

The low temperature behavior of $C_V$ at $n=1$ is easy to understand if we take into consideration that the low energy spectrum of the AHM maps into an $S=1/2$ $XXZ$ model in the strong coupling regime. The effective couplings are: $J_z=2(t_\uparrow^2+t_\downarrow^2)/U^{fd}$ and $J_\perp=4t_\uparrow t_\downarrow/U^{fd}$. $^4$ The $C_V(T)$ curves calculated with an $XXZ$ model on 20 lattice sites are presented in Fig. 1 with tiny dashed lines for $t_\uparrow/t_\downarrow=0.3$, 0.1, and 0. The peak positions and the widths are well captured by this effective model even though the ratio $U^{fd}/W$ is not so high. The $XXZ$ model becomes an Ising model when $J_\perp=0$. If we consider that the Ising variables take the values $\pm1$, the effective coupling becomes $J_{Ising}=J_z/4=t_\downarrow^2/2U^{fd}$. The $C_V$ of the Ising model has a logarithmic singularity at the phase transition temperature $T_c\sim2.27J_{Ising}\sim1.14t_\downarrow^2/U^{fd}$ which roughly agrees with the position of the low temperature peak at $t_\downarrow=0$. Due to obvious limitations in the size of our system we cannot study the development of the singularity in the specific heat that is expected for the thermodynamic limit. Instead of this singularity, we observe a finite peak which becomes sharper for lower values of $t_\uparrow/t_\downarrow$, since the effective model becomes more Ising-like.

There is a substantial difference in $C_V$ between the symmetric and asymmetric Hubbard models at low temperatures. In the symmetric case, the low temperature behavior is governed by the two-dimensional AFM magnon spectra which leads to $C_V\propto T^2$, while for $t_\uparrow/t_\downarrow\neq1$ a gap opens in the magnon spectrum leading to an exponentially activated behavior of $C_V$. Those details cannot be clearly seen in Fig. 1 because we are unable to study the system at low enough temperatures.

At small doping away from half-filling, e.g., $n=0.9$, the low temperature peak at $t_\uparrow/t_\downarrow=1$ substantially diminishes, while for $t_\uparrow/t_\downarrow<1$ it moves toward smaller temperatures indicating a softening of the low energy collective excitations. At even larger dopings, e.g., $n\lesssim0.7$, the two peaked structure completely disappears. In the symmetric limit, $C_V$ approaches the result for noninteracting electrons, while for $t_\uparrow/t_\downarrow\neq1$ an asymmetric peak develops at $T/t_\downarrow\sim0.25$ and at even lower temperatures $C_V$ exponentially approaches zero. This rather unexpected difference is caused by the fact that doping away from half-filling turns the asymmetric system into a band ferromagnet. As we will see below, this band ferromagnetism is reinforced by the addition of the Coulomb repulsion $U^{fd}$. Band ferromagnetism is caused by the different dispersion of spin up and spin down bands. It is energetically convenient to remove more fermions from the $f$ band because it has a higher density of states.

![](./images/812376854441754624_2.jpg)

FIG. 2. (Color online) Entropy density $s$ vs $T$ for $U^{fd}=8$, $B_z=0$, various electron densities $n$, and different ratios of $t_\uparrow/t_\downarrow$.

In Fig. 2 we present the results for the entropy density $s$ defined in Eq. (3). While most of the physical interpretation given in the previous paragraphs applies equally well to the analysis of $s$, examining Fig. 2 gives a new perspective. For $n=1$ we observe the increase in $s$ with temperature that becomes steeper as the ratio $t_\uparrow/t_\downarrow$ decreases. This can easily be explained with the flattening of the band for spin up electrons. The plateau located near $s\sim\ln(2)$, which also becomes more pronounced with decreasing the ratio $t_\uparrow/t_\downarrow$, is caused by the strong Coulomb interaction $U^{fd}$ which introduces a gap for charge excitations. The value of the charge gap is proportional to $U^{fd}$ in the strong coupling limit. The position of the plateau in Fig. 2 and $t_\uparrow/t_\downarrow\gtrsim0$ corresponds to a deep in $C_V$, seen in Fig. 1, while the gradual increase of $s$ at higher temperatures, i.e., $T/t_\downarrow\gtrsim0.6$, corresponds to formation of the broad high temperature peak in $C_V$ whose position is governed by $U^{fd}$.

### B. Spin susceptibility and magnetization

We next turn to the uniform spin susceptibility defined as $\chi_s^z=\partial M/\partial B_z$ with $M=\langle S_z\rangle/N$. In terms of the original vari-

![](./images/812376854441754624_3.jpg)

FIG. 3. (Color online) Spin susceptibility $\chi_{s}^{z}$ vs $T$ for $U^{fd}=8$, $B_{z}=0$, various electron densities $n$, and different ratios of $t_{\uparrow}/t_{\downarrow}$. Insets present noninteracting $\chi_{s}^{z}(T)$ calculated on the infinite square lattice for the same values of $n$ as in finite-$U^{fd}$ cases.

ables, $\chi_{s}^{z}$ represents the charge-transfer susceptibility, i.e., a large value of $\chi_{s}^{z}$ indicates that the system is close to a valence instability. This valence instability can be induced by applying pressure. In Fig. 3 we show the calculated spin susceptibility $\chi_{s}^{z}(T)$. A peak is located around $T^{*}\sim0.3t_{\downarrow}$ for $t_{\uparrow}/t_{\downarrow}=1$ and $n=1$. With lowering the temperature, $\chi_{s}^{z}(T)$ slightly decreases and saturates, which is a signature of the formation of antiferromagnetic correlations. $^{6}$ Decreasing the doping, this peak shifts to lower temperatures. In the anisotropic case, e.g., $t_{\uparrow}/t_{\downarrow}<1$, $\chi_{s}^{z}(T)$ displays a considerably different behavior at low temperatures and for all fillings. At half-filling, $n=1$, $\chi_{s}^{z}(T)$ approaches zero at low temperatures. This is a consequence of the spin gap introduced by the Ising-like anisotropy $(J_{\perp}=2(t_{\uparrow}^{2}+t_{\downarrow}^{2})/U^{fd}$ and $J_{z}=4t_{\uparrow}t_{\downarrow}/U^{fd})$ associated with the asymmetric regime. $^{4}$ At a lower band filling, $n\sim0.8$, $\chi_{s}^{z}$ seems to saturate displaying a Pauli like behavior. At even lower fillings, $n\leq0.7$, it again approaches zero. For comparison we also show, in the insets of Fig. 3, noninteracting $\chi_{s}^{z}$ for $t_{\uparrow}/t_{\downarrow}=0.3,0.1,0$. A logarithmic divergence of noninteracting $\chi_{s}^{z}$ at $n=1$ and low $T$, seen in $t_{\uparrow}/t_{\downarrow}=0.3,0.1$ and for all fillings in $t_{\uparrow}=0$ system, is a consequence of the divergent density of states near the Fermi level. A more detailed understanding of the behavior of $\chi_{s}^{z}$ at various band fillings can be obtained by inspecting the magnetization $M=(n_{\uparrow}-n_{\downarrow})/2$ as a function of filling $n$ which is presented in Fig. 4. $M$ is zero for any filling in the symmetric limit. In contrast, a finite magnetization is obtained when doping the asymmetric system $(t_{\uparrow}\neq t_{\downarrow})$ away from halffilling. As the band filling decreases, a larger number of spin-up electrons is removed from the system due to higher density of states of the spin-up polarization band at the Fermi level. The effect of finite interaction at smaller fillings, $n<1$, is to increase the magnetization in comparison to its noninteracting value (see the insets of Fig. 4). For $U^{fd}=0$, the magnetization peaks at $n^{*}=0.5$ with a maximum value of $M(n=1/2,T=0)=-n/2=-0.25$. At finite $U^{fd}$, for all the interacting cases presented in Fig. 4, the peak value $M(n^{*})$ exceeds the noninteracting limit. If $t_{\uparrow}=0$, $M(n)$ nearly follows its saturated value $M=-n/2$, presented with a tiny dashed line in the interval $n\leq0.7$. This also explains why $\chi_{s}^{z}(T)$ approaches zero at lower fillings for the asymmetric case. Therefore, even though the ferromagnetism is a band effect, a finite Coulomb repulsion $U^{fd}$ enhances the magnetization. This is an expected behavior, since by transferring charge from the band with lower occupancy to the more populated one, the interband Coulomb energy is reduced.

![](./images/812376854441754624_4.jpg)

FIG. 4. (Color online) Magnetization $M$ (per unit cell) vs $n$ for $U^{fd}=8$, $B_{z}=0$, various temperatures $T$, and different ratios of $t_{\uparrow}<t_{\downarrow}$. Tiny dashed lines represent $T=0$ and the $U^{fd}=0$ saturation limit $-M=n/2$. Insets present noninteracting $M(T)$ calculated on the infinite square lattice for the same values of $T$ as in finite-$U^{fd}$ cases.

### C. Thermodynamics at finite $B_{z}$

In this subsection we focus on the thermodynamic properties at half-filling, $n=1$, as a function of the pseudomagnetic field $B_{z}=\epsilon_{f}-\epsilon_{d}$, which in the original version of the extended FKM [Eq. (1)] represents the energy difference between the centers of the $f$ and $d$ bands. Starting with $C_{V}(T)$ shown in Fig. 5, we first notice that the effect of $B_{z}$ on the low-$T$ behavior of $C_{V}(T)$ changes substantially between the symmetric and asymmetric limits. While the effect of increasing $B_{z}$ is small for $t_{\uparrow}=t_{\downarrow}$, a much more pronounced change is observed in the asymmetric case. In particular, increasing $B_{z}$ for the symmetric case in the interval $0\leq B_{z}<t_{\downarrow}$ only diminishes the low-$T$ peak slightly. In contrast, if $t_{\uparrow}=0.3t_{\downarrow}$, the low-$T$ peak moves toward smaller temperatures and broadens in the regime $B_{z}\lesssim0.8t_{\downarrow}$. For $B_{z}\gtrsim0.8t_{\downarrow}$ only a broad shoulder remains visible. For even smaller ratios of the hoppings, $t_{\uparrow}=0.1t_{\downarrow},0$, and $B_{z}\gtrsim0.4t_{\downarrow}$, the low-$T$ peak either completely disappears or moves to temperatures which are not accessible to our calculations. $C_{V}(T)$ is small and nearly $T$ independent at low temperatures, $0.05<T/t_{\downarrow}<0.5$, in the interval $0.4<B_{z}/t_{\downarrow}<0.6$. Such a behavior indicates that the entropy increases at low $T$. As we can see in Fig. 6, the magnetization changes very rapidly in this interval of magnetic fields. For larger values of the magnetic field,

![](./images/812376854441754624_5.jpg)

FIG. 5. (Color online) Specific heat $C_V$ (per unit cell) vs $T$ for $U^{fd}=8$, $n=1$, various values of $B_z$, and different ratios of $t_\uparrow/t_\downarrow$.

$B_z\geq 0.8t_\downarrow$, the low-$T$ behavior of $C_V(T)$ again shows the activated behavior of gaped systems. In terms of the original language, this band gap originates from the complete transfer of charge from the $d$ band to the $f$ band. In terms of the spin variables, the magnetization is saturated ($M=-n/2$), and there is an energy gap proportional to $|B_z-B_z^c|$ ($B_z^c$ is the critical field that saturates the magnetization).$^{4}$

In Fig. 6, we also show $M(T,B_z)$ for different values of asymmetry ratio $t_\uparrow/t_\downarrow$ and $n=1$. Note that for $B_z=0$, $M(T)=0$ in all the cases. While at high temperature, i.e., $T/t_\downarrow>1$, $M(T,B_z)$ shows a small variance between systems with different values of $t_\uparrow/t_\downarrow$, the change is much more pronounced at small temperatures. In the symmetric limit, $M(T,B_z)$ changes nearly linearly with increasing $B_z$. Away from this limit, a strong nonlinear behavior resembling an Ising-like metamagnetic transition is observed at low temperatures for $t_\uparrow/t_\downarrow\sim 0.3$. This behavior is more pronounced near $t_\uparrow\sim 0$. A metamagnetic transition in the asymmetric Hubbard model corresponds to a valence transition in the extended FKM. Due to our limitation to small system sizes that is reflected in our inability to extend the calculation to smaller temperatures, we are unable to determine whether the jump in $M(T\rightarrow 0,B_z)$ is discontinuous for $t_\uparrow<t_\downarrow$ or not. However, quantum Monte Carlo simulations of the $XXZ$ model$^{14}$ in very large clusters show that there is a discontinuous change of the magnetization as a function of $B_z$. A finite jump can also be seen at $t_\uparrow=0$ and $B_c\sim 0.4t_\downarrow$ presented in the inset of Fig. 6, where we show $M(T)$ for a large number of chosen values of $B_z$. This is also in agreement with the investigations of the FKM on small clusters$^{15}$ and in infinite dimensions.$^{9}$ The existence of an Ising-like metamagnetic transition was clearly established for the strong coupling regime in Ref. 4.

The discontinuous change of $M$ as a function of $B_z$ is associated with a first order quantum phase transition between the Ising-like (orbital ordering) antiferromagnetic phase with $M=0$ and the $xy$-like (Bose-Einstein condensation of excitons) phase that has a finite value of $M^4$. In other words, the transition between orbital ordering and the Bose-Einstein condensation of excitons is also a valence transition.

![](./images/812376854441754624_6.jpg)

FIG. 6. (Color online) Magnetization $M$ (per unit cell) vs $T$ for $U^{fd}=8$, $n=1$, various values of $B_z$, and different ratios of $t_\uparrow/t_\downarrow$. The inset shows a blowup region of $M$ for a large number of $B_z$ $=0.05,0.1,\dots 0.7$. The critical value $B_c\sim 0.4$ is represented with a thicker line.

## IV. CONCLUSIONS

We have studied the thermodynamic properties of the asymmetric Hubbard model as a function of $T$, $n$, and $B_z$. In particular, we followed the change of the thermodynamic properties as the system evolves from its symmetric limit represented by the original Hubbard model ($t_\uparrow=t_\downarrow$) to the other limiting case, $t_\downarrow=0$, which corresponds to the original FKM for spinless fermions. The results of $C_V(T)$ for $n=1$ and $B_z=0$ always show two peaks: a low-$T$ peak associated with low-energy collective spin excitations (orbital excitations in the original language) and a high-energy peak that corresponds to charge excitations. More pronounced differences between the symmetric and asymmetric regimes appear in the specific heat away from half-filling. This effect is related to the band ferromagnetism produced by the different hopping amplitudes of each spin polarization, which is in addition enhanced by the presence of a strong Coulomb interaction. The enhancement of ferromagnetism by $U^{fd}$ is clearly seen in the $M(n)$ plots where the saturation value of the magnetization ($M=-n/2$) is reached in a wide interval of densities and temperatures. The magnetization can be up to three times higher for $U^{fd}=8t_\downarrow$ than for the noninteracting limit. In terms of our original variables, the large change of the magnetization indicates the presence of a valence instability.

The response of the system to the external magnetic field $B_z$ or the shift of the $f$ level position in the original FKM strongly depends on the ratio of $t_\uparrow/t_\downarrow$ as well. In the symmetric limit, we obtain small changes of $C_V$ as $B_z$ is varied in the interval $0<B_z/t_\downarrow<1$. In the asymmetric case, $B_z$ is

much more effective in softening and suppressing collective spin excitations causing the shift and suppression of the low- $T$ peak of $C_V$, which is accompanied by a rapid change of the magnetization with increasing $B_z$. The rapid change in magnetization represents a valence transition driven by the shift of the $f$ level position in the original FKM. Our results indicate that this valence transition exists in the extended FKM for the whole range of hopping ratios $t_\uparrow<t_\downarrow$ and disappears when this ratio becomes equal to one.

## ACKNOWLEDGMENT
The authors acknowledge the support of the Ministry of Education, Science and Sport of Slovenia.

$^{1}$L.M. Falicov and J.C. Kimball, Phys. Rev. Lett. 22, 997 (1969).

$^{2}$T. Portengen, Th. Östreich, and L.J. Sham, Phys. Rev. Lett. 76, 3384 (1996); Phys. Rev. B 54, 17 452 (1996).

$^{3}$V. Zlatić, J.K. Freericks, R. Lemanski, and G. Czycholl, Philos. Mag. B 81, 1443 (2001).

$^{4}$C.D. Batista, Phys. Rev. Lett. 89, 166403 (2002).

$^{5}$J. Jaklič and P. Prelovšek, Phys. Rev. Lett. 77, 892 (1996).

$^{6}$J. Jaklič and P. Prelovšek, Adv. Phys. 49, 1 (2000).

$^{7}$J. Bonča and P. Prelovšek, Phys. Rev. B 67, 085103 (2003).

$^{8}$D. Poilblanc, Phys. Rev. B 44, 9562 (1991).

$^{9}$J.K. Freericks and V. Zlatić, Phys. Rev. B 58, 322 (1998).

$^{10}$J.K. Freericks, Phys. Rev. B 47, 9263 (1993).

$^{11}$P. Farkašovský, Z. Phys. B: Condens. Matter 102, 91 (1997).

$^{12}$C.A. Macêdo, L.G. Azevedo, and A.M.C. de Souza, Phys. Rev. B 64, 184441 (2001).

$^{13}$T. Paiva, R.T. Scalettar, C. Huscroft, and A.K. McMahan, Phys. Rev. B 63, 125116 (2001).

$^{14}$G. Schmid, S. Todo, M. Troyer, and A. Dorneich, Phys. Rev. Lett. 88, 167208 (2002).

$^{15}$P. Farkašovský, Phys. Rev. B 52, R5463 (1995); 54, 11 261 (1996).