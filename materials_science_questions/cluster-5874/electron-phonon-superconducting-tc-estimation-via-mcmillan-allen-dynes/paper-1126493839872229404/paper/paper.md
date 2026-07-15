
# Spin liquid phase in the Hubbard model: Luttinger-Ward analysis of the slave-rotor formalism

Xia-Ming Zheng and Mehdi Kargarian \( ^{*} \) 

Department of Physics, Sharif University of Technology, Tehran 14588-89694, Iran

We propose an approach for studying the spin liquid phase of the Hubbard model on the triangular lattice by combining the Baym–Kadanoff formalism with the slave rotor parton construction. This method enables the computation of a series of two-body Feynman diagrams for the Luttinger–Ward (LW) functional using a one-loop truncation. This approach enables us to study the U(1) quantum spin liquid phase characterized by a spinon Fermi surface and to derive the Green's functions for spinons, chargons, and electrons. Our findings extend beyond the standard mean-field approximation by accounting for the effects of gauge field fluctuations. The spatial components of the U(1) gauge field are equivalently represented by interactions that incorporate corrections from the spinon-chargon two-particle random phase approximation. This framework effectively captures the long-range correlations inherent to the U(1) quantum spin liquid and combines non-perturbative quantum field theory with the projective construction, providing new insights into the study of quantum spin liquids and other strongly correlated electron systems. We demonstrate that our approach correctly reproduces the anomalous low-temperature behavior of specific heat – namely, the upturn in  \( C_{V}/T \)  as a function of  \( T^{2} \) – in agreement with recent measurements on  \( 1T-TaS_{2} \) . Moreover, this approach reproduces the resonant peaks in the Mott gap, as observed in cobalt atoms on single-layer  \( 1T-TaS_{2} \) .

## I. INTRODUCTION

In tackling the challenges posed by strong correlation problems in quantum many-body systems, perturbation theories based on free-particle ground states often prove inadequate. Nevertheless, in many situations, non-perturbative effects are crucial for accurately capturing the behavior of such systems. A commonly employed approach entails solving Green's functions using non-perturbative quantum field theory techniques. Within this framework, a quintessential example is the approximate computation of the Schwinger-Dyson equations, where suitable truncations are introduced to yield relatively precise results. Additionally, self-consistent methods like GW theory  \( [1-3] \)  and the Luttinger–Ward (LW) functional theory  \( [4-8] \)  (also known as the two-particle effective action theory,  \( \Phi \) -derivable theory, or Baym–Kadanoff (BK) theory) have witnessed remarkable advancements in both theoretical developments and practical applications in recent years  \( [9-13] \) . However, due to the inclusion of infinite-order Feynman diagrams in vertex functions, exact solutions remain unattainable. The computation of higher-order vertex corrections presents monumental challenges in terms of computational complexity, making it generally infeasible to calculate high-loop Green's functions on large-scale lattices.

Beyond directly computing non-perturbative many-body Green's functions, an alternative strategy is to manually incorporate non-perturbative many-body correlation effects. A typical scheme in this vein is the projective construction, encompassing formulations such as Abrikosov fermion  \( [14] \) , Schwinger boson  \( [15] \) , slave rotor  \( [16, 17] \) , auxiliary spin  \( [18, 19] \)  etc. The central idea is to transform the original Hamiltonian to manifest as fractionalized quasiparticles rather than the real particles of the original Hamiltonian. This method has successfully elucidated phenomena like the Kondo effect  \( [18, 20, 21] \)  and heavy fermion behavior  \( [20–23] \)  and has qualitatively described Mott transitions and spin liquids  \( [16, 17, 24–27] \) . However, there are debates regarding quantitative calculations  \( [19, 25, 28–30] \) , especially at intermediate interaction strengths. Notably, recent works reveal that to accurately describe the system at the intermediate interaction strengths, one must transcend the mean-field approximation accounting for bound states of fractionalized quasiparticles and gauge fluctuations around saddle points  \( [26, 31–34] \) . Taking the potential ground state of a U(1) quantum spin liquid (QSL) with a spinon Fermi surface (SFS) in the triangular lattice Hubbard model as an example, increasing interaction strength drives the system from a Fermi liquid phase to a Mott insulator phase with spin liquid ground state. Many-body correlation effects cause electrons to fractionalize into distinct excitations known as spinons and chargons. Spinons carry spin-1/2 degrees of freedom and are electrically neutral fermions, while chargons are complex scalar fields with charge -e. In the spin liquid phase, chargons exhibit an energy gap, while spinons form a Fermi surface. Furthermore, gauge fluctuations within the system induce novel physical effects beyond the mean-field level, such as spinon Kondo effects, collective spin wave excitations and so on  \( [33–36] \) .

In this paper, we introduce a novel approach to treating the Hubbard model within the slave-rotor formulation. Our method integrates techniques from quantum field theory with parton constructions. Specifically, we employ the Luttinger–Ward (LW) functional to compute the Green's functions of various quantum fields, thereby enabling us to extract both the single-particle and two-particle spectral properties as well as the system's transport characteristics. To outline our methodology, we proceed as follows. In Sec. II, we define the model, introduce the one-loop Luttinger–Ward (LW) functional, and derive the corresponding self-consistent equations. Next, we describe the main algorithm for numerically calculating the Green's functions. These results are then used to demonstrate the existence of a spin liquid ground state in the triangular lattice Hubbard model at the one-loop exact level, as well as to showcase the density of states and spectral densities for various quasiparticles. The thermodynamic properties such as spin susceptibility, thermal conductivity, and specific
 

heat and comparison with recent measurements on  \( 1T-TaS_{2} \)  are discussed in Sec. III. Further, motivated by recent experimental observation of resonant states in cobalt atoms on single-layer  \( 1T-TaSe_{2} \)  [34] and subsequent theoretical works [33, 37], in Sec. IV we use our method to analyze the Hubbard model coupled with a single impurity. We compute the self-energy within the self-consistent first-order Born approximation and use the Bethe-Salpeter equation to calculate the impurity Green's function. Sec. V summarizes the main findings and results. The details of derivations are relegated to appendices.

## II. LUTTINGER-WARD FUNCTIONAL ANALYSIS OF HUBBARD MODEL USING THE SLAVE ROTOR CONSTRUCTION

We study the Hubbard model on a triangular lattice, which offers a rich framework for investigating strong electron correlations. The Hamiltonian reads as

 \[ H=\sum_{i,j,\sigma}t_{i j}c_{i,\sigma}^{\dagger}c_{j,\sigma}-\sum_{i,\sigma}\mu c_{i,\sigma}^{\dagger}c_{i,\sigma}+\frac{U}{2}\sum_{i}(n_{i,c}-1)^{2}, \quad (1) \] 

where  \( c_{i,\sigma} \)  ( \( c_{i,\bar{\sigma}}^{\dagger} \) ) annihilates (creates) an electron with spin  \( \sigma \)  at site i, and  \( t_{ij} \)  describes the hopping integral between sites i and j.  \( \mu \)  and U denote, respectively, the chemical potential and on-site Coulomb repulsion. By employing a U(1) slave rotor decomposition [16, 17], the electron operators are fractionalized into spinons and chargons as  \( c_{i,\sigma} = f_{i,\sigma}X_{i}^{\dagger} \) . Consequently, the Hamiltonian is transformed to [35]

 \[ \begin{align*}H=&\sum_{i,j,\sigma}t_{ij}f_{i,\sigma}^{\dagger}f_{j,\sigma}X_{j}^{\dagger}X_{i}+\mathrm{h.c.}-\sum_{i\sigma}\left(\mu+h_{i}\right)f_{i,\sigma}^{\dagger}f_{i,\sigma}\\&+U\sum_{i}P_{i}^{\dagger}P_{i}+i\sum_{i}h_{i}P_{i}X_{i}-i\sum_{i}h i X_{i}^{\dagger}P_{i}^{\dagger}\\&+\sum_{i}\lambda_{i}\left(X_{i}^{\dagger}X_{i}-1\right)+\sum_{i}h_{i}.\end{align*} \quad (2) \] 

In this formulation,  \( f_{i,\sigma} \)  ( \( f_{i,\bar{\sigma}}^{\dagger} \) ) is annihilation (creation) spinon operator.  \( X_{i,\sigma} \)  is the chargon operator as canonical coordinate and  \( P_{i,\sigma} \)  is the momentum of scalar field of chargon. They satisfy the commutation relations  \( [X_{i,\sigma}, P_{j,\sigma}] = [X_{i,\bar{\sigma}}^{\dagger}, P_{j,\sigma}^{\dagger}] = i\delta_{ij} \) .  \( \lambda_{i} \)  and  \( h_{i} \)  are the Lagrange multipliers ensuring that the constraints  \( X_{i}^{\dagger}X_{i} = 1 \)  and  \( L_{X,i} = i(X_{i}P_{i} - X_{i}^{\dagger}P_{i}^{\dagger}) = \sum_{\sigma} f_{i,\sigma}^{\dagger}f_{i,\sigma} - 1 \)  hold.

The above decomposition maps the original strong-coupling electron model into a weakly coupled one described by both spinons and chargons, where the kinetic energy term of electrons has been transformed into a two-body term

 \[ T_{k i n i c t e}=\sum_{i j\sigma}t_{i j}f_{i,\sigma}^{\dagger}f_{j,\sigma}X_{j}^{\dagger}X_{i}=\sum_{\pmb{k},\pmb{k}^{\prime},\pmb{q},\sigma}t(\pmb{q})f_{k+q,\sigma}^{\dagger}X_{k^{\prime}+q}^{\dagger}f_{k^{\prime},\sigma}X_{k}, \quad (3) \] 

![](./images/1126493839872229404_1.jpg)

FIG. 1. One loop Luttinger–Ward functional of spinons and chargons. (a) Spinon-chargon kinetic interaction in momentum-space  \( t(q)f_{k+q,\sigma}^{\dagger}X_{k+q}^{\dagger}f_{k^{\prime},\sigma}X_{k} \) . Red and blue lines represent the Green's functions of spinons and chargons, respectively. (b) Hartree-Fock diagrams, which are equivalent to the conventional mean-field theory. (c) Self-RPA polarization processes of spinons and chargons known as the self-interaction diagrams. (d) Polarization processes where spinons and chargons merge into electrons known as the binding-interaction diagrams.

where  \( t(\pmb{q}) = t\gamma(\pmb{q}) \)  with  \( \gamma(\pmb{q}) = 2(2\cos\frac{1}{2}q_{x}a\cos\frac{\sqrt{3}}{2}q_{y}a + \cos q_{x}a) \)  as the triangular lattice form factor. We call  \( T_{kinetic} \)  the kinetic interaction. To study the correlation properties of this system, we introduce a closed set of Feynman diagrams for two-particle processes, which define the Luttinger–Ward functional. The kinetic interaction is diagramatically shown in Fig. 1 (a). The Luttinger–Ward functional of spinons and chargons is written as

 \[ \Omega_{\mathrm{L W}}=\Omega_{\mathrm{H F}}+\Omega_{\mathrm{s e l f}}+\Omega_{\mathrm{b i n d}}. \quad (4) \] 

Each term is described as follows. The quantity  \( \Omega_{HF} \)  represents the self-consistent Hartree-Fock approximation – commonly known as the standard mean-field theory – and is illustrated by the diagrams in Fig. 1(b). The second term,  \( \Omega_{self} \) , represents the polarization of spinons and chargons within the random phase approximation (RPA) and is known as the self-interaction diagram. The corresponding diagrams are shown in Fig. 1(c). The last term,  \( \Omega_{bind} \) , encapsulates the polarization processes where spinons and chargons merge into electrons – a mechanism represented by the binding interaction diagrams shown in Fig. 1(d). The sum of these Feynman diagrams forms the one-loop LW functional  \( \Omega_{LW} \) . Its relationship with the self-energy of spinons and chargons – as well as with the effective kinetic interaction – is given by the following functional derivatives:
 
![](./images/1126493839872229404_2.jpg)

FIG. 2. Algorithm for self-consistent iterations of Green's functions and self-energies of spinon and chargon. We initially set self-energies ansatz  \( \Sigma(k) = C_{f}\gamma(k) \)  and  \( \Pi(k) = -C_{X}\gamma(k) \)  which are proportional to the lattice form factor. To simplify the one-loop susceptibility and self-energy calculations, we follow the widely used fast Fourier transform (FFT) trick [12, 13, 38] to avoid the Matsubara frequency summation in the convolution process.

 \[ \Sigma(k)=\frac{\delta\Omega_{\mathrm{LW}}}{\delta G_{f}(k)},\quad\Pi(k)=\frac{\delta\Omega_{\mathrm{LW}}}{\delta G_{X}(k)} \quad (5) \] 

 \[ T_{f/X,\mathrm{s e l f}}(k)=\frac{\delta^{2}\Omega_{\mathrm{s e l f}}}{\delta G_{X/f}(k)\delta G_{X/f}}(k) \quad (6) \] 

 \[ T_{\mathrm{b i n d}}(k)=\frac{\delta^{2}\Omega_{\mathrm{b i n d}}}{\delta G_{f}(k)\delta G_{X}(k)}, \quad (7) \] 

where  \(  k = (k, i\omega_{n})  \)  is 2 + 1 dimensional Matsubara frequency-momentum vector. The fermionic and bosonic frequencies shall be understood as  \(  \omega_{n} = (2n + 1)\pi/\beta  \)  and  \( v_{n} = 2n\pi/\beta \) , respectively. Based on these relationships, we derive a series of self-consistent equations that yield the Green's functions of spinons and chargons. An overview of our computational procedure is provided in the flowchart in Fig. 2.

The Green’s functions are expressed as follows:

 \[ G_{f}^{-1}(k)=G_{f,0}^{-1}(k)-\Sigma(k)+\mu, \quad (8) \] 

 \[ G_{X}^{-1}(k)=G_{X,0}^{-1}(k)-\Pi(k)-\lambda, \quad (9) \] 

with the bare Green’s functions defined as  \( G_{f,0}(k) = (i\omega_{n} + \mu)^{-1} \)  and  \( G_{X,0}(k) = -(v_{n}^{2} + \lambda)^{-1} \) . Following the steps in the flowchart in Fig. 2, the susceptibilities are expressed as

 \[ \chi^{f/X}(q)=\frac{\chi_{0}^{f/X}(q)}{1-T_{f/X,\mathrm{s e l f},0}(q)\chi_{0}^{f/X}(q)}, \quad (10) \] 

where  \( T_{f/X,self,0}(q) = -t(q)\chi_{0}^{X/f}(q)t(q) \)  is defined as bare kinetic interaction and the bare susceptibilities. They are given by  \( \chi_{0}^{f/X}(q) = \mp \sum_{k,\sigma} G_{f/X}(k)G_{f/X}(k+q) \) . The expressions for the effective kinetic interactions T are given by:

 \[ T_{f/X,\mathrm{s e l f}}(q)=t(q)\chi^{f/X}(q)t(q)=\frac{T_{f/X,\mathrm{s e l f},0}(q)}{1-T_{f/X,\mathrm{s e l f},0}(q)\chi_{0}^{f/X}(q)}, \quad (11) \] 

 \[ T_{\mathrm{b i n d}}(q)=t(q)+t(q)[-G_{c}(q)]t(q). \quad (12) \] 

The first term in  \( T_{bind} \)  represents the mean-field contribution. Additionally, the self-energies of spinon and chargon, denoted by  \( \Sigma(k) \)  and  \( \Pi(k) \) , are calculated as follows:

 \[ \Sigma(k)=-\frac{1}{\beta N}\sum_{q}\left[T_{f,\mathrm{s e l f}}(q)G_{f}(k+q)+T_{\mathrm{b i n d}}(q)G_{X}(k+q)\right], \quad (13) \] 

 \[ \Pi(k)=-\frac{1}{\beta N}\sum_{q}\left[T_{X,\mathrm{s e l f}}(q)G_{f}(k+q)+T_{\mathrm{b i n d}}(q)G_{f}(k+q)\right]. \quad (14) \] 

In addition to the self-consistent equations outlined above, the following expressions enforce the slave-rotor constraints [16, 17, 33]:

 \[ 1=-\frac{1}{\beta N}\sum_{k}G_{X}(k)e^{i\nu_{n}0^{+}}, \quad (15) \] 

 \[ \begin{align*}0&=-\frac{1}{2U\beta N}\sum_{k}i\nu_{n}G_{X}(k)\left[e^{i\nu_{n}0^{+}}+e^{-i\nu_{n} 0^{+}}\right]\\&+\frac{h}{U}+\frac{1}{\beta N}\sum_{k}G_{f,\sigma}(k)e^{i\omega_{n}0^{+}}-\frac{1}{2}.\end{align*} \quad (16) \] 

As we are interested in the spin liquid phase, the chemical potential imposing the half-filling case is set by

 \[ 1=\frac{1}{\beta N}\sum_{k,\sigma}G_{f,\sigma}(k)e^{i\omega_{n}0^{+}}. \quad (17) \]
 
![](./images/1126493839872229404_3.jpg)

![](./images/1126493839872229404_4.jpg)

![](./images/1126493839872229404_5.jpg)

![](./images/1126493839872229404_6.jpg)

FIG. 3. Density of states of (a) spinon and chargon and (b) spinon-chargon bound state, namely the physical electron. Spectral density representing the excitations of (c) spinon and (d) the physical electron.

The Eq. (16) has a solution for h = 0, thus eliminating the need for further calculation. We solve the self-consistent Eqs. (9)-(17) to obtain the spectral functions of spinons and chargons from the corresponding Green's functions. For numerical calculations we set  \( t = 0.0913935 \, eV \)  and  \( U = 0.775 \, eV \)  [33, 35]. For transition from imaginary to real frequencies, we employ intermediate representation (IR) basis [39–42] to store and calculate Matsubara Green's function, and perform Nevanlinna analytical continuation (NAC) [43–45] to achieve real frequency Green's function numerically.

Not only does the binding kinetic interaction between spinons and chargons,  \( T_{bind} \) , contribute to the aforementioned self-energy, but it also merges them into a bound state – that is, the physical electron. This process is described by ladder diagrams in the Bethe-Salpeter equation (BSE). However, employing the BSE with non-zero center-of-mass momentum in the IR basis poses significant challenges. Fortunately, since our kinetic interactions originate from electron hopping, their form simplifies the BSE on the lattice. Hence, it is more convenient to consider the BSE on a real-space lattice with imaginary time:

 \[ \begin{aligned}G_{c}\left(x_{1}^{\prime \prime},x_{2}^{\prime \prime};x_{1},x_{2}\right)=&G_{c,0}\left(x_{1}^{\prime \prime},x_{2}^{\prime \prime};x_{1},x_{2}\right)\\&-\sum_{\substack{x_{1}^{\prime},x_{2}^{\prime}\\ x_{1}^{\prime \prime},x_{2}^{^{\prime \prime}}}}G_{c,0}\left(x_{1}^{\prime \prime},x_{2}^{\prime \prime};x_{1}^{\prime},x_{2}^{^{\prime}}\right)\\&\times K^{*}\left(x_{1}^{\prime},x_{2}^{\prime};x_{1}^{\prime}, x_{2}^{\prime}\right)G_{c}\left(x_{1}^{\prime},x_{2}^{\prime};x_{1},x_{2}\right).\end{aligned} \quad (18) \] 

Here,  \( G_{c}\left(x_{1}^{\prime},x_{2}^{\prime};x_{1},x_{2}\right) \)  is the general two-body Green's function for the electron bound state, with two incoming particles with spacetime coordinates  \( x_{1},x_{2} \)  and outgoing coordinates  \( x_{i}^{\prime},x_{2}^{\prime} \) . Since in the original slave rotor theory the electron operator is defined as  \( c_{i,\sigma}=f_{i,\sigma}X_{i}^{\dagger} \) , the electron bound state is formed solely by combining the spinon and chargon at the same lattice site. Consequently, the BSE reduces to

 \[ G_{c}\left(x^{\prime\prime},x\right)=G_{c,0}\left(x^{\prime \prime},x\right)+\sum_{x^{\prime},x^{\prime \prime}}G_{c,0}\left(x^{\prime \prime},x^{\prime \prime}\right)t(x^{\prime \prime}\setminus x^{\prime})G_{c}\left(x^{\prime},x\right). \quad (19) \] 

In this equation, we substitute the first-order interaction kernel  \( K^{*}\left(x_{1}^{\prime\prime},x_{2}^{\prime\prime};x_{1}^{\prime},x_{2}^{\ prime}\right)=-t(\boldsymbol{r}_{2}^{\prime},\boldsymbol{r}_{1}^{\prime})\delta(\boldsymbol{r}_{1},\boldsymbol{r}_{2})\delta(\boldsymbol{r}^{\prime}_{1},\boldsymbol{r}^{\prime}_{2}) \)  into the BSE. As a result, the electron Green's function can be readily obtained as:

 \[ G_{c}(x^{\prime\prime},x)=\sum_{x^{\prime}}\left[1-G_{c,0}l\right]^{-1}(x^{\prime\prime},x^{\prime})G_{c,0}(x^{\prime},x). \quad (20) \] 

Using the Green’s functions  \( G_{f} \) ,  \( G_{X} \)  and  \( G_{c} \) , we show in Fig. 3 the density of states and spectral densities by computing  \( A(\boldsymbol{k}, \omega) = -\frac{1}{\pi} \operatorname{Im} \left[ G(k, i \omega_{n} \to \omega + i0^{+}) \right] \) . Fig. 3(a) shows the density of states for spinons and chargons separately. In Figure 3(b), the electron density of states reveals clear peaks corresponding to the Mott-Hubbard energy bands. Figure 3(c) illustrates the spinon spectrum, indicating the presence of a spinon Fermi surface. As expected, the electron spectrum – the bound state formed by spinons and chargons – exhibits the Mott-Hubbard energy bands, as seen in Figure 3(d). Notably, these results are obtained without invoking gauge fields, yet the spectrum closely resembles those derived using conventional mean-field theory supplemented by gauge field fluctuation methods [35, 46].

## III. THERMODYNAMIC PROPERTIES

The thermodynamic characterization of U(1) quantum spin liquids is essential for unveiling their low-energy effective field theories and underlying quantum orders. In this section, we analyze key thermodynamic observables – such as spin susceptibility, thermal conductivity, and specific heat – to elucidate the interplay between fluctuations in kinetic interactions and spinon correlations within these systems. We compute the corresponding response functions using the properties of Matsubara Green's functions and linear response theory. Investigating the physical properties of QSLs has long been challenging, primarily because the quasiparticle excitations – the spinons – are charge-neutral. Leveraging the efficiency of the IR basis to simplify Green's function calculations, we evaluate the following physical quantities:

- Spin susceptibility of spinons: Since spinons carry the intrinsic spin degrees of freedom of fractionalized electrons, their spin susceptibility directly reflects the collective magnetic excitations within the spin liquid. By analyzing this response, one can gain valuable insights into the underlying interactions governing the spin excitations.

- Thermal conductivity and specific heat: Determining the nature of QSLs often hinges on a detailed comparison of their thermodynamic and thermal transport properties. These properties are particularly contentious
 

for U(1) QSLs with a spinon Fermi surface. Here, we incorporate the temperature dependence of the self-energies to calculate the spinon thermal conductivity and specific heat. These calculations aim to provide insights into the interplay between kinetic interaction fluctuations and spinon correlations, further illuminating the low-energy behavior of these systems.

## A. Spin susceptibility

The spin structure factor  \(  S^{\alpha\beta}(q)  \)  is related to the spin relaxation rate as  \(  \tau_{1}^{-1} \propto \sum_{q} S(q)  \) . Furthermore, the  \(  S^{\alpha\beta}(q)  \)  and the spin susceptibility tensor  \( X_{\text{spin}}^{\alpha\beta} \)  is related by

 \[ S^{\alpha\beta}(q)=\frac{-2\mathrm{I m}\chi_{\mathrm{s p i n}}^{\alpha\beta}(q)}{1-e^{-\beta\omega}}, \quad (21) \] 

where  \( \chi_{\mathrm{spin}}^{\alpha\beta}(k) = -\frac{1}{N}\sum_{i}\int_{0}^{\beta}d\tau e^{i\nu_{n}\tau-i\mathbf{k}\cdot\mathbf{r}_{i}}\left\langle S^{\alpha}(\mathbf{r}_{i},\tau)S^{\beta}(0,0)\right\rangle \)  and the spin operator is defined as  \( S^{\alpha}(\mathbf{r}_{i})=\frac{1}{2}f_{i\varsigma}^{\dagger}\sigma_{\varsigma\varsigma^{\prime}}^{\alpha}f_{i,\varsigma^{\prime}} \)  [47].

The system is spin-degenerate, so we focus solely on the longitudinal component of the susceptibility. This allows us to employ Eq. (10) to compute the spin susceptibility and the corresponding spin structure factor using the one-loop exact spinon Green's function. Figure 4 shows the spin susceptibility,  \( S(\omega) \) , alongside the spin spectral density,  \( -\frac{1}{T}\mathrm{Im}\chi_{\mathrm{spin}}^{\alpha\beta}(\pmb{q},\omega) \) . At the mean-field level, as depicted in panels (a) and (c), only a single spectrum is observed at low energies. However, once the kinetic interaction is taken into account, additional features appear at higher energies manifested as broad peaks in  \( S(\omega) \)  (Fig. 4(b)) and as nearly dispersionless collective excitations in the spin spectral density (Fig. 4(d)).

## B. Thermal conductivity

In the absence of mobile charge carriers, thermal conductivity is predominantly governed by spinon contributions, thereby revealing the gapless nature of the spinon Fermi surface. The thermal conductivity is defined by [48, 49]:

 \[ \kappa_{f}(T)=-\frac{1}{T}\lim_{\omega\rightarrow0}\frac{\mathrm{I m}[\Pi_{f}(\pmb{q}=0,\omega)]}{\omega}, \quad (22) \] 

where  \( \Pi_{f}(\pmb{q},\omega) \)  is the xx-component of spinon energy current-current correlation function. To account for the effects of interactions, the energy flow correlation function is separated into the free and interaction parts:  \( \Pi_{f} = \Pi_{f,0} + \Pi_{f,\nu} \) . The interaction part  \( \Pi_{f,\upsilon} \)  is computed as [50]:

 \[ \Pi_{f,\upsilon}(q)=-\Pi_{f,l c}(q)T_{\mathrm{s e l f}}(q)\Pi_{f,r c}(q), \quad (23) \] 

where the left and right vertices are:

 \[ \Pi_{f,l c}(q)=\Pi_{f,r c}(q)=-\frac{1}{\beta N}\sum_{k}\Gamma_{x}(\pmb{k},\pmb{k}+\pmb{q})G_{c}(k)G_{c}(k+q) \quad (24) \] 

![](./images/1126493839872229404_7.jpg)

![](./images/1126493839872229404_8.jpg)

![](./images/1126493839872229404_9.jpg)

![](./images/1126493839872229404_10.jpg)

FIG. 4. Spin structure factor  \( S(\omega) \)  calculated by considering (a) only the Hartree-Fock diagrams and (b) incorporates the kinetic effective self-interactions on top of the Hartree-Fock result. The spectral density of the spin susceptibility along high-symmetry paths in momentum space using only (c) Hartree-Fock diagrams (d) including the self-interaction corrections.

with bare vertex \(\Gamma_{x}(\pmb{k},\pmb{k}+\pmb{q})=\frac{1}{2}\left(\frac{\partial\gamma}{\partial\kappa_{i}}\bigg|_{\pmb{k}}+\frac{\partial\gamma}{\partial\kappa_{i}}\bigg|_{\pmb{k}+\pmb{q}}\right)\). The details are given in Appendix A.

As shown in Fig. 5(a), the spectral density of the spinon current-current correlation function as a function of frequency clearly reveals both a Drude peak and side peaks induced by  \( T_{self} \) , which is reminiscent of a typical Fermi liquid [51–53]. Meanwhile, in order to investigate the thermal transport properties of the spin liquid, it is crucial to examine the temperature dependence of the spinon thermal conductivity—this quantity often reflects the type of spin liquid and the characteristics of its low-energy excitations. Fig. 5(b) presents the approximate variation of the spinon DC conductivity, with increasing temperature. Here, the DC conductivity is estimated using the Matsubara data,  \( \sigma_{f} \sim T\kappa_{f} \approx -Im\left[\frac{\Pi_{f(\nu_{l})}}{\nu_{l}}\right] \) , where  \( i\nu_{1} = 2\pi/\beta \)  is the lowest bosonic Matsubara frequency. The fitting of the numerical data indicates that the spinon DC conductivity exhibits an inverse linear dependence on temperature, from which one readily deduces that the spinon thermal conductivity should vary inversely with the square of the temperature as shown in Fig. 5(c). This result is in contrast to earlier theoretical predictions that the thermal conductivity of a clean U(1) spin liquid with a Fermi surface should scale as  \( T^{1/3} \)  [48, 54].

The above conclusion can be further corroborated by examining the temperature dependence of the spinon self-energy at low energies. As depicted in Fig. 5 (d), a clear linear relationship emerges for the imaginary part. Here, we are concerned about the contribution of effective kinetic interaction scattering to the spinon thermal transport. The scattering rate is directly connected to the imaginary part of the self-energy via  \( \Gamma_{f} = -2\mathrm{Im}[\Sigma] \propto T \)  which implies  \( \sigma_{f} \propto \frac{1}{\Gamma_{f}} \propto T^{-1} \) . Hence, the spinon thermal conductivity indeed scales inversely with the
 
![](./images/1126493839872229404_11.jpg)

![](./images/1126493839872229404_12.jpg)

![](./images/1126493839872229404_13.jpg)

![](./images/1126493839872229404_14.jpg)

![](./images/1126493839872229404_15.jpg)

![](./images/1126493839872229404_16.jpg)

FIG. 5. (a) Imaginary part of spinon current-current correlation function  \( -\frac{1}{\pi}\mathrm{Im}[\Pi_{f}(\boldsymbol{q}\to0,\omega)] \) . (b) Temperature variation of spinon DC conductivity calculated by evaluation of  \( -\mathrm{Im}\left[\Pi_{f}(iv_{1})/iv_{1}\right] \)  at the lowest Bosonic Matsubara frequency. Here the blue dots correspond to numerical data fitted by  \( a + b/T \) . (c) Spinon thermal conductivity as a function of  \( T^{-2} \) . (d) Imaginary and real parts of spinon self-energy. Panel (e) displays the electron internal energy computed by incorporating the temperature dependence of the self-energy, resulting in a linear-in-T behavior. In contrast, panel (f) shows the electron internal energy determined using zero-temperature parameters ( \( T = 10^{-4}K \) ), which yields a quadratic temperature dependence.

square of the temperature.

## C. Specific heat

One of the key physical observables for probing and characterizing spin liquids is the temperature-dependent behavior of internal energy and specific heat. Using the electron Green's function obtained in Eq. (20), the average electron internal energy is calculated as  \( \langle E_{c}\rangle = \frac{1}{\beta N} \sum_{k} i\omega_{n} G_{c}(k) e^{i\omega_{n} 0^{+}} \) , which increases linearly with temperature, as illustrated in Fig. 5(e). In this analysis, we allow the mean-field parameters to vary with temperature as expected. According to the definition of the electronic specific heat,  \( C_{V} = \left. \frac{\partial \langle E_{c} \rangle}{\partial T} \right|_{V} \) , one might expect that the specific heat of the U(1) spin liquid remains temperature-independent—a prediction that contrasts with previous calculations reporting a linear-T electron specific heat [35, 37, 48, 49, 55]. However, if the mean-field parameters are assumed to be temperature-independent, the internal energy grows quadratically with temperature (see Fig. 5(f)), thereby yielding a linear-T specific heat.

The specific heat of the layered transition-metal dichalcogenide 1T-TaS \( _{2} \)  [56, 57], which is believed to host a putative spin liquid ground state, has been measured. We employed the software described in [58] to digitize the experimental data (represented by circular and triangular markers in Fig. 6), and Wolfram Mathematica [59] was used to perform the fitting. The experimental data indicate that the temperature dependence of the specific heat is best captured by  \( C_{V} = \alpha + \beta T^{3} \) , where  \( \alpha \)  represents the electronic contribution to the specific heat and  \( \beta \)  is the Debye coefficient associated with the phonon contribution. We adopt the high-temperature Debye coefficient  \( \beta \)  from [56] and determine electronic contribution  \( \alpha \)  by using the internal energy data from Fig. 5(e) to plot  \( C_{V}/T \)  as a function of  \( T^{2} \) . The measured upturn in the low-temperature regime is correctly captured by the solid blue line in Fig. 6—a feature that the previously assumed linear electronic specific heat could not account for.

To clarify the discrepancies between our findings and those obtained via conventional methods, we present the following comments.

1. In conventional approaches, a mean-field saddle-point solution is adopted with gauge fluctuations treated at the quadratic level. In this framework, the inverse of the transverse gauge-field Green's function is expressed as  \( D_{ij}^{-1}(q) = \Pi_{f,ij} + \Pi_{X,ij} \) , where  \( \Pi_{f,ij} \)  and  \( \Pi_{X,ij} \)  denote the ij components of the spinons and chargons (or holons) current-current correlation function, respectively [54, 60, 61]. In the long-wavelength limit, the transverse gauge-field propagator vanishes as  \( q^{3} \) . Consequently, its interaction with the spinons generates a self-energy with both real and imaginary parts scaling as  \( \operatorname{Re}[\Sigma] \sim \operatorname{Im}[\Sigma] \propto \omega^{2/3} \) . This behavior leads directly to a divergent density of states and effective mass, a specific heat that scales as  \( T^{2/3} \) , and a thermal conductivity varying as  \( T^{1/3} \) .

2. In this work, we derive the spinon self-energy from Eqs.
 
![](./images/1126493839872229404_17.jpg)

FIG. 6. The measured (digitized) and calculated  \( C_{V}/T \)  as a function of  \( T^{2} \) . The red open circles correspond to zero-field specific heat measurements of  \( 1T-TaS_{2} \)  reported in [56] and the green triangles indicate the zero-field specific heat of  \( 1T-TaS_{2} \)  presented in [57]. The reuse of measured data – shown by red and green markers – is with permission. The blue solid curve is obtained by combining our theoretically evaluated internal energy with the phonon contribution reported in [56]. Our theoretical approach successfully captures the upturn behavior at low temperatures, where only the electronic contributions are present.

(12)-(14). The effective kinetic interaction,  \( T_{f,\mathrm{self}}(q) \) , defined relative to the Hartree-Fock diagrams at the mean-field level, plays a role analogous to the conventional RPA correction in an interacting Fermi gas. The poles in the high-frequency regime correspond to collective spinon excitations, as illustrated in Fig. 4 (b) and (d). Importantly, the absence of divergence in the low-energy density of states ensures that the spinons possess a well-defined, stable Fermi surface.

3. In [55], it was demonstrated that a proper treatment of the emergent gauge field restricts its low-energy excitations to contribute no more than a  \( T^{2} \)  term to the specific heat. This result rules out the previously reported anomalous behaviors—namely, the  \( T^{2/3} \)  variation in specific heat and the  \( T^{1/3} \)  scaling of thermal conductivity. Consequently, in the U(1) spinon Fermi surface spin liquid considered here, both the specific heat and the thermal conductivity follow conventional Fermi liquid behavior.

4. Although our work acknowledges the similarity between U(1) spinon Fermi surface spin liquid and that studied in [55], our analysis reveals a distinct temperature dependence. As the temperature increases, electrons maintain their spin liquid phase over a certain range, and the spinons preserve their Fermi liquid character. However, beyond the thermal fluctuations, we observe that both the Green's functions and the real parts of the self-energies for spinons and chargons decrease notably with rising temperature, as shown in Fig. 5(d). This behavior contrasts with previous studies that have assumed temperature-independent spinon and chargon Green's functions and self-energies, assumptions that may lead to contentious conclusions. Furthermore, as illustrated in Fig. 5(f), when we calculate the electron Green's function at nearly zero temperature and then simply increase the temperature – thereby accounting solely for thermal fluctuations – the electron internal energy exhibits a quadratic growth with temperature. This quadratic increase predicts an electron specific heat that scales linearly with temperature – a characteristic of conventional Fermi liquid behavior – which, however, fails to account for the anomalous specific heat behavior observed in Fig. 6.

## IV. SPINON KONDO EFFECT AND THE ROLE OF KINETIC INTERACTION

To further validate and extend the applicability of our method, in this section we study a spin liquid phase coupled to dilute magnetic impurities. This study is motivated by recent experimental observation of resonant states in cobalt atoms on single-layer  \( 1T-TaSe_{2} \)  [34]. A slave-rotor analysis of the model supplemented by gauge fields can account for the resonant states [33, 37]. Here, we reconsider the problem and treat it using the approach stated in preceding section. The Hubbard model coupled with a magnetic impurity reads as

 \[ \begin{aligned}H_{\mathrm{hybrid}}=&\sum_{i,j,\sigma}t_{ij}c_{i,\sigma}^{\dagger}c_{j,\sigma}+\sum_{\sigma}\epsilon_{d}d_{r}^{\dagger}d_{\sigma}+V\sum_{\sigma}c_{0,\sigma}^{\dagger}d_{\sigma}+\mathrm{h.c.}\\&+\frac{U}{2}\sum_{i}(n_{i,c}-1)^{2}+\frac{U_{\mathrm{imp}}}{2}(n_{d}-1)^{2},\end{aligned} \quad (25) \] 

In this equation, parameter V is the local impurity-host electron hybridize and  \( U_{imp} \)  is local impurity interaction. Similarly, by replacing the electron operators with slave particles as  \( c_{i,\sigma} = f_{i,\sigma} X_{i}^{\dagger} \) ,  \( d_{i,\sigma} = a_{i,\sigma} Y_{i}^{\dagger} \) , in this representation we obtain the impurity hybridized Hamiltonian  \( H_{hybrid} = H + H' \) , where H is the Hamiltonian of spin liquid in Eq. (2) and  \( H' \)  describes the impurity and hybridization with the spin liquid:

 \[ \begin{aligned}H^{\prime}=&(\epsilon_{d}-h_{2})a_{r}^{\dagger}a_{\sigma}+U_{\mathrm{imp}}Q^{\dagger}Q+\lambda_{2}\left(Y^{\dagger}Y-1\right)+h_{2}\\&+V\sum_{\sigma}f_{r}^{\dagger}a_{\sigma}Y^{\dagger}X+h.c.\end{aligned} \quad (26) \] 

The operator Q is canonical momentum of Y which satisfies  \( [Q,Y]=i \) . Additionally, the parameters  \( \lambda_{2} \)  and  \( h_{2} \)  are Lagrange multiplies, constraining the norm of impurity chargon Y and impurity angular momentum.

In terms of coupled system, it is straightforward to define the joined field basis:  \( \psi = (a, f)^{T} \)  and  \( \phi = (Y, X)^{T} \) . Then the self-energies of coupled system take forms of symmetric off-diagonal matrices:  \( \Sigma_{hybrid} = -i\omega\sigma_{y} \) ,  \( \Pi_{hybrid} = i\omega\sigma_{y} \)  where  \( \sigma_{y} \)  denotes the y-Pauli matrix. Finally, the self-consistent equations within the first-order Born approximation are derived as (the details of derivation are given in Appendix B):
 
![](./images/1126493839872229404_18.jpg)

![](./images/1126493839872229404_19.jpg)

FIG. 7. (a) Variation of coupling and constraint fields in the first order self-consistent Born approximation. Datas are shown as a function of increasing V with  \( U_{imp} = 3 \)  eV. (b) Impurity electron spectral functions with (red) and without (blue) the contribution of binding interaction  \( T_{bind} \) , when V = 0.2 eV. Close to the main Hubbard bands the resonant peaks appear due to the bindig interaction.

 \[ u=-\frac{2V}{\beta}\sum_{n}G(a,f^{\dagger},i\omega_{n},\sigma), \quad (27) \] 

 \[ w=-\frac{V}{\beta}\sum_{n}G(X,Y^{\dagger},i\nu_{n}), \quad (28) \] 

 \[ 1=-\frac{1}{\beta}\sum_{n}G(Y,Y^{\dagger},i\nu_{n})e^{i\nu_{n}0^{+}}, \quad (29) \] 

 \[ \begin{align*}0=&-\frac{1}{2U\beta}\sum_{n}i\nu_{n}G(Y,Y^{\dagger},i\nu_{n})\Big[e^{i\nu_{n}0^{+}}+e^{-i\nu_{n} 0^{+}}\Big]\\&+\frac{h_{2}}{U}+\frac{1}{\beta}\sum_{n}G(a,a^{\dagger},i\omega_{n},\sigma)e^{i\omega_{n}0^{+}}-\frac{1}{2}.\end{align*} \quad (30) \] 

In equations Eqs (28)-(30), u and w represent the impurity scattering self-energies for chargon and spinon respectively. Additionally, Eqs (29) and (30) correspond to the constraints on the norm and angular momentum of the chargons, respectively.

The variation of effective couplings u and w is shown in Fig. 7(a). It is evident that as the impurity hybridization strength V increases, a critical point emerges. For values of V below this threshold, the impurity decouples from the spin liquid [33, 34]. However, beyond the critical point a hybridized phase sets in; in this phase, the self-energies u and w as well as the angular momentum Lagrange multiplier  \( h_{2} \)  acquire nonzero values. Moreover, the chargon amplitude Lagrange multiplier  \( \lambda_{2} \)  grows with V, a consequence of the local impurity no longer being restricted to single occupancy.

Within our approach the resonant states, as observed experimentally in [34], are captured by computing the local Green's function taking into account binding interaction  \( T_{bind} \)  derived from the  \( \Omega_{LW} \) . As mentioned before, the  \( T_{bind} \)  fuses spinons and chargons into bound states forming electrons. We calculate the impurity electron Green's function corrected by the BSE effective interaction:

 \[ \begin{align*}G_{d}(i\omega_{n})=&G_{d,0}(i\omega_{n})-[G(a,f^{\dagger})*G(X,Y^{\dagger})](i\omega_{n})\\&\times T_{\mathrm{bind}}(i\omega_{n},0)[G(f,a^{\dagger})*G(Y,X^{\dagger})](i\omega_{n}).\end{align*} \quad (31) \] 

Here,  \(  G_{d,0}(i\omega_{n}) = -[G(a, a^{\dagger}) * G(Y, Y^{\dagger})](i\omega_{n}) = -\frac{1}{\beta} \sum_{n} G(a, a^{\dagger}, i\omega_{n} + i\nu_{n}) G(Y, Y^{\dagger}, i\nu_{n})  \)  is the impurity electron Green's function. The symbol * denotes convolution in Matsubara-momentum space. We present the local impurity density of states in Fig. 7 (b), where we considered the cases with and without the corrections yielded by kinetic interaction  \( T_{bind} \) . As seen, the differences are significant. The inclusion of kinetic interaction leads to the formation of resonant peaks, while in for the case of no kinetic interaction only the local Hubbard states are observed.

## V. CONCLUSIONS

In this work, we have developed a unified framework combining the Luttinger–Ward functional approach with the slave rotor formalism to investigate the U(1) quantum spin liquid (QSL) phase in the triangular lattice Hubbard model. By systematically constructing the one-loop LW functional for spinons and chargons, we derived self-consistent equations for Green's functions while incorporating gauge field fluctuations beyond conventional mean-field approximations. Our results demonstrate the emergence of a spin liquid ground state characterized by a spinon Fermi surface and gapped chargon excitations, consistent with spin-charge separation in strongly correlated systems.

The main findings are summarized as follows: (1) at the level of self-consistent one-loop truncation, the triangular lattice Hubbard model with slave rotor construction admits a U(1) spin liquid with a spinon Fermi surface ground state. (2) in this approach the effective kinetic interaction  \( T_{bind} \)  (equivalent to emergent U(1) photons) mediates spinon-chargon binding processes, enabling the reconstruction of electronic spectral functions through Bethe-Salpeter equations. (3) the spinon-dominated thermal conductivity exhibits a linear behavior in  \( T^{-2} \) , which is in contrast to prior theoretical predictions of  \( T^{1/3} \)  scaling. This discrepancy highlights the critical role of gauge fluctuations in modifying low-energy transport properties. (4) compared with recent specific heat measurements on  \( 1T-TaS_{2} \)  [56, 57], our approach correctly captures the anomalous behavior of electronic specific heat at low temperatures akin to the unconventional temperature dependence of the spinon/chargon Green's functions, suggesting a reinterpretation of thermodynamic signatures in QSL candidates. (5) the effective kinetic interaction  \( T_{bind} \)  introduced in this approach also mimicks the resonant peaks as observed in cobalt atoms on single-layer  \( 1T-TaSe_{2} \)  [34].

The methodology presented here combines non-perturbative quantum field theory with projective construction techniques, offering a versatile platform to explore intertwined orders and fractionalized phases in correlated systems. Future extensions could incorporate higher-loop corrections to refine gauge fluctuation effects or generalize the formalism to  \( Z_{2} \)  or SU(2) spin liquids. Experimental verification of our predictions—such as the  \( T^{-2} \) -scaling thermal conductivity and impurity-induced spectral features—would provide crucial tests for U(1) QSL scenarios in triangular lattice materials. This work establishes a pathway for quantitatively connecting microscopic strong correlation physics with macroscopic observable quantities in quantum spin liquids.
 

and related phases.

## ACKNOWLEDGMENTS

The authors would like to thank Sharif University of Technology for supports. ZXM thanks Elahe Davari, Yin Zhong and Hui Li for helpful discussion. We also thank Microsoft’s Copilot for revising several sentences in the latest version of the manuscript to enhance clarity.

## Appendix A: Current operator and current-current correlation function on lattice

To calculate the thermal conductivity of spinons, it is essential to consider the energy flow density correlation function. The energy flow density, also referred to as the momentum density, is expressed as  \( [62] \) :

 \[ p_{x}(\boldsymbol{r})=\frac{1}{i a}\sum_{i}\cos(\phi_{i})(\psi^{\dagger}(\boldsymbol{r})\psi(\boldsymbol{r}+\boldsymbol{a}_{i})-\psi^{\dagger}(\boldsymbol{r}+\boldsymbol{a_{i}})\psi(\boldsymbol{r})), \quad (A1) \] 

where  \( a_{i} \)  represents the lattice vector. The term  \( \cos(\phi_{i}) \)  represents the cosine of the angle between the lattice vector and the direction of the energy flow (in this case, evidently the x-direction). The angle  \( \phi_{i} \)  is defined as  \( \phi_{l} = \arctan(a_{1,l}/a_{1,x}) \) . By Fourier transforming the energy flow density into the crystal momentum representation, it becomes:

 \[ p_{x}(\boldsymbol{q})=\frac{1}{N}\sum_{k}\left[\frac{1}{2}\left(\frac{\partial\gamma(\boldsymbol{k})}{\partial k_{x}}\bigg|_{k}+\frac{\partial\gamma(\boldsymbol{k})}{\partial k_{x}}\bigg|_{k+q}\right)\psi^{\dagger}(\boldsymbol{k})\psi(\boldsymbol{k}+\boldsymbol{q})\right], \quad (A2) \] 

where the operator  \( \psi \)  is any Schrodinger bosonic or fermionic operator. Here, only the xx-component of the correlation function is calculated:  \( \Pi_{xx}(x_{2},x_{1}) = -\langle p_{x}(\boldsymbol{r}_{2},\tau_{2})p_{x}(\boldsymbol{r}, \tau_{1})\rangle \) . where  \( x = (r, \tau) \)  is the Euclidean spacetime coordinate. Substituting the  \( p_{x} \)  operator into  \( \Pi_{xx} \) , the expansion consists of multiple ensemble averages of products of four  \( \psi \) -operators, which are:

 \[ \left\langle\psi^{\dagger}(x_{2})\psi(x_{2}+\boldsymbol{a}_{i})\psi^{\dagger}(x_{1})\psi(x_{1}+\boldsymbol{a}_{j})\right\rangle=\pm G_{\psi}(x_{2}+\boldsymbol{a}_{i},x_{1})G_{\psi}(r_{1}+\boldsymbol{a}_{j},x_{2})=\pm G_{\psi}(\Delta x+\boldsymbol{a}_{i})G_{\psi}(-\Delta x_{1}+\boldsymbol{a}_{j}) \] 

 \[ \left\langle\psi^{\dagger}(x_{2}+\boldsymbol{a}_{i})\psi(x_{2})\psi^{\dagger}(x_{1})\psi(x_{1}+\boldsymbol{a}_{j})\right\rangle=\pm G_{\psi}(x_{2},x_{1})G_{\psi}(x_{1}+\boldsymbol{a}_{j},x_{2}+\boldsymbol{a}_{i})=\pm G_{\psi}(\Delta x)G_{\psi}(-\Delta x+\Delta\boldsymbol{a}_{ji}) \] 

 \[ \left\langle\psi^{\dagger}(x_{2})\psi(x_{2}+\boldsymbol{a}_{i})\psi^{\dagger}(x_{1}+\boldsymbol{a}_{j})\psi(x_{1})\right\rangle=\pm G_{\psi}(x_{2}+\boldsymbol{a}_{i},x_{1}+\boldsymbol{a}_{j})G_{\psi}(x_{1},x_{2})=\pm G_{\psi}(\Delta x+\Delta\boldsymbol{a}_{ij})G_{\psi}(-\Delta x) \] 

 \[ \left\langle\psi^{\dagger}(x_{2}+\boldsymbol{a}_{i})\psi(x_{2})\psi^{\dagger}(x_{1}+\boldsymbol{a}_{j})\psi(x_{1})\right\rangle=\pm G_{\psi}(x_{2},x_{1}+\boldsymbol{a}_{j})G_{\psi}(x_{1},x_{2}+\boldsymbol{a}_{i})=\pm G_{\psi}(\Delta x-\boldsymbol{a}_{j})G_{\psi}(-\Delta x-\boldsymbol{a_{i}}) \quad (A3) \] 

where  \( \pm \)  takes -1 for fermions and +1 for bosons, and  \( G_{\psi}(x_{2},x_{1}) \)  denotes the single-particle Green's function corresponding to the operator  \( \psi \) . In the case of equilibrium systems with lattice symmetry, the Green's function depends only on  \( \Delta x = x_{2} - x_{2} = (r_{2} - r_{1}, \tau_{2} - \tau_{1}) \) . The symbol  \( \Delta a_{ij} = a_{i} - a_{j} \)  is definitely as the difference between two lattice vector. Consequently, the spatial-temporal correlation function becomes:

 \[ \begin{align*}\Pi_{xx}(\Delta x)=\pm\frac{1}{a^{2}}\sum_{ij}\cos(\phi_{i})\cos(\phi_{j})\Big[G_{\psi}(\Delta x+\boldsymbol{a}_{i})G_{\psi}(-\Delta x_{1}+\boldsymbol{a}_{j})+G_{\psi}(\Delta x)G_{\psi}(-\Delta x+\Delta\boldsymbol{a}_{ji})\\+G_{\psi}(\Delta x+\Delta\boldsymbol{\boldsymbol{a}}_{ij})G_{\psi}(-\Delta x)+G_{\psi}(\Delta x-\boldsymbol{a}_{j})G_{\psi}(-\Delta x-\boldsymbol{a_{i}})\Big]\end{align*} \quad (A4) \] 

After Fourier transformation, the momentum-Matsubara frequency correlation function is obtained:

 \[ \Pi_{x x}(k)=\pm\sum_{k}\Gamma_{x x}(k,\boldsymbol{k}+\boldsymbol{q})\Gamma_{x x}({\boldsymbol{k}}+\boldsymbol{q},\boldsymbol{k})G_{\psi}(\boldsymbol{k},i\nu_{n})G_{\psi}(\pmb{k}+\pmb{q},i\nu_{n}+i\omega_{n}), \quad (A5) \] 

where the bare current vertex is defined as:  \( \Gamma_{x}(k,k+q)=\frac{1}{2}\left(\left.\frac{\partial\gamma}{\partial k_{x}}\right|_{k}+\left.\frac{\partial\gamma}{\partial k_{x}}\right|_{k+q}\right) \) . In the continuum model, bare current vertex reduces to the usual form  \( \Gamma_{x}(k,k+q)=\frac{1}{2m}(2k_{x}+q_{x}) \) .

To account for the effects of interactions, the energy flow correlation function is separated into the free and interaction parts:  \( \Pi_{xx} = \Pi_{0,xx} + \Pi_{v,xx} \) . The interaction part  \( \Pi_{v,XX} \)  is computed as [50]:

 \[ \Pi_{v,xx}(q)=-\Pi_{l,c,xx}(q)V(q)\Pi_{rc,xx}(q), \quad (A6) \]
 

where  \( V(q) \)  represents the particle interaction, and:

 \[ \Pi_{l c,x x}(q)=\Pi_{r c,x x}(q)=-\frac{1}{\beta N}\sum_{k}\Gamma_{x x}(k,k+q)G_{\psi}(k)G_{\psi}({k+q}). \quad (A7) \] 

By substituting  \( T_{\mathrm{self}}(q) \)  into  \( V_{eff} \) , and setting  \( \psi \)  to the spinon operator f, the spinon energy flow correlation function is thus obtained.

## Appendix B: Self-Consistent Equations of Impurity coupled quantum spin liquid Hamiltonian Under First-Order Born Approximation

We consider the case of infinite single-impurity scattering processes. Since the original Hamiltonian does not include the self-energy from impurity coupling, it must be manually introduced and solved self-consistently, which is equivalent to the first-order self-consistent Born approximation. Assuming that the spinon and chargon Green's functions after impurity coupling take the following forms:

 \[ \begin{align*}G(\psi,\psi^{\dagger},i\omega_{n},\sigma)=&\left[\left(i\omega_{n}-\epsilon_{d}+i\hbar_{2}\quad0\quad0\right)^{-}\Sigma_{\mathrm{hybrid}}\right]^{-1},\\G(\phi,\phi^{\dagger},i\nu_{n})=&-\left[\left(\begin{array}{cc}-(i\nu_{n}+\hbar_{2})^{2}/U_{\mathrm{imp}}+\lambda&0\\0&G^{-1}(X,X^{\dagger},i\nu_{n},\boldsymbol{r}=0)\end{array}\right)+\Pi_{\mathrm{hybrid}}\right]^{-1}.\end{align*} \quad (B1) \] 

Here,  \( \psi = (a, f)^{T} \)  and  \( \phi = (Y, X)^{T} \)  are the composite operator bases for spinons and chargons, respectively.  \( \Sigma_{hybrid} \)  and  \( \Pi_{hybrid} \) , are the self-energies of spinons and chargons due to their coupling, which are assumed to be frequency-independent. Specifically, we have:

 \[ \begin{aligned}\Sigma_{hybrid}&=\left(\begin{array}{cc}{{{0}}}&{{{w}}} \\{{{w}}}&{{{0}}}\end{array}\right)\\\Sigma_{hybrid}&=\left(\begin{array}{cc}{{{0}}}&{{{-u}}} \\{{{-u}}}&{{{0}}}\end{array}\right)\end{aligned} \quad (B2) \] 

Next, the self-energy equations are derived based on the scattering processes:

 \[ \begin{aligned}\Sigma_{hybrid}&=-VG(\phi,\phi^{\dagger},\tau=0),\\\Pi_{hybrid}&=-VG(\psi,\psi^{\dagger},i\omega_{n},\sigma,\tau=0).\end{aligned} \quad (B3) \] 

By expanding these expressions, the self-consistent equations (27)-(28) presented in the main text are obtained.

[1] J. J. Quinn and R. A. Ferrell, Electron self-energy approach to correlation in a degenerate electron gas, Phys. Rev. 112, 812 (1958).

[2] L. Hedin, New method for calculating the one-particle green’s function with application to the electron-gas problem, Phys. Rev. 139, A796 (1965).

[3] F. Aryasetiawan and O. Gunnarsson, The gw method, Reports on Progress in Physics 61, 237 (1998).

[4] J. M. Luttinger and J. C. Ward, Ground-state energy of a many-fermion system. ii, Phys. Rev. 118, 1417 (1960).

[5] G. Baym and L. P. Kadanoff, Conservation laws and correlation functions, Phys. Rev. 124, 287 (1961).

[6] G. Baym, Self-consistent approximations in many-body sys-

tems, Phys. Rev. 127, 1391 (1962).

[7] N. Dupuis, Field Theory Of Condensed Matter And Ultracold Gases - Volume 1 (World Scientific Publishing Europe Limited, 2023).

[8] G. Stefanucci and R. van Leeuwen, Nonequilibrium Many-Body Theory of Quantum Systems: A Modern Introduction, 2nd ed. (Cambridge University Press, 2025).

[9] H. Li, Y. Su, J. Xiong, H. Lin, H. Huang, and D. Li, Post-gw theory and its application to pseudogap in strongly correlated system (2024), arXiv:2409.16762 [cond-mat.str-el].

[10] Z. Sun, Z. Fan, H. Li, D. Li, and B. Rosenstein, Modified gw method in electronic systems, Phys. Rev. B 104, 125137 (2021).

[11] H. Li, Quantum Many-Body Self-Consistent Theory and Its Ap-
 

plications, Ph.D. thesis, Peking University (2023).

[12] S. Sumita, M. Naka, and H. Seo, Fulde-ferrell-larkin-ovchinnikov state induced by antiferromagnetic order in  \( \kappa \) -type organic conductors, Phys. Rev. Res. 5, 043171 (2023).

[13] N. Witt, E. G. C. P. van Loon, T. Nomoto, R. Arita, and T. O. Wehling, Efficient fluctuation-exchange approach to low-temperature spin fluctuations and superconductivity: From the hubbard model to  \( na_{x}coo_{2} \cdot \eta H_{2}O \) , Phys. Rev. B 103, 205148 (2021).

[14] A. A. Abrikosov, Electron scattering on magnetic impurities in metals and anomalous resistivity effects, Physics Physique Fizika 2, 5 (1965).

[15] J. Schwinger, On Angular Momentum, Dover Books on Physics (Dover Publications, 2015).

[16] S. Florens and A. Georges, Quantum impurity solvers using a slave rotor representation, Phys. Rev. B 66, 165111 (2002).

[17] S. Florens and A. Georges, Slave-rotor mean-field theories of strongly correlated systems and the mott transition in finite dimensions, Phys. Rev. B 70, 035114 (2004).

[18] S. Sachdev, Quantum Phases of Matter (Cambridge University Press, 2023).

[19] M. Christos, Z.-X. Luo, H. Shackleton, Y.-H. Zhang, M. S. Scheurer, and S. Sachdev, A model ofd-wave superconductivity, antiferromagnetism, and charge order on the square lattice, Proceedings of the National Academy of Sciences 120, 10.1073/pnas.2302701120 (2023).

[20] A. Hewson, The Kondo Problem to Heavy Fermions, Cambridge Studies in Magnetism (Cambridge University Press, 1997).

[21] P. Coleman, Introduction to Many-Body Physics (Cambridge University Press, 2015).

[22] S. Burdin, D. R. Grempel, and A. Georges, Heavy-fermion and spin-liquid behavior in a kondo lattice with magnetic frustration, Phys. Rev. B 66, 045111 (2002).

[23] P. Coleman,  \( \frac{1}{\lambda} \)  expansion for the kondo lattice, Phys. Rev. B 28, 5255 (1983).

[24] K. T. Law and P. A. Lee, 1t-tas;sub \( _{c} \) 2!/sub \( _{c} \(  as a quantum spin liquid, Proceedings of the National Academy of Sciences 114, 6996 (2017), https://www.pnas.org/doi/pdf/10.1073/pnas.1706769114.} \) 

[25] P. A. Lee, N. Nagaosa, and X.-G. Wen, Doping a mott insulator: Physics of high-temperature superconductivity, Rev. Mod. Phys. 78, 17 (2006).

[26] D. Podolsky, A. Paramekanti, Y. B. Kim, and T. Senthil, Mott transition between a spin-liquid insulator and a metal in three dimensions, Phys. Rev. Lett. 102, 186401 (2009).

[27] T. Senthil, Theory of a continuous mott transition in two dimensions, Phys. Rev. B 78, 045109 (2008).

[28] M. Hermele, T. Senthil, M. P. A. Fisher, P. A. Lee, N. Nagaosa, and X.-G. Wen, Stability of  \( u(1) \)  spin liquids in two dimensions, Phys. Rev. B 70, 214437 (2004).

[29] S.-S. Lee, Stability of the  \( u(1) \)  spin liquid with a spinon fermi surface in  \( 2 + 1 \)  dimensions, Phys. Rev. B 78, 085129 (2008).

[30] Y.-H. Zhang and S. Sachdev, From the pseudogap metal to the fermi liquid using ancilla qubits, Phys. Rev. Res. 2, 023172 (2020).

[31] S.-S. Lee and P. A. Lee, U(1) gauge theory of the hubbard model: Spin liquid states and possible application to  \( \kappa \) -(BEDT-TTF) \( _{2} \) cu \( _{2} \) (CN) \( _{3} \) , Phys. Rev. Lett. 95, 036403 (2005).

[32] S.-S. Lee, Low-energy effective theory of fermi surface coupled with u(1) gauge field in  \( 2 + 1 \)  dimensions, Phys. Rev. B 80, 165102 (2009).

[33] W.-Y. He and P. A. Lee, Magnetic impurity as a local probe of

the  \( u(1) \)  quantum spin liquid with spinon fermi surface, Phys. Rev. B 105, 195156 (2022).

[34] Y. Chen, W.-Y. He, W. Ruan, J. Hwang, S. Tang, R. L. Lee, M. Wu, T. Zhu, C. Zhang, H. Ryu, F. Wang, S. G. Louie, Z.-X. Shen, S.-K. Mo, P. A. Lee, and M. F. Crommie, Evidence for a spinon kondo effect in cobalt atoms on single-layer 1t-tase2, Nature Physics 18, 1335 (2022).

[35] X.-M. Zheng and M. Kargarian, Spinon kondo lattice in quantum spin liquids using the slave-rotor formalism, Phys. Rev. B 110, 115116 (2024).

[36] L. Balents and O. A. Starykh, Collective spinon spin wave in a magnetized u(1) spin liquid, Phys. Rev. B 101, 020401 (2020).

[37] W. He, Quantum spin liquid physics in 1t-tas2 and 1t-tase2 (2023).

[38] P. M. Dee, K. Nakatsukasa, Y. Wang, and S. Johnston, Temperature-filling phase diagram of the two-dimensional holstein model in the thermodynamic limit by self-consistent migdal approximation, Phys. Rev. B 99, 024514 (2019).

[39] J. Otsuki, M. Ohzeki, H. Shinaoka, and K. Yoshimi, Sparse modeling in quantum many-body problems, Journal of the Physical Society of Japan 89, 012001 (2020), https://doi.org/10.7566/JPSJ.89.012001.

[40] H. Shinaoka, N. Chikano, E. Gull, J. Li, T. Nomoto, J. Otsuki, M. Wallerberger, T. Wang, and K. Yoshimi, Efficient ab initio many-body calculations based on sparse modeling of Matsubara Green's function, SciPost Phys. Lect. Notes, 63 (2022).

[41] H. Shinaoka, J. Otsuki, M. Ohzeki, and K. Yoshimi, Compressing green’s function using intermediate representation between imaginary-time and real-frequency domains, Phys. Rev. B 96, 035147 (2017).

[42] J. Li, M. Wallerberger, N. Chikano, C.-N. Yeh, E. Gull, and H. Shinaoka, Sparse sampling approach to efficient ab initio calculations at finite temperature, Phys. Rev. B 101, 035144 (2020).

[43] K. Nogaki and H. Shinaoka, Bosonic nevanlinna analytic continuation, Journal of the Physical Society of Japan 92, 035001 (2023), https://doi.org/10.7566/JPSJ.92.035001.

[44] K. Nogaki, J. Fei, E. Gull, and H. Shinaoka, Nevanlinna.jl: A Julia implementation of Nevanlinna analytic continuation, SciPost Phys. Codebases, 19 (2023).

[45] J. Fei, C.-N. Yeh, and E. Gull, Nevanlinna analytical continuation, Phys. Rev. Lett. 126, 056402 (2021).

[46] W.-Y. He and P. A. Lee, Electronic density of states of a  \( u(1) \)  quantum spin liquid with spinon fermi surface. i. orbital magnetic field effects, Phys. Rev. B 107, 195155 (2023).

[47] M. S. Scheurer and S. Sachdev, Orbital currents in insulating and doped antiferromagnets, Phys. Rev. B 98, 235126 (2018).

[48] Y. Werman, S. Chatterjee, S. C. Morampudi, and E. Berg, Signatures of fractionalization in spin liquids from interlayer thermal transport, Phys. Rev. X 8, 031064 (2018).

[49] M. Fabrizio, Spin-liquid insulators can be landau's fermi liquids, Phys. Rev. Lett. 130, 156702 (2023).

[50] Z. Khatibi, R. Ahemeh, and M. Kargarian, Excitonic insulator phase and condensate dynamics in a topological one-dimensional model, Phys. Rev. B 102, 245121 (2020).

[51] O. Gunnarsson, M. W. Haverkort, and G. Sangiovanni, Analytical continuation of imaginary axis data for optical conductivity, Phys. Rev. B 82, 165125 (2010).

[52] H. Mei, H. Yuan, H. Wen, H. Yao, S. Sun, X. Zheng, F. Liu, H. Li, and W. Xu, Optical conductivity of an electron gas driven by a pulsed terahertz radiation field, The European Physical Journal B 95, 111 (2022).

[53] L. Huang, Aclfow: An open source toolkit for analytic continuation of quantum monte carlo data, Computer Physics Commun
 

nications 292, 108863 (2023).

[54] C. P. Nave and P. A. Lee, Transport properties of a spinon fermi surface coupled to a  \( u(1) \)  gauge field, Phys. Rev. B 76, 235124 (2007).

[55] T. Li, Absence of a  \( T^{2/3} \)  specific heat anomaly in a  \( u(1) \)  spin liquid with a large spinon fermi surface, Phys. Rev. B 104, 165123 (2021).

[56] A. Ribak, I. Silber, C. Baines, K. Chashka, Z. Salman, Y. Dagan, and A. Kanigel, Gapless excitations in the ground state of  \( 1t-tas_{2} \) , Phys. Rev. B 96, 195131 (2017).

[57] H. Murayama, Y. Sato, T. Taniguchi, R. Kurihara, X. Z. Xing, W. Huang, S. Kasahara, Y. Kasahara, I. Kimchi, M. Yoshida, Y. Iwasa, Y. Mizukami, T. Shibauchi, M. Konczykowski, and

Y. Matsuda, Effect of quenched disorder on the quantum spin liquid state of the triangular-lattice antiferromagnet 1t - tas \( _{2} \) , Phys. Rev. Res. 2, 013099 (2020).

[58] Webplotdigitizer : Version 4.7 (2024).

[59] W. R. Inc., Mathematica, Version 14.2, champaign, IL, 2024.

[60] P. A. Lee and N. Nagaosa, Gauge theory of the normal state of high- \( t_{c} \)  superconductors, Phys. Rev. B 46, 5621 (1992).

[61] N. Nagaosa and P. A. Lee, Normal-state properties of the uniform resonating-valence-bond state, Phys. Rev. Lett. 64, 2450 (1990).

[62] I. Montvay and G. Münster, Quantum Fields on a Lattice, Cambridge Monographs on Mathematical Physics (Cambridge University Press, 1994).
 
