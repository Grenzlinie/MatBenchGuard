SciPost Phys. 7, 046 (2019)

# Unfrustrating the $t$-$J$ model:
d-wave BCS superconductivity in the $t'$-$J_z$-$V$ model

Kevin Slagle$^{1,2\star}$

1 Walter Burke Institute for Theoretical Physics,
California Institute of Technology, Pasadena, California 91125, USA
2 Institute for Quantum Information and Matter,
California Institute of Technology, Pasadena, California 91125, USA

$\star$ kslagle@caltech.edu

## Abstract
The $t$-$J$ model is believed to be a minimal model that may be capable of describing the low-energy physics of the cuprate superconductors. However, although the $t$-$J$ model is simple in appearance, obtaining a detailed understanding of its phase diagram has proved to be challenging. We are therefore motivated to study modifications to the $t$-$J$ model such that its phase diagram and mechanism for d-wave superconductivity can be understood analytically without making uncontrolled approximations. The modified model we consider is a $t'$-$J_z$-$V$ model on a square lattice, which has a second-nearest-neighbor hopping $t'$ (instead of a nearest-neighbor hopping $t$), an Ising (instead of Heisenberg) antiferromagnetic coupling $J_z$, and a nearest-neighbor repulsion $V$. In a certain strongly interacting limit, the ground state is an antiferromagnetic superconductor that can be described exactly by a Hamiltonian where the only interaction is a nearest-neighbor attraction. BCS theory can then be applied with arbitrary analytical control, from which nodeless d-wave or s-wave superconductivity can result

![](./images/812727153731829760_1.jpg)
Copyright K. Slagle.
This work is licensed under the Creative Commons
Attribution 4.0 International License.
Published by the SciPost Foundation.

Received 03-08-2019
Accepted 01-10-2019
Published 09-10-2019
doi:10.21468/SciPostPhys.7.4.046
![](./images/812727153731829760_2.jpg)

## Contents
1 Introduction 2

2 $t'$-$J_z$-$V$ Model 3
2.1 Effective Model 4

3 Conclusion 5

A Saturated Antiferromagnetism 6

B Mean Field Theory 8
B.1 Approximate Gap Scaling 10

References 11


## 1 Introduction

The $t$-$J$ and Hubbard models have been studied extensively as toy models for high-temperature superconductivity in the cuprate superconductors [1-4]. However, the ground states of these models and materials are often frustrated by multiple competing or intertwining orders [5]. For example, in the $t$-$J$ model, the antiferromagnetic Heisenerg term $J$ results in antiferromagnetic order at half-filling; however, when the system is hole doped, then the hopping of holes will locally destroy the antiferromagnetic alignment. The competition between the $t$ and $J$ terms makes well-controlled analytical study of the $t$-$J$ model difficult.

Nevertheless, one might hope to find a corner of the Hubbard or $t$-$J$ model phase diagram that exhibits superconductivity while maintaining analytical control. Although this can be done for the weakly-interacting Hubbard model [6,7], in the limit of strong Hubbard $U$, which corresponds to small $J$ in the $t$-$J$ model, there is evidence that superconductivity does not occur [8-11]. To gain insight on the strongly-interacting regime, the large $J$ limit of the $t$-$J$ model has been studied; but this regime has been shown to be dominated by (unphysical$^1$) phase separation [9]. To make progress, many works have considered a large variety of modifications to the $t$-$J$ model in order to improve analytical tractability. Such modifications include explicit symmetry breaking [12,13], large spatial dimension [14], large $N$ [15], nonlocality [16,17], SYK-like nonlocality with large $N$ [18], and replacing the Heisenberg interaction $J$ with an Ising interaction $J_z$ [19-24].

In this work, our goal will be to study the simplest modification to the $t$-$J$ model (that does not enlarge the Hilbert space) such that a superconducting phases exists and can be well-understood with analytical control. Since the nearest-neighbor hopping frustrates the antiferromagnetic order in the $t$-$J$ model, we replace the nearest-neighbor hopping $t$ with a next-nearest-neighbor hopping $t'$ which does not compete with antiferromagnetism. To further simplify, we replace the Heisenberg interaction $J$ with an antiferromagnetic Ising interaction $J_z$.$^2$ We also add a nearest-neighbor repulsion $V$ to prevent unphysical charge separation. See Fig. 1.

The absence of a nearest-neighbor hopping may be an unrealistic aspect of our model. However, this omission is loosely motivated since nearest-neighbor hopping is strongly suppressed in $t$-$J$-like models near half-filling when $J$ is large [27-29]. Also note that next-nearest-neighbor hopping keeps the fermions on the same sublattice, which is a constraint that can also occur for polarons in an antiferromagnet [30-32]. Thus, our model could also be considered to be a toy model for polarons in an Ising antiferromagnet.

In Sec. 2, we show that in a certain large $J_z$ and $V$ limit, the ground state of the $t'$-$J_z$-$V$ model [Eq. (1)] is antiferromagnetic and the low-energy Hamiltonian can be exactly mapped to a Hamiltonian [Eq. (6)] where the only interaction is an attractive interaction. When the effective attraction is weak, the simplified model can be studied using BCS mean-field theory, which we carry out in detail.

---
$^1$ Here, phase separation means that a fraction of the system is completely unfilled while the rest is full of electrons. This state is unphysical because it has an infinite energy density when the $1/r$ Coulomb repulsion is not ignored.
$^2$ The $t$-$t'$-$t''$-$J_z$ model has been studied in Ref. [25,26].

![](./images/812727153731829760_3.jpg)

Figure 1: A depiction of the $t'$-$J_z$-$V$ model [Eq. (1)] that we study. This model includes a next-nearest-neighbor hopping $t'$ across the dashed gray links instead of a nearest-neighbor hopping $t$ across the solid black links. The model also includes an antiferromagnetic Ising interaction $J_z$ and nearest-neighbor repulsion $V$ across each solid black link. Unlike a nearest-neighbor hopping $t$, the next-nearest-neighbor hopping $t'$ does not frustrate the antiferromagnetic interaction. The red and blue arrows denote spin up and spin down fermions.

##  $t'$-$J_z$-$V$ Model

In this work, we study the $t'$-$J_z$-$V$ model on a square lattice (Fig. 1), which has the following Hamiltonian:
$$
H_{t'-J_z-V}=t' \sum_{\langle\langle i j\rangle\rangle} \sum_{s=\uparrow, \downarrow} \mathcal{P}\left(c_{i s}^{\dagger} c_{j s}+c_{j s}^{\dagger} c_{i s}\right) \mathcal{P}+J_{z} \sum_{\langle i j\rangle} S_{i}^{z} S_{j}^{z}+V \sum_{\langle i j\rangle} n_{i} n_{j},
\tag{1}
$$
with the single-occupancy constraint $n_i = n_{i\uparrow} + n_{i\downarrow} \leq 1$. The first term hops electrons diagonally between next-nearest-neighbor sites $\langle\langle ij\rangle\rangle$ while imposing the $n_i \leq 1$ constraint via the projection operator $\mathcal{P}$, which projects out $n_i=2$ states. The second term is a nearest-neighbor antiferromagnetic Ising interaction where $S_i^z = \frac{1}{2}(n_{i\uparrow}-n_{i\downarrow})$. The third term is a nearest-neighbor repulsive interaction. We study $H_{t'-J_z-V}$ on a square lattice; however, many of our results readily generalize to any bipartite lattice. The model has a $U(1)^4$ symmetry resulting from conserved charge and $z$-component of spin on each sublattice.

It is convenient to redefine the nearest-neighbor repulsion as $V=\frac{1}{4}J_z - V_0$ and rewrite the Hamiltonian as:
$$
H_{t'-J_z-V_0}=t' \sum_{\langle\langle i j\rangle\rangle, s} \mathcal{P}\left(c_{i s}^{\dagger} c_{j s}+c_{j s}^{\dagger} c_{i s}\right) \mathcal{P}+J_{z} \sum_{\langle i j\rangle}\left(S_{i}^{z} S_{j}^{z}+\frac{1}{4} n_{i} n_{j}\right)-V_{0} \sum_{\langle i j\rangle} n_{i} n_{j}.
\tag{2}
$$

We will focus on the following limit:
$$
V_0 \ll |t'| \ll J_z,
\tag{3}
$$
with electron filling $\langle n\rangle<1$.

It is useful to consider the energy levels of two nearest-neighbor sites in the $t'=0$ limit:
<table>
  <thead>
    <tr>
      <th>state</th>
      <th>$t'=0$ energy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\uparrow\uparrow, \downarrow\downarrow$</td>
      <td>$J_z/2 - v$</td>
    </tr>
    <tr>
      <td>$\uparrow 0, \downarrow 0, 0\uparrow, 0\downarrow$</td>
      <td>$0$</td>
    </tr>
    <tr>
      <td>$00$</td>
      <td>$0$</td>
    </tr>
    <tr>
      <td>$\uparrow\downarrow, \downarrow\uparrow$</td>
      <td>$-v$</td>
    </tr>
  </tbody>
</table>
(4)


In the above table, $\uparrow$ and $\downarrow$ refer to spin up and down electrons, while 0 refers to an empty site.

Thus, in the large $J_z$ limit, parallel spins are strongly suppressed. We argue that the ground state never has parallel spins in the $V_0 \ll |t'| \ll J_z$ limit for sufficiently large electron fillings. This occurs because all of the eigenstates have definite $S^z$ spin on each sublattice, and the lowest energy state is a fully-polarized antiferromagnet where one sublattice has only spin-up electrons and the other has only spin-down. This is the lowest-energy symmetry sector since it minimizes the energy from the $J_z$ term and also minimizes the energy of the $t'$ term by allowing for the most electron hopping. See Fig. 1 for an example of a state in this symmetry sector. In Appendix A, we provide a rigorous numerical argument that the ground state is fully antiferromagnetic when $V_0 \ll |t'| \ll J_z$ and for sufficiently large electron filling: $\langle n \rangle > n_c$ where we bound $n_c < 0.265$.

### 2.1 Effective Model
Since the ground states are fully-polarized Ising antiferromagnets, let us consider the antiferromagnetic ground state where the A and B sublattices have only spin-up and spin-down electrions, respectively. It is then convenient to define new electron operators:

$$
d_{i}=
\begin{cases}
c_{i\uparrow} & i \in \mathrm{A} \\
c_{i\downarrow} & j \in \mathrm{B}
\end{cases}. \tag{5}
$$

Within this subspace of only fully-polarized antiferromagnetic states, the $t'$-$J_z$-$V_0$ model [Eq. (2)] simplifies significantly:

$$
H_{\mathrm{AF}}=t^{\prime} \sum_{\langle\langle i j\rangle\rangle}\left(d_{i}^{\dagger} d_{j}+d_{j}^{\dagger} d_{i}\right)-V_{0} \sum_{\langle i j\rangle} n_{i} n_{j}. \tag{6}
$$

That is, the ground states of the $t'$-$J_z$-$V_0$ model can be described by the above Hamiltonian, $H_{\mathrm{AF}}$, which only involves fermions with a next-nearest-neighbor hopping $t'$ and attractive interaction $V_0$.

When $V_0 \ll t'$, we can apply BCS mean-field-theory to study $H_{\mathrm{AF}}$, which we work out in detail in Appendix B. The BCS order parameter is

$$
\Delta_{\delta}=V_{0}\left\langle d_{i} d_{i+\delta}\right\rangle, \text{ where } i \in \mathrm{A}, \tag{7}
$$

where $\delta=\hat{x}, \hat{y}$. The symmetry of the order parameter can be s-wave $(\Delta_x=\Delta_y)$ or d-wave $(\Delta_x=-\Delta_y)$, depending on the electron filling and sign of $t'$. Since the order parameter $\Delta_{\delta}$ is not on-site, its Fourier transformation [$\Delta_k$ in Eq. (18)] has nodal lines (where $\Delta_k=0$) in $k$-space for both s-wave and d-wave symmetry. However, if $\langle n \rangle \neq 1/2$, then the nodal lines never touch the fermi surface for either s-wave and d-wave symmetry, as shown in Fig. 2.

In the $V_0 \ll t'$ limit, the BCS order parameter satisfies the standard BCS gap equation

$$
\left|\Delta_{x}\right|=\left|\Delta_{y}\right|=2 \omega e^{-1 / V_{0} g_{0}}, \tag{8}
$$

where $\omega$ and $g_0$ are parameters, which we calculated numerically and show in Fig. 3 as a function of the filling fraction $\langle n \rangle$.

Although the density of states at the Fermi surface diverges at half filling, $g_0$ and the BCS gap $|\Delta_x|$ (in the weak interaction limit $V_0 \ll t'$) actually decrease as half filling is approached. This might conflict with one's intuition that a large density of states strengthens superconductivity. However, the diverging density of states occurs due to saddle points in the energy dispersion at momenta $k=(\pm\frac{\pi}{2},\pm\frac{\pi}{2})$ (black dots in Fig. 2), and these saddle points sit on the nodal lines of the BCS order parameter $\Delta_k$. Therefore, these states do not contribute to the BCS gap $\Delta_x$. In Appendix B.1, we mathematically confirm this argument.

![](./images/812727153731829760_4.jpg)

Figure 2: The nodal lines of the order parameter [black lines where $\Delta_k$=0 in Eq. (18)] and the fermi surface for various electron fillings (colored lines). The symmetry of the order parameter depends on the electron filling. When $t' > 0$, the symmetry is d-wave when $\langle n \rangle < 1/2$ and s-wave when $\langle n \rangle > 1/2$. The nodal lines never touch the fermi surface as long as $\langle n \rangle \neq 1/2$. The $t' < 0$ case follows from noting that the physics is symmetric under $t' \to -t'$ and $\langle n \rangle \to 1-\langle n \rangle$.

![](./images/812727153731829760_5.jpg)

Figure 3: The BCS gap equation parameters $\omega$ (left in green) and $g_0$ (right in blue) from Eq. (8), and the density of states at the Fermi surface (right in red). The parameters are rescaled by $t'$ to make them unitless. The density of states is defined by $\text{DoS} = \int_k \delta(\varepsilon_k)$, where we absorbed the chemical potential $\mu$, which depends on $\langle n \rangle$, into the electron dispersion $\varepsilon_k$ [Eq. (18)]. The density of states has a log divergence at $\langle n \rangle = 1/2$ where $\text{DoS} \sim 0.05 - 0.06\log|\langle n \rangle - \frac{1}{2}|$.

## 3 Conclusion

As part of a program to identify simple and analytically tractable toy models of superconductivity [33–35], in this work we identify three modifications to the $t$-$J$ model, resulting in the $t'$-$J_z$-$V$ model, that allow for an analytically controlled understanding of its antiferromagnetic d-wave superconducting ground state using BCS theory. Due to the second-nearest-neighbor hopping and antiferromagnetic ground state, the onsite Hubbard repulsion effectively disappears from the effective Hamiltonian $H_{\text{AF}}$ [Eq. (6)], and the antiferromagnetic

Heisenburg term leads to an effective nearest-neighbor attractive interaction $V_0$ in the antiferromagnetic ground state. Since the attractive interaction $V_0$ does not have to compete with an onsite Hubbard interaction (due to its absence in $H_{\text{AF}}$), the mechanism for Cooper pairing is very simple and results from a BCS description of the attractive interaction $V_0$. We then studied the small $V_0$ limit in detail using BCS theory. We also discussed why a diverging density of states at the Fermi level does not contribute to superconductivity in our model.

An interesting property of our model is the coexistence of antiferromagnetism and superconductivity. This coexistence has been studied and predicted in a number of works on (sometimes extended) Hubbard and $t$-$J$ models [36-40]. Our model provides an example of such a coexistence in an analytically tractable setting.

It would be interesting to combine the $t$-$J$ and $t'$-$J_z$-$V$ models into a single $t$-$t'$-$J_{xy}$-$J_z$-$V$ model to understand how universal the superconducting state we found is, to what extent it extends into the larger phase diagram, and if it boarders different superconducting states.

In Appendix A we showed that if $V_0 \ll |t'| \ll J_z$ and the electron filling is greater than $n_c = 0.265$, then the ground state is a fully polarized antiferromagnet. However, we did not consider the small filling case $n \ll 1$. It could be possible that sufficiently small fillings also lead to a fully polarized antiferromagnet.

Nevertheless, the $t'$-$J_z$-$V$ model that we studied has a number of limitations. Although it may be applicable to the study of polarons in an Ising antiferromagnet for which a nearest-neighbor hopping is not allowed, the absence of a nearest-neighbor hopping in our model is unnatural for an electron model. Furthermore, the tractable limit of our model was in a large antiferromagnetic interaction $J_z$ limit, which may not be experimentally accessible. Finally, the superconducting state that we found has large Cooper pairs (since it's described by BCS theory) and no gapless nodes (i.e. the lines where the order parameter is zero $\Delta_k = 0$ never touch the Fermi surface). This makes the superconducting state we found qualitatively different from more interesting superconducting states, such as the ones found in the cuprate superconductors [1-4] . In the future, it would be interesting to identify other simple and analytically tractable models with less of these shortcomings, or to include more exotic physics, such as emergent gauge fields [41,42], while retaining analytical control.

### Acknowledgements
We thank Patrick Lee and Assa Auerbach for helpful discussions.

Funding information KS acknowledges support from the Walter Burke Institute for Theoretical Physics at Caltech.

## A Saturated Antiferromagnetism
In order to reduce the $t'$-$J_z$-$V_0$ model [Eq. (2)] to the effective antiferromagnetic model [Eq. (6)], we need to show that the ground states of the $t'$-$J_z$-$V_0$ model have only spin up electrons on a one sublattice and only spin down electrons on the other sublattice. In this appendix, we argue that this is the case when

$$
V_0 \ll |t'| \ll J_z \text{ and } \langle n \rangle \gtrsim 0.265. \tag{9}
$$

To show this, we show that Eq. (9) implies that the lowest-energy fully-polarized antiferromagnetic state has a lower energy than any state state with a single flipped spin. By "flipped spin," we mean an electron with a spin in the opposite direction from the


antiferromagnetic order parameter. We expect that if a single spin flip costs energy, then flipping more spins will not result in a lower energy. If this expectation is true, then we have shown that the ground state is a fully polarized antiferromagnet when Eq. (9) is satisfied.

More precisely, assuming $V_0 \ll |t'| \ll J_z$, we numerically calculated a lower bound on the energy cost $E^{\rm flip}(N)$ to flip a single electron spin for a state with $N$ electrons on a square lattice with $N_{\rm sites}$ sites. Mathematically, $E^{\rm flip}(N)$ is defined as

$$
\begin{aligned}
E^{\mathrm{flip}}(N) &= E_{N-1,1}^{\mathrm{AF}} - E_{N,0}^{\mathrm{AF}}, \\
E_{N_1,N_2}^{\mathrm{AF}} &= E\left(N_{A\uparrow}^{\mathrm{tot}} + N_{B\downarrow}^{\mathrm{tot}} = N_1 \, ; \, N_{A\downarrow}^{\mathrm{tot}} + N_{B\uparrow}^{\mathrm{tot}} = N_2\right),
\end{aligned}
\tag{10}
$$

where $E_{N_1,N_2}^{\rm AF}$ is the lowest energy state with $N_1$ electrons that are either spin-up on the A sublattice or spin-down on the B sublattice and $N_2$ electrons that are either spin-down on the A sublattice or spin-up on the B sublattice.

We want to show that $E^{\rm flip}(N)$ is positive for sufficiently large $\langle n \rangle = N/N_{\rm sites}$ (as $N \to \infty$). Since we're assuming $V_0 \ll |t'| \ll J_z$, and the $t'$ and $J_z$ terms are sufficient to eliminate any extensive degeneracy, it's sufficient to ignore the attractive $V_0$ term and only consider states in the ground state of the $J_z$ term in Eq. (2). That is, we can simplify the calculation by considering the following limit:

$$
V_0 = 0, \qquad J_z = \infty.
\tag{11}
$$

$E_{N,0}^{\rm AF}$ is the fully-polarized antiferromagnet ground state energy. $E_{N,0}^{\rm AF}$ can be efficiently calculated since it only involves free fermions since the $J_z$ term does not contribute to fully-polarized states and we are ignoring the $V_0$ term.

$E_{N-1,1}^{\rm AF}$ is more complicated to calculate, but we can place a lower bound on it. Let $|\Psi_{N-1,1}^{\rm AF}\rangle$ be an eigenstate with energy $E_{N-1,1}^{\rm AF}$. Let us decompose $|\Psi_{N-1,1}^{\rm AF}\rangle$ as a sum of states with a definite position for the flipped spin:

$$
|\Psi_{N-1,1}^{\rm AF}\rangle = \sqrt{\frac{2}{N_{\rm sites}}} \sum_{i \in \text{A}} \alpha_i c_{i\downarrow}^\dagger |\psi_{N-1,0}^{(i)}\rangle.
\tag{12}
$$

$|\psi_{N-1,0}^{(i)}\rangle$ is a state with $N$ electrons that are either spin-up on the A sublattice or spin-down on the B sublattice, and where $|\psi_{N-1,0}^{(i)}\rangle$ depends on the lattice site $i$ of the flipped spin. Translation symmetry implies that $\alpha_i$ is only a phase (i.e. $|\alpha_i| = 1$) and the states $|\psi_{N-1,0}^{(i)}\rangle$ are related by translation (i.e. $T_\delta |\psi_{N-1,0}^{(i)}\rangle = |\psi_{N-1,0}^{(i+\delta)}\rangle$ where $T_\delta$ is a translation operator).

We can now derive the following bound:

$$
\begin{aligned}
E_{N-1,1}^{\mathrm{AF}}&=\left\langle\Psi_{N-1,1}^{\mathrm{AF}}\left|H_{t'-J_{z}-V_{0}}\right| \Psi_{N-1,1}^{\mathrm{AF}}\right\rangle \\
&=\frac{2}{N_{\text {sites }}}\left[\sum_{\substack{i, j \in \mathrm{A} \\
i \neq j}} \alpha_{i}^{*} \alpha_{j}\left\langle\psi_{N-1,0}^{(i)}\left|c_{i \downarrow} H_{t^{\prime}} c_{j \downarrow}^{\dagger}\right| \psi_{N-1,0}^{(j)}\right\rangle+\sum_{i \in \mathrm{A}}\left\langle\psi_{N-1,0}^{(i)}\left|H_{t^{\prime}}\right| \psi_{N-1,0}^{(i)}\right\rangle\right] \\
&=\sum_{j=i \pm \hat{x} \pm \hat{y}} t^{\prime} \alpha_{i}^{*} \alpha_{j}\left\langle\psi_{N-1,0}^{(i)} \mid \psi_{N-1,0}^{(j)}\right\rangle+\left\langle\psi_{N-1,0}^{(i)}\left|H_{t^{\prime}}\right| \psi_{N-1,0}^{(i)}\right\rangle, \text { where } i \in \mathrm{A} \\
& \geq-4\left|t^{\prime}\right|+\widetilde{E}_{N-1,0}^{\mathrm{AF}},
\end{aligned}
\tag{13}
$$
$$\tag{14}$$

$H_{t'}$ is the $t'$ term in $H_{t'-J_z-V_0}$ [Eq. (2)]. Only the $t'$ term contributes due to the $V_0 = 0$ limit [Eq. (11)]. In Eq. (13), $i$ can be any site in the A sublattice. The first term in Eq. (14) results from bounding $t' \alpha_i^* \alpha_j \langle \psi_{N-1,0}^{(i)} | \psi_{N-1,0}^{(j)} \rangle \geq -|t'|$. $\widetilde{E}_{N-1,0}^{\rm AF}$ is the energy defined in Fig. 4. $\widetilde{E}_{N-1,0}^{\rm AF}$ bounds the second term in Eq. (13) since it is the ground state energy of $H_{t'}$ subject to the

![](./images/812727153731829760_6.jpg)

Figure 4: $\widetilde{E}_{N-1,0}^{\mathrm{AF}}$ is the ground state energy of $H_{t'}$ [i.e. the $t'$ term in $H_{t'-J_z-V_0}$ from Eq. (2)] with $N-1$ electrons that are either spin-up on the A sublattice (red sites) or spin-down on the B sublattice (blue sites) and subject to the constraint that there are no fermions on the five sites marked with crosses.

same constraint that is enforced upon $|\psi_{N-1,0}^{(i)}\rangle$ [due to $J_z = \infty$ in Eq. (11)]. $\widetilde{E}_{N-1,0}^{\mathrm{AF}}$ can be efficiently calculated since the projection operators $\mathcal{P}$ in $H_{t'}$ act as the identity operator for the electron filling under consideration; thus we only need to calculate the ground state energy of a free fermion Hamiltonian.

In Fig. 5, we plot
$$
E^{\mathrm{flip}}(N) \geq-4 t^{\prime}+\widetilde{E}_{N-1,0}^{\mathrm{AF}}-E_{N, 0}^{\mathrm{AF}},\qquad(15)
$$
where the bound follows from Eqs. (10) and (14). Fig. 5 is therefore evidence that the ground state is a fully-polarized antiferromagnet.

## B Mean Field Theory

In this appendix, we study $H_{\mathrm{AF}}$ [Eq. (6)] using BCS mean-field theory. We primarily do this to check the symmetry of the BCS order parameter (see e.g. Fig. 2). We also numerically calculate the scaling of the order parameter for weak interactions and display the result in Fig. 3.

We begin with the following BCS mean-field expansion
$$
n_{i} n_{j} \approx\left\langle d_{i} d_{j}\right\rangle d_{j}^{\dagger} d_{i}^{\dagger}+\left\langle d_{i} d_{j}\right\rangle^{*} d_{i} d_{j}-\left|\left\langle d_{i} d_{j}\right\rangle\right|^{2},\qquad(16)
$$
where we have dropped $O(\left.d_{i} d_{j}-\left\langle d_{i} d_{j}\right\rangle\right)^{2}$ terms.

After applying the above mean-field expansion and a Fourier transformation $(d_{k}=N^{-1/2}\sum_{j}e^{-\mathrm{i}k\cdot j}d_{j})$, $H_{\mathrm{AF}}$ becomes
$$
H_{\mathrm{BCS}}=\sum_{k}^{0 \leq k_{x}<\pi}\left(\begin{array}{c}
d_{k}^{\dagger} \\
d_{\pi-k}^{\dagger}
\end{array}\right)\left(\begin{array}{cc}
+\varepsilon_{k} & -\Delta_{k} \\
-\Delta_{k}^{*} & -\varepsilon_{k}
\end{array}\right)\left(\begin{array}{c}
d_{k} \\
d_{\pi-k}^{\dagger}
\end{array}\right)+\frac{N}{V}\left(\left|\Delta_{x}\right|^{2}+\left|\Delta_{y}\right|^{2}\right),\qquad(17)
$$
where we have dropped a constant that does not depend on $\Delta_{x}$ or $\Delta_{y}$. The electron dispersion $\varepsilon_{k}$ and gap function $\Delta_{k}$ are:
$$
\begin{aligned}
& \varepsilon_{k}=4 t^{\prime} \cos k_{x} \cos k_{y}-\mu, \\
& \Delta_{k}=2 \Delta_{x} \cos k_{x}+2 \Delta_{y} \cos k_{y},
\end{aligned}\qquad(18)
$$

![](./images/812727153731829760_7.jpg)

Figure 5: A lower bound on the energy $E^{\rm flip}$ [Eq. (10)] required to flip an electron spin on one of the sublattices when $V_0 \ll |t'| \ll J_z$. We used a square lattice with $N_{\rm sites}=2 \times 200 \times 200$, where the A and B sublattices are each $200 \times 200$ square lattices with periodic boundary conditions which are rotated $45^\circ$ with respect to Fig. 1. We expect the reduced model [Eq. (6)] to be valid when $E^{\rm flip} > 0$. The figure shows that there is a critical filling $n_c$ such that $E^{\rm flip} > 0$ for all $\langle n \rangle > n_c$. (b) Zooming in suggests an upper bound on the critical filling: $n_c < 0.265$. We also show the $N_{\rm sites}=2 \times 100 \times 100$ lattice result as evidence that larger system sizes would only improve our bound.

where $\mu$ is the chemical potential. The mean-field order parameter $\Delta_\delta$ is defined by
$$
\Delta_{\delta}=V_{0}\langle d_{i}d_{i+\delta}\rangle,\ \text{where }i\in\mathrm{A}. \tag{19}
$$
$\sum_{k}^{0 \leq k_x < \pi}$ sums over all momenta $k$ in the half-Brillouin zone with $0 \leq k_x < \pi$. $\pi - k$ is defined by $\pi - k = (\pi - k_x, \pi - k_y)$ where $k=(k_x,k_y)$.

$H_{\rm BCS}$ can be diagonalized by a Bogoliubov transformation:
$$
H_{\text{Bogoliubov}}=\sum_{k}^{0\leq k_{x}<\pi}\begin{pmatrix}
\alpha_{k}^{\dagger}\\
\beta_{k}^{\dagger}
\end{pmatrix}\begin{pmatrix}
+\lambda_{k} & 0\\
0 & -\lambda_{k}
\end{pmatrix}\begin{pmatrix}
\alpha_{k}\\
\beta_{k}
\end{pmatrix}+\frac{N}{V_{0}}\left(|\Delta_{x}|^{2}+|\Delta_{y}|^{2}\right), \tag{20}
$$

$$
\lambda_{k}=\sqrt{\varepsilon_{k}^{2}+|\Delta_{k}^{2}|}, \tag{21}
$$
where $\pm\lambda_{k}$ are the Bogoliubov quasi-particle energies. The Bogoliubov quasi-particle operators $\alpha_{k}$ and $\beta_{k}$ with $0 \leq k_x < \pi$ are defined in terms of the electron operators $d_k$ by the following Bogoliubov transformation:
$$
\begin{pmatrix}
d_{k}\\
d_{\pi-k}^{\dagger}
\end{pmatrix}=\begin{pmatrix}
+\cos\theta_{k} & +\sin\theta_{k}e^{+\mathrm{i}\phi_{k}}\\
-\sin\theta_{k}e^{-\mathrm{i}\phi_{k}} & +\cos\theta_{k}
\end{pmatrix}\begin{pmatrix}
\alpha_{k}\\
\beta_{k}
\end{pmatrix}, \tag{22}
$$
where the angle $0 < \theta_{k} < \pi/4$ is defined by $\tan(2\theta_{k})=|\Delta_{k}|/\varepsilon_{k}$ and $\phi$ is the phase of $\Delta_{k}=|\Delta_{k}|e^{\mathrm{i}\phi_{k}}$.

The order parameters $\Delta_x$ and $\Delta_y$ can be obtained by variationally minimizing the ground state energy density
$$
\frac{E}{N}=-\frac{1}{2}\int_{k}\lambda_{k}+V_{0}^{-1}\left(|\Delta_{x}|^{2}+|\Delta_{y}|^{2}\right), \tag{23}
$$
or by solving the self-consistency condition:
$$
\begin{aligned}
\Delta_{\delta} & =V_{0}\langle d_{i}d_{i+\delta}\rangle,\ \text{where }i\in\mathrm{A}\\
& =\frac{V_{0}}{2N}\int_{k}\cos k_{\delta}\frac{\Delta_{k}}{\lambda_{k}},
\end{aligned} \tag{24}
$$


where $\int_{k} = \int \frac{\mathrm{d}k_x}{2\pi} \frac{\mathrm{d}k_y}{2\pi}$.

We will assume that $\Delta_x$ and $\Delta_y$ are related by a phase $s$ ($|s| = 1$):

$$
\Delta_y = s\Delta_x . \tag{25}
$$

Solving the self-consistency Eq. (24) for $V_0^{-1}$ results in

$$
V_0^{-1} = \frac{1}{2} \int_{k} \left| \cos k_x + s \cos k_y \right|^2 / \lambda_k . \tag{26}
$$

From the above Eq. (26), we can calculate the interaction strength $V_0$ as a function of the order parameter $\Delta_y = s\Delta_x$ and chemical potential $\mu$. We use Eq. (23) to find which order parameter symmetry ($s = 1$, i, or $-1$) gives the lowest ground state energy; the result in summarized in Fig. 2.

We numerically calculate the scaling coefficients of the order parameter in the weak interaction limit $V_0 \ll |t'|$ by calculating $V_0$ from Eq. (26) for a few very small values of the order parameter: $|\Delta_x / t'| \sim 10^{-5}$. We then fit the resulting $(V_0, |\Delta_x|)$ data to the standard BCS gap equation

$$
|\Delta_x| = |\Delta_y| = 2\omega e^{-1/V_0 g_0} \tag{27}
$$

using $\omega$ and $g_0$ as free parameters. The result is shown in Fig. 3 as a function of the filling fraction $\langle n \rangle$.

### B.1 Approximate Gap Scaling

In the usual s-wave BCS theory, $g_0$ in Eq. (8) is approximately equal to the density of states at the Fermi level [43]. However, Fig. 3 shows that this is clearly not the case in our model. This occurs because in Eq. (26), the integral can not be reformulated in terms of the density of states $g(\varepsilon)$ as just a function of the energy $\varepsilon$. Rather, one requires a density of states $g(\varepsilon, \chi)$ that is also a function of the shape of the gap function $\chi = |\Delta_k / \Delta_x|$, which can be seen by rewriting Eq. (26) as

$$
V_0^{-1} = \frac{1}{8} \int \mathrm{d}\varepsilon \int \mathrm{d}\chi \, g(\varepsilon, \chi) \frac{\chi^2}{\sqrt{\varepsilon^2 + |\Delta_x^2| \chi^2}}, \tag{28}
$$

$$
g(\varepsilon, \chi) = \int_{k} \delta(\varepsilon_k - \varepsilon) \delta(|\Delta_k / \Delta_x| - \chi) . \tag{29}
$$

In Fig. 6, we plot $g(\varepsilon, \chi)$ for our model.

Note that the integral in Eq. (28) is dominated by the region near the Fermi level where $\varepsilon = 0$. Thus, similar to ordinary BCS theory, we can approximate the $\varepsilon$ dependence as a box distribution:

$$
g(\varepsilon, \chi) \approx
\begin{cases}
g(\chi) & |\varepsilon| < W \\
0 & \text{otherwise}
\end{cases} . \tag{30}
$$

We can now perform the $\varepsilon$ integral in Eq. (28) to obtain:

$$
V_0^{-1} = \int \mathrm{d}\chi \, \frac{1}{4} g(\chi) \chi^2 \ln \frac{2W}{|\Delta_x| \chi} . \tag{31}
$$

Solving the above equation for $\Delta_x$ results in the BCS gap equation [Eq. (27)] with the following

![](./images/812727153731829760_8.jpg)

Figure 6: The density of states $g(\varepsilon,\chi)$ [Eq. (29)] as a function of the single-particle energy $\varepsilon$ and gap function $\chi$ for our model [Eq. (18)] when $\Delta_x=-\Delta_y$ (which occurs when $\mu/t'<0$). The $\Delta_x=+\Delta_y$ case is obtained by reflecting $\varepsilon+\mu\rightarrow-\varepsilon-\mu$. The density of states $g(\varepsilon)$ as a function of only the single-particle energy $\varepsilon$ is shown in Fig. 3. The grayscale legend should not be taken seriously at the bottom-right corner where $g(\varepsilon,\chi)$ diverges.

BCS parameters:

$$
\begin{aligned}
g_{0} & =\int \mathrm{d} \chi \frac{1}{4} g(\chi) \chi^{2}, \\
\omega & =W \exp \left(-\frac{1}{g_{0}} \int \mathrm{d} \chi \frac{1}{4} g(\chi) \chi^{2} \ln \chi\right) \\
& =W \exp \left(-\langle\ln \chi\rangle_{P(\chi)=\frac{1}{4 g_{0}} g(\chi) \chi^{2}}\right).
\end{aligned}\tag{32}
$$

$g_0$ does not depend on $W$, which shows that $g_0$ only depends on the states near the Fermi level $\varepsilon=0$. We also see that states where the gap function $\chi=|\Delta_k/\Delta_x|$ is larger contribute the most to $g_0$. In particular, states along the nodal lines of $\Delta_k$ (i.e. where $\chi=\Delta_k=0$) do not contribute to $g_0$. This mathematically explains our intuition for $g_0$ that we explained in the last paragraph of Sec. 2.1.

$\omega$ does depend on $W$, and therefore $\omega$ also depends on the states away from the Fermi level $\varepsilon=0$. $\omega$ is most intuitively expressed in terms of an expectation value of $\langle\ln\chi\rangle$ where $\chi$ is thought of as a random variable with the probability distribution $P(\chi)=\frac{1}{4g_0}g(\chi)\chi^2$.

## References
[1] B. Keimer, S. A. Kivelson, M. R. Norman, S. Uchida and J. Zaanen, *From quantum matter to high-temperature superconductivity in copper oxides*, **Nature 518**, 179 (2015), doi:10.1038/nature14165.

[2] E. W. Carlson, V. J. Emery, S. A. Kivelson and D. Orgad, *Concepts in high temperature superconductivity* (2002), arXiv:cond-mat/0206217.

[3] P. A. Lee, N. Nagaosa and X.-G. Wen, *Doping a Mott insulator: Physics of high temperature superconductivity* (2004), arXiv:cond-mat/0410445.

[4] D. J. Scalapino, A common thread: The pairing interaction for unconventional superconductors, Rev. Mod. Phys. 84, 1383 (2012), doi:10.1103/RevModPhys.84.1383.

[5] E. Fradkin, S. A. Kivelson and J. M. Tranquada, Colloquium: Theory of intertwined orders in high temperature superconductors, Rev. Mod. Phys. 87, 457 (2015), doi:10.1103/RevModPhys.87.457.

[6] S. Raghu, S. A. Kivelson and D. J. Scalapino, Superconductivity in the repulsive Hubbard model: An asymptotically exact weak-coupling solution, Phys. Rev. B 81, 224505 (2010), doi:10.1103/PhysRevB.81.224505.

[7] S. Maiti and A. V. Chubukov, Superconductivity from repulsive interaction, Am. Inst. Phys. Conf. Ser. 1550, 3 (2013), doi:10.1063/1.4818400.

[8] L. Liu, H. Yao, E. Berg, S. R. White and S. A. Kivelson, Phases of the infi- nite U Hubbard model on square lattices, Phys. Rev. Lett. 108, 126406 (2012), doi:10.1103/PhysRevLett.108.126406.

[9] V. J. Emery, S. A. Kivelson and H. Q. Lin, Phase separation in the t-J model, Phys. Rev. Lett. 64, 475 (1990), doi:10.1103/PhysRevLett.64.475.

[10] M. M. Maška, M. Mierzejewski, E. A. Kochetov, L. Vidmar, J. Bonča and O. P. Sushkov, Effective approach to the Nagaoka regime of the two-dimensional t-J model, Phys. Rev. B 85, 245113 (2012), doi:10.1103/PhysRevB.85.245113.

[11] Y. Nagaoka, Ferromagnetism in a narrow, almost half-filled s band, Phys. Rev. 147, 392 (1966), doi:10.1103/PhysRev.147.392.

[12] Z. Chen, X. Li and T. Kai Ng, Exactly solvable BCS-Hubbard model in arbitrary dimensions, Phys. Rev. Lett. 120, 046401 (2018), doi:10.1103/PhysRevLett.120.046401.

[13] J.-J. Miao, D.-H. Xu, L. Zhang and F.-C. Zhang, Exact solution to the Haldane-BCS-Hubbard model along the symmetric lines: Interaction-induced topological phase transition, Phys. Rev. B 99, 245154 (2019), doi:10.1103/PhysRevB.99.245154.

[14] E. W. Carlson, S. A. Kivelson, Z. Nussinov and V. J. Emery, Doped antiferromagnets in high dimension, Phys. Rev. B 57, 14704 (1998), doi:10.1103/PhysRevB.57.14704.

[15] I. Affleck and J. Brad Marston, Large-n limit of the Heisenberg-Hubbard model: Implications for high-$T_c$ superconductors, Phys. Rev. B 37, 3774 (1988), doi:10.1103/PhysRevB.37.3774.

[16] H. R. Krishnamurthy and B. Sriram Shastry, Exact solution of a repulsive Fermi model with enhanced superconducting correlations, Phys. Rev. Lett. 84, 4918 (2000), doi:10.1103/PhysRevLett.84.4918.

[17] L. Lepori and M. Roncaglia, Solvable two-dimensional superconductors with l-wave pairing, Phys. Rev. B 98, 144504 (2018), doi:10.1103/PhysRevB.98.144504.

[18] W. Fu, Y. Gu, S. Sachdev and G. Tarnopolsky, $Z_2$ fractionalized phases of a solvable disordered t-J model, Phys. Rev. B 98, 075150 (2018), doi:10.1103/PhysRevB.98.075150.

[19] Z. Nussinov and A. Rosengren, Exact ground states of extended $t-J_z$ models on a square lattice (2005), arXiv:cond-mat/0504650.

[20] P. Prelovšek and I. Sega, $t$-$J_z$ model on the Cayley tree and the square lattice, Phys. Rev. B 49, 15241 (1994), doi:10.1103/PhysRevB.49.15241.


[21] C. D. Batista and G. Ortiz, *Quantum phase diagram of the t-$J_z$ chain model*, Phys. Rev. Lett. **85**, 4755 (2000), doi:10.1103/PhysRevLett.85.4755.

[22] Yu. A. Dimashko, *The t-$J_z$ model: two holes pairing by means of one string*, Phys. C: Supercond. **206**, 393 (1993), doi:10.1016/0921-4534(93)90539-3.

[23] M. M. Maśka, M. Mierzejewski and E. Kochetov, *The Ising version of the t-J model*, Philos. Mag. **95**, 583 (2015), doi:10.1080/14786435.2014.977371.

[24] A. L. Chernyshev and P. W. Leung, *Holes in the t-$J_z$ model: A diagrammatic study*, Phys. Rev. B **60**, 1592 (1999), doi:10.1103/PhysRevB.60.1592.

[25] J. Bała, *Structure of spin polarons in the t-t'-t''-$J^z$ model*, Eur. Phys. J. B **16**, 495 (2000), doi:10.1007/s100510070208.

[26] R. M. Fye, G. B. Martins and E. Dagotto, *Hole-pair symmetry and excitations in the strong-coupling extended t-$J_z$ model: competition between d-wave and p-wave symmetry*, Phys. Rev. B **69**, 224507 (2004), doi:10.1103/PhysRevB.69.224507.

[27] S. A. Trugman, *Interaction of holes in a Hubbard antiferromagnet and high-temperature superconductivity*, Phys. Rev. B **37**, 1597 (1988), doi:10.1103/PhysRevB.37.1597.

[28] C. L. Kane, P. A. Lee and N. Read, *Motion of a single hole in a quantum antiferromagnet*, Phys. Rev. B **39**, 6880 (1989), doi:10.1103/PhysRevB.39.6880.

[29] J. Sous and M. Pretko, *Fractons from polarons and hole-doped antiferromagnets: Microscopic realizations* (2019), arXiv:1904.08424.

[30] A. Auerbach and B. E. Larson, *Small-polaron theory of doped antiferromagnets*, Phys. Rev. Lett. **66**, 2262 (1991), doi:10.1103/PhysRevLett.66.2262.

[31] E. Altman and A. Auerbach, *Plaquette boson-fermion model of cuprates*, Phys. Rev. B **65**, 104508 (2002), doi:10.1103/PhysRevB.65.104508.

[32] A. Auerbach, *Interacting electrons and quantum magnetism*, Graduate Texts in Contemporary Physics. Springer-Verlag, (1994), ISBN 978-0-387-94286-5.

[33] K. Slagle and Y. B. Kim, *A simple mechanism for unconventional superconductivity in a repulsive fermion model*, SciPost Phys. **6**, 016 (2019), doi:10.21468/SciPostPhys.6.2.016.

[34] L. Isaev, G. Ortiz and C. D. Batista, *Superconductivity in strongly repulsive fermions: The role of kinetic-energy frustration*, Phys. Rev. Lett. **105**, 187002 (2010), doi:10.1103/PhysRevLett.105.187002.

[35] H. Yao, W.-F. Tsai and S. A. Kivelson, *Myriad phases of the checkerboard Hubbard model*, Phys. Rev. B **76**, 161104 (2007), doi:10.1103/PhysRevB.76.161104.

[36] M. Inui, S. Doniach, P. Hirschfeld and A. Ruckenstein, *Coexistence of antiferromagnetism and superconductivity in a mean-field theory of high-$T_c$ superconductors*, Phys. Rev. B **37**, 2320 (1988), doi:10.1103/PhysRevB.37.2320.

[37] A. Foley, S. Verret, A.-M. S. Tremblay and D. Sénéchal, *Coexistence of superconductivity and antiferromagnetism in the Hubbard model for cuprates*, Phys. Rev. B **99**, 184510 (2019), doi:10.1103/PhysRevB.99.184510.

[38] M. Capone and G. Kotliar, *Competition between d-wave superconductivity and antiferromagnetism in the two-dimensional Hubbard model*, Phys. Rev. B **74**, 054513 (2006), doi:10.1103/PhysRevB.74.054513.

[39] A. Himeda and M. Ogata, *Coexistence of $d_{x^2-y^2}$ superconductivity and antiferromagnetism in the two-dimensional t-J model and numerical estimation of Gutzwiller factors*, Phys. Rev. B **60**, R9935 (1999), doi:10.1103/PhysRevB.60.R9935.

[40] K. Park, *Quantum antiferromagnetism and high $T_c$ superconductivity: A close connection between the t-J model and the projected BCS Hamiltonian*, Phys. Rev. B **72**, 245116 (2005), doi:10.1103/PhysRevB.72.245116.

[41] S. Sachdev, *Emergent gauge fields and the high-temperature superconductors*, Phil. Trans. R. Soc. A **374**, 20150248 (2016), doi:10.1098/rsta.2015.0248.

[42] P. A. Lee, N. Nagaosa and X.-G. Wen, *Doping a Mott insulator: Physics of high-temperature superconductivity*, Rev. Mod. Phys. **78**, 17 (2006), doi:10.1103/RevModPhys.78.17.

[43] J. Bardeen, L. N. Cooper and J. R. Schrieffer, *Theory of superconductivity*, Phys. Rev. **108**, 1175 (1957), doi:10.1103/PhysRev.108.1175.