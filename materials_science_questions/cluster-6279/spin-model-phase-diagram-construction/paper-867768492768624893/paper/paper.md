# A new effective field theory for spin-$S$ ($S \leq 1$) dilute Ising ferromagnets

Ümit Akıncı, Yusuf Yüksel, and Hamza Polat*
Department of Physics, Dokuz Eylül University, TR-35160 Izmir, Turkey
(Dated: November 4, 2018)

Site diluted spin-1/2 Ising and spin-1 Blume Capel (BC) models in the presence of transverse field interactions are examined by introducing an effective-field approximation that takes into account the multi-site correlations in the cluster of a considered lattice with an improved configurational averaging technique. The critical concentration below which the transition temperature reduces to zero is determined for both models, and the estimated values are compared with those obtained by the other methods in the literature. It is found that diluting the lattice sites by non magnetic atoms may cause some drastic changes on some of the characteristic features of the model. Particular attention has been paid on the global phase diagrams of a spin-1 BC model, and it has also been shown that the conditions for the occurrence of a second order reentrance in the system is rather complicated, since the existence or extinction of reentrance is rather sensitive to the competing effects between $D/J$, $\Omega/J$ and $c$.

## Contents

I. Introduction
1

II. Formulation
2
A. Site diluted spin-$\frac{1}{2}$ system
2
B. Site diluted spin-1 Blume-Capel model with transverse field interactions
5

III. Results and discussion
7
A. Site diluted spin-1/2 model
7
B. Site diluted spin-1 model
8

IV. Concluding remarks
12

Acknowledgements
14

A. Derivation of complete set of linear equations for spin-1/2 Ising Model
15

B. Derivation of complete set of linear equations for spin-1 BC model
16

References
18

# I. INTRODUCTION

Investigation of disorder effects on the critical phenomena has a long history and there have been a great many of theoretical studies focused on disordered magnetic materials with quenched randomness where the random variables of a magnetic system such as random fields [1, 2] or random bonds [3, 4] may not change its value over time. On the other hand, site diluted ferromagnets constitute another example of magnetic systems with quenched disorder such as a compound $\text{A}_x\text{B}_{1-x}\text{C}$ where magnetic A atoms in a pure magnet AC are replaced by non-magnetic B impurities. Formerly, Sato et al. [5] have shown that in a dilute lattice a Curie or a Néel temperature does not appear until a finite concentration of magnetic atoms is obtained if the atomic distribution is random. They have also found that this concentration depends on the coordination number of the lattice. After this seminal work of Sato et al. [5], much attention has been paid to site dilution problem and the situation has been handled by a wide variety of techniques such as Bethe-Peierls-Weiss (BPW) method [6], renormalization group (RG) technique [7-10], correlated effective field theory (CEFT) [11-13], effective field theory (EFT) based on decoupling (or Zernike [14]) approximation

---
*Electronic address: hamza.polat@deu.edu.tr; Phone: +90 2324128672; fax: +90 2324534188.

(DA) [15-33], an integral representation method [34], Monte Carlo (MC) simulation technique [35-38], Bogoliubov inequality approach [39], Bethe-Peierls approximation (BPA) [40], finite cluster approximation (FCA) which gives results identical to those obtained by EFT for a one spin cluster [41-44], third order Matsudaira approximation [45], EFT with probability distribution technique [46-52] and cluster variational method (CVM) [53]. Among the theoretical works mentioned above, some of the authors extended the standard dilution problem to more complicated versions by taking into account the transverse field interactions [54], random fields and random bonds, as well as bilinear and biquadratic exchange couplings and crystal field interactions for the systems with $S > 1/2$.

Mean field theory (MFT) of site dilution problem predicts that the system always has a finite critical temperature and stays in a ferromagnetic state at lower temperatures, except that $c = 0$ where $c$ denotes the magnetic atom concentration. Therefore, it is not capable of locating a critical site concentration at which the transition temperature reduces to zero. The reason is due to the fact that MFT neglects single-site and multi-spin correlations. On the other hand, EFT based on DA accounts all the single site correlations, but it also neglects multi-spin correlations between different sites. Hence, EFT provides results that are superior to those obtained within the traditional MFT. Furthermore, CEFT which is an extension of EFT partially takes into account the effects of multi-spin correlations and improves the results of conventional EFT in many cases. Based on the physical aspects of the problem, whether in EFT or CEFT formalism, evaluation of configurational averages emerging in definition of spin identities plays a critical role. However, as mentioned by Tucker [23], the conventional configurational averaging technique applied in Refs. [11, 12, 16, 22, 27, 31, 32] is based on a procedure that decouples the site occupation variable from the thermal average of spin variables, even when both quantities referred to the same site while in Refs. [19, 23-26, 29, 44], the authors used an improved configurational averaging method in which only the correlations between quantities pertaining to different sites are neglected (decoupled). However, it is possible to improve the accuracy of these methods by including multi-site, as well as single site correlations.

In this paper, we describe a new type of EFT method for investigating the thermal and magnetic properties of a site diluted Ising model on 2D lattices. Recently, we have successfully applied our method to random bond [55] and random field [56] problems on 2D and 3D lattices with various coordination numbers. As we emphasized in these previous works, an advantage of the approximation method proposed by this method is that no decoupling procedure is used for the higher-order correlation functions. Therefore, it is expected that the accuracy of the results obtained within the present work may improve those of the works based on conventional and improved DA. For this purpose, we organized the paper as follows: In Sec. II we briefly present the formulations. The results and discussions are presented in Sec. III, and finally Sec. IV contains our conclusions.

## II. FORMULATION

In this section, we give the formulation of the present study for site diluted spin-1/2 Ising and spin-1 Blume Capel (BC) models on 2D lattices. As our model, we consider $N$ identical spins arranged on a 2D regular lattice. Then we define a cluster on the lattice which consists of a central spin labeled $S_0$ and $q$ perimeter spins being the nearest neighbors of the central spin. The cluster consists of $(q+1)$ spins being independent from the value of $S$. The nearest-neighbor spins are in an effective field produced by the outer spins, which can be determined by the condition that the thermal average of the central spin is equal to that of its nearest-neighbor spins. In the following subsections, we give a detailed discussion of how the present method can be formulated for spin-1/2 Ising and spin-1 BC models with quenched site dilution.

### A. Site diluted spin-$\frac{1}{2}$ system

As a site diluted spin-1/2 Ising model, we consider the following Hamiltonian

$$
H=-J \sum_{<i,j>} c_i c_j S_i^z S_j^z, \tag{1}
$$

where the summation is over the nearest-neighbor pairs of spins and the operator $S_i^z$ takes the values $S_i^z = \pm 1$. We assume that the lattice sites are randomly diluted and $c_i$ denotes a site occupation variable which equals to 1 if the site is occupied by a magnetic atom or to 0 if it is empty.

According to the Callen identity [57] for the spin-1/2 Ising system, the thermal average of the identity $c_i S_i^z$ at the

site $i$ is given by

$$
c_{i}\left\langle\left\{f_{i}\right\} S_{i}^{z}\right\rangle=c_{i}\left\langle\left\{f_{i}\right\} \tanh \left[\beta c_{i}\left(J \sum_{j} c_{j} S_{j}\right)\right]\right\rangle,
\tag{2}
$$

where $\beta=1 / k_{B} T$, $j$ expresses the nearest-neighbor sites of the central spin and $\{f_{i}\}$ can be any function of the Ising variables as long as it is not a function of the site. Applying the differential operator technique [58, 59] in Eq. (2) and using the relation

$$
\exp \left(\alpha c_{i}\right)=c_{i} \exp (\alpha)+1-c_{i},
\tag{3}
$$

with the fact that $c_{i}^{n}=c_{i}$, we get

$$
c_{i}\left\langle\left\{f_{i}\right\} S_{i}^{z}\right\rangle=c_{i}\left\langle\left\{f_{i}\right\} \prod_{j=1}^{q} \exp \left(J c_{j} S_{j}^{z} \nabla\right)\right\rangle\left.\tanh (\beta x)\right|_{x=0}.
\tag{4}
$$

By putting Eq. (3) into Eq. (4) we obtain

$$
c_{i}\left\langle\left\{f_{i}\right\} S_{i}^{z}\right\rangle=c_{i}\left\langle\left\{f_{i}\right\} \prod_{j=1}^{q}\left\{c_{j} \cosh (J \nabla)+c_{j} S_{j}^{z} \sinh (J \nabla)+1-c_{j}\right\}\right\rangle\left.\tanh (\beta x)\right|_{x=0},
\tag{5}
$$

where $\nabla$ is a differential operator, $q$ is the coordination number of the lattice, and $\langle...\rangle$ represents the thermal average. Eq. (5) is valid only for a given specific magnetic atom configuration. Hence, if we consider configurational averages then we may rewrite Eq. (5) as

$$
\left\langle c_{i}\left\langle\left\{f_{i}\right\} S_{i}^{z}\right\rangle\right\rangle_{r}=\left\langle c_{i}\left\langle\left\{f_{i}\right\} \prod_{j=1}^{q}\left\{c_{j} \cosh (J \nabla)+c_{j} S_{j}^{z} \sinh (J \nabla)+1-c_{j}\right\}\right\rangle\right\rangle_{r}\left.\tanh (\beta x)\right|_{x=0},
\tag{6}
$$

where $\langle...\rangle_{r}$ represents random configurational averages. When the right-hand side of Eq. (6) is expanded, the multi-site correlation functions appear. The simplest approximation, and one of the most frequently adopted is to decouple these correlations which is called decoupling approximation (DA). In conventional manner, eliminating the term $c_{i}$ from both sides of Eq. (5) then performing the configurational average with $\{f_{i}\}=1$ leads to the following equation,

$$
\left\langle\left\langle S_{i}^{z}\right\rangle\right\rangle_{r}=\left\langle\left\langle\prod_{j=1}^{q}\left\{c_{j} \cosh (J \nabla)+c_{j} S_{j}^{z} \sinh (J \nabla)+1-c_{j}\right\}\right\rangle\right\rangle_{r}\left.\tanh (\beta x)\right|_{x=0}.
\tag{7}
$$

In conventional DA one expands the right-hand side of Eq. (7) then decouples the multi-site correlations according to

$$
\left\langle\left\langle c_{i}... c_{j} c_{k} S_{k}^{z} c_{l} S_{l}^{z}... c_{m} S_{m}^{z}\right\rangle\right\rangle_{r} \cong\left\langle c_{i}\right\rangle_{r}...\left\langle c_{j}\right\rangle_{r}\left\langle c_{k}\right\rangle_{r}\left\langle\left\langle S_{k}^{z}\right\rangle\right\rangle_{r}\left\langle c_{l}\right\rangle_{r}\left\langle\left\langle S_{l}^{z}\right\rangle\right\rangle_{r}...\left\langle c_{m}\right\rangle_{r}\left\langle\left\langle S_{m}^{z}\right\rangle\right\rangle_{r}
\tag{8}
$$

with
$$
\left\langle c_{\alpha}\right\rangle_{r}=c \quad \text { and } \quad\left\langle\left\langle S_{\alpha}^{z}\right\rangle\right\rangle_{r}=m \quad \alpha=i,... j, k, l,..., m.
$$

However, this approximation decouples the site occupation variable from the thermal and configurational averages of spin variable, even when both quantities referred to the same site.

On the other hand, an improved version of decoupling approximation deals with the quantity $\langle c_{i}\langle S_{i}^{z}\rangle\rangle_{r}$. In other words, in an improved decoupling procedure, one expands the right-hand side of Eq. (6) instead of Eq. (7) and decouples the multi-site correlations according to

$$
\left\langle\left\langle c_{i}... c_{j} c_{k} S_{k}^{z} c_{l} S_{l}^{z}... c_{m} S_{m}^{z}\right\rangle\right\rangle_{r} \cong\left\langle c_{i}\right\rangle_{r}...\left\langle c_{j}\right\rangle_{r}\left\langle c_{k}\left\langle S_{k}^{z}\right\rangle\right\rangle_{r}\left\langle c_{l}\left\langle S_{l}^{z}\right\rangle\right\rangle_{r}...\left\langle c_{m}\left\langle S_{m}^{z}\right\rangle\right\rangle_{r}
\tag{9}
$$

with
$$
\left\langle c_{i}\right\rangle_{r}=\left\langle c_{j}\right\rangle_{r}=c \quad \text { and } \quad\left\langle c_{\alpha}\left\langle S_{\alpha}^{z}\right\rangle\right\rangle_{r}=m \quad \alpha=k, l,..., m
$$

In this approximation, only the correlations between quantities pertaining to different sites are neglected. A detailed discussion about these configurational averaging techniques is also given by Tucker [23]. Whether conventional method or improved one, the papers which utilize these approximations claim that if we try to treat exactly all the spin-spin correlations emerging on the right-hand side of Eqs. (6) and (7), the problem becomes mathematically intractable. In order to overcome this point, recently we proposed an approximation that takes into account the correlations between different sites in the cluster of a considered lattice [55, 56]. Namely, an advantage of the approximation method proposed by those studies is that no decoupling procedure is used for the higher-order correlation functions.

We state that hereafter, we will carry on the formulation of the dilute spin-1/2 system for a honeycomb lattice ($q=3$), however a brief explanation of the method for a square lattice ($q=4$) can be found in A. Now, if we expand the right-hand side of Eq. (6) for $q=3$ without using DA, we get some certain identities in the form

$$\langle\langle c_{i}... c_{j} c_{k} S_{k}^{z} c_{l} S_{l}^{z}... c_{m} S_{m}^{z}\rangle\rangle_{r}=\langle c_{i}... c_{j}\rangle_{r}\langle\langle c_{k} S_{k}^{z} c_{l} S_{l}^{z}... c_{m} S_{m}^{z}\rangle\rangle_{r}.\tag{10}$$

In Eq. (10), we use the fact that occupation number $c_{i}$ of a given site $i$ is independent from the thermal average, as long as the correlation function does not contain a spin variable $S_{i}^{z}$, and the site occupation numbers pertaining to different sites are assumed to be statistically independent from each other. Hence, we may rearrange Eq. (10) as

$$\langle\langle c_{i}... c_{j} c_{k} S_{k}^{z} c_{l} S_{l}^{z}... c_{m} S_{m}^{z}\rangle\rangle_{r}=\langle c_{i}\rangle_{r}...\langle c_{j}\rangle_{r}\langle\langle c_{k} S_{k}^{z} c_{l} S_{l}^{z}... c_{m} S_{m}^{z}\rangle\rangle_{r}.\tag{11}$$

where $\langle c_{i}\rangle_{r}=\langle c_{j}\rangle_{r}=c$. In the present formulation, it is clear that Eq. (11) improves EFT based on Eqs. (8) and (9) by taking into account the multi-site correlations. With the help of Eq. (11), and by expanding the right-hand side of Eq. (6) for the central site $c_{0} S_{0}^{z}$ with $\{f_{i}\}=1$ we have

$$m=\langle\langle c_{0} S_{0}\rangle\rangle_{r}=x_{1}=\left(3 c-6 c^{2}+3 c^{3}\right) x_{4} K_{1}+\left(6 c^{2}-6 c^{3}\right) x_{4} K_{2}+3 c^{3} x_{4} K_{3}+c x_{6} K_{4}.\tag{12}$$

where the terms $x_{i}$ in Eq. (12) are defined in A. In obtaining Eq. (12) we use the fact that $\tanh(\beta x)$ is an odd function. Hence, only the odd coefficients give non-zero contribution which can be given as follows:

$$\begin{aligned}
K_{1} & =\left.\sinh(J \nabla) \tanh(\beta x)\right|_{x=0}, \\
K_{2} & =\left.\cosh(J \nabla) \sinh(J \nabla) \tanh(\beta x)\right|_{x=0}, \\
K_{3} & =\left.\cosh^{2}(J \nabla) \sinh(J \nabla) \tanh(\beta x)\right|_{x=0}, \\
K_{4} & =\left.\sinh^{3}(J \nabla) \tanh(\beta x)\right|_{x=0}.
\end{aligned}\tag{13}$$

For comparison, if we apply the improved decoupling approximation given in Eq. (9) then Eq. (12) reduces to

$$m=\left(3 c-6 c^{2}+3 c^{3}\right) m K_{1}+\left(6 c^{2}-6 c^{3}\right) m K_{2}+3 c^{3} m K_{3}+c m^{3} K_{4},\tag{14}$$

which is identical to those obtained in Refs. [19, 23, 25]. Additionally, applying the conventional method (8) gives the following result

$$m=\left(3 c-6 c^{2}+3 c^{3}\right) m K_{1}+\left(6 c^{2}-6 c^{3}\right) m K_{2}+3 c^{3} m K_{3}+c^{3} m^{3} K_{4}.\tag{15}$$

It seems like it is fortuitous that although, the equations of states of approximations (8) and (9) are differ from each other in the last term, they give the same phase diagram in $(k_{B} T_{c} / J-c)$ plane. The reason comes from the fact that both approximations ignore the term $m^{3}$ in the limit $T \rightarrow T_{c}$. Hence, it should be emphasized that the importance and distinction of our method becomes evident by expansion of Eq. (6) without using any kind of DA.

The next step is to carry out the configurational and thermal averages of the perimeter site in the system, and it is found as

$$\langle\langle\left\{f_{\delta}\right\} c_{\delta} S_{\delta}\rangle\rangle_{r}=\langle c_{\delta}\left\langle\left\{f_{\delta}\right\}\left(c_{0} \cosh(J \nabla)+c_{0} S_{0} \sinh(J \nabla)+1-c_{0}\right)\right\rangle\rangle_{r} \tanh(\beta(x+\gamma)).\tag{16}$$

From Eq. (16) with $\delta=\{f_{\delta}\}=1$ we get the following identity

$$\langle\langle c_{1} S_{1}\rangle\rangle_{r}=x_{4}=\left(c-c^{2}\right) A_{1}+c^{2} A_{2}+c x_{1} A_{3}.\tag{17}$$

For the sake of simplicity, the superscript $z$ is omitted from the left- and right-hand sides of Eqs. (12) and (17). The coefficients in Eq. (17) are given as

$$\begin{aligned}
A_{1} & =\left.\tanh(\beta(x+\gamma))\right|_{x=0}, \\
A_{2} & =\left.\cosh(J \nabla) \tanh(\beta(x+\gamma))\right|_{x=0}, \\
A_{3} & =\left.\sinh(J \nabla) \tanh(\beta(x+\gamma))\right|_{x=0}.
\end{aligned}\tag{18}$$

The coefficients in Eqs. (13) and (18) can easily be calculated by applying a mathematical relation, $e^{\alpha \nabla} f(x)=f(x+\alpha)$.
In Eq. (18), $\gamma=(q-1) A$ is the effective field produced by the $(q-1)$ spins outside of the cluster, and $A$ is an unknown parameter to be determined self-consistently.

Eqs. (12) and (17) are the fundamental correlation functions of the system. On the other hand, for a honeycomb lattice, taking Eqs. (6) and (16) as basis, we derive a set of linear equations of the site correlation functions in the system. At this point, we assume that (i) the correlations depend only on the distance between the spins and (ii) the average values of a central site and its nearest-neighbor site (it is labeled as the perimeter site) are equal to each other with the fact that, in the matrix representations of spin operator $\hat{S}$, the spin-1/2 system has the property $(\hat{S})^{2}=1$.
Thus, the number of linear equations obtained for $q=3$ and $q=4$ reduces to six and eight, respectively, and the complete sets are given in A.

Finally, e.g. if Eq. (A2) for $q=3$ is written in the form of $6 \times 6$ matrix and solved in terms of the variables $x_{i}$
$(i=1,2, ...6)$ of the linear equations, all of the site correlation functions can be easily determined as functions of the temperature and Hamiltonian parameters. Since the thermal and configurational average of the central site is equal to that of its nearest-neighbor sites within the present method, the unknown parameter $A$ can be numerically determined by the relation

$$
x_{1}=x_{4}. \tag{19}
$$

By solving Eq. (19) numerically for a given fixed set of Hamiltonian parameters, we obtain the parameter $A$. Then we use the numerical values of $A$ to obtain the site correlation functions which can be found from Eq. (A2). Note that $A=0$ is always a root of Eq. (19) corresponding to the disordered state of the system whereas the nonzero root of $A$ in Eq. (19) corresponds to the long-range-ordered state of the system. Once the site correlation functions have been evaluated then we can give the numerical results for the thermal and magnetic properties of the system. Since the effective field $\gamma$ is very small in the vicinity of $k_{B} T_{c} / J$, we can obtain the critical temperature for the fixed set of Hamiltonian parameters by solving Eq. (19) in the limit of $\gamma \to 0$, and then we can construct the whole phase diagrams of the system.

## B. Site diluted spin-1 Blume-Capel model with transverse field interactions

Site diluted spin-1 Blume-Capel (BC) [60, 61] model with transverse field interaction is represented by the following Hamiltonian

$$
H=-J \sum_{<i, j>} c_{i} c_{j} S_{i}^{z} S_{j}^{z}-D \sum_{i} c_{i}\left(S_{i}^{z}\right)^{2}-\Omega \sum_{i} c_{i} S_{i}^{x}, \tag{20}
$$

where $S_{i}^{z}$ and $S_{i}^{x}$ denote the $z$ and $x$ components of the spin operator, respectively. The first summation in Eq. (20) is over the nearest-neighbor pairs of spins and the operator $S_{i}^{z}$ takes the values $S_{i}^{z}=0, \pm 1$. $J, D$ and $\Omega$ terms stand for the exchange interaction, single-ion anisotropy (i.e. crystal field) and transverse field, respectively.

By using the approximated spin correlation identities [62]

$$
c_{i}\left\langle\left\{f_{i}\right\} S_{i}^{z}\right\rangle=c_{i}\left\langle\left\{f_{i}\right\} \frac{\operatorname{Tr}_{i} S_{i}^{z} \exp \left(-\beta H_{i}\right)}{\operatorname{Tr}_{i} \exp \left(-\beta H_{i}\right)}\right\rangle, \tag{21}
$$

$$
c_{i}\left\langle\left\{f_{i}\right\}\left(S_{i}^{z}\right)^{2}\right\rangle=c_{i}\left\langle\left\{f_{i}\right\} \frac{\operatorname{Tr}_{i}\left(S_{i}^{z}\right)^{2} \exp \left(-\beta H_{i}\right)}{\operatorname{Tr}_{i} \exp \left(-\beta H_{i}\right)}\right\rangle, \tag{22}
$$

and following the same methodology of Sec. II A, we can obtain the general form of the site correlation functions for the central site as follows

$$
\left\langle c_{i}\left\langle\left\{f_{i}\right\} S_{i}^{z}\right\rangle\right\rangle_{r}=\left\langle c_{i}\left\langle\left\{f_{i}\right\} \prod_{j=1}^{q}\left[c_{j}\left(S_{j}^{z}\right)^{2} \cosh (J \nabla)+c_{j} S_{j}^{z} \sinh (J \nabla)+1-c_{j}\left(S_{j}^{z}\right)^{2}\right]\right\rangle\right\rangle_{r}\left.F(x)\right|_{x=0}, \tag{23}
$$

$$
\left\langle c_{i}\left\langle\left\{f_{i}\right\}\left(S_{i}^{z}\right)^{2}\right\rangle\right\rangle_{r}=\left\langle c_{i}\left\langle\left\{f_{i}\right\} \prod_{j=1}^{q}\left[c_{j}\left(S_{j}^{z}\right)^{2} \cosh (J \nabla)+c_{j} S_{j}^{z} \sinh (J \nabla)+1-c_{j}\left(S_{j}^{z}\right)^{2}\right]\right\rangle\right\rangle_{r}\left.G(x)\right|_{x=0}, \tag{24}
$$

where the functions $F(x)$ ad $G(x)$ can be found in Ref. [55]. By expanding the right hand side of Eqs. (23) and (24) according to Eq. (11) for $c_0S_0^z$ and $c_0(S_0^z)^2$, respectively with $\{f_i\}=1$ and taking only the nonzero terms we get magnetization and quadrupolar moment of the central site as follows

$$
m=\left\langle\left\langle c_{0} S_{0}\right\rangle\right\rangle_{r}=x_{1}=3 c x_{4} k_{1}+c x_{6} k_{3}+\left(-6 k_{1}+6 k_{2}\right) c x_{8}+\left(3 k_{1}-6 k_{2}+3 k_{4}\right) c x_{14},
\tag{25}
$$

$$
\begin{aligned}
q_{z}=\left\langle\left\langle c_{0} S_{0}^{2}\right\rangle\right\rangle_{r}=x_{16}= & c r_{0}+3 c x_{5} r_{2}+\left(-3 r_{0}+3 r_{1}\right) c x_{7}+\left(3 r_{0}-6 r_{1}+3 r_{3}\right) c x_{9} \\
& +\left(-3 r_{2}+3 r_{4}\right) c x_{13}+\left(-r_{0}+3 r_{1}-3 r_{3}+r_{5}\right) c x_{15},
\end{aligned}
\tag{26}
$$

where the coefficients in Eqs. (25) and (26) are given as follows

$$
\begin{aligned}
& k_{1}=\left.\sinh (J \nabla) F(x)\right|_{x=0}, \\
& k_{2}=\left.\cosh (J \nabla) \sinh (J \nabla) F(x)\right|_{x=0}, \\
& k_{3}=\left.\sinh ^{3}(J \nabla) F(x)\right|_{x=0}, \\
& k_{4}=\left.\cosh ^{2}(J \nabla) \sinh (J \nabla) F(x)\right|_{x=0},
\end{aligned}
\qquad
\begin{aligned}
& r_{0}=G(0), \\
& r_{1}=\left.\cosh (J \nabla) G(x)\right|_{x=0}, \\
& r_{2}=\left.\sinh ^{2}(J \nabla) G(x)\right|_{x=0}, \\
& r_{3}=\left.\cosh ^{2}(J \nabla) G(x)\right|_{x=0}, \\
& r_{4}=\left.\cosh (J \nabla) \sinh ^{2}(J \nabla) G(x)\right|_{x=0}, \\
& r_{5}=\left.\cosh ^{3}(J \nabla) G(x)\right|_{x=0}.
\end{aligned}
\tag{27}
$$

If we use improved decoupling approximation given in Eq. (9) then Eqs. (23) and (24) reduce to the following coupled equations

$$
\begin{aligned}
m & =\left.c\left[\cosh (J \nabla)+m \sinh (J \nabla)+1-q_{z}\right]^{3} F(x)\right|_{x=0}, \\
& =3 c m k_{1}+c m^{3} k_{3}+\left(-6 k_{1}+6 k_{2}\right) c m q_{z}+\left(3 k_{1}-6 k_{2}+3 k_{4}\right) c m q_{z}^{2},
\end{aligned}
\tag{28}
$$

$$
\begin{aligned}
q_{z} & =\left.c\left[q \cosh (J \nabla)+m \sinh (J \nabla)+1-q_{z}\right]^{3} G(x)\right|_{x=0}, \\
& =c r_{0}+3 c m^{2} r_{2}+\left(-3 r_{0}+3 r_{1}\right) c q_{z}+\left(3 r_{0}-6 r_{1}+3 r_{3}\right) c q_{z}^{2} \\
& \quad+\left(-3 r_{2}+3 r_{4}\right) c m^{2} q_{z}+\left(-r_{0}+3 r_{1}-3 r_{3}+r_{5}\right) c q_{z}^{3},
\end{aligned}
\tag{29}
$$

where $m=\left\langle\left\langle c_{i} S_{i}^{z}\right\rangle\right\rangle_{r}$ and $q_{z}=\left\langle\left\langle c_{i}\left(S_{i}^{z}\right)^{2}\right\rangle\right\rangle_{r}$. Eqs. (28) and (29) are nothing but just the results obtained in Refs.[23, 24, 26, 44] which exposes the superiority of the present method.

Now, we should evaluate the thermal and configurational averages of the perimeter site correlations within the present formalism. Thus, corresponding to Eqs. (23) and (24) we have

$$
\left\langle c_{\delta}\left\langle\left\{f_{\delta}\right\} S_{\delta}^{z}\right\rangle\right\rangle_{r}=\left\langle c_{\delta}\left\langle\left\{f_{\delta}\right\}\left[c_{0}\left(S_{0}^{z}\right)^{2} \cosh (J \nabla)+c_{0} S_{0}^{z} \sinh (J \nabla)+1-c_{0}\left(S_{0}^{z}\right)^{2}\right]\right\rangle\right\rangle_{r}\left.F(x+\gamma)\right|_{x=0},
\tag{30}
$$

$$
\left\langle c_{\delta}\left\langle\left\{f_{\delta}\right\}\left(S_{\delta}^{z}\right)^{2}\right\rangle\right\rangle_{r}=\left\langle c_{\delta}\left\langle\left\{f_{\delta}\right\}\left[c_{0}\left(S_{0}^{z}\right)^{2} \cosh (J \nabla)+c_{0} S_{0}^{z} \sinh (J \nabla)+1-c_{0}\left(S_{0}^{z}\right)^{2}\right]\right\rangle\right\rangle_{r}\left.G(x+\gamma)\right|_{x=0},
\tag{31}
$$

where $\gamma=(q-1) A$ represents the effective field produced by the $(q-1)$ spins outside of the cluster. From Eqs. (30) and (31) with $\delta=\left\{f_{\delta}\right\}=1$, we can get the perimeter site correlation functions as follows

$$
\left\langle\left\langle c_{1} S_{1}\right\rangle\right\rangle_{r}=x_{4}=a_{1} c+a_{2} c x_{1}+\left(a_{3}-a_{1}\right) c x_{16},
\tag{32}
$$

$$
\left\langle\left\langle c_{1} S_{1}^{2}\right\rangle\right\rangle_{r}=x_{7}=b_{1} c+b_{2} c x_{1}+\left(b_{3}-b_{1}\right) c x_{16},
\tag{33}
$$

where

$$
\begin{array}{ll}
a_{1}=F(\gamma), & b_{1}=G(\gamma), \\
a_{2}=\sinh (J \nabla) F(x+\gamma), & b_{2}=\sinh (J \nabla) G(x+\gamma), \\
a_{3}=\cosh (J \nabla) F(x+\gamma), & b_{3}=\cosh (J \nabla) G(x+\gamma).
\end{array}
\tag{34}
$$

The coefficients in Eqs. (27) and (34) can be calculated by using the relation $e^{\alpha \nabla} f(x)=f(x+\alpha)$.

For a dilute spin-1 BC model, using Eqs. (23), (24), (30) and (31) we derive a set of linear equations by considering that (i) the correlations depend only on the distance between the lattice sites, (ii) the average values of a central site and its nearest-neighbor site (it is labeled as the perimeter site) are equal to each other with the fact that, in the

matrix representations of spin operator $\hat{S}$, the spin-1 system has the properties $(S_{j}^{z})^{3}=S_{j}^{z}$ and $(S_{j}^{z})^{4}=(S_{j}^{z})^{2}$. Thus, the number of the set of linear equations obtained for the spin-1 Ising system with $q=3$ reduces to twenty one, and a detailed derivation and the complete set is given in B.

Since the thermal and configurational averages of the central site is equal to that of its nearest-neighbor sites within the present method then the unknown parameter $A$ in Eq. (34) can be numerically determined by the relation

$$
x_{1}=x_{4}. \tag{35}
$$

By solving Eq. (35) numerically at a given fixed set of Hamiltonian parameters we obtain the parameter $A$. Then we use the numerical values of $A$ to obtain the site correlation functions such as the longitudinal magnetization $\langle\langle c_{0} S_{0}\rangle\rangle_{r}$, longitudinal quadrupolar moment $\langle\langle c_{0} S_{0}^{2}\rangle\rangle_{r}$ and so on, which can be found from Eq. (B2). $A=0$ always satisfies Eq. (35) and gives paramagnetic solution. On the other hand, nonzero solutions of $A$ which satisfy Eq. (35) just correspond to ferromagnetic state solutions of the system. The critical temperature $k_{B} T_{c} / J$ can be found by solving Eq. (35) in the limit of $\gamma \to 0$. Depending on the Hamiltonian parameters, there may be two solutions [i.e.,two critical temperature values satisfy Eq. (35)] corresponding to the first (or second) and second-order phase-transition points, respectively. We determine the type of the transition by looking at the temperature dependence of magnetization for selected values of system parameters.

## III. RESULTS AND DISCUSSION

### A. Site diluted spin-1/2 model

In Fig. (1) we show the phase diagrams and magnetization, as well as specific heat curves for honeycomb $(q=3)$ and square $(q=4)$ lattices which can be obtained by solving Eqs. (A2) and (A4) numerically. In Fig. (1a) variation of magnetization curves are depicted as a function of temperature $k_{B} T / J$ with typical values of site concentration $c$. As expected, we see in Fig. (1a) that as the temperature increases starting from zero, the magnetization of the system decreases continuously, and it falls rapidly to zero at the critical temperature $k_{B} T_{c} / J$ for selected $c$ values. The number of interacting sites on the lattice decreases as $c$ decreases and hence, $k_{B} T_{c} / J$ value of the system and the saturation value of magnetization curves also decrease as $c$ decreases.

In Fig. (1b) we examine the effect of site concentration $c$ on the temperature dependence of specific heat of the system. We see that as the temperature increases starting from zero, then the specific heat curves exhibit a sharp peak at a second-order phase transition temperature which decreases with decreasing $c$. As $c$ approaches its critical value $c^{*}$ at which critical temperature reduces to zero then an additional broad cusp appears and below $c^{*}$ phase transition disappears. For $c>c^{*}$ the system forms an infinite cluster of lattice sites however, as $c$ gets closer to $c^{*}$ then isolated finite clusters appear and for $c<c^{*}$ the system cannot exhibit long range ferromagnetic order even at zero temperature which causes a broad cusp in specific heat vs temperature curves. These observations are qualitatively agree with those of Refs. [13, 15, 19, 42] and show the proper thermodynamic behavior over the whole range of temperatures, including the ground-state behavior $(C / N k_{B} \to 0$ as $k_{B} T / J \to 0)$ and the thermal stability condition $(C / N k_{B} \geq 0)$. Next, Fig. (1c) represents the variation of the saturation magnetization with site concentration. In this figure, we also compare our results (blue line) with those of EFT based on conventional DA (C-DA, black line) and improved DA (I-DA, red line) methods. It is clearly evident that site dilution lowers down the saturation magnetization. According to C-DA saturation magnetization of the system continuously decreases as $c$ decreases then falls rapidly to zero at $c^{*}$. On the other hand, I-DA predicts a linear decrease at high magnetic atom concentrations, but as $c$ decreases gradually then a monotonic decline is observed in the saturation magnetization value. On the other hand, according to our results we observe a linear decrement trend up to the vicinity of $c^{*}$ which originates as a result of considering the multi-site correlations. Finally, we represent the phase diagram of the system in $(k_{B} T_{c} / J-c)$ plane which separates the ferromagnetic and paramagnetic phases and we compare our results with those of the other methods in the literature. According to this figure, critical temperature $k_{B} T_{c} / J$ of system decreases gradually, and ferromagnetic region gets narrower as $c$ increases, and $k_{B} T_{c} / J$ value depresses to zero at $c=c^{*}$. Such a behavior is an expected fact in dilution problems. Numerical value of critical concentration $c^{*}$ for honeycomb $(q=3)$ and square $(q=4)$ lattices is given in Table I, and compared with the other works in the literature. It is well known that the series expansion (SE) method gives the best approximate values to the known exact results [66]. Therefore, we see in Table I that the present work improves the results of finite cluster approximation (OSCA and TSCA), as well as the other works based on EFT with DA. The reason is due to the fact that, in contrast to the previously published works mentioned above, there is no uncontrolled decoupling procedure used for the higher-order correlation functions within the present approximation.

![](./images/867768492768624893_1.jpg)

FIG. 1: Temperature dependence of (a) magnetization, (b) specific heat curves of dilute ferromagnetic system for honeycomb $(q=3)$ and square $(q=4)$ lattices with some selected values of site concentration $c$. (c) Ground state magnetizations as a function of temperature for $q=3$, and $q=4$. (d) Phase diagrams of the system in $(k_{B}T_{c}/J - c)$ plane obtained by MFT (dash-dotted), DA (dotted), and present work (solid).

<table>
<caption>TABLE I: Numerical values of critical site concentration $c^{*}$ for spin-1/2 system obtained within the present work for $q=3,4$ and comparison with various approximations in the literature: Average coordination number approximation $2/q$ and Bethe approximation $(q-1)^{-1}$ [5], RG [7, 8], CEFT [11], EFT [19, 20, 25, 50], OSCA [42, 44], TSCA [41, 44], CVM [53], MC [37], SE [63, 64].</caption>
<thead>
<tr>
<th>$q$</th>
<th>MFT</th>
<th>$2/q$</th>
<th>$(q-1)^{-1}$</th>
<th>RG</th>
<th>CEFT</th>
<th>EFT</th>
<th>OSCA</th>
<th>TSCA</th>
<th>CVM</th>
<th>MC</th>
<th>SE</th>
<th>Present Work</th>
</tr>
</thead>
<tbody>
<tr>
<td>3</td>
<td>0</td>
<td>0.667</td>
<td>0.5</td>
<td></td>
<td>0.711</td>
<td>0.5575</td>
<td>0.5575</td>
<td>0.5706</td>
<td>0.768</td>
<td></td>
<td>0.698</td>
<td>0.6727</td>
</tr>
<tr>
<td>4</td>
<td>0</td>
<td>0.5</td>
<td>0.333</td>
<td></td>
<td>0.602</td>
<td>0.558</td>
<td>0.4284</td>
<td>0.4284</td>
<td>0.4303</td>
<td>0.640</td>
<td>0.413</td>
<td>0.593</td>
<td>0.4594</td>
</tr>
</tbody>
</table>

## B. Site diluted spin-1 model

For a site diluted spin-1 BC model defined by Hamiltonian (20), we investigate the thermal and magnetic properties of the system by solving Eq. (B2) numerically with condition (35). At first, we shall examine the variation of the site percolation threshold $c^{*}$ with $D/J$ and $\Omega/J$. In Fig. (2a) we plot the dependence of the site percolation threshold surface with $5.0 < D/J < -1.0$ and $0.3 < \Omega/J < 2.5$. As we can see from Fig. (2a), the effect of the transverse field $\Omega/J$ on the percolation threshold value clearly depends on the value of the crystal field $D/J$ and vice versa. Namely, for the values of $\Omega/J > 0.565$ if we decrease the value of crystal field starting from $D/J=5.0$ then $c^{*}$ value increases

![](./images/867768492768624893_2.jpg)

FIG. 2: (a) Variation of critical site concentration of a diluted spin-1 BC model for $q=3$ with crystal field $D/J$ and transverse field $\Omega/J$. (b) Critical bond concentration of the same model projected on the same plane. (For interpretation of the references to color in these figure legends, the reader is referred to the web version of this article.)

and and reaches its maximum value. On the other hand, for $0.3 < \Omega/J \leq 0.565$ $c^*$ value increases or decreases depending on the value of $D/J$. Furthermore, for $\Omega/J \leq 1.56$ and sufficiently large positive $D/J$, $c^*$ value remains more or less constant and we obtain $c^*=0.6727$ which is the critical site concentration of spin-1/2 system for $q=3$. Besides, for $D/J=0$ and $\Omega/J=0$ we get $c^*=0.6211$ which is higher than the bond percolation threshold value of the same system obtained by the same method [55]. This value can be compared with the results obtained by the other works given in Table II. In Table II, two different critical concentrations obtained by EFT comes from the usage of exact or approximate Van der Waerden identity. Using the exact identity one obtains the result of OSCA. By comparing Table I and Table II we see that critical site concentration $c^*$ of a dilute system depends on the spin value $S$. However, according to the percolation theory [65, 66] $c^*$ only depends on the topology of the lattice and must be independent of $S$. In order to fix this problem, Refs. [27, 31, 32] suggested to include a positive crystal field $D/J$ but, it is clear in Fig. (2) that there is an exceptional situation (dark blue region in Fig. (2b)) due to the presence of $\Omega/J$. Therefore, we can say that topology deformation of the percolation threshold surface illustrated in Fig. (2) originates from a competition due to the presence of $D/J$ and $\Omega/J$ in the system. For completeness of the work, we also give the critical bond concentration surface of the same model obtained by the same methodology presented in this paper for $q=3$ [55]. By drawing inspiration from Figs. (2a) and (2b), we think that whether in a site or bond dilution problem, the mechanism underlying the complex topological behavior of the critical concentration completely originates from a collective effect of both $\Omega/J$ and $D/J$.

TABLE II: Site percolation threshold value $c^*$ for $D/J=0$ and $\Omega/J=0$ obtained by present work for spin-1 system on a honeycomb lattice. For comparison, the results obtained by OSCA and TSCA [44], EFT [31, 32] and SE [63, 64] are also given.

<table>
<thead>
<tr>
<th>OSCA</th>
<th>TSCA</th>
<th>EFT</th>
<th>EFT</th>
<th>SE</th>
<th>Present Work</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.5158</td>
<td>0.5449</td>
<td>0.5085</td>
<td>0.5158</td>
<td>0.698</td>
<td>0.6211</td>
</tr>
</tbody>
</table>

In Fig. (3), we represent the phase diagrams of the system in $(k_BT_c/J-D/J)$ plane for $\Omega/J=0, 0.5, 1.0$ and 1.5 where the solid and dotted lines correspond to the second and first order transitions and hollow circles denote the tricritical points. The numbers accompanying each curve denote the value of site concentration $c$. In Fig. (3), it is obvious that diluting the lattice sites reduces the critical temperatures of the second order phase transitions in

![](./images/867768492768624893_3.jpg)

FIG. 3: The phase diagrams of a diluted spin-1 BC model in $(k_BT_c/J-D/J)$ plane for $q=3$ with selected values of transverse field $\Omega/J=0.0,0.5,1.0$ and 1.5. Solid and dotted curves correspond to the second and first order phase transitions, respectively. Solid circles represent the tricritical points, and the numbers on the curves denote the site concentration $c$.

the system for $D/J\geq0$. As seen in the upper left panel of Fig. (3), the curve corresponding to pure case ($\Omega/J=0$ and $c=1.0$) exhibits a reentrant behavior of first order where a second order phase transition is followed by a first order phase transition at low temperatures for certain negative values of $D/J$. On the other hand, for $c=0.9$ we observe an extraordinary feature in the phase diagrams. In other words, there are two regions in $D/J$ plane at which a reentrant behavior occurs. The usual one is located within the interval $-1.3059<D/J<-1.0$ with a tricritical point $(D_t/J=-1.3058,k_BT_t/J=0.4192)$, and the other is found between $-1.0<D/J<0.0$. The latter behavior is quite interesting, since another tricritical point appears at $D_t/J=-1.0$ and $k_BT_t/J=0.0$. Besides, for $0>D/J>-1.0$ the system exhibits a reentrant behavior of second order. On the other hand, if we select $c=0.8$ then we see that the first order phase transitions and tricritical points disappear, and the system exhibits a reentrant behavior of second order within the interval $-1.1471<D/J<0.0$. Furthermore, the reentrance disappears as $D/J$ becomes positive for all selected values of $c$. Meanwhile, $(k_BT_c/J-D/J)$ phase diagrams for some selected values of $c$ with $\Omega/J=0.5$ are depicted on the upper right panel in Fig. (3). It is clearly seen from this figure that the system exhibits a first order reentrance for $c=1.0$ only in a narrow region $-1.4077<D/J<-1.3796$. For $c=0.9$, tricritical point and reentrance tends to disappear, but if we decrease the magnetic atom concentration further, such as for $c=0.8$ then the phase diagrams exhibit a bulge with a pronounced second order reentrance within the interval $-0.9358<D/J<-0.3554$. If we select sufficiently large transverse field strengths, such as $\Omega/J=1.0$, and 1.5 then the system cannot exhibit first order transitions and tricritical points anymore, even if $c=1.0$. In this case, we observe only second order phase transitions and ferromagnetic region gets narrower as $c$ decreases. In Ref.[51], the authors studied the same model for $q=4$, but they have not reported the behavior shown in Fig.(3) in their paper. All of the observations reported here can also be verified by examining the corresponding magnetization curves (see Fig.7).

The evolution of the phase diagrams shown in Fig. (3) for $\Omega/J=0$ and 0.5 are depicted in Fig. (4). As seen in Fig. (4a) where $\Omega/J=0$, the phase diagrams exhibit a reentrant behavior of second order within the interval $-1.0<D/J<0.0$ for $c=0.80,0.78,0.76$ and 0.75 whereas the reentrant phase transition region for $c=0.74$ and 0.73 is divided into two parts: The first part is located in the vicinity of $D/J=-1.0$ which gets narrower as $c$ decreases while the second one is observed between $-0.3607<D/J<0.0$. If we decrease $c$ further, such as for $c=0.69$ and 0.68 (see Fig. (4b)) reentrance disappears. However, for $0.62\leq c\leq0.67$ another reentrant regime appears, but now for $D/J\geq0$ which gets narrower as $c$ decreases. Similarly, Figs. (4c) and (4d) represents the evolution of phase diagrams of the system corresponding to the upper right panel in Fig. (3) where $\Omega/J=0.5$. As seen in Fig. (4c), the system undergoes only a second order phase transition for $c=0.87$. However for lower site concentrations e.g. $c=0.83$ and 0.81, reentrant behavior of second order appears between $-0.609<D/J<-0.4938$ and $-0.7891<D/J<-0.386$,

![](./images/867768492768624893_4.jpg)

FIG. 4: Evolution of the phase diagrams given in Fig. (3) for (a) $\Omega/J = 0.0$ and $0.73 \leq c \leq 0.80$, (b) $\Omega/J = 0.0$ and $0.62 \leq c \leq 0.69$, (c) $\Omega/J = 0.5$ and $0.72 \leq c \leq 0.87$, (d) $\Omega/J = 0.5$ and $0.63 \leq c \leq 0.69$. The numbers accompanying each curve denote the site concentration $c$.

respectively. In addition, for $c \leq 0.79$ the system exhibits a bulge in the reentrant phase transition regime which gets narrower as $c$ decreases. For $c < 0.72$ (Fig.(4d)), reentrance disappears, and the system undergoes a second order phase transition form a paramagnetic state to a ferromagnetic state with increasing temperature. For $c < 0.63$, site concentration of the system approaches to percolation threshold $c^{*}$, hence the ferromagnetic region becomes fairly narrow.

Next, as a complementary investigation of Fig. (3), we investigate the effects of transverse field interactions $\Omega/J$ on the phase diagrams of the system in Fig. (5) for some selected values of $c$. The upper left panel in Fig. (5) corresponds to the phase diagrams of the pure system [67] where we see that reentrant phase transitions tend to disappear and tricritical points decrease as $\Omega/J$ decreases for $c = 1.0$. Moreover, according to the upper right panel in Fig. (5), another ferromagnetic phase boundary arises between $-1.0 \leq D/J \leq 0.0$ and $-0.833 \leq D/J \leq -0.0434$ for $c = 0.9$ and $\Omega/J = 0.0, 0.25$, respectively. These additional phase transition lines get narrower as $\Omega/J$ increases, and disappear after a certain value of $\Omega/J$. Furthermore, phase diagrams shown in lower left and right panels invariably exhibit second order phase transitions for $c = 0.8$ and $0.7$ which is independent from transverse field value, and the reentrance is not observed anymore for $c = 0.7$ and $\Omega/J \geq 0.5$.

In Fig. (6), we examine the phase diagrams of the system in a $(k_{B}T_{c}/J - c)$ plane for $D/J = -1.25, -0.5, 0.0$ and $1.0$ with some typical $\Omega/J$ values. As seen in this figure, the system exhibits a tricritical behavior and its critical temperature cannot reach zero for $D/J = -1.25$ and $\Omega/J = 0.0$, hence we cannot speak on any percolation threshold value. However, phase transition temperature of the system reduces to zero at $c^{*} = 0.9764$ for $\Omega/J = 0.25$. It is clear from upper left panel in Fig. (6) that $c^{*}$ value for $\Omega/J = 0.75$ is greater than those of $\Omega/J = 0.5$, however it is lower than those of $\Omega/J = 0.25$. On the other hand, for $D/J = -1.25$ and $\Omega/J = 0.5$ the first order phase

![](./images/867768492768624893_5.jpg)

FIG. 5: The phase diagrams of a diluted spin-1 BC model in $(k_BT_c/J-D/J)$ plane for $q=3$ with selected values of site concentration $c=1.0,0.9,0.8$ and $0.7$. Solid and dotted curves correspond to the second and first order phase transitions, respectively. Solid circles represent the tricritical points, and the numbers on the curves denote the value of transverse field $\Omega/J$.

transitions and tricritical points disappear, and we barely observe a second order reentrance which also disappears for $\Omega/J=0.75$. If we select $D/J=-0.5$ then we cannot see any evidence of first order phase transitions, and critical site concentration $c^*$ of the system decreases as $\Omega/J$ increases up to $\Omega/J=0.75$. For $\Omega/J\geq0.75$ we observe that $c^*$ value tends to increase as $\Omega/J$ increases which is consistent with the indications depicted in Fig. (2a). Similar discussions are also valid for $D/J=0.0$ and $1.0$. Additionally, as an interesting characteristic of the system, we may note that the conditions for the occurrence of a second order reentrance in the system is rather complicated, since the existence or extinction of reentrance is rather sensitive to the collective effects of $D/J$, $\Omega/J$ and $c$.

As a final investigation, let us represent the temperature dependence of the magnetization for some selected values of Hamiltonian parameters corresponding to the phase diagrams depicted throughout Figs. (3)-(6). In Fig. (7), the typical transition profiles are shown for several values of Hamiltonian parameters. For example, if we select $D/J=-1.25$ and $\Omega/J=0.0$ magnetization curves corresponding to $c=1.0$, $0.95$ and $0.90$ exhibit a discontinuous jump at a first order transition temperature then gradually decrease and reduce to zero at a second order phase transition temperature with increasing temperature. This is an example of reentrance of first order in which a first order transition is followed by a second order transition. As an example of second order reentrant behavior, we can take a look at the magnetization curves that exist in a second order reentrant regime. For instance, we see that the magnetization curves exhibit two critical temperatures of the second order for $c=0.90$, $0.85$ and $0.80$ with $D/J=-0.5$ and $\Omega/J=0.0$. On the other hand, as an example of a second order ferromagnetic-paramagnetic phase transition, magnetization curves exhibit two different characteristics. As an example of the first case, we see that as the temperature increases then the magnetization of the system falls gradually from its saturation magnetization value at $k_BT/J=0.0$ and decreases continuously up to the vicinity of the transition temperature and vanishes at a critical temperature $k_BT_c/J$ for $c=1.0$ with $D/J=-0.5$ and $\Omega/J=0.0$ (corresponding to pure case), whereas in the second case the magnetization of the system exhibits a temperature-induced maximum with increasing temperature which is depicted on the lower left and right panels of Fig. (7).

## IV. CONCLUDING REMARKS

In this work, we have investigated the thermal and magnetic properties of a site diluted spin-1/2 Ising model and a spin-1 Blume Capel (BC) model in the presence of transverse field interactions. We have introduced an effective-field approximation that takes into account the multi-site correlations in the cluster of a considered lattice

![](./images/867768492768624893_6.jpg)

FIG. 6: The phase diagrams of a diluted spin-1 BC model in $(k_{B}T_{c}/J - c)$ plane for $q=3$ with selected values of the crystal field $D/J=-1.25,-0.5,0.0$ and 0.5. Solid and dotted curves correspond to the second and first order phase transitions, respectively. Solid circle denotes the tricritical point, and each curve in panels is plotted for a specific transverse field value.

![](./images/867768492768624893_7.jpg)

FIG. 7: Temperature dependence of the magnetization curves as functions of Hamiltonian parameters $D/J$, $\Omega/J$ and $c$. Solid and dotted magnetization curves exhibit second and first order phase transition properties, respectively.

with an improved configurational averaging technique. Our method is capable of locating the possible first order phase transition temperatures, as well as tricritical points, and under certain simplifications, equations of state obtained within the present approximation can be reduced to those obtained by conventional or improved decoupling approximation techniques which exposes the superiority of the present work.

For a spin-1/2 Ising system, we have obtained results that are superior to those estimated by conventional mean

field theory (MFT) and effective field theory (EFT) based on a decoupling approximation, especially for the critical site concentration (i.e. site percolation threshold) value $c^*$ for honeycomb ($q=3$) and square ($q=3$) lattices. Our estimated values $c^*=0.6727$ and $c^*=0.4594$ for $q=3$ and $q=4$, respectively are the best approximate values to the results of MC and SE methods among the other works based on MFT or EFT.

In particular, we have investigated the phase diagrams and magnetization curves of a site diluted spin-1 BC model in the presence of transverse field interactions and we have shown that diluting the lattice sites may cause some drastic changes on some of the characteristic features of the model. For this model, we have examined the variation of the site percolation threshold $c^*$ with the crystal and transverse field interactions which has not been reported in the literature before. In the absence of crystal and transverse fields, the percolation threshold value of a site diluted spin-1 model for $q=3$ is estimated as $c^*$=0.6211 which improves the results obtained by other EFT based approximations. In addition, we have found that the percolation threshold value $c^*$ strictly depends on the value of crystal and transverse field interactions, as well as the topology of the lattice. We have also given the global phase diagrams, especially the first order phase transition lines that include reentrant phase transition regions. The results presented in this paper clearly indicate that the conditions for the occurrence of a second order reentrance in the system is rather complicated, since the existence or extinction of reentrance is rather sensitive to the competing effects between $D/J$, $\Omega/J$ and $c$. These observations cannot be observed by ignoring any of these Hamiltonian parameters in the system.

As a result, we can conclude that all of the points mentioned above show that our method improves the conventional EFT methods based on decoupling approximation. Therefore, we hope that the results obtained in this work may be beneficial from both theoretical and experimental points of view.

### Acknowledgements

One of the authors (Y.Y.) would like to thank the Scientific and Technological Research Council of Turkey (TÜBİTAK) for partial financial support. This work has been completed at Dokuz Eylül University, Graduate School of Natural and Applied Sciences, and the numerical calculations reported in this paper were performed at TÜBİTAK ULAKBIM, High Performance and Grid Computing Center (TR-Grid e-Infrastructure). Partial financial support from SRF (Scientific Research Fund) of Dokuz Eylül University (2009.KB.FEN.077) (H.P.) is also acknowledged.

### Appendix A: Derivation of complete set of linear equations for spin-1/2 Ising Model

In the present formalism, all of the site correlations including central, as well as perimeter site magnetizations are denoted by $x_i$. For instance, for a honeycomb lattice $(q=3)$ we have

$$
\begin{aligned}
x_1 & = \langle \langle c_0 S_0 \rangle \rangle_r, \\
x_2 & = \langle \langle c_0 S_0 c_1 S_1 \rangle \rangle_r, \\
x_3 & = \langle \langle c_0 S_0 c_1 S_1 c_2 S_2 \rangle \rangle_r, \\
x_4 & = \langle \langle c_1 S_1 \rangle \rangle_r, \\
x_5 & = \langle \langle c_1 S_1 c_2 S_2 \rangle \rangle_r, \\
x_6 & = \langle \langle c_1 S_1 c_2 S_2 c_3 S_3 \rangle \rangle_r.
\end{aligned} \tag{A1}
$$

Basis correlation functions for central and perimeter sites are defined respectively as follows:

$$
\begin{aligned}
m = \langle \langle c_0 S_0 \rangle \rangle_r = x_1 & = (3c - 6c^2 + 3c^3)x_4 K_1 + (6c^2 - 6c^3)x_4 K_2 + 3c^3 x_4 K_3 + c x_6 K_4, \\
\langle \langle c_1 S_1 \rangle \rangle_r = x_4 & = (c - c^2)A_1 + c^2 A_2 + c x_1 A_3.
\end{aligned}
$$

By expanding Eq. (6) with $i=0$ and $\{f_i\} = c_1 S_1$ we get

$$
\langle \langle c_1 S_1 c_0 S_0 \rangle \rangle_r = x_2 = (3c^2 - 6c^3 + 3c^4)K_1 + (6c^3 - 6c^4)K_2 + 3c^4 K_3 + c^2 x_5 K_4.
$$

By the same way, putting $i=0$ and $\{f_i\} = c_1 S_1 c_2 S_2$ in Eq. (6) we obtain

$$
x_3 = (-3c^2 + 3c^3)x_4 K_1 + (6c^2 - 6c^3)x_4 K_2 + 3c^3 x_4 K_3 + c^3 x_4 K_4.
$$

Similarly, by using Eq. (16) with $\delta=1$ and $\{f_\delta\} = c_2 S_2$, and $\{f_\delta\} = c_2 S_2 c_3 S_3$ we find $x_5$ and $x_6$, respectively. Hence, we get the complete set of correlation functions as follows:

$$
\begin{aligned}
x_1 & = (3c - 6c^2 + 3c^3)x_4 K_1 + (6c^2 - 6c^3)x_4 K_2 + 3c^3 x_4 K_3 + c x_6 K_4, \\
x_2 & = (3c^2 - 6c^3 + 3c^4)K_1 + (6c^3 - 6c^4)K_2 + 3c^4 K_3 + c^2 x_5 K_4, \\
x_3 & = (-3c^2 + 3c^3)x_4 K_1 + (6c^2 - 6c^3)x_4 K_2 + 3c^3 x_4 K_3 + c^3 x_4 K_4, \\
x_4 & = (c - c^2)A_1 + c^2 A_2 + c x_1 A_3, \\
x_5 & = c x_2 A_3, \\
x_6 & = c x_3 A_3.
\end{aligned} \tag{A2}
$$

where the coefficients $K_n, (n=1,...,4)$ and $A_l, (l=1,...,3)$ are given in Eqs. (13) and (18), respectively.

On the other hand, corresponding to Eq. (A1), for a square lattice $(q=4)$ we have

$$
\begin{aligned}
x_1 & = \langle \langle c_0 S_0 \rangle \rangle_r, \\
x_2 & = \langle \langle c_0 S_0 c_1 S_1 \rangle \rangle_r, \\
x_3 & = \langle \langle c_0 S_0 c_1 S_1 c_2 S_2 \rangle \rangle_r, \\
x_4 & = \langle \langle c_0 S_0 c_1 S_1 c_2 S_2 c_3 S_3 \rangle \rangle_r, \\
x_5 & = \langle \langle c_1 S_1 \rangle \rangle_r, \\
x_6 & = \langle \langle c_1 S_1 c_2 S_2 \rangle \rangle_r, \\
x_7 & = \langle \langle c_1 S_1 c_2 S_2 c_3 S_3 \rangle \rangle_r, \\
x_8 & = \langle \langle c_1 S_1 c_2 S_2 c_3 S_3 c_4 S_4 \rangle \rangle_r.
\end{aligned} \tag{A3}
$$

By following the same procedure given for $q=3$ above, we get the complete set of linear equations for a square lattice $(q=4)$ as follows:

$$
\begin{aligned}
x_1 & = (4c - 12c^2 + 12c^3 - 4c^4)x_5 L_1 + (12c^2 - 24c^3 + 12c^4)x_5 L_2 + (12c^3 - 12c^4)x_5 L_3 \\
& \quad + 4c^4 x_5 L_4 + (4c - 4c^2)x_7 L_5 + 4c^2 x_7 L_6, \\
x_2 & = (4c^2 - 12c^3 + 12c^4 - 4c^5)L_1 + (12c^3 - 24c^4 + 12c^5)L_2 + (12c^4 - 12c^5)L_3 + 4c^5 L_4 \\
& \quad + (4c^2 - 4c^3)x_6 L_5 + 4c^3 x_6 L_6, \\
x_3 & = (-8c^2 + 12c^3 - 4c^4)x_5 L_1 + (12c^2 - 24c^3 + 12c^4)x_5 L_2 + (12c^3 - 12c^4)x_5 L_3
\end{aligned}
$$

$$+4 c^{4} x_{5} L_{4}+\left(4 c^{3}-4 c^{4}\right) x_{5} L_{5}+4 c^{4} x_{5} L_{6},$$
$$\begin{aligned}
x_{4}= & \left(4 c^{2}-4 c^{3}\right) x_{6} L_{1}+\left(-12 c^{2}+12 c^{3}\right) x_{6} L_{2}+\left(12 c^{2}-12 c^{3}\right) x_{6} L_{3}+4 c^{3} x_{6} L_{4} \\
& +\left(4 c^{2}-4 c^{3}\right) x_{6} L_{5}+4 c^{3} x_{6} L_{6},
\end{aligned}$$
$$x_{5}=\left(c-c^{2}\right) B_{1}+c^{2} B_{2}+c x_{1} B_{3},$$
$$x_{6}=\left(c-c^{2}\right) x_{5} B_{1}+c^{2} x_{5} B_{2}+c x_{2} B_{3},$$
$$x_{7}=\left(c-c^{2}\right) x_{6} B_{1}+c^{2} x_{6} B_{2}+c x_{3} B_{3},$$
$$x_{8}=\left(c-c^{2}\right) x_{7} B_{1}+c^{2} x_{7} B_{2}+c x_{4} B_{3}, \tag{A4}$$
where

$$L_{1}=\left.\sinh (J \nabla) \tanh (\beta x)\right|_{x=0},$$
$$L_{2}=\left.\cosh (J \nabla) \sinh (J \nabla) \tanh (\beta x)\right|_{x=0},$$
$$L_{3}=\left.\cosh ^{2}(J \nabla) \sinh (J \nabla) \tanh (\beta x)\right|_{x=0},$$
$$L_{4}=\left.\cosh ^{3}(J \nabla) \sinh (J \nabla) \tanh (\beta x)\right|_{x=0},$$
$$L_{5}=\left.\sinh ^{3}(J \nabla) \tanh (\beta x)\right|_{x=0},$$
$$L_{6}=\left.\cosh (J \nabla) \sinh ^{3}(J \nabla) \tanh (\beta x)\right|_{x=0}.$$

$$B_{1}=\left.\tanh (\beta(x+\gamma))\right|_{x=0},$$
$$B_{2}=\left.\cosh (J \nabla) \tanh (\beta(x+\gamma))\right|_{x=0},$$
$$B_{3}=\left.\sinh (J \nabla) \tanh (\beta(x+\gamma))\right|_{x=0},$$

Phase diagrams and magnetization curves can be obtained by solving Eq. (A4) numerically with the condition
$$x_{1}=x_{5}. \tag{A5}$$

### Appendix B: Derivation of complete set of linear equations for spin-1 BC model

We label the site correlations as $x_i$, $i=1,2,...,21$. The complete list is as follows

$$x_{1}=\left\langle\left\langle c_{0} S_{0}\right\rangle\right\rangle_{r}, \quad x_{12}=\left\langle\left\langle c_{0} S_{0} c_{1} S_{1}^{2} c_{2} S_{2}^{2}\right\rangle\right\rangle_{r},$$
$$x_{2}=\left\langle\left\langle c_{0} S_{0} c_{1} S_{1}\right\rangle\right\rangle_{r}, \quad x_{13}=\left\langle\left\langle c_{1} S_{1} c_{2} S_{2} c_{3} S_{3}^{2}\right\rangle\right\rangle_{r},$$
$$x_{3}=\left\langle\left\langle c_{0} S_{0} c_{1} S_{1} c_{2} S_{2}\right\rangle\right\rangle_{r}, \quad x_{13}=\left\langle\left\langle c_{1} S_{1} c_{2} S_{2}^{2} c_{3} S_{3}^{2}\right\rangle\right\rangle_{r},$$
$$x_{4}=\left\langle\left\langle c_{1} S_{1}\right\rangle\right\rangle_{r}, \quad x_{15}=\left\langle\left\langle c_{1} S_{1}^{2} c_{2} S_{2}^{2} c_{3} S_{3}^{2}\right\rangle\right\rangle_{r},$$
$$x_{5}=\left\langle\left\langle c_{1} S_{1} c_{2} S_{2}\right\rangle\right\rangle_{r}, \quad x_{16}=\left\langle\left\langle c_{0} S_{0}^{2}\right\rangle\right\rangle_{r},$$
$$x_{6}=\left\langle\left\langle c_{1} S_{1} c_{2} S_{2} c_{3} S_{3}\right\rangle\right\rangle_{r}, \quad x_{17}=\left\langle\left\langle c_{0} S_{0}^{2} c_{1} S_{1}\right\rangle\right\rangle_{r},$$
$$x_{7}=\left\langle\left\langle c_{1} S_{1}^{2}\right\rangle\right\rangle_{r}, \quad x_{18}=\left\langle\left\langle c_{0} S_{0}^{2} c_{1} S_{1}^{2}\right\rangle\right\rangle_{r},$$
$$x_{8}=\left\langle\left\langle c_{1} S_{1} c_{2} S_{2}^{2}\right\rangle\right\rangle_{r}, \quad x_{19}=\left\langle\left\langle c_{0} S_{0}^{2} c_{1} S_{1} c_{2} S_{2}\right\rangle\right\rangle_{r},$$
$$x_{9}=\left\langle\left\langle c_{1} S_{1}^{2} c_{2} S_{2}^{2}\right\rangle\right\rangle_{r}, \quad x_{20}=\left\langle\left\langle c_{0} S_{0}^{2} c_{1} S_{1} c_{2} S_{2}^{2}\right\rangle\right\rangle_{r},$$
$$x_{10}=\left\langle\left\langle c_{0} S_{0} c_{1} S_{1}^{2}\right\rangle\right\rangle_{r}, \quad x_{21}=\left\langle\left\langle c_{0} S_{0}^{2} c_{1} S_{1}^{2} c_{2} S_{2}^{2}\right\rangle\right\rangle_{r},$$
$$x_{11}=\left\langle\left\langle c_{0} S_{0} c_{1} S_{1} c_{2} S_{2}^{2}\right\rangle\right\rangle_{r}. \tag{B1}$$

The correlation functions $x_i$, $i=1,2,3$ are obtained from Eq. (23). For example, putting $i=0$ and $\{f_i\}=c_1S_1$ and $\{f_i\}=c_1S_1c_2S_2$ in Eq. (23) we obtain $x_2$ and $x_3$ correlation functions, respectively as follows

$$\left\langle\left\langle c_{0} S_{0} c_{1} S_{1}\right\rangle\right\rangle_{r}=x_{2}=3 c k_{1} x_{7}+\left(-6 k_{1}+6 k_{2}\right) c x_{9}+c k_{3} x_{13}+\left(3 k_{1}-6 k_{2}+3 k_{4}\right) c x_{15},$$
$$\left\langle\left\langle c_{0} S_{0} c_{1} S_{1} c_{2} S_{2}\right\rangle\right\rangle_{r}=x_{3}=\left(-3 k_{1}+6 k_{2}\right) c x_{8}+\left(3 k_{1}-6 k_{2}+k_{3}+3 k_{4}\right) c x_{14},$$

The equations labeled $x_j$ with $j=4,5,6$ are derived from Eq. (30). In a similar way, the correlation functions $x_k$ with $k=7,8,...,15$ and $x_l$ with $l=16,17,...,21$ can be easily obtained by using Eqs. (24) and (31), respectively. By following the above procedure, we can get the complete set of linear equations as follows:

$$x_{1}=3 c x_{4} k_{1}+c x_{6} k_{3}+\left(-6 k_{1}+6 k_{2}\right) c x_{8}+\left(3 k_{1}-6 k_{2}+3 k_{4}\right) c x_{14},$$
$$x_{2}=3 c k_{1} x_{7}+\left(-6 k_{1}+6 k_{2}\right) c x_{9}+c k_{3} x_{13}+\left(3 k_{1}-6 k_{2}+3 k_{4}\right) c x_{15},$$
$$x_{3}=\left(-3 k_{1}+6 k_{2}\right) c x_{8}+\left(3 k_{1}-6 k_{2}+k_{3}+3 k_{4}\right) c x_{14},$$
$$x_{4}=a_{1} c+a_{2} c x_{1}+\left(a_{3}-a_{1}\right) c x_{16},$$

$$
\begin{align*}
x_{5} &= a_{1}cx_{4} + a_{2}cx_{2} + (a_{3} - a_{1})cx_{17}, \\
x_{6} &= a_{1}cx_{5} + a_{2}cx_{3} + (a_{3} - a_{1})cx_{19}, \\
x_{7} &= b_{1}c + b_{2}cx_{1} + (b_{3} - b_{1})cx_{16}, \\
x_{8} &= b_{1}cx_{4} + b_{2}cx_{2} + (b_{3} - b_{1})cx_{17}, \\
x_{9} &= b_{1}cx_{7} + b_{2}cx_{10} + (b_{3} - b_{1})cx_{18}, \\
x_{10} &= b_{2}cx_{16} + b_{3}cx_{1}, \\
x_{11} &= b_{2}cx_{17} + b_{3}cx_{2}, \\
x_{12} &= b_{2}cx_{18} + b_{3}cx_{10}, \\
x_{13} &= b_{1}cx_{5} + b_{2}cx_{3} + (b_{3} - b_{1})cx_{19}, \\
x_{14} &= b_{1}cx_{8} + b_{2}cx_{11} + (b_{3} - b_{1})cx_{20}, \\
x_{15} &= b_{1}cx_{9} + b_{2}cx_{12} + (b_{3} - b_{1})cx_{21}, \\
x_{16} &= cr_{0} + 3cr_{2}x_{5} + (-3r_{0} + 3r_{1})cx_{7} + (3r_{0} - 6r_{1} + 3r_{3})x_{9} \\
&\quad + (-3r_{2} + 3r_{4})cx_{13} + (-r_{0} + 3r_{1} - 3r_{3} + r_{5})cx_{15}, \\
x_{17} &= (-2r_{0} + 3r_{1})cx_{4} + (3r_{0} + 3r_{2} + 3r_{3} - 6r_{1})cx_{8} \\
&\quad + (-r_{0} + 3r_{1} - 3r_{2} - 3r_{3} + 3r_{4} + r_{5})cx_{14}, \\
x_{18} &= (-2r_{0} + 3r_{1})cx_{7} + (3r_{0} - 6r_{1} + 3r_{2} + 3r_{3})cx_{9} \\
&\quad + (-r_{0} + 3r_{1} - 3r_{2} - 3r_{3} + 3r_{4} + r_{5})x_{15}, \\
x_{19} &= (r_{0} - 3r_{1} + 3r_{2} + 3r_{3})cx_{5} \\
&\quad + (-r_{0} + 3r_{1} - 3r_{2} - 3r_{3} + 3r_{4} + r_{5})cx_{13}, \\
x_{20} &= (r_{0} - 3r_{1} + 3r_{2} + 3r_{3})cx_{8} \\
&\quad + (-r_{0} + 3r_{1} - 3r_{2} - 3r_{3} + 3r_{4} + r_{5})cx_{14}, \\
x_{21} &= (r_{0} - 3r_{1} + 3r_{2} + 3r_{3})cx_{9} \\
&\quad + (-r_{0} + 3r_{1} - 3r_{2} - 3r_{3} + 3r_{4} + r_{5})cx_{15}. \tag{B2}
\end{align*}
$$

[1] A. I. Larkin, Sov. Phys. JETP 31, 784 (1970).

[2] Y. Imry and S. K. Ma, Phys. Rev. Lett. 35, 1399 (1975).

[3] S. F. Edwards and P. W. Anderson, J. Phys. F: Met. Phys. 5 (1975) 965.

[4] D. Sherington and S. Kirkpatrick, Phys. Rev. Lett. 35 (1975) 1792.

[5] H. Sato, A. Arrott, and R. Kikuchi, J. Phys. Chem. Solids 10 (1959) 19.

[6] S. H. Charap, Phys. Rev. 126 (1962) 1393.

[7] J. M. Yeomans and R. B. Stinchcombe, J. Phys. C: Solid State Phys. 11 (1978) L525.

[8] J. M. Yeomans and R. B. Stinchcombe, J. Phys. C: Solid State Phys. 12 (1979) 347.

[9] A. Benyoussef, N. Boccara and M. Saber, J. Phys. C: Solid State Phys. 18 (1985) 4275.

[10] E. Mina, A. Bohórquez, L. E. Zamora and G. A. P. Alcazar, Phys. Rev. B 47 (1993) 7925.

[11] G. B. Taggart, Physica A 116 (1982) 34.

[12] T. Kaneyoshi, I. Tamura and R. Honmura, Phys. Rev. B 29 (1984) 2769.

[13] A. Bobák and M. Jaščur, J. Magn. Magn. Mater. 136 (1994) 105.

[14] F. Zernike, Physica 7 (1940) 565.

[15] O. F. De Alcantara Bonfim and I. P. Fittipaldi, Phys. Lett. A 98 (1983) 199.

[16] N. Boccara, Phys. Lett. A 94 (1983) 185.

[17] T. Kaneyoshi, R. Honmura, I. Tamura and E. F. Sarmento, Phys. Rev. B 29 (1984) 5121.

[18] I. P. Fittipaldi, F. C. Sá Barreto and P. R. Silva, Physica A 131 (1985) 599.

[19] T. Balcerzak, A. Bobák, J. Mielnicki and V. H. Truong, Phys. Stat. Sol. B 130 (1985) 183.

[20] Z. Y. Li and C. Z. Yang, Solid State Commun. 56 (1985) 445.

[21] T. Kaneyoshi, J. Phys. C: Solid State Phys. 19 (1986) 2979.

[22] C. Z. Yang and J. L. Zhong, Phys. Stat. Sol. B 153 (1989) 323.

[23] J. W. Tucker, J. Magn. Magn. Mater. 102 (1991) 144.

[24] M. Saber and J. W. Tucker, J. Magn. Magn. Mater. 102 (1991) 287.

[25] A. Bobák and M. Jaščur, J. Phys. Condens. Matter 3 (1991) 6613.

[26] J. W. Tucker, J. Magn. Magn. Mater. 104-107 (1992) 191.

[27] T. Kaneyoshi and M. Jaščur, Phys. Stat. Sol. B 173 (1992) K37.

[28] M. Saber and J. W. Tucker, J. Magn. Magn. Mater. 114 (1992) 11.

[29] E. F. Sarmento and T. Kaneyoshi, Phys. Rev. B 48 (1993) 3232.

[30] T. Kaneyoshi, M. Jaščur, J. Magn. Magn. Mater. 130 (1994) 29.

[31] T. Kaneyoshi, Physica A 222 (1995) 450.

[32] T. Kaneyoshi, Physica A 218 (1995) 46.

[33] Y. Q. Liang, G. Z. Wei and Z. D. Zhang, J. Magn. Magn. Mater. 320 (2008) 1680.

[34] J. Mielnicki, T. Balcerzak, V. H. Truong, G. Wiatrowski and L. Wojtczak, J. Magn. Magn. Mater. 58 (1986) 325.

[35] J. Marro, A. Labarta and J. Tejada, Phys. Rev. B 34 (1986) 347.

[36] J. K. Kimand and A. Patrascioiu, Phys. Rev. Lett. 72 (1993) 2785.

[37] Z. Néda, J. Phys. I France 4 (1994) 175.

[38] H. G. Ballesteros, L. A. Fernández, V. M. Mayor, A. M. Sudupe, G. Parisi and J. J. R. Lorenzo, J. Phys. A: Math. Gen.
30 (1997) 8379.

[39] G. A. P. Alcazar, J. A. Plascak and E. G. da Silva, Phys. Rev. B 34 (1986) 1940.

[40] A. Labarta, J. Marro and J. Tejada, J. Phys. C: Solid State Phys. 19 (1986) 1567.

[41] A. Bobǎk and J. Karaba, Phys. Stat. Sol. B 142 (1987) 575.

[42] G. Wiatrowski, T. Balcerzak and J. Mielnicki, J. Magn. Magn. Mater. 71 (1988) 197.

[43] S. Mockovčiak, M. Jaščur and A. Bobák, Phys. Stat. Sol. B 166 (1991) K25.

[44] A. Bobák, S. Mockovčiak and J. Sivulka, Phys. Stat. Sol. B 176 (1993) 477.

[45] T. Balcerzak, J. Mielnicki, G. Wiatrowski and A. U. Kucharczyk, J. Phys.: Condens. Matter 2 (1990) 3955.

[46] M. Kerouad, M. Saber and J. W. Tucker, Phys. Stat. Sol. B 180 (1993) K23.

[47] A. Bakkali, M. Kerouad and M. Saber, Phys. Stat. Sol. B 186 (1994) 505.

[48] J. W. Tucker, M. Saber and L. Peliti, Physica A 206 (1994) 497.

[49] M. Kerouad, M. Saber and J. W. Tucker, J. Magn. Magn. Mater. 132 (1994) 223.

[50] M. Saber, Chinese Journal of Physics 35 (1997) 577.

[51] K. Htoutou, A. Oubelkacem, A. Ainane and M. Saber, J. Magn. Magn. Mater. 288 (2005) 259.

[52] K. Htoutou, A. Ainane, M. Saber and J. J. de Miguel, Physica A 358 (2005) 184.

[53] T. Balcerzak, J. Magn. Magn. Mater. 223 (2001) 309.

[54] P. G. de Gennes, Solid State Commun. 1 (1963) 132.

[55] Ü. Akıncı, Y. Yüksel and H Polat, Physica A 390 (2010) 541.

[56] Ü. Akıncı, Y. Yüksel and H Polat, Phys. Rev. E 83 (2011) 061103.

[57] H. B. Callen, Phys. Lett. 4, (1963) I61.

[58] R. Honmura, T. Kaneyoshi, J. Phys. C 12 (1979) 3979.

[59] T. Kaneyoshi, Acta Phys. Pol. 83 (1993) 703.

[60] M. Blume, Phys. Rev. 141 (1966) 517.

[61] H. W. Capel, Physica 32 (1966) 966.

[62] F. C. SáBarreto, I.P. Fittipaldi, B. Zeks, Ferroelectrics 39 (1981) 1103.

[63] M. F. Sykes, J. W. Essam, Phys. Rev. 133 (1964) 97 A310.

[64] M. F. Sykes, D. S. Gaunt and M. Glen, J. Phys. A: Math. Gen. 9 (1976) 97.

[65] J. M. Ziman, Models of Disorder, Cambridge University Press, Cambridge, 1979.

[66] D. Stauffer, A. Aharony, Introduction To Percolation Theory, Taylor & Francis, London, 1991.

[67] Y. Yuksel, H. Polat, J. Magn. Magn. Mater. 322 (2010) 3907.