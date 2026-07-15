# Mechanisms and origins of half-metallic ferromagnetism in CrO₂
I. V. Solovyev, $^{1,2,*}$ I. V. Kashin, $^{2}$ and V. V. Mazurenko $^{2}$

$^{1}$Computational Materials Science Unit, National Institute for Materials Science, 1-1 Namiki, Tsukuba, Ibaraki 305-0044, Japan
$^{2}$Department of Theoretical Physics and Applied Mathematics, Ural Federal University, Mira Street 19, 620002 Ekaterinburg, Russia

(Received 9 June 2015; revised manuscript received 21 August 2015; published 7 October 2015)

Using a realistic low-energy model, derived from the first-principles electronic structure calculations, we investigate the behavior of interatomic exchange interactions in CrO₂, which is regarded to be one of the canonical half-metallic (HM) ferromagnetics. For these purposes we employ the dynamical mean-field theory (DMFT), based on the exact diagonalization of the effective Anderson impurity Hamiltonian, which was further supplemented with the theory of infinitesimal spin rotations for the exchange interactions. In order to elucidate the relative roles played by static and dynamic electron correlations, we compare the obtained results with several static techniques, including the unrestricted Hartree-Fock (HF) approximation, static DMFT (corresponding to the infinite frequency limit for the self-energy), and optimized effective potential method for treating the correlation interactions in the random-phase approximation. Our results demonstrate that the origin of the HM ferromagnetism in CrO₂ is highly nontrivial. As far as the interactions in the neighboring coordination spheres are concerned, HF and DMFT methods produce very similar results, due to the partial cancellation of ferromagnetic (FM) double-exchange and antiferromagnetic (AFM) superexchange contributions, which represent two leading terms in the $(\Delta\hat{\Sigma})^{-1}$ expansion for the exchange interactions ($\Delta\hat{\Sigma}$ being the intra-atomic spin splitting). Both contributions are weaker in the HF approximation due to, respectively, additional orbital polarization of the $t_{2g}$ states and neglect of dynamic correlations. The role of higher-order terms in the $(\Delta\hat{\Sigma})^{-1}$ expansion is twofold. On the one hand, they give rise to additional FM contributions to the neighboring exchange interactions, which tend to stabilize the FM state. On the other hand, they produce AFM long-range interactions, which make the FM state unstable in the single-site DMFT calculations for the minimal model, consisting of the $t_{2g}$ bands. Thus, the robust ferromagnetism in the minimal model, which can be easily obtained using static approximations, is fortuitous and this picture is largely revised at the level of more rigorous DMFT approach. We argue that the main ingredients, which are missing in the minimal model, are the direct exchange interactions and the magnetic polarization of the oxygen $2p$ band. We evaluate these contributions in the local-spin-density approximation and argue that they play a very important role in stability of the FM ground state in CrO₂.

DOI: 10.1103/PhysRevB.92.144407
PACS number(s): 75.10.—b, 75.30.Et, 75.50.Ss, 71.10.Fd

## I. INTRODUCTION
CrO₂ provides a rare example of metallic ferromagnetism in stoichiometric oxides. It is widely used in magnetic recording and still considered to be one of the best particulates ever invented for these purposes [1,2]. Besides magnetorecording, chromium dioxide has attracted considerable interest due to its half-metallic (HM) electronic structure, which was predicted by the first-principles calculations [3]. The HM electronic structure is such that the majority-spin electrons are metallic, whereas the minority-spin electrons are semiconducting [4]. In CrO₂, such behavior has been supported by point-contact Andreev reflection measurements [5]. Because of its implication in various spin-dependent transport phenomena [6], the half-metallicity is the very important property of magnetic substances, which is intensively studied today [7]. These studies typically include both fundamental and practical aspects.

Needless to say, ferromagnetism is one of the key properties of CrO₂, which predetermines its popularity and importance in all the applications. Although the Curie temperature is not exceptionally high from the view point of practical applications (about 390 K, meaning that the magnetic properties are significantly deteriorated at room temperature) [2], it is still sufficiently high to classify CrO₂ as "robust ferromagnet."

Because of its popularity, CrO₂ is the well-studied material, both theoretically and experimentally. There is a fair number of theoretical works, focusing on the analysis of structural, transport, optical, and electronic properties of CrO₂ [3,8–14]. Many of them are based on the first-principles electronic structure calculations. These works clarify many important aspects of the material properties of CrO₂. However, despite its immanent importance in the field, the problem of interatomic magnetic interactions and stability of the ferromagnetic (FM) ground state in CrO₂ remains in the shadow. Particularly, why is CrO₂ FM? What are the main microscopic mechanisms yielding the FM ground state in CrO₂? From our point of view, these important questions remain largely unanswered and in the present work we try to fill in this gap.

The ferromagnetism in CrO₂ is typically ascribed to the double-exchange (DE) mechanism [10,15,16], which was originally introduced for magnetoresistive manganites [17–20]. This mechanism is governed by the large intra-atomic exchange splitting ($\Delta\hat{\Sigma}$) between the majority ($\uparrow$) and the minority ($\downarrow$) spin states, which penalizes the electron hoppings between atoms with the opposite directions of spins. In such a situation, the FM state will be the most stable one because any deviation from the collinear FM alignment of spins will increase the kinetic energy of electrons. The DE picture is well justified for large-spin ($S$) systems. In manganites, where $S=2$, it can be very useful for semiquantitative analysis, and, in many cases, provides a

*solovyev.Igor@nims.go.jp

valuable insight in understanding their electronic and magnetic properties [20,21]. However, even in this case, the additional effects can play an important role and substantially modify the canonical DE picture [22]. For instance, the well-known antiferromagnetic (AFM) superexchange interaction [23], which is also important in manganites, is formally a next-order effect in the $(\Delta \hat{\Sigma})^{-1}$ expansion for interatomic exchange interactions [21,22]. In $CrO_2$, where $S=1$, the interatomic spin splitting is not particularly large and the DE picture can be even more problematic: Namely, besides FM DE interactions between the nearest neighbors, one can expect other magnetic interactions (not necessarily the FM ones), which can alter the magnetic ground state [21]. Another important factor, which is not treated by the DE model, is the oxygen states [24–27].

Another disputable point is the role of electron correlations beyond the local-spin-density approximation (LSDA) and whether $CrO_2$ should be regarded as a strongly correlated material or not. On the one hand, LSDA and generalized gradient approximation (GGA) already provide a reasonable description for the structural, transport, and optical properties of $CrO_2$ with only moderate manifestation of many-body effects [8,9,11]. On the other hand, it was also suggested that electron correlations are essential for understanding results of photoemission, x-ray absorption, optical, and resistivity measurements [14]. We are not aware of any investigation of the effect of electron correlations on the behavior of interatomic exchange interactions in $CrO_2$. Basically, there is only one theoretical work [28], which addresses the problem of interatomic exchange interactions in $CrO_2$ on the basis of first-principles GGA and LSDA $+U$ calculations. However, both are static techniques and do not treat dynamic correlations. Moreover, the reliability of the LSDA $+U$ approach suffers from the use of the adjustable parameters as well as the still unresolved problem of how to construct the LSDA $+U$ functional in order to avoid the double-counting problem [29]. Taking into account the above controversy, it is crucially important to treat the electron correlations (if any) in the most unambiguous manner. In the present work, we try to pursue this strategy, first, by constructing the realistic model for $CrO_2$ and deriving all the parameters from first-principles calculations and, second, by solving this model within the dynamical mean-field theory (DMFT), supplemented with the exact diagonalization (ED) method for the quantum impurity problem. We show that the problem of stability of the HM FM ground state in $CrO_2$ is highly nontrivial. If one considers only the static on-site electron correlations in the frameworks of either unrestricted Hartree-Fock (HF) or static DMFT techniques, the FM ground state can be formally obtained already in the minimal model, consisting only of the closest to the Fermi level $t_{2g}$ bands. However, the dynamic correlations tend to destabilize this state. Therefore, in order to explain the experimentally observed ferromagnetism in $CrO_2$, it is crucially important to consider other magnetic interactions and we argue that these are the direct exchange interactions between Wannier functions centered at different Cr sites and the polarization of the oxygen $2p$ band. Another static approach—the so-called optimized effective potential (OEP) method—treating the correlation interactions in the random-phase approximation, produces a curious but unphysical insu- lating solution and further suppresses the tendencies towards the ferromagnetism. This again emphasizes the importance of consistent treatment of the correlation interactions in $CrO_2$.

The rest of the article is organized as follows. In Sec. II we explain the details of our method: the construction of the effective low-energy model (Sec. II A), the solution of the DMFT equations (Sec. II B), and the difference between unrestricted HF and static DMFT techniques (Sec. II C). In Sec. III we present our results for interatomic exchange interactions and discuss them in many details: the $(\Delta \hat{\Sigma})^{-1}$ expansion for nearest-neighbor (NN) and next-NN interactions (Sec. III A), the magnetic-state dependence of the interatomic exchange interactions (Sec. III B), the behavior of long- range interactions (Sec. III C), the contributions of the direct exchange interactions and the oxygen states (Sec. III D), as well as results of the OEP method (Sec. III E). Finally, in Sec. IV, we present a summary of our work.

## II. METHOD
### A. Parameters of effective low-energy model

In this section, we briefly remind the reader of the main ideas behind the construction of an effective low-energy model and present results of such construction for $CrO_2$. The methodological details can be found in the review article [30]. All calculations have been performed using parameters of the experimental rutile structure (the space group $P4_2/mnm = D_{4h}^{14}$) [31]. For practical electronic structure calculations we employ the linear muffin-tin orbital (LMTO) method in the atomic-spheres approximation (ASA) [32–34]. Technical aspects and corresponding details of the electronic structure of $CrO_2$ in comparison with results of full-potential calculations can be found in the Supplemental Material [35].

The model Hamiltonian,
$$
\begin{aligned}
\hat{\mathcal{H}}= & \sum_{i j} \sum_{\sigma} \sum_{a b} t_{i j}^{a b} \hat{c}_{i a \sigma}^{\dagger} \hat{c}_{j b \sigma} \\
& +\frac{1}{2} \sum_{i} \sum_{\sigma \sigma^{\prime}} \sum_{a b c d} U_{a b c d}^{i} \hat{c}_{i a \sigma}^{\dagger} \hat{c}_{i c \sigma^{\prime}}^{\dagger} \hat{c}_{i b \sigma^{\prime}} \hat{c}_{i d \sigma},
\end{aligned}\quad (1)
$$

![](./images/814591350367322112_1.jpg)

FIG. 1. (Color online) Total and partial densities of states of $CrO_2$ in the LDA. The shaded light (blue) area shows the contribution of the Cr $3d$ states. The positions of the main bands are indicated by symbols. The Fermi level is at zero energy (shown by dot-dashed line).

![](./images/814591350367322112_2.jpg)

FIG. 2. (Color online) Atomic electron densities, explaining relative positions of Cr $t_{2g}$ orbitals at the sites 1, 1$'$, and 2. The oxygen atoms are indicated by the green circles.

is formulated on the basis of Wannier orbitals $\{\phi_{ia}\}$, which are constructed for the magnetically active Cr $t_{2g}$ bands near the Fermi level, starting from the band structure in the local-density approximation (LDA) (Fig. 1). Here, $\sigma(\sigma')=\uparrow/\downarrow$ are the spin indices, while $a,b,c$, and $d$ label three $t_{2g}$ orbitals, which have the following form in the global coordinate frame: $|1\rangle=\pm\frac{1}{2}|xy\rangle+\frac{\sqrt{3}}{2}|3z^2-r^2\rangle$, $|2\rangle=\frac{1}{\sqrt{2}}|yz\rangle\pm\frac{1}{\sqrt{2}}|zx\rangle$, and $|3\rangle=|x^2-y^2\rangle$, where the upper and lower signs stand for the Cr sites 1 and 2, respectively (see Fig. 2). These orbitals are sometimes denoted as, respectively, $|xy\rangle,|yz-zx\rangle$, and $|yz+zx\rangle$, referring to the local coordinate frame [12]. It is important that at Cr sites all three orbitals belong to different irreducible representations of the point group $mmm=D_{2h}$, meaning that all local quantities, including the crystal field, DMFT self-energy, and local Green's function, will be diagonal with respect to these orbital indices. Moreover, the diagonal matrix elements will be the same for the Cr sites 1 and 2. In the following, we call this model the "minimal $t_{2g}$ model" or, simply, "minimal model."

Each lattice point $i$ ($j$) is specified by the position $\boldsymbol{\tau}$ ($\boldsymbol{\tau}'$) of the Cr site in the primitive cell and the lattice translation $\mathbf{R}$. Hence, the basis orbital $\phi_{ia}(\mathbf{r})\equiv\phi_{\tau a}(\mathbf{r}-\mathbf{R}-\boldsymbol{\tau})$ is centered in the lattice point $(\mathbf{R}+\boldsymbol{\tau})$ and labeled by the indices $\boldsymbol{\tau}$ and $a$. The Wannier basis was calculated using the projector-operator technique [30,36] and the orthonormal linear muffin-tin orbitals (LMTOs) [32-34] as the trial wave functions. In physical terms, LMTO can be viewed as the localized atomiclike Wannier function constructed for the whole region of valence states. Therefore, the projector-operator technique allows us to generate well-localized Wannier functions for the $t_{2g}$ bands, which is guaranteed by the good localization of LMTOs themselves. Then, the one-electron part of the model is identified with the matrix elements of the LDA Hamiltonian ($\mathcal{H}_{\text{LDA}}$) in the Wannier basis: $t_{\boldsymbol{\tau},\boldsymbol{\tau}'+\mathbf{R}}^{ab}=\langle\phi_{\tau a}(\mathbf{r}-\boldsymbol{\tau})|\hat{\mathcal{H}}_{\text{LDA}}|\phi_{\tau'b}(\mathbf{r}-\mathbf{R}-\boldsymbol{\tau}')\rangle$. Since the Wannier basis is complete in the low-energy part of the spectrum, the construction is exact in the sense that the band structure, obtained from $t_{\boldsymbol{\tau},\boldsymbol{\tau}'+\mathbf{R}}^{ab}$, exactly coincides with the one of LDA.

I. V. SOLOVYEV, I. V. KASHIN, AND V. V. MAZURENKO

PHYSICAL REVIEW B 92, 144407 (2015)

The site-diagonal part of $\hat{t}_{ij} \equiv [t_{ij}^{ab}]$ describes the crystal field splitting. It has the following form (in meV):

$$
\hat{t}_{11} = \begin{pmatrix}
-246 & 0 & 0 \\
0 & 60 & 0 \\
0 & 0 & 186
\end{pmatrix}. \tag{2}
$$

The matrices of transfer integrals in the bonds 1-1' and 1-2 are given by

$$
\hat{t}_{11'} = \begin{pmatrix}
-67 & 0 & 0 \\
0 & -191 & 0 \\
0 & 0 & 158
\end{pmatrix} \tag{3}
$$

and

$$
\hat{t}_{12} = \begin{pmatrix}
-15 & 0 & 0 \\
-28 & 0 & 0 \\
0 & 194 & -119
\end{pmatrix}, \tag{4}
$$

respectively. Other transfer integrals are considerably weaker [37]. The obtained values are in reasonable agreement with results of previous calculations [12]. One interesting aspect is the large matrix element $t_{11'}^{33} = 158$ meV, which is formally of the $dd\delta$ type (see Fig. 2) and, therefore, supposed to be weak [38]. Nevertheless, such large transfer integrals are possible due to the peculiar geometry of the $CrO_2$ lattice and contributions of the intermediate O $2p$ and Cr $e_g$ states [12]. In terms of the Wannier functions, this means that the functions should have a sizable tail spreading to the oxygen and other Cr sites [12]. Thus, already from this fact one can expect appreciable direct exchange interactions, which will be evaluated in Sec. III D. Another interesting aspect is the large asymmetric contribution $t_{12}^{32} = 194$ meV, caused by the electron transfer via intermediate oxygen atom [see Fig. 2(h)]. The same mechanism is responsible for finite $t_{12}^{21}$. However, it is considerably smaller than $t_{12}^{32}$.

Matrix elements of the on-site Coulomb interactions can be also obtained in the Wannier basis as

$$
U_{abcd}^i = \int d\mathbf{r} \int d\mathbf{r}' \phi_{ia}^*(\mathbf{r}) \phi_{ib}(\mathbf{r}) v_{\text{scr}}(\mathbf{r},\mathbf{r}') \phi_{ic}^*(\mathbf{r}') \phi_{id}(\mathbf{r}'),
$$

where the screened interaction $v_{\text{scr}}(\mathbf{r},\mathbf{r}')$ is computed in the constrained random-phase approximation (RPA) [39]. Since RPA is very time consuming, we apply additional approximations, which were discussed in [30]. Namely, first we evaluate the screened Coulomb and exchange interactions between atomic Cr $3d$ orbitals, using a fast and more suitable for these purposes, constrained LDA technique. After that, we consider an additional channel of screening caused by the $3d \to 3d$ transitions in the polarization function of the constrained RPA and project this function onto the $3d$ orbitals. The so-obtained parameters of Coulomb interactions are typically well consistent with results of full-scale constrained RPA calculations without additional approximations.

The obtained matrices of the on-site Coulomb interactions were fitted in terms of two Kanamori parameters [40]: the parameter of intraorbital Coulomb interaction $\mathcal{U} = 2.84$ eV and the exchange interaction $\mathcal{J} = 0.70$ eV. The third Kanamori parameter—the so-called interorbital Coulomb interaction— can be obtained from $\mathcal{U}$ and $\mathcal{J}$ as $\mathcal{U}' = \mathcal{U} - 2\mathcal{J}$. These parameters were used in the DMFT calculations.

After the construction, we fix the parameters of the effective model and solve it by using different many-body techniques. Since we deal only with the $3d$ ($t_{2g}$) states, we do not need to worry about the double-counting term [29], which in the present case would result only in the shift of the energy reference point. The feedback of the electron and spin-density change, developed in the $t_{2g}$ band in the process of solution of the minimal model, on other parts of the electronic structure (the so-called charge and spin self-consistency) will be addressed in Sec. III D, in the framework of the self-consistent linear response (SCLR) theory [41].

### B. Dynamical mean-field theory

Solution of the low-energy model, represented by the Hamiltonian (1), is a complicated numerical and methodological problem. In general, microscopic properties of a periodic magnetically collinear system can be expressed via one-electron Green's function $\hat{G}^{\uparrow,\downarrow}(\omega,\mathbf{k})$, which, in the reciprocal space, can be formally related to the frequency- and momentum-dependent self-energy $\hat{\Sigma}^{\uparrow,\downarrow}(\omega,\mathbf{k})$,

$$
\hat{G}^{\uparrow,\downarrow}(\omega,\mathbf{k}) = \left[ \omega - \hat{t}(\mathbf{k}) - \hat{\Sigma}^{\uparrow,\downarrow}(\omega,\mathbf{k}) \right]^{-1}, \tag{5}
$$

where $\hat{t}(\mathbf{k})$ is the one-electron part of the Hamiltonian (1) in the reciprocal space and all kinds of correlation effects are described by $\hat{\Sigma}^{\uparrow,\downarrow}(\omega,\mathbf{k})$.

The basic approximation, underlying the dynamical mean-field theory (DMFT), is that the self-energy is assumed to be independent on $\mathbf{k}$,

$$
\hat{\Sigma}^{\uparrow,\downarrow}(\omega,\mathbf{k}) \approx \hat{\Sigma}^{\uparrow,\downarrow}(\omega), \tag{6}
$$

which becomes exact in the limit of infinite dimensions (or coordination numbers) [42]. The main idea of DMFT is to map the initial many-body problem for the crystalline lattice onto the quantum impurity one, surrounded by an effective electronic bath, and find self-consistently the parameters of this bath. Namely, the local (or site-diagonal) Green's function of the crystal is given by

$$
\hat{G}^{\uparrow,\downarrow}(\omega) = \sum_{\mathbf{k}} \hat{G}^{\uparrow,\downarrow}(\omega,\mathbf{k}).
$$

It can be further used to obtain the bath Green's function, $\hat{\mathcal{G}}^{\uparrow,\downarrow}(\omega)$, from the Dyson equation:

$$
\hat{G}^{\uparrow,\downarrow}(\omega) = \hat{\mathcal{G}}^{\uparrow,\downarrow}(\omega) + \hat{\mathcal{G}}^{\uparrow,\downarrow}(\omega) \hat{\Sigma}^{\uparrow,\downarrow}(\omega) \hat{G}^{\uparrow,\downarrow}(\omega). \tag{7}
$$

Then, new $\hat{G}^{\uparrow,\downarrow}(\omega)$ is obtained by solving the Anderson impurity model. The corresponding Hamiltonian is given by

$$
\begin{aligned}
\hat{\mathcal{H}}_{imp} &= \sum_{a\sigma} E_{a\sigma} \hat{d}_{a\sigma}^{\dagger} \hat{d}_{a\sigma} + \frac{1}{2} \sum_{abcd,\sigma,\sigma'} U_{abcd} \hat{d}_{a\sigma}^{\dagger} \hat{d}_{c\sigma'}^{\dagger} \hat{d}_{b\sigma} \hat{d}_{d\sigma'} \\
&+ \sum_{ap\sigma} [ V_{ap\sigma} \hat{d}_{a\sigma}^{\dagger} \hat{c}_{p\sigma} + \text{H.c.} ] + \sum_{p\sigma} \epsilon_{p\sigma} \hat{c}_{p\sigma}^{\dagger} \hat{c}_{p\sigma}, \tag{8}
\end{aligned}
$$

where $\hat{d}(\hat{d}^{\dagger})$ and $\hat{c}(\hat{c}^{\dagger})$ are the electron annihilation(creation) operators for the impurity and bath states, respectively, $V_{ap\sigma}$ is impurity-bath hybridization, and $E_{a\sigma}$ ($\epsilon_{p\sigma}$) are the noninteracting energy levels of the impurity (bath). In order to obtain parameters of the Anderson impurity model, we adapt

144407-4

the following analytical form of the bath Green's function (separately for each $t_{2g}$ orbital $a$),
$$
\mathcal{G}_{a \sigma}^{N_{p}}(\omega)=\left(\omega-E_{a \sigma}-\sum_{p=1}^{N_{p}} \frac{\left|V_{a p \sigma}\right|^{2}}{\omega-\epsilon_{p \sigma}}\right)^{-1},
$$
and fit it in terms of $E_{a \sigma}$, $\epsilon_{p \sigma}$, and $V_{a p \sigma}$. Generally speaking, the number of bath states $p$ is infinite. However, in order to handle this problem numerically by means of ED, we discretize the bath and use a finite number of bath orbitals $N_{p}$ for each impurity orbital. It enables us to numerically diagonalize the impurity Hamiltonian (8) and obtain $\hat{\mathcal{G}}_{i m p}^{\uparrow, \downarrow}$, which is further identified with $\hat{G}^{\uparrow, \downarrow}(\omega)$. Then, using $\mathcal{G}_{a}(\omega) \equiv \mathcal{G}_{a}^{N_{p}}(\omega)$, the new self-energy can be found from the Dyson equation (7). After that, it is substituted into Eq. (5) to obtain new $\hat{G}^{\uparrow, \downarrow}(\omega, \mathbf{k})$, and the problem is solved self-consistently.

The ED method allows us to find the ground state as well as the low-lying excitations of the quantum impurity model. The standard numerical algorithms to treat the eigenproblem are based on the matrix-vector multiplication, where the initial vector, matrix, and net vector are stored in computer's random-access memory (RAM). In order to make our model treatment realistic, it is necessary to take the total number of the effective orbitals ranging from 15 to 18. However, it would lead to the Hamiltonian matrix (8) of the dimensionality $\sim(10^{10} \times 10^{10})$, which makes the diagonalization procedure troublesome, even for modern multiprocessor computers.

In this study we use the newly developed numerical ED scheme, based on the standard Arnoldi algorithm implemented in the ARPACK program package [43], where the Hamiltonian matrix is not stored in the RAM, but efficiently recalculated "on-the-fly" at each matrix-vector multiplication step. It makes the computational time increase by only $10\%-15\%$. However, the amount of necessary RAM is decreased by $80\%-90\%$, giving us the possibility to perform realistic calculations with a large number of effective orbitals. More details can be found in the separate article [44]. Particularly, using this scheme, we were able to include four bath states per each $t_{2g}$ orbital in the framework of DMFT. We have confirmed that the obtained electronic structure is well converged depending on the number of the bath states. The numerical calculations have been performed for the temperature $T=232$ K, which is substantially smaller than the magnetic transition temperature,
![](./images/814591350367322112_3.jpg)

FIG. 3. (Color online) Partial densities of states as obtained in the unrestricted HF approach (left) and the DMFT (right) for the FM state. The Fermi level is at zero energy (shown by a dot-dashed line).

<table>
<caption>Table I. Self-consistent orbital populations $\{n_a^{\uparrow,\downarrow}\}$ for the FM states, as obtained in DMFT and unrestricted HF calculations for the minimal $t_{2g}$ model.</caption>
<thead>
<tr>
<th>
</th>
<th>
$n_1^{\uparrow}$
</th>
<th>
$n_2^{\uparrow}$
</th>
<th>
$n_3^{\uparrow}$
</th>
<th>
$n_1^{\downarrow}$
</th>
<th>
$n_2^{\downarrow}$
</th>
<th>
$n_3^{\downarrow}$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
DMFT
</td>
<td>
0.934
</td>
<td>
0.587
</td>
<td>
0.431
</td>
<td>
0.010
</td>
<td>
0.020
</td>
<td>
0.023
</td>
</tr>
<tr>
<td>
HF
</td>
<td>
0.999
</td>
<td>
0.710
</td>
<td>
0.291
</td>
<td>
0
</td>
<td>
0
</td>
<td>
0
</td>
</tr>
</tbody>
</table>

and in the external magnetic field $\mu_{\text{B}}H=5$ meV, which is required in order to lift the magnetic degeneracy of multiplet states [45]. The example of the electronic spectrum is shown in Fig. 3, which is in remarkable agreement with results of the previous DMFT studies [13].

### C. Static DMFT versus unrestricted Hartree-Fock approach

The asymptotic high-frequency behavior of $\hat{\Sigma}^{\uparrow,\downarrow}(\omega)$ in DMFT is given by [46],
$$
\begin{aligned}
\Sigma_{1}^{\uparrow}(\infty)=&(\mathcal{U}-3 \mathcal{J})(n_{2}^{\uparrow}+n_{3}^{\uparrow})+\mathcal{U} n_{1}^{\downarrow} \\
&+(\mathcal{U}-2 \mathcal{J})(n_{2}^{\downarrow}+n_{3}^{\downarrow}),
\end{aligned}
\tag{9}
$$
where $\{n_a^{\uparrow,\downarrow}\}$ are the self-consistent populations in DMFT:
$$
n_a^{\uparrow,\downarrow}=-\frac{1}{\pi} \operatorname{Im} \int_{-\infty}^{\varepsilon_{\text{F}}} d \omega G_a^{\uparrow,\downarrow}(\omega).
$$

Other matrix elements of $\hat{\Sigma}^{\uparrow,\downarrow}(\infty)$ can be obtained from Eq. (9) by the permutation of the spin and orbital indices. $\hat{\Sigma}^{\uparrow,\downarrow}(\infty)$ has the same form as the potential matrix in the unrestricted HF method [30], but with different populations: In DMFT, these populations include the effect of frequency-dependence of the self-energy, while in HF, they do not. For the FM state, these populations are summarized in Table I. Besides the small population of the $\downarrow$-spin states (and, therefore, small deviation from the HM behavior), the main difference between DMFT and HF is in the orbital polarization of the $\uparrow$-spin states (see Fig. 3). The first orbital is practically fully occupied in both approaches. The population of other two orbitals tends to be nearly equal in DMFT, while in HF these states are strongly polarized and there is an additional redistribution of electrons between $n_2^{\uparrow}$ and $n_3^{\uparrow}$. Finite values of $\{n_a^{\downarrow}\}$ is the natural result of DMFT calculations for the HM magnets, which is related to the existence of nonquasiparticle $\downarrow$-spin states near the Fermi level [7,13]. Nevertheless, we have found that these states have a minor effect on the behavior of interatomic exchange interactions and, from this point of view, $\text{CrO}_2$ can be still treated as the HM ferromagnet, even in DMFT.

## III. INTERATOMIC EXCHANGE INTERACTIONS

We consider the mapping of the electron model (1) onto the Heisenberg model with $S=1$:
$$
\hat{\mathcal{H}}_S=-\frac{1}{2} \sum_{i j} J_i \hat{\boldsymbol{S}}_j \cdot \hat{\boldsymbol{S}}_{j+i}.
$$

In these notations, $J_i$ is the exchange coupling between two Cr sites, located in the origin (0) and in the point $i$ of the lattice, relative to the origin. The mapping onto the spin model

144407-5

<table>
<caption>TABLE II. Parameters of interatomic exchange interactions (in meV) as obtained in the theory of infinitesimal spin rotations for the minimal $t_{2g}$ model, supplemented with different types of approximations for treating the electron correlations: unrestricted Hartree-Fock approximation (HF), dynamical mean-field theory (DMFT), static limit for the DMFT self-energy $\hat{\Sigma}(\omega \to \infty)$ (SDMFT), and local-spin-density approximation (LSDA). The notations of parameters $J_i$ are explained in Fig. 4.</caption>
<thead>
  <tr>
    <th>Parameter</th>
    <th>HF</th>
    <th>DMFT</th>
    <th>SDMFT</th>
    <th>LSDA</th>
  </tr>
</thead>
<tbody>
  <tr>
    <th>$J_1$</th>
    <td>14.06</td>
    <td>16.35</td>
    <td>19.63</td>
    <td>17.20</td>
  </tr>
  <tr>
    <th>$J_2$</th>
    <td>12.26</td>
    <td>12.14</td>
    <td>13.65</td>
    <td>10.34</td>
  </tr>
  <tr>
    <th>$J_3$</th>
    <td>1.16</td>
    <td>0.60</td>
    <td>0.82</td>
    <td>0.65</td>
  </tr>
  <tr>
    <th>$J_4$</th>
    <td>0.96</td>
    <td>0.35</td>
    <td>0.78</td>
    <td>0.27</td>
  </tr>
  <tr>
    <th>$J_5$</th>
    <td>$-0.39$</td>
    <td>$-1.15$</td>
    <td>$-0.72$</td>
    <td>$-1.49$</td>
  </tr>
  <tr>
    <th>$J_6$</th>
    <td>$-1.87$</td>
    <td>$-1.85$</td>
    <td>$-1.78$</td>
    <td>$-5.67$</td>
  </tr>
  <tr>
    <th>$J_7^{<}$</th>
    <td>$-1.21$</td>
    <td>$-2.58$</td>
    <td>$-1.45$</td>
    <td>$-2.63$</td>
  </tr>
  <tr>
    <th>$J_7^{>}$</th>
    <td>$-3.26$</td>
    <td>$-4.19$</td>
    <td>$-3.25$</td>
    <td>$-8.40$</td>
  </tr>
  <tr>
    <th>$J_8^{<}$</th>
    <td>$-0.31$</td>
    <td>$-0.94$</td>
    <td>$-0.47$</td>
    <td>$-1.85$</td>
  </tr>
  <tr>
    <th>$J_8^{>}$</th>
    <td>$-0.46$</td>
    <td>$-2.44$</td>
    <td>$-1.00$</td>
    <td>$-1.55$</td>
  </tr>
</tbody>
</table>

implies the adiabatic motion of spins when all instantaneous changes of the electronic structure adjust slow rotations of the spin-magnetic moments. The parameters of this model can be obtained by using the theory of infinitesimal spin rotations [47,48],

$$
J_{i}=\frac{1}{2 \pi} \operatorname{Im} \int_{-\infty}^{\varepsilon_{\mathrm{F}}} d \omega \operatorname{Tr}_{L}\left\{\Delta \hat{\Sigma}(\omega) \hat{G}_{0 i}^{\uparrow}(\omega) \Delta \hat{\Sigma}(\omega) \hat{G}_{i 0}^{\downarrow}(\omega)\right\}, \quad(10)
$$

where $\hat{G}_{0 i}^{\uparrow, \downarrow}(\omega)=\left[\omega-\hat{t}-\hat{\Sigma}^{\uparrow, \downarrow}(\omega)\right]_{0 i}^{-1}$ is the one-electron Green's function between sites 0 and $i$, $\Delta \hat{\Sigma}=\hat{\Sigma}^{\uparrow}-\hat{\Sigma}^{\downarrow}$, and $\operatorname{Tr}_{L}$ denotes the trace over the orbital indices. The parameters $\{J_{i}\}$ given by Eq. (10) are nothing but the second derivatives of the total energy with respect to the rotations of spins. Therefore, this definition of the Heisenberg model is valid only for small rotations of the magnetic moments near the FM state and characterizes the local stability of this state. The effect of finite rotations is discussed in Sec. III B.

The parameters of interatomic magnetic interactions, obtained in the theory of infinitesimal spin rotations, are listed in Table II and their behavior is explained in Fig. 4. We note the following. (i) As expected, the FM ground state is stabilized by the NN and next-NN interactions ($J_1$ and $J_2$, respectively). The values of these interactions, obtained in the DMFT and unrestricted HF approach, are surprisingly close, while static DMFT overestimates both of them. (ii) Besides strong FM interactions $J_1$ and $J_2$, there are several types of AFM interactions, operating in the fifth, sixth, seventh, and eighth coordination spheres, which tend to destabilize the FM state. These interactions are especially strong in the case of DMFT. For comparison, we also show in Table II and Fig. 4 the parameters of interatomic exchange interactions, obtained in LSDA for the minimal $t_{2g}$ model. For these purposes, we derive parameters of the one-electron Hamiltonian $[t_{ij}^{ab}]$ for the spin-polarized $t_{2g}$ bands in LSDA and then use them for the calculation of the exchange interactions (10). Then spin dependence of the electronic structure in this case is solely described by the parameters $t_{ij}^{ab}$, which are different for different spin channels. One can clearly see that the LSDA results for the isolated $t_{2g}$ band reveal a very similar tendency: The FM interactions $J_1$ and $J_2$ are counterbalanced by even stronger AFM interactions in the sixth and seventh coordination spheres. In the next sections, we elucidate the microscopic origin of such behavior and its consequences on the properties of $\mathrm{CrO}_{2}$.

![](./images/814591350367322112_4.jpg)

FIG. 4. (Color online) (Left) Distance dependence of interatomic exchange interactions as obtained in the theory of infinitesimal spin rotations for the minimal $t_{2g}$ model, supplemented with different types of approximations for treating the electron correlations: local-spin density approximation (LSDA), unrestricted Hartree-Fock approximation (HF), dynamical mean-field theory (DMFT), and static limit for the DMFT self-energy $\hat{\Sigma}(\omega \to \infty)$ (SDMFT). (Right) Lattice of Cr sites with the notation of interatomic exchange interactions.

### A. Double exchange and beyond

The ferromagnetism of $\mathrm{CrO}_{2}$ is frequently attributed to the DE mechanism [10,15,16]. This is a very important point, which needs to be clarified.

In the HM regime, all poles of $\hat{G}^{\downarrow}(\omega)$ are located in the unoccupied part of the spectrum and $\Delta \hat{\Sigma}$ can be regarded as a large parameter. This justifies the use of the $(\Delta \hat{\Sigma})^{-1}$ expansion in the occupied part [22],

$$
\hat{G}^{\downarrow}(\omega)=-(\Delta \hat{\Sigma})^{-1} \sum_{n=0}^{\infty}\left(\left[\Delta \hat{\Sigma} \hat{G}^{\uparrow}\right]^{-1}\right)^{n},
$$

which follows from the identity $\hat{G}^{\downarrow}=\left(\left[\hat{G}^{\uparrow}\right]^{-1}-\Delta \hat{\Sigma}\right)^{-1}$. The $n=0$ term of this expansion contains only site-diagonal elements and does not contribute to Eq. (10). Therefore, in the HM state, $J_i$ can be presented as an infinite series,

$$
J_{i}=\sum_{n=1}^{\infty} J_{i}^{(n)}, \quad(11)
$$

where

$$
\begin{aligned}
J_{i}^{(n)}= & -\frac{1}{2 \pi} \operatorname{Im} \int_{-\infty}^{\varepsilon_{\mathrm{F}}} d \omega \operatorname{Tr}_{L} \\
& \times\left(\hat{G}_{0 i}^{\uparrow}(\omega)\left\{\left[\Delta \hat{\Sigma}(\omega) \hat{G}^{\uparrow}(\omega)\right]^{-1}\right\}_{i 0}^{n} \Delta \hat{\Sigma}(\omega)\right). \quad(12)
\end{aligned}
$$

The $n=1$ term corresponds to the DE interaction, which can be easily found analytically [22]:

$$
J_{i}^{(1)}=\frac{1}{2 \pi} \operatorname{Im} \int_{-\infty}^{\varepsilon_{\mathrm{F}}} d \omega \operatorname{Tr}_{L}\left\{\hat{G}_{0 i}^{\uparrow}(\omega) \hat{t}_{i 0}\right\}. \quad(13)
$$

Moreover, using the identity $\hat{G}^{\uparrow}(\omega)[\omega-\hat{t}-\hat{\Sigma}^{\uparrow}(\omega)]=\hat{1}$, it is straightforward to show that

$$
\sum_{i} J_{i}^{(1)}=-\frac{1}{2} E_{\text {kin }}, \tag{14}
$$

where $E_{\text {kin }}$ is the kinetic energy (per one Cr site):

$$
E_{\text {kin }}=-\frac{1}{\pi} \operatorname{Im} \int_{-\infty}^{\varepsilon_{\mathrm{F}}} d \omega \operatorname{Tr}_{L}\left\{\hat{G}_{00}^{\uparrow}(\omega)\left[\omega-\hat{t}_{00}-\hat{\Sigma}^{\uparrow}(\omega)\right]\right\}.
$$

From Eq. (14) it is clear that the main interactions $J_{i}^{(1)}$ should be positive (or FM). This equation is nearly perfectly reproduced by our calculations. For instance, we have obtained the following values of DE interactions in DMFT: $J_{1}^{(1)}=$ 28.95 meV, $J_{2}^{(1)}=19.44$ meV, $J_{3}^{(1)}=1.33$ meV, and $J_{4}^{(1)}=$ 1.59 meV. Since the Wannier functions are localized and the transfer integrals connecting more remote sites are small, the corresponding parameters of DE interactions are also small. Then, by considering the sum of DE interactions up to the fourth coordination sphere, we find $2 J_{1}^{(1)}+8 J_{2}^{(1)}+4 J_{3}^{(1)}+$ $8 J_{4}^{(1)}=231.50$ meV, which readily reproduces 99% of the kinetic energy $-\frac{1}{2} E_{\text {kin }}=234.13$ meV. A similar conclusion holds for unrestricted HF and SDMFT.

Moreover, SDMFT yields very similar parameters of the main DE interactions: $J_{1}^{(1)}=28.71$ meV and $J_{2}^{(1)}=$ 19.82 meV, which are practically undistinguishable from the ones in DMFT. However, the parameters obtained in the HF method are considerably smaller, especially for the NNs: $J_{1}^{(1)}=23.75$ meV and $J_{2}^{(1)}=19.03$ meV. Such behavior is directly related to the orbital polarization and additional splitting of the states 2 and 3 around the Fermi level (see Fig. 3), which tend to decrease $|E_{\text {kin }}|$ and, therefore, the values of DE interactions. For instance, in the case of $J_{1}^{(1)}$, all transfer integrals (3) are diagonal with respect to the orbital indices. Therefore, as the orbitals 2 and 3 become, respectively, more and less populated in the case of HF calculations (see Table I), the DE interaction $J_{1}^{(1)}$ will decrease. In the case of $J_{2}^{(1)}$, the situation is less straightforward, because the transfer integrals (4) mix the orbitals 2 and 3, counterbalancing the change of the orbital occupations.

Other contributions to $J_{i}^{(n)}$ can be found numerically. Particularly, $J_{i}^{(2)}$ is of the first order of $[\Delta \hat{\Sigma}(\omega)]^{-1}$. It contains the contributions of superexchange interactions and the ex- change processes between sites separated by two hoppings. In the static case, all these parameters can be expressed via the moments of the local density of states [21]. However, in the dynamic case such a simple relationship does not take place, because of the frequency dependence of $\hat{\Sigma}$.

The results of these calculations are shown in Fig. 5. Both $J_{1}^{(n)}$ and $J_{2}^{(n)}$ display some characteristic oscillating behavior, where the odd FM contributions are partially compensated by the even AFM ones. This tendency is observed in all the calculations, based on the unrestricted HF, SDMFT, and DMFT techniques. The main difference is the conver- gence of $\sum_{n} J_{i}^{(n)}$, which is noticeably slower in DMFT: the frequency-dependence substantially reduces $\operatorname{Re}[\Delta \hat{\Sigma}]$ in the occupied part, especially in the region close to the Fermi level (see Fig. 6) and, therefore, slows down the convergence of the $(\Delta \hat{\Sigma})^{-1}$ expansion. On the other hand, $\operatorname{Im}[\Delta \hat{\Sigma}]$ is relatively small in the occupied part and does not play a significant role. Another important aspect is the cancellation of FM and AFM contributions to $J_{1}$ and $J_{2}$. As discussed above, the unrestricted HF approach yields somewhat weaker FM DE contributions $J_{1}^{(1)}$ and $J_{2}^{(1)}$, due to the orbital polarization effects. However, the next AFM contributions $J_{1}^{(2)}$ and $J_{2}^{(2)}$ are also weaker due to the larger spin splitting $\Delta \hat{\Sigma}$ in comparison with DMFT. Thus, the total values of $J_{1}$ and $J_{2}$, obtained after summation

![](./images/814591350367322112_5.jpg)

FIG. 5. (Color online) Results of the $(\Delta \hat{\Sigma})^{-1}$ expansion for the NN (top) and next-NN (bottom) exchange interactions. The individual contributions, $J_{i}^{(n)}$, are shown on the left panel and their sum is shown on the right panel. The asymptotic values of $J_{1}$ and $J_{2}$ are shown by the dash-dotted lines.

![](./images/814591350367322112_6.jpg)

FIG. 6. (Color online) Frequency dependence of the intraatomic spin splitting $\Delta \hat{\Sigma}(\omega)$ in DMFT. The static limit $\Delta \hat{\Sigma}(\omega \to \infty)$ is shown by dashed lines. The Fermi level is at zero energy (shown by a dot-dashed line).

of all these contributions, appear to be very close in the case of HF and DMFT.

The series $\sum_{n} J_{i}^{(n)}$ is practically converged for $n=5$, where these sums are close to the saturated values of $J_{1}$ and $J_{2}$. The major FM contribution to $J_{1}$ and $J_{2}$ is indeed due to the DE mechanism $(n=1)$. However, this contribution is not the only one and, at least, the $n=3$ term is also very important in stabilizing the FM ground state. Thus, already from this point of view, it is not quite right to consider $CrO_{2}$ as the DE system: The behavior of $J_{1}$ and $J_{2}$ involves other important mechanisms besides the DE and superexchange interactions, which are considered in the conventional DE model [19,20].

### B. Magnetic-state dependence of interatomic exchange interactions and Curie temperature

The exchange interactions (10) depend on the magnetic state in which they are calculated. This dependence reflects the change of the electronic structure in different magnetic states and such information is incorporated in the one-electron Green's function $\hat{G}^{\uparrow, \downarrow}(\omega)$. The magnetic state dependence of exchange interactions may have different physical origin. For instance, it can be the orbital ordering in insulating [49] or metallic [50] systems, or simply the change of the bandwidth in metallic compounds depending on the magnetic state [19]. The theory of infinitesimal spin rotations [47,48] is more suitable for the description of the effects, which are related to small variations of the magnetic moments near the ground state (for instance, the spin waves). Generally speaking, it is not applicable for the analysis of large perturbations, such as the spin disorder near the Curie temperature $(T_{C})$, unless the exchange interactions do not depend on the magnetic state.

The comparison of interatomic exchange interactions, calculated in the FM and AFM states using the theory of infinitesimal spin rotations in the frameworks of unrestricted HF and DMFT methods, is given in Table III (throughout this work we consider the simplest AFM configuration, where the corner and body-centered $Cr$ moments in the single unit cell are oriented antiferromagnetically). One can clearly see that the exchange interactions are quite sensitive to the magnetic state in which they are calculated. Generally, the AFM structure remains unstable and is not the ground state of $CrO_{2}$. Nevertheless, the AFM spin alignment tends to reconstruct the electronic structure (Fig. 7) in such a way as to additionally stabilize the FM interactions $J_{1}$ in the NN ferromagnetically coupled bond. Moreover, in DMFT, the FM interactions $J_{2}$ in the antiferromagnetically coupled next-NN bond are strongly reduced, which also works in the direction of stabilizing the AFM state. Similar tendency holds for longer-range interactions. Thus, if one tries to use the parameters obtained in the AFM state in order to describe the FM state, one can easily find that this FM state will be unstable, even in the unrestricted HF approach. Perhaps this was an extreme example; below we consider a more realistic strategy for the evaluation of $T_{C}$.

Taking into consideration the strong magnetic state dependence of exchange interactions, we tried to go beyond the theory of infinitesimal spin rotations and evaluated the exchange interactions using results of self-consistent total energy calculations for the spin-spiral configurations with arbitrary wave vectors $\mathbf{q}$. Namely, using a generalized Bloch theorem [51], we performed the unrestricted HF calculations for the spin-spiral configurations, where the directions of magnetic moments varied as

$$
\boldsymbol{e}_{\boldsymbol{\tau}+\mathbf{R}}=\left(\begin{array}{c}
\cos (\boldsymbol{\tau}+\mathbf{R}) \cdot \mathbf{q} \\
\sin (\boldsymbol{\tau}+\mathbf{R}) \cdot \mathbf{q} \\
0
\end{array}\right),
$$

calculated the total energy $(E_{\mathbf{q}})$ for each $\mathbf{q}$, and evaluated the exchange interactions from the Fourier transform of $E_{\mathbf{q}}$. The results are also listed in Table III, in the column "SCHF". Par- ticularly, we expected that the exchange interactions, obtained by mapping the total energies of the spin-spiral configurations onto the Heisenberg model, should provide a good estimate for $T_{C}$. The latter was evaluated using Tyablikov's RPA [52]. The results are also listed in Table III and can be summarized as follows: As long as we use the unrestricted HF approximation, supplemented either with the theory of infinitesimal spin rota- tions near the FM state or with the self-consistent spin-spiral

TABLE III. Parameters of interatomic exchange interactions (in meV) and corresponding Curie temperature (in K), obtained using different techniques and starting conditions, such as the theory of infinitesimal spin rotations near the ferromagnetic (F) and antiferromagnetic (A) state in the frameworks of unrestricted HF and DMFT methods, as well as the mapping of the total energies obtained in the self-consistent HF calculations for the spin-spiral configurations onto the Heisenberg model (SCHF). The notations of parameters $J_{i}$ are explained in Fig. 4. The dash sign in the row $T_{C}$ means that for the given set of parameters the ferromagnetic state is unstable.

| Parameter | HF       |       | DMFT     |       | SCHF |
|-----------|----------|-------|----------|-------|------|
|           | F        | A     | F        | A     |      |
| $J_{1}$   | 14.06    | 23.77 | 16.35    | 18.14 | 11.00|
| $J_{2}$   | 12.26    | 14.91 | 12.14    | 6.73  | 15.43|
| $J_{3}$   | 1.16     | 0.25  | 0.60     | 0.21  | 2.90 |
| $J_{4}$   | 0.96     | 1.39  | 0.35     | $-1.08$| 1.43 |
| $J_{5}$   | $-0.39$  | 1.39  | $-1.15$  | $-2.66$| 0.10 |
| $J_{6}$   | $-1.87$  | $-0.14$| $-1.85$  | 0.22  | $-1.36$|
| $J_{7}^{<}$| $-1.21$ | $-6.21$| $-2.58$  | $-2.68$| $-4.13$|
| $J_{7}^{>}$| $-3.26$ | $-7.99$| $-4.19$  | $-5.03$| $-4.13$|
| $J_{8}^{<}$| $-0.31$ | $-0.94$| $-0.94$  | $-3.57$| $-1.41$|
| $J_{8}^{>}$| $-0.46$ | $-3.05$| $-2.44$  | $-1.60$| $-1.41$|
| $T_{C}$   | 581      | $-$   | $-$      | $-$   | 684  |

![](./images/814591350367322112_7.jpg)

FIG. 7. (Color online) Partial densities of states as obtained in the unrestricted HF approach (left) and the DMFT (right) for the antiferromagnetic state. The Fermi level is at zero energy (shown by a dot-dashed line).

calculations for finite $\mathbf{q}$'s, running through the first Brillouin zone (BZ), $T_{\mathrm{C}}$ is even overestimated in comparison with the experimental data, meaning that the FM state is indeed very robust. However, when we switch to more rigorous DMFT technique, the FM state appears to be unstable because of the longer-range AFM interactions (and any numerical estimates of $T_{\mathrm{C}}$ in this case become meaningless). This is a very serious problem, which we discuss in detail in the next section.

### C. Long-range interactions and stability of the ferromagnetic state

In Sec. III A, we have seen that, as far as the NN and next-NN interactions are concerned, unrestricted HF and DMFT techniques produce very similar results. Nevertheless, there is an important difference in the behavior of longer- range interactions, which has fundamental consequences. Since the frequency-dependence reduces the intra-atomic spin splitting $\operatorname{Re}[\Delta \hat{\Sigma}(\omega)]$ near the Fermi level, the series (11) converges somewhat slower in the case of DMFT. Besides oscillating behavior depicted in Fig. $5$, smaller $\operatorname{Re}[\Delta \hat{\Sigma}(\omega)]$ is responsible for larger spacial extension of the exchange interactions. This can be directly seen from the construction $([\Delta \hat{\Sigma}(\omega) \hat{G}^{\uparrow}(\omega)]^{-1})_{i 0}^{n}$ in Eq. (12): Since $[\hat{G}^{\uparrow}(\omega)]_{i j}^{-1}=\hat{t}_{i j}$ for $i \neq j$, and the transfer integrals are typically restricted by only few coordination spheres, the $n$-order term will include the processes, which connect two remote sites 0 and $i$ by $n$ sequential hoppings between NNs or next-NNs. Obviously, such contributions will be stronger for smaller $\operatorname{Re}[\Delta \hat{\Sigma}(\omega)]$. Moreover, the number of nodes of the integrand in Eq. (12) increases with the distance between 0 and $i$ [53,54]. Therefore, it is possible that some of these long-range interactions can easily become antiferromagnetic. Such behavior is clearly seen in Table II and Fig. 4: Besides FM interactions, there are several relatively strong AFM interactions, connecting the sites in the fifth-eighth coordination spheres. These interactions become more pronounced in DMFT because of smaller spin splitting $\operatorname{Re}[\Delta \hat{\Sigma}(\omega)]$. As expected, the strongest effect is found in LSDA, which is characterized by the smallest spin splitting between the $t_{2 g}$ states (about 1.5 eV).

The appearance of the AFM interactions naturally rises the question about the stability of the FM state and whether it is indeed the magnetic ground state of the considered $t_{2 g}$ model. In order to investigate this problem, we evaluate the spin-wave dispersion, $\omega(\mathbf{q})$, using the interatomic exchange interactions obtained in the theory of infinitesimal spin rotations. In the $P4_{2}/mnm$ structure, containing two magnetic sublattices, $\omega(\mathbf{q})$ can be obtained from the diagonalization of the $2 \times 2$ matrix (for $S=1$),
$$
\hat{\Omega}(\mathbf{q})=\left(\begin{array}{cc}
J_{11}(\mathbf{q})-J_{0} & J_{12}(\mathbf{q}) \\
J_{21}(\mathbf{q}) & J_{22}(\mathbf{q})-J_{0}
\end{array}\right),
$$
where $J_{\alpha \beta}(\mathbf{q})$ is the Fourier image of magnetic interactions between sublattices $\alpha$ and $\beta$, and $J_{0}=J_{11}(0)+J_{12}(0)$. In principle, due to the symmetry properties, $J_{22}(\mathbf{q})$ can be related to $J_{11}(\mathbf{q}^{*})$ in some other $\mathbf{q}$ point. The same holds for $J_{12}(\mathbf{q})$ and $J_{21}(\mathbf{q}^{*})$. The results of these calculations are shown in Fig. 8. The negative spin-wave frequencies signal that the FM state is unstable. One can clearly see that as long as we use the static HF and SDMFT techniques, there is no problem with the stability of the FM state, and $T_{\mathrm{C}}$ is even overestimated in comparison with the experimental data (Table III). Thus, one could naively think that the FM state is very robust. Nevertheless, in DMFT, which is definitely the most rigorous approach among the considered ones, the FM state appears to be unstable. This instability occurs along three high-symmetry directions of the BZ ($\Gamma$-X, $\Gamma$-M, and $\Gamma$-Z). This is a very serious problem, meaning that there should be additional factors, which are not taken into account in the minimal model for the $t_{2 g}$ bands and which stabilize the FM state. It could be regarded as the failure of the conventional single-site DMFT for the description of the ferromagnetism in $\mathrm{CrO}_{2}$, and the formal extension would be to consider the intersite interactions [56,57]. However, it is not $a$ priori clear what is the microscopic origin of these interactions and what are the real physical processes, which stand behind them. In the next section, we study this problem more in detail.

![](./images/814591350367322112_8.jpg)

FIG. 8. (Color online) Results of calculations of the spin-wave dispersion with the parameters, obtained in the theory of infinitesimal spin rotations in the cases of HF, SDMFT, and DMFT techniques. Notations of the high-symmetry points of the Brillouin zone are taken from [55].

### D. Direct exchange interactions and contributions of the oxygen states

In this section, we evaluate the change of the magnetic energy, caused by the polarization of the O $2p$ band and other contributions, which are not taken into account in the minimal model for the $t_{2 g}$ bands.

For these purposes, after the solution of the minimal model in DMFT, we go back from the Wannier basis $\{\phi_{\tau a}\}$ of the model to the original LMTO basis $\{\chi_{v b}\}$,
$$
\phi_{\tau a}(\mathbf{r}-\boldsymbol{\tau})=\sum_{v b} q_{\tau a}^{v b} \chi_{v b}(\mathbf{r}-\boldsymbol{v}),\qquad(15)
$$
and construct the spin magnetization density, $m(\mathbf{r})=n_{\uparrow}(\mathbf{r})-$ $n_{\downarrow}(\mathbf{r})$, associated with the $t_{2 g}$ band. This $m(\mathbf{r})$ has major contributions at the Cr sites, as well as some hybridization-induced contribution at the oxygen sites. Following the philosophy of the low-energy model [30], the interaction of $m(\mathbf{r})$ with the rest of the electronic states should be well described already at the LSDA level. Therefore, our strategy is to evaluate, in LSDA, the exchange-correlation (xc) field $b(\mathbf{r})=v_{\downarrow}(\mathbf{r})-v_{\uparrow}(\mathbf{r})$ ($v_{\uparrow,\downarrow}$ being the xc potential in LSDA, which is induced by $m(\mathbf{r})$ and polarizes the O $2p$ band, and find the self-consistent change of $m(\mathbf{r})$ and $b(\mathbf{r})$, caused by the interaction between

$t_{2g}$ and O $2p$ bands. For these purposes, it is convenient to use the SCLR theory [41]. For simplicity, let us consider the discrete lattice model and assume that all weights of $m(\mathbf{r})$ are concentrated in the lattice points: $m(\mathbf{r})=\sum_{v} m_{v} \delta(\mathbf{r}-\boldsymbol{v})$, where $m_{v}$ is the local magnetic moment at the site $v$. Furthermore, we recall that LSDA is conceptually close to the Stoner model, where the xc energy is given by [58]

$$
E_{\mathrm{xc}}=-\frac{1}{4} \sum_{v} I_{v} m_{v}^{2}. \tag{16}
$$

In practical calculations, the parameters $\{I_{v}\}$ can be found using the values of intra-atomic spin splitting and local magnetic moments in LSDA. Meanwhile, the intra-atomic spin splitting can be obtained using the LMTO parameters of the centers of gravity for the $\uparrow$- and $\downarrow$-spin states [33], which yields $I_{\mathrm{Cr}}=0.98$ eV and $I_{\mathrm{O}}=1.68$ eV.

Then, the self-consistent field can be found as

$$
\vec{b}=[1+\hat{\mathcal{I}} \hat{\mathcal{R}}]^{-1} \vec{b}^{0},
$$

where we have introduced the vector $\vec{b} \equiv[b_{v}]$ and the tensors $\hat{\mathcal{I}}=[I_{v} \delta_{v v^{\prime}}]$ and $\hat{\mathcal{R}}=[\mathcal{R}_{v v^{\prime}}]$. In this equation, $\vec{b}^{0}=\hat{\mathcal{I}} \vec{m}$ is the xc field induced by the $t_{2g}$ band, and the response tensor $\hat{\mathcal{R}}$ is obtained in the first-order perturbation theory for the wave functions, starting from the nonmagnetic LDA band structure,

$$
\mathcal{R}_{v v^{\prime}}=\sum_{a b} \sum_{n}^{\text {occ }} \sum_{n^{\prime}}^{\text {unocc }} \sum_{\mathbf{k}}^{\text {BZ }}\left\{\frac{\left(C_{n \mathbf{k}}^{v a}\right)^{*} C_{n^{\prime} \mathbf{k}}^{v a}\left(C_{n^{\prime} \mathbf{k}}^{v^{\prime} b}\right)^{*} C_{n \mathbf{k}}^{v^{\prime} b}}{\varepsilon_{n \mathbf{k}}-\varepsilon_{n^{\prime} \mathbf{k}}}+\text { c.c. }\right\},
$$

where $\{C_{n \mathbf{k}}^{v a}\}$ are the coefficients of the expansion of the LDA wave functions over LMTOs, $\{\varepsilon_{n \mathbf{k}}\}$ are the LDA eigenvalues, and $\mathbf{k}$ runs over the first BZ. Moreover, similar to the constrained RPA [39], we have to exclude from Eq. (17) the contributions, where both indices $n$ and $n^{\prime}$ belong to the $t_{2g}$ band. In the perturbation theory, such terms describe the change of the magnetization in the $t_{2g}$ band, which is caused by the LSDA potential. However, in the minimal model, this part is replaced with the more rigorous DMFT solution with the screened Coulomb interactions. Therefore, in order not to take them into account twice, such contributions should be excluded in the process of SCLR calculations. In practice, $n$ runs over the occupied O $2p$ bands and $n^{\prime}$ runs over the unoccupied Cr $t_{2g}$ and $e_{g}$ bands. Note also that we do not explicitly use the double-counting term, which controls the relative position of the Cr $3d$ and O $2p$ states [29]. However, by using the LDA band structure as the starting point for the SCLR calculations, we imply that this relative position can be well described on the LDA level.

Once the self-consistent field $\vec{b}$ is known, the change of $\vec{m}$ and $\vec{b}$, caused by the polarization of the oxygen band, can be found as $\delta \vec{m}=-\hat{\mathcal{R}} \vec{b}$ and $\delta \vec{b}=\hat{\mathcal{I}} \delta \vec{m}$, respectively. Since the O $2p$ band is occupied, the net change of magnetic moment will vanish: $\sum_{v} \delta m_{v}=0$, irrespectively on the type of the magnetic order. Nevertheless, the individual moments $\delta m_{v}$ can be finite and contribute to the total energy. The corresponding energy change, caused by the magnetic polarization of the oxygen band, consists of the two parts: $\delta E^{\mathrm{pol}}=\delta E_{\mathrm{Cr}-\mathrm{O}}^{\mathrm{pol}}+\delta E_{\mathrm{O}}^{\mathrm{pol}}$, where $\delta E_{\mathrm{Cr}-\mathrm{O}}^{\mathrm{pol}}=-\frac{1}{2} \delta \vec{m}^{T} \hat{\mathcal{I}} \vec{m}$ is the interaction of $\delta m_{v}$ with the "external" xc field, created by the $t_{2g}$ band and $\delta E_{\mathrm{O}}^{\mathrm{pol}}$ is the energy change caused by $\delta \vec{m}$ in the O $2p$ band. It also consists of two parts: $\delta E_{\mathrm{O}}^{\mathrm{pol}}=\delta E_{\mathrm{sp}}+\delta E_{\mathrm{dc}}$, where $\delta E_{\mathrm{sp}}$ is the single-particle energy, which can be found in the second order of $\delta \vec{b}$ as $\delta E_{\mathrm{sp}}=\frac{1}{4} \delta \vec{b}^{T} \hat{\mathcal{R}} \vec{b}$ [41], and $\delta E_{\mathrm{dc}}=\frac{1}{4} \delta \vec{m}^{T} \hat{\mathcal{I}} \delta \vec{m}$ is the double-counting energy, where $\delta \vec{m}^{T}$ is the row vector, corresponding to the column vector $\delta \vec{m}$. In all these calculations, it is assumed that the magnetic energy of the $t_{2g}$ band itself is described by DMFT.

<table>
<caption>Table IV. The values of local magnetic moments at the chromium and oxygen sites $\{m_{v}\}$ as obtained in DMFT calculations for the isolated $t_{2g}$ band in the case of ferromagnetic (F) and antiferromagnetic (A) alignment of Cr spins and the moments $\{\delta m_{v}\}$, caused by the polarization of the O $2p$ band. All values are in $\mu_{\text{B}}$.</caption>
<tbody>
<tr><th rowspan="2"></th><td colspan="2">F</td><td colspan="2">A</td></tr>
<tr><th>$m_{v}$</th><th>$\delta m_{v}$</th><th>$m_{v}$</th><th>$\delta m_{v}$</th></tr>
<tr><th>Cr</th><td>1.628</td><td>0.594</td><td>1.392</td><td>0.584</td></tr>
<tr><th>O</th><td>0.134</td><td>−0.297</td><td>0.029</td><td>−0.089</td></tr>
</tbody>
</table>

The polarization energy $\delta E^{\text{pol}}$ may have different values in the case of the FM and AFM alignment of spins and, thus, contributes to interatomic exchange interactions. In principle, in order to be consistent with the theory of infinitesimal spin rotations [47,48], the magnetic state dependence of $\delta E^{\text{pol}}$ should be treated in a similar way. Nevertheless, in the first application of this method, which we consider below, we evaluate this dependence from the total energy difference between FM and AFM states. The latter approach is more transparent. Moreover, it is easier to realize technically. Since the magnetic polarization of the oxygen band is not particularly large, we expect the considered energy change to be well described by the Heisenberg model, even for finite rotations of spins. Furthermore, the direct exchange interactions, which we also consider below, are, by the definition, of the Heisenberg form [59].

The obtained magnetic moments are listed in Table IV and the energies are in Table V. The spin moments $m_{v}$ are redistributed between Cr and oxygen sites. As expected for the FM state, the total moment is $m_{\mathrm{Cr}}+2 m_{\mathrm{O}}=1.9$ $\mu_{\text{B}}$, which is totally consistent with the value obtained in the Wannier basis (see Table I). The small deviation from $2\ \mu_{\text{B}}$ is caused by nonquasiparticle $\downarrow$-spin states near the Fermi level.

<table>
<caption>Table V. The energy changes (in meV per one formula unit), caused by the magnetic polarization of the O $2p$ band in the ferromagnetic (F) and antiferromagnetic (A) states: the interaction energy between Cr $t_{2g}$ and O $2p$ bands ($\delta E_{\mathrm{Cr}-\mathrm{O}}^{\mathrm{pol}}$), the magnetic energy in the O $2p$ band ($\delta E_{\mathrm{O}}^{\mathrm{pol}}$), and the total energy ($\delta E^{\mathrm{pol}} = \delta E_{\text{Co-O}}^{\mathrm{pol}}+\delta E_{\mathrm{O}}^{\mathrm{pol}}$). All values were derived using DMFT magnetization density for the $t_{2g}$ band.</caption>
<tbody>
<tr><th rowspan="2"></th><td>F</td><td>A</td></tr>
<tr><th>$\delta E_{\mathrm{Cr}-\mathrm{O}}^{\mathrm{pol}}$</th><td>−449.27</td><td>−434.67</td></tr>
<tr><th>$\delta E_{\mathrm{O}}^{\mathrm{pol}}$</th><td>99.04</td><td>66.42</td></tr>
<tr><th>$\delta E^{\mathrm{pol}}$</th><td>−350.24</td><td>−368.24</td></tr>
</tbody>
</table>
144407-10

The moments $m_v$ and $\delta m_v$ are parallel at the Cr sites and antiparallel at the oxygen sites. This tendency is consistent with results of first-principles calculations and can be deduced from the analysis of hybridization between the Cr $3d$ and O $2p$ states [60]. Therefore, the negative sign of $\delta E_{\text{Cr-O}}$ is due to the contributions of the Cr sites, which are partly compensated by positive contributions of the oxygen sites. The absolute value of $\delta E_{\text{Cr-O}}$ is larger in the FM state, mainly because $m_{\text{Cr}}$ and $\delta m_{\text{Cr}}$ are larger. Thus, the Cr-O interaction additionally stabilizes the FM state. The contribution of the O $2p$ band to the magnetic energy is positive. This is because the O $2p$ band itself does not favor the magnetism and any magnetic polarization of this band will increase the total energy. This also explains why $\delta E_{\text{O}}$ is smaller in the AFM state: The magnetic moments $\delta m_v$ are smaller and, therefore, the magnetic perturbation of the O $2p$ band is also smaller. In $\text{CrO}_2$, the second effect ($\delta E_{\text{O}}$) dominates and the polarization of the O $2p$ slightly favors the AFM alignment. The corresponding energy difference between FM and AFM states, $\Delta E^{\text{pol}} = \delta E^{\text{pol}}(\text{F}) - \delta E^{\text{pol}}(\text{A})$, is about 18 meV per one formula unit.

Another contribution to the magnetic energy is related to the direct interactions between Wannier functions in the $t_{2g}$ bands [26,27], which are centered at different Cr sites. They are not taken into account in the minimal model, because the latter treats only on-site Coulomb and exchange interactions. Nevertheless, these interactions can be evaluated in LSDA. First, let us evaluate the difference of LSDA xc energies between FM and AFM states in the $t_{2g}$ band, $\Delta E_{\text{xc}} = \delta E_{\text{xc}}(\text{F}) - \delta E_{\text{xc}}(\text{A})$, using the values of magnetic moments $\{m_v\}$ from Table IV and Eq. (16) for $E_{\text{xc}}$. This yields $\Delta E_{\text{xc}} = -199.65$ meV per one formula unit, where the main contribution (about 93%) comes from the Cr sites. This energy difference favors the FM alignment. Then we note that the xc interaction between Wannier orbitals centered at the same Cr site is already taken into account in the minimal model in the framework of DMFT. Therefore, we should subtract this on-site "self-interaction" (SI) part from the LSDA xc energy difference. This can be done as follows. Using the spin magnetization matrix

$$
\hat{\mathcal{M}}_{\tau} \equiv\left[\mathcal{M}_{\tau}^{a b}\right]=-\frac{1}{\pi} \operatorname{Im} \int_{-\infty}^{\varepsilon_{\mathrm{F}}} d \omega\left[\hat{G}_{\tau \tau}^{\uparrow}(\omega)-\hat{G}_{\tau \tau}^{\downarrow}(\omega)\right],
$$

obtained in the Wannier basis at the Cr site $\tau$, and the expansion (15) over LMTOs, we evaluate magnetic moments, which are produced by $\hat{\mathcal{M}}_{\tau}$ at the central and neighboring sites $v$:

$$
\bar{m}_{v}=\sum_{a b c}\left(q_{\tau a}^{v c}\right)^{*} \mathcal{M}_{\tau}^{a b} q_{\tau b}^{v c}.
$$

The difference between $\bar{m}_{v}$ and $m_{v}$ is that $\bar{m}_{v}$ is the contribution of the single Cr site $\tau$ to the magnetic moment at the site $v$, while $m_{v}$ takes into account the contributions of all sites of the Cr lattice. Therefore, $\bar{m}_{v}$ at the central site $\tau$ is substantially smaller than $m_{v}$ ($\bar{m}_{v}=1.169$ and $1.099\ \mu_{\text{B}}$ in the FM and AFM state, respectively). The total moment $\sum_{v} \bar{m}_{v}$ in the FM state is only $1.543\ \mu_{\text{B}}$, which also substantially deviates from $\sum_{v} m_{v}=1.9\ \mu_{\text{B}}$. Then, we evaluate the SI energy, which is also given by (16), but after replacing $\{m_v\}$ with $\{\bar{m}_{v}\}$. This yields the following energy difference between FM and AFM states: $\Delta E_{\text{SI}} \equiv \delta E_{\text{SI}}(\text{F}) - \delta E_{\text{SI}}(\text{A}) = -39.19$ meV per one formula unit. Therefore, by subtracting the SI term, we additionally shift the energy balance in the favor of antiferromagnetism.

![](./images/814591350367322112_9.jpg)

FIG. 9. (Color online) Results of calculations of the spin-wave dispersion with the DMFT parameters obtained for the isolated $t_{2g}$ band (solid line) and after taking into account the additional FM contribution $\Delta J_{2}=17.81$ meV, arising from magnetic polarization of the oxygen band and direct exchange interactions in the $t_{2g}$ band (dotted line). Notations of the high-symmetry points of the BZ are taken from [55].

Thus, by combining all the contributions, the total energy difference $\Delta E = \Delta E^{\text{pol}} + \Delta E_{\text{xc}} - \Delta E_{\text{SI}}$ is about $-142.46$ meV per one formula unit. By mapping this total energy difference onto the Heisenberg model and assuming that it contributes only to the next-NN interactions, connecting two Cr sites in the primitive cell, one can find the following correction to this interaction, arising from the polarization of the oxygen band and direct exchange interactions in the $t_{2g}$ band: $\Delta J_{2} \equiv -\Delta E/8 = 17.81$ meV. The spin-wave dispersion, which takes into account the additional FM contribution $\Delta J_{2}$, is plotted in Fig. 9 in comparison with results of regular DMFT calculations for the isolated $t_{2g}$ band. One can clearly see that all $\omega(\mathbf{q})$ in this case become non-negative and the FM state is stable. Thus, the magnetic polarization of the oxygen band and direct exchange interactions in the $t_{2g}$ band play a very important role in the stability of the FM state in $\text{CrO}_2$.

## E. Optimized effective potential method and importance of dynamic correlations

In this section, we discuss results of the OEP method [61-65], which we consider mainly for pedagogical purposes, in order to emphasize the importance of careful treatment of the correlation effects. OEP is a numerical realization of the Kohn-Sham density functional theory [66], where

(1) the one-electron band structure is obtained from solution of Schrödinger equations with some effective static local potential $\hat{v}$,

$$
\left(\hat{t}_{\mathbf{k}}+\hat{v}\right)\left|c_{n \mathbf{k}}\right\rangle=\varepsilon_{n \mathbf{k}}\left|c_{n \mathbf{k}}\right\rangle ; \quad(18)
$$

14407-11

(2) the obtained band structure is used to calculate the total energy,
$$
E = E_{\text{kin}} + E_{\text{C}} + E_{\text{X}} + E_{\text{corr}}, \tag{19}
$$
consisting of kinetic ($E_{\text{kin}}$, which also includes the energy of crystal-field splitting), Coulomb ($E_{\text{C}}$), exchange ($E_{\text{X}}$), and correlation ($E_{\text{corr}}$) parts;

(3) the parameters of effective potential $\hat{v}$ are found numerically, so to minimize the total energy (19).

Thus, the OEP method provides some alternative possibility for the construction of static potential, which, in addition to the standard Coulomb and exchange contribution, includes the effect of correlation interactions and, in this sense, can be regarded as a step beyond the HF approximation. Details of calculations can be found in the Appendix.

By applying the OEP approach, we expected that the correlation effects, beyond the HF approximation, will reduce the orbital polarization and yield an improved description, at least for the majority-spin states and DE interactions. Moreover, we expected RPA to work reasonably well for metallic systems, such as $\text{CrO}_2$. Since the RPA total energy of HM systems does not depend on the position of unoccupied $\downarrow$-spin states, we cannot easily determine in the framework of this method the spin-splitting $\Delta\hat{\Sigma}$ and the parameters of exchange interactions, which depend on $\Delta\hat{\Sigma}$ and $\hat{G}^\downarrow(\omega)$. Nevertheless, at least we should be able to evaluate the DE interactions, which do not depend on $\Delta\hat{\Sigma}$.

However, somewhat surprisingly, we have obtained very curious, but unphysical results: the correlation interactions, treated in RPA with the static effective potential, tend to additionally stabilize the orbital ordering and increase the orbital polarization, leading to the insulating solution, which is shown in Fig. 10. The reason for such unphysical behavior is related to the additional stabilization of the correlation energy in RPA by the hybridization between occupied and unoccupied orbitals across the Fermi level, which is activated in the insulating state (more details can be found in the Appendix).

The kinetic energy (without the energy of the crystal field splitting), obtained in the OEP method, is only $-168.57$ meV per formula unit and corresponding parameters of DE interactions can be estimated as $J_1^{(1)} = 3.80$ meV and $J_2^{(1)} = 8.74$ meV. Thus, the DE interactions are strongly underestimated in the insulating ground state of the OEP method.

![](./images/814591350367322112_10.jpg)

FIG. 10. (Color online) Electronic band structure of $\text{CrO}_2$, obtained in the OEP approach: (Left) Total and partial densities of states of three $t_{2g}$ orbitals and (right) band dispersion along high-symmetry directions of the BZ (notations of the high-symmetry points are taken from [55]) The Fermi level is at zero energy.

## IV. SUMMARY AND CONCLUSIONS

We have presented results of detailed theoretical analysis of the behavior of interatomic exchange interactions in $\text{CrO}_2$, which was based on the solution of realistic low-energy model, derived from the first-principles electronic structure calculations, and has involved various techniques for treating the electron correlations in the narrow $t_{2g}$ band, ranging from the static HF approximation to the DMFT. Such analysis allowed us to elucidate different contributions to the exchange couplings and understand the origin of these contributions on the microscopic level. Despite practical importance and broad interest to the HM ferromagnetism in $\text{CrO}_2$, the problem was far from being fully understood. There are several reasons for this.

First, there is no single microscopic mechanism, which is primarily responsible for the ferromagnetism of $\text{CrO}_2$. Our analysis clearly shows that it is a joint effect of several contributions, of very different origin, and besides conventional DE in the $t_{2g}$ band, there are other magnetic interactions, which are equally important in stabilizing the FM ground state in $\text{CrO}_2$. They include direct exchange interactions, the interactions between $t_{2g}$ and magnetically polarized oxygen $2p$ band, as well as higher-order contributions in the $(\Delta\hat{\Sigma})^{-1}$ expansion for the magnetic energy.

Second, the description of interatomic exchange interactions in $\text{CrO}_2$ may have many traps, because the behavior of these interactions strongly depends on the method in use, which may lead to different conclusions. Particularly, if one sticks to static methods, which totally neglect the effect of correlation interactions on the magnetic properties (such as the unrestricted HF approximation), the solution of the problem may look very easy and the robust HM ferromagnetism emerges already in the minimal model for the $t_{2g}$ bands. However, this "easy solution" appears to be largely incomplete, as it becomes clear after considering the correlation interactions. Moreover, one should be most careful with the use of additional approximations for treating the correlation interactions, because some of these approximations may lead to unphysical results. For instance, somewhat surprisingly, by using the RPA for the correlation energy and treating this problem in the spirit of the OEP method with some static local potential, we have obtained the insulating ground state for $\text{CrO}_2$, which suppresses the tendencies towards the ferromagnetism. This curious example demonstrates the importance of dynamic correlations.

The most reliable technique for dealing with this kind of problem is the DMFT. In the present work, we have employed the new realization of this method, which is based on the ED solution of the quantum impurity problem, performed "on-the-fly." The use of this numerically advanced algorithm enabled us not only to solve the standard DMFT equations, but also to study in many details the behavior of interatomic exchange interactions. Our study provides an important insight into the origin of HM ferromagnetism in $\text{CrO}_2$. It clearly shows that, besides conventional processes, related to the change of the kinetic energy of electrons in the $t_{2g}$ band, the realistic microscopic model for $\text{CrO}_2$ should also include the direct

exchange interactions and the magnetic polarization of the oxygen $2p$ band. Finally, we have proposed how the latter two contributions can be evaluated using results of electronic structure calculations in the LSDA. In this regard, we would like to emphasize two points: (i) Although we consider the new contributions of the oxygen $2p$ band, there is still the possibility to formulate this problem in the Hilbert space of the original $t_{2g}$ model, but with some additional interactions. In the present work, we have demonstrated how this can be done by using the SCLR theory, which allows us to treat the magnetic polarization of the oxygen $2p$ band as the response to the change of the magnetization density in the $t_{2g}$ band. Moreover, the direct interactions are also formulated in the basis of the $t_{2g}$ states. Of course, a more straightforward way for treating this problem is to expand the model by explicitly including into the model the oxygen $2p$ and all Cr $3d$ states. (ii) All-electron LSDA, although largely oversimplifying the problem of on-site electron correlations, takes into account other important ingredients, which are responsible for the stability of the FM ground state. We believe that this fact partly explains the success of LSDA in the description of CrO$_2$ [11].

In conclusion, our work provides the firm microscopic basis for understanding the magnetic properties of CrO$_2$, the canonical and technologically important half-metallic ferromagnet.

## ACKNOWLEDGMENT
This work is partly supported by a grant from Russian Science Foundation (Project No. 14-12-00306).

## APPENDIX: DETAILS OF THE OEP METHOD
The OEP procedure was implemented for the solution of the minimal model for the $t_{2g}$ band [67]. Here we assume that the one-electron band structure is half-metallic and all minority-spin states are unoccupied. Therefore, we drop the spin indices, but keep in mind that both the potential and the electronic structure are referred to the $\uparrow$-spin states. Then, because of the symmetry, the potential matrix is diagonal $\hat{v} = [v_{ab}\delta_{\tau\tau'}\delta_{ab}]$ and does not depend on the indices $\tau = 1$ or 2 of the Cr-atoms in the primitive cell. Therefore, the effective potential has only two independent parameters (apart from the constant energy shift): $\Delta_{2-1} = v_{22} - v_{11}$ and $\Delta_{3-2} = v_{33} - v_{22}$. Note also that the eigenvector $|c_{n\mathbf{k}}\rangle$ in Eq. (18) is the row-vector of the form $|c_{n\mathbf{k}}\rangle = [c_{n\mathbf{k}}^{a\tau}]$.

The correlation energy can be evaluated in RPA as [68,69]
$$
\begin{aligned}
E_{\text{corr}} =& \frac{1}{4\pi} \sum_{\mathbf{q}} \int_{0}^{\infty} d\omega \text{Tr}\{\ln[1 - \hat{P}(i\omega,\mathbf{q})\hat{U}] \\
& \times [1 - \hat{U}\hat{P}(i\omega,\mathbf{q})] + 2\hat{P}(i\omega,\mathbf{q})\hat{U}\}, \quad \text{(A1)}
\end{aligned}
$$
where $\hat{U}$ is the matrix $[U_{abcd}]$ of the on-site Coulomb interaction and $\hat{P} = [P_{abcd}^{\tau\tau'}]$ is the polarization in the imaginary frequency:
$$
\begin{aligned}
P_{abcd}^{\tau\tau'}(i\omega,\mathbf{q}) =& \sum_{n}^{\text{occ}} \sum_{n'}^{\text{unocc}} \sum_{\mathbf{k}} \frac{2(\varepsilon_{n\mathbf{k}} - \varepsilon_{n'\mathbf{k}+\mathbf{q}})}{\omega^{2} + (\varepsilon_{n\mathbf{k}} - \varepsilon_{n'\mathbf{k}+\mathbf{q}})^{2}} \\
& \times c_{n'\mathbf{k}+\mathbf{q}}^{a\tau *}c_{n\mathbf{k}}^{b\tau}c_{n\mathbf{k}}^{c\tau' *}c_{n'\mathbf{k}+\mathbf{q}}^{d\tau'}. \quad \text{(A2)}
\end{aligned}
$$

![](./images/814591350367322112_11.jpg)

FIG. 11. (Color online) Results of energy minimization in the OEP method versus the splitting in the potential between atomic levels 3 and 2: the HF part of the energy $E_{\text{HF}} = E_{\text{kin}} + E_{\text{C}} + E_{\text{X}}$, the correlation energy $E_{\text{corr}}$, and the total energy $E = E_{\text{HF}} + E_{\text{corr}}$.

The matrix multiplication in Eq. (A1) implies the summation over two intermediate orbital indices: $(\hat{U}\hat{P})_{abcd}^{\tau\tau'} \equiv \sum_{ef} U_{abef} P_{efcd}^{\tau\tau'}$ and the $\omega$ integration has been performed using a ten-point Gaussian quadrature method [69].

The example of minimization of the total energy with respect to $\Delta_{3-2}$ is shown in Fig. 11. The most unusual aspect is that, even when the HF energy $E_{\text{HF}} = E_{\text{kin}} + E_{\text{C}} + E_{\text{X}}$ reaches its minimum, $E_{\text{corr}}$ continues to decrease as a function of $\Delta_{3-2}$. Obviously, $E_{\text{corr}}$ decreases when the polarization decreases (note that $\hat{P}$ is the negative-defined matrix in the imaginary frequency). Then, there are two competing effects. On the one hand, the additional splitting of orbitals 2 and 3 across the Fermi level is expected to suppress the correlation interactions. This is a rather general property of correlation energy, which follows from the perturbation theory analysis [70]. If there were no transfer integrals, connecting orbitals 2 and 3, the effect of $\Delta_{3-2}$ would be equivalent to the scissors operator and the behavior of $E_{\text{corr}}$ would be totally described by the above-mentioned mechanism (which indeed dominates for large $\Delta_{3-2}$). Nevertheless, the strong hybridization between orbitals 2 and 3 [see Eq. (4)] may change this canonical behavior. First, we note that, in order to produce a large contribution to $E_{\text{corr}}$, one should activate the channels involving the large Coulomb matrix elements $U_{aacc}$ (where $a$ and $c$ are 2 or 3). This can be done only if the polarization matrix has sizable elements of the same $P_{aacc}$ type [see Eq. (A1)]. Such matrix elements are indeed produced by the hybridization effects in the insulating state [see Eq. (A2)]: Because of the hybridization, the orbital 3 may have a substantial weight in the occupied part of the spectrum (so as the orbital 2 in the unoccupied part), yielding finite matrix elements $P_{aacc}$. Thus, we believe that the decreasing of $E_{\text{corr}}$ in

Fig. 11 is a specific property of $CrO_2$ and related to the strong hybridization between occupied and unoccupied orbitals in the orbitally polarized state. Nevertheless, such a behavior is, of course, unphysical and this example demonstrates again the importance of explicit consideration of dynamic correlations.

[1] R. Skomski and J. M. D. Coey, *Permanent Magnetism* (Taylor & Francis, New York, 1999).

[2] R. Skomski, *Simple Models of Magnetism* (Oxford University Press, Oxford, UK, 2008).

[3] K. Schwarz, $CrO_2$ predicted as a half-metallic ferromagnet, J. Phys. **F 16**, L211 (1986).

[4] R. A. de Groot, F. M. Mueller, P. G. van Engen, and K. H. J. Buschow, New Class of Materials: Half-Metallic Ferromagnets, Phys. Rev. Lett. **50**, 2024 (1983).

[5] R. J. Soulen, Jr., J. M. Byers, M. S. Osofsky, B. Nadgorny, T. Ambrose, S. F. Cheng, P. R. Broussard, C. T. Tanaka, J. Nowak, J. S. Moodera, A. Barry, and J. M. D. Coey, Measuring the spin polarization of a metal with a superconducting point contact, Science **282**, 85 (1998).

[6] A. Singh, S. Voltan, K. Lahabi, and J. Aarts, Colossal Proximity Effect in a Superconducting Triplet Spin Valve Based on the Half-Metallic Ferromagnet $CrO_2$, Phys. Rev. X **5**, 021019 (2015).

[7] M. I. Katsnelson, V. Yu. Irkhin, L. Chioncel, A. I. Lichtenstein, and R. A. de Groot, Half-metallic ferromagnets: From band structure to many-body effects, Rev. Mod. Phys. **80**, 315 (2008).

[8] P. I. Sorantin and K. Schwarz, Chemical bonding in rutile-type compounds, Inorg. Chem. **31**, 567 (1992).

[9] S. P. Lewis, P. B. Allen, and T. Sasaki, Band structure and transport properties of $CrO_2$, Phys. Rev. B **55**, 10253 (1997).

[10] M. A. Korotin, V. I. Anisimov, D. I. Khomskii, and G. A. Sawatzky, $CrO_2$: A Self-Doped Double Exchange Ferromagnet, Phys. Rev. Lett. **80**, 4305 (1998).

[11] I. I. Mazin, D. J. Singh, and C. Ambrosch-Draxl, Transport, optical, and electronic properties of the half-metal $CrO_2$, Phys. Rev. B **59**, 411 (1999).

[12] A. Yamasaki, L. Chioncel, A. I. Lichtenstein, and O. K. Andersen, Model Hamiltonian parameters for half-metallic ferromagnets NiMnSb and $CrO_2$, Phys. Rev. B **74**, 024419 (2006).

[13] L. Chioncel, H. Allmaier, E. Arrigoni, A. Yamasaki, M. Daghofer, M. I. Katsnelson, and A. I. Lichtenstein, Half-metallic ferromagnetism and spin polarization in $CrO_2$, Phys. Rev. B **75**, 140406(R) (2007).

[14] L. Craco, M. S. Laad, and E. Müller-Hartmann, Orbital Kondo Effect in $CrO_2$: A Combined Local-Spin- Density-Approximation Dynamical-Mean-Field-Theory Study, Phys. Rev. Lett. **90**, 237203 (2003).

[15] M. S. Laad, L. Craco, and E. Müller-Hartmann, Orbital correlations in the ferromagnetic half-metal $CrO_2$, Phys. Rev. B **64**, 214421 (2001).

[16] P. Schlottmann, Double-exchange mechanism for $CrO_2$, Phys. Rev. B **67**, 174419 (2003).

[17] C. Zener, Interaction between the d shells in the transition metals, Phys. Rev. **81**, 440 (1951).

[18] P. W. Anderson and H. Hasegawa, Considerations on double exchange, Phys. Rev. **100**, 675 (1955).

[19] P.-G. de Gennes, Effects of double exchange in magnetic crystals, Phys. Rev. **118**, 141 (1960).

[20] E. Dagotto, T. Hotta, and A. Moreo, Colossal magnetoresistant materials: The key role of phase separation, Phys. Rep. **344**, 1 (2001).

[21] I. V. Solovyev and K. Terakura, in *Electronic Structure and Magnetism of Complex Materials*, edited by D. J. Singh and D. A. Papaconstantopoulos (Springer, Berlin, 2003).

[22] I. V. Solovyev and K. Terakura, Zone Boundary Softening of the Spin-Wave Dispersion in Doped Ferromagnetic Manganites, Phys. Rev. Lett. **82**, 2959 (1999).

[23] P. W. Anderson, New approach to the theory of superexchange interactions, Phys. Rev. **115**, 2 (1959).

[24] T. Oguchi, K. Terakura, and A. R. Williams, Band theory of the magnetic interaction in MnO, MnS, and NiO, Phys. Rev. B **28**, 6443 (1983).

[25] P. Mahadevan, I. V. Solovyev, and K. Terakura, Low- temperature spin dynamics of doped manganites: Roles of Mn $t_{2g}$, Mn $e_g$, and O $2p$ states, Phys. Rev. B **60**, 11439 (1999).

[26] W. Ku, H. Rosner, W. E. Pickett, and R. T. Scalettar, Insulat- ing Ferromagnetism in $La_4Ba_2Cu_2O_{10}$: An *ab initio* Wannier Function Analysis, Phys. Rev. Lett. **89**, 167204 (2002).

[27] V. V. Mazurenko, S. L. Skornyakov, A. V. Kozhevnikov, F. Mila, and V. I. Anisimov, Wannier functions and exchange integrals: The example of $LiCu_2O_2$, Phys. Rev. B **75**, 224408 (2007).

[28] H. Sims, S. J. Oset, W. H. Butler, J. M. MacLaren, and M. Marsman, Determining the anisotropic exchange coupling of $CrO_2$ via first-principles density functional theory calculations, Phys. Rev. B **81**, 224436 (2010).

[29] I. V. Solovyev and K. Terakura, Effective single-particle poten- tials for MnO. in light of interatomic magnetic interactions: Existing theories and perspectives, Phys. Rev. B **58**, 15496 (1998).

[30] I. V. Solovyev, Combining DFT and many-body methods to understand correlated materials, J. Phys.: Condens. Matter **20**, 293201 (2008).

[31] P. Porta, M. Marezio, J. P. Remeika, and P. D. Dernier, Chromium dioxide: High pressure synthesis and bond lengths, Mater. Res. Bull. **7**, 157 (1972).

[32] O. K. Andersen, Linear methods in band theory, Phys. Rev. B **12**, 3060 (1975).

[33] O. Gunnarsson, O. Jepsen, and O. K. Andersen, Self-consistent impurity calculations in the atomic-spheres approximation, Phys. Rev. B **27**, 7144 (1983).

[34] O. K. Andersen, Z. Pawlowska, and O. Jepsen, Illustration of the linear-muffin-tin-orbital tight-binding representation: Compact orbitals and charge density in Si, Phys. Rev. B **34**, 5253 (1986).

[35] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.92.144407 for technical details of the ASA- LMTO calculations and corresponding electronic structure of $CrO_2$ in comparison with results of full-potential calculations.

[36] N. Marzari, A. A. Mostofi, J. R. Yates, I. Souza, and D. Vanderbilt, Maximally localized Wannier functions: Theory and applications, Rev. Mod. Phys. **84**, 1419 (2012).

[37] All model parameters are available upon request.

[38] J. C. Slater and G. F. Koster, Simplified LCAO method for the periodic potential problem, Phys. Rev. 94, 1498 (1954).

[39] F. Aryasetiawan, M. Imada, A. Georges, G. Kotliar, S. Biermann, and A. I. Lichtenstein, Frequency-dependent local interactions and low-energy effective models from electronic structure calculations, Phys. Rev. B 70, 195104 (2004).

[40] J. Kanamori, Electron correlation and ferromagnetism of transition metals, Prog. Theor. Phys. 30, 275 (1963).

[41] I. V. Solovyev, Self-consistent linear response for the spin-orbit interaction related properties, Phys. Rev. B 90, 024417 (2014).

[42] A. Georges, G. Kotliar, W. Krauth, and M. J. Rozenberg, Dynamical mean-field theory of strongly correlated fermion systems and the limit of infinite dimensions, Rev. Mod. Phys. 68, 13 (1996).

[43] ARPACK software, http://www.caam.rice.edu/software/ARPACK/.

[44] I. V. Kashin and V. V. Mazurenko, On-the-fly exact diagonalization solver for quantum electronic models, arXiv:1508.04895.

[45] V. V. Mazurenko, S. N. Iskakov, A. N. Rudenko, I. V. Kashin, O. M. Sotnikov, M. V. Valentyuk, and A. I. Lichtenstein, Correlation effects in insulating surface nanostructures, Phys. Rev. B 88, 085112 (2013).

[46] X. Wang, H. T. Dang, and A. J. Millis, High-frequency asymptotic behavior of self-energies in quantum impurity models, Phys. Rev. B 84, 073104 (2011).

[47] A. I. Liechtenstein, M. I. Katsnelson, V. P. Antropov, and V. A. Gubanov, Local spin density functional approach to the theory of exchange interactions in ferromagnetic metals and alloys, J. Magn. Magn. Mater. 67, 65 (1987).

[48] M. I. Katsnelson and A. I. Lichtenstein, First-principles calculations of magnetic interactions in correlated systems, Phys. Rev. B 61, 8906 (2000).

[49] K. I. Kugel and D. I. Khomskii, The Jahn-Teller effect and magnetism: Transition metal compounds, Sov. Phys. Usp. 25, 231 (1982).

[50] I. V. Solovyev and K. Terakura, Spin canting in three-dimensional perovskite manganites, Phys. Rev. B 63, 174425 (2001).

[51] L. M. Sandratskii, Noncollinear magnetism in itinerant-electron systems: Theory and applications, Adv. Phys. 47, 1 (1998).

[52] S. V. Tyablikov, Methods of Quantum Theory of Magnetism (Nauka, Moscow, 1975).

[53] V. Heine and J. H. Samson, Theory of some physical properties and competing processes in tight-binding bands, J. Phys. F 10, 2609 (1980).

[54] V. Heine and J. H. Samson, Magnetic, chemical and structural ordering in transition metals, J. Phys. F 13, 2155 (1983).

[55] C. J. Bradley and A. P. Cracknell, The Mathematical Theory of Symmetry in Solids (Clarendon, Oxford, 1972).

[56] P. Sun and G. Kotliar, Extended dynamical mean-field theory and GW method, Phys. Rev. B 66, 085120 (2002).

[57] T. Ayral, S. Biermann, and P. Werner, Screening and nonlocal correlations in the extended Hubbard model from self-consistent combined GW and dynamical mean field theory, Phys. Rev. B 87, 125149 (2013).

[58] O. Gunnarsson, Band model for magnetism of transition metals in the spin-density-functional formalism, J. Phys. F 6, 587 (1976).

[59] W. Heisenberg, Zur theorie des ferromagnetismus, Z. Phys. 49, 619 (1928).

[60] I. Solovyev, Long-range magnetic interactions induced by the lattice distortions and the origin of the E-type antiferromagnetic phase in the undoped orthorhombic manganites, J. Phys. Soc. Jpn. 78, 054710 (2009).

[61] J. D. Talman and W. F. Shadwick, Optimized effective atomic central potential, Phys. Rev. A 14, 36 (1976).

[62] T. Kotani and H. Akai, KKR-ASA method in exact exchange-potential band-structure calculations, Phys. Rev. B 54, 16502 (1996).

[63] T. Kotani, An optimized-effective-potential method for solids with exact exchange and random-phase approximation correlation, J. Phys.: Condens. Matter 10, 9241 (1998).

[64] E. Engel and R. N. Schmid, Insulating Ground States of Transition-Metal Monoxides from Exact Exchange, Phys. Rev. Lett. 103, 036404 (2009).

[65] H. Grabo and E. K. U. Gross, The optimized effective potential method of density functional theory: Applications to atomic and molecular systems, Int. J. Quantum Chem. 64, 95 (1997).

[66] W. Kohn and L. J. Sham, Self-consistent equations including exchange and correlation effects, Phys. Rev. 140, A1133 (1965).

[67] I. V. Solovyev, Optimized effective potential model for the double perovskites $Sr_{2-x}Y_xVMoO_6$ and $Sr_{2-x}Y_xVTcO_6$, J. Phys. Condens. Matter 23, 326002 (2011).

[68] D. Pines, Elementary Excitations in Solids (Westview, Oxford, 1999).

[69] F. Aryasetiawan, T. Miyake, and K. Terakura, Total Energy Method from Many-Body Formulation, Phys. Rev. Lett. 88, 166401 (2002).

[70] J. Callaway, Correlation energy in a model semiconductor, Phys. Rev. 116, 1368 (1959).

144407-15