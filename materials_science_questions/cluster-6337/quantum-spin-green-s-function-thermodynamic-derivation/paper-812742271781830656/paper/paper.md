# Application of spin-wave theory to the ground state of $XY$ quantum Hamiltonians

G. Gomez-Santos and J. D. Joannopoulos

Department of Physics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139
(Received 4 June 1987)

Spin-wave theory is successfully applied to study the ground state of the quantum $XY$ Hamiltonian. It is found that a judicious choice of the quantized spin axis removes difficulties of previous applications. Results for the simplest one-, two-, and three-dimensional lattices are shown to compare favorably with either exact or other approximate calculations.

## I. INTRODUCTION

Spin models with continuous symmetry have been the subject of much attention over the years. Among them, the quantum $XY$ model is considered to describe physical systems such as quantum lattice fluids and some magnetic insulators. $^{1}$ As a theoretical model, much of the current interest has been devoted to the understanding of the critical behavior, particularly in two dimensions where exact results forbid the existence of long-range magnetization. $^{2}$ This paper deals with the very basic problem of investigating the ground state of the spin-$\frac{1}{2}$ $XY$ Hamiltonian in the simplest one-, two-, and three-dimensional lattices.

Despite the simplicity of the Hamiltonian, the exact ground state is only known in the one-dimensional case. $^{3}$ In higher dimensionality, the ground-state properties have been studied by extrapolation from exact finite lattice calculations, $^{4,5}$ using variational methods $^{6}$ or from perturbation theory. $^{7}$

In our work we use simple linear spin-wave theory. Spin-wave analysis has proved to be quite satisfactory in studying the ground-state properties of the similar Heisenberg antiferromagnet as explained in the early works of Anderson $^{8}$ and Kubo. $^{9}$ Although Villain $^{10}$ has studied the $XY$ model in a special spin-wave representation, to our knowledge, the only attempts to apply spin-wave theory in the traditional Holstein-Primakoff $^{11}$ representation have obtained results that are far from satisfactory, and definitely below the level of quality reached by similar analysis for the Heisenberg antiferromagnet. $^{12}$ This has led to the conclusion that the corresponding spin-wave study is fortuitously good in the Heisenberg antiferromagnet and, at most, of dubious applicability in the related $XY$ Hamiltonian.

It is the purpose of this paper to show that a proper spin-wave treatment can yield results for the ground state of $XY$ models with, at least, the same quality as the corresponding study for the Heisenberg model. The basis of our treatment consists of a trivial but judicious choice of the classical state upon which spin vibrations are supposed to be a small perturbation. To this end, we choose as the quantization axis one that lies on the plane where the coupling takes place and not, as has been done before, $^{12}$ the direction normal to that plane. Having specified this choice, the spin-wave treatment follows the standard procedure and the results are parallel to those obtained in the Heisenberg case. We believe that this simple treatment places spin-wave theory of antiferromagnets in a better perspective removing its apparent limitations to the Heisenberg model.

The paper is organized as follows. In Sec. II the formalism of our spin-wave treatment is introduced. In Sec. III, the results for the simplest one-, two-, and three-dimensional lattices are presented and compared with exact results and other approximations. The validity of the approximation along with the typical divergences of this theory are discussed in Sec. IV. Finally, the work is summarized in Sec. V.

## II. SPIN-WAVE THEORY

The basis of our application of spin-wave analysis relies on a proper choice of the classical state upon which the spin waves represent small vibrations. To this end we take the $XZ$ rather than the $XY$ Hamiltonian and choose the $z$ direction as the quantization axis. The Hamiltonian can be written as follows:

$$
\begin{aligned}
H= & -J \sum_{\langle i, j\rangle}\left(S_{i}^{x} S_{j}^{x}+S_{i}^{z} S_{j}^{z}\right) \\
= & -J \sum_{\langle i, j\rangle} S_{i}^{z} S_{j}^{z}-\frac{J}{4} \sum_{\langle i, j\rangle}\left(S_{i}^{+} S_{j}^{-}+S_{i}^{-} S_{j}^{+}\right. \\
& \left.+S_{i}^{+} S_{j}^{+}+S_{i}^{-} S_{j}^{-}\right), \quad(1)
\end{aligned}
$$

where $S_{i}^{\alpha}$ is the $\alpha$ component of the spin-$\frac{1}{2}$ operator on site $i$ and $S_{i}^{\pm}$ are the corresponding raising and lowering operators ($z$ axis). The sum is over nearest-neighbor pairs. In this paper we restrict our attention to bipartite lattices, so that the ferromagnetic and antiferromagnetic cases are related to each other by a simple rotation. This allows us to take the positive sign of the coupling constant $J$ without loss of generality.

The advantage of this choice of axis is evident from


(1), where the first term on the right-hand side is the Is- ing Hamiltonian in the $Z$ direction whose ground state (all spins pointing up) is to be perturbed by the presence of oscillations coming from the rest of the Hamiltonian.

$$
\begin{aligned}
H=-J \sum_{\langle i, j\rangle}\left(n_{i}-\frac{1}{2}\right)\left(n_{j}-\frac{1}{2}\right)-\frac{J}{4} \sum_{\langle i, j\rangle} & {\left[a_{i}^{\dagger} a_{j}^{\dagger}\left(\sqrt{1-n_{i}} \sqrt{1-n_{j}}\right)+\left(\sqrt{1-n_{i}} \sqrt{1-n_{j}}\right) a_{i} a_{j}\right.} \\
& \left.+a_{i}^{\dagger}\left(\sqrt{1-n_{i}} \sqrt{1-n_{j}}\right) a_{j}+a_{j}^{\dagger}\left(\sqrt{1-n_{i}} \sqrt{1-n_{j}}\right) a_{i}\right],
\end{aligned}
$$

with $n_{i}=a_{i}^{\dagger} a_{i}$ and $[a_{i}, a_{j}^{\dagger}]=\delta_{i j},[a_{i}^{\dagger}, a_{j}^{\dagger}]=[a_{i}, a_{j}]=0$.

No approximation is made here and, although the space of the new boson operators include unphysical states with occupation numbers greater than 1, the phys- ical $(n_{i}=0,1)$ and unphysical $(n_{i}>1)$ states are not mixed by the Hamiltonian.

In order to solve $H$ we make the usual linear approxi mations by keeping terms quadratic in the operators. The linearized Hamiltonian $H_{L}$ given by

$$
\begin{aligned}
H_{L}= & -J \sum_{\langle i, j\rangle}\left[\frac{1}{4}-\frac{1}{2}\left(n_{i}+n_{j}\right)\right] \\
& -\frac{J}{4} \sum_{\langle i, j\rangle}\left(a^{\dagger}{ }_{i} a^{\dagger}{ }_{j}+a_{i}^{\dagger} a_{j}+a_{i} a_{j}^{\dagger}+a_{i} a_{j}\right).
\end{aligned}
$$

The approximations introduced in the linearization are of two types. First, we neglect the interaction be- tween spin waves (higher order terms in the operators) and second, the separability of both physical and un- physical states no longer holds. This last point implies the presence of unphysical contributions to the ground state of $H_{L}$. Clearly, the criterion for the validity of $H_{L}$ is related to the occupation number $n_{i}$. If $\langle n_{i}\rangle$ is well below 1, it is reasonable to neglect the interaction be- tween spin waves and, furthermore, the main contribu- tion to the eigenstates comes from the physical subspace $(n=0,1)$.

It is important to stress that a small value of $\langle n_{i}\rangle$ is favored (although not guaranteed) by the presence of the z component of the interaction as the unperturbed Ham- iltonian. This important aspect is lacking if we take the usual $X Y$ version of the Hamiltonian and choose the $z$ axis as the quantization direction $^{12}$ in the linearized Hamiltonian.

The diagonalization of $H_{L}$ is accomplished in the standard way: $^{12}$ introducing Bloch-type operators $a_{k}$ (ak†) and using the Bogoliubov transformation. This gives

$$
\begin{aligned}
a_{\mathbf{k}} & =\left(\cosh u_{\mathbf{k}}\right) b_{\mathbf{k}}+\left(\sinh u_{\mathbf{k}}\right) b_{-\mathbf{k}}^{\dagger}, \\
a^{\dagger}{ }_{\mathbf{k}} & =\left(\cosh u_{\mathbf{k}}\right) b^{\dagger}{ }_{\mathbf{k}}+\left(\sinh u_{\mathbf{k}}\right) b_{-\mathbf{k}},
\end{aligned}
$$

and

$$
\begin{aligned}
H_{L}= & -J \frac{N z}{8}+\sum_{k} \omega(\mathbf{k}) b^{\dagger}{ }_{\mathbf{k}} b_{\mathbf{k}} \\
& +\frac{z}{2} \sum_{k} \sinh u_{\mathbf{k}}\left(\sinh u_{\mathbf{k}}-\cosh u_{\mathbf{k}}\right),
\end{aligned}
$$

where $N$ represents the number of lattice sites, $z$ is the coordination of the lattice, the sum in $\mathbf{k}$ space runs over the entire Brillouin zone, and

$$
\omega(\mathbf{k})=z / 2\left(\cosh u_{\mathbf{k}}-\sinh u_{\mathbf{k}}\right)^{2}.
$$

The application of spin-wave (SW) theory to $H$ is straightforward. Introducing boson creation and annihi- lation operators by means of the Holstein-Primakoff transformation, $^{11}$ we obtain

The auxiliary quantity $u_{\mathbf{k}}=u_{-\mathbf{k}}=u^{*}{ }_{\mathbf{k}}$ is fixed by the following equation:

$$
\tanh \left(2 u_{\mathbf{k}}\right)=\frac{S(\mathbf{k}) / 2 z}{1-S(\mathbf{k}) / 2 z},
$$

where $S(\mathbf{k})$ is the structure factor of the lattice

$$
S(\mathbf{k})=\sum_{i=1}^{z} \cos \left(\mathbf{k} \cdot \boldsymbol{\delta}_{i}\right),
$$

$\boldsymbol{\delta}_{i}$ being the lattice vector of the nearest neighbor labeled $i$.

The ground-state properties $H_{L}$ can now be obtained in the usual way. The ground-state energy $E$, local occu- pation number $n$, magnetization $M$, and out-of-plane nearest-neighbor correlation are found to be

$$
\frac{E}{N J}=-\frac{z}{8}+\frac{z}{4 N} \sum_{\mathbf{k}}\left\{[1-S(\mathbf{k}) / z]^{1 / 2}-1\right\},
$$

$$
n \equiv\left\langle n_{i}\right\rangle=\left\langle a_{i}^{\dagger} a_{i}\right\rangle=\frac{1}{N} \sum_{\mathbf{k}}\left(\sinh u_{\mathbf{k}}\right)^{2},
$$

$$
\frac{\langle M\rangle}{N}=\frac{1}{N} \sum_{i}\left\langle S_{i}^{z}\right\rangle=n-\frac{1}{2},
$$

$$
\left\langle S_{0}^{y} S_{1}^{y}\right\rangle=\frac{1}{4 z N} \sum_{\mathbf{k}} S(\mathbf{k}) \sqrt{1-S(\mathbf{k}) / z}.
$$

Before analyzing these results in terms of 1D, 2D, and3D lattices, it is instructive to note the following points:

(i) In the expression of the energy (9a), the first term represents the energy of the classical state while the second corresponds to the contribution arising from spin oscillations. The first part accounts for a fairly large part of the total energy, especially in higher dimensions, explaining why our choice of axis is important in getting good results.

(ii) The dispersion relation $\omega(\mathbf{k})$ is linear with $\mathbf{k}$ for long wavelengths. This linear behavior is found in the exactly known low-lying excitations of both Heisenberg and $X Y$ models in one dimension and is believed to be a common feature of antiferromagnetic models. This be- havior is not found if the quantization axis is taken per-pendicular to the interaction plane. $^{12}$

(iii) The spin-wave ground state, by construction, ex- hibits a total magnetization along the quantization axis, while the exact ground state is isotropic in the interac-

tion plane. $^{13}$ Thus, it is important that the different symmetry of the exact and approximate ground states be taken into account when comparing properties such as the long-range order. This point is discussed further in the next section.

## III. RESULTS
In this section we present the results of our spin-wave analysis to the linear chain, square lattice, and simple- cubic lattice. The relevant data are summarized in Tables I-III, where comparisons with either exact re- sults or extrapolations from finite lattices are made. The results obtained with the conventional choice of quanti- zation axis $^{12}$ are also included for illustrative purposes.

### A. Linear chain
As shown in Table I, the energy obtained with spin- wave theory is in good agreement (within 6 percent) with the known exact result $1 / \pi$ .
The out-of-plane nearest-neighbor correlation $\langle s_{0}^{y} s_{1}^{y}\rangle$  is also reasonably close to the exact value. $^{3}$ In one di mension it is straightforward to go one step further and analyze the decay of the out-of-plane correlation with the separation between spins. In our spin-wave treat- ment, this correlation is given by
$$\left\langle S_{0}^{y} S_{m}^{y}\right\rangle \propto \frac{1}{N} \sum_{k} e^{i \mathbf{k} \cdot \mathbf{m}}\left(\cosh u_{\mathbf{k}}-\sinh u_{\mathbf{k}}\right)^{2} \propto \frac{1}{m^{2}}.\qquad(10)$$
This has the same asymptotic behavior as obtained fromexact calculations. $^{3}$
The occupation per site $\langle n_{i}\rangle$ is divergent in one di mension, a fact consistent with the lack of long-range or- der exhibited by the exact solution. $^{3}$ Although this divergence seems to imply the breakdown of the spin- wave approximation, it turns out that the agreement ob- tained in the previously mentioned quantities is not for- tuitous. This situation is similar to that encountered in the spin-wave treatment of the Heisbenberg antifer- romagnet and is considered more carefully in Sec. IV.

### B. Square lattice
The mean occupation per site $\langle n_{i}\rangle$ , shown in TableII, is consistent with the approximations involved in thespin-wave Hamiltonian. In particular, its value of 0.06 guarantees that the projection of the ground state on the physical subspace $(n_{i}=0,1)$ of an arbitrary lattice site accounts for, at least, 97 percent of the norm of the ground state. The ground-state energy and nearest- neighbor out-of-plane correlation compare very well with the best numerical estimates from finite lattices.
TABLE I. Comparison of the present results for the ground-state energy, local occupation number, nearest- neighbor out-of-plane correlation and long-range order with exact calculations (Ref. 3) and conventional spin-wave treat- ments (Ref. 12) for the one-dimensional lattice.
</content> TABLE I. Comparison of the present results for the ground-state energy, local occupation number, nearest- neighbor out-of-plane correlation and long-range order with exact calculations (Ref. 3) and conventional spin-wave treat- ments (Ref. 12) for the one-dimensional lattice.<content/>
TABLE II. Comparison of the present results for the ground-state energy, local occupation number, nearest- neighbor out-of-plane correlation, and long-range order with the best numerical estimates from finite lattice calculations(Ref. 5) and conventional spin-wave treatments (Ref. 12) for the square lattice.
</content> TABLE II. Comparison of the present results for the ground-state energy, local occupation number, nearest- neighbor out-of-plane correlation, and long-range order with the best numerical estimates from finite lattice calculations(Ref. 5) and conventional spin-wave treatments (Ref. 12) for the square lattice.<content/>
The ground state of this system is believed to show long-range order $^{5}$ and so does the spin-wave result. As mentioned in Sec. II, the numerical comparison of the amount of long-range order in spin-wave theory with ex- act diagonalizations in finite systems deserves some ex- planation. The exact ground state is nondegenerate and shows the full symmetry of the Hamiltonian. $^{13}$ This im plies the absence of total magnetization while the spin- wave ground state shows its long-range order as a mag- netization along the z direction. If we choose the square of the magnetization as the order parameter, then
$$\frac{1}{N^{2}}\left\langle M_{z}^{2}\right\rangle=\frac{1}{N^{2}}\left\langle M_{x}^{2}\right\rangle, \quad \frac{1}{N^{2}}\left\langle M_{y}^{2}\right\rangle=0\qquad(11a)$$
 for the exact ground state and
$$\frac{1}{N^{2}}\left\langle M_{z}^{2}\right\rangle \neq 0 \quad, \frac{1}{N^{2}}\left\langle M_{x}^{2}\right\rangle=\frac{1}{N^{2}}\left\langle M_{y}^{2}\right\rangle=0\qquad(11b)$$
 for the spin wave ground state.
If we compare $< M_{z}^{2}> / N^{2}$ in the spin-wave theory with the corresponding value of finite-size diagonalizations, the spin-wave result is systematically greater than that of the exact analysis. This behavior is also encountered in the spin-wave theory of the Heisenberg antiferromagnet and in other approaches in which the starting state
TABLE III. As in Table II for the simple-cubic lattice. In this case the numerical estimates for the out-of-plane nearest- neighbor correlation and long-range order are taken from the variational approach of Ref. 6.
</content> TABLE III. As in Table II for the simple-cubic lattice. In this case the numerical estimates for the out-of-plane nearest- neighbor correlation and long-range order are taken from the variational approach of Ref. 6.<content/>

displays a broken symmetry. This systematic disagreement in the long-range order as opposed to the good results obtained for other quantities has caused concern when comparing approximations with finite-size extrapolations. $^{12}$

The position we adopt here is that the different symmetry of the spin-wave and exact ground states makes meaningless the comparison of a given component of the square of the magnetization. Instead, we believe that it is the length of the total magnetization, irrespective of orientation, that should be taken as the proper order parameter. This means that we should compare $\langle M_{z}^{2}\rangle /$ $N^{2}$ in the spin-wave approximation with $(\langle M_{x}^{2}\rangle$ $+\langle M_{z}^{2}\rangle) / N^{2}$ from the exact calculations.

The value of the square of the magnetization is shown in Table II along with the results obtained in finite-size calculations. The agreement is excellent and comparable to that obtained with the energy and out-of-plane correlations.

### C. Simple cubic lattice
The mean occupation per site is quite small $(\langle n_{i}\rangle=0.022)$ and thus the spin-wave analysis is again internally consistent. The values of the energy, out-of-plane correlation, and square magnetization, as shown in Table III, compare well with information obtained from exact diagonalization.

## IV. DIVERGENCES AND THE VALIDITY OF SPIN-WAVE THEORY
The most severe divergence of the theory is that appearing in the linear chain for the mean occupation per site. As discussed earlier, such a divergence would make any results from spin-wave analysis meaningless. Yet the values of the energy and out-of-plane correlations compare fairly well with the exact solution. The conventional view would be that this is all completely fortuitous. An inspection of the nature of the divergence reveals that it is related to the behavior of the spin-wave approximation at small $\mathbf{k}$ (long wavelengths). As argued by Berezinskii et al., $^{14}$ the inadequacy in the description over long distances does not necessarily invalidate the spin-wave results for local properties such as the energy, giving some justification to the spin-wave analysis even in this extreme one-dimensional case.

Although the two- and three-dimensional lattices do not suffer the extreme divergences of the linear chain, there can be divergences in other quantities such as the fluctuation of the magnetization. Again, this fact resembles what happens in the Heisenberg antiferromagnet. Now, we study the nature of this divergence. The fluctuations in the magnetization are related to the corresponding fluctuations in the total occupation number
$$
N_{T}=\sum_{i} n_{i}, \quad(12)
$$
where $i$ runs over lattice sites. The fluctuations can be written as follows:
$$
\left\langle N_{T}^{2}\right\rangle-\left\langle N_{T}\right\rangle^{2}=N \sum_{j=0}^{N}\left\langle n_{0} n_{j}\right\rangle-N^{2}\langle n\rangle^{2}. \quad(13)
$$

The ground-state correlation $\langle n_{0} n_{j}\rangle$ is easily shown to be
$$
\begin{aligned}
\left\langle n_{0} n_{j}\right\rangle= & \langle n\rangle^{2}+\langle n\rangle \delta_{0 j}+\left\lceil\frac{1}{N} \sum_{\mathbf{k}} e^{i \mathbf{k} \cdot \mathbf{r}_{j}} \sinh ^{2} u_{\mathbf{k}}\right\rceil^{2} \\
& +\left\lceil\frac{1}{N} \sum_{\mathbf{k}} e^{i \mathbf{k} \cdot \mathbf{r}_{j}} \sinh u_{\mathbf{k}} \cosh u_{\mathbf{k}}\right\rceil^{2}.
\end{aligned}
$$

Taking into account (7) and performing the lattice sum, (13) can be expressed as follows:
$$
\left\langle N_{T}^{2}\right\rangle-\left\langle N_{T}\right\rangle^{2}=N\langle n\rangle+N\left\lceil\frac{1}{N} \sum_{\mathbf{k}} \sinh ^{4}\left(u_{\mathbf{k}}\right)+\frac{1}{N} \sum_{\mathbf{k}} \sinh ^{2}\left(u_{\mathbf{k}}\right) \cosh ^{2}\left(u_{\mathbf{k}}\right)\right\rceil
$$

where the value with $\mathbf{k}=0$ has been removed. The integrals of (15) contain terms that behave like $1 /|\mathbf{k}|^{2}$ near the center of the Brillouin zone and, so, they are divergent in one and two dimensions. We can obtain the $N$ dependence of these quantities taking into account the discrete nature of the allowed reciprocal-space vectors.
$$
\mathbf{k}= \begin{cases}\frac{\pi}{N} m, \quad m= \pm 1, \ldots, \pm N, & 1 \mathrm{D} \\ \frac{\pi}{N^{1 / 2}}(n, m), \quad n, m= \pm 1, \ldots, \pm N^{1 / 2}, & 2 \mathrm{D} \\ \frac{\pi}{N^{1 / 3}}(n, m, l), \quad n, m, l= \pm 1, \ldots, \pm N^{1 / 3}), & 3 \mathrm{D}.\end{cases}
$$

With these expressions we obtain the following $N$ dependence:
$$
\left\langle N_{T}^{2}\right\rangle-\left\langle N_{T}\right\rangle^{2}-N\langle n\rangle \propto \begin{cases}N^{2}, & 1 \mathrm{D} \\ N \ln N, & 2 \mathrm{D} \\ N, & 3 \mathrm{D}\end{cases}.
$$

We observe that in three dimensions the fluctuations are normal (linear in $N$ ). The behavior in one dimension does not add any new information since $\langle n\rangle$ is already divergent. More interesting is the result in two dimensions in which the fluctuations, although abnormally large, do not prevent the existence of a well-defined magnetization in the macroscopic limit
$$
\frac{\left\langle N_{T}^{2}\right\rangle-\left\langle N_{T}\right\rangle^{2}}{\left\langle N_{T}\right\rangle^{2}} \propto \frac{N \ln N}{N^{2}} \underset{N \rightarrow \infty}{\rightarrow} 0. \quad(18)
$$

Again, this behavior of the fluctuation resembles that

obtained in the spin-wave ground state of the Heisenberg antiferromagnet.

## V. SUMMARY
In this paper we have studied the ground-state properties of the quantum $XY$ Hamiltonian in bipartite lattices by means of the linear spin-wave theory. It has been shown that the usual spin-wave theory, despite claims to the contrary, can give a rather accurate picture of the ground state of this model. The basis of our treatment relies on a judicious choice of the "classical state" upon which the spin oscillations represent a small perturbation. Once this is done, the treatment follows the standard procedure.

Results have been presented for the energy correlations and long-range order parameter in the simplest one-, two-, and three-dimensional lattices. Comparison of our results with either exact values or available extrapolations from finite lattice calculations have proved to be satisfactory even in the most unfavorable one-dimensional case. We have analyzed the validity of the approximation and studied the nature of the divergences.

The main conclusion to be drawn from this work is that once a proper quantization direction has been chosen, the application and results of spin-wave theory in the usual Holstein-Primakoff representation follow in a manner quite similar to that of the antiferromagnetic Heisenberg model. With this, we hope to have clarified that the quality of the spin-wave theory as applied to the Heisenberg Hamiltonian is not fortuitously limited to that model but is a rather general feature shared by the closely related $XY$ Hamiltonian. This reinforces the view that, despite its limitations, spin-wave theory still stands as one of the simplest but physically meaningful approaches to study ground-state properties of antiferromagnetic systems.

## ACKNOWLEDGMENTS
This work was supported in part by U.S. Office of Naval Research Grant No. N00014-85-K-0158. One of us (G.G.-S.) would like to thank the Fulbright-MEC program for additional support.

---

¹D. D. Betts, in *Phase Transitions and Critical Phenomena*, edited by C. Domb and M. S. Green (Academic, New York, 1974), Vol. 3.
²N. D. Mermin and H. Wagner, Phys. Rev. Lett. **17**, 1133 (1966).
³E. Lieb, T. Schultz, and D. Mattis, Ann. Phys. (N.Y.) **16**, 407 (1961).
⁴J. Oitmaa and D. D. Betts, Phys. Lett. **68A**, 450 (1978).
⁵J. Oitmaa and D. D. Betts, Can. J. Phys. **56**, 897 (1978).
⁶M. Suzuki and S. Miyashita, Can. J. Phys. **56**, 902 (1978).
⁷R. B. Pearson, Phys. Rev. B **16**, 1109 (1977).
⁸P. W. Anderson, Phys. Rev. **86**, 694 (1952).
⁹R. Kubo, Phys. Rev. **87**, 568 (1952).
¹⁰J. Villain, J. Phys. (Paris) **35**, 27 (1974).
¹¹T. Holstein and H. Primakoff, Phys. Rev. **58**, 1908 (1940).
¹²See, e.g., D. C. Mattis, in *The Theory of Magnetism I* (Springer Verlag, Berlin, 1982).
¹³D. Mattis, Phys. Rev. Lett. **42**, 1503 (1979).
¹⁴V. L. Berezinskii and A. Ya-Blank, Zh. Eksp. Teor. Fiz. **64**, 725 (1973) [Sov. Phys. JETP **37**, 369 (1973)].