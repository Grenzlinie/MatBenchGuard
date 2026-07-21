
# Coupled dynamics of fast spins and slow exchange interactions in the XY spin-glass

G Jongen  \( \dagger \) , J Anemüller  \( \ddagger \) , D Bollé  \( \dagger \) , A C C Coolen  \( \ddagger \)  and C Pérez-Vicente  \( \S \) 

† Instituut voor Theoretische Fysica, K.U. Leuven, B-3001 Leuven, Belgium

 \( ^{\dagger} \)  Department of Mathematics, King's College London, The Strand, London WC2R 2LS, UK

§Departament de Fisica Fonamental, Facultat de Fisica, Universitat de Barcelona, 08028 Barcelona, Spain

E-mail: greet.jongen@khleuven.be, joern@anemueller.de, desire.bolle@fys.kuleuven.ac.be, tcoolen@mth.kcl.ac.uk, conrad@ffn.ub.es

Abstract. We investigate an XY spin-glass model in which both spins and interactions (or couplings) evolve in time, but with widely separated time-scales. For large times this model can be solved using replica theory, requiring two levels of replicas, one level for the spins and one for the couplings. We define the relevant order parameters, and derive a phase diagram in the replica-symmetric approximation, which exhibits two distinct spin-glass phases. The first phase is characterized by freezing of the spins only, whereas in the second phase both spins and couplings are frozen. A detailed stability analysis leads also to two distinct corresponding de Almeida-Thouless lines, each marking continuous replica-symmetry breaking. Numerical simulations support our theoretical study.

PACS numbers: 75.10.Nr, 05.20.-v, 64.60.Cn

## 1. Introduction

The study of coupled dynamics of fast Ising spins and slow couplings has received considerable interest recently (see e.g.  \( [1]-[5] \)  and references therein), stimulated by considerations of simultaneous learning and retrieval in recurrent neural networks and the influence of slow atomic diffusion processes in disordered magnetic systems.

Generalizing spin systems by taking their interactions to be (slowly) time dependent was first considered in  \( [6] \) , as a mechanism with which to restore broken ergodicity at low temperature in the SK model  \( [7] \) . Another conceptually similar process, but now describing slow and deterministic synaptic modification in neural systems, driven by averages over neuron states, was first introduced in  \( [8] \) . Explicit stochastic dynamical laws for the interactions were defined in  \( [1, 3, 9] \) , where spin-glass models with coupled dynamics were studied within replica mean-field theory. It turned out that the replica
 

dimension in such models has a direct physical interpretation as the ratio of two temperatures characterizing the stochasticity in the spin dynamics and the coupling dynamics, respectively. Later it was shown that the case of negative replica dimension represents an over-frustrated system  \( [2] \) . In a similar spirit, neural network models with a coupled dynamics of fast neurons and slow neuronal connections were treated in  \( [10] \) – \( [14] \) .

In this paper the results previously obtained by others for Ising spin models are further extended to a classical XY spin glass with dynamic couplings, whose continuous spin variables are physically more realistic than Ising ones. Moreover, the XY model is closely related to models of coupled oscillators  \( [15] \) , of which the neural network version  \( [16] \)  provides a phenomenological description of neuronal firing synchronization in brain tissue. In particular, we examine the effects of including an explicit frozen randomness into the dynamics of the interaction weights.

The model is solved using the replica formalism. Relevant order parameters are defined and a phase diagram is obtained upon making the replica-symmetric Ansatz. Similarly to the Ising case, we find two different spin glass phases in addition to a paramagnetic phase. One spin-glass phase exhibits freezing of the spins in random directions, but on the time-scale of the coupling dynamics these 'frozen directions' still continue to change. A second spin-glass phase exhibits freezing of the spins as well as of the couplings, such that even on the large time-scales the 'frozen directions' of the spins remain stationary. We perform a detailed stability analysis and calculate the de Almeida-Thouless (AT) lines  \( [17] \)  (of which here there are two types), where continuous transitions occur to phases of broken replica symmetry. A brief preliminary account of the first part of the present work has been presented in  \( [18] \) . Finally, we discuss and tackle the problem of simulating this model numerically.

The remainder of this paper is organized as follows. In section 2 the classical XY spin glass model with coupled dynamics is defined. In section 3 the order parameters are calculated in the replica symmetric (RS) Ansatz and a phase diagram is presented. As is well known, the solutions of this Ansatz are not always stable against replica symmetry breaking (RSB). Therefore, the lines of instability are calculated in section 4. Finally, section 5 presents the results of the numerical simultions of this model, followed by a concluding discussion in section 6. The appendix describes all eigenvectors and eigenvalues of the Hessian matrix determining the stability of the replica symmetric solutions.

## 2. The model

We consider a system of N classical two-component spin variables  \( \pmb{S}_{i} = (\cos\theta_{i}, \sin\theta_{i}) \) ,  \( i = 1 \ldots N \) , with symmetric couplings (or exchange interactions)  \( J_{ij} \) , taken to be of infinite range. In contrast to the standard XY spin glass, these couplings are not static but are allowed to evolve in time, albeit slowly. The spins are taken to have a stochastic Glauber-type dynamics such that for stationary choices of the couplings the microscopic
 

spin probability density would evolve towards a Boltzmann distribution

 \[ P(\{\boldsymbol{S}_{i}\},\{J_{i j}\})\sim\exp[-\beta H(\{\boldsymbol{S}_{i}\},\{J_{i j}\})] \quad (1) \] 

with the standard Hamiltonian

 \[ H(\{\boldsymbol{S}_{i}\},\{J_{i j}\})=-\sum_{k<\ell}J_{k\ell}\boldsymbol{S}_{k}\cdot\boldsymbol{S}_{\ell} \quad (2) \] 

and with inverse temperature  \( \beta = T^{-1} \) , where  \( k, l \in \{1, \ldots, N\} \) , and where, at least for the purpose of the dynamics of the spins, the  \( \{J_{ij}\} \)  are to be considered as quenched variables.

We remark that this system is equivalent to a system of N coupled oscillators with phases  \( \theta_{i} \)  [15], whose time evolution is described by a Langevin equation

 \[ \frac{d}{d t}\theta_{i}=\sum_{j}J_{i j}\sin(\theta_{j}-\theta_{i})+\sqrt{\frac{2\pi}{\beta}}\xi_{i}(t), \quad (3) \] 

where the  \( \xi_{i}(t) \)  are defined as independent white noise variables, drawn from a Gaussian probability distribution with

 \[ \langle\xi_{i}(t)\rangle=0\qquad\langle\xi_{i}(t){\xi_{j}}(t^{\prime})\rangle=\delta_{i j}\delta(t-t^{\prime}). \quad (4) \] 

In our model, the couplings also evolve in a stochastic manner, partially in response to the states of the spins and to externally imposed biases. However, we assume that the spin dynamics is very fast compared to that of the couplings, such that on the time-scales of the couplings the spins are effectively in equilibrium (i.e. we take the adiabatic limit). For the dynamics of the couplings the following Langevin form is proposed :

 \[ \frac{d}{d t}J_{i j}=\frac{\langle\boldsymbol{S}_{i}\cdot\boldsymbol{S}_{j}\rangle+K_{i j}}{N}-\mu J_{i j}+\frac{\eta_{i j}(t)}{N^{1/2}}\qquad i<j=1\ldots N. \quad (5) \] 

The term  \( \langleS_{i}\cdotS_{j}\rangle \) , representing local spin correlations associated with the coupling  \( J_{ij} \) , is a thermodynamic average over the Boltzmann distribution (1) of the spins, given the instantaneous couplings  \( \{J_{k\ell}\} \) . No other spins are involved, in order to retain the local character of the couplings. We remark that only the thermal averages (or long time averages) of the spin correlations play a role, rather than the instantaneous correlations, since the dynamics of the couplings is (by definition) sufficiently slow. External biases  \( K_{ij}=\mu NB_{ij} \)  serve to steer the weights to some preferred values. The  \( B_{ij} \)  are chosen to be quenched random variables, drawn independently from a Gaussian probability distribution with mean  \( B_{0}/N \)  and variance  \( \tilde{B}/N \) :

 \[ p(B_{i j})=\frac{1}{\sqrt{2\pi\tilde{B}/N}}\mathrm{e x p}\left[-\frac{(B_{i j}-B_{0}/N)^{2}}{2\tilde{B}/N}\right] \quad (6) \] 

and are thus reminiscent of the couplings in the original SK model [7]. Here, in contrast, the  \( \{B_{ij}\} \)  generate frozen disorder in the dynamics of the couplings. The decay term  \( \mu J_{ij} \)  in (5) is added in order to limit the magnitude of the couplings. Finally, the terms  \( \eta_{ij}(t) \)  represent Gaussian white noise contributions, of zero mean and covariance  \( \langle\eta_{ij}(t)\eta_{kl}(t')\rangle=2\tilde{T}\delta_{ik}\delta_{jl}\delta(t-t') \) , with associated temperature  \( \tilde{T}=\tilde{\beta}^{-1} \) .
 

Appropriate factors of N are introduced in order to ensure non-trivial behaviour in the thermodynamic limit  \( N \rightarrow \infty \) .

The model exhibits three independent global symmetries, which can be expressed efficiently in terms of the Pauli spin matrices  \( \sigma_{x} \)  and  \( \sigma_{z} \) :

 \[ \begin{array}{ll}\text{inversion of both spin axes:}&\boldsymbol{S}_{i}\rightarrow-\boldsymbol{S}_{i}\quad\text{for all}i\\\text{inversion of one spin axis:}&\boldsymbol{S}_{i}\rightarrow\sigma_{z}\boldsymbol{S}_{i}\quad\text{for all}i\\\text{permutation of spin axes:}&\boldsymbol{S}_{i}\rightarrow\sigma_{x}\boldsymbol{S}_{i}\quad\text{for all}i.\end{array} \quad (7) \] 

Upon using algebraic relations such as  \( \sigma_{x}\sigma_{z}\sigma_{x}=-\sigma_{z} \)  and  \( \sigma_{z}\sigma_{x}\sigma_{z}=-\sigma_{x} \)  we see that in the high T (ergodic) regime these three global symmetries generate the following local identities, respectively:

 \[ \langle\boldsymbol{S}_{i}\rangle=\mathbf{0},\qquad\langle\boldsymbol{S}_{i}\cdot\sigma_{x}\boldsymbol{S}_{j}\rangle=0,\qquad\langle\boldsymbol{S}_{i}\cdot\sigma_{z}\boldsymbol{S}_{j}\rangle=0. \quad (8) \] 

We note that the stochastic equation (5) for the couplings is conservative, i.e. it can be written as

 \[ \frac{d}{d t}J_{i j}=-\frac{1}{N}\frac{\partial}{\partial J_{i j}}\tilde{H}(\{J_{i j}\})+\frac{\eta_{i j}(t)}{N^{1/2}} \quad (9) \] 

with the following effective Hamiltionian for the couplings:

 \[ \tilde{H}(\{J_{i j}\})=-\frac{1}{\beta}\log\mathcal{Z}_{\beta}(\{J_{i j}\})+\frac{1}{2}\mu N\sum_{k<\ell}J_{k\ell}^{2}-\mu N\sum_{k<\ell}B_{k\ell}J_{k\ell}. \quad (10) \] 

The term  \( \mathcal{Z}_{\beta}(\{J_{ij}\})=\operatorname{Tr}_{\{\boldsymbol{S}_{i}\}}\exp[\beta\sum_{k<\ell}J_{k\ell}\boldsymbol{S}_{k}\cdot\boldsymbol{S}_{\ell}] \)  in this expression is the partition function of the XY spins with instantaneous couplings  \( \{J_{ij}\} \) . It follows from (9) that the stationary probability density for the couplings is also of a Boltzmann form, with the Hamiltonian (10), and that the thermodynamics of the slow system (the couplings) are generated by the partition function  \( \tilde{\mathcal{Z}}_{\tilde{\beta}}=\int\prod_{k<\ell}dJ_{k\ell}\exp[-\tilde{\beta}\tilde{H}(\{J_{ij}\})] \) , leading to (modulo irrelevant prefactors):

 \[ \tilde{\mathcal{Z}}_{\tilde{\beta}}=\int\prod_{k<\ell}d J_{k\ell}\left[\mathcal{Z}_{\beta}(\{J_{i j}\})\right]^{n}\exp\left[\mu\tilde{\beta}N\sum_{k<\ell}B_{k\ell}J_{k\ell}-\frac{1}{2}\mu\tilde{\beta}N\sum_{k<\ell}J_{k\ell}^{2}\right]. \quad (11) \] 

In contrast to the more conventional spin systems with frozen disorder, where the replica dimension n is a dummy variable, here we find that n is given by the ratio  \( n = \tilde{\beta} / \beta \) , and can take any real non-negative value. The limit  \( n \to 0 \)  corresponds to a situation in which the coupling dynamics is driven purely by the Gaussian white noise, rather than by the spin correlations. Therefore, in this limit the model is equivalent to the XY model with stationary couplings formulated, as in [19]. For n = 1 the two characteristic temperatures are the same, and the theory reduces to that corresponding to the exchange interactions being annealed variables. In the limit  \( n \to \infty \)  the influence of spin correlations on the coupling dynamics dominates, and the couplings  \( J_{ij} \)  only fluctuate modestly (if at all) around their mean values  \( (\langle \mathbf{S}_{i} \cdot \mathbf{S}_{j} \rangle + K_{ij}) / \mu N \) .
 

## 3. Statics

We define the disorder-averaged free energy per site

 \[ \tilde{f}=-\frac{1}{\tilde{\beta}N}\langle\log\tilde{\mathcal{Z}}_{\tilde{\beta}}\rangle_{B}, \quad (12) \] 

in which  \( \langle\cdot\rangle_{B} \)  denotes an average over the  \( \{B_{ij}\} \) . We carry out this average using the identity  \( \log\tilde{\mathcal{Z}}_{\tilde{\beta}}=\lim_{r\to0}r^{-1}[\tilde{\mathcal{Z}}_{\tilde{\beta}}^{-1}] \) , evaluating the latter by analytic continuation from integer r. Our system, characterized by the partition function  \( \tilde{Z}_{\tilde{\beta}} \) , is thus replicated r times; we label each replica by a Roman index. Each of the r functions  \( \tilde{Z}_{\tilde{\beta}} \) , in turn, is given by (11), and involves  \( \mathcal{Z}_{\beta}(\{J_{ij}\})^{n} \)  which is replaced by the product of n further replicas, labeled by Greek indices. For non-integer n, again analytic continuation is made from integer n. Therefore, performing the disorder average in  \( \tilde{f} \)  boils down to performing the disorder average of  \( [\tilde{\mathcal{Z}}_{\tilde{\beta}}]^{r} \) , involving nr coupled replicas of the original system:  \( \{S_{i}\}\to\{S_{ia}^{\alpha}\} \) , with  \( \alpha=1\ldots n \)  and  \( a=1\ldots r \) . We obtain

 \[ \begin{align*}\langle[\tilde{\mathcal{Z}}_{\tilde{\beta}}]^{r}\rangle_{B}&=\int\prod_{i<j}\{dB_{ij}p(B_{ij})\}\int\prod_{i<j}\left\{\prod_{a}dJ_{ij}^{a}\left[\frac{N}{2\pi\tilde{J}}\right]^{1/2}\right\}\\&\times\mathrm{Tr}_{\{\boldsymbol{S}_{ia}^{\alpha}\}}\exp\left[-\frac{N}{2\tilde{J}}\sum_{i<j}\sum_{a}(J_{ij}^{a})^{2}+\frac{N}{\tilde{J}}\sum_{i<j}\sum_{a}B_{ij}J_{ij}^{a}+\beta\sum_{i<j}\sum_{a}\sum_{\alpha}B_{ij}\boldsymbol{S}_{ia}^{\alpha}\cdot\boldsymbol{S}_{jb}^{\beta}\right]\end{align*} \quad (13) \] 

where  \( \tilde{J}=1/\mu\tilde{\beta} \) , and with the Gaussian probability distribution of the external biases  \( B_{ij} \)  as given by eq. (6). The Roman indices  \( (a,b,\ldots) \)  run from 1 to r; the Greek ones  \( (\alpha,\beta,\ldots) \)  from 1 to n. Expression (13) can be evaluated using the standard techniques of replica mean-field theory [20]. Because of the complexity of the replica structure we indicate the most important steps. We first perform the integrals over the couplings and the biases, giving

 \[ \begin{align*}\langle[\tilde{\mathcal{Z}}_{\tilde{\beta}}]^{r}\rangle_{B}&=\mathrm{Tr}_{\{\boldsymbol{S}_{ia}^{\alpha}\}}\exp\left[\beta\frac{B_{0}}{N}\sum_{i<j}\sum_{a}\sum_{\alpha}\boldsymbol{S}_{ia}^{\alpha}\cdot\boldsymbol{S}_{ja}^{\alpha}+\beta^{2}\frac{\tilde{B}}{N}\sum_{i<j}\left(\sum_{a}\sum_{\alpha}\boldsymbol{S}_{ia}^{\alpha}\cdot\boldsymbol{S}_{ja}^{\alpha}\right)^{2}\right.\\&\left.+\frac{1}{2N}\beta^{2}\tilde{J}\sum_{i<j}\sum_{a}\left(\sum_{\alpha}\boldsymbol{S}_{ia}^{\alpha}\cdot\boldsymbol{S}_{ja}^{\alpha}\right)^{2}\right]\end{align*} \quad (14) \] 

and decouple the i- and j-components using

 \[ \boldsymbol{S}_{i a}^{\alpha}\cdot\boldsymbol{S}_{j a}^{\alpha}\quad\boldsymbol{S}_{i b}^{\beta}\cdot\boldsymbol{S}_{j b}^{\beta}=\frac{1}{2}\left(\left(\boldsymbol{S}_{a b}^{\alpha\beta}\right)_{i}\cdot\left(\boldsymbol{S}_{a b}^{\alpha\beta}\right)_{j}+\left(\boldsymbol{T}_{a b}^{\alpha\dot{\beta}}\right)_{i}\cdot\left(\boldsymbol{T}_{a b}^{\alpha\dot{\beta}}\right)_{j}\right). \quad (15) \] 

Here the quantity  \( (\boldsymbol{S}_{ab}^{\alpha\beta})_{i} \)  is defined as a two-dimensional unit vector with reference angle equal to the difference of the reference angles of  \( S_{ia}^{\alpha} \)  and  \( S_{ib}^{\beta} \) , whereas  \( (\boldsymbol{T}_{ab}^{\alpha\beta})_{i} \)  is defined as a two-dimensional unit vector with reference angle equal to the sum of both these angles. Upon applying the saddle-point method in the thermodynamic limit  \( N \to \infty \)  we then arrive at

 \[ \left\langle\left[\tilde{\mathcal{Z}}_{\tilde{\beta}}\right]^{r}\right\rangle_{B}=\exp\left[N\exp F(\{\boldsymbol{m}_{a}^{\alpha}\},\{\boldsymbol{s}_{a}^{\alpha\beta}\},\{\boldsymbol{s}{}_{ab}^{\alpha\beta}\},\left\{\boldsymbol{t}_{a}^{\alpha\beta}\right\},\left\{\boldsymbol{t}{}_{ab}^{\alpha\beta}\right\}\right] \quad (16) \] 

 \[ F(\{\boldsymbol{m}_{a}^{\alpha}\},\{\boldsymbol{s}_{a}^{\alpha\beta}\},\{\boldsymbol{s}{}_{ab}^{\alpha\beta}\},\left\{\boldsymbol{t}_{a}^{\alpha\beta}\right\},\left\{\boldsymbol{t}{}_{ab}^{\alpha\beta}\right\})=-\frac{1}{8}\tilde{B}\beta^{2}\sum_{a\neq b}\sum_{\alpha\beta}\left((\boldsymbol{s}_{ab}^{\alpha\beta})^{2}+(\boldsymbol{t}_{ab}^{\alpha\beta}){}^{2}\right) \]
 

 \[ \begin{aligned}&-\frac{1}{8}\beta^{2}(\tilde{B}+\tilde{J})\sum_{a}\sum_{\alpha\neq\beta}\left((\boldsymbol{s}_{a}^{\alpha\beta})^{2}+(\boldsymbol{t}_{a}^{\alpha\beta})^{\prime2}\right)\\&-\frac{1}{2}\beta B_{0}\sum_{a}\sum_{\alpha}(\boldsymbol{s}_{a}^{\alpha})^{2}-\frac{1}{2}\beta^{2}\tilde{J}\sum_{a}\sum_{\alpha}(\boldsymbol{t}_{a}^{\alpha})^{2}\\&+\log G(\{\boldsymbol{m}_{a}^{\alpha}\},\{\boldsymbol{s}_{a}^{\alpha\beta}\},\{\boldsymbol{s}^{\alpha\beta}_{ab}\},\{\boldsymbol{t}_{a}^{\alpha\beta}\},\{\boldsymbol{t}^{\alpha\beta}_{ab}\})\\G(\{\boldsymbol{m}_{a}^{\alpha}\},\{\boldsymbol{s}_{a}^{\alpha\beta}\},\{\boldsymbol{s}^{\alpha\beta}_{ab}\},\{\boldsymbol{t}_{a}^{\alpha\beta}\})=\mathrm{Tr}_{\{\boldsymbol{S}_{a}^{\alpha}\}}\exp\left[\beta B_{0}\sum_{a}\sum_{\alpha}\boldsymbol{m}_{a}^{\alpha}\cdot\boldsymbol{S}_{a}^{\alpha}\right.\\&\left.+\frac{1}{4}\tilde{B}\beta^{2}\sum_{a\neq b}\sum_{\alpha,\beta}\left(\boldsymbol{s}_{ab}^{\alpha\beta}\cdot\boldsymbol{S}_{ab}^{\alpha\beta}+\boldsymbol{t}_{ab}^{\alpha\beta}\cdot\boldsymbol{T}_{ab}^{\alpha\beta} \right)\right.\\&\left.+\frac{1}{4}(\tilde{B}+\tilde{J})\beta^{2}\sum_{a}\sum_{\alpha}\left(\boldsymbol{s}_{a}^{\alpha\beta}\cdot\boldsymbol{S}_{a}^{\alpha\beta}+\boldsymbol{t}_{a}^{\alpha\beta}\cdot\boldsymbol{T}_{a}^{\alpha\beta} \right)\right.\\&\left.+\frac{1}{4}\beta^{2}\tilde{J}\sum_{a}\sum_{\alpha}\boldsymbol{t}_{a}^{\alpha}\cdot\boldsymbol{T}_{a}^{\alpha}\right].\end{aligned} \quad (17) \quad (18) \] 

The parameters  \( \{m_{a}^{\alpha}\} \) ,  \( \{s_{a}^{\alpha\beta}\} \) ,  $ \{s_{ab}^{\alpha\beta}\} \( ,  \) \{t_{a}^{\alpha\beta}\} $  and  \( \{t_{ab}^{\alpha\beta}\} \)  introduced by this procedure are vectors, hence the extremum is taken over both components. They carry Greek and Roman replica labels.

Those parameters which have only one Greek and Roman replica label  \( (\boldsymbol{m}_{a}^{\alpha}, \boldsymbol{t}_{a}^{\alpha}) \) , can be interpreted as

 \[ \boldsymbol{m}_{a}^{\alpha}=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{i}\left\langle\sqrt{\boldsymbol{S}_{i a}^{\alpha}}\right\rangle_{B}\qquad\boldsymbol{t}_{a}^{\alpha}=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{i}\left\langle\sqrt{\boldsymbol{T}_{i a}^{\alpha}}\right\rangle_{B}. \quad (19) \] 

The horizontal bar denotes thermal averaging over the coupling dynamics with fixed biases  \( \{B_{ij}\} \) . Those parameters which involve pairs of replicas either connect two distinct Greek replicas with a single Roman replica,  \( (\boldsymbol{s}_{a}^{\alpha\beta}, \boldsymbol{t}_{a}^{\alpha\beta}) \) , or with two distinct Roman replicas,  \( (\boldsymbol{s}_{ab}^{\alpha\beta}, \boldsymbol{t}_{ab}^{\alpha\beta}) \) . The latter vector variables can, equivalently, be expressed in terms of the following scalar order parameters, which measure the correlations between the various replicas:

 \[ \begin{aligned}&q_{ab}^{\alpha\beta}=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{i}\left\langle\left\langle\boldsymbol{S}_{ia}^{\alpha}\cdot\boldsymbol{S}_{ib}^{\beta}\right\rangle\right\rangle_{B}\\&u_{ab}^{\alpha\beta}=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{i}\left\langle\left\langle\boldsymbol{S}_{ia}^{\alpha}\cdot\sigma_{x}\boldsymbol{S}_{ib}^{\beta}\right\rangle\right\rangle_{B}\\&v_{ab}^{\alpha\beta}=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{i}\left\langle\left\langle\boldsymbol{S}_{ia}^{\alpha}\cdot\sigma_{z}\boldsymbol{S}_{ib}^{\beta}\right\rangle\right\rangle_{B}.\\ \end{aligned} \quad (20) \] 

At this point we remark that the order parameters  \( u_{ab}^{\alpha\beta} \)  and  \( v_{ab}^{\alpha\beta}\alpha \)  are typical for the XY-model [19], and do not appear in the SK-model; comparison with (8) shows that, together with  \( m_{a}^{\alpha} \)  and  \( t_{a}^{\alpha} \( , they measure the breaking of the global symmetries (7). For simplicity we will henceforth choose  \( B_{0}=0 \) . We will make the usual assumption that, in the absence of global symmetry-breaking forces, phase transitions can lead to at most local violation of the identities (8). Thus the latter will remain valid if averaged over all sites, at any temperature, which implies that  \( m_{a}^{\alpha}=t_{a}^{\alpha}=0 \)  and that  \( u_{ab}^{\alpha\beta}=v_{ab}^{\alpha\beta}\equiv0 \) . The spin-glass order parameters  \( q_{ab}^{\alpha\beta} \) , on the other hand, are not related to simple global
 

symmetries, but measure the overlap of two vector spins, and serve to characterize the various phases.

At this stage in the calculation we make the replica symmetry (RS) Ansatz. Since observables with identical Roman indices refer to system copies with identical couplings, whereas observables with identical Roman indexes and identical Greek indices refer to system copies with identical couplings and identical spins, in the present problem the RS ansatz for the spin-glass order parameters takes the form  \( q_{ab}^{\alpha\beta} = \delta_{ab} \left\{ \delta_{\alpha\beta} + q_{1} [1 - \delta_{\alpha\beta}] \right\} + q_{0} [1 - \delta_{ab}] \) . Here we remark that  \( S_{a}^{\alpha} \cdot S_{a}^{\alpha'} = 1 \)  and that, in the absence of global symmetry breaking forces,  \( s_{ab}^{\alpha\beta} \)  becomes a vector of length  \( q_{ab}^{\alpha\beta} \)  and reference angle 0.

The asymptotic disorder-averaged free energy per site can now be written as

 \[ \begin{align*}\tilde{f}=\frac{1}{8}\tilde{B}\beta^{2}n^{2}q_{0}^{2}-\frac{1}{8}(\tilde{B}+\tilde{J})\beta^{2}n(n-1)q_{1}^{2}-\frac{1}{4}(\tilde{B}+\tilde{J})\beta^{2}n q_{1}\\+\int\mathcal{D}\boldsymbol{p}\log\left\{\int\mathcal{D}\boldsymbol{q}\left[\mathrm{Tr}\boldsymbol{S}\exp\left[\beta\sqrt{\frac{1}{2}\tilde{B}q_{0}}\boldsymbol{p}\cdot\boldsymbol{S}+\beta\Xi\boldsymbol{q}\cdot\boldsymbol{S}\right]\right]^{n}\right\},\end{align*} \quad (21) \] 

with the short-hand  \( \Xi=\beta\sqrt{\frac{1}{2}(\tilde{J}+\tilde{B})q_{1}-\frac{1}{2}\tilde{B}q_{0}} \) , and where we have introduced the two-dimensional Gaussian measure

 \[ \mathcal{D}\boldsymbol{p}=(2\pi)^{-1}d p_{x}d p_{y}\exp\left[-\frac{1}{2}(p_{x}^{2}+p_{y}^{2})\right]. \quad (22) \] 

The remaining two order parameters  \( q_{0} \)  and  \( q_{1} \)  are determined as the solutions of the following coupled saddle-point equations

 \[ q_{0}=\int d x\;P(x)\left\{\frac{\int d z\;P(z)\left[I_{0}(z\Xi)\right]^{n-1}I_{1}(z\Xi)\;I_{1}(z x\beta\Xi^{-1}\sqrt{\frac{1}{2}\tilde{B}q_{0}})}{\int d z\;P(z)\left[I_{0}(z\Xi)\right]^{n}I_{0}(z x\beta\Xi^{-1}\sqrt{\frac{1}{2}\tilde{B}q_{0}})}\right\}^{2} \quad (23) \] 

 \[ q_{1}=\int d x\;P(x)\left\{\frac{\int d z\;P(z)\left[I_{0}(z\Xi)\right]^{n-2}\left[I_{1}(z\Xi)\right]^{2}I_{0}(z x\beta\Xi^{-1}\sqrt{\frac{1}{2}\tilde{B}q_{0}})}{\int d z\;P(z)\left[I_{0}(z\Xi)\right]^{n}I_{0}(z x\beta\Xi^{-1}\sqrt{\frac{1}{2}\tilde{B}q_{0}})}\right\} \quad (24) \] 

with  \( P(x)=xe^{-\frac{1}{2}x^{2}}\theta[x] \) , and where the functions  \( I_{n}(x) \)  are the Modified Bessel functions of integer order [21].

One can give a simple physical interpretation of these order parameters in terms of the appropriate averages over the various dynamics

 \[ \begin{aligned}&q_{0}=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{i}\left\langle\sqrt{\boldsymbol{S}_{i}}\right\rangle^{2}\Big)_{B}\\&q_{1}=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{i}\left\langle\sqrt{\boldsymbol{S}_{i}}\right\rangle^{2}\Big)_{B}.\\ \end{aligned} \quad (25) \] 

It is clear that  \( 0 \leq q_{0} \leq q_{1} \leq 1 \) .

We have studied the fixed-point equations (23,24), after having first eliminated the parameter redundancy by putting  \( \tilde{B}=1 \)  and  \( \tilde{J}=3 \) . The resulting phase diagram in the n-T plane is shown in Fig. 1. The appearance of two different spin-glass order parameters suggests that two different spin-glass phases are to be expected. Indeed, in
 
![](./images/867747320999968980_1.jpg)

Figure 1. Phase diagram of the XY spin glass with slow dynamic couplings, drawn in the n-T plane with  \( B_{0}=0 \) ,  \( \tilde{B}=1 \)  and  \( \tilde{J}=3 \) . P: paramagnetic phase,  \( q_{1}=q_{0}=0 \) ; SG1: first spin-glass phase,  \( q_{1}>0 \)  and  \( q_{0}=0 \)  (freezing on spin time-scales only); SG2: second spin-glass phase,  \( q_{1}>0 \)  and  \( q_{0}>0 \)  (freezing on all time-scales); AT lines:  \( \lambda_{R}=0 \)  (Roman replicon),  \( \lambda_{G}=0 \)  (Greek replicon).

addition to a paramagnetic phase (P), where  \( q_{0}=q_{1}=0 \) , we find two distinct spin-glass phases: SG1, where  \( q_{1}>0 \)  but  \( q_{0}=0 \) , and SG2, where both  \( q_{1}>0 \)  and  \( q_{0}>0 \) . The SG1 phase describes freezing of the spins on the fast time-scales only (where spin equilibration occurs); on the large time-scales, where coupling equilibration occurs, we find that, due to the slow motion of the couplings, the frozen spin directions continually change. In the SG2 phase, on the other hand, both spins and couplings freeze, with the net result that even on the large time-scales the frozen spin directions are 'pinned'. The SG1-SG2 transition is always second order and occurs for  \( T=(n-1)q_{1}+1/2 \) . The transition SG1-P is second order for  \( n<2 \)  (in which case its location is given by  \( \tilde{B}+\tilde{J}=4T^{2} \) ), but first order for n>2. When n further increases to n>3.5, the SG1 phase disappears, and the system exhibits a first order transition directly from P to SG2. Fig. 2 shows for several values of n the values of the order parameters as a function of the temperature.

Qualitatively, the phase diagram of the present model is very similar to that of the Ising spin glass with dynamic couplings [3]. The main difference is the re-scaling by a factor two of the transition temperature from the first spin-glass phase to the paramagnetic phase, as has already been noticed in [19].

The existence of two types of spin-glass order parameters is directly related to the presence of quenched disorder in the couplings, which allows the latter to freeze in random directions at low coupling temperature  \( \tilde{T} \) . In a model with homogeneous external biases [1, 22], where no preferred direction of the couplings is assumed, one distinguishes (in contrast to the present situation) only the paramagnetic phase and the spin-glass phase SG1. Qualitatively, the transition line separating the paramagnetic
 
![](./images/867747320999968980_2.jpg)

![](./images/867747320999968980_3.jpg)

![](./images/867747320999968980_4.jpg)

Figure 2. Dependence of the order parameters  \( q_{0} \)  (broken curve) and  \( q_{1} \)  (full curve) on the temperature T for various temperature ratios n, all at  \( B_{0}=0 \) ,  \( \tilde{B}=1 \)  and  \( \tilde{J}=3 \) . For n=1.0 there is a continuous phase transition from P to SG1 at T=0.5 and from SG1 to SG2 at T=1. For n=2.5 the first transition occurs at T=0.98 while the parameter  \( q_{1} \)  drops discontinuous from 0.18 to 0 at T=1.03. Finally for n=10 both order parameters vanish at T=1.83 (limit value  \( q_{0}=0.13 \) ,  \( q_{1}=0.29 \) ) indicating a first order transition from P to SG2.

phase from the spin-glass phase in the case of absent coupling disorder is the same as that in Fig. 1, viz. a second order transition for  \( n \leq 2 \)  given by  \( \tilde{J} = 2T \)  and a first order transition for n > 2. The corresponding expressions for the order parameters can immediately be deduced from the results above: when the quenched disorder in the couplings is absent, the partition function itself is self-averaging and the replica method is simply no longer needed. Therefore all order parameters concerning different Roman indices are redundant and drop out automatically, such that one ends up with only one spin-glass order parameter. Its explicit value is obtained by putting  \( B_{0} = 0 \)  and  \( \tilde{B} = 0 \) in (24).

## 4. Stability of the replica-symmetric solutions

Additional transitions may occur in our model due to a continuous breaking of replica symmetry. Here we expect two distinct types of replica symmetry breaking, with respect to the two distinct replicas, viz. the Roman and the Greek ones. The stability of the RS solution is, as always, expressed in terms of the matrix of second derivatives of quadratic fluctuations at the saddle point  \( [17] \) . We calculate all eigenvalues and their multiplicity following the ideas in  \( [3, 17] \) . We remark that our results differ from, and improve upon those of  \( [3] \) . It turns out that the (restricted) set of eigenvectors and eigenvalues given in  \( [3] \)  satisfy only part of the relevant orthogonality conditions used in their calculations. In the following we present a summary of the results. More details can be found in Appendix A.

We start by rewriting (17), taking into account its invariance with respect to the
 

global symmetries and the absence of global symmetry breaking forces

 \[ \begin{aligned}F_{S}(\{q_{ab}^{\alpha\beta}\},\{q_{a}^{\alpha\beta}\})&=-\frac{1}{8}\tilde{B}\beta^{2}\sum_{a\neq b}\sum_{\alpha\beta}\left(q_{ab}^{\alpha\beta}\right)^{2}-\frac{1}{8}\left(\tilde{B}+\tilde{J}\right)\beta^{2}\sum_{a}\sum_{\alpha\neq\beta}\left(q_{a}^{\alpha\beta}\right)^{2}\\&+\log G_{S}(\{q_{ab}^{\alpha\beta}\},\{q_{a}^{\alpha\beta}\})\end{aligned} \quad (26) \] 

 \[ \begin{align*}G_{S}(\{q_{ab}^{\alpha\beta}\},\{q_{a}^{\alpha\beta}\})&=\mathrm{Tr}_{\{\boldsymbol{S}_{a}^{\alpha}\}}\exp\left[\frac{1}{4}\tilde{B}\beta^{2}\sum_{a\neq b}\sum_{\alpha\beta}q_{ab}^{\alpha\beta}\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{b}^{\beta}\right.\\&\left.+\frac{1}{4}\left(\tilde{B}+\tilde{J}\right)\beta^{2}\sum_{a}\sum_{\alpha\neq\beta}q_{a}^{\alpha\beta}\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{a}^{\beta}\right].\end{align*} \quad (27) \] 

We consider small fluctuations of the order parameters around their RS saddle-point values

 \[ q_{a}^{\alpha\beta}=q_{0}+\epsilon_{a}^{\alpha\beta}\quad(\alpha<\beta)\qquad\mathrm{a n d}\qquad q_{a b}^{\alpha\beta}=q_{1}+\eta_{a b}^{\alpha\underline{\beta}}\quad(a<b) \quad (28) \] 

and expand (27) up to second order in  \( \epsilon_{a}^{\alpha\beta} \)  and  \( \eta_{ab}^{\alpha\beta} \) . The first order terms vanish by construction. The coefficients of the second order terms form the so-called Hessian matrix and are denoted by

 \[ \mathcal{H}(a b\alpha\beta,c d\gamma\delta)=\frac{\partial^{2}F_{S}(\{q_{a b}^{\alpha\beta}\},\{q_{a}^{\alpha\beta}\})}{\partial q_{a b}^{\alpha\beta}\partial q_{c d}^{\delta}}\Bigg|_{q_{0},q_{1}}. \quad (29) \] 

The first argument of H (4 components  \( (ab\alpha\beta) \)  when  \( a \neq b \)  and 3 components  \( (a\alpha\beta) \)  when  \( a = b \)  but  \( \alpha \neq \beta \) ) denotes the index of the row of the matrix; the last one the column index. Because of the symmetry of the order parameters (20) we can always take a < b or  \( \alpha < \beta \)  when a = b. Therefore the square matrix H has dimension  \( \frac{1}{2}[rn(n-1) + r(r-1)n^{2}] \) . One can distinguish three groups of matrix elements: firstly, those related to RSB fluctuations around  \( q_{1} \)  only,

 \[ \begin{aligned}&A_{1}=\mathcal{H}(a\alpha\beta,a\alpha\beta)=-J+J^{2}\left\{\left\langle\left(\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{a}^{\beta}\right)^{2}\right\rangle\right\}-q_{0}^{2}\Bigg\}\\&A_{2}=\mathcal{H}(a\alpha\beta,a\alpha\delta)=\mathcal{H}(a\alpha\upbeta,a\gamma\upbeta)=J^{2}\left\{\left\langle\overline{\left\langle\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{a}^{\beta}\boldsymbol{S}_{a}^{\alpha},\boldsymbol{S}_{a}^{\delta}\right\rangle\right\rangle-q_{0}^{2}\right\}\\&A_{3}=\mathcal{H}(a\alpha\upbeta,a\gamma\delta)=J^{2}\left\{\left\langle\overline{\left\langle\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{a}^{\beta}\boldsymbol{S}_{a}^{\gamma},\boldsymbol{S}_{a}^{\delta}\right\rangle\right\rangle-q_{0}^{2}\right\}\\&A_{4}=\mathcal{H}(a\alpha\upbeta,c\gamma\delta)=J^{2}\left\{\left\langle\overline{\left\langle\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{a}^{\beta}\boldsymbol{S}_{c}^{\gamma},\boldsymbol{S}_{c}^{\delta}\right\rangle\right\rangle-q_{0}^{2}\right\};\\ \end{aligned} \quad (30) \] 

secondly, those related to fluctuations around  \( q_{0} \) ,

 \[ B_{1}=\mathcal{H}(a b\alpha\beta,a b\alpha\beta)=-B+B^{2}\left\{\left\langle\overline{{\left(\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{b}^{\beta}\right)}^{2}}\right\rangle-q_{1}^{2}\right\} \] 

 \[ B_{2}=\mathcal{H}(a b\alpha\beta,a b\alpha\delta)=\mathcal{H}(a b\upalpha\beta,a b\gamma\beta)=B^{2}\left\{\left\langle\overline{{\left\langle\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{b}^{\beta}\boldsymbol{S}_{a}^{\alpha},\boldsymbol{S}_{b}^{\delta}\right\rangle}}\right\rangle-q_{1}^{2}\right\} \] 

 \[ B_{3}=\mathcal{H}(a b\alpha\beta,a b\gamma\delta)=B^{2}\left\{\left\langle\overline{{\left\langle\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{b}^{\beta}\boldsymbol{S}_{a}^{\gamma}\cdot\boldsymbol{S}_{c}^{\delta}\right\rangle}}\right\rangle-q_{1}^{2}\right\} \] 

 \[ B_{4}=\mathcal{H}(a b\alpha\beta,a d\alpha\delta)=\mathcal{H}(a b\upalpha\beta,c b\gamma\beta)=B^{2}\left\{\left\langle\overline{{\left\langle\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{b}^{\beta}\boldsymbol{S}_{a}^{\alpha},\boldsymbol{S}_{a}^{\delta}\right\rangle}}\right\rangle-q_{1}^{2}\right\} \]
 

 \[ \begin{aligned}&B_{5}=\mathcal{H}(ab\alpha\beta,ad\gamma\delta)=\mathcal{H}(ab\alpha\dot{\beta},cb\gamma\delta)=B^{2}\left\{\left\langle\overline{\left\langle\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{b}^{\beta}\boldsymbol{S}_{a}^{\gamma}\cdot\boldsymbol{S}_{d}^{\delta}\right\rangle\right\rangle-q_{1}^{2}\right\}\\&B_{6}=\mathcal{H}(ab\alpha\beta,cd\gamma\delta)=B^{2}\left\{\left\langle\overline{\left\langle\boldsymbol{S}_{a}^{\alpha}\cdot\boldsymbol{S}_{b}^{\beta}\boldsymbol{S}_{c}^{\gamma}\cdot\boldsymbol{S}_{d}^{\delta}\right\rangle\right\rangle-q_{1}^{2}\right\};\\ \end{aligned} \quad (31) \] 

and finally the matrix elements describing mixed RSB fluctuations

 \[ C_{1}=\mathcal{H}(a\alpha\beta,a d\alpha\delta)=\mathcal{H}(a\alpha\dot{\beta},c a\gamma\beta)=J B\left\{\left\langle\overline{{\left\langle S_{a}^{\alpha}\cdot S_{a}^{\beta}S_{a}^{\alpha}\cdots S_{d}^{\delta}\right\rangle}}\right\rangle-q_{0}q_{1}\right\} \] 

 \[ C_{2}=\mathcal{H}(a\alpha\beta,a d\gamma\delta)=\mathcal{H}(a\alpha\dot{\beta},c a\gamma\delta)=J B\left\{\left\langle\overline{{\left\langle S_{a}^{\alpha}\cdot S_{a}^{\beta}S_{a}^{\gamma}\cdots S_{d}^{\delta}\right\rangle}}\right\rangle-q_{0}q_{1}\right\} \] 

 \[ C_{3}=\mathcal{H}(a\alpha\beta,c d\gamma\delta)=J B\left\{\left\langle\overline{{\left\langle S_{a}^{\alpha}\cdot S_{a}^{\beta}S_{c}^{\gamma}\cdot S_{d}^{\delta}\right\rangle}}\right\rangle-q_{0}q_{1}\right\}, \quad (32) \] 

with

 \[ B=\frac{1}{4}\tilde{B}\beta^{2}\quad J=\frac{1}{4}\left(\tilde{B}+\tilde{J}\right)\beta^{2}. \quad (33) \] 

A simple interpretation of these matrix elements, similar to that given in e.g. [3], is not possible here, due to the vector character of the spins.

The RS solutions are stable when the matrix (29) is negative definite. Upon analysing all eigenvalues (see Appendix A) it turns out that only two of these can cause the occurrence of a region of broken stability. The first replicon eigenvalue, which we will call the Greek replicon, reads

 \[ \lambda_{G}=A_{1}-2A_{2}+A_{3} \quad (34) \] 

and determines the Greek de Almeida-Thouless (AT) line  \( \lambda_{G}=0 \) . This AT-line measures the breaking of the symmetry with respect to the Greek indices. The corresponding eigenvectors are given by eq. (A.11). The structure of the Greek replicon resembles the one of the replicon mode of the SK model found in [17], and also the Greek replicon mode of the SK model with coupled dynamics as studied in [3]. Since the Greek replicas are (by construction) related to the spin dynamics, the associated region of broken symmetry is located in the region of the phase diagram with low temperature T. The Roman replicon eigenvalue is given by

 \[ \lambda_{R}=(B_{1}-2B_{2}+B_{3})+2n(B_{2}-B_{3}-B_{4}+B_{5})+n^{2}(B_{3}-2B_{5}+B_{6}) \quad (35) \] 

and measures the breaking of the symmetry with respect to the Roman replicas. This occurs at low coupling temperature  \( \tilde{T} \) . Similar to the Greek replicon (34), the eigenvectors corresponding to the Roman replicon instability are symmetric under interchanging all but exactly two – in this case Roman – indices. It turns out that eigenvalues corresponding to eigenvectors which are symmetric under interchanging all but a number of indices which is larger than two, whether Roman, Greek or a mixture of both, can not induce an extra region of broken replica symmetry. Therefore, all regions where the RS Ansatz is unstable, are defined by the locations of the Greek AT line ( \( \lambda_{G}=0 \) ) and the Roman AT line ( \( \Lambda_{R}=0 \) ). These lines are drawn in Fig. 1 and Fig. 3. The latter shows explicitly that there is no re-entrance from the region SG1 to the region with broken replica symmetry (RSB) when T is varied for fixed  \( \tilde{T} \) .
 
![](./images/867747320999968980_5.jpg)

Figure 3. Phase diagram of the XY spin glass with slow dynamic couplings, drawn in the  \( \tilde{T}-T \)  plane; for  \( B_{0}=0 \) ,  \( \tilde{B}=1 \)  and  \( \tilde{J}=3 \) . Further notation as in Fig. 1.

RS solution is always stable in SG1 with respect to the Roman replicas. In fact one can show analytically that the Roman AT line coincides with the SG1-SG2 transition line.

The RS replica theory developed for our model, with spin and coupling dynamics on two different time-scales, is reminiscent of that of the simple XY model with one step replica symmetry breaking (1RSB). Our eigenvalues also formally resemble e.g. those describing the stability of the 1RSB solution in the perceptron model  \( [12, 23] \) . Note also that the position of the Roman AT line in our model is quite different from that in  \( [3] \) , although the phase diagrams of both models are qualitatively the same. The set of eigenvectors given there turn out to satisfy only part of the required orthogonality relations used in their calculations. An improved phase diagram for the SK model can be found in  \( [18] \) .

Finally we remark that the simpler model with homogeneous biases, mentioned earlier, does not involve Roman replicas, such that there appears only a Greek AT line. The latter line is qualitatively the same as the one in the model considered here.

## 5. Simulations

In order to complete our study and verify the predictions of our theory, we have performed numerical simulations of our model (note that, due to the parameter redundancy in our model, we can always restrict ourselves to  \( \tilde{J}=3 \)  and  \( \tilde{B}=1 \) ). We have considered a population of XY spins, evolving according to the coupled Langevin equations (3) and (5), which were discretised according to a standard Euler method, with iteration time step  \( \Delta t=0.001 \) . Several interesting and subtle aspects arise when one attempts to carry out numerical simulations of models of the type studied here, with its widely disparate time-scales. Firstly, it will be clear that the presence of two adiabatically separated time-scales induce extremely large computing times, which
 
![](./images/867747320999968980_6.jpg)

Figure 4. Evolution in time of the configurational energy (2) of the system, for parameters  \( B_{0}=0 \) ,  \( \tilde{B}=1 \) ,  \( \bar{J}=3 \) , T=1.1 and n=5, and with a system of size N=200. The first window is chosen on the basis of the time required for the combined dynamical system (spins and interactions) to reach equilibrium; here we decided on a window size of 200. The values of the observables  \( q_{0} \)  and  \( q_{1} \)  were obtained by performing a temporal average over a (third) time-window of the same size.

prevent us from numerical exploration of the equilibrium regime for large system sizes. This is a general and systematic constraint, which causes important finite size effects, mainly near the phase transitions. In all our numerical studies we have, as a result, been forced to restrict ourselves to relatively modest systems of N = 200 spins. A second point concerns the evolution of the relevant quantities of the problem, spins and couplings, in view of the need to calculate the two main observables of the problem through an averaging process. This will have to be done very carefully, in order for the measured objects to indeed be identical to (or at least an acceptable approximation of) those calculated in the theory. Again the problem is related to having a finite system size: this narrows the time window where, on the one hand, the fast processes can be assumed to have been equilibrated, yet, on the other hand, the slow processes can be assumed not to have taken place. Thirdly, there is the fundamental problem that in regions where replica symmetry no longer holds (beyond either of the two AT lines) already the spin dynamics will exhibit the traditional phenomena associated with ageing, including extremely slow relaxation towards equilibrium; even without the additional superimposed slow dynamics of the couplings, it would have been extremely difficult to carry out numerical simulations that would probe the true equilibrium regime.

We have dealt with these practical problems by adopting the following strategy. For a given set of couplings we first let spins to relax to their stationary state; then we
 
![](./images/867747320999968980_7.jpg)

Figure 5. Spin-glass order parameters  \( q_{0} \)  (circles) and  \( q_{1} \)  (squares) versus temperature, for n = 2. Continuous lines represent the theoretical predictions, while symbols denote simulation results (with N = 200, averaged over the time-window indicated in figure 4 and over 10 samples). As in the previous figures:  \( B_{0} = 0 \) ,  \( \tilde{B} = 1 \)  and  \( \tilde{J} = 3 \) .

![](./images/867747320999968980_8.jpg)

Figure 6. Spin-glass order parameters  \( q_{0} \)  (circles) and  \( q_{1} \)  (squares) versus temperature, for n = 5. Continuous lines represent the theoretical predictions, while symbols denote simulation results (with N = 200, averaged over the time-window indicated in figure 4 and over 10 samples). As in the previous figures:  \( B_{0} = 0 \) ,  \( \tilde{B} = 1 \)  and  \( \tilde{J} = 3 \) .
 
![](./images/867747320999968980_9.jpg)

Figure 7. Non-normalised phase distribution  \( P(\phi) = \sum_{i} \delta[\phi - \phi_{i}] \)  (discretised to a histogram) as observed at three different stages of the dynamical process towards equilibrium, for parameters  \( B_{0} = 0 \) ,  \( \tilde{B} = 1 \) ,  \( \bar{J} = 3 \) , T = 1.1 and n = 5, and with a system of size N = 200. Bottom graph: (random) phase distribution at t = 0. Middle graph: phase distribution at t =  100 (during transient stage). Top graph: phase distribution at  \( t = 200 \) .

perform the average  \( \langleS_{i}\cdotS_{j}\rangle \)  over a number of time steps sufficiently large to have a statistically reliable measurement. We subsequently modify the interactions  \( \{J_{ij}\} \)  for a certain number of time steps, completing what we call a 'dual iteration step'. This dual process is repeated until the global equilibrium state is reached. The key questions in the adequate employment of this strategy is to quantify rationally the various durations. According to the theory, since the time-scale associated with the couplings is infinitely slow compared to that of the fast variables (the spins), in each dual updating step we should modify the interactions  \( \{J_{ij}\} \)  only very slightly (and during only a small number of update steps  \( \Delta t \) ). However, there are limits in practice to the extent to which one can proceed in this manner, in view of the danger of the simulations becoming so slow that they exceed by far one's computing resources. In our simulations we have updated the interactions during several hundred steps  \( \Delta t \)  (after having satisfied ourselves experimentally that a duration somewhere between 500 and 1000 iteration steps is quite appropriate) before, in turn, allowing the spin states to evolve. In this manner we have managed to speed up the convergence process towards global equilibrium, whilst continually verifying that the stationary values of the order parameters  \( q_{0} \)  and  \( q_{1} \) , thus obtained, are not significantly affected. Even more delicate is deciding on the amount of time during which to evaluate the spin averages occurring in the stochastic equations.
 

for the interactions. If the number of time steps used to calculate these averages is too large, the spins will have enough time to diffuse over the whole circle (due to finite size fluctuations which would have been absent in an infinitely large system), leading to an underestimation of  \( q_{0} \) . Our experiments indicate that averaging over a period of between 2000 and 3000 iteration steps (of duration  \( \Delta t \)  each) gives reliable results. Finally, we have to decide on the window size (the number of dual updating steps) which we have to average over in order to compute the observables of the system. The logical approach would appear to be to monitor the evolution of quantities such as the energy (2), starting from the initial state, until the stationary state has been (or at least appears to have been) reached. Figure 4 shows a typical numerical experiment. The dynamics towards equilibrium on this time-scale is ultimately controlled by the slow variables, the couplings. The spins respond to changes in the couplings in a stochastic master/slave fashion, and only when the slow variables (the couplings) have reached a stationary stationary state can we speak about global (thermal) equilibrium. In figure 4 we see that 200 dual steps suffice to ensure the absence of the main transient effects.

The observed dependence on temperature of the two spin-glass order parameters,  \( q_{0} \)  and  \( q_{1} \) , is illustrated in figures 5 and 6, together with the corresponding theoretical predictions. We have carried out these numerical simulations for the temperature ratios  \( n = T/\tilde{T} = 2 \)  and 5, respectively. For the smaller temperature ratio n = 2 we observe that our simulations indeed confirm the existence of two spin-glass phases; one exhibiting freezing only on spin time-scales, and a second spin-glass phase where freezing is observed on all time scales. However, quantitative agreement between theory and simulations is extremely difficult to achieve, due to the practical problems outlined above. For n = 5 the system is in the region where the theory predicts that a first order phase transition from a paramagnetic phase to a second-spin glass phase should be found. We observe a good agreement between theory and simulations, except for temperatures close to the transition, where finite size effects are obviously increasingly important. In addition to the above equilibrium observables, we have investigated other, non-equilibrium, aspects of our model, by way of further illustration. We have measured, for instance, the distribution  \( P(\phi) = \sum_{i} \delta[\phi - \phi_{i}] \)  of phases  \( \phi_{i} \) , defined via  \( \mathbf{S}_{i} = (\cos \theta_{i}, \sin \theta_{i}) \) . Figure 7 shows this distribution at three different stages during the evolution towards equilibrium, for system parameters identical to those of figure 6. Initially the phases were distributed uniformly; one observes this distribution to deform spontaneously into a bi-modal one, driven in conjunction with the feedback provided by the (slow) dynamics of the couplings.

## 6. Concluding Discussion

In this paper we have discussed and solved a version of the classical XY spin-glass model in which both the spins and their couplings evolve stochastically, according to coupled equations, but on widely disparate time-scales. The spins play the role of fast variables, whereas the couplings evolve only very slowly, but according to local
 

stochastic laws which involve the states of the spins. In the context of disordered magnetic systems this model describes a situation where one takes into account the possible effects of slow diffusion of the magnetic impurities, without necessarily assuming energy equi-partitioning between the slow variables (the impurity locations) and the spins (hence the potentially different temperatures associated with each). Alternatively, in the context of neural systems this model would describe coupled neural oscillators  \( [15] \)  with autonomous stochastic Hebbian-type synaptic adaptation on the basis of the degree of firing synchrony of pairs of neurons.

We have solved our model within the replica-symmetric (RS) mean-field theory, involving two levels of replicas: one level related to the (slow) couplings, and one related to the disorder in the problem (the symmetry breaking terms in the dynamics of the couplings, representing preferred random values of the latter). The solution of our model, in RS ansatz, is mathematically similar to that of the XY model with static couplings, but with one-step RSB. This is reminiscent of the general connection between the breaking of replica symmetry and the existence of dynamics on many time scales  \( [24] \) . We have discussed in detail the stability of the RS-solutions, including the calculation of all eigenvalues and their multiplicities (details of which can be found in the appendices). It turns out that two distinct replicon eigenvalues determine the region of stability, and thus the region of validity of the RS solution.

The thermodynamic phase diagram is found to exhibit two different spin-glass phases, one where freezing occurs on all time-scales, and one where freezing occurs only on the (fast) time-scale of the spin dynamics. We also find both first- and second-order transitions; the origin of the first order ones is the positive feedback in the system (compared to a system with stationary spin-couplings) which is induced by the superimposed coupling dynamics. As could have been expected, the physics of the present model resembles that of the SK model with dynamic couplings, apart from a re-scaling in temperature and provided an appropriate adjustment of the calculation of the AT lines in  \( [3] \)  is made. Our calculations show how the methods used for solving the Ising case can be easily adapted to deal with more complicated spin types, and in addition illustrates further the robustness of the phase diagrams describing the behaviour of large spin systems with dynamic couplings.

Numerical simulations present further interesting technical challenges, due to the existence of adiabatically separated time scales (which requires equilibration of two different nested stochastic processes in order to test the theory), in addition to the already highly non-trivial and extremely slow dynamics of the fast (spin) system. In spite of the important finite size effects, which are inevitable given the practical constraints on available CPU time, our results show good agreement with the theory and confirm the main characteristics of the predicted behaviour.
 

## Acknowledgements

DB would like to thank the National Fund for Scientific Research-Flanders (Belgium) for financial support. ACCC and CPV are grateful for support from the Acciones Integradas programme (British Council & Ministerio de Educación y Cultura, grant 2235).

## References

[1] Coolen A C C, Penney R W and Sherrington D 1993 Phys. Rev. B 48 16116

[2] Dotsenko V, Franz S and Mézard M 1994 J. Phys. A: Math. Gen. 27 2351

[3] Penney R W and Sherrington D 1994 J. Phys. A: Math. Gen. 27 4027

[4] Feldman D E and Dotsenko V S 1994 J. Phys. A: Math. Gen. 27 4401

[5] Caticha N 1994 J. Phys. A: Math. Gen. 27 5501

[6] Horner H 1984 Z. Phys. B 57 29

[7] Sherrington D and Kirkpatrick S 1975 Phys. Rev. Lett. 35 1792

[8] Shinomoto S 1987 J. Phys. A: Math. Gen. 20 L1305

[9] Penney R W, Coolen A C C and Sherrington D 1993 J. Phys. A: Math. Gen. 26 3681

[10] Dong D W and Hopfield J J 1992 Network 3 267

[11] Dotsenko V S and Feldman D E 1994 J. Phys. A: Math. Gen. 27 L821

[12] Dorotheyev E A 1992 J. Phys. A: Math. Gen. 25 5

[13] Lattanzi G, Nardulli G, Pasquariello G and Stramaglia S 1997 Phys. Rev. E 56 4567

[14] Caroppo D and Stramaglia S 1998 Phys. Lett. A 246 55

[15] Kuramoto Y 1975 in International symposium on mathematical problems in theoretical physics, H. Araki, ed. (Springer, New York)

[16] Fukai T and Shiino M 1994 Europhys. Lett. 26 647

[17] de Almeida J R L and Thouless D J 1978 J. Phys. A: Math. Gen. 11 983

[18] Jongen G, Bollé D and Coolen A C C 1998 J. Phys. A: Math. Gen. 31 L737

[19] Kirkpatrick S and Sherrington D 1978 Phys. Rev. B 17 4384

[20] Mézard M, Parisi G and Virasoro M A 1997 Spin Glass Theory and Beyond (World Scientific, Singapore)

[21] Abramowitz M and Stegun I A (Eds) 1965 Handbook of Mathematical Functions (Dover Publications, New York)

[22] Anemiüller J 1996 IPNN MSc Project Report, King's College London

[23] Whyte W and Sherrington D 1996 J. Phys. A: Math. Gen. 29 3063

[24] van Mourik J and Coolen A C C 2000 cond-mat/0009151 (submitted to J. Phys. A)
 
![](./images/867747320999968980_10.jpg)

Figure A1. Graphical representation of the structure of a general eigenvector of the Hessian matrix (29). Dark spaces denote the  \( \epsilon \) -components; the other non-empty spaces are the  \( \eta \) -components. Further details are found in the text.

## Appendix A. The Hessian matrix

## Appendix A.1. Eigenvectors and eigenvalues

In this Appendix we show how to find all eigenvectors, eigenvalues and their multiplicity of the Hessian matrix (29). We immediately remark that H is symmetric, implying that its eigenvectors must be orthogonal, a property exploited heavily in finding its eigenvalues.

We denote the eigenvectors in the  \( \frac{1}{2}[rn(n-1)+r(r-1)n^{2}] \) -dimensional space by  \( (\epsilon_{a}^{\alpha\beta},\eta_{cd}^{\gamma\delta}) \)  with  \( \alpha<\beta \)  and c<d, and represent them graphically in a square matrix as in Fig. A1. This matrix is of size  \( nr\times nr \)  and is divided in  \( r^{2} \)  sub-matrices of size  \( n\times n \) , labeled by two Roman indices  \( (a,b,c=1\ldots r) \) . The elements of these sub-matrices, in turn, are labeled by two Greek indices  \( (\alpha,\beta,\gamma,\delta=1\ldots n) \) . Thus the rows and columns of the matrix carry a Roman and a Greek index. Each of the matrix elements corresponds to a component of the vector  \( (\epsilon_{a}^{\alpha\beta},\eta_{cd}^{\gamma\delta}) \) , except for the diagonal components, which are put equal to 0 (viz. an empty space). The elements of the type  \( (a\alpha,c\gamma) \)  correspond to  \( \eta_{ac}^{\alpha\gamma} \)  when  \( a\neq c \)  and to  \( \epsilon_{a}^{\alpha\gamma} \)  when  \( a=c \)  but  \( \alpha\neq\gamma \) . The matrix is symmetric, such that  \( \eta_{ac}^{\alpha\gamma}=\eta_{ca}^{\gamma\alpha} \)  and  \( \epsilon_{a}^{\alpha\gamma}=\epsilon_{a}^{\gamma\alpha} \) .

The eigenvectors of H with eigenvalue  \( \lambda \)  satisfy the eigenvalue equation

 \[ \mathcal{H}\left(\begin{array}{c}{\epsilon_{a}^{\alpha\beta}}\\ {\eta_{c d}^{\gamma\delta}}\end{array}\right)=\lambda\left(\begin{array}{c}{\epsilon_{a}^{\alpha\beta}}\\ {\eta_{c d}^{\gamma\delta}}\end{array}\right). \quad (A.1) \] 

At this point we remark that  \( \{\epsilon_{a}^{\alpha\beta}\} \)  are generally uncorrelated fluctuations of the order parameters  \( \{q_{a}^{\alpha\beta}\} \)  and  \( \{\eta_{cd}^{\gamma\delta}\} \)  of  \( \{q_{cd}^{\gamma\delta }\} \) . Therefore we call a vector  \( (\epsilon_{a}^{\alpha\beta},\eta_{cd}^{\gamma\delta}) \)  symmetric under permutation of the Roman and Greek indices when the components  \( \{\epsilon_{a}^{\alpha\beta}\} \)  and
 
![](./images/867747320999968980_11.jpg)

Figure A2. Representation of the replica symmetric eigenvector. Empty space denotes zero elements; spaces with the same fill pattern denote elements with identical matrix elements. The dark spaces indicate the  \( \epsilon \) -components; the other spaces indicate the  \( η \) -components.

 \( \{\eta_{cd}^{\gamma\delta}\} \)  are simultaneously symmetric under permutation of these indices. In order to find the explicit form of the eigenvectors we make a general proposal based on this symmetry. Furthermore, we use the eigenvalue equation (A.1) and the orthogonality of the eigenvectors corresponding to different eigenvalues.

We start from the symmetric solution where all components are identical, viz.

 \[ \epsilon_{c d}^{\alpha\beta}=f\quad\mathrm{a n d}\quad\eta_{c d}^{\gamma\delta}=g. \quad (A.2) \] 

These vectors are represented in Fig. A2. Substitution of (A.2) into the eigenvalue equation (A.1) reduces the number of equations to solve to two and we easily find

 \[ \begin{aligned}&(X_{1}-\lambda)f+Y_{1}g=0\\&X_{2}f+(Y_{2}-\lambda)g=0\\&X_1=A_1+2(n-2)A_2+\frac{1}{2}(n-2)(n-3)A_3\\&Y_1=2n(r-1)C_1+n(n-2)(r-1)C_2+\frac{1}{2}n^2(r-1)(r-2)C_3.\\ \end{aligned} \quad (A.3) \] 

From this we get two non-degenerate eigenvalues

 \[ \begin{aligned}&\lambda_{1,2}=\frac{1}{2}\left(Y_{2}+X_{1}\pm\sqrt{(Y_{2}+X_{ 1})^{2}-4(X_{1}Y_{2}-X_{2}Y_{1})}\right)\\&X_{2}=2(n-1)C_{1}+(n-1)(n-2)C_{2}+\frac{1}{2}n(n-1)(r-2)C_{3}\\&Y_{2}=B_{1}+2(n-1)B_{2}+(n-1)^{2}B_{3}+2n(r-2)B_{4}\\&\quad+2n(n-1)(r-2)B_{5}+\frac{1}{2}n^{2}(r-2)(r-3)B_{6}.\\ \end{aligned} \quad (A.4) \]
 
![](./images/867747320999968980_12.jpg)

Figure A3. Representation of the eigenvectors (A.6). Empty space denotes zero elements; spaces with the same fill pattern denote elements with identical matrix elements. The dark spaces denote the components  \( \epsilon_{x}^{\theta\beta} \) , the striped spaces the  \( \epsilon_{x}^{\alpha\beta} \) , the checked spaces the  \( \eta_{xb}^{\theta\beta} \) , the other non-empty spaces the  \( \eta_{xb}^{\alpha\beta} \) .

The matrix elements  \( A_{1},\ldots,C_{3} \)  are given by eqs. (29,30).

The other eigenvalues are related to the breaking of the symmetry in (A.2), both at the level of Roman indices and at that of the Greek indices. The most simple form of symmetry breaking is the case where almost all components are identical, except for those labeled by a single specific pair of indices  \( \{x,\theta\} \) :

 \[ \begin{aligned}\epsilon_{x}^{\theta\beta}&=f;\quad\epsilon_{x}^{\alpha\beta}=g;\quad\epsilon_{a}^{\alpha\beta}=h;\\\eta_{xb}^{\theta\beta}&=k;\quad\eta_{xb}^{\alpha\beta}=l;\quad\eta_{ab}^{\alpha\beta}=m\quad a,b\neq x;\alpha,\beta\neq\theta\end{aligned} \quad (A.5) \] 

This increases drastically the number of equations obtained from (A.1). A first trial solution within this group of candidate eigenvectors is obtained upon putting h = m = 0, giving a group of eigenvectors with all components vanishing, except the ones labeled by  \( \{x, \theta\} \) :

 \[ \begin{aligned}\epsilon_{x}^{\theta\beta}&=f;\quad\epsilon_{x}^{\alpha\beta}=-\frac{2}{n-2}f;\quad\epsilon_{a}^{\alpha\beta}=0;\\\eta_{xb}^{\theta\beta}&=k;\quad\eta_{xb}^{\alpha\beta}=-\frac{1}{n-1}k;\quad\eta_{ab}^{\alpha\beta}=0\\Y_{1}&k=(\lambda-X1)f\\X_{1}&=A_{1}+(n-4)A_{2}-(n-3)A_{3}\\Y_{1}&=\frac{n}{n-1}(n-2)(r-1)(C_{1}-C_{2}).\end{aligned} \quad (A.6) \] 

The graphical representation of these eigenvectors in the form of a matrix is drawn in Fig. A3. The associated eigenvalues read

 \[ \lambda_{3,4}=\frac{1}{2}\left(Y_{2}+X_{1}\pm\sqrt{(Y_{2}+X_{ 1})^{2}-4(X_{1}Y_{2}-X_{2}Y_{1})}\right) \]
 
![](./images/867747320999968980_13.jpg)

Figure A4. Representation of the eigenvectors (A.8). Empty space denotes zero elements; spaces with the same fill pattern denote elements with identical matrix elements. Striped spaces denote the components  \( \epsilon_{x}^{\alpha\beta} \) , dark spaces the components  \( \epsilon_{a}^{\alpha\beta} \) , checked spaces the components  \( \eta_{xb}^{\alpha\beta} \) , the other non-empty spaces the components  \( \eta_{ab}^{\alpha\beta} \) .

 \[ \begin{aligned}X_{2}&=(n-1)\left(C_{1}-C_{2}\right)\\Y_{2}&=B_{1}+(n-2)B_{2}-(n-1)B_{3}+n(r-2)B_{4}\\&\quad+n(n-1)(r-2)B_{5}.\end{aligned} \quad (A.7) \] 

The degeneracy of the associated eigenspace is  \(  r(n-1)  \) ; it is found by calculating explicitly the rank of the matrix composed by these eigenvectors, as will be outlined in appendix A2.

Insertion of the general proposal (A.5) into eq. (A.1), and subsequently requiring the orthogonality of this vector to the eigenvectors we have already found earlier, leads us to the new eigenspace

 \[ \begin{aligned}\epsilon_{x}^{\theta\beta}&=\epsilon_{x}^{\alpha\beta}=f\;;\quad\epsilon_{a}^{\alpha\beta}=-\frac{1}{r-1}f\;;\\\eta_{xb}^{\theta\beta}&=\eta_{xb}^{\alpha\beta}=k\;;\quad\eta_{ab}^{\alpha\beta}=-\frac{2}{r-2}k\\Y_{1}&k=(\lambda-X1)f\\X_{1}&=A_{1}+2(n-2)A_{2}+\frac{1}{2}\left(n-2)(n-3)A_{3}-\frac{1}{2}n(n-1)A_{4}\\Y_{1}&=2n(r-1)C_{1}+n(n-2)(r-2)C_{2}-n^{2}(r-1)C_{3}\end{aligned} \quad (A.8) \] 

with eigenvalue

 \[ \begin{aligned}&\lambda_{5,6}=\frac{1}{2}\left(Y_{2}+X_{1}\pm\sqrt{(Y_{2}+X_{11})^{2}-4(X_{1}Y_{2}-X_{2}Y_{1})}\right)\\&X_{2}=\frac{r-2}{r-1}\left((n-1)C_{1}+\frac{1}{2}\left(n-1)(n-2)C_{2}-\frac{1}{2}n(n-1)C_{3}\right)\right.\\ \end{aligned} \]
 
![](./images/867747320999968980_14.jpg)

Figure A5. Representation of the eigenvectors (A.11). Empty space denotes zero elements; spaces with the same fill pattern denote elements with identical matrix elements. the striped spaces indicate the components  \( \epsilon_{x}^{\theta\nu} \) , the dark spaces the components  \( \epsilon_{x}^{\theta\alpha} \)  and  \( \epsilon_{y}^{\alpha\nu} \) , the checked spaces the components  \( \epsilon_{x}^{\alpha\beta} \) .

 \[ \begin{aligned}Y_{2}\ =B_{1}+2(n-1)B_{2}+(n-1)^{2}B_{3}+n(r-4)B_{4}\\ \ +n(n-1)(r-4)B_{5}-n^{2}(r-3)B_{6}.\end{aligned} \quad (A.9) \] 

The vectors (A.8), represented graphically in Fig. A4, are symmetric under interchanging all indices but one Roman index x, and have associated with each eigenvalue a  \( (r-1) \) -dimensional eigenspace.

A second class of eigenvectors is found by considering a situation where one Roman index x and two different indices  \( \theta \)  and  \( \nu \)  cause breaking of the replica symmetry. In their most general form these are given by

 \[ \begin{array}{l}\epsilon_{x}^{\theta\nu}=f\;;\quad\epsilon_{x}^{\theta\beta}=\epsilon_{x}^{\alpha\nu}=g\;;\quad\epsilon_{x}^{\alpha\beta}=h\;;\quad\epsilon^{\alpha\beta}=k\;;\\ \eta_{xb}^{\theta\beta}=\eta_{xb}^{\nu\beta}=l\;;\quad\eta_{xb}^{\alpha\beta}=m\;;\quad\eta^{\alpha\beta}_{ab}=p\qquad(a,b\neq x;\alpha,\beta\neq\theta,\nu)\;.\end{array} \quad (A.10) \] 

More explicitly, we propose a vector with two special Greek indices, i.e. we try a solution with k = l = m = p = 0. It corresponds to a vector with all  \( \eta \) -components and all  \( \epsilon \) -components which are not related to this Roman index vanishing, and with broken replica symmetry with respect to the two Greek indices:

 \[ \begin{array}{l}\epsilon_{x}^{\theta\nu}=f\;;\quad\epsilon_{x}^{\theta\beta}=\epsilon_{x}^{\alpha\nu}=-\frac{1}{n-2}f\;;\quad\epsilon_{x}^{\alpha\beta}=\frac{2}{(n-2)(n-3)}f\;;\quad\epsilon_{a}^{\alpha\beta}=0;\\ \eta_{xb}^{\theta\beta}=\eta_{xb}^{\nu\beta}=0\;;\quad\eta_{xb}^{\alpha\beta}=0\;; \quad(a,b\neq x;\alpha,\beta\neq\theta,\nu)\;.\end{array} \quad (A.11) \] 

They are visualised in Fig. A5. The eigenvalue equals

 \[ \lambda_{7}=A_{1}-2A_{2}+A_{3} \quad (A.12) \] 

and has multiplicity  \(  rn(n-3)/2  \) .
 
![](./images/867747320999968980_15.jpg)

Figure A6. Representation of the eigenvectors (A.15). Empty space denotes zero elements; spaces with the same fill pattern denote elements with identical matrix elements. Dark spaces denote the components  \( \eta_{xy}^{\alpha\beta} \) , striped spaces the components  \( \eta_{xb}^{\alpha\beta} \)  and  \( \eta_{ay}^{\alpha\beta} \) , the other non-empty spaces the components  \( \eta_{ab}^{\alpha\beta} \) .

Finally, replica symmetry can also be broken by two spins with different Roman indices x and y. Upon calling the corresponding Greek indices  \( \theta \)  and  \( \nu \) , this group of eigenvectors reads in its most general form

 \[ \begin{aligned}&\epsilon_{x}^{\theta\beta}=\epsilon_{y}^{\nu\beta}=f\ ;\quad\epsilon_{x}^{\alpha\beta}=\epsilon_{y}^{\alpha\beta}=g\ ;\quad\epsilon_{a}^{\alpha\beta}=h\ ;\\&\eta_{xy}^{\theta\nu}=k\ ;\quad\eta_{xy}^{\alpha\beta}=\eta_{xy}^{\alpha\nu}=l\ ;\quad\eta_{xb}^{\theta\beta}=\eta_{ay}^{\alpha\nu}=m\ ;\\&\eta_{xy}^{\alpha\beta}=p\ ;\quad\eta_{xb}^{\alpha\beta}=\eta_{ay}^{\alpha\beta}=q\ ;\quad\eta_{ab}^{\alpha\beta}=t\quad(a,b\neq x,y;\alpha,\beta\neq\theta,\nu)\ .\\ \end{aligned} \quad (A.13) \] 

Again (A.1) and the orthogonality relations are used in order to find explicit solutions. One eigenvalue is given by

 \[ \lambda_{8}=(B_{1}-2B_{2}+B_{3})+2n(B_{2}-B_{3}-B_{4}+B_{5})+n^{2}(B_{3}-2B_{5}+B_{6}) \quad (A.14) \] 

with the corresponding eigenvectors (Fig. A6)

 \[ \begin{aligned}&\epsilon_{x}^{\theta\beta}=\epsilon_{y}^{\nu\beta}=\epsilon_{x}^{\alpha\beta}=\epsilon_{y}^{a\beta}=\epsilon_{a}^{\alpha\beta}=0\ ;\quad\eta_{xy}^{\theta\nu}=\eta_{xy}^{\theta\beta}=\eta_{xy}^{\alpha\nu}=\eta_{xy}^{a\beta}=k;\\&\eta_{xb}^{\theta\beta}=\eta_{ay}^{\alpha\nu}=\eta_{xb}^{\alpha\beta}=\eta_{ay}^{a\beta}=-\frac{1}{r-2}k\ ;\quad\eta_{ab}^{\alpha\beta}=\frac{2}{(r-2)(r-3)}k\\ \end{aligned} \quad (A.15) \] 

and with degeneracy  \(  r(r - 3)/2  \) . All  \( \epsilon \) -components vanish.

Yet another eigenvalue is

 \[ \lambda_{9}=B_{1}-2B_{2}+B_{3} \quad (A.16) \] 

with eigenvectors given by

 \[ \eta_{xy}^{\theta\nu}=k\;;\quad\eta_{xy}^{\theta\beta}=\eta_{xy}^{\alpha\nu}=-\frac{1}{n-1}k\;;\quad\eta_{xy}^{\alpha\beta}=\frac{1}{(n-1)^{2}}k; \]
 
![](./images/867747320999968980_16.jpg)

Figure A7. Representation of the eigenvectors (A.17). Empty space denotes zero elements; spaces with the same fill pattern denote elements with identical matrix elements. The dark spaces denote the components  \( \eta_{xy}^{\theta\nu} \) , the striped spaces the components  \( \eta_{xy}^{\alpha\beta} \)  and  \( \eta_{x'y'}^{\alpha\nu} \) , the other non-empty spaces the components  \( \eta_{xy}^{\alpha\beta} \) .

 \[ \begin{aligned}&\epsilon_{x}^{\theta\beta}=\epsilon_{y}^{\nu\beta}=\epsilon_{x}^{\alpha\beta}=\epsilon_{y}^{{\alpha\beta}}=\epsilon_{a}^{{\alpha\beta}}=0\;;\\ &\eta_{x b}^{\theta\beta}=\eta_{a y}^{\alpha\nu}=\eta_{x b}^{\alpha\beta}=\eta_{a y}^{\alpha\beta}=\eta_{\alpha b}^{\alpha\beta}=0\;;\\ \end{aligned} \quad (A.17) \] 

This corresponds to a situation where only the components with the marked indices x and y are non-vanishing. The vectors are drawn in Fig. A7. The degeneracy of the eigenvalue (A.16) is  \( \frac{1}{2} r(r - 1)(n - 1)^{2} \) .

Finally, the last eigenvector reads (Fig. A8)

 \[ \begin{aligned}&\epsilon_{x}^{\theta\beta}=\epsilon_{y}^{\nu\beta}=\epsilon_{x}^{\alpha\beta}=\epsilon_{y}^{{\alpha\beta}}=\epsilon_{a}^{{\alpha\beta}}=0\;;\quad\eta_{a b}^{\alpha\beta}=0\;.\\&\eta_{x y}^{\theta\nu}=k\;;\quad\eta_{x y}^{\theta\beta}=\eta_{x y}^{\alpha\nu}=\frac{n-2}{2(n-1)}k\;;\quad\eta_{x b}^{\theta\beta}=\eta_{a y}^{\alpha\nu}=-\frac{1}{2(r-2)}k\;;\\&\eta_{x y}^{\alpha\beta}=-\frac{1}{(n-1)}k;\quad\eta_{x b}^{\alpha\beta}=\eta_{a y}^{\alpha\beta}=\frac{1}{2(n-1)(r-2)}k\;.\\ \end{aligned} \quad (A.18) \] 

The corresponding eigenvalue is equal to

 \[ \lambda_{10}=B_{1}+(n-2)B_{2}-(n-1)B_{3}-n B_{4}+n B_{5} \quad (A.19) \] 

and has degeneracy  \( \frac{1}{2}r(r-2)2(n-1) \) .

## Appendix A.2. The multiplicity of the eigenvalues

This appendix has been included in the present paper since no information is available in the replica literature about explicit methods to find the multiplicity of the eigenvalues of the Hessian matrix. We do not aim for mathematical rigour, but just aim to aid the reader by giving a heuristic method for finding the solution.
 
![](./images/867747320999968980_17.jpg)

Figure A8. Representation of the eigenvectors (A.18). Empty space denotes zero elements; spaces with the same fill pattern denote elements with identical matrix elements. The dark spaces denote the components  \( \eta_{xy}^{\theta\nu} \) , the checked spaces the components  \( \eta_{xy}^{\theta\beta} \)  and  \( \eta_{x\nu}^{\alpha\gamma} \) , the diagonally striped spaces the components  \( \eta_{x\beta}^{\alpha\gamma} \) , the vertically striped spaces the components  \( \eta_{x\delta}^{\theta\beta} \)  or  \( \eta_{a\nu}^{\alpha\gamma} \) , the other non-empty spaces the components  \( \eta_{x\delta}^{\alpha\beta} \)  or  \( \eta_{a\nu}^{\alpha\beta} \) .

Appendix A.2.1. Eigenvalues  \( \lambda_{3,4} \)  and  \( \lambda_{5,6} \) . We first focus on  \( \lambda_{3,6} \) . The sum of all r eigenvectors (A.8) equals zero, such that there are at most r-1 linearly independent vectors. In the sequel we show that the rank of the matrix composed of all eigenvectors is exactly given by this latter value. We consider the r-dimensional sub-matrix constructed by that part of the  \( \epsilon \) -component of the vectors (A.8) with fixed Greek indices (e.g.  \( \alpha=1 \) ,  \( \beta=2 \) ) viz.  \( (\epsilon_{a}^{12}, a=1,\ldots,r) \) ; the r vectors are obtained by varying the Roman index x. This matrix reads

 \[ \mathbb{M}=(f-g)\mathbb{1}+g\mathbb{P}\qquad g=\frac{-1}{r-1}f \quad (A.20) \] 

where  \( \mathbb{I} \)  and  \( \mathbb{P} \)  are the unit matrix and the projector matrix, respectively, here both of dimension r. Since these matrices commute they can be diagonalized simultaneously. The only eigenvector of  \( \mathbb{P} \)  with a non-zero eigenvalue is the vector  \( (1,1,\ldots,1) \)  with eigenvalue r. All other eigenvectors can be chosen orthogonal to this vector. This results in the following eigenvalues for  \( \mathbb{M} \) : one non-degenerated eigenvalue  \( (f-g)+rg=0 \)  and an  \( (r-1) \) -fold degenerate eigenvalue  \( f-g=\frac{r}{r-1}f \) . We conclude that all four eigenvalues (A.9) have degeneracy  \( (r-1) \) .

The multiplicity of  \( \lambda_{3,4} \)  can be found in an analogous way. Since eigenvectors with a different Roman index x are always independent, it is sufficient to determine the dimension of the matrix constructed from the n eigenvectors with the Roman index fixed, e.g. x = 1, and with the Greek index  \( \theta \)  running from 1 to n.
 

Appendix A.2.2. Eigenvalues  \( \lambda_{7} \)  and  \( \lambda_{8} \)  We start with the less complicated calculation for  \( \lambda_{8} \) . As before we consider a sub-matrix which is the  \( r(r-1)/2 \) -dimensional matrix of the  \( \eta \) -part of the eigenvectors (A.15), with fixed Greek indices e.g.  \( \alpha=1=\beta \)  viz.  \( (\eta_{ab}^{\alpha/\beta}, a<b=1,\ldots,r) \) 

 \[ \begin{aligned}\mathbb{M}&=(f-g)\mathbb{1}+g\mathbb{P}+(h-g)\mathbb{I}\mathbb{B}\\&g=\frac{-1}{r-2}f\quad h=\frac{2}{(r-2)(r-3)}f\\&\mathbb{I}\mathbb{B}_{\alpha\beta,\gamma\delta}=(1-\delta_{\alpha\gamma})(1-\delta_{\alpha\delta})(1-\delta_{\beta\gamma})(1-\delta_{{\beta}\delta}),\alpha<\beta,\gamma<\delta.\end{aligned} \quad (A.21) \] 

Because the three matrices appearing above commute, the problem of finding the eigenvalues  \( \mu_{i} \)  of M reduces to finding the eigenvalues  \( \gamma_{i} \)  of I. First, one finds the non-trivial eigenvector of I,  \( (1,1,\ldots,1) \) , which is also an eigenvector of I with eigenvalue  \( (r-1)(r-3)/2 \) . The other eigenvectors  \( (x_{ab}) \) , with a < b, can be chosen orthogonal to the trivial one, i.e.  \( \sum_{a<b}x_{ab}=0 \) , leading to the following simplified eigenvalue equation for the eigenvectors of I.

 \[ \begin{aligned}\gamma x_{ab}&=\sum_{c<d}\mathbb{B}_{ab,cd}x_{cd}=x_{a}+y_{a}+x_{b}+y_{b}+x_{ab}\\\Downarrow\quad&x_{a}=\sum_{b(a)}x_{ab}\quad y_{b}=\sum_{a(<b)}x_{ab}\ $ 1-\gamma)x_{ab}&=x_{a}+y_{a}+x_{b}+y_{b}.\end{aligned} \quad (A.22) \] 

The first solution of these equations is  \( \gamma = 1 \) , with multiplicity  \( r(r - 1)/2 - r \)  due to the condition  \( x_{a} + y_{a} = 0 \) ,  \( a = 1, \ldots, r \) . When  \( \gamma \neq 1 \) , we can sum (A.22) in two different ways:

 \[ \begin{aligned}\sum_{a(<b)}&:(1-\gamma)y_{b}=(b-1)(x_{b}+y_{b})+\sum_{a(<b)}(x_{a}+x_{b})\\\sum_{b(a)}&:(1-\gamma)x_{a}=(n-a)(x_{a}+y_{a})+\sum_{b(a)}(x_{b}+y_{b}).\end{aligned} \] 

Adding the two equations gives

 \[ (3-\gamma-r)(x_{a}+y_{a})=0 \quad (A.23) \] 

and leads to the eigenvalue  \( \gamma = 3 - r \) . Because of the second factor in (A.23) we can conclude that I \( \mathbb{B} \)  has no other eigenvalues than the ones already found, leading to the multiplicity r - 1 for  \( \gamma = 3 - r \) . It turns out that only  \( \gamma = 1 \)  gives a non-zero eigenvalue of M. We can therefore conclude that the rank of M is equal to  \( r(r - 1)/2 - r = r(r - 3)/2 \) .

The same procedure can be followed to determine the multiplicity of  \( \lambda_{7} \) , but now by considering M as composed by the  \( \epsilon \) -part of the eigenvectors, for a fixed choice of the Roman index x. Eigenvectors with different Roman indices are again linearly independent.

Appendix A.2.3. Eigenvalue  \( \lambda_{9} \)  First, we note that each choice of the Roman indices x and y gives a set of independent eigenvectors, so we can limit ourselves to finding the
 

rank of the matrix generated by the vectors with x = 1 = y

 \[ \begin{aligned}\eta_{11}^{\theta\nu}&=f&\eta_{11}^{\theta\beta}&=\eta_{11}^{\alpha\nu}&=g&\eta_{11}^{\gamma\delta}&=h\\g&=\frac{-1}{n-1}&f&h&=\frac{1}{(n-1)^{2}}&f\end{aligned} \] 

which can be written as

 \[ \begin{aligned}\mathbb{M}&=(f-g)\mathbb{1}+g\mathbb{P}+(h-g)\mathbb{B}\\\mathbb{B}_{\alpha\beta,\gamma\delta}&=\left\{\begin{array}{cc}0&\alpha=\gamma\\\tilde{\mathbb{B}}_{\beta\delta}&\alpha\neq\gamma with\tilde{\mathbb{B}}=\mathbb{P}-\mathbb{1}\end{array}\right.\end{aligned} \quad (A.24) \] 

where the dimension of  \( \tilde{B} \)  is n. The special structure of B allows us to find its eigenvalues quite easily, namely: one non-degenerate eigenvalue  \( (n-1)^{2} \) , one  \( 2(n-1) \) -fold degenerate eigenvalue  \( -(n-1) \) , and one  \( (n-1)^{2} \) -fold degenerate eigenvalue 1. The first and second of these give a zero eigenvalue for M, leading to rank  \( \mathbb{M}=(n-1)^{2} \) .

Appendix A.2.4. Eigenvalue  \( \lambda_{10} \)  Calculating the multiplicity of this eigenvalue involves some more work. In contrast to the previous sections, we here have to calculate the dimension of the full matrix of eigenvectors, rather than just the dimension of a suitable sub-matrix. Upon writing the eigenvectors as

 \[ \begin{aligned}\epsilon_{x}^{\theta\beta}&=\epsilon_{y}^{\nu\beta}=\epsilon_{x}^{\alpha\beta}=\epsilon_{y}^{\alpha\beta}=\epsilon_{\alpha}^{\alpha\beta}=0\;;\quad\eta_{ab}^{\alpha\beta}=0\;.\\\eta_{xy}^{\theta\nu}&=f\;;\quad\eta_{xy}^{\theta\beta}=\eta_{xy}^{\alpha\nu}=g\;;\quad\eta_{xb}^{\theta\beta}=\eta_{ay}^{\alpha\nu}=h\;;\\\eta_{xy}^{\alpha\beta}&=k;\quad\eta_{xb}^{\alpha\beta}=\eta_{ay}^{\alpha\beta}=l;\end{aligned} \] 

the matrix of eigenvectors M reads

 \[ \begin{aligned}\mathbb{M}_{ab\alpha\beta,cd\gamma\delta}=\left\{\begin{array}{ll}f&a=c and b=d and\alpha=\gamma and\beta=\delta\\g&a=c and b=d and(\alpha=\gamma or\beta=\delta)\\k&a=c and b=d and\alpha\neq\gamma and\beta\neq\delta\\h&one subindex and the corresponding superindex are equal\\l&one subindex is equal (and not the superindex)\\0&otherwise\end{array}\right.\end{aligned} \quad (A.25) \] 

It is found to consist of sub-matrices B (containing elements f, g and k) on the diagonal, and sub-matrices  \( D_{i}, i = 1, \ldots, 4 \)  (containing elements h and l, ordered in four different ways) elsewhere. All of these sub-matrices have dimension  \( n^{2} \) .

In order to simplify the problem we first construct the matrix C which is made up of columns which are orthogonal and normalized eigenvectors of B. For every sub-matrix  \( D_{i} \)  we construct C  \( D_{i}C^{T} \) , where  \( C^{T} \)  is the transposed matrix of C. Next we construct the matrix

 \[ \hat{C}=\left(\begin{array}{c c}{\boldsymbol{C}}&{}\\ {}&{\ddots}\\ {}&{}\\ {}&{}&{\boldsymbol{C}}\end{array}\right). \quad (A.26) \]
 

Since  \( \hat{C}\hat{C}^{T}=1 \)  by construction, the eigenvalue equations of M and  \( M\equiv\hat{C} \)  M  \( \hat{C}^{T} \)  are the same, and we can restrict ourselves to solving the simpler eigenvalue problem of the latter matrix.

First we focus on the matrix B and the construction of the matrix C. As in Section Appendix A.2.3 we have

 \[ \begin{aligned}\mathbb{B}&=(f-g)\mathbb{I}+g\mathbb{P}+(k-g)\mathbb{I}\mathbb{K}\\\mathbb{K}_{\alpha\beta,\gamma,\delta}&=\left\{\begin{array}{ll}0&\alpha=\gamma\\\tilde{\mathbb{K}}_{\beta\delta}&\alpha\neq\gamma with\tilde{\mathbb{K}}=\mathbb{P}-\mathbb{I}\end{array}\right.\end{aligned} \] 

Upon using the Gramm-Schmidt procedure for constructing a set of orthogonal and normalized eigenvectors of  \( \tilde{K} \) , we arrive at the following result:

 \[ \tilde{C}=\left(\begin{array}{ccccc}\frac{1}{\sqrt{n}}&\frac{1}{\sqrt{\overline{n}}}&\frac{1}{\overline{\sqrt{n}}}&\frac{ 1}{\sqrt{\overline{n}}}&\frac{1}{\overline{\sqrt{n}}}&\cdots&\frac{1}{\sqrt{\overline{n}}}\\ \frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{\overline{2}}}&0&0&0&\cdots&0\\ \frac{1}{2}\sqrt{\frac{2}{3}}&\frac{1}{2} \sqrt{\frac{2}{3}}&-\sqrt{\frac{2}{\overline{3}}}&0&0&\cdots&0\\ \frac{1}{3}\sqrt{\frac{3}{4}}&\frac{1}{3} \sqrt{\frac{3}{4}}&\frac{1}{3} \sqrt{\frac{3}{\overline{4}}}&-\sqrt{\frac{3}{4}}&0&\cdots&0\\ \vdots&\vdots&\vdots&\vdots&&\vdots&\vdots\\ \frac{1}{n-1}\sqrt{\frac{n-1}{n}}&\frac{1}{n-1} \sqrt{\frac{n-1}{n}}&\frac{1}{n-1} \sqrt{\frac{n-1}{\overline{n}}}&\frac{1}{n-1} \sqrt{\frac{n-1}{\overline{n}}}&\frac{1}{n-1} \sqrt{\frac{n-1}{\overline{n}}}&\cdots&-\sqrt{\frac{n-11}{n}}\end{array}\right). \quad (A.27) \] 

Due to the similar structure of the two matrices  \( \tilde{K} \)  and I, we now can immediately read off the matrix of eigenvectors C of B: one takes a matrix with the structure of (A.27), and multiplies each matrix element by  \( \tilde{C} \) , arriving at a matrix with dimension  \( n^{2} \) . Given this matrix it is straightforward to calculate C  \( D_{i} \)   \( C^{T} \)  for all sub-matrices  \( D_{i} \) . We arrive at

 \[ \mathcal{M}_{a b\alpha\beta,c d\gamma\delta}=\left\{\begin{array}{l l}{{{\frac{n^{2}}{2(n-1)}}}}&{{{a=c a n d b=d a n d\alpha=\gamma=1a n d\beta=\delta\neq1}}} \\{{{a=c a n d b=d a n d\alpha=\gamma\neq1a n d\beta=\delta=1}}} \\{{{\frac{-n^{2}}{2(n-1)(r-2)}}}}&{{{a=c a n d b\neq d a n d\alpha=\gamma\neq1a n d\beta=\delta=1}}} \\{{{a=d a n d b\neq c a n d\alpha=\delta\neq1a n d\beta=\gamma=1}}} \\{{{a\neq d a n d b=c a n d\alpha=\delta=1a n d\beta=\gamma\neq1}}} \\{{{a\neq c a n d b=d a n d\alpha=\gamma=1a n d\beta=\delta\neq1}}} \\{{{0}}}&{{{o t h e r w i s e}}}\end{array}\right.. \quad (A.28) \] 

In view of the large number of zero-rows in this matrix, it is convenient to define a  \( \frac{1}{2}r(r-1)2(n-1) \) -dimensional matrix  \( \hat{M} \) , which contains only the non-trivial rows

 \[ \begin{aligned}\hat{\mathcal{M}}_{ab\alpha,c d\beta}&=\mathcal{M}_{ab\gamma\delta,c d\mu\nu}\\\gamma&=1&\delta&=\alpha+1&\text{for}\alpha=1,\cdots,n-1\\\gamma&=\alpha-(n-2)&\delta&=1&\text{for}\alpha=n,\cdots,2(n-1)\\\mu&=1&\nu&=\beta+1&\text{for}\beta=1,\cdots,n-1\\\mu&=\beta-(n-2)&\nu&=1&\text{for}\beta=n,\cdots,2(n-1)\end{aligned} \quad (A.29) \] 

This matrix can be written as  \( \hat{\mathcal{M}}=\frac{n^{2}}{2(n-1)}\mathbb{I}+\frac{-n^{2}}{2n-1(r-2)}\mathbb{N} \) , where  \( \mathbb{N} \)  is a matrix with elements 0 or 1 only. As in Section Appendix A.2.2 the eigenvalues of this matrix are obtained by summing the eigenvalue equation for  \( \mathbb{N} \)  in two different ways. We then find
 

the eigenvalue  \( \lambda = -1 \)  with multiplicity  \( \frac{1}{2}r(r-2)2(n-1) \) , and the eigenvalue  \( \lambda = r-2 \)  with multiplicity  \( r(n-1) \) . It turns out that only the first of these eigenvalues gives a non-zero eigenvalue for M, and we may conclude that rank M =  \( r(r-2)(n-1) \) .
 
