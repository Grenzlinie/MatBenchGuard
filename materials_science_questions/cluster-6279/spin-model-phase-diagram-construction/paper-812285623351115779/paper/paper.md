Z. Phys. B - Condensed Matter 66, 227-235 (1987)
![](./images/812285623351115779_1.jpg)

# The Bethe Approximation to the Three-State Chiral Clock Model

M. Siegert and H.U. Everts

Institut für Theoretische Physik, Universität Hannover, Federal Republic of Germany

Received October 3, 1986

The three-state chiral clock model is studied by means of the Bethe approximation. While the phase diagram obtained by this method resembles the mean-field phase diagram in the vicinity of the boundary to the paramagnetic phase, a significant improvement is achieved in the low and intermediate temperature regions: By a low-temperature expan- sion of the free energy, which is carried out to third order, we find that, up to this order, the Bethe approximation exactly reproduces the results of the low-temperature analysis of the full model by Yeomans and Fisher. This and the numerical evaluation of the free energy show that, as far as the longer wavelength phases are concerned, the Bethe approximation is in keeping with predictions of Yeomans and Fisher for low temperature, where mean-field theory is qualitatively misleading. At higher tempera- tures more complicated structures are found to evolve from the basic low-temperature phases by structure combination branching processes in the same fashion as in the phase diagram of the ANNNI model.

## I. Introduction

In many crystalline solids that exhibit long-wave- length uniaxially modulated phases the modulation pattern is found to change in a systematic fashion, as the external parameters are varied [1]. Sequences of ten or more phases of this kind have been observed in different classes of materials such as magnets [2], ferroelectrics [3] and metallic alloys [4]. It appears to be the accepted view that this behaviour results from competing short-range interactions between the entitities of the crystals along one lattice direction (axial direction). Two lattice models have repeatedly been investigated in this context: the axial next-near- est neighbour Ising (ANNNI) model [5] and the three-state chiral clock $(CC_{3})$ model [6]. Owing to the competing interactions both models exhibit a mul- tiphase point at T=0 from which an infinite sequence of distinct modulated phases evolves. Various differ- ent techniques have been invoked to explore in detail the phase diagrams of these models [7-17]. While a coherent picture of the entire phase diagram of the ANNNI model has emerged from these analyses, theyhave led to conflicting results in the case of the $CC_{3}$  model: By a low- T expansion Yeomans and Fisher(YF) [13] predicted that most of the phases that spring from the multiphase point of the $CC_{3}$ model vanish at certain cutoff temperatures. At higher tem- peratures the phase diagram of the $CC_{3}$ model should thus be much less rich in structure than that of the ANNNI model, for which no cutoffs were found [7]. Mean-field (MF) theory [15], on the other hand, pro- duces essentially the same structure for the phase dia- grams of both models at higher temperatures. In pre- vious work [17], the present authors observed, how- ever, that at low temperatures the MF-phase diagram differs qualitatively from the results of YF. Recently, Szpilka and Fisher [14] have uncovered the reason for this discrepancy. Their work implies that while MF-theory may yield a qualitatively correct picture of the entire phase diagram of the ANNNI model, it is qualitatively misleading for the $CC_{3}$ model, at least in the low-temperature region, where the YF expansion applies.

In this paper the phase diagram of the $CC_{3}$ model will be explored by means of the Bethe approxima- tion. The latter is known to improve on the MF ap- proximation: In addition to the mean field the nearest

neighbour correlations are regarded as independent variables in the variational free energy. The method will be outlined in the next section. In Sect. III we present and discuss the phase diagram of the $\mathrm{CC}_{3}$ model obtained by a numerical evaluation of the Bethe approximation. Within our numerical accura- cy it is found to agree with the results of YF at low temperatures. Contrary to the prediction of YF, how- ever, a rich phase structure is seen to develop from the basic low-temperature phases at higher tempera- tures by structure combination branching processes [10]. A systematic low-$T$ expansion of the Bethe ap- proximation is developed in Sect. IV. To third order this expansion is found to agree exactly with the YF expansion. By comparising the numerical results and the low-$T$ series expansion of the Bethe approxima- tion we measure the rate of convergence of the latter. The concluding Sect. V contains a short summary of this paper. Technical details pertaining to Sect. II have been deferred to Apps. A, B.

## II. The Model and the Bethe Approximation

The three-state chiral clock $(\mathrm{CC}_{3})$ model on a three dimensional layered lattice is defined by the Hamil- tonian

$$
H=-J_{0} \sum_{\alpha=1}^{N} \sum_{\langle k, l\rangle} \mathbf{S}_{k \alpha} \mathbf{S}_{l \alpha}-J \sum_{\alpha=1}^{N} \sum_{k} \mathbf{S}_{k \alpha} \hat{R}(\Delta) \mathbf{S}_{k \alpha+1} \quad(1)
$$

where

$$
\mathbf{S}_{k \alpha}=\left(\cos 2 \pi n_{k \alpha} / 3, \sin 2 \pi n_{k \alpha} / 3\right), \quad n_{k \alpha}=0,1,2 \quad(2)
$$

is a three-state spin variable. In each layer $\alpha$ nearest neighbour (n.n.) spin pairs interact ferromagnetically, $J_{0}>0$. The operator

$$
\hat{R}(\Delta)=\left(\begin{array}{cc}
\cos 2 \pi \Delta / 3 & \sin 2 \pi \Delta / 3 \\
-\sin 2 \pi \Delta / 3 & \cos 2 \pi \Delta / 3
\end{array}\right), \quad 0 \leqq \Delta \leqq 1 \quad \text { (3) }
$$

rotates the spins through the angle $2 \pi \Delta / 3$. Thus, with $J>0$ the inter-layer coupling favours ferromagnetic ordering among the layers, if $0 \leqq \Delta<1 / 2$, and right handed chiral ordering $\left(n_{k \alpha+1}=n_{k \alpha}+1\right)$, if $1 / 2<\Delta \leqq 1$. $\Delta=1 / 2$ is a multiphase point: All sequences of ferro- magnetically aligned layers, that correspond to se- quences $\left\{n_{k \alpha}\right\}$ such that

$$
n_{k \alpha+1}=n_{k \alpha} \quad \text { or } \quad n_{k \alpha+1}=n_{k \alpha}+1, \quad \alpha=1, \ldots N \quad \text { (4) }
$$

are degenerate ground states of the model at that point. The partition function of the $\mathrm{CC}_{3}$ model is invariant under the transformation

$$
\Delta \rightarrow \Delta^{\prime}=1-\Delta,
$$

$$
\mathbf{S}_{k \alpha} \rightarrow \mathbf{S}_{k \alpha}^{\prime}=\hat{R}^{T}(\alpha) \hat{M} \mathbf{S}_{k \alpha},
$$

where $\hat{R}^{T}$ is the transpose of $\hat{R}$ and

$$
\hat{M}=\left(\begin{array}{cc}
1 & 0 \\
0 & -1
\end{array}\right) \text {. }
$$

Owing to this symmetry the phase diagram is mirror symmetric with respect to the line $\Delta=1 / 2$ in the $\Delta$-$T$ plane. The phases to the right and to the left of this line are related by (5b) so that it suffices to consider either half of the phase diagram.

In the general frame of cluster variation methods for lattice systems [18] the Bethe approximation is the first step beyond the MF approximation. While in the latter the entropy is assumed to depend only on the probabilities of finding single spins in one of the accessible states, Bethe's approximation works with an entropy function that depends on the prob- abilities of finding single spins and n.n. spin pairs in one of the accessible states. The construction of this entropy function is the crucial step of the approxima- tion. For the case of Ising models with n.n. interac- tions this construction is explained in detail in [19]. Its extension to the ANNNI model has been devised by Taylor and Desjardin [11]. Their construction ap- plies almost literally to the $\mathrm{CC}_{3}$ model so that we need not repeat it here. (Our notation follows closely that of [11].)

The entropy function is

$$
S=\sum_{\alpha=1}^{N}(5 E(\alpha)-2 Y(\alpha)-U(\alpha))
$$

with

$$
E(\alpha)=\sum_{i=0}^{2} e_{i}(\alpha) \ln e_{i}(\alpha)
$$

$$
Y(\alpha)=\sum_{i=0}^{2} y_{i}(\alpha) \ln y_{i}(\alpha)+2 \sum_{i=3}^{5} y_{i}(\alpha) \ln y_{i}(\alpha)
$$

$$
U(\alpha)=\sum_{i=0}^{8} u_{i}(\alpha) \ln u_{i}(\alpha)
$$

Here $e_{i}(\alpha), i=0,1,2$, are the probabilities of finding a spin of the $\alpha$-th layer in one of the three possible states (2). $y_{i}(\alpha)$ are the probabilities of finding a n.n. spin pair of the $\alpha$-th layer in one of the possible states as listed in Table 1. Due to an obvious reflection sym- metry there are only six independent probabilities $y_{i}(\alpha)$. Similarly, $u_{i}(\alpha)$ are the probabilities of finding a spin pair on an intra-layer bound stretching be- tween the $\alpha$-th and the $(\alpha+1)$-st layer in one of the nine states. Since the equilibrium states of the model are expected to be homogeneous in each layer, all of these probabilities are assumed to be independent

<table><caption>Table 1. Probabilities of spin-pair states. The numbers in the first line are the values of $n_{k \alpha}$ (cf. (2))</caption>
<tbody><tr><td>Pair state</td><td>0-0</td><td>1-1</td><td>2-2</td><td>0-1</td><td>1-2</td><td>2-0</td><td>0-2</td><td>1-0</td><td>2-1</td></tr>
<tr><td>Probability (in-layer)</td><td>$y_0$</td><td>$y_1$</td><td>$y_2$</td><td>$y_3$</td><td>$y_5$</td><td>$y_4$</td><td>$y_4$</td><td>$y_3$</td><td>$y_5$</td></tr>
<tr><td>Probability (intra-layer)</td><td>$u_0$</td><td>$u_1$</td><td>$u_2$</td><td>$u_3$</td><td>$u_4$</td><td>$u_5$</td><td>$u_6$</td><td>$u_7$</td><td>$u_8$</td></tr>
</tbody></table>

of the in-layer positions of the objects to which they refer.

The variables $e_{i}(\alpha), y_{i}(\alpha)$ and $u_{i}(\alpha)$ are not independent. Normalization requires, e.g., that

$$
\sum_{i=0}^{2} e_{i}(\alpha)=1. \quad (7)
$$

This condition can be satisfied by introducing the components $m_{1}, m_{2}$ of the layer magnetization,

$$
\left\langle\mathbf{S}_{k \alpha}\right\rangle=\mathbf{M}(\alpha)=\left(m_{1}(\alpha), m_{2}(\alpha)\right), \quad (8)
$$

as independent variables:

$$
e_{0}(\alpha)=\left(1+2 m_{1}(\alpha)\right) / 3, \quad (9 \mathrm{a})
$$

$$
e_{1(2)}(\alpha)=\left(1-m_{1}(\alpha)+\sqrt{3} m_{2}(\alpha)\right) / 3. \quad (9 \mathrm{~b}, \mathrm{c})
$$

The conditions imposed on the probabilities $y_{i}, u_{i}$ by normalization are listed in App. A, where also the remaining independent variables $f_{i}(\alpha), i=0,1,2$ and $g_{i}(\alpha), i=0,..., 3$ are defined. Thus in total we have nine independent variables per layer.

The energy of the model (1) is immediately expressed in terms of the $y$'s and $u$'s:

$$
\begin{aligned}
E= & -J_{0} \sum_{\alpha}\left\{2 \sum_{i=0}^{2} y_{i}(\alpha)-2 \sum_{i=3}^{5} y_{i}(\alpha)\right\} \\
& -J \sum_{\alpha}\left\{\cos \frac{2 \pi}{3} \Delta \sum_{i=0}^{2} u_{i}(\alpha)+\cos \frac{2 \pi}{3}(1-\Delta) \sum_{i=3}^{5} u_{i}(\alpha)\right. \\
& \left.+\cos \frac{2 \pi}{3}(1+\Delta) \sum_{i=6}^{8} u_{i}(\alpha)\right\}.
\end{aligned}
$$

Equations (6) and (10) yield the free energy function

$$
F(\{e\},\{y\},\{u\})=E-T S \quad (11)
$$

of Bethe's approximation.

The MF free energy is recovered from (11), if one factorizes the spin pair probabilities in terms of the $e_{i}$ in a manner that is obvious from Table 1,

$$
y_{i}(\alpha)=e_{1}^{2}(\alpha), \quad i=0,1,2, \quad y_{3}=e_{1}(\alpha) e_{2}(\alpha) \text { etc., (12) }
$$

and then replaces the $e_{i}$ by the layer magnetization $\mathbf{M}(\alpha)$ using $(9 \mathrm{a}-\mathrm{c})$.

Our aim is to determine for any given pair of parameters $K \equiv J / T, \Delta$ (we assume $J=J_{0}$ henceforth) that magnetization pattern $\mathbf{M}(\alpha)$ which minimizes the free energy (11). For a pattern of period $s$ in the axial direction we thus have to minimize (11) with respect to the $9 \cdot s$ independent variables $m_{i}(\alpha), f_{i}(\alpha), g_{i}(\alpha), \alpha$ $=1,2,..., s$. The equilibrium conditions

$$
\partial F / \partial m_{i}(\alpha)=0, \quad \partial F / \partial f_{i}(\alpha)=0, \quad \partial F / \partial g_{i}(\alpha)=0 \quad (13)
$$

are given explicitly in App. B. We solved them by means of a Newton iteration procedure, which was devised such as to account for the constraints on the variables $m_{i}, f_{i}$ and $g_{i}$ that result from the natural constraints on the probabilities $e_{i}, y_{i}$ and $u_{i}$. By construction any solution of (13) found by this method is a true minimum of $F$ although not necessarily the absolute minimum. Symmetry considerations allow for a reduction in the number of independent variables from $9 s$ to $9 s / 2+2$ ( $s$ even) or $9(s+1) / 2-3$ ( $s$ odd) for a pattern of period $s$. This allowed us to evaluate patterns with periods $s \leqq 101$. To be able to exploit the above-mentioned symmetries one has of course to choose an appropriate set of initial values $m_{i o}(\alpha), f_{i o}(\alpha), g_{i o}(\alpha)$ for the Newton iteration. We obtained such a set by using for $m_{i o}(\alpha)$ the results of the first-order low-temperature expansion of the MF theory [17], which have the correct symmetries. Within MF-theory the initial values $f_{i o}(\alpha), g_{i o}(\alpha)$ of the remaining variables are determined by $m_{i o}(\alpha)$ (cf. Eqs. $(9 \mathrm{a}-\mathrm{c}),(12),(\mathrm{A} 3))$. Remarkably, with these initial values rapid convergence of the iteration is achieved for all temperatures up to the critical temperature:after about 20 steps the relative difference of the free energies obtained in successive steps is less than $10^{-13}$.

### III. Numerical Results

The phase diagram is obtained from the numerical calculations described in the previous section by selecting for a given region of the $\Delta$ - $T$-plane that magnetization which corresponds to the absolute minimum of the free energy. Figures $1 \mathrm{a}$ and $\mathrm{b}$ display the phase diagram resulting from the Bethe approximation and the MF phase diagram on a scale that emphasizes the structures in the vicinity of the order-disorder transition line. On this scale several, mostly quantitative differences between the two approximations appear: As expected the transition line to the ordered phases $T_{c}^{\text {Bethe }}(\Delta)$ falls below the MF transition line $T_{c}^{\mathrm{MF}}(\Delta)$. The transition to the ferromagnetic state is

![](./images/812285623351115779_2.jpg)

![](./images/812285623351115779_3.jpg)

Fig. 1a and b. Phase diagram of the $CC_3$ model in the vicinity of the critical temperature: a Bethe approximation, b Mean-field approximation.
Bold lines display first-order transitions; dotted lines: pinning temperature of the incommensurate structures. Commensurate phases are characterized by their wavenumbers (in units of $2\pi$)

p/s=12/83 T=2.235 Δ=0.4720
p/s=12/83 T=2.225 Δ=0.4720

![](./images/812285623351115779_4.jpg)

Fig. 2a and b. Moduli (|M|) and phases ($\varphi$) of the magnetizations of the ($q=2\pi\frac{12}{83}$)-orbit. a $T>T_{\text{pin}}$ b $T<T_{\text{pin}}$

found to be discontinuous in both approximations. The discontinuity of the magnetization $\Delta|M|$ is larger than 0.5 and weakly $\Delta$ dependent in the Bethe approximation while $\Delta|M|=0.5$ in MF theory. In the MF phase diagram the critical line ends in multicritical point $\Delta_{\text{mc}}=1/3$, $T_{\text{mc}}=3J$; for $\Delta<\Delta_{\text{mc}}$ discontinuous transitions to modulated phases occur [16, 17]. A Landau expansion of the Bethe free energy (11) yields the same type of behaviour for the critical line $T_{c}^{\text{Bethe}}(\Delta)$. The numerical analysis reveals, however, that the corresponding multicritical point lies within the ferromagnetic region and is thus of no relevance to the phase diagram. In particular no discontinuous transitions to modulated phases occur in the Bethe approximation.

The dotted lines represent the pinning temperature $T_{\text{pin}}(\Delta)$ below which incommensurate phases cease to exist due to pinning effects. Within the Bethe approximation $T_{\text{pin}}(\Delta)$ has been obtained by visual inspection of long period magnetization patterns that can be viewed as defected short period patterns the defects being domain walls. As has previously been

![](./images/812285623351115779_5.jpg)

Fig. 3. Low-temperature phase diagram of the Bethe approximation to the $CC_{3}$ model

explained [9,17] such structures are commensurate approximants to the truly incommensurate structures. An example is the pattern with wave number $q=2 \pi$
$$\frac{p}{s}=2 \pi \frac{12}{83} \text { which contains three walls within } p=12$$
windings of the $q=2 \pi \frac{1}{7}$ pattern. As shown in Fig. 2a, b this pattern develops discontinuities in the phase $\varphi$ and in the modulus $m$ of the magnetization $M$ $=m(q \alpha) \mathrm{e}^{\mathrm{i} \varphi(q \alpha)}$ at a certain temperature. The onset of these discontinuities indicates the onset of wall pin- ning [17] and can hence be used to identify $T_{pin }(\Delta)$ . There is of course no qualitative difference between the graphs of $T_{pin }(\Delta)$ derived from the two different approximations. Remarkably, however, the portion of the orderer region of the phase diagram occupied by incommensurate phases is found to be considera- bly larger in the Bethe approximation than in MF theory.

The important qualitative features by which the Bethe approximation deviates from MF theory in the case of the $CC_{3}$ model are depicted schematically in Fig. 3, which emphasizes the low-temperature part of the phase diagram. The phases are labeled by the sequences of equally oriented bands of which their periods consist [7]. In agreement with the prediction of the direct low- $T$ expansion of YF and in contrast to the MF results only phases with band structures $\langle 32^{n}\rangle,\langle 2^{n} 1\rangle, n=1,2,...$ and $\langle 2\rangle$ where found to exist in the immediate vicinity of the multicritical point $\Delta=0.5, T=0$ . At higher temperatures new lon ger period phases develop by a process that has pre-viously been observed by Selke and Duxbury [10] in the MF theory of the ANNNI model: Two adja- cent periodic structures $\langle A\rangle$ and $\langle B\rangle$ become unsta ble at a branching point $\Delta(A, B), T_{b}(A, B)$ against a new phase. The period of this new intervening phase is just the combination of the structures $A$ and $B$ . Several examples of such branching processes can be seen in Fig.(3). It would of course be interesting toknow the branching points of the $\langle 2^{n+1} 1\rangle:\langle 2^{n} 1\rangle$  phase boundaries for a sufficient number of $n$ -values so that one could decide whether $T_{b}(2^{n+1} 1: 2^{n} 1)$ tendsto zero, as the first two of these points in Fig.(3) seem to indicate. If this were the case the transition from $\langle 2\rangle$ -phase to any of the longer period phases would be quasi continuous at all temperatures. Also, one would like to know whether the points at which phases with successively longer band structures branch off a given phase accumulate and, if so, at which temperature $T_{ac}$ this happens. Unfortunately the calculations necessary to decide these questions are beyond the reach of computer accuracy (128 bits). In concluding this section we should like to emphasizethe similarity between the phase diagram of the $CC_{3}$  derived here from the Bethe approximation, Fig. 3, and the MF phase diagram of the ANNNI model as shown in Ref. [10]. It confirms the intuitive suppo- sition, that the physical process by which the longer period phases evolve from short period structures should be the same in both models.

## IV. Low-Temperature Expansion
The ground states of a $CC_{3}$ model with $N$ layers in the axial direction consist in all order parameter se- quences
$$\begin{aligned}
\mathbf{m}(\alpha)= & \left(\cos 2 \pi n_{\alpha} / 3, \sin 2 \pi n_{\alpha} / 3\right), \\
n_{\alpha}= & 0,1,2, \\
\alpha= & 1, \ldots, N
\end{aligned}\qquad(14)$$
 in which the integer variables $n_{\alpha}$ satisfy the restriction(4).
The corresponding sequences of probabilities $e_{i}(\alpha)$  are
$$\begin{aligned}
& e_{i}(\alpha)=\delta_{n_{\alpha}, i} \\
& n_{\alpha}, i=0,1,2, \quad \alpha=1, \ldots, N
\end{aligned}\qquad(15)$$
 with the same restrictions on the $n_{\alpha}$ .
At small but finite temperatures these probabili- ties will deviate from zero or unity by small quantities  +, _ which are conveniently defined in the follow-ing manner:
$$\xi_{+}(\alpha)=e_{i}(\alpha), \quad i=n_{\alpha}+1 \bmod 3 \quad(16 a)$$

$$\xi_{-}(\alpha)=e_{i}(\alpha), \quad i=n_{\alpha}-1 \bmod 3 \quad(16 b)$$

Normalization of the $e_{i}(\alpha),(7)$, requires that
$$1-\xi_{+}(\alpha)-\xi_{-}(\alpha)=e_{i}(\alpha), \quad i=n_{\alpha}\qquad(16c)$$

The linear relations of App. A and the equilibrium conditions (B1a-c, B2a-d) are then used to obtain power series expansions of the probabilities $y_{i}, u_{i}$ in terms of $\xi_{ \pm}$. Inserting these into the last two equilibrium conditions (B3a, b) one can solve these iteratively to obtain series expansions for $\xi_{ \pm}$:
$$\xi_{ \pm}(\alpha)=\xi_{ \pm}^{(1)}(\alpha)+\xi_{ \pm}^{(2)}(\alpha)+\ldots,\qquad(17)$$

From these series similar expansions for the probabilities $y_{i}$ and $u_{i}$ and thus, via (11), also for the free energy follow:
$$F=\sum_{\alpha=1}^{N}\left\{f^{(0)}(\alpha)+f^{(1)}(\alpha)+f^{(2)}(\alpha)+f^{(3)}(\alpha) \ldots\right\}.\qquad(18)$$

Here,
$$F^{(0)}=\sum_{\alpha} f^{(0)}(\alpha)=-\sum_{\alpha}\left\{2 J_{0}+J_{1}+\delta_{n_{\alpha+1}, n_{\alpha+1}} J_{1} \delta\right\} \quad(19)$$
with
$$\delta=\sqrt{3}(\tan 2 \pi \Delta / 3-\sqrt{3}) / 2 \text { and } J_{1}=J \cos 2 \pi \Delta / 3 \quad(20)$$
is the ground state energy.

The first-order results are as follows $(K_{0}=J_{0} / T$ , $K_{1}=J_{1} / T$ ; Boltzmann's constant is set equal to unitythroughout):
$$\xi_{ \pm}^{(1)}(\alpha)=\mathrm{e}^{-6 K_{0}} \mathrm{e}^{-\frac{3}{2} K_{1}(R(\alpha) \mp S(\alpha))}, \quad(21)$$
where
$$\begin{aligned}
R(\alpha)=\cos \frac{2 \pi}{3}\left(n_{\alpha+1}-n_{\alpha}\right) & +\cos \frac{2 \pi}{3}\left(n_{\alpha}-n_{\alpha-1}\right) \\
+\sqrt{3}(1+2 \delta / 3) & \left(\sin \frac{2 \pi}{3}\left(n_{\alpha+1}-n_{\alpha}\right)\right. \\
& \left.+\sin \frac{2 \pi}{3}\left(n_{\alpha}-n_{\alpha-1}\right)\right), \quad(22 \mathrm{a})
\end{aligned}$$

$$\begin{aligned}
S(\alpha)= & \left(\sin \frac{2 \pi}{3}\left(n_{\alpha+1}-n_{\alpha}\right)-\sin \frac{2 \pi}{3}\left(n_{\alpha}-n_{\alpha-1}\right)\right) / \sqrt{3} \\
& -(1+2 \delta / 3)\left(\cos \frac{2 \pi}{3}\left(n_{\alpha+1}-n_{\alpha}\right)\right. \\
& \left.-\cos \frac{2 \pi}{3}\left(n_{\alpha}-n_{\alpha-1}\right)\right), \quad(22 \mathrm{~b})
\end{aligned}$$

$$f^{(1)}(\alpha)=-\left(\xi_{+}(\alpha)+\xi_{-}(\alpha)+\xi_{-}(\alpha)\right) / T.\qquad(23)$$

Clearly, the magnitude of these first-order results is controlled by $e^{-6 K_{0}}$ . Note that they depend on a string of three integer variable spanning three succes- sive layers $(n_{\alpha-1}, n_{\alpha}, n_{\alpha+1})$ .

The higher order terms are too complicated to be presented here. We shall briefly describe their mainfeatures. The $r$ -the order term in the expansion (18)of the free energy, $f^{(r)}(\alpha)$ , depends on a string of $r+2$  integer variables $n_{\alpha}$ spanning $r+2$ layers. $f^{(2)}(\alpha)$ is a quadratic form in $\xi_{ \pm}^{(1)}(\alpha), \xi_{ \pm}^{(1)}(\alpha+1)$ , and $f^{(3)}(\alpha)$ is athird-order polynomial in $\xi_{ \pm}^{(1)}(\alpha-1), \xi_{ \pm}^{(1)}(\alpha), \xi_{ \pm}^{(1)}(\alpha+1)$  and $\xi_{ \pm}^{(2)}(\alpha)$ . The leading term in the second-order quantities $\xi_{ \pm}^{(2)}(\alpha)$ is of order $e^{-9 K_{0}}$ . Comparing this with the order of magnitude of $\xi_{ \pm}^{(1)}(\alpha)$ one might infer that the expansion (17) is a power series in $e^{-3 K_{0}}$ . Evidence against this inference will be given shortly.

To obtain the phase diagram within this low-tem- perature expansion one has to minimize the free ener- gy (18) over the set of integer variables $n_{\alpha}, \alpha=1,..., N$ under the constraint (4). As has previously been dem- onstrated [7, 13] this task is reduced to a linear pro- gramming problem by introducing structural vari- ables $l_{\{k_{i}\}}$ instead of the variables $n_{\alpha}$ . The free energy is linear in these variables. The zeroth and first-order contributions to $F$ , e.g., take the following form
$$\begin{aligned}
F^{(0)}+F^{(1)}= & \sum_{\alpha}\left\{f^{(0)}(\alpha)+f^{(1)}(\alpha)\right\} \\
= & N T\left\{\alpha_{0}^{(1)}(\delta)+a_{1}^{(1)}(\delta) l_{1}\right. \\
& \left.+\sum_{n=3}^{N}(n-2) a_{\infty}^{(1)}(\delta) l_{n}\right\}
\end{aligned}\qquad(24)$$

The structural variables $l_{k}$ are defined such that for a periodic structure comprising $N$ layers $N l_{k}$ is the number of $k$ -bands (i.e. strings of $k$ variables $n_{\alpha}$ with identical values) in that structure. The structural coef- ficients $a_{0}^{(0)}(\delta), a_{k}^{(1)}(\delta)$ are deduced from $f^{(0)}(\alpha)$ and f(1)(a). Minimization of (24) with respect to the struc- tural variable $l_{k}$ yields the first-order phase boundary $\delta_{\langle 2\rangle:\langle 1\rangle}^{(1)}(T)$ between the $\langle 2\rangle$ -phase and the chiral(<1>-)phase. (We only mention the results pertaining to the right hand side $(\delta>0)$ of the phase diagram since the rest follows by symmetry,(5)). The phase boundaries $\delta_{\langle 2\rangle:\langle 21\rangle}^{(2)}(T), \delta_{\langle 21\rangle:\langle 1\rangle}^{(2)}(T)$ are obtained in similar fashion by considering $F^{(2)}. F^{(3)}$ is needed to decide whether the $\langle 211\rangle$ -phase or any longer struc ture intervenes between the $\langle 21\rangle$ - and the $\langle 1\rangle$ -phase. We calculated the relevant structural coefficients $a_{0}^{(1)}(\delta), a_{1}^{(1)}(\delta), a_{\infty}^{(1)}(\delta), a_{1}^{(2)}(\delta), a_{12}^{(2)}(\delta)$ and $a_{112}^{(3)}(\delta)$ and found exact agreement with the results of YF. YF show that the stability of the $\langle 211\rangle$ -phase on the sec ond-order phase boundary $\delta_{\langle 21\rangle:\langle 1\rangle}(T)$ depends ex clusively on the sign of the structural coefficient a112(8) on this line. In third order this coefficient is found to be negative, $a_{112}^{(3)}(\delta_{\langle 21\rangle:\langle 1\rangle}^{(2)})<0$ . This proves the $\langle 211\rangle$ -phase to be unstable at sufficiently low temperatures where the third-order result can be ex- pected to apply. As is seen in Fig.3 this is confirmed by the numerical evaluation of the Bethe approxima-

$$\left|\frac{a_{112}-a_{112}^{(3)}}{a_{112}^{(3)}}\right|$$

![](./images/812285623351115779_6.jpg)

Fig. 4. Deviation of the structure coefficient $a_{112}$ from its third-order result of the low-temperature expansion

tion. Clearly, however, the third-order result is invalid at temperatures higher than the branching temperature $T_{b}(21,1)=0.963 J$ where the $\langle 211\rangle$-phase exists. We have determined the structural coefficient $a_{112}$ numerically and have calculated the relative deviation

$$
\alpha\left(K_{0}\right)=\left|\frac{a_{112}-a_{112}^{(3)}}{a_{112}^{(3)}}\right|.
$$

The results depicted in Fig. 4 are incompatible with the behaviour $\alpha\left(K_{0}\right) \propto \exp \left(-3 K_{0}\right)$ suggested by the lowest order terms of the expansion (17). Rather, a good fit is provided by

$$
\alpha\left(K_{0}\right)=4 \exp \left(-1.5 K_{0}\right)
$$

This shows that the higher order corrections to $a_{112}^{(3)}$ may not be neglected unless $K_{0} \ll 1$, i.e. $T \ll J$.

Having emphasized so far the agreement between the YF results and ours at low temperatures we must now point to the differences. YF find no branching points. On the contrary all structures $\left\langle 2^{n} 1\right\rangle$ with $n>1$ (and those related to them by symmetry, (5)) are pre- dicted to disappear at upper cutoff temperatures $T_{\mathrm{co}}(n)$ which tend to zero as $n \rightarrow \infty$. YF determine these temperatures from the leading contributions to the pertinent structural coefficients. From their equation for $T_{\mathrm{co}}(n)$, Eq. (A25) of Ref. [13], one finds that $T_{\mathrm{co}}(n) \gtrsim J$ for $n \lesssim 10$. According to recent work by Szpilka [20], however, the range of validity of the YF results is confined to temperatures $T \ll J$. Thus, as far as the structures $\left\langle 2^{n} 1\right\rangle$ with $n \leqq 10$ are con- cerned, the cutoffs predicted by YF are presumably insignificant. Furthermore, the above example of the coefficient $a_{112}$ suggests that the neglect of higher order corrections to the structural coefficients in the YF analysis precludes the detection of branching points by this technique. There remains the question of whether the cutoffs of the long-period phases $\left\langle 2^{n} 1\right\rangle$ with $n \gg 10$, which according to YF occur at low temperatures $T_{\mathrm{co}}(n) \ll J$, i.e. within the range of validity of their approach, are present in the Bethe approximation. Limitations set by computer precision prevent us from answering this question. We find, however, that at $T \cong J$ the long-period phases are present again. Thus, if cutoffs occur in the Bethe approximation they must be followed by branching points at which the phases reappear.

## V. Summary

In this article we have employed the Bethe approximation to explore the phase diagram of the $\mathrm{CC}_{3}$ model. The transition to the disordered state is found to occur at a considerably lower temperature than in MF-theory; otherwise, the features of the phase diagram in the vicinity of the transition line resemble those of the MF phase diagram. A low-T expansion of the Bethe approximation carried out to third order reproduces exactly the results obtained by YF from a low- $T$ analysis of the full $\mathrm{CC}_{3}$ model. We take this as an indication that the Bethe approximation provides a valid interpolation scheme between the low and the high temperature region of the phase diagram of the $\mathrm{CC}_{3}$ model. The numerical analysis of the Bethe approximation reveals that the complexity of the phase diagram at intermediate temperatures is due to structure combination branching processes by which phases with increasingly longer periods evolve from shorter-period structures. These processes were first detected by Selke and Duxbury in the phase diagram of the ANNNI. They are presumably typical for models with competing interactions.

Financial support from the Bundesministerium für Forschung und Technologie is gratefully acknowledged. The numerical calculations were performed at Regionales Rechenzentrum für Niedersachsen.

## Appendix A

Normalization of the probabilities $y_{i}(\alpha), u_{i}(\alpha)$ requires that they satisfy the following set of relations (cf. Table I):

$$y_{0}(\alpha)+y_{3}(\alpha)+y_{4}(\alpha)=e_{0}(\alpha) \tag{A1a}$$

$$y_{1}(\alpha)+y_{3}(\alpha)+y_{5}(\alpha)=e_{1}(\alpha) \tag{A1b}$$

$$y_{2}(\alpha)+y_{4}(\alpha)+y_{5}(\alpha)=e_{2}(\alpha) \tag{A1c}$$

$$u_{0}(\alpha)+u_{3}(\alpha)+u_{6}(\alpha)=e_{0}(\alpha) \tag{A2a}$$

$$u_{1}(\alpha)+u_{4}(\alpha)+u_{7}(\alpha)=e_{1}(\alpha) \tag{A2b}$$

$$u_{2}(\alpha)+u_{5}(\alpha)+u_{8}(\alpha)=e_{2}(\alpha) \tag{A2c}$$

$$u_{0}(\alpha)+u_{5}(\alpha)+u_{7}(\alpha)=e_{0}(\alpha+1) \tag{A2d}$$

$$u_{1}(\alpha)+u_{3}(\alpha)+u_{8}(\alpha)=e_{1}(\alpha+1) \tag{A2e}$$

The independent variables $f_{i}(\alpha), g_{i}(\alpha)$ were chosen as follows:

$$f_{i}(\alpha)=1 / 9-y_{i+3}(\alpha), \quad i=0,1,2 \tag{A3a}$$

$$g_{i}(\alpha)=1 / 3+3 u_{i}(\alpha)-e_{i}(\alpha)-e_{i}(\alpha+1) \quad i=0,1,2 \tag{A3b}$$

$$\begin{aligned}
g_{3}(\alpha)= & 3\left(u_{3}(\alpha)-u_{7}(\alpha)\right)-e_{0}(\alpha)+e_{0}(\alpha+1) \\
& +e_{1}(\alpha)-e_{1}(\alpha+1)
\end{aligned} \tag{A3c}$$

## Appendix B

The equilibrium conditions (13) expressed in terms of the original variables $e_{i}(\alpha), y_{i}(\alpha), u_{i}(\alpha)$ are represented by the following nine equations:

$$y_{0} y_{1}=y_{2}^{3} \mathrm{e}^{3 K_{0}} \tag{B1a}$$

$$y_{0} y_{2}=y_{4}^{2} \mathrm{e}^{3 K_{0}} \tag{B1b}$$

$$y_{1} y_{2}=y_{5}^{2} \mathrm{e}^{3 K_{0}} \tag{B1c}$$

$$u_{0} u_{1}=u_{3} u_{7} \mathrm{e}^{3 K_{1}} \tag{B2a}$$

$$u_{0} u_{2}=u_{5} u_{6} \mathrm{e}^{3 K_{1}} \tag{B2b}$$

$$u_{3} u_{5}=u_{0} u_{8} \mathrm{e}^{3 K_{1}(1+\delta)} \tag{B2c}$$

$$u_{3} u_{4}=u_{1} u_{6} \mathrm{e}^{3 K_{1}(1+\delta)} \tag{B2d}$$

Here $K_{0}=J_{0} / T, K_{1}=K \cos 2 \pi \Delta / 3, \delta=\sqrt{3}(\tan 2 \pi \Delta / 3$
$-\sqrt{3}) / 2$; the layer index $\alpha$ is the same in all members of these equations and has therefore been omitted.

$$\left(\frac{e_{1}(\alpha)}{e_{0}(\alpha)}\right)^{5}=\left(\frac{y_{1}(\alpha)}{y_{0}(\alpha)}\right)^{2} \frac{u_{1}(\alpha) u_{3}(\alpha-1)}{u_{3}(\alpha) u_{0}(\alpha-1)} \tag{B3a}$$

$$\left(\frac{e_{2}(\alpha)}{e_{0}(\alpha)}\right)^{5}=\left(\frac{y_{2}(\alpha)}{y_{0}(\alpha)}\right)^{2} \frac{u_{5}(\alpha) u_{2}(\alpha-1)}{u_{0}(\alpha) u_{5}(\alpha-1)} \tag{B3b}$$

## References

1. For a survey see: Modulated structure materials. Tsakalakos, T. (ed.). NATO ASI Series. The Hague, Boston, London: Martin Nijhoff 1984
2. Rossat-Mignod, H., Burlet, P., Bartholin, H., Vogt, O., Lagniet, R.: J. Phys. **C13**, 6381 (1980)
3. Jamet, J.P., Lederer, P., Moudden, A.H.: Phys. Rev. Lett. **48**, 442 (1982); Moudden, A.H., Svensson, E.C., Shirane, G.: Phys. Rev. Lett. **49**, 557 (1982); Moudden, A.H., Moncton, D.E., Axe, J.D.: Phys. Rev. Lett. **51**, 2390 (1983); Durand, D., Denoyer, F., Lefur, D., Currat, R., Bernard, L.: J. Phys. Lett. (Paris) **44**, L207 (1983); Durand, D., Denoyer, F., Currat, R., Vettier, C.: Phys. Rev. **B30**, 1112 (1984)
4. Fontaine, D. de, Kulik, J.: Acta Metall. **33**, 145 (1985); Portier, R., Gratias, D., Guymont, M., Stobbs, W.M.: Acta Crystallogr. **A36**, 190 (1980); Loiseau, A., Tendeloo, G. van, Portier, R., Ducastelle, F.: J. Phys. (Paris) **46**, 595 (1985)
5. Elliott, Phys. Rev. **124**, 346 (1961)
6. Ostlund, S.: Phys. Rev. **B24**, 398 (1981); Huse, D.A.: Phys. Rev. **B24**, 5180 (1981)
7. Fisher, M.E., Selke, W.: Phys. Rev. Lett. **44**, 1502 (1980); Fisher, M.E., Selke, W.: Philos. Transact. R. Soc. London **302**, 1 (1981)
8. Boehm, J. von, Bak, P.: Phys. Rev. Lett. **42**, 122 (1979); Bak, P., Boehm, J. von: Phys. Rev. **B21**, 5297 (1980)
9. Jensen, M.H., Bak, P.: Phys. Rev. **B27**, 6853 (1983)
10. Selke, W., Duxbury, P.M.: Z. Phys. B - Condensed Matter **57**, 49 (1984)
11. Taylor, J.H., Desjardin, J.S.: Phys. Rev. **B30**, 5203 (1984)
12. Yeomans, J.M., Fisher, M.E.: J. Phys. **C14**, L835 (1981)
13. Yeomans, J.M., Fisher, M.E.: Physica A **127**, 1 (1984)
14. Szpilka, A.M., Fisher, M.E.: Phys. Rev. Lett. **57**, 1044 (1986)
15. Öttinger, H.C.: J. Phys. **C15**, L1257 (1982)
16. Öttinger, H.C.:J. Phys. **C16**, L597 (1983)
17. Siegert, M., Everts, H.U.: Z. Phys. B - Condensed Matter **60**, 265 (1985)
18. Burley, D.M.: In: Phase transitions and critical phenomena, Domb, C., Green, M.S. (eds.), Vol. 2, p. 329. New York: Academic Press 1972
19. Kikuchi, R.: Phys. Rev. **81**, 988 (1951)
20. Szpilka, A.M.: Ph.D. Thesis, Cornell University (1985)

M. Siegert
H.U. Everts
Institut für Theoretische Physik
Universität Hannover
Appelstrasse 2
D-3000 Hannover 1
Federal Republic of Germany