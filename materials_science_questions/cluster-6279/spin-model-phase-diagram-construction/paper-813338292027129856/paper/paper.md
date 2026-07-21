# Ground states of a mixture of two species of spin-1 Bose gases with interspecies spin exchange in a magnetic field

Yu Shi* and Li Ge

Department of Physics, Fudan University, Shanghai 200433, China

We consider a mixture of two species of spin-1 atoms with both interspecies and intraspecies spin exchanges in a weak magnetic field. Under the usual single mode approximation, it can be reduced to a model of coupled giant spins. We find most of its ground states. This is a complicated problem of energy minimization, with three quantum variables under constraints, i.e. the total spin of each species and the total spin of the whole mixture, as well as four parameters, including intraspecies and interspecies spin coupling strengths and the magnetic field. The quantum phase diagram is very rich. Compared with the case without a magnetic field, the ground states are modified by a magnetic field, which also modifies the ground state boundaries or introduces new crossover regimes on the phase diagram. Without interspecies spin coupling, the quantum phase transitions existing in absence of a magnetic field disappear when a magnetic field is applied, which leads to crossover regimes in the phase diagram. Under ferromagnetic interspecies spin coupling, the ground states remain disentangled no matter whether there is a magnetic field. For antiferromagnetic interspecies spin coupling, a magnetic field entangles the ground states in some parameter regimes. When the intraspecies spin couplings are both ferromagnetic, the quantum phase transition between antifer- romagnetic and zero interspecies spin couplings survives the magnetic field. When the intraspecies spin couplings are both antiferromagnetic, a magnetic field induces new quantum phase transitions between antiferromagnetic and zero interspecies spin couplings.

PACS numbers: 03.75.Mn, 03.75.Gg

## I. INTRODUCTION

Spinor Bose gases have been extensively studied since a decade ago when it was discovered that they display remarkable spin correlations because of spin-exchange scattering between atoms [1–7, 9–11]. However, there have not been many investigations on many-body phenomena in mixtures of different spinor Bose gases with interspecies spin exchanges. In the first instance, spin-exchange scattering between distinguishable atoms have been less studied, perhaps because of incomplete information on inter-atomic potential. To motivate more interests in this direction, we note that interspecies spin-exchange interaction can be significant. The previous experiments on multi-component Bose gases often had atom loss due to spin exchanges [11, 12]. There were early calculations indicating that the cross-sections of spin-exchange scattering between different atoms may not be smaller than those between identical atoms [13]. Recently, there were more calculations as mentioned in the following, though motivated by studying a mixture of two species of atoms in frozen spin states, for which spin-exchange scattering is regarded as inelastic. A calculation for $^{23}$Na-$^{85}$Rb scattering indicated a quite large difference between scattering lengths of electronic singlet and triplet states [14]. This paper also reported a small value of such a singlet-triplet difference of scattering lengths for $^{23}$Na-$^{87}$Rb scattering, but contrary result was later reported [15]. Another calculation found significant singlet- triplet differences of scattering lengths for X-$^{133}$Cs scattering, where X=$^{6}$Li, $^{7}$Li, $^{39}$K, $^{41}$K, $^{85}$Rb and $^{87}$Rb [16]. Experimentally, significant differences between singlet and triplet scattering lengths have been observed in $^{41}$K-$^{87}$Rb, $^{40}$K-$^{87}$Rb and $^{6}$Li($^{7}$Li)-$^{23}$Na mixtures [17–20], implying significant interspecies spin exchanges. Spin-changing scattering was also observed in $^{7}$Li-$^{133}$Cs [21]. Moreover, heteronuclear Feshbach resonances can be implemented [22], which can enhance both elastic and inelastic collision rates [23–25]. To our understanding, some recent experimental set-ups on multi-species Bose gases have come to close to what we need to realize a mixture of two species of spinor gases with interspecies spin exchange [26].

Further researches on mixtures of spinor gases with interspecies spin exchanges can be motivated by novel many- body quantum phenomena in such mixtures, as demonstrated first in a model of a mixture of pseudospin-$\frac{1}{2}$ atomic gases, where interspecies spin exchange leads to richer ground states and phenomena, especially Bose-Einstein con- densation (BEC) with interspecies quantum entanglement, which was dubbed entangled Bose-Einstein condensation (EBEC) [27–30]. As usual, two subsystems constituting the total system are entangled if the state of the total system

*Electronic address: yushi@fudan.edu.cn

is not a direct product of those of the subsystems. Otherwise, they are called disentangled.

This line of researches has been extended to a mixture of two species of spin-1 atomic gases [31, 32], in which the interspecies spin coupling is simply of Heisenberg form [33]. In the usual approach of single orbit-mode approximation, most of the exact ground states in absence of a magnetic field have been found [31, 32]. However, in presence of a magnetic field, only two special parameter regimes have been considered [31]. Given that the magnetic field effect is an important issue, in the present paper, we systematically study the ground states in presence of a weak magnetic field, and find out how a magnetic field affects the ground states and phase diagrams of a spinor mixture with interspecies spin exchanges.

The rest of the paper is organized as the following. To make the paper self-contained, we set the stage in Sec. II. Then we discuss in Sec. III the ground states of a mixture of two spin-1 Bose gases in a magnetic field, but without interspecies spin coupling. In Sec. IV, we find the ground states of a mixture with ferromagnetic interspecies spin coupling in a magnetic field, based on the calculations detailed in the Appendix A. For antiferromagnetic interspecies spin coupling $c^{ab}>0$, we divide the range of $c^{ab}$ to three intervals. In Sec. V, based on the calculations detailed in the Appendices B, C, D and E, we find the ground states of a mixture with $0<c^{ab}\leq2\gamma B$, where $\gamma$ is the gyromagnetic ratio, $B$ is the magnitude of the field. In Sec. VI, we make some brief discussions on the regime $c^{ab}>2\gamma B$. In Sec. VII, quantum phase transitions are described. The issue of characterizing interspecies entanglement is discussed in Sec. VIII. A summary is made in Sec. IX.

## II. THE SYSTEM

Consider a mixture of two species $a$ and $b$ of spin-1 atoms, whose numbers $N_a$ and $N_b$ are conserved respectively. The single-atom Hamiltonian of species $\alpha$ ($\alpha=a,b$) is

$$
h_{\alpha}=-\frac{\hbar^{2}}{2m_{\alpha}}\nabla^{2}+U_{\alpha}(\mathbf{r})-\gamma_{\alpha}\mathbf{B}\cdot\mathbf{F}_{\alpha},
\tag{1}
$$

where $\mathbf{B}$ is a uniform magnetic field, $m_{\alpha}$, $\gamma_{\alpha}>0$, $U_{\alpha}$ and $\mathbf{F}_{\alpha}$ are the mass, the gyromagnetic ratio, the external potential and the single-spin operator, respectively, for an atom of species $\alpha$. With $\psi_{\alpha\mu}$ representing the field operator corresponding to spin $\mu$ component of species $\alpha$ ($\mu=-1,0,1$), the many-body Hamiltonian is

$$
\mathcal{H}=\sum_{\alpha=a,b}\mathcal{H}_{\alpha}+\mathcal{H}_{ab},
\tag{2}
$$

where

$$
\mathcal{H}_{\alpha}=\int d\mathbf{r}\psi_{\alpha\mu}^{\dagger}h_{\alpha}(\mathbf{r})_{\mu\nu}\psi_{\alpha\nu}+\frac{1}{2}\int d\mathbf{r}\psi_{\alpha\mu}^{\dagger}\psi_{\alpha\rho}^{\dagger}(\overline{c}_{0}^{\alpha}\delta_{\mu\nu}\delta_{\rho\sigma}+\overline{c}_{2}^{\alpha}\mathbf{F}_{\alpha\mu\nu}\cdot\mathbf{F}_{\alpha\rho\sigma})\psi_{\alpha\sigma}\psi_{\alpha\nu}
\tag{3}
$$

is the usual Hamiltonian of spin-1 atoms [1],

$$
\mathcal{H}_{ab}=\int d\mathbf{r}\psi_{a\mu}^{\dagger}\psi_{b\rho}^{\dagger}(\overline{c}_{0}^{ab}\delta_{\mu\nu}\delta_{\rho\sigma}+\overline{c}_{2}^{ab}\mathbf{F}_{a\mu\nu}\cdot\mathbf{F}_{b\rho\sigma})\psi_{b\sigma}\psi_{a\nu}
\tag{4}
$$

is the interspecies interaction [31], where $\overline{c}_{0}^{\alpha}$ and $\overline{c}_{2}^{\alpha}$ are expansion coefficients in terms of powers of dot product of the single-spin matrices of two atoms of species $\alpha$ and are linear combinations of singlet and triplet scattering lengths, $\overline{c}_{2}^{\alpha}$ is proportional to the differences between triplet and single scattering lengths of intraspecies scattering [1, 10], $\overline{c}_{0}^{ab}$ and $\overline{c}_{2}^{ab}$ are similar quantities for scattering between an $a$-atom and a $b$-atom, $\overline{c}_{2}^{ab}$ is proportional to the differences between triplet and single scattering lengths of interspecies scattering, and it has been shown that the coefficient of $(\mathbf{F}_{a}\cdot\mathbf{F}_{b})^{2}$ is zero [33].

For each species and each spin state, we follow the usual single mode approximation for the single-particle orbital wave function, and the usual assumption that this single particle orbital wave function is independent of spin. Therefore we have $\psi_{\alpha\mu}(\mathbf{r})=\alpha_{\mu}\phi_{\alpha}(\mathbf{r})$, where $\alpha_{\mu}=a_{\mu},b_{\mu}$ is the annihilation operator and $\phi_{\alpha}$ is the lowest single-particle orbital wave function for species $\alpha$ and spin-independent. Then the Hamiltonian can be simplified as

$$
\mathcal{H}=\frac{c^{a}}{2}\mathbf{S}_{a}^{2}+\frac{c^{b}}{2}\mathbf{S}_{b}^{2}+c^{ab}\mathbf{S}_{a}\cdot\mathbf{S}_{b}-\gamma\mathbf{B}\cdot\mathbf{S}_{a}-\gamma\mathbf{B}\cdot\mathbf{S}_{b},
\tag{5}
$$

where a constant is neglected,

$$
\mathbf{S}_{\alpha}=\alpha_{\mu}^{\dagger}\mathbf{F}_{\mu\nu}\alpha_{\nu}
\tag{6}
$$

is the total spin operator for species $\alpha$, $c^{\alpha}=\bar{c}_{2}^{\alpha} \int d^{3} r|\phi_{\alpha}|^{4}$ is the intraspecies spin coupling strength, $c^{ab}=$ $\bar{c}_{2}^{a b} \int d^{3} r|\phi_{a} \phi_{b}|^{2}$ is the interspecies spin coupling strength, and we have set $\gamma_{a}=\gamma_{b}=\gamma$, as indeed so for atoms with a same nuclear spin. Here we have neglected the quadratic Zeeman effect. This is reasonable under certain circumstances, as can be estimated by using parameter values for Na [11]. The quadratic Zeeman energy is $\hat{q} B_{0}^{2}$, where $\hat{q}=278 Hz / G^{2}, B_{0}$ can be 10mG to 500mG, hence the quadratic Zeeman energy is about $2.78 \times 10^{-2}$ to 70Hz. The linear Zeeman energy is about 1 to 100HZ. Therefore it is easy to reach the regime where the quadratic Zeeman effect is negligible.

$S_{a}, S_{b}$ together with the total spin $S$ and its $z$-component $S_{z}$ are all good quantum numbers, as $\mathbf{S}_{a}^{2}, \mathbf{S}_{b}^{2}$ and $\mathbf{S}^{2}$ all commute with the Hamiltonian (5). However it should be noted that $S_{a}$ and $S_{b}$ are not fixed numbers, as in the case of pseudospin-$\frac{1}{2}$ atoms, for which one can find $S_{a}=N_{a} / 2$ and $S_{b}=N_{b} / 2$. In the present case, $S_{a}, S_{b}$ and $S$ should all be determined by minimizing the energy.

In the presence of a magnetic field, for a given $S, S_{z}=S$ minimizes the energy. With $S_{a}, S_{b}, S$ and $S_{z}$ all being good quantum numbers, the ground state is

$$
|G\rangle=\left|S_{a}^{m}, S_{b}^{m}, S^{m}, S^{m}\right\rangle,
\tag{7}
$$

where $S_{a}^{m}, S_{b}^{m}$ and $S^{m}$ are, respectively, the values of $S_{a}, S_{b}$ and $S$ that minimize the energy

$$
\begin{aligned}
E= & \frac{c^{a}-c^{a b}}{2} S_{a}\left(S_{a}+1\right)+\frac{c^{b}-c^{a b}}{2} S_{b}\left(S_{b}+1\right) \\
& +\frac{c^{a b}}{2} S(S+1)-\gamma B S,
\end{aligned}
\tag{8}
$$

under the constraints

$$
\left|S_{a}-S_{b}\right| \leq S \leq S_{a}+S_{b}.
\tag{9}
$$

Note that the existence of three quantities $S_{a}, S_{b}$ and $S$ with the constraint (9) as well as the limited ranges of $S_{a}$ and $S_{b}$, and the dependence on the three parameters $c^{a}, c^{b}$ and $c^{a b} \neq 0$ makes this minimization problem highly nontrivial. We have managed to solve this problem in most of the parameter regimes, as reported in in Appendices. Before discussing these cases of $c^{a b} \neq 0$, we shall first take a look at the case of $c^{a b}=0$.

As we shall discuss different ground states in different regimes of the parameter space, some explanation of the nomenclature is in order here. The ground states in two neighboring parameter regimes are said to be continuously connected if each of them approaches the ground state on the boundary, when the parameters approach the boundary. It is then said that they belong to a same quantum phase. In contrast, if the two ground states in the two neighboring regimes approach different limits when the parameters approach the boundary, it is said that there is a discontinuity or quantum phase transition. There are several cases of discontinuity, for example, the two limits may be both different from the that on boundary, and they may also be two of the degenerate ground states on the boundary, besides, there is also the case that the ground state in one of the regimes approaches a ground state on the boundary, while the ground state in the other regime approaches a different limit.

The most interesting ground states in our system are those of EBEC, i.e. BEC with interspecies entanglement. Note that throughout this paper, a state which may be entangled is written in the the general form, i.e. $|S_{a}^{m}, S_{b}^{m}, S^{m}, S^{m}\rangle$. A state which is certainly disentangled is written in the form of $|S_{a}^{m}, S_{a}^{m}\rangle_{a}|S_{b}^{m}, S_{b}^{m}\rangle_{b}$

### III. $c^{ab}=0$

Without spin-exchange interaction between the two species, i.e. $c^{a b}=0$, the two species can be considered independently. The ground states are all disentangled. We have $E=E_{a}+E_{b}$, with

$$
\begin{aligned}
E_{\alpha} & =\frac{c^{\alpha}}{2} S_{\alpha}\left(S_{\alpha}+1\right)-\gamma B S_{\alpha} \\
& =\frac{c^{\alpha}}{2}\left(S_{\alpha}-\frac{\gamma B}{c^{\alpha}}+\frac{1}{2}\right)^{2}+const,
\end{aligned}
\tag{10}
$$

for $\alpha=a, b$. Throughout the paper, we use const to represent a constant whose actual value is not concerned and may not be the same each time it appears.

If $c^{\alpha}<0$, we always have $S_{\alpha}^{m}=N_{\alpha}$. If $c^{\alpha}>0$, one finds the following three subcases. (i) If $c^{\alpha} \geq 2 \gamma B$, then $S_{\alpha}^{m}=0$. (ii) If $\frac{2 \gamma B}{2 N_{\alpha}+1} \leq c^{\alpha} \leq 2 \gamma B$, then $S_{\alpha}^{m}=n_{\alpha} \equiv Int(\frac{\gamma B}{c^{\alpha}}-\frac{1}{2})$, where $Int(x)$ denotes the integer closest to $x$ while in its legitimate range, e.g. $0 \leq n_{\alpha} \leq N_{\alpha}$. (iii) If $c^{\alpha} \leq \frac{2 \gamma B}{2 N_{\alpha}+1}$, then $S_{\alpha}^{m}=N_{\alpha}$. As $n_{\alpha}$ reduces to 0 and $N_{\alpha}$ respectively at

<table>
<tbody><tr><td>$|N_a,N_a\rangle_a|0,0\rangle_b$</td><td>$|n_a,n_a\rangle_a|0,0\rangle_b$</td><td>$|0,0\rangle_a|0,0\rangle_b$</td></tr>
<tr><td></td><td></td><td></td></tr>
<tr><td>$|N_a,N_a\rangle_a|n_b,n_b\rangle_b$</td><td>$|n_a,n_a\rangle_a|n_b,n_b\rangle_b$</td><td>$|0,0\rangle_a|n_b,n_b\rangle_b$</td></tr>
<tr><td></td><td></td><td></td></tr>
<tr><td>$|N_a,N_a\rangle_a|N_b,N_b\rangle_b$</td><td>$|n_a,n_a\rangle_a|N_b,N_b\rangle_b$</td><td>$|0,0\rangle_a|N_b,N_b\rangle_b$</td></tr>
</tbody></table>

FIG. 1: Ground states in $c^a - c^b$ parameter plane for $c^{ab}=0$ and $B>0$. They are all direct products of the ground states of the two species, and are thus written in the form of $|S_a^m,S_a^m\rangle_a|S_b^m,S_b^m\rangle_b$. The two horizontal lines are $c^a=\frac{2\gamma B}{2N_a+1}$ and $c^a=2\gamma B$, while the two vertical lines are $c^b=\frac{2\gamma B}{2N_b+1}$ and $c^b=2\gamma B$. $n_a\equiv Int(\frac{\gamma B}{c^a}-\frac{1}{2})$, $n_b\equiv Int(\frac{\gamma B}{c^b}-\frac{1}{2})$.

the two boundaries, the ground state in $\frac{2\gamma B}{2N_a+1}\leq c^a\leq2\gamma B$ is continuously connected with those in $c^\alpha\geq2\gamma B$ and in $c^\alpha\leq\frac{2\gamma B}{2N_a+1}$.

Thus one obtains all the ground states in the parameter subspace of $c^{ab}=0$ and $B>0$, which can be written in the form of $|S_a^m,S_a^m\rangle_a|S_b^m,S_b^m\rangle_b$ and as depicted in FIG. 1. There are nine regimes, each is defined by the range of $c^a$ and $c^b$ specified above. In each regime, the ground state is a direct product of the ground states of the two species given above accordingly. Each ground state is continuously connected with those in the neighboring regimes. Therefore, on $c^a - c^b$ plane, ground states in all regimes belong to a same quantum phase.

As $B\rightarrow0$, however, the five crossover regimes tend to vanish, and the four ground states in the remaining four corner regimes become discontinuous, as already known [32]. Therefore, the quantum phase transitions among the ground states in the four quadrants of $c^a - c^b$ plane for $c^{ab}=0$ in absence of a magnetic field can be circumvented by turning on and then off a magnetic field. Hence a magnetic field has an interesting effect even in the regime without interspecies spin exchange.

One can imagine the three-dimensional parameter subspace of $c^{ab}=0$, with $c^a$, $c^b$ and $B\geq0$ as the three coordinates. The boundaries $c^a=\frac{2\gamma B}{2N_a+1}$, $c^a=2\gamma B$, $c^b=\frac{2\gamma B}{2N_b+1}$ and $c^b=2\gamma B$ are all planes starting from the origin and extending to positive infinities.

## IV. $c^{ab}<0$

For $c^{ab}\neq0$, we have worked out the complicated problem of minimizing $E$ with four variables $S_a$, $S_b$, $S$ and $B$ in most parameter regimes. But in some regimes, the calculations are too difficult or complicated for us to obtain the results. The calculation details are given in Appendix A. The ground states we obtained are listed in Table I.

For $c^{ab}<0$ while $B>0$, we have found the ground states in the second, third and fourth quadrants of $c^a - c^b$ plane, as depicted in FIG. 2. In comparison with the case of $B=0$ [32], a magnetic field $B>0$ both shifts the positions of the boundaries and modifies the ground states in the crossover regimes.

In the three outmost regimes, only the boundaries are shifted, while the ground states remain the same as those of $B=0$. The ground state is $|N_a,N_a\rangle_a|N_b,N_b\rangle_b$ in the regime $c^a\leq0$ while $c^b\leq\frac{2\gamma B-2N_a c^{ab}}{2N_b+1}$ and $c^b\leq0$ while $c^a\leq\frac{2\gamma B-2N_b c^{ab}}{2N_a+1}$. In the regimes $c^a\leq0$ while $c^b\geq2\gamma B-2N_a c^{ab}$ and $c^b\leq0$ while $c^a\geq2\gamma B-2N_b c^{ab}$, the ground states are $|N_a,N_a\rangle_a|0,0\rangle_b$ and $|0,0\rangle_a|N_b,N_b\rangle_b$ respectively.

In the crossover regimes, the ground states are also modified. For $c^a\leq0$ while $\frac{2\gamma B-2N_a c^{ab}}{2N_b+1}\leq c_b\leq2\gamma B-2N_a c^{ab}$, the ground state is $|N_a,N_a\rangle_a|n_1',n_1'\rangle_b$, where $n_1'=Int[\frac{\gamma B+N_a|c^{ab}}{c^b}-\frac{1}{2}]$. Likewise, for $c^b\leq0$ while $\frac{2\gamma B-2N_b c^{ab}}{2N_a+1}\leq c_a\leq$

<table>
  <thead>
    <tr>
      <th>No.</th>
      <th colspan="2">Parameter regimes</th>
      <th>Ground states</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">1,A2a</td>
      <td rowspan="6">$c^{ab}<0$</td>
      <td>$c^a\leq0$,<br>$c^b\leq\frac{2\gamma B - 2N_a c^{ab}}{2N_b + 1}$</td>
      <td>$|N_a,N_a\rangle_a|N_b,N_b\rangle_b$,<br>disentangled</td>
    </tr>
    <tr>
      <td>$c^a\leq0$,<br>$\frac{2\gamma B - 2N_a c^{ab}}{2N_b + 1}\leq c_b\leq2\gamma B - 2N_a c^{ab}$</td>
      <td>$|N_a,N_a\rangle_a|n_1',n_1'\rangle_b$<br>disentangled, $n_1'\equiv Int\left[\frac{\gamma B + N_a|c^{ab}|}{c^b}-\frac{1}{2}\right]$</td>
    </tr>
    <tr>
      <td>A2c</td>
      <td>$c^a\leq0$,<br>$c^b\geq2\gamma B - 2N_a c^{ab}$</td>
      <td>$|N_a,S_z\rangle_a|0,0\rangle_b$,<br>disentangled</td>
    </tr>
    <tr>
      <td>1,A3a</td>
      <td>$c^b\leq0$,<br>$c^a\leq\frac{2\gamma B - 2N_b c^{ab}}{2N_a + 1}$</td>
      <td>$|N_a,N_a\rangle_a|N_b,N_b\rangle_b$,<br>disentangled</td>
    </tr>
    <tr>
      <td>A3b</td>
      <td>$c^b\leq0$,<br>$\frac{2\gamma B - 2N_b c^{ab}}{2N_a + 1}\leq c_a\leq2\gamma B - 2N_b c^{ab}$</td>
      <td>$|n_2',n_2'\rangle_a|N_b,N_b\rangle_b$<br>disentangled, $n_2'\equiv Int\left[\frac{\gamma B + N_b|c^{ab}|}{c^a}-\frac{1}{2}\right]$</td>
    </tr>
    <tr>
      <td>A3c</td>
      <td>$c^b\leq0$,<br>$c^a\geq2\gamma B - 2N_b c^{ab}$</td>
      <td>$|0,0\rangle_a|N_b,N_b\rangle_b$,<br>disentangled</td>
    </tr>
    <tr>
      <td>IV</td>
      <td rowspan="11">$0 < c^{ab}\leq2\gamma B$</td>
      <td colspan="2">$c^a < c^{ab}, c^b < c^{ab}$<br>(boundaries were discussed in Ref. [30])</td>
      <td>$|N_a,N_b,n,n\rangle$, $n\equiv Int\left(\frac{\gamma B}{c^{ab}}-\frac{1}{2}\right)$<br>entangled,</td>
    </tr>
    <tr>
      <td>B1</td>
      <td rowspan="4">$c^a\geq c^b > c^{ab}$<br>$N_a=N_b=N$</td>
      <td>$c^b\geq2\gamma B$</td>
      <td>$|0,0\rangle_a|0,0\rangle_b$,<br>disentangled</td>
    </tr>
    <tr>
      <td>B2a</td>
      <td>$c^b < 2\gamma B\leq\frac{c^a - c^{ab}}{c^b - c^{ab}}c^b$</td>
      <td>$|0,0\rangle_a|n_b,n_b\rangle_b$, $n_b\equiv Int\left[\frac{\gamma B}{c^b}-\frac{1}{2}\right]$<br>disentangled</td>
    </tr>
    <tr>
      <td>B2b</td>
      <td>$2\gamma B > \frac{c^a - c^{ab}}{c^b - c^{ab}}c^b$</td>
      <td>$|n_{a3},n_{a3}\rangle_a|n_{b1},n_{b1}\rangle_b$, $n_{a3}\equiv Int\left[\frac{2\gamma B|c^b - c^{ab}|-c^b(c^a - c^{ab})}{2[c^a c^b - (c^{ab})^2]}\right]$<br>disentangled, $n_{b1}\equiv Int\left[\frac{\gamma B - c^{ab}n_{a3}}{c^b}-\frac{1}{2}\right]$</td>
    </tr>
    <tr>
      <td>C1</td>
      <td rowspan="2">$c^a > c^{ab} > c^b$<br>$c^a c^b > (c^{ab})^2$<br>$N_a=N_b=N > N^*$</td>
      <td>$2\gamma B\leq\frac{c^a - c^{ab}}{c^{ab} - c^b}c^b$</td>
      <td>$|0,n_b,n_b,n_b\rangle=|0,0\rangle_a|n_b,n_b\rangle_b$<br>disentangled</td>
    </tr>
    <tr>
      <td>C2</td>
      <td>$2\gamma B > \frac{c^a - c^{ab}}{c^{ab} - c^b}c^b$</td>
      <td>$|n_{a3},n_{b2},n_{b2}-n_{a3},n_{b2}-n_{a3}\rangle$<br>entangled, $n_{b2}\equiv Int\left[\frac{\gamma B + c^{ab}n_{a3}}{c^b}-\frac{1}{2}\right]$</td>
    </tr>
    <tr>
      <td>D1</td>
      <td rowspan="4">$c^b\geq c^a > c^{ab}$<br>$N_a=N_b=N$</td>
      <td>$c^a\geq2\gamma B$</td>
      <td>$|0,0\rangle_a|0,0\rangle_b$,<br>disentangled</td>
    </tr>
    <tr>
      <td>D2a</td>
      <td>$c^a < 2\gamma B\leq\frac{c^b - c^{ab}}{c^a - c^{ab}}c^a$</td>
      <td>$|n_a,n_a\rangle_a|0,0\rangle_b$, $n_a\equiv Int\left[\frac{\gamma B}{c^a}-\frac{1}{2}\right]$<br>disentangled</td>
    </tr>
    <tr>
      <td>D2b</td>
      <td>$2\gamma B > \frac{c^b - c^{ab}}{c^a - c^{ab}}c^a$</td>
      <td>$|n_{a1},n_{a1}\rangle_a|n_{b3},n_{b3}\rangle_b$, $n_{b3}\equiv Int\left[\frac{2\gamma B|c^a - c^{ab}|-c^a(c^b - c^{ab})}{2[c^a c^b - (c^{ab})^2]}\right]$<br>disentangled, $n_{a1}\equiv Int\left[\frac{\gamma B - c^{ab}n_{b3}}{c^a}-\frac{1}{2}\right]$</td>
    </tr>
    <tr>
      <td>E1</td>
      <td rowspan="2">$c^b > c^{ab} > c^a$<br>$c^a c^b > (c^{ab})^2$<br>$N_a=N_b=N > N^*$</td>
      <td>$2\gamma B\leq\frac{c^b - c^{ab}}{c^{ab} - c^a}c^a$</td>
      <td>$|n_a,0,n_a,n_a\rangle=|n_a,n_a\rangle_a|0,0\rangle_b$<br>disentangled</td>
    </tr>
    <tr>
      <td>E2</td>
      <td>$2\gamma B > \frac{c^b - c^{ab}}{c^{ab} - c^a}c^a$</td>
      <td>$|n_{a2},n_{b3},n_{a2}-n_{b3},n_{a2}-n_{b3}\rangle$<br>entangled, $n_{a2}\equiv Int\left[\frac{\gamma B + c^{ab}n_{b3}}{c^a}-\frac{1}{2}\right]$</td>
    </tr>
    <tr>
      <td>II</td>
      <td rowspan="2">$c^{ab}\geq2\gamma B > 0$</td>
      <td colspan="2">$c^a > c^{ab}, c^b > c^{ab}$<br>(boundaries were discussed in Ref. [30])</td>
      <td>$|0,0\rangle_a|0,0\rangle_b$,<br>disentangled</td>
    </tr>
    <tr>
      <td>III</td>
      <td colspan="2">$c^a < c^{ab}, c^b < c^{ab}$, $N_a=N_b=N$<br>(boundaries were discussed in Ref. [30])</td>
      <td>$|N,N,0,0\rangle$<br>entangled</td>
    </tr>
  </tbody>
</table>

TABLE I: Ground states of a mixture of two spin-1 atomic gases in different parameter regimes for $c^{ab}\neq0$ and $B>0$. For $c^{ab}<0$, the ground states are always disentangled, and are written in the form of $|S_a^m,S_a^m\rangle_a|S_b^m,S_b^m\rangle_b$. For $c^{ab}>0$, some ground states are disentangled and are also written in this form. Some ground states are written in the form of $|S_a^m,S_a^m,S^m,S^m\rangle$, which may be entangled or disentangled, depending on the parameter values. The ordering numbers are just the corresponding section numbers in the Appendices where the calculation are done, or as numbered in Ref. [31] for those calculated there (IV, II and III). $N^*$ is defined in Eq. (C4).

$2\gamma B - 2N_b c^{ab}$, the ground state is $|n_2',n_2'\rangle_a|N_b,N_b\rangle_b$, where $n_2'=Int\left[\frac{\gamma B + N_b|c^{ab}|}{c^a}-\frac{1}{2}\right]$.

We see continuous connections in both $c^{ab}$ and $B$ dimensions. As $B\rightarrow0$, all the ground states in these three quadrants of $c^a - c^b$ plane for $c^{ab}<0$ reduce to the corresponding ones in absence of a magnetic field. On the other hand, as $c^{ab}\rightarrow0$, the ground states in the these three quadrants reduce to those for $c^{ab}=0$, given in last section.

Note that in all subregimes of $c^{ab}\leq0$, the ground states are always disentangled, as $S^m=S_a^m+S_b^m$.

![](./images/813338292027129856_1.jpg)

FIG. 2: Ground states in $c^a - c^b$ parameter plane for $c^{ab} < 0$ and $B > 0$. They are all disentangled and are thus written in the form of $|S_a^m,S_a^m\rangle_a|S_b^m,S_b^m\rangle_b$. The states in the second, third and fourth quadrants are all continuously connected on boundaries. $n_1' \equiv Int[\frac{\gamma B+N_a|c^{ab}|}{c^b}-\frac{1}{2}], n_2' \equiv Int[\frac{\gamma B+N_b|c^{ab}|}{c^a}-\frac{1}{2}]$. The four boundaries are $c_a=\frac{2\gamma B-2N_b c^{ab}}{2N_a+1}$, $c_a=2\gamma B-2N_b c^{ab}$, $c_b=\frac{2\gamma B-2N_a c^{ab}}{2N_b+1}$ and $c_b=2\gamma B-2N_a c^{ab}$. The states in the first quadrant have not yet been determined.

### V. $0 < c^{ab} < 2\gamma B$

Now we turn to antiferromagnetic interspecies spin coupling. For $0 < c^{ab} \leq 2\gamma B$, it has been known previously that if $c^a < c^{ab}$ and $c^b < c^{ab}$, the ground state is $|N_a,N_b,n,n\rangle$, where $n \equiv Int(\frac{\gamma B}{c^{ab}}-\frac{1}{2})$ satisfies $|N_a-N_b| \leq n \leq N_a+N_b$ [32]. This state is entangled unless $n = N_a + N_b$. The ground states on the boundaries $c^a = c^{ab}$ and $c^b = c^{ab}$ have also been discussed in details. Especially, it has been known that if $c^a = c^b = c^{ab}$, then there are many degenerate ground states in the form of $|S_a,S_b,n,n\rangle$, as far as $S_a, S_b$ and $n$ satisfy the constraint $|S_a - S_b| \leq n \leq S_a + S_b$.

We have also determined the ground states in the regime $0 < c^{ab} \leq 2\gamma B$ and $c^a c^b > (c^{ab})^2$. This regime is divided into seven subregimes, but the ground states are all continuously connected on the boundaries between these subregimes, as depicted in $c^a - c^b$ phase diagram for a given value of $c^{ab}$ with $0 < c^{ab} < 2\gamma B$ (FIG. 3), drawn according to Table I.

For $c^b > 2\gamma B$ and $c^a > 2\gamma B$, the ground state is $|0,0,0,0\rangle = |0,0\rangle_a|0,0\rangle_b$. In the regime defined by $c^b \leq 2\gamma B$, $2\gamma B \leq \frac{c^a - c^{ab}}{c^b - c^{ab}}c^b$ (i.e. below the hyperbola $2\gamma B = \frac{c^a - c^{ab}}{c^b - c^{ab}}c^b$), and $2\gamma B \leq \frac{c^a - c^{ab}}{c^{ab} - c^b}c^b$ (i.e. above the hyperbola $2\gamma B = \frac{c^a - c^{ab}}{c^{ab} - c^b}c^b$), the ground state is $|0,0\rangle_a|n_b,n_b\rangle_b$, where $n_b \equiv Int[\frac{\gamma B}{c^b} - \frac{1}{2}]$, which reduces to 0 when $c^b = 2\gamma B$. In the regime defined by $c^a \geq c^b > c^{ab}$ and $2\gamma B > \frac{c^a - c^{ab}}{c^b - c^{ab}}c^b$, that is, surrounded by $c^a = c^b$ and $2\gamma B = \frac{c^a - c^{ab}}{c^b - c^{ab}}c^b$, the ground state is $|n_{a3},n_{a3}\rangle_a|n_{b1},n_{b1}\rangle_b$, where $n_{a3} \equiv Int[\frac{2\gamma B|c^b - c^{ab}|-c^b(c^a - c^{ab})}{2[c^a c^b - (c^{ab})^2]}]$, $n_{b1} \equiv Int[\frac{\gamma B - c^{ab}n_{a3}}{c^b} - \frac{1}{2}]$. These states are all disentangled. The ground state is $|n_{a3},n_{b2},n_{b2}-n_{a3},n_{b2}-n_{a3}\rangle$, where $n_{b2} \equiv Int[\frac{\gamma B + c^{ab}n_{a3}}{c^b} - \frac{1}{2}]$, in the regime numbered as C2 and defined by $c^a > c^{ab} > c^b$, $c^a c^b > (c^{ab})^2$ and $2\gamma B \geq \frac{c^a - c^{ab}}{c^{ab} - c^b}c^b$, for $N_a = N_b = N > N^*$, where $N^*$ is given in (C4). This state is always entangled except on the boundary $2\gamma B = \frac{c^a - c^{ab}}{c^{ab} - c^b}c^b$, where the state reduces to $|0,0\rangle_a|n_b,n_b\rangle_b$. By substituting the boundary values of $c^a$ and $c^b$ to the values of $S_a, S_b$ and $S$ that depend on them, it is not difficult to see that the ground states in each subregime continuously connected with those in its neighboring subregimes.

Similarly, by exchanging the labels $a$ and $b$, we know the ground states in the part of $c^a c^b > (c^{ab})^2$ with $c^a \leq c^b$ and $c^a \leq 2\gamma B$. In the subregime defined by $c^a \leq 2\gamma B$, $2\gamma B \leq \frac{c^b - c^{ab}}{c^a - c^{ab}}c^a$ (i.e. above the hyperbola $2\gamma B = \frac{c^b - c^{ab}}{c^a - c^{ab}}c^a$), and $2\gamma B \leq \frac{c^b - c^{ab}}{c^{ab} - c^a}c^a$ (i.e. on the right of the hyperbola $2\gamma B = \frac{c^b - c^{ab}}{c^{ab} - c^a}c^a$), the ground state is $|n_a,n_a\rangle_a|0,0\rangle_b$, where $n_a \equiv Int[\frac{\gamma B}{c^a} - \frac{1}{2}]$. In the regime defined by $c^b \geq c^a > c^{ab}$ and $2\gamma B > \frac{c^b - c^{ab}}{c^a - c^{ab}}c^a$, that is, surrounded by $c^a = c^b$ and $2\gamma B = \frac{c^b - c^{ab}}{c^a - c^{ab}}c^a$, the ground state is $|n_{a1},n_{a1}\rangle_a|n_{b3},n_{b3}\rangle_b$, where $n_{b3} \equiv Int[\frac{2\gamma B|c^a - c^{ab}|-c^a(c^b - c^{ab})}{2[c^a c^b - (c^{ab})^2]}]$,

![](./images/813338292027129856_2.jpg)

FIG. 3: Ground states in $c^a \ -\ c^b$ parameter plane for $0 < c^{ab} \leq 2\gamma B$ and $B > 0$, with $N_a = N_b = N$. A state which is disentangled is written in the form of $|S_a^m,S_a^m\rangle_a|S_b^m,S_b^m\rangle_b$. A state which may be entangled is written in the general form of $|S_a^m,S_b^m,S^m,S^m\rangle$. The borders of $|N,N,n,n\rangle$ in the lower left part is $c^a = c^{ab}$ and $c^b = c^{ab}$. The ground state here is $|N_a,N_b,n,n\rangle$ for generic $N_a$ and $N_b$, which is entangled unless $n = N_a + N_b$. The complete hyperbola is $c^a c^b = (c^{ab})^2$, above which all the ground states are continuous connected, forming a single quantum phase. It is $|0,0\rangle_a|0,0\rangle_b$ in the upper right part $c^a \geq 2\gamma B$ and $c^b \geq 2\gamma B$. Below it the ground state is $|0,0\rangle_a|n_b,n_b\rangle_b$, which is bounded on the left by $2\gamma B \leq \frac{c^a - c^{ab}}{c^b - c^{ab}}c^b$, and on the bottom by $2\gamma B \leq \frac{c^a - c^{ab}}{c^{ab} - c^b}c^b$. Surrounded by the former boundary and $c^a = c^b$ is the regime numbered as B2b, where the ground state is $|n_{a3},n_{a3}\rangle_a|n_{b1},n_{b1}\rangle_b$. In the regime numbered as C2, i.e. between $2\gamma B \leq \frac{c^a - c^{ab}}{c^{ab} - c^b}c^b$ and $c^a c^b = (c^{ab})^2$, the ground state is $|n_{a3},n_{b2},n_{b2}-n_{a3},n_{b2}-n_{a3}\rangle$, which is entangled except on the boundary with $|0,0\rangle_a|n_b,n_b\rangle_b$. Similarly, the ground state is $|n_a,n_a\rangle_a|0,0\rangle_b$, in the regime bounded by $c^a = 2\gamma B$ on the right, $2\gamma B = \frac{c^b - c^{ab}}{c^a - c^{ab}}c^a$ below and $2\gamma B = \frac{c^b - c^{ab}}{c^{ab} - c^a}c^a$ on the left. In the regime numbered as D2b, as surrounded by $c^a = c^b$ and $2\gamma B = \frac{c^b - c^{ab}}{c^a - c^{ab}}c^a$, the ground state is $|n_{a1},n_{a1}\rangle_a|n_{b3},n_{b3}\rangle_b$. In the regime numbered as E2, i.e. between $c^a c^b = (c^{ab})^2$ and $2\gamma B = \frac{c^b - c^{ab}}{c^{ab} - c^a}c^a$, the ground state is $|n_{a2},n_{b3},n_{a2}-n_{b3},n_{a2}-n_{b3}\rangle$, which is entangled except on the boundary with $|n_a,n_a\rangle_a|0,0\rangle_b$. For the regimes $c^a > c^{ab} > c^b$ and $c^b > c^{ab} > c^a$, the results are subject to the condition $N > N^*$. $n$, $n_a$, $n_b$, $n_{a2}$, $n_{b2}$ $n_{a3}$, $n_{b3}$ and $N^*$ are defined in the main text and Table I.

$n_{a1} \equiv Int[\frac{\gamma B - c^{ab}n_{b3}}{c^a} - \frac{1}{2}]$. These states are all disentangled. Finally, the ground state is $|n_{a2},n_b,n_{a2}-n_b,n_{a2}-n_b\rangle$, where $n_{a2} \equiv Int[\frac{\gamma B + c^{ab}n_b}{c^b} - \frac{1}{2}]$, in the regime numbered as E2 and defined by $c^b > c^{ab} > c^a$, $c^a c^b > (c^{ab})^2$ and $2\gamma B \geq \frac{c^b - c^{ab}}{c^{ab} - c^a}c^a$, for $N_a = N_b = N > N^*$. This state is always entangled except on the boundary $2\gamma B = \frac{c^b - c^{ab}}{c^{ab} - c^a}c^a$, where the state reduces to $|n_a,n_a\rangle_a|0,0\rangle_b$. The ground states in each subregime continuously connected with those in its neighboring subregimes.

Also, the ground states $|n_{a1},n_{a1}\rangle_a|n_{b3},n_{b3}\rangle_b$ and $|n_{a3},n_{a3}\rangle_a|n_{b1},n_{b1}\rangle_b$ are continuously connected on the boundary $c^{ab} < c^a = c^b \leq 2\gamma B$, with $n_{a3}=n_{b1}=n_{a1}=n_{b3}=\frac{2\gamma B - c^a}{2(c^a + c^{ab})}$.

But at the point $c^a = c^b = c^{ab}$, the ground states in the six subregimes of $c^a c^b > (c^{ab})^2$ converging at this point are discontinuous with other, as one can see from $n_a = n_b = Int(\frac{\gamma B}{c^{ab}} - \frac{1}{2})$, $n_{a3}=n_{b1}=n_{b3}=n_{a1}=Int(\frac{\gamma B}{2c^{ab}} - \frac{1}{4})$ and $n_{b2}=n_{a2}=Int(\frac{3\gamma B}{2c^{ab}} - \frac{3}{4})$ at this point.

As $c^{ab} \to 2\gamma B$, $c^a = c^b = 2\gamma B$ approaches $c^a = c^b = c^{ab}$, hence the regimes B2b and D2b tend to vanish.

### VI. $c^{ab} \geq 2\gamma B$

For $c^{ab} \geq 2\gamma B$ [30], it has been known that the ground state is $|0,0\rangle_a|0,0\rangle_b$ for $c^a > c^{ab}$ and $c^b > c^{ab}$, and is $|N,N,0,0\rangle$ for $c^a < c^{ab}$, $c^b < c^{ab}$ and $N_a = N_b = N$. This result is consistent with with those obtained for $0 < c^{ab} \leq 2\gamma B$. Hence for the regime $c^a > c^{ab}$ and $c^b > c^{ab}$ and the regime $c^a < c^{ab}$, $c^b < c^{ab}$, $N_a = N_b = N$, the ground states for $c^{ab} \leq 2\gamma B$ and those for $c^{ab} \geq 2\gamma B$ are continuously connected at $c^{ab} = 2\gamma B$.

![](./images/813338292027129856_3.jpg)

FIG. 4: Ground states in $c^a$ $-$ $c^b$ parameter plane for $c^{ab} \geq 2\gamma B$ and $B > 0$, with $N_a = N_b = N$. The ground state is the entangled state $|N,N,0,0\rangle$ in the regime $c^a < c^{ab}$ and $c^b < c^{ab}$. It is the disentangled state $|0,0\rangle_a|0,0\rangle_b$ in the regime $c^a > c^{ab}$ and $c^b > c^{ab}$.

Especially, in the cases we have studied, under the condition $N_a = N_b = N$, in the regime $c^a < c^{ab}$ and $c^b < c^{ab}$ and in the regime $c^a > 2\gamma B$ and $c^b > 2\gamma B$, $c^{ab}=2\gamma B > 0$ is not a boundary, i.e. the ground states are respectively the same in these two regimes for $c^{ab} \geq 2\gamma B$ and for $0 < c^{ab} \leq 2\gamma B$.

## VII. QUANTUM PHASE TRANSITIONS

### A. Quantum phase transitions at $c^a = c^b = c^{ab}$

In the regime of $0 < c^{ab} < 2\gamma B$, quantum phase transitions take place at $c^a = c^b = c^{ab}$, which is the boundary between the two phases discussed above for $0 < c^{ab} \leq 2\gamma B$. It is a point on $c^a - c^b$ plane with given $c^{ab}$ and $B$, and is a line in the three dimensional $c^a - c^b - c^{ab}$ subspace with a given $B$, and is a two-dimensional surface in the four dimensional $c^a - c^b - c^{ab} - B$ space.

At $c^a = c^b = c^{ab}$, any state in the form of $|S_a,S_b,n,n\rangle$ with arbitrary legitimate values of $S_a$, $S_b$ and $n$ is a ground state. Therefore its degenerate ground state space includes the ground states in all the seven regimes we have studied that contact at this degenerate point, that is, the ground states of the six subregimes of $c^a c^b > (c^{ab})^2$ neighboring at $c^a = c^b = c^{ab}$, as well as the ground state $|N_a,N_b,n,n\rangle$ in the regime $c^a < c^{ab}$ and $c^b < c^{ab}$. Therefore in entering $c^a = c^b = c^{ab}$ from one of the two phases, the ground state remains as the original, and then discontinues in entering the any of the other six regimes. Note that there is also a discontinuity in transiting, through the critical point $c^a = c^b = c^{ab}$, from one of the six regimes belonging to the same phase.

In any of these seven regimes converging at the point $c^a = c^b = c^{ab}$, we always have $S^m = S_z^m = n$. Therefore, the quantum phase transition is a continuous transition.

If $B \to 0$, for $0 < c^{ab} < 2\gamma B$, the range of $c^{ab}$ has to be diminished as well, hence in this regime $c^{ab} \to 0$ too. Consequently the regime of $|0,0\rangle_a|0,0\rangle_b$ expands to occupy the whole first quadrant of $c^a - c^b$ plane, while the other regimes in the first quadrant have to be diminished. On the other hand, we have $n \to 0$ as a consequence of $B \to 0$. Therefore the ground states approach to the corresponding ones for $c^{ab} > 2\gamma B$, but $c^{ab}$ being infinitesimally positive is qualitatively different from the case of $c^{ab} = 0$, as will be discussed in the next subsection.

For $c^{ab} \geq 2\gamma B$, the quantum phase transition from the ground state $|N,N,0,0\rangle$ in the regime $c^a < c^{ab}$ while $c^b < c^{ab}$ to the ground state $|0,0\rangle_a|0,0\rangle_b$ in the regime $c^a > c^{ab}$ and $c^b > c^{ab}$ is similar to the one for $c^{ab} < 2\gamma B$, with $n$ in the latter becoming 0. Hence it is also a continuous quantum phase transition.

<table>
    <tbody>
        <tr>
            <td rowspan="3">$|N_a,N_b,n,n\rangle$</td>
            <td>$|n_a,n_a\rangle_a|0,0\rangle_b$</td>
            <td>$|0,0\rangle_a|0,0\rangle_b$</td>
        </tr>
        <tr>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>$|n_a,n_a\rangle_a|n_b,n_b\rangle_b$</td>
            <td>$|0,0\rangle_a|n_b,n_b\rangle_b$</td>
        </tr>
    </tbody>
</table>

FIG. 5: Ground states in $c^a - c^b$ parameter plane for $c^{ab}=0+$ and $B>0$. The two horizontal lines are $c^a=0$ and $c^a=2\gamma B$, while the two vertical lines are $c^b=0$ and $c^b=2\gamma B$. The ground states are in the disentangled form of $|S_a^m,S_a^m\rangle_a|S_b^m,S_b^m\rangle_b$ in all the regimes with $c^a>0$ and $c^b>0$, but are in the form of $|S_a^m,S_b^m,S^m,S^m\rangle$ in the regime with $c^a<0$ and $c^b<0$.

### B. Quantum phase transitions from $c^{ab}=0$ to $c^{ab}>0$

On the other hand, when $c^{ab}\to0$ from the positive side, i.e, $c^{ab}=0+$, under a given $B$, the regime of $|0,0\rangle_a|0,0\rangle_b$ remains unchanged, while the regime of $|N_a,N_b,n,n\rangle$ approaches the third quadrant, and the hyperbola $c^a c^b=(c^{ab})^2$ approaches the positive $c^a$ and $c^b$ axes. The regime of $|0,0\rangle_a|n_b,n_b\rangle_b$ approaches $c^a\geq2\gamma B$ while $0<c^b<2\gamma B$, similarly the regime of $|n_a,n_a\rangle_a|0,0\rangle_b$ approaches $c^b\geq2\gamma B$ while $0<c^a<2\gamma B$. The regimes B2b plus D2b become the regime $0<c^a<2\gamma B$ and $0<c^b<2\gamma B$, where the ground state approaches $|n_a,n_a\rangle_a|n_b,n_b\rangle_b$. Note that the subregime of $c^a c^b>(c^{ab})^2$ with $c^a>c^{ab}>c^b$ and that with $c^b>c^{ab}>c^a$, including the two subregimes of entangled ground states, tend to vanish. In FIG. 5, we draw the $c^a - c^b$ phase diagram for a given $B$ while $c^{ab}=0+$, referring to that $c^{ab}\to0$ from positive.

Comparing the ground states of $c^{ab}=0$ (FIG. 1) and $c^{ab}=0+$ (FIG. 5), we can see there are discontinuities between $c^{ab}>0$ and $c^{ab}=0$. First, in the third quadrant, the ground state is $|N_a,N_a\rangle_a|N_b,N_b\rangle_b$ for $c^{ab}=0$, discontinuing with $|N_a,N_b,n,n\rangle$ for $c^{ab}>0$. This discontinuity already exists when $B=0$ [32]. This quantum phase transition is first order as $S^m$ has a discontinuity except in the special case $n=N_a+N_b$, for which the transition becomes continuous.

Moreover, there are also other discontinuities, which are induced by $B>0$. On a $c^a - c^b$ plane, the boundaries $c^a=2\gamma B$ and $c^b=2\gamma B$ exist both for $c^{ab}=0+$ and $c^{ab}=0$. However, the other two boundaries are different, that is, they are $c^a=0$ and $c^b=0$ for $c^{ab}=0+$, but are $c^a=\frac{2\gamma B}{2N_a+1}$ and $c^b=\frac{2\gamma B}{2N_b+1}$ for $c^{ab}=0$, though the differences diminish as $N_a$ and $N_b$ approach infinities.

Consequently, there are five discontinuities induced by $B$ for $c^a>0$ and $c^b>0$. In the regime $0\leq c^a\leq\frac{2\gamma B}{2N_a+1}$ and $c^b\geq2\gamma B$, the ground state discontinues from $|n_a,n_a\rangle_a|N_b,N_b\rangle$ for $c^{ab}=0+$ to $|N_a,N_a\rangle|N_b,N_b\rangle$ for $c^{ab}=0$. This is a first order quantum phase transition except in the special case of $n_a=N_a$, in which the transition becomes continuous.

In the regime $0\leq c^a\leq\frac{2\gamma B}{2N_a+1}$ and $\frac{2\gamma B}{2N_b+1}\leq c^b\leq2\gamma B$, the ground state discontinues from $|n_a,n_a\rangle_a|n_b,n_b\rangle$ for $c^{ab}=0+$ to $|N_a,N_a\rangle|n_b,n_b\rangle$ for $c^{ab}=0$. This is a first order quantum phase transition except in the special case of $n_a=N_a$.

In the regime $0\leq c^a\leq\frac{2\gamma B}{2N_a+1}$ and $0\leq c^b\leq\frac{2\gamma B}{2N_b+1}$, the ground state discontinues from $|n_a,n_a\rangle_a|n_b,n_b\rangle$ for $c^{ab}=0+$ to $|N_a,N_a\rangle_a|N_b,N_b\rangle$ for $c^{ab}=0$. This is a first order quantum phase transition except in the special case of $n_a=N_a$ while $n_b=N_b$.

In the regime $\frac{2\gamma B}{2N_a+1}\leq c^a\leq2\gamma B$ and $0\leq c^b\leq\frac{2\gamma B}{2N_b+1}$, the ground state discontinues from $|n_a,n_a\rangle_a|n_b,n_b\rangle$ for $c^{ab}=0+$ to $|n_a,n_a\rangle_a|N_b,N_b\rangle$ for $c^{ab}=0$. This is a first order quantum phase transition except in the special case of $n_b=N_b$.

In the regime $c^a \geq 2\gamma B$ and $0 \leq c^b \leq \frac{2\gamma B}{2N_b+1}$, the ground state discontinues from $|0,0\rangle_a|n_b,n_b\rangle$ for $c^{ab}=0+$ to $|0,0\rangle_a|N_b,N_b\rangle$ for $c^{ab}=0$. This is a first order quantum phase transition except in the special case of $n_b=N_b$.

Therefore, we find five places of quantum phase transitions from $B=0$ to $B>0$. In other words, the entire subspace of $B=0$ is critical.

## VIII. INTERSPECIES ENTANGLEMENT

Our results indicate that a necessary condition for the ground state to be entangled between the two species is $c^{ab}>0$. We have found that the ground state is an entangled state entangled $|N_a,N_b,n,n\rangle$ for $0<c^{ab}<2\gamma B$, $c^a<c^{ab}$ and $c^b<c^{ab}$. In case $N_a=N_B=N$, we have also found that the ground state is a maximal entangled state $|N,N,0,0\rangle$ for $c^{ab}>2\gamma B$, $c^a<c^{ab}$ and $c^b<c^{ab}$.

With interspecies entanglement, the occupation number of each spin state of each species is subject to fluctuation [28]. However, even in absence of interspecies entanglement, such fluctuations can still exist, and there can be occupation number entanglement among different single particle states defined by the spin and the species. Such is the singlet ground state of single species of spinor atoms, for example. Therefore particle number fluctuations are not satisfactory characterizations of interspecies entanglement caused by interspecies spin exchanges.

A better characterization is an interspecies correlation function, e.g. $\langle N_{a\sigma}N_{b\sigma'}\rangle-\langle N_{a\sigma}\rangle\langle N_{b\sigma'}\rangle$, which vanishes for disentangled state and is nonvanishing if there is interspecies entanglement [28].

One can also simply use the spin of freedom of the two species to discuss the entanglement between the two species, treating the two species like two giant spins. Then, of course, the entanglement entropy can be calculated. For state $|S_a^m,S_b^m,S^m,S^m\rangle$, the entanglement entropy is
$$
\mathcal{E}=-\sum_{S_{bz}=-S_b^m}^{S_b^m} |g(S_{bz})|^2\log_{2S_b^m+1}|g(S_{bz})|^2,
\tag{11}
$$
where it is assumed that $S_a^m\geq S_b^m$, $g(S_{bz})\equiv\langle S_a^m,S^m-S_{bz};S_b^m,S_{bz}|S_a^m,S_b^m,S^m,S^m\rangle$ is the Clebsch-Gordan coefficient. If $S_a^m\leq S_b^m$, the subscripts $a$ and $b$ are exchanged. $\mathcal{E}=0$ for disentangled states, while $\mathcal{E}=1$ for state $|N,N,0,0\rangle$.

We also note that there is a simple yet experimentally measurable quantity as a characterization of the interspecies entanglement. This is just the total magnetization $S^m$. If $S^m=S_a^m+S_b^m$, there can only be one term in the Schmidt decomposition of the ground state in terms of $|S_a^m,S_{az}\rangle$ and $|S_b^m,S_{bz}\rangle$, consequently it is disentangled. If $S^m=|S_a^m-S_b^m|$, the ground state is entangled, as there is $2L+1$ terms in the Schmidt decomposition, where $L$ represents represents the smaller one of $S_a^m$ and $S_b^m$.

## IX. SUMMARY

We have obtained most of the ground states of a mixture of spin-1 Bose gases with interspecies spin coupling in presence of a magnetic field. For $c^{ab}\leq0$, the ground states, which are all disentangled, belong to a single quantum phase. For $c^{ab}<0$, a magnetic field modifies the ground states and the boundaries between them. For $c^{ab}=0$, a magnetic field induces some crossover regimes, hence discontinuities between ground states in different quadrants of $c^a-c^b$ plane in absence of a magnetic field now disappear.

For $c^a<c^{ab}$ and $c^b<c^{ab}$, a magnetic field divides the regime of $c^{ab}>0$ into two regimes continuously connecting at $c^{ab}=2\gamma B$. For $0<c^{ab}<2\gamma B$, in this regime of $c^a$ and $c^b$, the ground state is $|N_a,N_b,n,n\rangle$, where $n\equiv Int(\frac{\gamma B}{c^{ab}}-\frac{1}{2})$ satisfies $|N_a-N_b|\leq n\leq N_a+N_b$. For $N_a=N_b$, it is continuously connected with $|N,N,0,0\rangle$ for $c^{ab}\geq2\gamma B$ in the same ranges of $c^a$ and $c^b$. It is discontinuous with $|N_a,N_a\rangle_a|N_b,N_b\rangle_b$ for $c^{ab}=0$ in the same ranges of $c^a$ and $c^b$, as in the case without a magnetic field. This is a first order quantum phase transition except $n=N_a+N_b$.

Moreover, a magnetic field causes discontinuities of ground states between $c^{ab}>0$ and $c^{ab}=0$ in the first quadrant of $c^a-c^b$ plane. These discontinuities do not exist in absence of a magnetic field. As $c^{ab}\to0$ but remains positive, a magnetic field causes the division of the first quadrant into four regimes with continuous connecting ground states, as shown in FIG. 5, while for $c^{ab}=0$ there are nine regimes with continuous connecting ground states, as shown in FIG. 1. The boundaries of the ground states in these two cases do not match, leading to discontinuities between $c^{ab}>0$ and $c^{ab}=0$. These are usually first order quantum phase transitions except in some special cases.

$c^a=c^b=c^{ab}>0$ is extremely interesting place, where continuous quantum phase transitions take place no matter whether there is a magnetic field and no matter what is the actual value.

In terms of bosonic degrees of freedom, the general expression and its composite structure of $|S_a,S_b,S,S\rangle$ have been discussed previously [31, 32]. It will be very appealing to study the different physical consequences and the experimental probes of the crossovers and the discontinuities or quantum phase transitions of the ground states, and the effects of interspecies entanglement.

## Acknowledgments

This work was supported by the National Science Foundation of China (Grant No. 11074048) and the Ministry of Science and Technology of China (Grant No. 2009CB929204).

Note added: after this paper had been initially submitted to Phys. Rev. A on September 15 2010, there appeared a paper treating the subject in a mean field approach [34].

## Appendix A: $S_a^m$, $S_b^m$ and $S^m$ for $c^{ab}<0$, $B>0$

In this appendix, we find out $S_a^m$,$S_b^m$ and $S^m$, in which $E$ is minimal, in the case of $c^{ab}<0$ and $B>0$. In the discussions, $E$ always represent the energy as low as can be determined in the regime under discussion, i.e. the meaning of $E$ keeps updating.

With $c^{ab}<0$, $E$ is minimal when $S=S_a+S_b$. Hence the ground state with $S_z=S$ is always disentangled. Now

$$
E=\frac{c^a}{2}S_a(S_a+1)+\frac{c^b}{2}S_b(S_b+1)+c^{ab}S_aS_b-\gamma B(S_a+S_b). \tag{A1}
$$

Thus

$$
\frac{\partial E}{\partial S_a}=c^aS_a+c^{ab}S_b+\frac{c^a}{2}-\gamma B, \tag{A2}
$$

$$
\frac{\partial E}{\partial S_b}=c^bS_b+c^{ab}S_a+\frac{c^b}{2}-\gamma B. \tag{A3}
$$

We consider three subcases in the following.

### 1. $c^a\leq0$, $c^b\leq0$

In this subcase, $\frac{\partial E}{\partial S_a}<0$, $\frac{\partial E}{\partial S_b}<0$, hence $S_a^m=N_a$, $S_b^m=N_b$,$S^m=N_a+N_b$.

### 2. $c^a\leq0$, $c^b>0$

In this subcase, $\frac{\partial E}{\partial S_a}<0$, hence $S_a^m=N_a$,

$$
E(N_a,S_b)=\frac{c^b}{2}S_b(S_b+1)+c^{ab}N_aS_b-\gamma BS_b+const. \tag{A4}
$$

We represent all the values of $S_a$ and $S_b$ as points $(S_a,S_b)$ within the rectangular defined by $0\leq S_a\leq N_a$ and $0\leq S_b\leq N_b$ on $S_a$-$S_b$ plane (FIG. 6). $\frac{\partial E}{\partial S_b}=0$ defines a stationary line. The points above this line satisfy $\frac{\partial E}{\partial S_b}>0$, while the points below the line satisfy $\frac{\partial E}{\partial S_b}<0$. One can see three possibilities.

#### a. $0<c^b\leq\frac{2\gamma B-2N_ac^{ab}}{2N_b+1}$

The stationary line, depicted as the dashed line in FIG. 6, crosses with the line $S_b=N_b$. Hence all points with $S_a=N_a$ satisfy $\frac{\partial E}{\partial S_b}\leq0$. Consequently $S_a^m=N_a$, $S_b^m=N_b$, $S^m=N_a+N_b$. Note that this regime so defined can be combined with case A 1, with the same result.

![](./images/813338292027129856_4.jpg)

FIG. 6: All possible values of $(S_a, S_b)$ are within the rectangular $0 \leq S_a \leq N_a$ and $0 \leq S_b \leq N_b$. $\frac{\partial E}{\partial S_b}=0$ is represented as the dashed line in case $c^a \leq 0$ and $0 < c^b \leq \frac{2\gamma B-2N_a c^{ab}}{2N_b+1}$, and is represented as the solid line in case $c^a \leq 0$ and $\frac{2\gamma B-2N_a c^{ab}}{2N_b+1} \leq c^b \leq 2\gamma B-2N_a c^{ab}$.

$$b.\quad \frac{2\gamma B-2N_a c^{ab}}{2N_b+1} \leq c^b \leq 2\gamma B-2N_a c^{ab}$$

The stationary line, depicted as the solid line in FIG. 6, crosses with the line $S_a = N_a$. The crossing point gives the minimal energy. Hence $S_a^m = N_a$, $S_b^m = n_1$, with

$$n_1' \equiv Int\left[\frac{\gamma B + N_a|c^{ab}}{c^b} - \frac{1}{2}\right], \tag{A5}$$

where $Int(x)$ represents the integer closest to $x$ and in the legitimate range of $S_b$, i.e. now $0 \leq Int(x) \leq N_b$. $S^m = N_a + n_1$.

$$c.\quad c^b \geq 2\gamma B-2N_a c^{ab}$$

All points $(S_a, S_b)$ in the rectangular satisfy $\frac{\partial E}{\partial S_b} > 0$. Therefore $S_b^m = 0$, $S_a^m = S^m = N_a$.

$$3.\quad c^a > 0,\ c^b \leq 0$$

One simply exchanges the subscripts or superscripts $a$ and $b$ in the preceding subcase. Thus there are also three possibilities.

$$a.\quad 0 < c^a \leq \frac{2\gamma B-2N_b c^{ab}}{2N_a+1}$$

$S_a^m = N_a$, $S_b^m = N_b$, $S^m = N_a + N_b$. This regime can be combined with case A 1, without the same result.

$$b.\quad \frac{2\gamma B-2N_b c^{ab}}{2N_a+1} \leq c^a \leq 2\gamma B-2N_b c^{ab}.$$

$S_a^m = n_{b2}$, with

$$n_2' \equiv Int\left[\frac{\gamma B + N_b|c^{ab}|}{c^a} - \frac{1}{2}\right], \tag{A6}$$

now $0 \leq Int(x) \leq N_a$, $S_b^m = N_b$, $S^m = n_2 + N_b$.

$$c.\quad c^a \geq 2\gamma B-2N_b c^{ab}$$

$S_a^m = 0$, $S_b^m = S^m = N_b$.

![](./images/813338292027129856_5.jpg)

FIG. 7: For $0 < c^{ab} \leq 2\gamma B$ and $N_a = N_b = N$, the whole region of $(S_a, S_b)$, which satisfy $0 \leq S_a \leq N$ and $0 \leq S_b \leq N$, can be divided into four regions. (I) $S_b - S_a \geq S_0 \geq 0$, (III) $|S_b - S_a| \leq S_0 \leq S_b + S_a$, and the rest regions of (II) and (III). The dashed line represents $\frac{\partial E}{\partial S_b}=0$ in the case $c^a \geq c^b > c^{ab}$ and $c^b < 2\gamma B$. The solid line represents $\frac{\partial E}{\partial S_b}=0$ in the case $c^a > c^{ab} > c^b$ and $c^a c^b > (c^{ab})^2$.

## Appendix B: $S_a^m$, $S_b^m$ and $S^m$ for $0 < c^{ab} \leq 2\gamma B$, $c^a \geq c^b > c^{ab}$, $N_a = N_b = N$

Define

$$
S_0 \equiv \frac{\gamma B}{c^{ab}} - \frac{1}{2}, \tag{B1}
$$

which is the value of $S$ on which $S$-dependent part of $E$ is minimal if there were no constraint on $S$.

With $0 < c^{ab} \leq 2\gamma B$, it can be found that the whole region of $(S_a, S_b)$ can be divided into four regions, as shown in FIG. 7.

In region I, $S_b - S_a \geq S_0 \geq 0$, hence $E$ is minimal when $S = S_b - S_a$, with

$$
E = \frac{c^a}{2}S_a(S_a + 1) + \frac{c^b}{2}S_b(S_b + 1) - c^{ab}S_aS_b - c^{ab}S_a - \gamma B(S_b - S_a), \tag{B2}
$$

for which it is found that $\frac{\partial E}{\partial S_b} > 0$. Thus in region I, $E$ reaches its minimum at $S_b = S_a + S_0$. It is then easy to note that the minimum of $E$ in this region rests on $S_a = 0$, $S_b = S_0$.

Similarly, it can be shown that in region II the minimum of $E$ rests on $S_b = 0$, $S_a = S_0$. Since both $(0, S_0)$ and $(S_0, 0)$ also belong to region III, the minimum of $E$ in the whole rectangular must be in regions III and IV.

In region III, $|S_b - S_a| \leq S_0 \leq S_b + S_a$, hence $S$ can reach $S_0$, hence

$$
E = \frac{c^a - c^{ab}}{2}S_a(S_a + 1) + \frac{c^b - c^{ab}}{2}S_b(S_b + 1) + \frac{c^{ab}}{2}S_0(S_0 + 1) - \gamma BS_0, \tag{B3}
$$

for which $\frac{\partial E}{\partial S_a} > 0$, $\frac{\partial E}{\partial S_b} = \frac{c^b - c^{ab}}{2}(2S_b + 1) > 0$. Thus the minimum of $E$ in region III must rest on the border between III and IV, defined by $S_a + S_b = S_0$.

To conclude the above discussion, the minimum $E$ must locate in region IV, where $S_a + S_b \leq S_0$, hence the minimum of $E$ lies on $S = S_a + S_b$,

$$
E = \frac{c^a}{2}S_a(S_a + 1) + \frac{c^b}{2}S_b(S_b + 1) + c^{ab}S_aS_b - \gamma B(S_a + S_b). \tag{B4}
$$

One obtains

$$
\frac{\partial E}{\partial S_a} = c^a S_a + c^{ab}S_b + \frac{c^a}{2} - \gamma B, \tag{B5}
$$

$$
\frac{\partial E}{\partial S_{b}}=c^{b} S_{b}+c^{a b} S_{a}+\frac{c^{b}}{2}-\gamma B,
\tag{B6}
$$

according to which one needs to consider two subcases.

### 1. $c^{b} \geq 2 \gamma B$

In this parameter regime, $\frac{\partial E}{\partial S_{a}} \geq 0$, $\frac{\partial E}{\partial S_{b}} \geq 0$. Therefore $E$ is minimal when $S_{a}^{m}=S_{b}^{m}=S^{m}=0$.

### 2. $c^{b}<2 \gamma B$

In this parameter regime, $\frac{\partial E}{\partial S_{b}}=0$ defines a stationary line, shown as the dashed line in FIG. 7. Consequently, the minima of $E$ in different parts of region IV are

$$
E= \begin{cases}\frac{c^{a} c^{b}-\left(c^{a b}\right)^{2}}{2 c^{b}} S_{a}^{2}+\left[\frac{c^{a}-c^{a b}}{2}-\frac{c^{b}-c^{a b}}{c^{b}} \gamma B\right] S_{a}-\frac{c^{b}}{8}-\frac{\gamma^{2} B^{2}}{2 c^{b}}, & \text { if } \quad 0 \leq S_{a}<\frac{\gamma B}{c^{a b}}-\frac{c^{b}}{2 c^{a b}}, \\ \frac{c^{a}}{2} S_{a}\left(S_{a}+1\right)-\gamma B S_{a}, & \text { if } \quad \frac{\gamma B}{c^{a b}}-\frac{c^{b}}{2 c^{a b}} \leq S_{a} \leq S_{0},\end{cases}
\tag{B7}
$$

For $S_{a} \geq \frac{\gamma B}{c^{a b}}-\frac{c^{b}}{2 c^{a b}}$, it is found that $\frac{\partial E}{\partial S_{a}}>0$, hence $E$ reaches its minimum at $\left(\frac{\gamma B}{c^{a b}}-\frac{c^{b}}{2 c^{a b}}, 0\right)$, i.e. the point bordering the other part of region IV.

Therefore, the minimum of $E$ in the whole rectangular must locate on the dashed line in sector IV, on which $E$ is given by (B7). Then there are two possibilities.

### a. $c^{b}<2 \gamma B \leq \frac{c^{a}-c^{a b}}{c^{b}-c^{a b}} c^{b}$

We have $S_{a}^{m}=0, S_{b}^{m}=S^{m}=\frac{\gamma B}{c^{b}}-\frac{1}{2}$.

### b. $2 \gamma B>\frac{c^{a}-c^{a b}}{c^{b}-c^{a b}} c^{b}$

One finds that

$$
S_{a}^{m}=\operatorname{Int}\left[\frac{\gamma B\left(c^{b}-c^{a b}\right)-c^{b}\left(c^{a}-c^{a b}\right) / 2)}{c^{a} c^{b}-\left(c^{a b}\right)^{2}}\right],
\tag{B8}
$$

$$
S_{b}^{m}=\frac{\gamma B-c^{a b} S_{a}}{c^{b}}-\frac{1}{2},
\tag{B9}
$$

$$
S^{m}=S_{a}^{m}+S_{b}^{m}.
\tag{B10}
$$
(B11)

## Appendix C: $S_{a}^{m}, S_{b}^{m}$ and $S^{m}$ for $0<c^{a b} \leq 2 \gamma B, c^{a}>c^{a b}>c^{b}, c^{a} c^{b}>\left(c^{a b}\right)^{2}, N_{a}=N_{b}=N$

Again, we use FIG. 7. It can be shown that in region IV, $\frac{\partial E}{\partial S_{b}}<0$, thus the minimum of $E$ in this region lies on the border line with region III, i.e. $S_{a}+S_{b}=S_{0}$. It can be shown that the minimum of $E$ in region II lies on the border line $S_{a}-S_{b}=S_{0}$ with region III. Therefore we need only to consider regions I and III.

In region III, as shown in last section, $S^{m}=S_{0}$, and $E$ is given in Eq. (B4). But now that $c^{b} \leq c^{a b} \leq c^{a}$, we have $\frac{\partial E}{\partial S_{a}}>0$ and $\frac{\partial E}{\partial S_{b}}<0$. Consequently the minimum of $E$ lies in the border line $S_{b}-S_{a}=S_{0}$.

Therefore, we conclude that $E$ takes its global minimum in region I, where, as discussed in last section, $S^{m}=S_{b}-S_{a}$, $E$ is as given in Eq. (B2), for which

$$
\frac{\partial E}{\partial S_{b}}=c^{b} S_{b}-c^{a b} S_{a}+\frac{c^{b}}{2}-\gamma B.
\tag{C1}
$$

As shown in FIG. 7, $\frac{\partial E}{\partial S_{b}}=0$ defines a stationary line which crosses with $S_{b}=N$ at $\left(\frac{c^{b} N+c^{b} / 2-\gamma B}{c^{a b}}, N\right)$. The minima of $E$ are found to be:

$$
E=
\begin{cases}
\frac{c^a c^b-(c^{ab})^2}{2c^b}S_a^2+\left[\frac{c^a-c^{ab}}{2}-\frac{c^{ab}-c^b}{c^b}\gamma B\right]S_a+\left(\frac{3\gamma B}{2}+\frac{c^b}{4}\right)\left(\frac{\gamma B}{c^b}-\frac{1}{2}\right), & \text{if}\ \ 0\leq S_a<\frac{c^b N+c^b/2-\gamma B}{c^{ab}}, \\
\frac{c^a}{2}S_a(S_a+1)-c^{ab}(N+1)S_a+\gamma B S_a+\frac{c^b}{2}N(N+1)-\gamma B N, & \text{if}\ \ \frac{c^b N+c^b/2-\gamma B}{c^{ab}}\leq S_a\leq N-S_0.
\end{cases} \tag{C2}
$$

In the second interval $\frac{c^b N+c^b/2-\gamma B}{c^{ab}}\leq S_a\leq N-S_0$,

$$
\begin{aligned}
\frac{\partial E}{\partial S_a} &= c^a S_a - c^{ab}(N+1) + \gamma B + \frac{c^a}{2} \\
&\geq \frac{c^a c^b-(c^{ab})^2}{c^{ab}}N+\frac{c^a}{2}\left(\frac{c^b}{c^{ab}}+1\right) \\
&\quad -c^{ab}-\gamma B\left(\frac{c^a}{c^{ab}}-1\right),
\end{aligned} \tag{C3}
$$

which is positive if $N>N^*$, where

$$
N^*\equiv\frac{\gamma B(c^a-c^{ab})+(c^{ab})^2-c^{ab}c^a-\frac{c^a c^b}{2}}{c^a c^b-(c^{ab})^2}. \tag{C4}
$$

Then the minimum of $E$ must locate on the stationary line $c^b S_b - c^{ab} S_a + \frac{c^b}{2} - \gamma B=0$, with $0\leq S_a<\frac{c^b N+c^b/2-\gamma B}{c^{ab}}$.
One can see two possibilities.

$$\text{1.}\ \ 2\gamma B\leq\frac{c^a-c^{ab}}{c^{ab}-c^b}c^b$$

In this case, $\frac{c^a-c^{ab}}{2}-\frac{c^{ab}-c^b}{c^b}\gamma B\geq0$. Thus we have $S_a^m=0$, $S_b^m=S^m=Int\left[\frac{\gamma B}{c^b}-\frac{1}{2}\right]$.

$$\text{2.}\ \ 2\gamma B>\frac{c^a-c^{ab}}{c^{ab}-c^b}c^b$$

Then

$$
S_a^m=Int\left[\frac{\gamma B(c^{ab}-c^b)-c^b(c^a-c^{ab})/2}{c^a c^b-(c^{ab})^2}\right], \tag{C5}
$$

$$
S_b^m=Int\left[\frac{\gamma B+c^{ab}S_a^m}{c^b}-\frac{1}{2}\right], \tag{C6}
$$

$$
S^m=S_b^m-S_a^m. \tag{C7}
$$

## Appendix D: $S_a^m$, $S_b^m$ and $S^m$ for $0<c^{ab}\leq2\gamma B$, $c^b\geq c^a>c^{ab}$, $N_a=N_b=N$

By exchanging the labels $a$ and $b$ in Appendix B, one obtains the following results.

$$\text{1.}\ \ c^a\geq2\gamma B$$

$$S_a^m=S_b^m=S^m=0.$$

$$\text{2.}\ \ c^a<2\gamma B$$

$$\text{a.}\ \ c^a<2\gamma B\leq\frac{c^b-c^{ab}}{c^a-c^{ab}}c^a$$

We have $S_b^m=0$, $S_a^m=S^m=\frac{\gamma B}{c^a}-\frac{1}{2}$.

$$\text { b. } 2 \gamma B>\frac{c^{b}-c^{a b}}{c^{a}-c^{a b}} c^{a}$$

$$
S_{b}^{m}=\operatorname{Int}\left[\frac{\gamma B\left(c^{a}-c^{a b}\right)-c^{a}\left(c^{b}-c^{a b}\right) / 2)}{c^{a} c^{b}-\left(c^{a b}\right)^{2}}\right], \tag{D1}
$$

$$
S_{a}^{m}=\frac{\gamma B-c^{a b} S_{b}}{c^{a}}-\frac{1}{2}, \tag{D2}
$$

$$
S^{m}=S_{a}^{m}+S_{b}^{m}. \tag{D3}
$$

---

### Appendix E: $S_a^m$, $S_b^m$ and $S^m$ for $0 < c^{ab} \leq 2\gamma B$, $c^b > c^{ab} > c^a$, $c^a c^b > (c^{ab})^2$, $N_a=N_b$

By exchanging the labels $a$ and $b$ in Appendix C, one obtains the following results.

$$\text{1. }2\gamma B \leq \frac{c^{b}-c^{a b}}{c^{a b}-c^{a}} c^{a}$$

$$S_{b}^{m}=0, S_{a}^{m}=S^{m}=\operatorname{Int}[\frac{\gamma B}{c^{a}}-\frac{1}{2}].$$

$$\text{2. }2\gamma B>\frac{c^{b}-c^{a b}}{c^{a b}-c^{a}} c^{a}$$

$$
S_{b}^{m}=\operatorname{Int}[\frac{\gamma B\left(c^{a b}-c^{a}\right)-c^{a}\left(c^{b}-c^{a b}\right) / 2)}{c^{a} c^{b}-\left(c^{a b}\right)^{2}}], \tag{E1}
$$

$$
S_{a}^{m}=\operatorname{Int}[\frac{\gamma B+c^{a b} S_{b}^{m}}{c^{a}}-\frac{1}{2}], \tag{E2}
$$

$$
S^{m}=S_{b}^{m}-S_{a}^{m}. \tag{E3}
$$

---

[1] T.-L. Ho, Phys. Rev. Lett. 81, 742 (1998); T. Ohmi and K. Machida, J. Phys. Soc. Jpn. 67, 1822 (1998).
[2] C. K. Law, H. Pu, and N. P. Bigelow, Phys. Rev. Lett. 81, 5257 (1998).
[3] M. Koashi and M. Ueda, Phy. Rev. Lett. 84, 1066 (2000).
[4] T. L. Ho and S. K. Yip, Phy. Rev. Lett. 84, 4031 (2000).
[5] T. L. Ho and L. Yin, Phy. Rev. Lett. 84, 2302 (2000).
[6] F. Zhou, Phys. Rev. Lett. 87, 080401 (2001); E. Demler and F. Zhou, Phys. Rev. Lett. 88, 163001 (2002); F. Zhou, Int. J. Mod. Phys. B 17, 2643 (2003); F. Zhou, Ann. Phys. 308, 692 (2003).
[7] M. C. V. Ciobanu et al., Phy. Rev. Lett. 61, 033607 (2000); Koashi and M. Ueda, Phy. Rev. A 65, 063602 (2000).
[8] A. B. Kuklov and B. V. Svistunov, Phy. Rev. Lett. 89, 170403 (2002); S. Ashhab and C. Lobo, Phys. Rev. A 66, 013609 (2002); S. Ashhab and A. J. Leggett, Phys. Rev. A 68, 063612 (2003).
[9] K. Yang, arXiv:0907.4739.
[10] C. J. Pethick and H. Smith, Bose-Einstein condensation in dilute gases (Cambridge University Press, Cambridge, 2002).
[11] J. Stenger et al., Nature 396, 345 (1998); H.-J. Miesner et al., Phy. Rev. Lett. 82, 2228 (1999); D. M. Stamper-Kurn et al., Phy. Rev. Lett. 83, 661 (1999); A. Gölitz et al., Phy. Rev. Lett. 90, 090401 (2003); H. Schmaljohann et al., Phy. Rev. Lett. 92, 040402 (2004); M. S. Chang et al., Phy. Rev. Lett. 92, 140403 (2004); T. Kuwamoto et al., Phy. Rev. A 69, 063604 (2004); M. S. Chang et al., Nature Phys. 1, 111 (2005); L. E. Sadler et al., Nature 443, 312 (2006).
[12] C. J. Myatt, et al., Phy. Rev. Lett. 78, 586 (1997); D. S. Hall et al., Phy. Rev. Lett. 81, 1539 (1998); D. S. Hall et al., Phy. Rev. Lett. 81, 1543 (1998).
[13] A. Dalgarno and M. R. H. Rudge, Proc. Roy. Soc. London Series A 286, 519 (1965).
[14] S. B. Weiss, M. Bhattacharya and N. P. Bigelow, Phys. Rev. A 68, 042708 (2003); erratum: 69, 049903 (2004).
[15] A. Pashov et al., Phys. Rev. A 72, 062505 (2005).
[16] A. L. Zanelatto et al., J. Chem. Phys. 123, 014311 (2005).

[17] G. Ferrari *et al.*, Phys. Rev. Lett. **89**, 053202 (2002).

[18] A. Simoni *et al.*, Phys. Rev. Lett. **90**, 163202 (2003).

[19] S. Inouye *et al.*, Phys. Rev. Lett. **93**, 183201 (2004).

[20] M. Gacesa, P. Pellegrini and R. Côté, Phys. Rev. A **78**, 010701 (R) (2008).

[21] M. Mudrich *et al.*, Phys. Rev. A **70**, 062712 (2004).

[22] C. Chin, R. Grimm, P. Julienne and E. Tiesinga, Rev. Mod. Phys. **82**, 1225 (2010).

[23] Z. Li *et al.*, Phys. Rev. A **78**, 022710 (2008).

[24] C. Marzok *et al.*, Phys. Rev. A **79**, 012717 (R) (2009).

[25] B. Deh *et al.*, Phys. Rev. A **82**, 020701 (R) (2010).

[26] G. Modugno *et al.*, Phy. Rev. Lett. **89**, 190404 (2002); G. Thalhammer *et al.*, Phy. Rev. Lett. **100**, 210402 (2008); S. B.
Papp, J. M. Pino and C. E. Wieman, Phy. Rev. Lett. **97**, 180404 (2006); S. B. Papp, J. M. Pino and C. E. Wieman, Phy.
Rev. Lett. **101**, 040402 (2008).

[27] Y. Shi, Int. J. Mod. Phys. B **15**, 3007 (2001).

[28] Y. Shi and Q. Niu, Phy. Rev. Lett. **96**, 140401 (2006).

[29] Y. Shi, EPL **86**, 60008 (2009).

[30] Y. Shi, Phys. Rev. A **82**, 013637 (2010).

[31] Y. Shi, e-print arXiv:0912.2209 (2009), Phys. Rev. A **82**, 023603(2010).

[32] Y. Shi and L. Ge, Phys. Rev. A **83**, 013616 (2010).

[33] M. Luo, Z. Li and C. Bao, Phys. Rev. A **75**, 043609 (2007); M. Luo, C. Bao and Z. Li, J. Phys. B: At. Mol. Opt. Phys **41**,
245301 (2008).

[34] Z. F. Xu, J. W. Mei, R. Lü and L. You, Phys. Rev. A **82**, 053626 (2010).