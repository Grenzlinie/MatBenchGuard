
# Conductance from Non-perturbative Methods I

Olalla A. Castro-Alvaredo and Andreas Fring \( ^{*} \) 

Institut für Theoretische Physik, Freie Universität Berlin,

Arnimallee 14, D-14195 Berlin, Germany

E-mail: Olalla@physik.fu-berlin.de, Fring@physik.fu-b erlin.de

ABSTRACT: We investigate different methods to compute the DC conductance in a quantum wire doped with some impuritied by exploiting the integrability of the theories under consideration. As an essential ingredient in all methods we evaluate the reflection and transmission amplitudes of the impurities for a variety of defects. When the impurities in the wire are coupled to an external three dimensional laser field, we predict the generation of harmonic emission spectra. We propose a modified version of the well-known Kubo formula, which incorporates the impurities of the system and evaluates the current-current two-point correlation function it involves with the help of a form factor expansion. A comparison with the corresponding quantities computed in a Landauer transport theory picture is carried out in part II.

The work I want to report about is based on a series of papers  \( [1, 2, 3, 4, 5, 6] \)  with an emphasis on the first two. Olalla Castro-Alvaredo will present the second part of this talk.

## 1. Generalities on conductance

In the context of  \( 1+1 \)  dimensional quantum field theories an impressive arsenal of non-perturbative techniques has been developed over the last 25 years. The original motivation was to use the lower dimensional set up as a testing ground for general conceptual ideas and possibly to apply them in the context of string theory, such that most of the work in this area can be characterized very often as rather formal. However, lately the experimental techniques have advanced to such an extent that one might realistically hope to measure various quantities which can be predicted based on these approaches.

One of those quantities, which is particularly easy to access, is the conductance (conductivity). It can be measured in general directly without perturbing very much the behaviour of the system, e.g. a rigid-lattice bulk metal, such that the uncertainty of experimental artefacts is reduced to a minimum. Indeed, there have been some fairly recent
 

measurements [7] of this quantity in  \( 1+1 \)  dimensions and the challenge is of course to explain these data theoretically and possibly inspire more experiments of a similar type.

There exist two main theoretical descriptions to compute the conductance, the Kubo formula  \( [8, 9] \) , which is the outcome of a dynamical linear-response theory and the Landauer-Büttinger theory  \( [10] \) , which is a semi-classical transport theory. The main purpose of the work I want to present is a comparison between these two descriptions by employing non-perturbative methods of  \( 1+1 \)  dimensional integrable models. It is in this sense the wording non-perturbative is to be understood, that is despite the fact that the overall theoretical description is of a perturbative nature, within these frameworks we use non-perturbative methods. I will concentrate on our proposal of a generalized Kubo formula and in the second part, presented by Olalla Castro-Alvaredo, the computations within the Landauer-Büttinger transport theory framework will be presented.

I will start by anticipating the quantities we have to compute. The system we consider is a one-dimensional quantum wire doped with some impurities (defects). For the time being we leave the theory describing the wire and also the nature of the impurities unspecified. In linear response theory one essentially needs the Fourier transform of the current-current two-point correlation function. This so-called Kubo formula has been adopted to a situation with a boundary  \( [11] \) . Since this only captures effects coming from the constriction of the wire a generalization to a set up with defects was needed, which we proposed in  \( [1] \)  as

 \[ G^{\alpha}(T)=-\lim_{\omega\rightarrow0}\frac{1}{2\omega\pi^{2}}\int_{-\infty}^{\infty}d t e^{i\omega t}\left\langle J(t)Z_{\alpha}J(0)\right\rangle_{T,m}. \quad (1.1) \] 

Here the defect operator  \( Z_{\alpha} \)  enters in-between the two local currents J within the temperature T and mass m dependent correlation function. The Matsubara frequency is denoted by  \( \omega \) .

The other possibility of determining the conductance which we want to study, is a generalization of the Landauer-Büttinger transport theory picture. Within this framework a proposal for the conductance through a quantum wire with a defect (impurity) has been made in  \( [12, 13] \) 

 \[ G^{\alpha}(T)=\sum_{i}\lim_{(\mu_{i}^{s}-\mu_{i}^{r})\to0}\frac{q_{i}}{2}\int_{-\infty}^{\infty}d\theta\left[\rho_{i}^{r}(\theta,T,\mu_{i}^{l})|T_{i}^{\alpha}\left(\theta\right)|^{2}-\rho_{i}^{r}(\theta,T,\mu_{i}^{r})|\tilde{T}_{i}^{\alpha}\left(\theta\right)|^{2}\right], \quad (1.2) \] 

which we only modify to accommodate parity breaking. This means we allow the transmission amplitudes for a particle of type i with charge  \( q_{i} \)  passing with rapidity  \( \theta \)  through a defect of type  \( \alpha \)  from the left  \( T_{i}^{\alpha}(\theta) \)  and right  \( \tilde{T}_{i}^{\alpha}(\theta) \)  to be different. The density distribution function  \( \rho_{i}^{r}(\theta,T,\mu_{i}) \)  depends on the temperature T, and the potential at the left  \( \mu_{i}^{l} \)  and right  \( \mu_{r}^{r} \)  constriction of the wire.

The main quantities we have to compute before we can evaluate (1.1) and (1.2) are the transmission amplitudes  \( T_{i} \) , the current-current correlation functions  \( \langle\ldots\rangle_{T,m} \)  and the density distributions  \( \rho_{i} \) . We obtain all of them non-perturbatively, the  \( T \) 's by means of potential scattering theory, e.g. [14], the correlation function from a form factor [15, 16, 17] expansion and the  \( \rho \) 's from a thermodynamic Bethe (TBA) ansatz [18] analysis.
 

## 2. Impurity systems

## 2.1 Constraints from the generalized Yang-Baxter equations

Let me start with the evaluation of the transmission amplitudes, since they will be required in (1.1) as well as in (1.2). One of the great advantages of integrability in  \( 1+1 \)  dimensional models is that the n-particle scattering matrix factorises into two-particle S-matrices, which can be determined by some constraining equations such as the Yang-Baxter [19] and bootstrap equations [20]. Similar equations hold in the presence of a boundary [21, 22, 23] or a defect [24, 4]. It is clear that with regard to the conductance a situation with a pure boundary, i.e. non-trivial effects on the constrictions, or purely transmitting defects will be rather uninteresting and we would like to consider the case when R and T are simultaneously non-vanishing. Unfortunately, it will turn out that for that situation the Yang-Baxter equations are so constraining that not many integrable theories will be left to consider. Thus this section serves essentially to motivate the study of the free Fermion, which after all is very close to a realistic system of electrons propagating in quantum wires.

We label now particle types by Latin and degrees of freedom of the impurity by Greek letters, the bulk scattering matrix by S, and the left/right reflection and transmission amplitudes of the defect by  \( R/\tilde{R} \)  and  \( T/\tilde{T} \) , respectively. Then the transmission and reflection amplitudes are constrained by the “unitarity” relations

 \[ R_{i\alpha}^{j\beta}(\theta)R_{j\beta}^{k\gamma}(-\theta)+T_{i\alpha}^{j\beta}(\theta)\tilde{T}_{j\beta}^{k\gamma}(-\theta)=\delta_{i}^{k}\delta_{\alpha}^{\gamma}, \quad (2.1) \] 

 \[ R_{i\alpha}^{j\beta}(\theta)T_{j\beta}^{k\gamma}(-\theta)+T_{i\alpha}^{j\beta}(\theta)\tilde{R}_{j\beta}^{k\gamma}(-\theta)=0, \quad (2.2) \] 

and the crossing-hermiticity relations

 \[ R_{\gamma}^{\alpha}(\theta)=\tilde{R}_{\gamma}^{\alpha}(-\theta)^{*}=S_{j j}(2\theta)\tilde{R}_{\gamma}^{\alpha}(i\pi-\theta), \quad (2.3) \] 

 \[ T_{j}^{\alpha}(\theta)=\tilde{T}_{j}^{\alpha}(-\theta)^{*}=\tilde{T}_{j}^{\beta}(i\pi-\theta). \quad (2.4) \] 

The equations (2.1) and (2.2) also hold after performing a parity transformation, that is for  \( R \leftrightarrow \tilde{R} \)  and  \( T \leftrightarrow \tilde{T} \) .

Depending now on the choice of the initial asymptotic condition one can derive the following two non-equivalent sets of generalized Yang-Baxter equations by exploiting the associativity of the extended Zamolodchikov-Faddeev algebra  \( [21, 22, 23, 24, 4] \) 

 \[ S(\theta_{12})[\mathbb{I}\otimes R_{\alpha}^{\beta}(\theta_{1})]S(\hat{\theta}_{12})[\mathbb{I}\otimes R_{\beta}^{\gamma}(\theta_{2})]=[\mathbb{I}\otimes R_{\alpha}^{\beta}(\theta_{2})]S(\hat{\theta}_{12})[\mathbb{I}\otimes R_{\beta}^{\gamma}(\theta_{1})]S(\theta_{12}), \quad (2.5) \] 

 \[ S(\theta_{12})[\mathbb{I}\otimes R_{\alpha}^{\beta}(\theta_{1})]S(\hat{\theta}_{12})[\mathbb{I}\otimes T_{\beta}^{\gamma}(\theta_{2})]=R_{\beta}^{\gamma}(\boldsymbol{\theta}_{1})\otimes T_{\alpha}^{\beta}(\theta_{2}), \quad (2.6) \] 

 \[ S(\theta_{12})[T_{\alpha}^{\beta}(\theta_{2})\otimes T_{\beta}^{\gamma}(\theta_{1})]=[T_{\alpha}^{\beta}(\theta_{1})\otimes T_{\beta}^{\gamma}(\theta_{2})]S(\theta_{12}), \quad (2.7) \] 

and

 \[ R_{\alpha}^{\beta}(\theta_{1})\otimes\tilde{R}_{\beta}^{\gamma}(\theta_{2})=R_{\beta}^{\gamma}(\theta{}_{1})\otimes\tilde{R}_{\alpha}^{\beta}(\theta_{2}), \quad (2.8) \] 

 \[ [T_{\alpha}^{\beta}(\theta_{2})\otimes\mathbb{I}]S(\hat{\theta}_{12})[\tilde{R}_{\beta}^{\gamma}(\theta_{1})\otimes\mathbb{I}]S(\theta_{12})=T_{\beta}^{\gamma}(\theta_{2})\otimes\tilde{R}_{\alpha}^{\beta}(\theta_{1}), \quad (2.9) \] 

 \[ [\mathbb{I}\otimes\tilde{T}_{\alpha}^{\beta}(\theta_{2})]S(\hat{\theta}_{12})[\mathbb{I}\otimes R_{\beta}^{\gamma}(\theta_{1})]S(\theta_{12})=R_{\alpha}^{\beta}(\theta_{1})\otimes\tilde{T}_{\beta}^{\gamma}(\theta_{2}), \quad (2.10) \] 

 \[ [T_{\alpha}^{\beta}(\theta_{1})\otimes\mathbb{I}]S(\hat{\theta}_{12})[\tilde{T}_{\beta}^{\gamma}(\theta_{2})\otimes\mathbb{I}]=[\mathbb{I}\otimes\tilde{T}_{\alpha}^{\beta}(\theta_{2})]S(\hat{\theta}_{12})[\mathbb{I}\otimes T_{\beta}^{\gamma}(\theta_{1})]. \quad (2.11) \]
 

We used here the convention  \( (A \otimes B)_{ij}^{kl} = A_{i}^{k} B_{j}^{l} \)  for the tensor product and abbreviated the rapidity sum  \( \hat{\theta}_{12} = \theta_{1} + \theta_{2} \)  and difference  \( \theta_{12} = \theta_{1} - \theta_{2} \) . Once again the same equations also hold for  \( R \leftrightarrow \tilde{R} \)  and  \( T \leftrightarrow \tilde{T} \) .

Apart from some discrepancies in the indices the equations (2.5)-(2.7) correspond to a more simplified, in the sense that there were no degrees of freedom in the defect and parity invariance is assumed, set of equations considered previously in [24]. For diagonal scattering it was argued in [24] that one can only have reflection and transmission simultaneously when  \( S = \pm1 \) . In [4] a more general set up which includes all degrees of freedom was studied. A second set of equations (2.8)-(2.11), which is not equivalent to (2.5)-(2.7) was found. It was shown that in the absence of degrees of freedom in the defect no theory which has a non-diagonal bulk scattering matrix admits simultaneous reflection and transmission. This result even holds for the completely general case including degrees of freedom in the defect upon a mild assumption on the commutativity of R and T in these variables. It was further shown that besides  \( S = \pm1 \)  also the Federbush model [25] and the generalized coupled Federbush models [6] allow for  \( R \neq 0 \)  and  \( T \neq 0 \) .

## 2.2 Multiple impurity systems

The most interest situation in impurity systems arises when instead of a single one considers multiple defects, since that leads to the occurrence of resonance phenomena and when the number of defects tends to infinity even to band structures. Assuming that the distance between the defects is small in comparison to the length of the wire one can easily construct the transmission and reflection amplitudes of the multiple defect system from the knowledge of the corresponding quantities in the single defect system. For instance for two defects one obtains

 \[ T_{i}^{\alpha\beta}(\theta)=\frac{T_{i}^{\alpha}(\theta)T_{i}^{\beta}(\theta)}{1-R_{i}^{\beta}(\θ)\tilde{R}_{i}^{\alpha}(\theta)},\qquad R_{i}^{\alpha\beta}(\theta)=R_{i}^{\alpha}(\theta)+\frac{R_{i}^{\beta}(\theta)T_{i}^{\alpha}(\theta)\tilde{T}_{i}^{\alpha}(\theta)}{1-R_{i}^{\beta}(\theta)\tilde{R}_{i}^{\alpha}(\theta)}, \quad (2.12) \] 

 \[ \tilde{T}_{i}^{\alpha\beta}(\theta)=\frac{\tilde{T}_{i}^{\α}(\theta)\tilde{T}_{i}^{\β}(\theta)}{1-R_{i}^{\β}(\theta)\tilde{R}_{i}^{\α}(\theta)},\qquad\tilde{R}_{i}^{\alpha\beta}(\theta)=\tilde{R}_{i}^{\β}(\theta)+\frac{R_{i}^{\α}(\theta)T_{i}^{\β}(\theta)\tilde{T}_{i}^{\β}(\theta)}{1-R_{i}^{\β}(\theta)\tilde{R}_{i}^{\α}(\theta)}. \quad (2.13) \] 

These expressions allow for a direct intuitive understanding, for instance we note that the term  \( [1 - R_{i}^{\beta}(\theta)\tilde{R}_{i}^{\alpha}(\theta)]^{-1} = \sum_{n=1}^{\infty}(R_{i}^{\beta}(\theta)\tilde{R}_{i}^{\alpha}(\theta))^{n} \)  simply results from the infinite number of reflections which we have in-between the two defects. This is of course well known from Fabry-Perot type devices of classical and quantum optics. For the case  \( T = \tilde{T} \) ,  \( R = \tilde{R} \)  the expressions (2.12) and (2.13) coincide with the formulae proposed in [26]. When absorbing the space dependent phase factor into the defect matrices, the explicit example presented in [24] for the free Fermion perturbed with the energy operator agree almost for  \( T = \tilde{T} \) ,  \( R = \tilde{R} \)  with the general formulae (2.12). They disagree in the sense that the equality of  \( R_{i}^{\alpha\beta}(\theta) \)  and  \( \tilde{R}_{i}^{\alpha\beta}(\theta) \)  does not hold for generic  \( \alpha \) ,  \( \beta \)  as stated in [24].

It is now straightforward to generalize the expressions for an arbitrary number of defects, say n, in a recursive manner

 \[ T_{i}^{\overline{\alpha}}(\theta)=\frac{T_{i}^{\alpha_{1}\ldots\alpha_{k}}(\theta)T_{i}^{\alpha_{k+1}\ldots\alpha_{n}}(\theta)}{1-\tilde{R}_{i}^{\alpha_{1}\ldots\alpha_{k}}(\theta)R_{i}^{\alpha_{k+1}\ldots\alpha_{n}}(\theta)},\quad1<k<n, \quad (2.14) \]
 

 \[ R_{i}^{\vec{\alpha}}(\theta)=R_{i}^{\alpha_{1}\ldots\alpha_{k}}(\theta)+\frac{R_{i}^{\alpha_{k+1}\ldots\alpha_{n}}(\theta)T_{i}^{\alpha_{1}\ldots\alpha_{k}}(\theta)}{1-\tilde{R}_{i}^{\alpha_{1}\ldots\alpha_{k}}(\theta)R_{i}^{\alpha_{k+1}\ldots\alpha_{n}}(\theta)},\quad1<k<n. \quad (2.15) \] 

We encoded here the defect degrees of freedom into the vector  \( \vec{\alpha}=\{\alpha_{1},\cdots,\alpha_{n}\} \) . Similar expressions also hold for  \( \tilde{T}_{i}^{\vec{\alpha}}(\theta)=\tilde{T}_{i}^{\alpha_{1}\ldots\alpha_{n}}(\theta) \)  and  \( \tilde{R}_{i}^{\vec{\alpha}}(\theta)=\tilde{R}_{i}^{\alpha_{1}\ldots\alpha_{n}}(\theta) \) .

Alternatively, we can define, in analogy to standard quantum mechanical methods (see e.g. [14]), a transmission matrix which takes the particle i from one side of the defect of type  \( \alpha \)  to the other

 \[ \mathcal{M}_{\alpha}^{i}(\theta)=\left(\begin{array}{c c}{T_{i}^{\alpha}(\theta)^{-1}}&{-R_{i}^{\alpha}(\partial)T_{i}^{\alpha}(\theta)^{-1}}\\ {-R_{i}^{\alpha}(-\partial)T_{i}^{\alpha}(-{\partial})^{-1}}&{T_{i}^{\alpha}(-\partial)^{-1}}\\ \end{array}\right). \quad (2.16) \] 

Then alternatively to the recursive way (2.14) and (2.15), we can also compute the multi-defect transmission and reflection amplitudes as

 \[ T_{i}^{\vec{\alpha}}(\theta)=\left(\prod_{k=1}^{n}\mathcal{M}_{\alpha_{k}}^{i}(\theta)\right)^{-1}_{11},\quad R_{i}^{\vec{\alpha}}(\theta)=-\left(\prod_{k=1}^{n}\mathcal{M}_{\alpha_{k}}^{i}(\theta)\right)_{12}\left(\prod_{k=1}^{n}\mathcal{M}_{\alpha_{k}}^{i}(\theta)\right)^{-1}_{11}. \quad (2.17) \] 

This formulation has the virtue that it is more suitable for numerical computations, since it just involves matrix multiplications rather than recurrence operations. In addition it allows for an elegant analytical computation of the band structures for  \( n \to \infty \) , which I will however not comment upon further in this talk.

## 2.3 Constraints from potential scattering theory

As we argued in section 2.1., in order to obtain a non-trivial conductance we are lead to consider free theories, possibly with some exotic statistics. Trying to be as close as possible to some realistic situation, i.e. electrons, we consider first the free Fermion, which with a line of defect was first treated in [27]. Thereafter it has also been considered in [28, 24] and [29] from different points of view. In [27, 28, 24] the defect line was taken to be of the form of the energy operator and in [29] also a perturbation in form of a single Fermion has been considered. In [1] we treated a much wider class of possible defects.

Let us consider the Lagrangian density for a complex free Fermion  \( \psi \)  with  \( \ell \)  defects \( ^{1} \) 

 \[ \mathcal{L}=\bar{\psi}(i\gamma^{\mu}\partial_{\mu}-m)\psi+\sum_{n=1}^{\ell}\mathcal{D}^{\alpha_{n}}(\bar{\psi},\psi,\partial_{t}\bar{\psi},\partial_{t}\psi)\delta(x-x_{n}). \quad (2.18) \] 

The defect is described here by the functions  \( \mathcal{D}^{\alpha_{n}}(\bar{\psi},\psi,\partial_{t}\bar{\psi},\partial_{t}\psi) \) , which we assume to be linear in the Fermi fields  \( \bar{\psi},\psi \)  and their time derivatives. We can now proceed in

 \( ^{1} \) We use the conventions:

 \[ \begin{aligned}x^{\mu}&=(x^{0},x^{1}),\qquad p^{\mu}=(m\cosh\theta,m\sinh\theta),\quad g^{00}=-g^{11}=\varepsilon^{01}=-\varepsilon^{10}=1,\\\gamma^{0}&=\begin{pmatrix}{{{0}}}&{{{1}}} \\{{{1}}}&{{{0}}}\end{pmatrix},\qquad\gamma^{1}=\begin{pmatrix}{{{0}}}&{{{1}}} \\{{{-1}}}&{{{0}}}\end{pmatrix},\quad\gamma^{5}=\gamma^{0}\gamma^{1},\qquad\psi_{\alpha}=\begin{pmatrix}{{{\psi_{\alpha}^{(1)}}}} \\{{{\psi_{\alpha}^{(2)}}}}\end{pmatrix},\quad\bar{\psi}_{\alpha}=\psi_{\alpha}^{\dagger}\gamma^{0}.\end{aligned} \] 

We adopt relativistic units  \( 1 = c = \hbar = m \approx e^{2}137 \)  as mostly used in the particle physics context rather than atomic units  \( 1 = e = \hbar = m \approx c/137 \)  more natural in atomic physics.
 

analogy to standard quantum mechanical potential scattering theory (see also [28, 24, 29]) and construct the amplitudes by adequate matching conditions on the field. We consider first a single defect at the origin which suffices, since multiple defect amplitudes can be constructed from the single defect ones, according to the arguments of the previous section. We decompose the fields of the bulk theory as  \( \psi(x)=\Theta(x)\psi_{+}(x)+\Theta(-x)\psi_{-}(x) \) , with  \( \Theta(x) \)  being the Heavyside unit step function, and substitute this ansatz into the equations of motion. As a matching condition we read off the factors of the delta function and hence obtain the constraints

 \[ i\gamma^{1}(\psi_{+}(x)-\psi_{-}(x))|_{x=0}=\left.\frac{\partial\mathcal{D}}{\partial\bar{\psi}(x)}\right|_{x=0}-\left.\frac{\partial}{\partial t}\left[\frac{\partial\mathcal{D}}{\partial(\partial_{t}\bar{\psi}(x))}\right]\right|_{x=0}. \quad (2.19) \] 

We then use for the left  \( (-) \)  and right  \( (+) \)  parts of  \( \psi \)  the well-known Fourier decomposition of the free field

 \[ \psi_{j}^{f}(x)=\int\frac{d\theta}{\sqrt{4\pi}}\left(a_{j}(\theta)u_{j}(\theta)e^{-i p_{j}\cdot x}+a_{j}^{\dagger}(\theta)v_{j}(\theta)e^{i p_{j}\cdot x}\right), \quad (2.20) \] 

with the Weyl spinors

 \[ u_{j}(\theta)=-i\gamma^{5}v_{j}(\theta)=\sqrt{\frac{m_{j}}{2}}\left(\begin{array}{c}e^{-\theta/2}\\ e^{\theta/2}\end{array}\right) \quad (2.21) \] 

and substitute them into the constraint (2.19). Treating the equations obtained in this manner componentwise, stripping off the integrals, one can bring them thereafter into the form

 \[ a_{j,-}(\theta)=R_{j}(\theta)a_{j,-}(-\theta)+T_{j}(\theta)a_{\bar{\jmath},+}(\theta), \quad (2.22) \] 

which defines the reflection and transmission amplitudes in an obvious manner. When parity invariance is broken, the corresponding amplitudes from the right to the left do not have to be identical and we also have

 \[ a_{j,+}(-\theta)=\tilde{T}_{j}(\theta)a_{j,-}(-\theta)+\tilde{R}_{j}(\theta)a_{\bar{\jmath},+}(\theta). \quad (2.23) \] 

The creation and annihilation operators  \( a_{i}^{\dagger}(\theta) \)  and  \( a_{i}(\theta) \)  satisfy the usual fermionic anticommutation relations  \( \{a_{i}(\theta_{1}), a_{j}(\theta_{2})\} = 0 \) ,  \( \{a_{i}(\theta_{1}), a_{j}^{\dagger}(\theta_{2})\} = 2\pi\delta_{ij}\delta(\theta_{12}) \) . In this way one may construct the  \( R' \) s and  \( T' \) s for any concrete defect which is of the generic form as described in (2.18). After the construction one may convince oneself that the expressions found this way indeed satisfy the consistency equations like unitarity (2.1), (2.2) and crossing (2.3), (2.4). Unfortunately the equations (2.1)-(2.4) cannot be employed for the construction, since they are not restrictive enough by themselves to determine the  \( R' \) s and  \( T' \) s. We consider now some concrete examples:

## 2.3.1 Impurities of Luttinger liquid type  \( \mathcal{D}(\bar{\psi},\psi)=\bar{\psi}(g_{1}+g_{2}\gamma^{0})\psi \) 

Luttinger liquids [30] are of great interest in condensed matter physics, which is one of the motivations for our concrete choice of the defect  \( \mathcal{D}(\bar{\psi},\psi)=\bar{\psi}(g_{1}+g_{2}\gamma^{0})\psi \) . When taking the conformal limit of the defect one obtains an impurity which played a role in this
 

context, see e.g. [31], after eliminating the bosonic number counting operator. In the way outlined above, we compute the related transmission and reflection amplitudes

 \[ R_{j}(\theta,g_{1},g_{2},-y)=\tilde{R}_{j}(\theta,g_{1},g_{2},y)=\frac{4i(g_{2}+g_{1}\cosh\theta)e^{2i y m\sinh\theta}}{(4+g_{1}^{2}-g_{2}^{2})\sinh\theta-4i(g_{1}+g_{2}\cosh\theta)}, \quad (2.24) \] 

 \[ R_{j}(\theta,g_{1},g_{2},-y)=\tilde{R}_{j}(\theta,g_{1},g_{2},y)=\frac{4i(g_{1}-g_{2}\cosh\theta)e^{-2i y m\sinh\theta}}{(4+g_{1}^{2}-g_{2}^{2})\sinh\theta-4i(g_{1}-g_{2}\cosh\theta)}, \quad (2.25) \] 

 \[ T_{j}(\theta,g_{1},g_{2})=\tilde{T}_{j}(\theta,g_{2})=\frac{(4+g_{2}^{2}-g_{1}^{2})\sinh\theta}{(4+g_{1}^{2}-g_{2}^{2})\sinh\theta-4i(g_{1}+g_{2}\cosh\theta)}, \quad (2.26) \] 

 \[ T_{j}(\theta,g_{1},g_{2})=\tilde{T}_{j}(\theta,g_{2})=\frac{(4+g_{2}^{2}-g_{1}^{2})\sinh\theta}{(4+g_{1}^{2}-g_{2}^{2})\sinh\theta-4i(g_{1}-g_{2}\cosh\theta)}. \quad (2.27) \] 

In the limit  \( \lim_{g_{2}\to0}\mathcal{D}(\tilde{\psi},\psi)=g_{1}\tilde{\psi}\psi \) , we recover the related results for the  \( T/\tilde{T} \) 's and  \( \tilde{R}/\tilde{R} \) 's for the energy defect operator. For this type of defect we present  \( |T|^{2} \)  and  \( |R|^{2} \)  in figure 1 with varying parameters in order to illustrate some of the characteristics of these functions.

![](./images/867756429077905572_1.jpg)

![](./images/867756429077905572_2.jpg)

![](./images/867756429077905572_3.jpg)

![](./images/867756429077905572_4.jpg)

Figure 1: (a) Single defect with varying coupling constant.  \( |T|^{2} \)  and  \( |R|^{2} \)  correspond to curves starting at 0 and 1 of the same line type, respectively. (b) Double defect with varying distance y. (c) Double defect with varying effective coupling constant  \( B = \arcsin(-4g_{1}/(4 + g_{1}^{2})) \) . (d) Double defect  \( \equiv \)  dotted line, eight defects  \( \equiv \)   solid line.
 

Part (a) of figure 1 confirms the unitarity relation (2.1). Part (b) and (c) show the typical resonances of a double defect, which become stretched out and pronounced with respect to the energy when the distance becomes smaller and the coupling constant increases, respectively. Part (d) exhibits a general feature, that is when the number of defects is increased, for fixed distance between the outermost defects, the resonances become more and more dense in that region such that one may speak of energy bands.

## 2.3.2 The defect  \( \mathcal{D}(\bar{\psi},\psi,\partial_{t}\bar{\psi},\partial_{t}\psi)=ig/2(\bar{\psi}\partial_{t}\psi-\partial_{t}\bar{\psi}\psi) \) 

This type of defect reminds on the first non-trivial charge occurring in the free Fermion model. In this case we compute by the same means the related transmission and reflection amplitudes to

 \[ \tilde{R}_{j}^{\alpha}(\theta,y)=R_{j}^{\alpha}(\theta, y)=R_{j}^{\infty}(\theta,-y)=\tilde{R}_{j}^{\infty}(\theta, -y)=\frac{-4i g\cosh\theta e^{2i y m\sinh\theta}}{4i g+\tanh\theta(4+g^{2}\cosh^{2}\theta)}, \quad (2.28) \] 

 \[ T_{j}^{\alpha}(\theta)=\tilde{T}_{j}^{\alpha}(\theta)=T_{j}^{\infty}(\theta)=\frac{(4-g^{2}\cosh^{2}\theta)\tanh\theta}{4i g+\tanh\theta(4+g^{2}\cosh^{2}\theta)}. \quad (2.29) \] 

In [1] we also computed the  \( T/\tilde{T} \) 's and  \( R/\tilde{R} \) 's for other types of defects, such as  \( D = g\bar{\psi}\gamma^{1}\psi \) ,  \( D = g\bar{\psi}\gamma^{5}\psi \) ,  \( D = g\bar{\psi}(\gamma^{1} \pm \gamma^{5})\psi \ldots \)  As an overall conclusion we observed that all possible types of parity breaking, that is  \( T \neq \tilde{T} \) ;  \( R \neq \tilde{R} \)  or  \( T \neq \tilde{T} \) ;  \( R = \tilde{R} \) , etc., do occur. We also confirm a general principle one knows well from quantum mechanics, namely that parity is preserved when the potential is real, that is in this case the defect satisfies  \( D^{*} = D \) .

## 2.4 Impurities coupled to laser fields

Let us now consider a more complex situation in which a three dimensional laser field hits the quantum wire polarized in such a way that it has a vector field component along the wire. Since the work of Weyl [32], one knows that matter may be coupled to light by means of a local gauge transformation, which reflects itself in the usual minimal coupling prescription, i.e.  \( \partial_{\mu} \rightarrow \partial_{\mu} - ieA_{\mu} \) , with  \( A_{\mu} \)  being the vector gauge potential. The free Fermions in the wire are then described by the Lagrangian density

 \[ \mathcal{L}_{A}=\bar{\psi}(i\gamma^{\mu}\partial_{\mu}-m+e\gamma^{\mu}A_{\mu})\psi. \quad (2.30) \] 

When the laser field is switched on, we can solve the equation of motion associated to  \( (2.30) \) 

 \[ (i\gamma^{\mu}\partial_{\mu}-m+e\gamma^{\mu}A_{\mu})\psi=0 \quad (2.31) \] 

by a Gordon-Volkov type solution [33]

 \[ \psi_{j}^{A}(x,t)=\exp\left[ie\int^{x}d s A_{1}(s,t)\right]\psi_{j}^{f}(x,t)=\exp\left[ie\int^{t}d s A_{0}(x,s)\right]\psi_{j}^{f}(x,t). \quad (2.32) \] 

Using now a linearly polarized laser field along the direction of the wire, the vector potential can typically be taken in the dipole approximation to be a superposition of monochromatic
 

light with frequency  \( \omega \) , i.e.

 \[ A(t):=A_{1}(t)=\frac{1}{x}\int_{0}^{t}d s A_{0}(s)=-\frac{1}{2}\int_{0}^{t}d s E(s)=-\frac{E_{0}}{2}\int_{0}^{t}d s f(s)\cos(\omega s) \quad (2.33) \] 

with  \(  f(t)  \)  being an arbitrary enveloping function equal to zero for t < 0 and  \( t > \tau \) , such that  \( \tau \)  denotes the pulse length. In the following we will always take  \(  f(t) = \Theta(t) \Theta(\tau - t)  \) , with  \(  \Theta(x)  \)  being again the Heavyside unit step function. The second equality in (2.33),  \(  A_{0}(x, t) = x \dot{A}(t)  \) , follows from the fact that we have to solve (2.32).

I want to comment on the validity of the dipole approximation in this context. It consists usually in neglecting the spatial dependence of the laser field, which is justified when  \( x\omega < c = 1 \) , where x is a representative scale of the problem considered. In the context of atomic physics this is typically the Bohr radius. In the problem investigated here, this approximation has to hold over the full spatial range in which the Fermi-Fermi-Fermi-Fermion-Fermion-Fermi-Fermio follows the electric field. We can estimate this classically, in which case the maximal amplitude is  \( eE_{0}/\omega^{2} \)  and therefore the following constraint has to hold.

 \[ \left(\frac{e E_{0}}{\omega}\right)^{2}=4U_{p}<1, \quad (2.34) \] 

for the dipole approximation to be valid. Due to the fact that x is a function of  \( \omega \) , we have now a lower bound on the frequency rather than an upper one as is more common in the context of atomic physics. We have also introduced here the ponderomotive energy  \( U_{p} \)  for monochromatic light, that is the average kinetic energy transferred from the laser field to the electron in the wire.

The solutions to the equations of motion of the free system and the one which includes the laser field are then related by a factor similar to the gauge transformation from the length to the velocity gauge

 \[ \psi_{j}^{A}(x,t)=\exp\left[i x e A(t)\right]\psi_{j}^{f}(x). \quad (2.35) \] 

In an analogous fashion one may use the same minimal coupling procedure also to couple in addition the laser field to the defect. One has to invoke the equation of motion in order to carry this out. For convenience we assume now that the defect is linear in the fields  \( \bar{\psi} \)  and  \( \psi \) . The Lagrangian density for a complex free Fermion  \( \psi \)  with  \( \ell \)  defects  \( \mathcal{D}^{\alpha}(\bar{\psi},\psi,A_{\mu}) \)  of type  \( \alpha \)  at the position  \( x_{n} \)  subjected to a laser field then reads

 \[ \mathcal{L}_{A D}=\mathcal{L}_{A}+\sum_{n=1}^{\ell}\mathcal{D}^{\alpha_{n}}(\bar{\psi},\psi,A_{\mu})\delta(x-x_{n}). \quad (2.36) \] 

Considering for simplicity first the case of a single defect situated at x = 0, the solution to the equation of motion resulting from (2.36) is taken to be of the form  \( \psi_{j}^{A}(x,t) = \Theta(x)\psi_{j,+}^{A}(x,t)+\Theta(-x)\psi_{j,-}^{A}(x,t) \) , which means as before we distinguish here by notation the solutions (2.35) on the left and right of the defect,  \( \psi_{j,-}^{A}(x,t) \)  and  \( \psi_{j,+}^{A}(x,t) \) , respectively. Proceeding as before, the matching condition reads now

 \[ i\gamma^{1}\big(\psi_{j,+}^{A}(x,t)-\psi_{j,-}^{A}(x,t)\big)|_{x=0}=\left.\frac{\partial\mathcal{D}_{A D}(\bar{\psi},\psi,A_{\mu})}{\partial\bar{\psi}_{j}^{A}(x,t)}\right|_{x=0}. \quad (2.37) \]
 

It is clear, that in this case the transmission and reflection amplitudes will in addition to  \( \theta \)  and g also depend on the characteristic parameters of the laser field

 \[ T(\theta,g,E_{0},\omega,t)\qquad and\qquad R(\theta,g,E_{o},\omega,t). \quad (2.38) \] 

With regard to the main theme of this talk, it is clear that the laser field can be used to control the conductance. For instance defects which have transmission amplitudes of the form as the solid line in figure 1 (c), can be used as optically controllable switching devices. I want to deviate now slightly from the main line of argument and report briefly on an interesting phenomenon one can predict with solutions of the type (2.38).

## 2.5 Harmonic generation

Let me first briefly explain what harmonics are. The first experimental evidence can be traced back to the early sixties  \( [34] \) . Franken et al found that when hitting a crystalline quartz with a weak ultraviolet laser beam of frequency  \( \omega \) , it emits a frequency which is  \( 2\omega \) . Generalizing this phenomenon to higher multiples, one says nowadays that high harmonics generation is the non-linear response of a medium (a crystal, an atom, a gas, ...) to a laser field. Harmonic generation is important, since it allows to convert infrared input radiation of frequency  \( \omega \)  into light in the extreme ultraviolet regime whose frequencies are multiples of  \( \omega \)  (even up to order  \( \sim 1000 \) , see e.g.  \( [35] \)  for a recent review). A typical experimental spectrum is presented in figure 2.

In gases, composed of atoms or small molecules, this phenomenon is well-understood and, to some extent, even controllable in the sense that the frequency of the highest harmonic, the so-called “cut-off”, visible in figure 2, can be tuned as well as the intensities of particular groups of harmonics. In more complex systems, however, for instance solids, or larger molecules, high-harmonic generation is still an open problem. This is due to the fact that, until a few years ago, such systems were expected not to survive the strong laser fields one needs to produce such effects. How-

![](./images/867756429077905572_5.jpg)

Figure 2: Harmonic spectrum for Neon for a Ti:Sa laser with  \( \lambda = 795nm \) . Measured at the Max Born Institut Berlin [36]

ever, nowadays, with the advent of ultrashort pulses, there exist solid-state materials whose damage threshold is beyond the required intensities of  \( 10^{14}W/cm^{2} \)  [37]. As a direct consequence, there is an increasing interest in such materials as potential sources for high-harmonics. In fact, several groups are currently investigating this phenomenon in systems such as thin crystals [38, 39], carbon nanotubes [40], or organic molecules [41, 42].
 

We will therefore try to answer here the question, whether it is possible to generate harmonics from solid state devices and as a prototype of such a system we study a quantum wire coupled to the laser field in the way described in section 2.4.

In order to answer that question, we first have to study the spectrum of frequencies which is filtered out by the defect while the laser pulse is non-zero. The Fourier transforms of the reflection and transmission probabilities provide exactly this information

 \[ \mathcal{T}(\Omega,\theta,E_{0},\omega,\tau)=\frac{1}{\tau}\int_{0}^{\tau}d t|T(\theta,E_{0},\omega,t)|^{2}\cos(\Omega t), \quad (2.39) \] 

 \[ \mathcal{R}(\Omega,\theta,E_{0},\omega,\tau)=\frac{1}{\tau}\int_{0}^{\tau}d t|R(\theta,E_{0},\omega,t)|^{2}\cos(\Omega t). \quad (2.40) \] 

When parity is preserved for the reflection and transmission amplitudes, that is for real defects with  \( D^{*} = D \) , we have  \( |T|^{2} + |R|^{2} = 1 \) , and it suffices to consider T in the following.

## 2.5.1 Type I defects

Many features can be understood analytically. Taking the laser field in form of monochromatic light in the dipole approximation  \( (2.33) \) , we may naturally assume that the transmission probability for some particular defects can be expanded as

 \[ |T_{I}(\theta,U_{p},\omega,t)|^{2}=\sum_{k=0}^{\infty}t_{2k}(\theta)(4U_{p})^{k}\sin^{2k}(\omega t). \quad (2.41) \] 

We shall refer to defects which admit such an expansion as “type I defects”. Assuming that the coefficients  \( t_{2k}(\theta) \)  become at most 1, we have to restrict our attention to the regime  \( 4U_{p}<1 \)  in order for this expansion to be meaningful for all t. Note that this is no further limitation, since it is precisely the same constraint as already encountered for the validity of the dipole approximation (2.34). The functional dependence of (2.41) will turn out to hold for various explicit defects considered below. Based on this equation, we compute for such type of defect

 \[ \mathcal{T}(\Omega,\theta,U_{p},\omega,\tau)=\sum_{k=0}^{\infty}\frac{(2k)!(U_{p})^{k}\sin(\tau\Omega)t_{2k}(\theta)}{\tau\Omega\prod_{l=1}^{k}[l^{2}-(\Omega/2\omega)^{2}]}. \quad (2.42) \] 

It is clear from this expression that type I defects will preferably let even multiples of the basic frequency  \( \omega \)  pass, whose amplitudes will depend on the coefficients  \( t_{2k}(\theta) \) . When we choose the pulse length to be integer cycles, i.e.  \( \tau = 2\pi n/\omega \)  for  \( n \in Z \) , the expression in (2.42) reduces even further. The values at even multiples of the basic frequency are simply

 \[ \mathcal{T}_{I}(2n\omega,\theta,U_{p})=(-1)^{n}\sum_{k=0}^{\infty}t_{2k}(\theta)\left(U_{p}\right)^{k}\left(\begin{array}{c}2k\\ k-n\end{array}\right), \quad (2.43) \] 

which becomes independent of the pulse length  \( \tau \) . Notice also that the dependence on  \( E_{0} \)  and  \( \omega \)  occurs in the combination of the ponderomotive energy  \( U_{p} \) . Further statements require the precise form of the coefficients  \( t_{2k}(\theta) \)  and can only be made with regard to a more concrete form of the defect.
 

## 2.5.2 Type II defects

Clearly, not all defects are of the form  \( (2.41) \)  and we have to consider also expansions of the type

 \[ |T_{I I}(\theta,E_{0}/e,\omega,t)|^{2}=\sum_{k,p=0}^{\infty}t_{2k}^{p}(\theta)\frac{E_{0}^{2k+p}}{\omega^{2k}}\cos^{p}(\omega t)\sin^{2k}(\omega t). \quad (2.44) \] 

We shall refer to defects which admit such an expansion as “type II defects”. In this case we obtain

 \[ \begin{align*}\mathcal{T}_{II}(\Omega,\theta,E_{0}/e,\omega,\tau)&=\sum_{k,p=0}^{\infty}\sum_{l=0}^{p}\binom{p}{l}\frac{\Omega\sin(\tau\Omega)}{(-1)^{l+1}\tau\omega^{2+2k}}E_{0}^{2k+2p}\\&\quad\times\left(\frac{(2k+2l)!t_{2k}^{2p}(\theta)}{\prod_{q=0}^{k+l}[(2q)^{2}-(\frac{\Omega}{\omega})^{2}]}+\frac{(2k+2l)!t_{2k}^{2p+1}(\theta)E_{0}}{\prod_{q=1}^{k+l+1}[(2q-1)^{2}-(\frac{\Omega}{\omega})^{2}]}\right).\end{align*} \quad (2.45) \] 

We observe from this expression that type II defects will filter out all multiples of  \( \omega \) . For the pulse being once again of integer cycle length, this reduces to

 \[ \mathcal{T}_{I I}(2n\omega,\theta,U_{p},E_{0})=\sum_{k,p=0}^{\infty}\sum_{l=0}^{p}(-1)^{l+n}\frac{t_{2k}^{2p}(\theta)}{2^{2l-2p}}\left(U_{p}\right)^{k+p}E_{0}^{2p}\left(\begin{array}{c}p\\ l\end{array}\right)\left(\begin{array}{l}2k+2l\\ k+l-n\end{array}\right) \quad (2.46) \] 

and

 \[ \begin{align*}\mathcal{T}_{II}((2n-1)\omega,\theta,E_{0}/e)&=\sum_{k,p=0}^{\infty}\sum_{l=0}^{p}(-1)^{l+n+1}\frac{t_{2k}^{2p+1}(\theta)}{2^{2l-2p+1}}\left(U_{p}\right)^{k+p}\\&\quad\times\left(\begin{array}{c}p\\ l\end{array}\right)\frac{(2k+2l)!(2n-1)E_{0}^{2p+1}}{(l+k-n+1)!(l+n+k)!},\end{align*} \quad (2.47) \] 

which are again independent of  \( \tau \) . We observe that in this case we can not combine the  \( E_{0} \)  and  \( \omega \)  into a  \( U_{p} \) .

## 2.5.3 One particle approximation

In spite of the fact that we are dealing with a quantum field theory, it is known that a one particle approximation to the Dirac equation is very useful and physically sensible when the external forces vary only slowly on a scale of a few Compton wavelengths, see e.g. [43]. We may therefore define the spinor wavefunctions

 \[ \Psi_{j,u,\theta}(x,t):=\psi_{j}^{A}(x,t)\frac{\left|a_{j}^{\dagger}(\theta)\right\rangle}{\sqrt{2\pi^{2}p_{j}^{0}}}=\frac{e^{-i\vec{p}_{j}\cdot\vec{x}}}{\sqrt{2\pi p_{j}^{0}}}u_{j}(\theta) \quad (2.48) \] 

 \[ \Psi_{j,v,\theta}(x,t)^{\dagger}:=\psi_{j}^{A}(x,t)^{\dagger}\frac{\left|a_{j}^{\dagger}(\theta)\right\rangle}{\sqrt{2\pi^{2}p_{j}^{0}}}=\frac{e^{-i\vec{p}_{j}\cdot\vec{x}}}{\sqrt{2\pi p_{j}^{0}}}v_{j}(\theta)^{\dagger}. \quad (2.49) \]
 

With the help of these functions we obtain then for the defect system

 \[ \begin{align*}\Psi_{i,u,\theta}^{A}(x,t):=\psi_{i}^{A}(x,t)\frac{\left|a_{i,-}^{\dagger}(\theta)\right\rangle}{\sqrt{2\pi^{2}p_{i}^{0}}}=\Theta(-x)\left[\Psi_{i,u,\theta}(x,t)+\Psi_{i,u,-\theta}(x,t)R_{i}^{*}(\theta)\right]\\+\Theta(x)T_{i}^{*}(\theta)&\left[\Psi_{i,u,\theta}(x,t)+\Psi_{i,u,-\theta}(x,t)\tilde{R}_{i}^{*}(-\theta)\right]\end{align*} \quad (2.50) \] 

and the same function with  \( u \rightarrow v \) . Since this expression resembles a free wave, it can not be normalized properly and we have to localize the wave in form of a wave packet by multiplying with an additional function,  \( \tilde{g}(p,t) \)  in (2.20) and its counterpart  \( g(x,t) \)  in (2.50), typically a Gaussian. Then for the function  \( \Phi_{i,u,\theta}^{A}(x,t) = g(x,t)\Psi_{i,u,\theta}^{A}(x,t) \) , we can achieve that  \( \|\Phi\| = 1 \) .

## 2.5.4 Harmonic spectra

We are now in the position to determine the emission spectrum for which we need to compute the absolute value of the Fourier transform of the dipole moment

 \[ \mathcal{X}_{j,u,\theta}(\Omega)=\left|\int_{0}^{\tau}d t\left\langle\Phi_{j,u,\theta}^{A}(x,t)^{\dagger}x\Phi_{j,u,0}^{A}(x,t)\right\rangle\exp i\Omega t\right|. \quad (2.51) \] 

We localize now the wave packet in a region much smaller than the classical estimate for the maximal amplitude the electron will acquire when following the laser field. We achieve this with a Gaußian  \( g(x,t)=\exp(-x^{2}/\Delta) \) , where  \( \Delta\ll eE_{0}/\omega^{2} \) .

## 2.5.5 An example: Impurity of energy operator type

As mentioned this type of defect, i.e.  \( \mathcal{D}(\bar{\psi},\psi)=g\bar{\psi}\psi(x) \)  can be obtained in a limit from the defect discussed in section 2.3.1. Coupling the vector potential minimally to it yields

 \[ \mathcal{D}_{A D}(\bar{\psi},\psi,A_{\mu})=g\bar{\psi}(1+e/m\gamma^{\mu}A_{\mu})\psi, \quad (2.52) \] 

by invoking the equation of motion. We can now determine the reflection and transmission amplitudes as outlined above

 \[ \begin{align*}R_{i}(\theta,g,A/e,y)&=\tilde{R}_{i}(\theta,g,-A/e,-y)=R_{i}(\theta,g,A/e,-y)=\tilde{R}_{i}(\theta,g,-A/e,y)=\\&\frac{[y\dot{A}-\cosh\theta]e^{-2iy\sinh\theta}}{[1-y\dot{A}\cosh\theta]-i\frac{q}{4}[\frac{4}{g^{2}}+1+A^{2}-y^{2}\dot{A}^{2}]\sinh\theta}.\end{align*} \quad (2.53) \] 

We denoted the differentiation with respect to time by a dot. The transmission amplitudes turn out to be

 \[ \begin{align*}T_{i}(\theta,g,A/e,y)&=\tilde{T}_{i}(\theta,g,-A/e,-y)=T_{i}(\theta,g,- A/e,y)=\tilde{T}_{i}(\theta,g,A/e,-y)=\\&\quad i\left[1-y^{2}\dot{A}^{2}+(A-\frac{2i}{g})^{2}\right]\sinh\theta\\&\frac{4}{g}[1-y\dot{A}\cosh\theta]-i[\frac{4}{g^{2}}+1+A^{2}-y^{2}\dot{A}^{2}]\sinh\theta.\end{align*} \quad (2.54) \] 

Locating the defect at y = 0, the derivative of A does not appear anymore explicitly in (2.53) and (2.54), such that it is clear that this defect is of type I and admits an expansion of
 

the form (2.41). With the explicit expressions (2.53) and (2.54) at hand, we can determine all the coefficients  \( t_{2k}(\theta) \)  in (2.41) analytically. For this purpose let us first bring the transmission amplitude into the more symmetric form

 \[ |T_{i}(\theta,g,A/e)|^{2}=\frac{\tilde{a}_{0}(\theta,g)+a_{2}(\theta,g)A^{2}+a_{4}(\theta,g)A^{4}}{a_{0}(\theta,g)+a_{2}(\theta,g)A^{2}+a_{4}(\theta,g)A^{4}}, \quad (2.55) \] 

with

 \[ a_{0}(\theta,g)=16g^{2}+(4+g^{2})^{2}\sinh^{2}\theta,\qquad\tilde{a}_{0}(\theta,g)=(g^{2}-4)^{2}\sinh^{2}\theta, \quad (2.56) \] 

 \[ a_{2}(\theta,g)=2g^{2}(4+g^{2})\sinh^{2}\theta,\quad a_{4}(\theta,g)=g^{4}\sinh^{2}\theta. \quad (2.57) \] 

We can now expand  \( |T(\theta,g,A)|^{2} \)  in powers of the field  \( A(t) \)  and identify the coefficients  \( t_{2k}(\theta,g) \)  in (2.41) thereafter. To achieve this we simply have to carry out the series expansion of the denominator in (2.55). The latter admits the following compact form

 \[ \frac{1}{a_{0}(\theta,g)+a_{2}(\theta,g)A^{2}+a_{4}(\theta,g)A^{4}}=\sum_{k=0}^{\infty}c_{2k}(\theta,g)A^{2k}, \quad (2.58) \] 

with  \( c_{0}(\theta,g)=1/a_{0}(\theta,g) \)  and

 \[ c_{2k}(\theta,g)=-\frac{c_{2k-2}(\theta,g)a_{2}(\theta,g)+c_{2k-4}(\theta,g)a_{4}(\theta,g)}{a_{0}(\theta,g)}, \quad (2.59) \] 

for k > 0. We understand here that all coefficients  \( c_{2k} \)  with k < 0 are vanishing, such that from this formula all the coefficients  \( c_{2k} \)  may be computed recursively. Hence, by comparing with the series expansion (2.41), we find the following closed formula for the coefficients  \( t_{2k}(\theta, g) \) 

 \[ t_{2k}(\theta,g)=[\tilde{a}_{0}(\theta,g)-a_{0}(\theta,g)]c_{2k}(\theta,g)\quad k>0. \quad (2.60) \] 

The first coefficients then simply read

 \[ t_{0}(\theta,g)=\frac{\tilde{a}_{0}(\theta,g)}{a_{0}(\theta,g)}=|T(\theta,E_{0}=0)|^{2}, \quad (2.61) \] 

 \[ t_{2}(\theta,g)=\frac{a_{2}(\theta,g)}{a_{0}(\theta,g)}\left[1-t_{0}(\theta,g)\right]=\frac{8g^{4}(4+g^{2})\sinh^{2}2\theta}{(16g^{2}+(4+g^{2})^{2}\sinh^{2}\theta)^{2}}, \quad (2.62) \] 

 \[ t_{4}(\theta,g)=\left[\frac{a_{4}(\theta,g)}{a_{2}(\theta,g)}-\frac{a_{2}(\theta,g)}{a_{0}(\theta,g)}\right]t_{2}(\theta,g), \quad (2.63) \] 

and so on. It is now clear how to obtain also the higher terms analytically, but since they are rather cumbersome we do not report them here.

Having computed the coefficients  \( t_{2k} \) , we can evaluate the series (2.42) and (2.43) in principle to any desired order. For some concrete values of the laser and defect parameters the results of our evaluations are depicted in figure 3.

The main observation from part (a) is that the defect acts as a filter selecting higher harmonics of even order of the laser frequency. Furthermore, from the zoom of the peak
 
![](./images/867756429077905572_6.jpg)

![](./images/867756429077905572_7.jpg)

![](./images/867756429077905572_8.jpg)

![](./images/867756429077905572_9.jpg)

Figure 3: Fourier transform of the transmission probability for a single (a) and double (b) defect with  \( E_{0}=2.0 \) , g=3.5,  \( \theta=1.2 \) ,  \( \omega=0.2 \) . Harmonic emission spectrum for a single (c) and double (d) defect with  \( E_{0}=2.0 \) , g=3.5,  \( \theta=1.2 \) ,  \( \omega=0.2 \) ,  $ \Delta=6.

regions, we see that there are satellite peaks appearing near the main harmonics. They reduce their intensity when  \( \tau \)  is increased, such that with longer pulse length the harmonics become more and more pronounced. We also investigated that for different frequencies  \( \omega \)  the general structure will not change. Increasing the field amplitude  \( E_{0} \) , simply lifts up the whole plot without altering very much its overall structure. We support these findings in two alternative ways, either by computing directly (2.39) numerically or, more instructively, by evaluating the sums (2.42) and (2.43).

Part (b) shows the analysis for a double defect system with one defect situated at x = 0 and the other at x = y. The double defect amplitudes are computed directly from (2.12) and (2.13) with the expression for the single defect (2.53) and (2.54). Since now both A and  \( \hat{A} \)  appear explicitly in the formulae for the  \( R' \) s and  \( T' \) s, it is clear that the expansion of the double defect can not be of type I, but it turns out to be of type II, i.e. of the form (2.44). Hence, we will now expect that besides the even also the odd multiples of  \( \omega \)  will be filtered out, which is indeed visible in part (b) for various distances. Here we have only plotted a continuous spectrum for y = 0.5, whereas for reasons of clarity, we only drew the enveloping function which connects the maxima of the harmonics for
 

the remaining distances. We observe that now not only odd multiples of the frequency emerge in addition to the ones in (a) as harmonics, but also that we obtain much higher harmonics and the cut-off is shifted further to the ultraviolet. Furthermore, we observe a regular pattern in the enveloping function, which appears to be independent of y. Similar patterns were observed before in the literature, as for instance in the context of atomic physics described by a Klein-Gordon formalism (see figure 2 in [44]).

Coming now to the main point of our analysis we would like to see how this structure is reflected in the harmonic spectra. The result of the evaluation of  \( (2.51) \)  is depicted in figure 3 parts (c) and (d). We observe a very similar spectrum as we have already computed for the Fourier transform of the transmission amplitude, which is not entirely surprising with regard to the expression  \( (2.51) \) . The cut-off frequencies are essentially identical. From the comparison between X and the enveloping function for T we deduce, that the term involving the transmission amplitude clearly dominates the spectrum.

The important general deduction from these computations is of course that harmonics of higher order do emerge in the emission spectrum of impurity systems, such that harmonics can be generated from solid state devices.

## 3. Conductance from the Kubo formula

Having characterized various features of defects, I will proceed with the main theme of the talk, that is the computation of the DC conductance. In the absence of impurities it can be obtained from the Kubo formula in the form

 \[ G(T)=-\lim_{\omega\rightarrow0}\frac{1}{2\omega\pi^{2}}\int_{-\infty}^{\infty}d t e^{i\omega t}\left\langle J(t)J(0)\right\rangle_{T,m}. \quad (3.1) \] 

We proposed in [1] a generalization of (3.1) in the form of (1.1). The key quantity needed for the explicit computation of (3.1) or (1.1) are the occurrence of the temperature dependent current-current correlation functions  \( \langle J(r)J(0)\rangle_{T,m} \)  or  \( \langle J(r)Z_{\alpha}J(0)\rangle_{T,m} \) , respectively.

In the zero temperature regime two-point correlation functions can be computed in general by means of the form factor bootstrap approach  \( [15, 16, 17] \) . In this approach one expands the two-point function between two local operators O and  \( O' \)  in terms of the series

 \[ \begin{align*}\left\langle\mathcal{O}(r)\mathcal{O}^{\prime}(0)\right\rangle_{T=0,m}=\sum_{n=1}^{\infty}\sum_{\mu_{1}\cdots\mu_{n}}\int\frac{d\theta_{1}\cdots d\theta_{n}}{n!(2\pi)^{n}}\prod_{i=1}^{n}e^{-rm_{i}\cosh\theta_{i}}\\ \times F_{n}^{\mathcal{O}|\mu_{1}\cdots\mu_{n}}(\theta_{1},\ldots,\theta_{n})\left[F_{n}^{\mathcal{O}^{\prime}|\mu_{1}\cdots\mu_{n}}(\theta_{1},\ldots,\theta_{n})\right]^{*},\end{align*} \quad (3.2) \] 

where we choose  \(  x^{\mu} = (-ir, 0)  \) . The form factors are defined as matrix elements of the local operator  \(  \mathcal{O}(\vec{x})  \)  located at the origin between a multiparticle in-state and the vacuum,

 \[ F_{n}^{\mathcal{O}|\mu_{1}\cdots\mu_{n}}(\theta_{1},\theta_{2}\cdots,\theta_{n}):=\langle0|\mathcal{O}(0)|Z_{\mu_{1}}^{\dagger}(\theta_{1})Z_{\mu_{2}}^{\dagger}(\theta_{2})\cdots Z_{\mu_{n}}^{\dagger}(\theta_{n})\rangle. \quad (3.3) \] 

The expansion (3.2) is simply obtained by inserting complete states on the r.h.s. One may proceed similarly by inserting one more set of complete states when a defect is present and
 

obtains

 \[ \begin{align*}\langle J(r)Z_{\alpha}J(0)\rangle_{T=0,m}=&\sum_{n,m=1}^{\infty}\sum_{\mu_{1}\cdots\mu_{n};\nu_{1}\cdots\nu_{m}}\int\frac{d\theta_{1}\cdots d\theta_{n}d\tilde{\theta}_{1}\cdots d\tilde{\theta}_{m}}{m!n!(2\pi)^{n+m}}F_{n}^{J|\mu_{1}\cdots\mu_{n}}(\theta_{1}\cdots\theta_{n})\\&\times\left\langle Z_{\mu_{n}}(\theta_{n})\cdots Z_{\mu_{1}}(\theta_{1})|Z_{\alpha}|Z_{\nu_{1}}(\tilde{\theta}_{1})\cdots Z_{\nu_{m}}(\tilde{\theta}_{m})\right\rangle F_{m}^{J|\nu_{1}\cdots\nu_{m}}(\tilde{\theta}_{1}\cdots\tilde{\theta}_{m})^{*}e^{-r\sum_{i=1}^{n}m_{i}\cosh\theta_{i}}.\end{align*} \quad (3.4) \] 

This means there are three principle steps left in order to obtain the conductance from the expression in (1.1). (a) The computation of the form factors (3.3) and the matrix elements involving the defect operator occurring in (3.4). (b) The integration in r and (c) the limit  \( \omega \rightarrow 0 \) . Step (a) can be performed in two alternative ways either by solving certain consistency equations for the form factors and defect matrix elements or by direct computation. For the latter we require a representation for the particle creation operators  \( Z_{\mu}(\theta) \) , the defect operator  \( Z_{\alpha} \)  and the local operator  \( \mathcal{O}(r) \)  which is the current in this case.

## 3.1 The massless limit

Remarkably when carrying out the massless limit of the above expressions, the steps (b) and (c) can be carried out generically. To perform such a limit we proceed according to the massless limit prescription as suggested originally in [45]. It consists of carrying out the limit  \( m \rightarrow 0 \)  in the high energy regime. In order to do this one replaces in every rapidity dependent expression  \( \theta \)  by  \( \theta \pm \sigma \) , where an additional auxiliary parameter  \( \sigma \)  has been introduced. Thereafter one takes the limit  \( \sigma \rightarrow \infty \) ,  \( m \rightarrow 0 \)  while keeping the quantity  \( \hat{m} = m/2 \exp(\sigma) \)  finite. For instance, carrying out this prescription for the momentum yields  \( p_{\pm} = \pm \hat{m} \exp(\pm \theta) \) , such that one may view the model as split into its two chiral sectors and one can speak naturally of left (L) and right (R) movers. For the form factors in (3.4) the massless limit yields

 \[ \lim_{\sigma\to\infty}F_{n}^{\mathcal{O}|\mu_{1}\cdots\mu_{n}}(\theta_{1}+\eta_{1}\sigma,\cdots,\theta_{n}+\eta_{n}\sigma)=F_{v_{1}\cdots v_{n}}^{\mathcal{O}|\mu_{1}\cdots\mu_{n}}(\theta_{1},\cdots,\theta_{n}), \quad (3.5) \] 

with  \( \eta_{i}=\pm1 \)  and  \( \nu_{i}=R \)  for  \( \eta_{i}=+ \)  and  \( \nu_{i}=L \)  for  \( \eta_{i}=- \) . Namely, in the massless limit every massive n-particle form factor is mapped into  \( 2^{n} \)  massless form factors. Using these expressions, performing a Wick rotation and introducing the variable  \( E=\sum_{i=1}^{n}\hat{m}_{i}e^{\theta_{i}} \) , we obtain from (3.4)

 \[ \begin{align*}&\langle J(r)Z_{\alpha}J(0)\rangle_{T=m=0}=\sum_{n,m=1}^{\infty}\sum_{\mu_{1}\cdots\mu_{n};\nu_{1}\cdots\nu_{m}}\int\frac{d\theta_{1}\cdots d\theta_{n}d\tilde{\theta}_{1}\cdots d\tilde{\theta}_{m}}{m!n!(2\pi)^{n+m}}F_{R_{1}\cdots R_{n}}^{J|\mu_{1}\cdots\mu_{n}}(\theta_{1},\cdots,\theta_{n})\\&\times\left\langle Z_{\mu_{n}}^{R}(\theta_{n})\cdots Z_{\mu_{1}}^{R}(\theta_{1})|Z_{\alpha}|Z_{\nu_{1}}^{R}(\tilde{\theta}_{1})\cdots Z_{\nu_{m}}^{R}(\tilde{\eta}_{n})\right\rangle F_{R_{1}\cdots R_{m}}^{J|\nu_{1}\cdots\nu_{m}}(\tilde{\theta}_{1},\cdots,\tilde{\theta}_{m})^{*}e^{-i r E}.\end{align*} \quad (3.6) \] 

We note that for the massless prescription to work, the matrix element involving the defect  \( Z_{\alpha} \)  can only depend on the rapidity differences, which will indeed be the case as we see below. Performing the variable transformation  \( \theta_{n} \rightarrow \ln E'/\hat{m}_{n} - \sum_{i=1}^{n} \hat{m}_{i}/\hat{m}_{n} e^{\theta_{i}} \) , we rewrite the r.h.s. of (3.6) as

 \[ \sum_{n,m=1}^{\infty}\sum_{\mu_{1}\cdots\mu_{n};\nu_{1}\cdots\nu_{m}}\int_{0}^{E}d E^{\prime}\int_{-\infty}^{\ln E^{\prime}/\hat{m}_{n}}\frac{d\theta_{1}\cdots d\theta_{n-1}}{n!(2\pi)^{n}}\int_{-\infty}^{\infty}\frac{d\tilde{\theta}_{1}\cdots d\tilde{\theta}_{m}}{m!(2\pi)^{m}}F_{R_{1}\cdots R_{n}}^{J|\mu_{1}\cdots\mu_{n}}(\theta_{1},\cdots,\theta_{n}(E^{\prime})) \]
 

 \[ \times\left\langle Z_{\mu_{n}}^{R}(\theta_{n}(E^{\prime}))\cdots Z_{\mu_{1}}^{R}(\theta_{1})|Z_{\alpha}|Z_{\nu_{1}}^{R}(\tilde{\theta}_{1})\cdots Z_{\nu_{n}}^{R}(\tilde{\eta}_{m})\right\rangle F_{R_{1}\cdots R_{m}}^{J|\nu_{1}\cdots\nu_{m}}(\tilde{\theta}_{1},\cdots,\tilde{\theta}_{m})^{*}e^{-i r E^{\prime}}. \quad (3.7) \] 

We substitute now this correlation function into the Kubo formula, shift all rapidities as  \( \theta_{i} \rightarrow \theta_{i} + \ln E'/\hat{m}_{n} \) ,  \( \tilde{\theta}_{i} \rightarrow \tilde{\theta}_{j} + \ln E'/\hat{m}_{n} \) , use the Lorentz invariance of the form factors \( ^{2} \)  and carry out the integration in  \( dE' \) 

 \[ \begin{align*}G^{\alpha}=&\lim_{\omega\to0}\frac{\omega^{2s-2}}{\hat{m}_{n}^{2s}\pi}\sum_{\mu_{1}\cdots\mu_{n};\nu_{1}\cdots\nu_{m}\sim\infty}\int\limits_{-\infty}^{0}\frac{d\theta_{1}\cdots d\theta_{n-1}}{n!(2\pi)^{n}}\int\limits_{-\infty}^{\infty}\frac{d\tilde{\theta}_{1}\cdots d\tilde{\theta}_{m}}{m!(2\pi)^{m}}\frac{1}{1-\sum_{i=1}^{n-1}\hat{m}_{i}/\hat{m}_{n}e^{\theta_{i}}}\\&\times\left\langle Z_{\mu_{n}}^{R}(\ln(1-\sum_{i=1}^{n-1}\hat{m}_{i}/\hat{m}_{n}e^{\theta_{i}}))\cdots Z_{\mu_{1}}^{R}(\theta_{1})|Z_{\alpha}|Z_{\nu_{1}}^{R}(\tilde{\theta}_{1})\cdots Z_{\nu_{m}}^{R}(\tilde{\eta}_{m})\right\rangle\\&\times F_{R_{1}\cdots R_{n}}^{J|\mu_{1}\cdots\mu_{n}}(\theta_{1},\cdots,\ln(1-\sum_{i=1}^{n-1}\hat{m}_{i}/\hat{m}_{n}e^{\theta_{i}}))F_{R_{1}\cdots R_{m}}^{J|\nu_{1}\cdots\nu_{m}}(\tilde{\theta}_{1},\cdots,\tilde{\theta}_{m})^{*}.\end{align*} \quad (3.8) \] 

We state various observations: Since the matrix element involving the defect only depends on the rapidity difference, it is not affected by the shifts. Operators with Lorentz spin s = 1 play a very special role in (3.8), which makes the current operator especially distinguished. In that case the r.h.s. of (3.8) becomes independent of the frequency  \( \omega \)  and the limit is carried out trivially. Furthermore, since the final expression has to be independent of  \( \hat{m}_{n} \) , we deduce that the form factors have to be linearly dependent on  \( \hat{m}_{n} \) .

## 3.2 Realization of the defect operator

A realization of  \( Z_{\alpha} \)  can be achieved very much in analogy to a realization of local operators, i.e. as exponentials of bilinears in Zamolodchikov–Faddeev operators [46]. For the case of a boundary a generic model independent realization for the boundary operator B was originally proposed in [28] for the parity invariant case, i.e.  \( R = \tilde{R} \) . This proposal was generalized to the defect operator in [26] with the same restriction and for self-conjugated particles. Here we extend this realization in order to incorporate the possibility of parity breaking as well as non self-conjugated particles. A non-trivial consistency check for the validity of our proposal will be ultimately provided when exploiting it in the computation of the conductance, obtained by entirely different means as will be presented in part II. The realization we want to propose here is a direct generalization of the one presented in [26], namely

 \[ Z_{\alpha}=:\exp[\frac{1}{4\pi}\int_{-\infty}^{\infty}D_{\alpha}(\theta)d\theta]:, \quad (3.9) \] 

where : : denotes normal ordering and the operator  \( D_{\alpha}(\theta) \)  has the form

 \[ \begin{align*}D_{\alpha}(\theta)=&\sum_{i}\left[K_{i}^{\alpha}(\theta)Z_{i}^{\dagger}(\theta)Z_{ i}^{\dagger}(-\theta)+\tilde{K}_{i}^{\alpha}(\theta)^{*}Z_{i}(-\theta)Z_{i}(\theta)\right.\\&\left.+W_{i}^{\alpha}(\theta)Z_{i}^{\dagger}(\theta)Z_{ i}(\theta)+\tilde{W}_{i}^{\alpha}(\theta)^{*}Z_{i}^{\dagger}(-\theta)Z_{i}(-\theta)\right],\end{align*} \quad (3.10) \] 

 \( ^{2} \) Denoting by s the Lorentz spin of the operator O and  \( \lambda \)  being a constant, the form factors satisfy

 \[ F_{n}^{\mathcal{O}|\mu_{1}\cdots\mu_{n}}(\theta_{1}+\lambda,\cdots,\theta_{n}+\lambda)=e^{s\lambda}F_{n}^{\mathcal{O}|\mu_{1}\cdots\mu_{n}}(\theta_{1},\cdots,\theta_{n}). \]
 

with  \( K_{i}^{\alpha}(\theta):=R_{i}^{\alpha}(\frac{i\pi}{2}-\theta) \) ,  \( \tilde{K}_{i}^{\alpha}(\theta):=\tilde{R}_{i}^{\alpha}(\frac{i\pi}{2}-\theta) \) ,  \( W_{i}^{\alpha}(\theta):=T_{i}^{\alpha}(\frac{i\pi}{2}-\theta) \)  and  \( \tilde{W}_{i}^{\alpha}(\theta):=\tilde{T}_{i}^{\alpha}(\frac{i\pi}{2}-\theta) \) . In comparison with [26] we have used a slightly different normalization factor, since in general we have contributions in the sum over i in (3.10) including both particles and anti-particles, as for the complex free Fermion we shall treat below. Following the arguments given in [28], the operator  \( D_{\alpha}(\theta) \)  depends on the amplitudes  \( R(\theta) \) ,  \( T(\theta) \) , and  \( \tilde{R}(\theta) \)  and  \( \tilde{T}(\theta) \)  with their arguments shifted, as considered also in [24, 26].

## 3.3 Defect matrix elements

Having now a concrete generic realization of the defect (3.9), we can compute the defect matrix elements. One way of doing this is to solve a set of consistency equations which relate the lower particle matrix elements to higher particle ones, similar as in the standard form factor program  \( [15, 16, 17] \) . Such kind of iterative equations were proposed in  \( [24] \)  for a parity invariant defect and for a real free fermionic and bosonic theory. We generalize this here and note first that the operator (3.9) becomes

 \[ \lim_{R,\tilde{R}\to0;T,\tilde{T}\to1}Z_{\alpha}=\exp[\frac{1}{2\pi}\int_{-\infty}^{\infty}d\theta\sum_{i}Z_{i}^{\dagger}(\theta)Z_{i}(\theta)]\;; \quad (3.11) \] 

and the defect should act in this case as the identity operator, which fixes our normalization to  \( \langle Z_{i}(\theta_{1})Z_{\alpha}Z_{j}^{\dagger}(\theta_{2})\rangle = 2\pi\delta(\theta_{12})\delta_{ij} \)  after having contracted according to Wick's theorem. For two particles we find,

 \[ \langle Z_{i}(\theta_{1})Z_{i}(\theta_{2})Z_{\alpha}\rangle=\pi\hat{K}_{i}^{\alpha}(\theta_{2})\delta(\hat{\theta}_{12}), \quad (3.12) \] 

 \[ \langle Z_{\alpha}Z_{i}^{\dagger}(\theta_{1})Z_{i}^{\dagger}\big(\theta_{2}\big)\rangle=\pi\hat{K}_{i}^{\alpha}(\theta_{1})^{*}\delta(\hat{\theta}_{12}), \quad (3.13) \] 

 \[ \langle Z_{i}(\theta_{1})Z_{\alpha}Z_{j}^{\dagger}(\theta_{2})\rangle=\pi\tilde{W}_{i}^{\alpha}(\theta_{1})\delta(\theta_{12})\delta_{i j}. \quad (3.14) \] 

For later convenience we have introduced the functions

 \[ \hat{K}_{i}^{\alpha}(\theta)=K_{i}^{\alpha}(\theta)+S_{i i}(-2\theta)K_{i}^{\alpha}(-\theta)=\tilde{K}_{i}^{\alpha}(\theta)+S_{i i}(2\theta)\tilde{K}_{i}^{\alpha}(-\theta), \quad (3.15) \] 

 \[ \tilde{W}_{i}^{\alpha}(\theta)=W_{i}^{\alpha}(\theta)+\tilde{W}_{i}^{\alpha}(-\theta)^{*}=\tilde{W}_{i}^{\gamma}(\theta)+W_{i}^{\alpha}(\theta)^{*}=\tilde{W}_{i}^{\alpha}(\theta)*, \quad (3.16) \] 

since the  \( K_{i}^{\alpha} \) ,  \( \tilde{K}_{i}^{\alpha} \)  \( ,W_{i}^{\alpha} \)   and  \( \tilde{W}_{i}^{\alpha} \)  amplitudes defined before will repeatedly appear in the combinations (3.15), (3.16) in what follows. The latter equalities in (3.15), (3.16) follow simply from

 \[ \tilde{W}_{i}^{\alpha}(\theta)=W_{i}^{\alpha}(-\theta)=\tilde{W}_{i}^{\alpha}(i\pi-\theta)^{*},\tilde{K}_{i}^{\alpha}(\theta)=S_{i i}(2\theta)K_{i}^{\alpha}(-\theta)=S_{i i}(2\theta)\tilde{K}_{i}^{\alpha}(i\pi-\theta)^{*}, \quad (3.17) \] 

which are in turn consequences of the crossing-hermiticity properties (2.3)-(2.4). With these matrix elements we can construct the ones involving more particles recursively from

 \[ F_{\alpha}^{\mu_{m}\cdots\mu_{1}\nu_{1}\cdots\nu_{n}}^{\mu}(\theta_{m}\cdots\theta_{1},\theta_{1}^{\prime}\cdots\theta_{n}^{\prime}):=\left\langle Z_{\mu_{m}}(\theta_{m})\cdots Z_{\mu_{1}}(\theta_{1})Z_{\alpha}Z_{\nu_{1}}^{\dagger}(\theta_{1}^{\prime})\cdots Z_{\nu_{n}}^{\dagger}(\theta_{n}^{\prime})\right\rangle= \] 

 \[ \pi\sum_{l=2}^{m}\delta_{\mu_{1}\bar{\mu}_{l}}\delta(\hat{\theta}_{1l})\hat{K}_{\mu_{1}}^{\alpha}(\theta_{1})\prod_{p=1}^{l-1}S_{\mu_{1}\mu_{p}}(\theta_{1p})F_{\alpha}^{\mu_{m}\cdots\bar{\mu}_{l}\cdots\mu_{2}\nu_{1}\cdots\nu_{n}}(\theta_{m}\cdots\hat{\theta}_{l}\cdots\theta_{2},\theta_{1}^{\prime}\cdots\theta_{n}^{\prime}) \quad (3.18) \] 

 \[ +\pi\sum_{l=1}^{n}\delta_{\mu_{1}\nu_{l}}\delta(\theta_{1}-\theta_{l}^{\prime})\hat{W}_{\mu_{1}}^{\alpha}(\theta_{1})\prod_{p=1}^{l-1}S_{\mu_{1}\nu_{p}}(\theta_{1p})F_{\alpha}^{\mu_{m}\cdots\mu_{2}\nu_{1}\cdots\bar{\nu}_{l}\cdots\nu_{n}}(\theta_{m}\cdots\theta_{2},\theta_{1}^{\prime}\cdots\hat{\theta}_{l}^{\prime}\cdots\theta_{n}^{\prime}) \]
 

 \[ \begin{align*}&F_{\alpha}^{\mu_{m}\cdots\mu_{1}\nu_{1}\cdots\nu_{n}}(\theta_{m}\cdots\theta_{1},\theta_{1}^{\prime}\cdots\theta_{n}^{\prime})=\\&\quad\pi\sum_{l=2}^{n}\delta_{\nu_{l}\bar{\nu}_{l}}\delta(\hat{\theta}_{l1}^{\prime})\hat{K}_{\nu_{1}}^{\alpha}(\theta_{1}^{\prime})^{*}\prod_{p=1}^{l-1}S_{\nu_{1}\mu_{p}}(\theta_{1p})F_{\alpha}^{\mu_{m}\cdots\mu_{1}\nu_{2}\cdots\bar{\nu}_{l}\cdots\nu_{n}}(\theta_{m}\cdots\theta_{1},\theta_{2}^{\prime}\cdots\bar{\theta}_{l}^{\prime}\cdots\theta_{n}^{\prime})\\&\quad+\pi\sum_{l=1}^{m}\delta_{\nu_{1}\mu_{l}}\delta(\theta_{1}^{\prime}-\theta_{l})\hat{W}_{\nu_{1}}^{\alpha}(\theta_{1}^{\prime})^{*}\prod_{p=1}^{l-1}S_{\nu_{1}\mu_{p}}(\theta_{1p})F_{\alpha}^{\mu_{m}\cdots\bar{\mu}_{l}\cdots\mu_{1}\nu_{2}\cdots\nu_{n}}(\theta_{m}\cdots\bar{\theta}_{l}\cdots\theta_{1},\theta_{2}^{\prime}\cdots\theta_{n}^{\prime}).\end{align*} \quad (3.19) \] 

Here we denoted with the check on the rapidities  \( \hat{\theta} \)  the absence of the corresponding particle in the matrix element. It is clear from the expressions (3.9) and (3.10) that the only possible non-vanishing matrix elements (3.18) are those when  \( n + m \)  is even. Taking (3.12)-(3.14) as the initial conditions for the recursive equations (3.18)-(3.19), we can now either solve them iteratively or use (3.9) and evaluate the matrix elements directly. Closed solutions for these equations have been presented for the first time in [1].

## 3.4 Free Fermion wire with impurities

At this point we have to abandon the general discussion and consider a concrete theory, which for the reasons already explained we choose to be the complex free Fermion. Then the generators of the ZF-algebra  \( Z_{i}(\theta) \) ,  \( Z_{i}^{\dagger}(\theta) \)  are just the usual creation and annihilation operators  \( a_{i}(\theta) \) ,  \( a_{i}^{\dagger}(\theta) \) .

## 3.4.1 Defect matrix elements

Let us now use  \( (3.9)-(3.10) \)  in order to evaluate matrix elements involving the defect operator. In what follows, the most relevant matrix elements are those involving four particles, for which we compute

 \[ \begin{align*}&\langle a_{i}(\theta_{1})a_{\bar{\imath}}(\theta_{2})Z_{\alpha}a_{i}^{\dagger}(\theta_{3})a_{i}^{\dagger}(\bar{\theta}_{4})\rangle=w_{i\bar{\imath}}^{\alpha}(\theta_{1},\theta_{2})\delta(\theta_{1\bar{\imath}})\delta(\theta_{2\bar{\imath}})+k_{i\bar{\imath}}^{\alpha}(\theta_{1},\theta_{4})\delta(\hat{\theta}_{12})\delta(\hat{\bar{\theta}}_{34}),\\&\langle a_{i}(\theta_{1})a_{i}(\theta_{2})Z_{\alpha}a_{j}^{\dagger}(\theta_{3})a_{j}^{\dagger}(\bar{\theta}_{4})\rangle=-\pi^{2}\hat{W}_{i}^{\alpha}(\theta_{1})\hat{W}_{i}^{\bar{\alpha}}(\theta_{2})\delta(\theta_{13})\delta(\bar{\theta}_{24})\delta_{ij},\\&\langle a_{i}(\theta_{1})a_{k}(\theta_{2})a_{i}(\theta_{3})Z_{\alpha}a_{i}^{\dagger}(\theta_{4})\rangle=\pi^{2}\hat{W}_{i}^{\alpha}(\theta_{4})\hat{K}_{i}^{\alpha}(-\theta_{2})\left[\delta(\theta_{14})\delta(\hat{\theta}_{23})-\delta(\hat{\theta}_{\bar{1}\bar{2}})\delta(\theta_{34})\right]\delta_{\bar{1}\bar{k}},\\&\langle a_{i}(\theta_{1})Z_{\alpha}a_{i}^{\dagger}(\theta_{2})a_{k}^{\dagger}(\theta_{3})a_{i}^{\dagger}(\theta_{4})\rangle=\pi^{2}\hat{W}_{i}^{\alpha}(\theta_{1})\hat{K}_{i}^{\alpha}(-\theta_{3})^{*}\left[\delta(\hat{\theta}_{23})\delta(\theta_{14})-\delta(\theta_{12})\delta(\hat{\theta}_{34})\right]\delta_{\bar{1}\bar{k}},\end{align*} \] 

with the abbreviations

 \[ w_{i\bar{\imath}}^{\alpha}(\theta_{1},\theta_{2})=\pi^{2}\hat{W}_{i}^{\alpha}(\theta_{1})\hat{W}_{i}^{\bar{\alpha}}(\theta_{2})\quad\mathrm{a n d}\quad k_{i\bar{\imath}}^{\alpha}(\theta_{1},\theta_{2})=\pi^{2}\hat{K}_{i}^{\alpha}(\theta_{1})\hat{K}_{i}^{\bar{\alpha}}(\theta_{2})^{*}. \quad (3.20) \] 

One can now try to find solutions for all n-particle form factors either from (3.18)-(3.19) or by direct computation. For instance for the stated choice of particles involved, we compute

 \[ \begin{align*}F_{\alpha}^{m\times(i\bar{\imath})n\times(\bar{\imath}\bar{\imath})}(\theta_{2m}\cdots\theta_{1},\theta_{1}^{\prime}\cdots\theta_{2n}^{\prime})&=\sum_{k=0}^{\min(n,m)}\frac{(-1)^{m+n-2k}\pi^{n+m}}{(m-k)!(n-k)!k!k!}\int_{-\infty}^{\infty}d\beta_{1}\cdots d\beta_{2n+2m}\\&\times\det\mathcal{A}^{2n}(\beta_{1}\cdots\beta_{2n};\theta_{1}^{\prime}\cdots\theta_{2n}^{\prime})\det\mathcal{A}^{2m}(\beta_{2n+1}\cdots\beta_{2n+2m};\theta_{1}\cdots\theta_{2m})\\&\times\prod_{p=1}^{k}\hat{W}_{i}^{\alpha}(\beta_{2p})\hat{W}_{i}^{\bar{\alpha}}(\beta_{2p-1})\delta(\beta_{2p}-\beta_{2n+2p})\delta(\beta_{{2p-1}}-\beta_{2n+2p-1})\\&\times\prod_{p=1+k}^{n}\hat{K}_{i}^{\alpha}(\beta_{2p})^{*}\delta(\beta_{2p}+\beta_{2p-1})\prod_{p=1+k+n}^{n+m}\hat{K}_{i}^{\alpha}(\beta_{2p})\delta(\beta_{2p}+\beta_{2p-1}),\end{align*} \quad (3.21) \]
 

where  \( \mathcal{A}^{\ell}(\theta_{1}\ldots\theta_{\ell};\theta_{1}^{\prime}\ldots\theta_{\ell}^{\prime}) \)  is a rank  \( \ell \)  matrix whose entries are given by

 \[ \mathcal{A}_{i j}^{\ell}=\cos^{2}[(i-j)\pi/2]\delta(\theta_{i}-\theta_{j}^{\prime}),\qquad1\leq i,j\leq\ell. \quad (3.22) \] 

The matrix elements are computed similarly as in [6] and references therein. Likewise we compute

 \[ \begin{align*}F_{\alpha}^{n\times i+m\times i}(\theta_{n}\cdots\theta_{1},\theta_{1}^{\prime}\cdots\theta_{m}^{\prime})&=\delta_{n,m}\frac{\pi^{n}(-1)^{n-1}}{n!}\int_{-\infty}^{\infty}d\beta_{1}\cdots d\beta_{n}\prod_{k=1}^{n}\hat{W}_{i}^{\alpha}(\theta_{k})\\&\times\det\mathcal{B}^{n}(\theta_{n}\cdots\theta_{1};\beta_{1}\cdots\beta_{n})\det\mathcal{B}^{n}(\beta_{1}\cdots \beta_{n};\theta_{1}^{\prime}\cdots\theta_{n}^{\prime}),\end{align*} \quad (3.23) \] 

where we introduced a new rank  \( \ell \)  matrix  \( \mathcal{B}^{\ell}(\theta_{1}\ldots\theta_{\ell};\theta_{1}^{\prime}\ldots\theta_{\ell}^{\prime}) \)  whose entries are now simply given by

 \[ \mathcal{B}_{i j}^{\ell}=\delta(\theta_{i}-\theta_{j}^{\prime}),\qquad1\leq i,j\leq\ell. \quad (3.24) \] 

One can verify explicitly [1] that these expressions indeed satisfy (3.18) and (3.19).

## 3.4.2 Conductance in the T = m = 0 regime

It is well-known that for a free Fermion theory (also for a single complex free Fermion) the conformal  \( U(1) \) -current-current correlation function is simply

 \[ \langle J(r)J(0)\rangle_{T=m=0}=\frac{1}{r^{2}}. \quad (3.25) \] 

This expression can also be obtained by using the expansion (3.2), together with the massless prescription as outlined above and the expressions for the only non-vanishing form factors of the current operator in the complex free Fermion theory

 \[ F_{2}^{J|\bar{u}}({\theta},\tilde{\theta})=-F_{2}^{J|\bar{u}}({\theta},\tilde{\theta})=-i\pi m e^{\frac{\theta+\tilde{\theta}}{2}}. \quad (3.26) \] 

In particular, the massless limit of the previous expressions gives, according to the massless prescription,

 \[ F_{2}^{J|\bar{u}}({\theta},\tilde{\theta})=-F_{LR}^{J|\bar{u}}({\theta},\tilde{\theta})=-2\pi i\tilde{m}e^{\frac{\theta+\tilde{\theta}}{2}}, \quad (3.27) \] 

 \[ F_{LR}^{J|\bar{u}}(\theta,\tilde{\theta})=F_{LR}^{J|\tilde{u}}(\theta,\tilde\theta)=F_{RL}^{J|\tilde{u}}({\theta},\tilde{\theta})=F_{LL}^{J|\tilde{u}}({\theta},\tilde{\theta})=F_{RL}^{J|\tilde{u}}({\theta},\tilde{\theta})=F_{RL}^{J|\tilde{u}}(\theta,\tilde{\theta})=0. \quad (3.28) \] 

We these expressions we can evaluate (3.2) to (3.25). We may the insert (3.25) into (3.1) and the problem is reduced to find the Fourier transform of the function  \( r^{-2} \) , which is given by  \( P\int_{-\infty}^{\infty}dr e^{i\omega r}r^{-2}=-\pi\omega \)  for  \( \omega>0 \) , with P denoting the principle value. This yields in the absence of a defect  \( G(0)=1/2\pi \) , in complete agreement with the well-known classical expression for the conductance in a wire without any impurities, see for instance [47].

For the more complicated situation of n defects  \( Z_{\alpha_{1}}\cdots Z_{\alpha_{n}} \)  located in space at positions  \( y_{\alpha_{1}}\cdots y_{\alpha_{n}} \) , we compute in the zero temperature and zero mass regime

 \[ \begin{align*}\langle J(r)Z_{\alpha_{1}}\cdots Z_{\alpha_{n}}J(0)\rangle_{T=m=0}=\frac{\hat{m}^{2}}{2}\sum_{i}\left[\int_{-\infty}^{\infty}\frac{d\theta_{1}}{2}e^{-2r\hat{m}\cosh\theta_{1}}\hat{K}_{i}^{\alpha|R}(\theta_{1})\int_{-\infty}^{\infty}\frac{d\theta_{2}}{2}\hat{K}_{i}^{\alpha|R}(\theta_{2})^{*}\right.\\ \left.+\int_{-\infty}^{\infty}\frac{d\theta_{1}}{2}e^{\theta_{1}-r\hat{m}e^{\theta_{1}}}\hat{W}_{i}^{\alpha|R}(\theta_{1})\int_{-\infty}^{\infty}\frac{d\theta_{2}}{2}e^{\theta_{2}-r\hat{m}e^{\theta_{2}}}\hat{W}_{i}^{\alpha|R}(\theta_{2})\right].\end{align*} \quad (3.29) \]
 

The functions  \( \hat{W}_{i}^{\alpha|R}(\theta) \) ,  \( \hat{K}_{i}^{\alpha|R}(\theta) \) , … defined in (3.29) are the massless limits of the corresponding functions  \( \hat{W}_{i}^{\alpha}(\theta) \) ,  \( \hat{K}_{i}^{\alpha}(\Theta) \) , … For all the defects we considered, it turned out that the first contribution to the previous correlation function is actually vanishing, so that (3.29) is considerably simplified. In many of the examples, this is due to the fact that the amplitudes  \( \hat{K}_{i}^{\alpha}(\theta) \)  are vanishing in the first place, as a consequence of the crossing relations (3.17). The vanishing of the reflection part in (3.29) also occurs in some cases as a consequence of the parity of the function  \( \hat{K}_{i}^{\alpha}(\theta) \) . For instance, we find that, for the energy operator defect such function, although initially non-vanishing, satisfies  \( \hat{K}_{i}^{\alpha}(\theta) = -\hat{K}_{i}^{\bar{\alpha}}(-\theta) \) , such that  \( \lim_{m\to0}\int_{-\infty}^{\infty}d\theta\,\hat{K}_{i}^{\alpha}(\theta)^{*}=0 \) .

We can now either use (3.29) to compute the conductance or evaluate the expression (3.8) directly in which the frequency limit is already taken, in both cases we obtain

 \[ G^{\alpha}(0)=\frac{1}{2(2\pi)^{3}}\sum_{i}\int\limits_{-\infty}^{0}d\theta e^{\theta}w_{i i}^{\alpha|R R}[\ln(1-e^{\theta}),\theta]. \quad (3.30) \] 

There are, in addition, further generic results which can be obtained independently of the specific form of the defect. We present them at this stage and will confirm their validity below by some specific examples. Specializing to the case in which all  \( \ell \)  defects are of the same type and equidistantly separated, i.e.  \( y = y_{\alpha_{1}} = \cdots = y_{\alpha_{n}} \) . We can identify two distinct regimes

 \[ w_{i i}^{\alpha|R R}(\theta_{1},\theta_{2})=\pi^{2}\left\{\frac{\hat{W}_{i}^{\alpha|R}(\theta_{1})\hat{W}_{i}^{\bar{\alpha}|R}(\theta_{2})^{*}}{|\hat{W}_{i}^{\alpha|R}|^{2}}\right.\left.\begin{array}{l l l}\text{for finite}y&\\ \text{for}y\rightarrow0\end{array}\right. \quad (3.31) \] 

where we used in addition (3.16). Supported by our explicit examples below, we find that for  \( y \to 0 \)  in (3.31) the amplitudes  \( \hat{W}_{i}^{\alpha|R}(\theta) \)  become independent functions of the rapidity. As we have already argued above

 \[ k_{i i}^{\alpha|R R}(\theta_{1},\theta_{2})=0. \quad (3.32) \] 

It will turn out, that the two regimes specified in (3.31) are also of a very distinct nature in the TBA context as presented in part II.

## 3.4.3 A wire with impurities of energy operator type

Let us exemplify the working of the above formulae with a concrete defect operator. As a simple example we choose the energy operator defect as presented in section 2.3.1. Considering first a wire possessing a single defect of this type, we compute

 \[ \hat{W}_{i}^{\alpha}(\theta)=\frac{4\cos B\cosh^{2}\theta}{\cosh2\theta+\cos2B},\quad\hat{K}_{i}^{\alpha}(\theta)=\frac{2i\sin B\sinh\theta}{\sin B-\cosh\theta},\quad w_{i i}^{\alpha|R R}(\theta_{1},\theta_{2})=(2\pi\cos B)^{2} \quad (3.33) \] 

with B being the effective coupling constant as defined in the caption of figure 1, such that

 \[ \langle J(r)Z_{\alpha}J(0)\rangle_{T=m=0}=\frac{\cos^{2}B}{r^{2}}\implies G^{\alpha}(0)=\frac{\cos^{2}B}{2\pi}. \quad (3.34) \]
 

It will turn out that this is in complete agreement with the corresponding result from the Landauer formula (1.1).

Proceeding in the same way for a wire with two or four impurities we evaluated  \( [1] \)  in the regime  \( y \gg r \) 

 \[ \langle J(r)Z_{\alpha_{1}}Z_{\alpha_{2}}J(0)\rangle_{T=m=0}=\frac{4\left[1+\sin^{4}B\right]}{r^{2}\left[\cos^{2}(2B)-3\right]^{2}}, \quad (3.35) \] 

 \[ G^{\alpha_{1}\alpha_{2}}(0)=\frac{2}{\pi}\frac{1+\sin^{4}B}{\left[3-\cos^{2}(2B)\right]^{2}}, \quad (3.36) \] 

 \[ \langle J(r)Z_{\alpha_{1}}Z_{\alpha_{2}}Z_{\alpha_{3}}Z_{\alpha_{4}}J(0)\rangle_{T=m=0}=\frac{1}{2r^{2}}\left[1+\frac{\cos^{8}B}{\left[\cos^{4}B-2(1+\sin^{2}B)^{2}\right]^{2}}\right], \quad (3.37) \] 

 \[ G^{\alpha_{1}\alpha_{2}\alpha_{3}\alpha_{4}}(0)=\frac{1}{4\pi}\left(1+\frac{\cos^{8}B}{\left[\cos^{4}B-2(1+\sin^{2}B)^{2}\right]^{2}}\right). \quad (3.38) \] 

In the regime  \( y \rightarrow 0 \) , we obtained [1]

 \[ \lim_{y\to0}\langle J(r)Z_{\alpha_{1}}Z_{\alpha_{2}}J(0)\rangle_{T=m=0}=\frac{1}{r^{2}}\frac{\cos^{4}B}{\left(1+\sin^{2}B\right)^{2}}, \quad (3.39) \] 

 \[ \lim_{y\to0}G^{\alpha_{1}\alpha_{2}}(0)=\frac{1}{2\pi}\frac{\cos^{4}B}{\left(1+\sin^{2}B\right)^{2}}, \quad (3.40) \] 

 \[ \lim_{y\to0}\langle J(r)Z_{\alpha_{1}}Z_{\alpha_{2}}Z_{\alpha_{3}}Z_{\alpha_{4}}J(0)\rangle_{T=m=0}=\frac{1}{r^{2}}\left(\frac{\cos^{4}B}{\cos^{4}B-2(1+\sin^{2}B)^{2}}\right)^{2}, \quad (3.41) \] 

 \[ \lim_{y\to0}G^{\alpha_{1}\alpha_{2}\alpha_{3}\alpha_{4}}(0)=\frac{1}{2\pi}\left(\frac{\cos^{4}B}{\cos^{4}B-2(1+\sin^{2}B)^{2}}\right)^{2}. \quad (3.42) \] 

It will turn out that we can reproduce these expressions by evaluating the Landauer formula (1.2) when computing the densities with the help of the TBA. This will now be outlined in part II together with the general conclusions concerning also this part.

## Acknowledgments

We would like to thank the organizers for their kind invitation, financial support and all their efforts to make this  \( 50^{th} \)  anniversary celebration of the Instituto de Física Teórica possible. Furthermore we thank Carla Figueira de Morisson Faria (Max Born Institut Berlin) and Frank Göhmann (Universität Bayreuth) for collaboration. We are grateful to the Deutsche Forschungsgemeinschaft (Sfb288) for financial support.

## References

[1] O.A. Castro-Alvaredo and A. Fring, From Integrability to Conductance, Impurity Systems, hep-th/0205076.

[2] O.A. Castro-Alvaredo, A. Fring and C. Figueira de Morisson Faria, Relativistic treatment of harmonics from impurity systems in quantum wires, cond-mat/0208128.

[3] O.A. Castro-Alvaredo and A. Fring, Unstable particles versus resonances in impurity systems, conductance in quantum wires, cond-mat/0112199.
 

[4] O.A. Castro-Alvaredo, A. Fring and F. Göhmann, On the absence of simultaneous reflection and transmission in integrable impurity systems, hep-th/0201142.

[5] O.A. Castro-Alvaredo and A. Fring, Nucl. Phys. B636 [FS] (2002) 611.

[6] O.A. Castro-Alvaredo and A. Fring, Nucl. Phys. B618 [FS] (2001) 437.

[7] F.P. Milliken, C.P. Umbach and R.A. Webb, Solid State. Comm. 97 (1996) 309.

[8] R. Kubo, Can. J. Phys. 34 (1956) 1274.

[9] R. Kubo, M. Toda and N. Hashitsume, Statistical Physics, 2-nd ed. (Springer, Berlin, 1995).

[10] R. Landauer, IBM J. Res. Dev. 1 (1957) 223; Philos. Mag. 21 (1970) 863; M. Büttinger, Phys. Rev. Lett. 57 (1986) 1761.

[11] F. Lesage, H. Saleur and S. Skorik, Nucl. Phys. B474 (1996) 602.

[12] P. Fendley, A.W.W. Ludwig and H. Saleur, Phys. Rev. B52 (1995) 8934.

[13] P. Fendley, A.W.W. Ludwig and H. Saleur, Phys. Rev. Lett. 74 (1995) 3005.

[14] C. Cohen-Tannoudji, Quantum Mechanic, (John Wiley & Sons, New York, 1977).

[15] P. Weisz, Phys. Lett. B67 (1977) 179; M. Karowski and P. Weisz, Nucl. Phys. B139 (1978) 445.

[16] F.A. Smirnov, Form Factors in Completely Integrable Models of Quantum Field Theory, Advanced Series in Mathematical Physics, Vol. 14, World Scientific, Singapore, 1992.

[17] H. Babujian, O.A. Castro-Alvaredo, A. Fring and M. Karowski, Correlation functions from form factors, an introduction, in preparation.

[18] Al.B. Zamolodchikov, Nucl. Phys. B342 (1990) 695.

[19] C.N. Yang, Phys. Rev. Lett. 19 (1967) 1312; R.J. Baxter, Ann. Phys. 70 (1972) 323.

[20] B. Schroer, T.T. Truong and P. Weisz, Phys. Lett. B63 (1976) 422; M. Karowski, H.J. Thun, T.T. Truong and P. Weisz, Phys. Lett. B67 (1977) 321; A.B. Zamolodchikov, JETP Lett. 25 (1977) 468.

[21] I.V. Cherednik, Theor. Math. Phys. 61 (1984) 977.

[22] E.K. Sklyanin, J. Math. Phys. A21 (1988) 2375.

[23] A. Fring and R. Köberle, Nucl. Phys. B421 (1994) 159; Nucl. Phys. B419 [FS] (1994) 647; Int. J. of Mod. Phys. A10 (1995) 739.

[24] G. Delfino, G. Mussardo and P. Simonetti, Phys. Lett. B328 (1994) 123, Nucl. Phys. B432 (1994) 518.

[25] P. Federbush, Phys. Rev. 121 (1961) 1247; Progress of Theo. Phys. 26 (1961) 148; B. Schroer, T.T. Truong and P. Weisz, Ann. of Phys. 102 (1976) 156; S.N.M. Ruijsenaars, Comm. of Math. Phys. 87 (1982) 181.

[26] R. Konik and A. LeClair, Phys. Rev. B58 (1998) 1872.

[27] D. Cabra and C. Naón, Mod. Phys. Lett. A9 (1994) 2107.

[28] S. Ghoshal and A.B. Zamolodchikov, Int. J. of Mod. Phys. A9 (1994) 3841.

[29] R. Konik and A. LeClair, Nucl. Phys. B538 (1999) 587.
 

[30] A. Luther and I. Peschel, Phys. Rev. B9 (1974) 2911; F.D.M. Haldane, J. of Phys. C (1981) 2585; C.L. Kane and M.P.A. Fisher, Phys. Rev. B46 (1992) 15233.

[31] I. Affleck and A.W.W. Ludwig, J. Phys. A27 (1994) 5375.

[32] H. Weyl, Gruppentheorie und Quantenmechanik, (Hirzel, Leipzig, 1928).

[33] W. Gordon, Zeit. für Physik 40, 117 (1926); D.M. Volkov, Zeit. für Physik 94, 250 (1935).

[34] P.A. Franken, A.E. Hill, C.W. Peters and G. Weinrich, Phys. Rev. Lett. 7 (1961) 118; W. Kaiser and C. Garret, Phys. Rev. Lett. 7 (1961) 229.

[35] T. Brabec and F. Krausz, Rev. of Mod. Phys. 72, 545 (2002).

[36] G. Sommerer, private communication (1999).

[37] M. Lenzner, J. Krüger, S. Sartania, Z. Cheng, Ch. Spielmann, G. Mourou, W. Kautek, and F. Krausz, Phys. Rev. Lett. 80, 4076 (1998).

[38] O. E. Alon, V. Averbukh, and N. Moiseyev, Phys. Rev. Lett. 80, 3743 (1998).

[39] K.Z. Hatsagortsyan and C.H. Keitel, Phys. Rev. Lett. 86, 2277 (2001); J. Phys. B 35, L175 (2002).

[40] O. E. Alon, V. Averbukh, and N. Moiseyev, Phys. Rev. Lett. 85, 5218 (2000); G. Ya. Slepyan, S. A. Maksimenko, V. P. Kalosha, A.V. Gusakov, and J. Herrmann, Phys. Rev. A 63, 053808 (2001).

[41] N. Hay, R. de Nalda, E. Springate, K.J. Mendham and J.P. Marangos, Phys. Rev. A 61, 053810 (2000); N. Hay, R. de Nalda, T. Halfmann, K.J. Mendham, M. B. Mason, M. Castillejo, and J.P. Marangos, Phys. Rev. A 62, 041803 (2000).

[42] V. Averbukh, O. E. Alon, and N. Moiseyev, Phys. Rev. A 64, 033411 (2001).

[43] C. Itzykson and J-B. Zuber, Quantum Field Theory, (McGraw-Hill, Singapore, 1980).

[44] R. E. Wagner, Q. Su and R. Grobe, Phys. Rev. A 60, 3233 (1999).

[45] Al. B. Zamolodchikov, Nucl. Phys. B358 (1991) 524.

[46] M. Sato, T. Miwa and M. Jimbo, Proc. Japan Acad. 53 (1977) 6; 147; 153.

[47] C.L. Kane and M.P.A. Fisher, Phys. Rev. B46 (1992) 15233.
 
