
# Classical Monte Carlo Study for Antiferro Quadrupole Orders in a Diamond Lattice

Kazumasa Hattori \( ^{1,2*} \)  and Hirokazu Tsunetsugu \( ^{1} \) 

 \( ^{1} \) The Institute for Solid State Physics, The University of Tokyo, 5-1-5, Kashiwanoha, Kashiwa, Chiba 277-8581, Japan  
 \( ^{2} \) Department of Physics, Tokyo Metropolitan University, 1-1 Minami-osawa, Hachioji, Tokyo 192-0397, Japan

We investigate antiferro quadrupole orders in a diamond lattice under magnetic fields by Monte Carlo simulations for two types of classical effective models. One is an XY model with  \( Z_{3} \)  anisotropy, and the other is a two-component  \( \phi^{4} \)  model with a third-order anisotropy. We confirm that the universality class of the zero-field transition is that for the three-dimensional XY model. Magnetic field corresponds to a  \( Z_{3} \)  field in the effective model, and under this field, we find that collinear and canted antiferro-quadrupole orders compete. Each phase is characterized by symmetry breaking in the sector of (sublattice  \( Z_{2} \) )⊗(reflection  \( Z_{2}^{2} \)  for the order parameter). When  \( Z_{3} \)  anisotropy and magnetic field vary, it turns out that this system is a good playground for various multicritical points; bicritical and tetracritical points emerge in a finite field. Another important finding is about the scaling of parasitic ferro quadrupole order at the zero-field critical point. This is the secondary order parameter induced by the primary antiferro order, and its critical exponent  \( \beta^{\prime}=0.815 \)  clearly differs from the expected value that is twice the value for the primary order parameter. The corresponding correlation length exponent is also different,  \( \nu^{\prime}=0.597(12) \) . We also discuss relation of the present effective quadrupole models with the 3-state Potts model as well as implication to undertanding of orbital orders in Pr-based 1-2-20 compounds.

KEYWORDS: orbital order, quadrupole, Monte Carlo simulation, Potts model

## 1. Introduction

Orbital physics in strongly correlated electron systems has been intensively studied in recent years. \( ^{1,2} \)  The orbital degrees of freedom in partially-filled d- or f-electron levels show a variety of interesting phases and properties. Anisotropic nature of these electron wavefunctions with nonzero angular momentum is a key to understanding these materials, and this leads to, for example, a strongly anisotropy in the spin space in addition to the orbital sector itself. \( ^{3-5} \) 

Recently, orbital degrees of freedom in Pr-based f-electron systems  \( PrT_{2}X_{20} \)  (T=V, Ti, Rh and X=Al, Zn) have attracted great attention. Quadrupolar Kondo effects \( ^{6)} \)  are expected to take place at Pr ions with non-Kramers-doublet ground state. \( ^{7-11)} \)  Electric resistivity approaches the zero-temperature limit with a negative finite-temperature correction that is singular at T=0. This is naively attributed to a local quadrupole Kondo effect, \( ^{10,11)} \)  and there have been a few theoretical developments about the two-channel Kondo lattice systems. \( ^{12,13)} \)  A microscopic model is also proposed for describing these compounds. \( ^{14)} \) 

Those compounds also have one or a few low-temperature phases at zero magnetic field and also multiple phases under magnetic fields. Most of them are considered to be antiferro quadrupole ordered phases. An exception is  \( PrTi_{2}Al_{20} \) , \( ^{10,11)} \)  and the neutron scattering \( ^{15)} \)  and ultrasound experiments \( ^{16)} \)  suggest a ferro quadrupole order in this compound. Anisotropy in the orbital sector in these systems is manifested in the strong anisotropy of the critical field and the phase diagram strongly dependent on the field direction. \( ^{9,10,17,18)} \)  Superconductivity appears in a couple of compounds near the quadrupole ordered phases, \( ^{7,19)} \)  and it is expected that orbital fluctuations in the non-Kramers doublet in the Pr ions contribute to its realization.

In our previous study, \( ^{20)} \)  antiferro orbital orders in the Pr 1-2-20 compounds were investigated. Using a mean-field and spin-wave theories, we determined the temperature-magnetic field phase diagram, and also calculated excitation spectra. Quantum effects at each Pr ion were taken into account by considering all the crystalline-electric-field (CEF) states within the J = 4 multiplet in the calculations, while the intersite correlations were approximated by static mean fields.

The purpose of the present work is to examine the effects of intersite thermal fluctuations on the antiferro quadrupole orders and the phase transitions, and we employ classical Monte Carlo (MC) method to this end. Since the transition temperatures of the ordered phases are much lower than the energy scales of the CEF excited states, \( ^{21)} \)  it is justified to use an effective classical model constructed in terms of the non-Kramers doublet CEF ground states alone. In addition to antiferro quadrupole orders, ferro quadrupole and octupole orders are other possibilities of symmetry breaking, but we will not examine them in this paper. We should note that antiferro orders exhibit much richer physics than ferro orders es-
 

specially in magnetic field. A challenging subject of octupole orders requires a formulation more complicated than those outlined in this paper, and therefore we leave this a future study.

We will introduce in Sec. 2 a system to be investigated and that is a model of the E-modes of electric quadrupoles in the Pr compounds. We will show that its classical effective model is a plane rotor (or XY) model with a  \( Z_{3} \)  single-site anisotropy, or if amplitude fluctuations are not traced out, a  \( \phi^{4} \)  model for a two-component field with a third-order term. Having the same symmetry, these two effective models are related to the 3-state Potts model (equivalent to the 3-state clock model), and this simpler model has been intensively studied in the community of statistical physics for the case of ferro interactions. \( ^{22)} \)  In contrast, the low-temperature ordered phases are not well understood when interactions are anti-ferro. There are controversies in their properties among the reported studies as we will explain later.

Another purpose of this paper is to achieve better understanding of the ordered phases of the antiferro 3-state Potts model on the basis of our calculations. Several previous works have studied the antiferro 3-state Potts model on three-dimensional bipartite lattices, \( ^{23-32} \)  and their results have agreed that the anisotropy is irrelevant at the phase transition and the transition belongs to the XY universality class in three dimensions. \( ^{23)} \)  However, their results are not consistent to each other about the ordered phases, and the nature of the ordered states has not been well clarified. \( ^{23-32)} \)  In our models, microscopic degrees of freedom of local order parameters are enlarged from three points in the Potts model, and can be located a unit circle (one-dimensional compact manifold) or a two-dimensional continuous vector space (two-dimensional noncompact manifold). This corresponds to coarse graining processes of the Potts model, and we expect that our models exhibit the nature of order parameter configuration more clearly.

This paper is organized as follows. In Sec. 2, a classical quadrupole Hamiltonian in a diamond lattice is introduced. We have analyzed the model by classical Monte Carlo simulations and the numerical results for zero magnetic field will be shown in Sec. 3. Detailed analysis of ordered states will be carried out in Sec. 4 with comparison to the antiferro 3-state Potts model. Effects of magnetic field will be examined in Sec. 5 and the temperature-magnetic field phase diagram will be constructed. The relevance of the present results on the Pr-based 1-2-20 systems are discussed in Sec. 6, and finally Sec. 7 concludes the present paper.

## 2. Models and Numerical Method

In this section, we briefly explain the characteristics of the non-Kramers doublet system in the Pr 1-2-20 compounds and introduce two model Hamiltonians to be studied in this paper.

## 2.1 Non-Kramers doublet for Pr ion

In the Pr 1-2-20 compounds, the Pr ions form a diamond sublattice. Each ion has valency  \( Pr^{3+} \)  and two f-electrons. On the basis of the LS coupling scheme, this electron configuration has the total angular momentum  \( J = 5 - 1 = 4 \) . The local point group symmetry at the Pr site is  \( T_{d} \) , and the CEF potential splits the J = 4 multiplet. It is known that the ground state is a non-Kramers doublet with  \( E(\Gamma_{3}) \)  representation. \( ^{21)} \)  Its basis states are

 \[ \left|\Uparrow\right\rangle=\frac{1}{\sqrt{12}}\Big[\sqrt{7}\frac{\left|4\right\rangle+\left|-4\right\rangle}{\sqrt{2}}-\sqrt{5}\left|0\right\rangle\Big], \quad (1) \] 

 \[ \left|\Downarrow\right\rangle=\frac{-\left|2\right\rangle+\left|-2\right\rangle}{\sqrt{2}}, \quad (2) \] 

where  \( |J_{z}\rangle \)  denotes the eigenstate of the total angular momentum J = 4 and its z-component  \( J_{z} \) . Note that these two states are both invariant upon time-reversal operation, and thus, the ground state is a non-Kramers doublet.

The internal dynamics in the non-Kramers doublet is completely described by three operators usually denoted by the three Pauli matrices  \( (\sigma_{x}, \sigma_{y}, \sigma_{z}) \) . Two of them are quadrupole operators  \( \sigma_{z} = \mathcal{P}_{0}\frac{1}{8}(2J_{z}^{2} - J_{x}^{2} - J_{\gamma}^{2})\mathcal{P}_{0} \)  and  \( \sigma_{x} = \mathcal{P}_{0}\frac{\sqrt{3}}{8}(J_{x}^{2} - J_{y}^{2})\mathcal{P}_{0} \) , where  \( P_{0} \)  is the projector onto the non-Kramers doublet ground state. They operate two basis states in the ground-state doublet as

 \[ \begin{aligned}\sigma_{x}\mid\Uparrow\rangle&=\mid\Downarrow\rangle,\quad\sigma_{x}\mid\Downarrow\rangle=\mid\Uparrow\rangle,\\\sigma_{z}\mid\Uparrow\Uparrow\rangle&=\mid\Uparrow\rangle,\quad\sigma_{z}\mid\Downarrow\rangle=-\mid\Downarrow\rangle.\end{aligned} \quad (3) \] 

The last one  \( \sigma_{y} \)  is an octupole moment  \( \sigma_{v} = \mathcal{P}_{0} \frac{1}{36 \sqrt{3}} [J_{x} J_{y} J_{z} + (\text{all permutations})] \mathcal{P}_{0} \) . As mentioned in the Introduction, we will concentrate on the quadrupole degrees of freedom  \( (\sigma_{z}, \sigma_{x}) \)  alone in this paper.

## 2.2 Classical mapping and single-ion anisotropy

For finite-temperature phase transitions, the most of essential fluctuations arise from thermal ones. In our previous study, \( ^{20)} \)  we have analyzed a microscopic model for the Pr 1-2-20 compounds by means of the mean-field theory and the spin-wave type analysis. The scheme based on the microscopic model takes into account the full information of the CEF states for the Pr ions, while it is insufficient for determining the universality class of the transition, since intersite fluctuations are not taken into account. In order to determine a phase diagram and universality class of the transitions, we will construct effective classical models and analyze them with fully taking account of thermal fluctuations. In the following, we will introduce two effective models and study them throughout this paper.

The classical correspondence of the pair of quadrupole operators  \( (\sigma_{z},\sigma_{x}) \)  at each Pr site is a two-component classical vector  \( \mathbf{Q}=(Q_{u},Q_{v}) \) . With symmetry operations of the  \( T_{d} \)  point group, its two elements transform as bases of the E representation, and they have the same
 

symmetry as  \( Q_{u} \sim 2z^{2} - x^{2} - y^{2} \)  and  \( Q_{v} \sim \sqrt{3}(x^{2} - y^{2}) \) . We also use the polar representation  \( \mathbf{Q} = Q(\cos\theta, \sin\theta) \) .

For considering effective interactions between quadrupole moments, it is important to count all the possible low-order invariants made of them. Local invariants are straightforwardly obtained, and some of them describe local anisotropy. Apart from the trivial quadratic term  \( \propto |Q|^{2} \) , it should be noted that the single ion terms contain a third-order anisotropy [see eq. (5)]. This  \( Z_{3} \)  anisotropy corresponds to the three choices of the uniaxial direction of the quadrupole moment, namely x, y, or z directions. It should be noted that this type of anisotropy does not exist, if the local order parameter is a magnetic dipole, since it is not invariant upon time reversal operation. Therefore, this anisotropy is specific to the quadrupole order parameters. Indeed, as discussed in Ref. 20, the magnitude of this anisotropy is about  \( \sim1 \)  K in Pr-based 1-2-20 compounds, and this is comparable to the transition temperature for the quadrupole orders. \( ^{7-11} \) 

Another point we should mention is the coupling to magnetic fields. Since the quadrupoles are nonmagnetic degrees of freedom, they do not couple to magnetic fields in the linear order. However, there exists a quadratic “Zeeman” coupling as will be introduced in Sec. 5, which is important for understanding the phase diagram of the Pr 1-2-20 compounds under magnetic fields.

## 2.3 Model Hamiltonian

In this paper, we are going to study a system of interacting quadrupoles  \( \{Q_{i}\} \)  on the diamond lattice. Here,  \( \mathbf{Q}_{i}=Q_{i}(\cos\theta_{i},\sin\theta_{i}) \)  represents two components of the quadrupole moment of Pr ion at the site i. In the following, we will call  \( Q_{i} \)  simply a pseudo spin, or otherwise explicitly a quadrupole moment. For this system, we first consider the Hamiltonian defined as

 \[ H=H_{\mathrm{l o c}}+H_{\mathrm{i n t}}, \quad (4) \] 

 \[ H_{\mathrm{l o c}}=\sum_{i}\left(\frac{a}{2}Q_{i}^{2}+\frac{b}{4}Q_{i}^{4}-\frac{c}{3}Q_{i}^{3}\cos3\theta_{i}\right), \quad (5) \] 

 \[ H_{\mathrm{i n t}}=J\sum_{\langle i,j\rangle}Q_{i}Q_{j}\cos(\theta_{i}-\theta_{j})=J\sum_{\langle i,j\rangle}\mathbf{Q}_{i}\cdot\mathbf{Q}_{j}. \quad (6) \] 

Note that magnitudes of quadrupole moments are variables in this model, and they fluctuate. In the interaction part  \( H_{int} \) , the coupling is an antiferro type and the sum is taken over all the nearest-neighbor bonds. It is a special feature of this system that only this isotropic coupling is allowed. This is because each Pr-Pr bond points along [111] or one of its equivalent directions and this restricts a possible form of intersite quadrupole coupling. \( ^{20)} \)  Describing the symmetries of the system properly, this Hamiltonian is sufficient for studying quadrupole orderings, while higher-order terms in Q's are safely neglected. As for the coupling constants, we set a = -5, b = 10 and the unit of energy is J = 1, throughout this paper. In Secs. 3 and 4, we will also study a further simplified model. Fluctuations of the amplitudes are traced out there and we set  \( Q_{i} = 1 \)  at all the sites, and each quadrupole moment has the angle degrees of freedom  \( \theta_{i} \)  alone. Thus, the simplified Hamiltonian is a plane rotor model with three-fold anisotropy:

 \[ H=-\frac{c}{3}\sum_{i}\cos3\theta_{i}+J\sum_{\langle i,j\rangle}\cos(\theta_{i}-\theta_{j}). \quad (7) \] 

The models (4) and (7) contain only the quadrupole degrees freedom of the localized f-electrons and we will not discuss their coupling to conduction electrons, which is important in the Kondo physics observed in the experiments. \( ^{10)} \)  As for the quadrupole ordering, however, these models capture its essential aspects in the Pr-based 1-2-20 compounds.

In the following sections, we will present our numerical results in the classical Monte Carlo (MC) simulations for the models (4) and (7). The typical system size defined by the number of sites is  \( N = L^{3} \)  ( \( 8 \leq L \leq 128 \) ), and the periodic boundary condition is used for all the three directions. To be specific, L = 2 corresponds to the cubic unit cell, which contains 8 sites. For updates in the MC simulation, we combined the Metropolis algorithm of single-site flips and the Wolff's algorithm. \( ^{33)} \)  We also use several global updates; the global  \( C_{3} \)  rotation ( \( \theta_{i} \rightarrow \theta_{i} + 2\pi/3 \) ) of Q when the applied magnetic field is zero or weak, or otherwise the global update of  \( Q_{v} \rightarrow -Q_{v} \)  [see eq. (14) for coupling to the magnetic field]. In the simulations, each MC run sampled  \( \sim 50,000 \)  snapshots after thermalization typically 50,000 MC steps, and the data were averaged over typically 64 MC runs starting from different initial configurations.

## 3. Phase Transition at Zero Magnetic Field

Let us start studying a phase transition in our quadrupole systems from the case of zero magnetic field. Our previous mean-field analysis \( ^{20)} \)  showed that the system undergoes a phase transition with decreasing temperature into an ordered phase. There, the  \( Z_{3} \)  symmetry in the quadrupole pseudospin space is spontaneously broken. The transition is continuous unless the anisotropy is too large. The mean-field theory also shows that the primary order parameter is the staggered  \( Q_{v} \)  component and that this is accompanied by the secondary order parameter, the uniform  \( Q_{u} \)  component. These order parameters are about one of the degenerate ordered phases. The ordered phase has degeneracy  \( 6 = 3 \times 2 \) , where 3 comes from  \( Z_{3} \)  symmetry and 2 comes from the symmetry between A- and B-sublattices. In the four other ordered phases, the primary and secondary order parameters are rotated by  \( \pm 2\pi/3 \)  in the Q space.

We will study the effects of thermal fluctuations on the phase transition by using classical Monte-Carlo simulations and confirm the symmetry breaking predicted by the mean-field theory. We will next investigate critical
 

behaviors of the phase transition. Several previous works have studied this problem of the antiferro 3-state Potts model on three-dimensional bipartite lattices. Their conclusion is that the anisotropy is irrelevant and the transition belongs to the XY universality class in three dimensions, \( ^{23)} \)  i.e., that of superfluid transition in liquid  \( {}^{4}He \) . Large-scale numerical simulations have been performed to study this universality class, and the values of critical exponents are determined in high precision: \( ^{34)} \)   \( \eta=0.0381(2) \) ,  \( \nu=0.6717(1) \) ,  \( a=-0.0151(3) \) ,  \( \gamma=1.3178(2) \) ,  \( b=0.3486(1) \) , and  \( \delta=4.780(1) \) . We will also check if our MC results are consistent with these exponents.

## 3.1 Monte Carlo calculations

In MC simulations, we calculated thermodynamic quantities including specific heat, order parameters, and correlation functions. For order parameters, the average  \( Q_{s} \)  is first defined for each sublattice s and then the staggered and the uniform components are defined as

 \[ \mathbf{Q}_{\mp}=\frac{\mathbf{Q}_{A}\mp\mathbf{Q}_{B}}{2},\mathbf{Q}_{s}=\frac{2}{N}\sum_{j\in s}\mathbf{Q}_{j},\ (s=A,B). \quad (8) \] 

With this normalization, their variance of fluctuation  \( \sqrt{\langle\mathbf{Q}_{\mp}^{2}\rangle} \)  plays the role of order parameters. In the limit of  \( N\to\infty \) , the order parameter is expected to vanish in the high-temperature para phase and stays finite in the low-temperature ordered phase.

As for the correlation functions, we will analyze their Fourier transform. The primitive unit cell consists of two sites, A and B, and each quadrupole moment has two components  \( (Q_{u}, Q_{v}) \) . Therefore, the Fourier transform of the correlation function is a  \( 4 \times 4 \)  matrix

 \[ C_{s\mu,s^{\prime}\mu^{\prime}}(\mathbf{k})=\frac{1}{N/2}\sum_{j\in s}\sum_{j^{\prime}\in s^{\prime}}\langle Q_{\mu,j}Q_{\mu^{\prime},j^{\prime}}\rangle e^{-i\mathbf{k}\cdot(\mathbf{r}_{j}-\mathbf{r}_{j^{\prime}})}, \quad (9) \] 

where s,  \( s' \)  are the sublattice index and  \( \mu \) ,  \( \mu' \)  are the pseudospin component u or v. This is a hermitian matrix and all of its four eigenvalues  \( \{\lambda_{n}(\mathbf{k})\} \)  are real. The wave vector  \( k^{*} \)  where the largest eigenvalue  \( \lambda_{1}(\mathbf{k}) \)  is maximum and its eigenvector describe the most dominant spatial correlation of quadrupoles. The correlation length  \( \xi \)  is a very important quantity for investigating critical properties, and we define it by the peak width of the largest eigenvalue  \( \lambda_{1}(\mathbf{k}) \)  as

 \[ \frac{\lambda_{1}(\mathbf{k}_{1})}{\lambda_{1}(\mathbf{\kappa}^{*})}=1-4\xi^{2}\sin^{2}\frac{\delta k}{2},\quad\mathbf{k}_{1}=\mathbf{k}^{*}+(\delta k,0,0), \quad (10) \] 

where  \( k_{1} \)  is the wave vector closest to the peak position  \( k^{*} \)  in the finite size system considered.

## 3.2 Thermodynamics

Figure 1(a) shows the temperature dependence of specific heat  \( C(T) \)  in the rotor model (7) with the anisotropy c = 3.0. Each curve of the data for the system size  \( 8 \leq L \leq 128 \)  has a peak around the temperature

(a)

![](./images/867754556975481338_1.jpg)

(b)

![](./images/867754556975481338_2.jpg)

Fig. 1. (Color online) Temperature dependence of specific heat. (a) Near  \( T=T_{c} \)  for c=3.0 and  \( 8 \leq L \leq 128 \) . (b) c dependence for L = 16. Inset in (b): the system size dependence of low-temperature peak for c=3.0.

T = 1.27. As the system size increases, the peak sharpens. This indicates the presence of a phase transition, but the peak value does not grow unlike many other transitions. This behavior is consistent with the expectation about the specific heat critical exponent  \( \alpha < 0 \) . Another possibility is that the transition is first order, but we have excluded this possibility by calculating internal energy  \( E(T) \) . It does not show a jump at the transition temperature, and thus, we conclude that the transition is continuous. We will examine the critical exponent later.

We also quickly examine the effects of anisotropy c. Figure 1(b) shows the specific heat  \( C(T) \)  for several values of the anisotropy from c = 0.0 to 3.0 calculated for the system size L = 16. The limit c = 0.0 is the isotropic XY model with antiferro nearest-neighbor couplings on the diamond lattice, and its  \( C(T) \)  should agree with the one of the ferro XY model, because of its bipartite lattice structure and no field applied. Critical behavior in the specific heat does not seem to depend sensitively on the value of the anisotropy up to c = 3.0.

The specific heat  \( C(T) \)  also has a broad peak at low temperature  \( T \sim 0.3 \) , and it grows as c increases. A few previous theories predicted the presence of multiple
 
![](./images/867754556975481338_3.jpg)

![](./images/867754556975481338_4.jpg)

Fig. 2. (Color online) k dependence of the largest eigenvalue  \( \lambda_{1}(\mathbf{k}) \)  in  \( (k_{x}, k_{y}, 0) \)  plane for c=3.0 and L=16. (a) T=2.5 and (b) T=0.5. The peak value in (b) is  \( \lambda_{1}(\mathbf{0}) \sim 1464 = 0.357N \) .

phase transitions in a model related to ours, \( ^{23-32} \)  but our result is not consistent with their prediction. The system size dependence of this peak is shown in the inset of Fig. 1(b) for c = 3.0. Our data do not show a noticeable system size dependence expected at a phase transition, and thus this small peak is not a phase transition. As for the origin of the peak, we have found a signature showing that the system gains a local anisotropy energy there. The temperature dependence of the average  \( \langle\cos3\theta_{i}\rangle \)  slightly steepens around the temperature at the specific heat peak. We will discuss the comparison to the related model in more detail in Sec. 6.

## 3.3 Order parameters and critical temperature

Next, let us investigate spatial correlations. The largest eigenvalue  \( \lambda_{1}(\mathbf{k}) \)  of  \( C_{s\mu,s^{\prime}\mu^{\prime}}(\mathbf{k}) \)  is plotted in Fig. 2 for the  \( k_{z}=0 \)  plane of the Brillouin zone. The peak value grows quickly with lowering T, and in the ordered phase it is very large and proportional to the system size. For example,  \( \lambda_{1}(\mathbf{0})\sim1464=0.357N \)  at T=0.5. This is an evidence that quadrupole moments order at this transition.

At all the temperatures in the calculation, the maximum of  \( \lambda_{1}(\mathbf{k}) \)  in the entire Brillouin zone is always located at  \( k^{*} = 0 \) . Of course, this does not mean that the order pattern is ferro-type; the unit cell of the diamond lattice contains A- and B-sublattices, and the antiferro order does not break the translation symmetry. To identify the order pattern, one needs to analyze the eigenvector of  \( C_{s\mu,s'\mu'} \) . Within statistical errors of MC simulation, the largest eigenvalue at  \( k^{*} = 0 \)  is doubly degenerate, and its eigenvectors are  \( (x_{Au}, x_{Av}, x_{Bu}, x_{Bv}) \approx (1, 0, -1, 0) \)  and  \( (0, 1, 0, -1) \) . Since the relative sign between the A- and B-sublattice elements is negative, the correlation is antiferro between the different sublattices. The direction of ordered quadrupole needs a more careful analysis, and we will study this problem in Sec. 4.

To determine critical exponents, one has to first locate the transition temperature  \( T_{c} \)  accurately. This can be done by calculating the Binder ratio of the primary order

![](./images/867754556975481338_5.jpg)

![](./images/867754556975481338_6.jpg)

Fig. 3. (Color online) (a) Binder ratio B for c=3.0 and  \( 8 \leq L \leq 40 \) . Lines are a guide for eyes. Inset shows the crossing point between the sets of two lines for  \( (L, L') = (8, 16) \) ,  \( (16, 32) \) ,  \( (\overline{32}, 64) \) , and  \( (64, 128) \) . The two filled circles connected with a line indicate 1/L and 1/L', respectively. The data for  \( L \geq 64 \)  are not shown in the main panel for clarity. (b) Correlation length  \( \xi \)  for c=3.0 and  \( 8 \leq L \leq 40 \) .

parameter

 \[ \mathcal{B}\equiv1-\frac{1}{3}\frac{\left\langle\left(\mathbf{Q}^{2}\right)^{2}\right\rangle}{\left\langle\mathbf{Q}^{2}\right\rangle^{2}}. \quad (11) \] 

Figure 3(a) shows its temperature dependence for various system sizes. The Binder ratio at  \( T = T_{c} \)  is a scale invariant quantity, and therefore, asymptotically independent of the system size at  \( T_{c} \) . Thus, the crossing point of curves for different L's determines the transition temperature  \( T_{c} \) . The value of the Binder ratio at the crossing  \( B_{c} \)  is a universal quantity, and the known value is  \( B_{c}=0.5856 \)  for the XY universality class in the spatial dimension  \( d = 3^{.34} \) . In our results, the crossing points for large L's approach the temperature  \( T_{c} \approx 1.2695(3) \) , and extrapolated value of  \( B_{c} \)  for  \( L \to \infty \)  is consistent with the known value as shown in the inset of Fig. 3(b).

Another scale invariant quantity is the ratio of two length scales,  \( \xi/L \) , and this also determines  \( T_{c} \) . Figure 3(b) shows its temperature dependence for the same system sizes as for the Binder ratio. It is known that
 
![](./images/867754556975481338_7.jpg)

![](./images/867754556975481338_8.jpg)

![](./images/867754556975481338_9.jpg)

Fig. 4. (Color online) (a) Temperature dependence of  \( \langle Q_{-}^{2}\rangle \)  near  \( T=T_{c} \)  for c=3.0 and  \( 8 \leq L \leq 40 \) . (b) c dependence of  \( \langle Q_{-}^{2}\rangle \)  for L=16. (c) Temperature dependence of  \( \langle Q_{+}^{2}\rangle \)  near  \( T=T_{c} \)  for c=3.0 and  \( 8 \leq L \leq 40 \) .

 \( (\xi/L)\big|_{T_{c}}=0.5924^{34}) \)  and now this value agrees very well with our data. The crossing position leads to  \( T_{c}\approx1.270 \) , which is slightly higher than the estimate based on the Binder ratio but agrees with it within statistical error in MC simulation.

Now, let us see the evolution of order parameters. We should note that the ordered phase has two types of order parameters and that this is a very characteristic point to the antiferro model with the  \( Z_{3} \)  anisotropy. The primary one is an antiferro component, and this is natural in the antiferro model. An interesting one is the secondary order parameter and this is a ferro component. It arises from the fact that the order parameter cannot form the complete antiferro. Due to the single-ion anisotropy, the

![](./images/867754556975481338_10.jpg)

![](./images/867754556975481338_11.jpg)

Fig. 5. (Color online) Scaling plot for the two order parameters calculated for  \( 16 \leq L \leq 128 \)  and c=3.0. For this analysis, we fix  \( T_{c}=1.2695 \) . (a)  \( \langle Q_{-}^{2}\rangle \)  and (b)  \( \langle Q_{+}^{2}\rangle \) . Inset:  \( \delta t\equiv1-T/T_{c} \)  dependence of uniform moment  \( \langle Q_{+}^{2}\rangle^{1/2} \) . The three lines  \( \propto\delta t^{2\beta} \) ,  \( \delta t^{\beta'} \) , and  \( \delta t \)  with  \( \beta \)  being the order-parameter exponent for the 3d-XY universality class:  \( \beta=0.3486 \)  and  \( \beta'=\nu'(d+\eta'-2)/2=0.815 \)  with d=3 are also shown for guide to eyes.

antiferro pattern slightly tilts.

Figure 4(a) shows the temperature dependence of the square of the primary order parameter,  \( \langle Q_{-}^{2}\rangle \) . With increasing system size, this vanishes above  \( T_{c} \) , but approaches a finite value below  \( T_{c}\cdot \) . This also confirms that the long range order below  \( T_{c} \)  is about the antiferro alignment of quadrupoles. The effects of the  \( Z_{3} \)  anisotropy are shown in Fig. 4(b). For larger value of the anisotropy parameter c, the order parameter is slightly reduced and the transition temperature also decreases a little, but the overall feature does not change. The square of the secondary order parameter  \( \langle Q_{+}^{2}\rangle \)  is shown in Fig. 4(c) in the log plot. The absolute value is tiny but it clearly develops below  \( T_{c} \) .

## 3.4 Scaling of primary order parameter

Now, we examine the critical behavior of primary order parameter in details. A conventional analysis is a finite-size scaling, and Fig. 5 shows the analysis for the temperature dependence of order parameter. The horizontal axis measures the distance from the critical temperature, while the vertical axis is the squared primary order parameter, and these two are normalized by the system size powered with the constants related to the two critical exponents  \( \nu \)  and  \( \eta \) .  \( \nu \) , describes divergent behavior of
 

the correlation length around the transition temperature,  \( \xi \sim |T - T_{c}|^{-\nu} \) , and the anomalous dimension  \( \eta \)  corresponds to the power-law exponent of the correlation function just at the transition temperature  \( C(\mathbf{k}) \sim 1/|\mathbf{k}|^{2-\eta} \) . We have fitted the numerical data by using different sets of  \( \nu \)  and  \( \eta \)  for the two components.

For this analysis about the primary order parameter, we have used the values known for the three-dimensional  \( (3d) \) -XY universality class,  \( \nu = 0.672 \)  and  \( \eta = 0.038 \) . The data for different system sizes nicely fall on a universal curve except for the low-temperature region of the smaller system sizes as shown in Fig. 5(a). Thus, this confirms that the transition belongs to the 3d-XY universality class as long as the primary order parameter is concerned.

## 3.5 Scaling of secondary order parameter

We have found that the criticality of the ferro secondary order parameter is distinctive and very interesting, but previous studies by other groups on related models have not addressed this point. The presence of the parasitic ferro order was first found in our mean-field analysis, \( ^{20} \)  and we are going to analyze their true criticality based on our MC data. Let us first explain a natural idea about the expected criticality and then show later that our MC results differ from that.

Naively speaking, the ferro moment is induced by the antiferro quadrupole order in the following way. In the effective free energy, the secondary order parameter couples to the primary order parameter in the lowest order as

 \[ \Delta F_{+-}=g_{+-}[Q_{u,+}(Q_{u,-}^{2}-Q_{v,-}^{2})-2Q_{v,+}Q_{u,-}Q_{v,-}], \quad (12) \] 

with a proper coupling constant  \( g_{+-} \) . In the ordered state, the primary order parameter  \( Q_{v,-} \)  acquires a finite expectation value and therefore the coupling term leads to an effective static field corresponding to the  \( Q_{u,+} \)  component,  \( h_{u,+} \sim g_{+} - \langle Q_{v,-} \rangle^{2} \) . Thus, it is expected that a finite ferro moment is induced in the ordered phase and within the linear response region, its size is given by  \( \langle Q_{u,+} \rangle \propto \chi_{+}^{uu_{+}} h_{u,+} \propto \langle Q_{v,-} \rangle^{2} \propto (1 - T/T_{c})^{2\beta} \) . Here,  \( \chi_{+}^{uu_{+}} \)  is the quadrupole susceptibility of the corresponding ferro component. This means that the order parameter critical exponent of the ferro component is twice the value of the primary order parameter  \( \beta' = 2\beta = 0.6972 \) . An important point is that the above scaling presumes non-singularity of  \( \chi_{+}^{uu_{+}} \)  at the critical point. We verified in our previous paper that it is nonsingular within the mean-field approximation. \( ^{20} \) 

The scaling of the calculated ferro component in our results is shown in the inset of Fig. 5(b), and one can see that it does not work well with the expected exponent  \( 2\beta \) . We also calculated the ratio  \( [\langle\mathbf{Q}_{+}^{2}\rangle]^{1/2}/\langle\mathbf{Q}_{-}^{2}\rangle \) , and found that it is not independent of T as expected but varies strongly with temperature, which also disproves the expectation  \( \beta^{\prime}=2\beta \) .
In order to determine the value of  \( \beta' \) , we tried a finite size scaling for the ferro component and determined the correlation length exponent  \( \nu' \)  and also  \( \eta' \) . One needs a caution about the meaning of  \( \eta' and it is not clear if  \) \eta' \(  is really the anomalous dimension of the ferro component, since we do not know if the scaling relation holds for  \) \mathbf{Q}_{+} \( . The scaled order parameter should be understood as  \) \langle\mathbf{Q}_{+}^{2}\rangle L^{2\beta'/\nu'} \( , and we simply denote the exponent of L-dependence  \) 2\beta'/\nu' \(  by  \) 1+\eta' $ . We have no prediction on a universality class for the ferro secondary order parameter. Therefore, no candidate values are available for these exponents, and we need an unbiased estimate for their precise values. A useful tool for finite size scaling was recently developed by Harada \( ^{35} \)  based on a Bayesian inference analysis. We used his method for the ferro components and obtained  \( \nu'=0.597(12) \)  and  \( \eta'=1.727(12) \) . As shown in Fig. 5(b), the finite size scaling works well and the data for different system sizes lie on a universal curve. The result leads to  \( \beta'=(1+1.727)\times\nu'/2\simeq0.815>2\beta \) , and the inset of Fig. 5(b) shows that this value describes nicely the temperature dependence in the double-logarithm plot except very close to the critical point, where finite size corrections are not negligible.

It is very interesting that the ferro secondary order parameter does not follow the naive scaling with  \( \beta^{\prime}=2\beta \)  but shows another type of criticality with the independent exponents  \( \nu^{\prime}<\nu \)  and  \( \beta^{\prime}>2\beta \) . Understanding this criticality and the validity of the naive scaling form for the secondary order parameter is important for the complete analysis of the ordered phase, but at the moment we are not equipped for reproducing these values by analytical calculations like the renormalization group theory. From this viewpoint, it is also an important open question how to calculate criticality behaviors of non-primary order parameters, and we leave this for a future work.

## 4. Low-temperature Ordered Phase

In this section, we investigate in detail the ordered phase in the low-temperature region. As explained before, the antiferro 3-state Potts model is a much simpler model that has the same symmetry with our models; each microscopic pseudospin can point to only three directions, which corresponds to the limit of  \( c \to \infty \)  in the model (7). Although there have been a pile of studies about this problem for the Potts case on bipartite lattices, \( ^{[23-31]} \)  several important points are not settled down about this model. Most importantly, the nature of the ordered states has not been well clarified for the Potts case. \( ^{[23-32]} \)  The consensus is that the lowest-temperature phase is the broken sublattice-symmetry (BSS) state. \( ^{[23]} \)  This is the phase in which the symmetry between the two sublattices is broken and this may also be called a ferri state. Existence of intermediate-temperature phase was also pointed out and an exotic configuration was proposed. This is called the permutationally symmetric sublattices (PSS) state. \( ^{[25]} \)  There are claims that the
 
![](./images/867754556975481338_12.jpg)

Fig. 6. (Color online) (a) Distribution of  \( \mathbf{Q}_{s}(s=A,B) \)  as a function of  \( \theta \)  for L=16. (b) The nearest-neighbor correlations of  \( Q_{A} \)  and  \( Q_{B} \)  for L=16. Temperature is T=0.5 and c=0.5 in both data.

high-temperature phase undergoes a transition into another intermediate-temperature phase named rotationally symmetric (RS) phase. Inside this phase the sublattice moments uniformly fluctuate. \( ^{26,28} \) 

We will examine the following two points in our rotor model (7). The first one is about the nature of the low-temperature ordered phase. The second one is whether an intermediate temperature phase exists.

To investigate the pseudospin configuration in the ordered phase, we first calculate the distribution of macroscopic sublattice moments,  \( Q_{A} \)  and  \( Q_{B} \)  [see eq. (8)], in our MC simulations. Figure 6(a) shows the distribution below  \( T_{c} \)  of their directions,  \( Q_{s} \propto (\cos \theta_{s}, \sin \theta_{s}) \) . While the distribution is almost independent of direction  \( \theta_{s} \)  above  \( T_{c} \) , each sublattice moment in the ordered phase mainly points around 6 directions as shown in Fig. 6(a). The distribution is identical for the two sublattices. These 6 directions are not equally separated on the circle in the Q-space, but located on both sides of the three favored directions of the  \( Z_{3} \)  anisotropy. This is consistent with our previous conclusion based on the mean-field analysis \( ^{20)} \)  that the ordered phase has a 6-fold degeneracy. Due to global updates in our simulation, the order parameter migrates from one of the 6 stable points to another, and the 6 points become equally populated after long Monte-Carlo runs in our simulation.
Figure 6(a) shows that  \( Q_{A} \)  and  \( Q_{B} \)  have the same distribution, but this does not mean that they point to the same direction. We have examined the correlation between  \( Q_{A} \)  and  \( Q_{B} \)  by calculating the two-body distribution of the directions of microscopic pseudospins on nearest-neighbor site pairs,  \( (\theta_{A}(\mathbf{r}), \theta_{B}(\mathbf{r}^{\prime})) \) . The distribution is calculated by evaluating nearest-neighbor configuration for all the sites during MC steps at T = 0.5, and its value is shown with color plot in Fig. 6(b). This plot provides valuable information on the moment configuration in the ordered phase. There are 6 peaks, and the most important point is that the 6 values of  \( \theta_{s} \)  are different to each other for either of s = A and B. This manifests that for each direction of ordered quadrupole in the A-sublattice, the favorite direction on the B-sublattice neighbor sites is uniquely determined, and vice versa. Therefore, the spatial quadrupole configuration is uniquely determined in the ordered state except for a domain structure due to the 6-fold degeneracy related to the global  \( Z_{3} \)  symmetry.

This conclusion differs from the case of the 3-state Potts model. It is believed that its lowest-temperature region is the phase of the broken sublattice-symmetry (BSS) state. \( ^{23)} \)  In this state, Potts spins on the A-sublattice point to one of the three directions, while B-sublattice Potts spins point to the two other directions randomly from site to site and this yields  \( \frac{1}{2}\log2 \)  residual entropy at T=0. Alternatively, the A- and B-sublattices switch their roles. Therefore, the symmetry between the two sublattices is broken. This may also be called a ferri state, since  \( \langle\mathbf{Q}_{s}\rangle=-2\langle\mathbf{Q}_{s^{\prime}}\rangle\neq\mathbf{0} \) .

It has been also proposed that an intermediate phase exists between the disordered phase and the low-temperature ordered phase, and that it is an exotic one named the permutationally symmetric sublattices (PSS) state. \( ^{25)} \)  In this phase, the most-favorite quadrupole (Potts spin) direction in the A-sublattice is the least-favorite direction in the B-sublattice, and vice versa. We find that the low-temperature phase in our model is equivalent to the PSS state, and show this below by calculating sublattice moments.

Let  \(  p_{n}(s)  \)  be the probability that s-sublattice Potts "spins" point to the direction  \( \theta_{n} \equiv 2n\pi/3 \)  ( \( n \in \{0, 1, 2\} \) ). In one of the PSS states,  \(  p_{2}(A) = p_{1}(B) = \frac{1}{3}(1 - w - w')  \) ,  \(  p_{0}(A) = p_{0}(B) = \frac{1}{3}(1 - w)  \) , and  \(  p_{1}(A) = p_{2}(B) = \frac{1}{3}(1 + 2w + w')  \) , with  \( w, w' > 0 \) . For this case, the sublattice moment averages are

 \[ \langle\mathbf{Q}_{A}\rangle=w(\cos\theta_{1},\sin\theta_{1})+\frac{1}{\sqrt{3}}w^{\prime}(0,1), \] 

 \[ \langle\mathbf{Q}_{B}\rangle=w(\cos\theta_{2},\sin\theta_{2})-\frac{1}{\sqrt{3}}w^{\prime}(0,1). \quad (13) \] 

Their directions are slightly shifted from the directions of Potts spins,  \( \theta_{A} = \theta_{1} - \delta\theta \)  and  \( \theta_{B} = \theta_{2} + \delta\theta \) , where  \( \tan\delta\theta = w' / [\sqrt{3}(2w + w')] \) . This is exactly what is realized in our simulations.
 

It has been also claimed that the high-temperature phase undergoes a transition into another intermediate-temperature phase when the model is on a simple cubic lattice. \( ^{[26,28]} \)  This is called the rotationally symmetric (RS) phase, and within this phase the moments in each sublattice fluctuate their directions uniformly in the entire range of angle  \( 0 \leq \theta_{s} < 2\pi \) . \( ^{[26,28]} \)  If this phase is realized, the two-angle distribution in Fig. 6(b) should have shown two straight bright bands that are parallel to each other and separated by the relative angle difference  \( \pi \) . We note that this is the behavior expected for the completely isotropic XY antiferromagnet, and also in the low-temperature part of the disordered phase in our models. Almost the same behavior is observed above  \( T_{c} \)  in our simulation, although the bands are not completely straight but slightly wind due to the  \( Z_{3} \)  anisotropy.

Thus, the two-angle distribution in Fig. 6(b) in our calculation negates the BSS state and also the RS state. The results agree only with the distribution in the PSS state. Rahman, et al. \( ^{31} \)  demonstrated that the PSS state claimed in Ref. 25 for the AF 3-state Potts model on a simple cubic lattice is an artifact of their incorrect way when taking the sublattice degeneracy into account. For a diamond lattice model, Ref. 30 suggests the PSS state occurs, which is consistent with our results in this paper. We note that in our simulations there is only one transition, and thus, there is no intermediate phase in our model.

## 5. Temperature-Magnetic Field Phase Diagram

So far, we have discussed the critical properties of the model (7) with no external field. Since quadrupole moments are equivalent to a second-order product of magnetic dipoles, a magnetic field H leads to a quadratic Zeeman coupling of  \( Q_{i} \) . Various quadrupolar systems such as Pr-based 1-2-20 \( ^{7-9,17,18} \)  and  \( PrPb_{3} \) , \( ^{36} \)  have several ordered phases in magnetic fields, and this depends on the field direction. Thus, it is worth examining the effects of magnetic fields when the quadratic Zeeman coupling is taken into account. \( ^{20)} \)  We denote this coupling as

 \[ H_{\mathrm{m a g}}=-h\sum_{i}Q_{i}\cos\theta_{i}, \quad (14) \] 

where  \( h \propto 2H_{z}^{2} - H_{x}^{2} - H_{\bar{y}}^{2} \)  is the conjugate field of  \( Q_{u} \)  component, and the sign of h depends on the direction of H and the microscopic parameters in the system such as the CEF level structures. \( ^{20)} \)  Magnetic field influences not only the direction but also the amplitude of quadrupole moments. \( ^{20)} \)  Their amplitude may vary from site to site, as was shown in our previous study, \( ^{20)} \)  and an experiment also found this in the related material  \( PrPb_{3} \) . \( ^{36)} \)  In order to take account of this effect, we will use throughout this section the model (4)-(6), in which  \( |Q_{i}| \) 's fluctuate.

As for the relation between the conjugate field h and the real magnetic field H, for example, h > 0 corresponds to  \( H \parallel [001] \)  and h < 0 to  \( H \parallel [110] \) . For other magnetic-field directions such as [010] or [100],  \( H_{mag} \)  contains an additional term  \( -h' \sum Q_i \sin \theta_i \) , where  \( h' \propto \sqrt{3}(H_x^2 - H_y^2) \) . For H  \( \parallel [111] \) , h and  \( h' \)  are both zero and the coupling to quadrupole moments vanishes. In this case, the leading-order effect of magnetic field is a coupling to octupole moments, but this is beyond the scope of the present study and we will not discuss it in this paper.

## 5.1 Symmetry of the quadrupole model in magnetic field

Before showing the results of phase diagram, let us briefly explain the symmetries of the Hamiltonian including the quadratic Zeeman coupling  \( H_{mag} \) . This will be important for discussing phase transitions in magnetic fields.

In the case of no magnetic field,  \( h = h' = 0 \) , the Hamiltonian has three types of symmetries. The first is the time-reversal symmetry, and the second is the  \( Z_{2} \)  symmetry of the two-sublattice exchange. The last one is related to the  \( Z_{3} \)  anisotropy, and its precise symmetry is the symmetric group  \( S_{3} \)  related to permutations of the three special Q directions. Recall that these directions correspond to the x, y, and z-axes of the cubic lattice structure in the real space. Since our models are about continuous “ \( \phi^{4} \)  spins”, more precisely speaking, the symmetry operations in the Q space are the three rotations with angle  \( \theta = 0, \pm 2\pi/3 \)  and the three mirrors like  \( R_{v}: Q_{v} \rightarrow -Q_{v} \) . By using the point group nomenclature, this symmetry group is  \( D_{3} \)  or  \( C_{3v} \) , which are isomorphic to  \( S_{3} \) .

When a finite uniform magnetic field H is applied, the  \( Z_{2} \)  sublattice symmetry persists. The time reversal symmetry also persists in our models of quadrupole moments, since the quadrupole operators and their conjugate field are both invariant. The internal  \( D_{3} \)  symmetry is generally broken, because the three principle axes in the lattice structure are no longer equivalent due to the applied field. However, the exception is the case of  \( H \parallel [001] \) , [110], or their equivalent directions. In this case, two of the three axes in the lattice remain equivalent, and correspondingly the  \( D_{3} \)  symmetry is not completely broken but reduced to the dihedral symmetry.

The internal symmetry is directly related to the point group symmetry of the lattice structure. The above symmetry operations in the internal Q space are equivalent to some lattice rotations. The  \( \pm2\pi/3 \)  rotation in the Q space is also a three-fold rotation about one of the trigonal axes of the lattice, e.g., [111] direction. The mirrors in the Q space are  \( \pm\pi/2 \)  rotation about one of the x, y, and z axes of the lattice. For example,  \( R_{v} \)  is equivalent to  \( \pm\pi/2 \)  rotation about the z axis.

Thus, the symmetries of the Hamiltonian under the field h are described by the group of symmetry operations,  \( G = \{1, P_{AB}, R_{v}, P_{AB}R_{v}\} \) , where  \( P_{AB} \)  denotes the exchange of the two sublattices, and note that  \( P_{AB}^{2} = R_{v}^{2} = 1 \)  and  \( P_{AB}R_{v} = R_{v}P_{AB} \) . Since this is an Abelian group, all of the four irreducible representations are one-
 
![](./images/867754556975481338_13.jpg)

Fig. 7. (Color online) (a) T-h phase diagram for the anisotropy c = 0.5. The conjugate field is proportional to the square of magnetic field,  \( h \propto H_{z}^{2} \) . Quadrupole configuration in each phase is schematically depicted with arrows with the 3-fold axes for the phases I and III. Phase I has four stable domains; the one with the depicted configuration and the other domains obtained with transformation  \( R_{v} \)  and/or  \( P_{AB} \) . [See (e)]. Just on the h = 0 line only one ordered phase I exists, and this has two additional stable domains that are transformed from the depicted one by  \( \pm2\pi/3 \)  rotation in the Q space. [See (f) and (i)]. (b)-(k) Distribution of local quadrupole moments  \( P(Q_{u}, Q_{v}) \)  for typical values of T and h calculated in the system of L = 16. The part of  \( -2 \leq Q_{u}, Q_{v} \leq 2 \)  is shown in all the panels. In the ordered phases I-III, different peaks correspond to different domains. The higher temperature result (i) in the phase I has broadened peaks that nearly merge pairwise due to large thermal fluctuations.

dimensional, and this means that the order parameters of spontaneous symmetry breaking are scalars and the universality class of the corresponding phase transitions is the 3d-Ising universality class, except at multi-critical points.

## 5.2 T-h phase diagram for h > 0

Let us first discuss the h > 0 part of the T-h phase diagram. This part corresponds the case of magnetic field  \( H \parallel [001] \) , and  \( h \propto H_{z}^{2} \) . The Hamiltonian has two types of symmetries, and ordered phases are related to their breaking. One symmetry operation is the exchange of the two sublattices  \( P_{AB} \) , and the other is the mirror that reverses the v-component  \( R_{v}: Q_{v} \to -Q_{v} \) . In terms of the point group, the latter is the diagonal mirror operation,  \( (x, y, z) \to (y, x, z) \) . Since both of  \( P_{AB}^{2} \)  and  \( R_{v}^{2} \)  are the identity operator, the Hamiltonian has corresponding parity symmetries, namely  \( Z_{2} \otimes Z_{2} \)  symmetry, when the quadratic Zeeman coupling (14) is present. As will be shown later, it is more convenient to consider instead of  \( P_{AB} \)  its product with the mirror operation,  \( R_{AB} \equiv P_{AB}R_{v} \) , and this also has a parity character,  \( R_{AB}^{2} = 1 \) . Ordered phases in the magnetic field along the [001] direction are related to how this  \( Z_{2} \otimes Z_{2} \)  symmetry is broken.

We determined the phase diagram by the MC calculations performed with global updates modified for the  \( R_{v} \)  symmetry, \( ^{33)} \)  and the result is shown in Fig. 7(a) for the anisotropy c = 0.5. The phase boundaries are determined by calculating Binder ratio for each order parameter with typically  \( L \leq 64 \)  (see also Fig. 10 and discussions there). Three ordered phases appear and their symmetry is summarized in Table I. All the three ordered phases were found in our previous mean-field study, \( ^{20)} \)  but the phase boundaries have a different geometry and different shapes.

The part at low-T and low-h is the phase I and this is essentially the same as the ordered phase at h=0. The difference from the h=0 case is about the degeneracy of stable domains. While the h=0 ordered phase has six types of domains, two of the six become unstable for h>0, and the stable four are related with each other under  \( R_{v} \) ,  \( R_{AB} \) , and  \( R_{AB}R_{v} \)  operations.

In a higher field part, there appears the phase III and the quadrupole moments exhibit a canted configuration;  \( Q_{v,-} \neq 0 \)  and  \( Q_{u,+} > 0 \) . The high-T side of the phase I touches another ordered phase, the phase II, and the quadrupole moments show a collinear (ferri) configuration there;  \( Q_{u,\pm} \neq 0 \)  and  \( Q_{v,\pm} = 0 \) . The polarized phase IV is the part at very large h, and the pseudospins are all aligned in the direction of the conjugate field,  \( Q_{u,+} > 0 \) . This phase smoothly continues to the disordered phase at h = 0 for high temperatures  \( T > T_{c} = 0.8914(1) \) . All the transitions are the second order for c = 0.5.

The phase I is stabilized by the inter-site interaction J, and this explains why it appears at low fields. The phase III has a configuration of symmetrically canted moments, and this gains an energy from both of the J and the h terms. The phase II has a collinear configuration of quadrupoles. It is not straightforward to understand its stability, but it is likely that it is stabilized by thermal fluctuations. The collinear configuration has a larger number of low-energy excited states compared with other orderings such as non-collinear configurations, and the corresponding large entropy lowers the free energy when the temperature is not so low. It should be
 

noted that the phase II is very sensitive to the third-order anisotropy term c. At c=0, this phase vanishes, and its region grows with increasing  \( |c| \) . Its detailed c dependence will be discussed at the end of this subsection.

Quadrupole order— Now, we investigate a microscopic structure of the order parameter in these phases by analyzing the distribution of local quadrupole moments. Figures 7(b)-(k) show the distribution of the A-sublattice quadrupole moments

 \[ P(\mathbf{Q})=\frac{2}{N}\sum_{i\in A}\langle\delta(\mathbf{Q}-\mathbf{Q}_{i})\rangle, \quad (15) \] 

where  \( \langle\cdots\rangle \)  denotes the MC average, and this is normalized such as  \( \int dQ P(Q) = 1 \) . In our simulations, the configuration migrates all the equivalent domains (if present) with the help of implemented global updates. \( ^{33} \)  This means that the distribution is invariant for all the symmetry operations of the model, and one symmetry is about sublattice exchange. Therefore, the distribution in the B-sublattice is identical to the above one within statistical errors.

The distribution  \( P(\mathbf{Q}) \)  is plotted in Figs. 7(b)-(k) for several typical points in the T-h parameter space, and it clearly exhibits the characteristics of each phase. The point (e) is in the phase I, while (c), (d) and (g) in the phase III. (h) is in the phase II, and the ferri nature is visible there. (b) and (j) are in the polarized phase IV, and the distribution has only one peak there. Note that on the h=0 line, the  \( Z_{3} \)  symmetry in the Q-space is recovered as it should be. At low temperatures, the distribution shows well-separated peaks and they correspond to different stable domains in the ordered phases. The sequence of (b)→(e) clearly demonstrates how the canted antiferro quadrupole order develops with decreasing h from the polarized phase IV. With the information of  \( P(\mathbf{Q}) \)  alone it is not conclusive that the order parameters have those configurations depicted in Fig. 7(a). Thus, we have additionally calculated the nearest-neighbor correlation, as was done in Sec. 4 and confirmed these configurations. The point of h=0 and T=0.65 is inside the phase I and this phase has six domains. However, the distribution at this point is very broadened as shown in Fig. 7(i), and each pair of nearest peaks is indistinguishable due to large thermal fluctuations. Lowering temperature suppresses these thermal fluctuations and each pair evolves into well-separated spots as shown in (f). The origin of large thermal fluctuations is related to the peculiar shape of the boundary between the phases I and II, and we will briefly discuss this below.

Phase boundaries— Now, we discuss the phase boundaries. The present MC results differ from our previous mean-field analysis \( ^{20)} \)  in several important points. In the mean-field analysis, the phase II lays between the phases I and III and the phase I does not touch the phase III. This is one important difference from the result in Fig. 7(a). Another but related difference is the boundary between the phases I and II. It did not show a reentrant behavior, and the phase II extended down to the T=0 limit in Ref. 20.

Before discussing the difference from the mean-field result, let us examine the order of transitions based on symmetry arguments. In the mean-field phase diagram, the transition from the phase II to the lower-field phase I is second order, while the transition to the higher-field phase III is first order. The symmetry of the ordered phases can explain the different orders of the transitions in our previous phase diagram and also the newly found I-III phase boundary. First of all, the phase I has no symmetry and both of  \( R_{v} \)  and  \( R_{AB} \)  symmetries are broken. In the phase III the  \( R_{AB} \)  symmetry remains unbroken. Therefore, the transition to the phase I is related to breaking the  \( R_{AB} \)  symmetry, and this is expected second order. The same is true for the I-II transition. It is related to breaking the remaining  \( R_{v} \)  symmetry, and thus, expected second order. The phases II and III have different types of order parameters, and therefore, their phase transition should be first order. Orders of the transitions have been successfully explained for the mean-field and MC phase diagrams.

Let us now analyze the difference in the topology of the ordered phases between the mean-field and MC studies. First, in the MC phase diagram, it should be noted that the lower-field side of the I-II phase boundary continues to the zero field critical point  \( (T,h)=(T_{c}(h=0),0) \)  without crossing or touching the h=0 line before that, but the part of  \( 0.4\lesssim T<T_{c}(h=0) \)  is so close to the h=0 line. Calculation to show this needs extremely high precision, and it is not easy to directly check this point. Therefore, we try an alternative proof. Using the MC data obtained in Sec. 3, we can show that the transition at  \( T_{c}(h=0) \)  upon varying temperature is surely of the 3d-XY type. This ensures that both  \( Q_{u} \)  and  \( Q_{v} \)  fluctuations diverge at this critical point, which in turn ensures the phase boundary between I and II continues up to  \( T_{c}(h=0) \) . To confirm this universality class, we carried out the finite-size scaling analysis of the fluctuation of the primary order parameter  \( \langle Q_{u-}^{2}\rangle \) , and show the result in Fig. 8 analyzed with the known exponents of the 3d-XY universality class. The data for different system sizes nicely collapse onto a universal curve and this confirms the transition is of the 3d-XY type as expected.

Applying the magnetic field reduces the symmetry of the system and the  \( Z_{3} \)  symmetry (more precisely,  \( D_{3} \)  asymmetry) is lost for  \( h \neq 0 \) . As explained before, the expected universality class of the transition between the para and ordered phases (II and III) is the 3d-Ising class. We have checked this point by analyzing the transition at fixed h = 0.9, where the transition temperature  \( T_{c}(h = 0.9) = 0.88598(5) \) . Figure 9 shows the scaling plot of the primary order parameter  \( Q_{u,-} \) . To identify the transition, two universality classes are examined. One is
 

Table I. Symmetry and order parameters in the phases I-IV and I'. Each symmetry operation is marked "inv." if the phase is invariant with its operation, or "×" otherwise. Note that  \( R_{AB}R_{v} \)  equals the simple sublattice exchange  \( P_{AB} \) . I-III are the ordered phases in the magnetic field  \( H \parallel [001] \) , while I' is the ordered phase in  \( H \parallel [110] \) .

<table><tr><td></td><td>\( R_{v} \)</td><td>\( R_{AB} \)</td><td>\( RA_{B}R_{v} \)</td><td>\( \langle Q_{u,+}\rangle \)</td><td>\( \overline{\langle Q_{u,-}\rangle} \)</td><td>\( \langle Q_{v,+}\rangle \)</td><td>\( \overline{\langle Q_{v,-}\rangle} \)</td></tr><tr><td>Phase I</td><td>✗</td><td>✗</td><td>\( \times \)</td><td>\( \geq 0 \)</td><td>\( \neq 0 \)</td><td>\) \neq 0 \(</td><td>\) \neq0 \(</td></tr><tr><td>Phase II</td><td>inv.</td><td>✗</td><td>✗</td><td>&gt;0</td><td>\( \neq 0 \)</td><td>0</td><td>0</td></tr><tr><td>Phase III</td><td>✗</td><td>inv.</td><td>✗</td><td>&gt;0</td><td>0</td><td>0</td><td>\( \neq 0 \)</td></tr><tr><td>Phase IV</td><td>inv.</td><td>inv.</td><td>\( \text{inv.} \)</td><td>\( \neq 0 \)</td><td>0</td><td>0</td><td>\( \neq0 \)</td></tr><tr><td>Phase I&#x27;</td><td>✗</td><td>inv.</td><td>✗</td><td>&lt;0</td><td>0</td><td>0</td><td>\( \neq0 \)</td></tr></table>

the 3d-Ising class shown in the panel (a) and the other is the 3d-XY class in (b). Since the two sets of the exponents  \( \nu \)  and  \( \eta \)  are very similar, the difference is small but one can see that the scaling with the 3d-Ising exponents \( ^{37)} \)  works better for a wider range of the reduced temperature.

Let us also examine other parts in the phase diagram; the I-III phase boundary and the high-field side of the I-II boundary. An important difference from our previous study \( ^{20)} \)  is that the bicritical point of the phases II, III, and IV in the mean-field phase diagram is now replaced by a tetracritical point where all the phases I-IV meet. Our MC calculations indicate that the phases II and III touch only at one point and the phase I intervenes between them. To confirm this, we have demonstrated the presence of two different transitions when h varies at a fixed temperature near the tetracritical point. This is done by calculating h-dependence of characteristic quantities of the two transitions at T = 0.8 fixed. Figure 10 shows the two Binder ratios  \( \mathcal{B}_{\mu}=\langle Q_{\mu,-}^{2}\rangle^{2}/\langle Q_{\mu,-}^{\mathrm{4}}\rangle \)  ( \( \mu = u, v \) ) for L=16, 32, and 64 as a function of h.  \( B_{u} \)  becomes L independent at the I-III phase boundary, while  \( B_{v} \)  does at the I-II phase boundary. Although the convergence with L is not sufficient, the tendency clearly shows that the two transitions occur at different h values.

Finally, let us discuss the dependence of the phase diagrams on anisotropy strength c. Figure 11 shows the  \( T-h \)  phase diagrams for c=0.1 and 3.0. Compared to the case of c=0.5 in Fig. 7(a), the phase II significantly shrinks at the smaller c [Fig. 11 (a)], while grows at the larger c [Fig. 1l (b)]. Thus, the anisotropy c stabilizes the phase II. We should also mention that the phase III disappears for larger  \( |c| \)  (c = 3.0) and the phase I now directly touches the phase IV at high field. Within our MC simulations, the IV-I phase boundary is a line of first-order transition. We can explain this result based on a symmetry argument. The transition from the disordered phase IV to the ordered phase I in the conjugate field h requires that the two symmetries  \( R_{v} \)  and  \( R_{AB} \)  need to be broken at the same time. The system has no further symmetry to enforce this, and therefore if these two phases share a boundary of a finite length, the transition should be first order. At the end point of the first-order transition line, the three phases II-IV meet and therefore this is a

![](./images/867754556975481338_14.jpg)

Fig. 8. (Color online) Scaling plot of  \( \langle Q_{u,-}^{2}\rangle \)  for h = 0, c = 0.5 and  \( 32 \leq L \leq 128 \) .

bicritical point. Needless to say, it does not refute the presence of the tetracritical point discussed before for smaller c, since the phases IV and I share only one point there. Other boundaries are lines of second order transitions as in the case c = 0.5. We also note that the reentrant behavior in the low-field part of the phase diagram is greatly enhanced at the larger anisotropy c = 3.0. The reentrant behavior will be discussed in details in Sec. 6.

## 5.3 T-h phase diagram for h < 0

Let us now discuss the case h < 0, i.e., H  \( \parallel \)  [110]. For h < 0, the anisotropy due to the c term does not compete with the conjugate field h unlike the case of h > 0. Thus, the unfavorable two domains in the phase I for h > 0 become stabilized for h < 0. Figure 12 shows the h < 0 part of T-h phase diagram for c = 0.1, 0.5, and 3.0. The order-parameter configuration for one of the domains is schematically shown in Fig. 12. Since the canted configuration shown has energy gain from both of the anisotropy and the field, the two domains with  \( \langle Q_{u,+}\rangle < 0 \)  are favored. As for the anisotropy of the critical field, the zero-temperature critical field is  \( |h_{c}(0)| \sim 9 \)  for c = 0.5, and this is about 50% larger than the value for h > 0 [see Fig. 7(a)]. This is because the domains realized for h < 0 are stabler against the applied field compared to the case of h > 0. The anisotropy c signif
 
![](./images/867754556975481338_15.jpg)

Fig. 9. (Color online) Scaling plot of  \( \langle Q_{u,-}^{2}\rangle \)  for h=0.9, c=0.5,  \( T_{c}=0.88598(5) \) , and  \( 16 < L < 64 \) . Comparison between (a) 3d-Ising ( \( \nu=0.62999 \)  and  \( \eta=0.03631 \) ) \( ^{37)} \)  and (b) 3d-XY ( \( \nu=0.672 \)  and  \( \eta=0.038 \) ).

![](./images/867754556975481338_16.jpg)

Fig. 10. (Color online) Binder Ratio  \( \mathcal{B}_{u}=\langle Q_{u,-}^{2}\rangle^{2}/\langle Q_{u,-}^{\mathrm{4}}\rangle \)  (dotted lines) and  \( \mathcal{B}_{v}=\langle Q_{v,-}^{2}\rangle^{2}/\langle Q_{v,-}^{\mathrm{4}}\rangle \)  (full lines) for T=0.8 and  \( L=16(\bigcirc) \) ,  \( L=32(\triangle) \) , and  \( L=64(\bigtriangledown) \) .

icantly enhances the reentrant behaviors as a function of h in the phase diagram. The highest transition temperature is around  \( T_{c} \sim 1.25 \)  at  \( -h \sim 5 \)  for c = 3.0, and this is about 40% higher than the zero-field critical temperature  \( T_{c}(h = 0) \) .

## 6. Discussion

We have investigated phase transitions in the rotor and  \( \phi^{4} \)  models with the  \( Z_{3} \)  anisotropy and determined the T-h phase diagram by MC simulations. In this section, we are going to discuss several points in more detail. We first carry out the Landau analysis for the phase boundaries in the T-h phase diagram. Then, we will compare the present results to previous studies on the 3-state Potts model. \( ^{23-31} \)  Finally, we will comment about recent ex-

![](./images/867754556975481338_17.jpg)

Fig. 11. (Color online) T-h phase diagram for (a) c=0.1 and (b) c=3.0 under magnetic field  \( H \parallel [001] \) . In (b), the part of thick line shows the first-order transition between the phases I and IV. The dotted line is the extrapolation to T=0.

![](./images/867754556975481338_18.jpg)

Fig. 12. (Color online) T-h phase diagram for c=0.1, 0.5, and 3.0 under magnetic field H || [110]. The dotted lines are the extrapolation to T=0. Quadrupole configuration is schematically shown by arrows along with the 3-fold axes.

perimental results in the Pr-based 1-2-20 compounds.

## 6.1 Phase boundaries

In Sec. 5, we have presented that the phase boundaries in the h > 0 part have a different geometry from the result of the mean-field analysis. In the following, we will show that a simple phenomenological theory can describe most of the characteristic features in the T-h phase diagram for both of the h > 0 and h < 0 cases.

To describe the multiple ordered phases on the same footing, let us consider the instability of the para/polarized phase IV on the basis of the following Landau-type free energy,

 \[ F=\sum_{s=A,B}V(\mathbf{Q}_{s})+\tilde{J}\mathbf{Q}_{A}\cdot\mathbf{Q}_{B}, \quad (16) \] 

where  \( V(\mathbf{Q}_{s}) \)  is the effective potential of the quadrupole moments on the sublattice s and  \( \tilde{J} > 0 \)  denotes the effective antiferro coupling between the two sublattice
 

quadrupole moments. The effective potential is the generalization of the one considered in our previous work \( ^{20)} \)  by including the quadratic Zeeman coupling to applied magnetic field

 \[ V(\mathbf{Q})=\textstyle{\frac{1}{2}}a\mathbf{Q}^{2}-\textstyle{\frac{ 冮 }{ 冮 }}c Q_{u}(Q_{u}^{2}-3Q_{v}^{2})+\textstyle{\frac{ 冮 }{ 冮 }}\tilde{b}|\mathbf{Q}|^{4}-h Q_{u}. \quad (17) \] 

Here,  \( \tilde{b} > 0 \)  and  \( \tilde{c} > 0 \) , are effective couplings and we assume that they are essentially constant in the part considered in the phase diagram.

An essential difference from the previous study is that a finite moment is induced in the para/polarized phase IV,  \( \langle\mathbf{Q}_{s}\rangle\equiv\bar{\mathbf{Q}}\equiv(\bar{Q},0) \) , due to the conjugate field h, and symmetry breaking is related to the instability of fluctuations around this value,  \( \deltaQ_{A,B}\equivQ_{A,B}-\bar{Q} \) . The corresponding free energy is

 \[ \begin{align*}\Delta F\sim\sum_{s=A,B}\frac{1}{2}(a_{u}\delta Q_{u,s}^{2}+a_{v}\delta Q_{v,s}^{2})+\tilde{J}\delta\mathbf{Q}_{A}\cdot\delta\mathbf{Q}_{B}+\cdots,\end{align*} \quad (18) \] 

where  \( \cdots \)  is the higher order terms. The two components have different coefficients, when a finite moment is induced

 \[ a_{u}=a-2\bar{c}\bar{Q}+3\tilde{b}\bar{Q}^{2},\ a_{v}=a+2\bar{c}\bar{Q}+\tilde{b}\bar{Q}^{2}. \quad (19) \] 

Concerning the staggered mode  \( \deltaQ_{-}=\deltaQ_{A}-\deltaQ_{B} \) , its u component becomes unstable when  \( a_{u}\leq\tilde{J} \) , while v component becomes unstable when  \( a_{v}\leq\tilde{J} \) . The former case corresponds to the ordered phase II, and the latter case corresponds to the ordered base III. When both components are unstable, this is the phase I. Thus, the geometry of the phase boundaries is nothing but how the two lines,  \( a_{u}=\tilde{J} \)  and  \( a_{v}=\tilde{J} \) , position themselves.

The result (19) is very informative. It should be noted that the induced moment  \( \bar{Q} \)  has the same sign as the conjugate field h and its amplitude  \( |\bar{Q}| \)  increases with  \( |h| \) . The common term a is the inverse of local quadrupole susceptibility at h = 0, and its value decreases with lowering temperature. These mean that the two boundaries,  \( a_{u} = \tilde{J} \)  and  \( a_{v} = \tilde{J } \) , cross at the h = 0 critical temperature, and their low-temperature sides are ordered phases.

What happens about the two boundaries depends on the sign of  \( \bar{Q} \) , i.e., the sign of h, which is related to the magnetic field direction. In the case of h < 0, one should notice that  \( a_{v} < a_{u} \)  always holds. Therefore, the transition of the phase IV is always into the phase III. This is consistent with our result in Fig. 7. It is not a problem that a sequential transition to the phase I does not occur. This is because the above result of  \( a_{u} \)  is obtained with assuming  \( \bar{Q}_{v} = 0 \)  and this no longer holds inside the phase III.

The more exotic geometry of the phase boundaries for h > 0 can be also explained by using a similar argument. As h > 0 increases, the leading instability changes.  \( a_{u} < a_{v} \)  for  \( 0 \leq \bar{Q} \leq \bar{Q}_{1} \)  and  \( a_{v} \leq a_{u} \)  for  \( \bar{Q} \geq \bar{Q}_{1} \) , and the leading instability is the mode with the smaller a. Here,  \( \bar{Q}_{1} = 2\bar{c}/\tilde{b} \) . This means that the two boundaries,  \( a_{u} = \tilde{J} \)  and  \( a_{v} = \tilde{J}, \)  cross to each other twice (at  \( \bar{Q} = 0 \)  and  \( \bar{Q}_{1} \) ) and the higher-field crossing is a tetracritical point. With lowering temperature, the phase IV changes to the phase III at small h, while to the phase II at large h. This explains the exotic geometry of the phase boundaries in the h > 0 phase diagram in Fig. 7. It is also explained that the tetracritical point moves toward larger h side for larger anisotropy c. These transitions are a  \( Z_{2} \)  symmetry breaking except at the tetracritical point. Therefore, they should belong to the 3d-Ising universality class.

Another interesting character in the phase diagrams is the reentrant behavior in the low-field part irrespective of the sign of h, and we can also explain this. The leading instability in the phase IV is determined by the smaller one of the two coefficients (19). Note that  \( \min\{a_{u}, a_{v}\} < a \)  due to the linear term in  \( \bar{Q} \)  as far as  \( \bar{Q}_{1} \)  is not so large. Therefore, the local quadrupole susceptibility is enhanced by h, as far as  \( |h| \)  is weak, and this means that the ordered phase expands with  \( |h| \) . This explains the reentrant phase boundary in the low-field parts. This argument also predicts that the reentrant behavior is more prominent for h < 0. This is because  \( a_{v} \)  determines the phase boundary then and its reduction due to  \( \bar{Q} \) -linear term persists up to a larger  \( |h| \)  since the second-order increase  \( \bar{Q}^{2} \)  has a smaller coefficient. Thus, this also agrees with our MC result.

## 6.2 Comparison to the antiferro 3-state Potts model

As we have discussed in Secs. 3 and 4, the present antiferro rotor model with  \( Z_{3} \)  anisotropy shows a single phase transition at a finite temperature when h = 0, and it belongs to the 3d-XY universality class. The result is qualitatively the same also for the  \( \phi^{4} \)  model with the third-order anisotropy discussed in Sec. 5. This indicates that the  \( Z_{3} \)  anisotropy is irrelevant for the critical phenomena in these kinds of models.

It has been recognized that the anisotropy is not completely irrelevant. In the renormalization-group processes, the effects of the anisotropy become strongly suppressed near the critical fixed point but start to grow as the system approaches the low-temperature fixed point. \( ^{[38,39]} \)  There, the macroscopic degeneracy inherent in the antiferro 3-state Potts model is lifted, and the  \( Z_{3} \)  symmetry is broken together with the  \( Z_{2} \)  sublattice symmetry. Remember that the “3” in  \( Z_{3} \)  corresponds to the three minima in the potential energy due to the 3-fold anisotropy. This seems to happen unless the anisotropy c is exactly zero. The symmetry broken state in our models is naturally connected to the PSS state proposed for the 3-state Potts model. \( ^{[25,30]} \)  We expect that an effective coarse-grained theory for the Potts model on the diamond lattice is equivalent to the present one.

Another interesting direction is to examine the same effective quadrupole models on different structures such as a simple cubic or body-centered cubic lattice, and this is related to a question if the ordered phase at h = 0 has a universal character independent of details of bipar-
 

tite lattice structures. Rahman et al. \( ^{31} \)  claimed that the PSS state is not stable on a simple cubic lattice and the RS state is realized instead. For example, PrPb \( _{3} \)  is known as a quadrupole system with a simple cubic structure \( ^{36} \)  and it is interesting to study if there are qualitative differences between that case and the present one. However, we should note that it is not appropriate to use our quadrupole models on a simple cubic lattice for discussing experimental results in PrPb \( _{3} \) . As emphasized in our previous work, intersite interactions are isotropic in the  \( Q_{u}-Q_{v} \)  space only if the all bonds are along [111] or its equivalent directions under  \( T_{d} \)  symmetry. This is not the case in a simple-cubic lattice, and therefore the intersite interactions are anisotropic and this anisotropy depends on the bond direction, which is similar to dipole-dipole interactions in this sense. One should use this type of quadrupole model with “dipole-type” interactions to discuss quadrupole orders in PrPb \( _{3} \) . Indeed, these anisotropic interactions are known to be very important in a context of the orbital orders in LaMnO \( _{3} \) . \( ^{40,41} \) 

## 6.3 Comparison to the Pr-based 1-2-20 systems

Recently, various Pr 1-2-20 compounds have been found to have interesting low-temperature states. \( ^{42} \)  Here, we discuss their phase diagram under magnetic field based on our results in this paper.

First, let us discuss experiments on  \( PrT_{2}Zn_{20} \) ,  \( (T=\mathrm{Ir}, \mathrm{Rh}) \) . Although no experiment has directly identified its order parameter, it is believed an antiferro quadrupole order, since the results of the ultrasonic experiments \( ^{17,18} \)  show properties similar to those with the antiferro quadrupole order in other systems. \( ^{36} \)  Several experiments have reported the existence of multiple phases in magnetic field. \( ^{7,17,18,43} \)  Our results predict their order parameters. As for the field direction dependence of the phase diagram, our results qualitatively agree with the experimental ones, and also explain that critical temperatures are higher for  \( H \parallel [110] \)  than for  \( H \ parallel [001] \) . This holds universally as far as the sign of the  \( Z_{3} \)  anisotropy is c > 0. This indicates that the anisotropy c is crucial for determining the field-direction dependence of the critical fields.

Another compound  \( PrV_{2}Al_{20}^{44-46} \)  shows a double transition at  \( H = 0.45 \) . Our results do not reproduce such a double transition at zero field, and this suggests that this system has other important interactions. In the present models, the zero-field ordered state is extremely sensitive to the anisotropy and conjugate field h, and thus, tiny extrinsic strain or disorders mask the true h = 0 properties, which might realize as a double transition. For clarifying these issues, we need further efforts and detailed analysis about such effects.

## 7. Conclusion

In this work, we have analyzed two antiferro quadrupole models by using classical Monte Carlo simulations. The first model describes the order parameter with a two-dimensional degrees of freedom. It is reduced to the second model of an antiferro rotor type with a 3-fold anisotropy, and both of them are related to the antiferro 3-state Potts model on the diamond lattice. We have clarified the universality class of the phase transition at zero field in these models is that of three-dimensional XY class, which is consistent with previous studies for related models. One important point of our results is that the low-temperature ordered state is similar to the permutationally symmetric sublattice (PSS) state proposed for the antiferro 3-state Potts model. Another important result is that the scaling of the secondary order parameter is exotic and has a new set of critical exponents  \( \nu' = 0.597(12) \) ,  \( \eta' = 1.727(12) \) , and  \( \beta' = \nu'(1 + \eta')/2 \simeq 0.815 \) . The secondary order parameter was first discovered in our previous study. \( ^{20} \)  It is the ferro component of quadrupole and induced by the antiferro primary order parameter through the local  \( Z_{3} \)  anisotropy.

We have also investigated the effects of magnetic field. By taking into account the quadratic Zeeman coupling of quadrupoles to magnetic fields, we have determined the temperature-field phase diagram for two typical directions of magnetic field. A schematic picture of the result is plotted in Fig. 13 for an intermediate strength of the anisotropy, and we should note that the phase diagram is particularly rich for  \( H \parallel [001] \) . With varying the anisotropy, we have further explored the phase diagram and found various multicritical points, which emerge as special points where multiple phases meet: bicritical and tetracritical points. Another important detail is reentrant behavior of the phase boundary near zero field, and this is prominent for larger anisotropy. We have succeeded in qualitative understanding of these phase structures and reentrant behaviors based on a simple phenomenology. Our results predict experimental realizations of multiple ordered states under magnetic field and their multicriticality in interacting quadrupole systems.

## Acknowledgment

The authors thank Tsuyoshi Okubo and Hiroshi Watanabe for fruitful discussions. This work is supported by a Grant-in-Aid for Scientific Research [Grant No. 23740258 and No. 16H01079 (J-Physics)] from the Japan Society for the Promotion of Science.

1) Y. Tokura and N. Nagaosa, Science, 288, 462 (2000).

2) Y. Kuramoto, H. Kusunose, and A. Kiss, J. Phys. Soc. Jpn. 78, 072001 (2009).

3) K. I. Kugel and D. I. Khomskii, Zh. Eksp. Teor. Fiz. 64, 369 (1973) [Sov. Phys. JETP 37, 725 (1973)].

4) A. Kitaev, Ann. Phys. 321, 2 (2006).

5) G. Jackeli and G. Khaliullin, Phys. Rev. Lett. 102, 017205 (2009).

6) D. L. Cox, Phys. Rev. Lett. 59, 1240 (1987).
 
![](./images/867754556975481338_19.jpg)

Fig. 13. (Color online) Schematic T-h phase diagram for an intermediate c > 0. h is related to magnetic field H as  \( h \propto 2H_{z}^{2} - H_{x}^{2} - H_{\eta}^{2} \) , and the results for the two directions are combined. Quadrupole configurations are schematically shown by arrows with the 3-fold axes for the phase I,  \( I' \) , and III. The zigzag line indicates first order transition at h = 0 and it terminates at the critical end point XY, where the transition belongs to the 3d-XY universality class. All the other lines correspond to the continuous transition of the 3d-Ising universality class. The point TC is a tetracritical point.  \( R_{v} \)  symmetry breaks on the red lines, while  \( R_{AB} \)  symmetry breaks on the blue lines.

7) T. Onimaru, K. T. Matsumoto, Y. F. Inoue, K. Umeo, Y. Saiga, Y. Matsushita, R. Tamura, K. Nishimoto, I. Ishii, T. Suzuki, and T. Takabatake, J. Phys. Soc. Jpn. 79, 033704 (2010).

8) T. Onimaru, K. T. Matsumoto, Y. F. Inoue, K. Umeo, T. Sakakibara, Y. Karaki, M. Kubota, and T. Takabatake, Phys. Rev. Lett. 106, 177001 (2011).

9) T. Onimaru, N. Nagasawa, K. T. Matsumoto, K. Wakiya, K. Umeo, S. Kittaka, T. Sakakibara, Y. Matsushita, and T. Takabatake, Phys. Rev. B 86, 184426 (2012).

10) A. Sakai and S. Nakatsuji, J. Phys. Soc. Jpn. 80, 063701 (2011).

11) A. Sakai, K. Kuga, and S. Nakatsuji, J. Phys. Soc. Jpn. 81, 083702 (2012).

12) S. Hoshino and Y. Kuramoto, Phys. Rev. Lett. 107, 247202 (2011); ibid., 112, 167204 (2014); J. Phys. Soc. Jpn. 82, 044707 (2013).

13) A. Tsuruta and K. Miyake, J. Phys. Soc. Jpn. 84, 114714 (2015).

14) H. Kusunose, J. Phys. Soc. Jpn. 85, 064708 (2016); H. Kusunose and T. Onimaru, J. Phys.: Conf. Ser. 592, 012099 (2015).

15) T. J. Sato, S. Ibuka, Y. Nambu, T. Yamazaki, T. Hong, A. Sakai, and S. Nakatsuji, Phys. Rev. B 86, 184419 (2012).

16) M. Koseki, Y. Nakanishi, K. Deto, G. Koseki, R. Kashiwazaki, F. Shichinomiya, M. Nakamura, M. Yoshizawa, A. Sakai, and S. Nakatsuji, J. Phys. Soc. Jpn. 80, SA049 (2011).

17) I. Ishii, H. Muneshige, Y. Suetomi, T. K. Fujita, T. Onimaru, K. T. Matsumoto, T. Takabatake, K. Araki, M. Akatsu, Y. Nemoto, T. Goto, and T. Suzuki, J. Phys. Soc. Jpn. 80, 093601 (2011).

18) I. Ishii, H. Muneshige, S. Kamikawa, T. K. Fujita, T. Onimaru, N. Nagasawa, T. Takabatake, and T. Suzuki, Phys. Rev. B 87, 205106 (2013).

19) K. Matsubayashi, T. Tanaka, A. Sakai, S. Nakatsuji, Y. Kubo, and Y. Uwatoko, Phys. Rev. Lett. 109, 187004 (2012).

20) K. Hattori and H. Tsunetsugu, J. Phys. Soc. Jpn. 83, 034709 (2014).

21) K. Iwasa, H. Kobayashi, T. Onimaru, K. T. Matsumoto, N. Nagasawa, T. Takabatake, S. O. Kawamura, T. Kikuchi, Y. Inamura, and K. Nakajima, J. Phys. Soc. Jpn. 82, 043707 (2013).

22) F. Y. Wu, Rev. Mod. Phys. 54, 235 (1982).

23) J. R. Banavar, G. S. Grest, and D. Jasnow, Phys. Rev. Lett. 45, 1424 (1980).

24) G. S. Grest and J. R. Banavar, Phys. Rev. Lett. 46, 1458 (1981).

25) A. Rosengren and S. Lapinskas, Phys. Rev. Lett. 71, 165 (1993).

26) M. Kolesik and M. Suzuki, Physica A 216, 469 (1995).

27) A. Pelizzola, Phys. Rev. E 54, 5885(R) (1996).

28) R. K. Heilmann, J.-S. Wang, and R. H. Swendsen, Phys. Rev. B 53, 2210 (1996).

29) J. Ni and B. Gu, Phys. Lett. A 259, 164 (1999).

30) S. Lapinskas and A. Rosengren, Phys. Rev. Lett. 81, 1302 (1998).

31) S. Rahman, E. Rush, and R. H. Swendsen, Phys. Rev. B 58, 9125 (1998).

32) C. Yamaguchi and Y. Okabe, J. Phys. A 34, 8781 (2001).

33) U. Wolff, Phys. Rev. Lett. 62, 361 (1989).

34) M. Campostrini, M. Hasenbusch, A. Pelissetto, and E. Vicari, Phys. Rev. B 74, 144506 (2006).

35) K. Harada, Phys. Rev. E 84, 056704 (2011).

36) T. Tayama, T. Sakakibara, K. Kitami, M. Yokayama, K. Tenya, H. Amitsuka, D. Aoki, Y. Ōnuki, Z. Kletowski, J. Phys. Soc. Jpn. 70, 248 (2001).

37) S. El-Showk, M. F. Paulos, D. Poland, S. Rychkov, D. Simmons-Duffin, and A. Vichi, J. Stat. Phys. 157, 869 (2014).

38) D. Blankschtein, M. Ma, A. N. Berker, G. S. Grest, and C. M. Soukoulis, Phys. Rev. B 29, 5250 (1984).

39) M. Oshikawa, Phys. Rev. B 61, 3430 (2000).

40) S. Okamoto, S. Ishihara, and S. Maekawa, Phys. Rev. B 65, 144403 (2002).

41) A. Rynbach, S. Todo, and S. Trebst, Phys. Rev. Lett. 105, 146402 (2010).

42) T. Onimaru and H. Kusunose, J. Phys. Soc. Jpn. 85, 082002 (2016).

43) T. Ikeura, T. Matsubara, Y. Machida, K. Izawa, N. Nagasawa, K. T. Matsumoto, T. Onimaru, and T. Takabatake, JPS Conf. Proc. 3, 011091 (2014), T. Onimaru, K. Izawa, K. T. Matsumoto, T. Yoshida, Y. Machida, T. Ikeura, K. Wakiya, K. Umeo, S. Kittaka, K. Araki, T. Sakakibara, and T. Takabatake, arXiv:1606.09571.

44) Y. Shimura, Y. Ohta, T. Sakakibara, A. Sakai, and S. Nakatsuji, J. Phys. Soc. Jpn. 82, 043705 (2013).

45) M. Tsujimoto, Y. Matsumoto, M. Tomita, A. Sakai and S. Nakatsuji, Phys. Rev. Lett. 113, 267001 (2014).

46) Y. Shimura, M. Tsujimoto, B. Zeng, L. Balicas, A. Sakai, and S. Nakatsuji, Phys. Rev. B 91, 241102(R) (2015).
 
