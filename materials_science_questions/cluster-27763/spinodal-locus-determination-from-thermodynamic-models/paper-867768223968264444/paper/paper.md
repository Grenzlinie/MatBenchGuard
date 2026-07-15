
# Static and dynamical aspects of the metastable states of first order transition systems

Tomoaki Nogawa \( ^{*} \)  and Nobuyasu Ito

Department of Applied Physics,

The University of Tokyo, Hongo,

Bunkyo-ku, Tokyo 113-8656, Japan

Hiroshi Watanabe \( ^{1} \) 

The Institute for Solid State Physics, The University of Tokyo,

Kashiwanoha 5-1-5, Kashiwa, Chiba 277-8581, Japan \( ^{1} \) 

## Abstract

We numerically study the metastable states of the 2d Potts model. Both of equilibrium and relaxation properties are investigated focusing on the finite size effect. The former is investigated by finding the free energy extremal point by the Wang-Landau sampling and the latter is done by observing the Metropolis dynamics after sudden heating. It is explicitly shown that with increasing system size the equilibrium spinodal temperature approaches the bistable temperature in a power-law and the size-dependence of the nucleation dynamics agrees with it. In addition, we perform finite size scaling of the free energy landscape at the bistable point.

PACS numbers:
 

## I. INTRODUCTION

Phase transition dynamics is ubiquitous in our everyday life. One of the most popular examples is boiling of water  \( [1] \) . In spite of its familiarity, our quantitative understanding of such phenomena remains quite poor due to its strong nonequilibrium property. The most popular theory of these first order transition dynamics is the classical nucleation theory  \( [2, 3] \)  based on the droplet excitation picture, which fundamentally considers the cost of surface energy and gain of bulk energy. However it is beyond this theory how many nuclei are produced for unit volume in the macroscopic system  \( [4] \) . It is necessary to consider multi-nucleation including the interaction between nuclei.

Although nucleation is essentially nonequilibrium process, equilibrium property is useful as a starting point. First order transition, however, leaves more unclear points even in equilibrium in comparison with second order transition. One reason is that the former is very hard to investigate with conventional numerical simulations such as Monte-Calro methods; in order to know fine metastable stricture we have to observe sufficiently large number of rare events, overcoming of free energy barrier. Extended ensemble methods, however, have made breakthrough to this problem  \( [5-7] \) . In this article, we report the detailed analysis of equilibrium metastable states by the Wang-Landau sampling method and its relation to the transition dynamics.

## II. EQUILIBRIUM SPINODAL POINT

To investigate the equilibrium metastability, we employ the Wang-Landau sampling method [7], which yields the density (number) of states as a function of macroscopic extensive quantities such as internal energy. This method is quite efficient to sample metastable states which appears with low probability in the Boltzmann distribution since this method realizes a flat energy histogram. For 2d Potts model, we calculate density of states  \( g(E) \)  as a function of the internal energy,

 \[ E=\sum_{<i,j>\in\mathbf{n.n.}}\left(1-\delta_{\sigma_{i}\sigma_{j}}\right)\quad\mathrm{w i t h}\quad\sigma=0,1,\cdots,q-1. \] 

The Helmholtz’s free energy  \(  F(\beta)  \)  is written as

 \[ e^{-\beta F(\beta)}=\sum_{X}e^{-\beta E(X)}=\sum_{E}g(E)e^{-\beta E}\equiv\sum_{E}e^{-\beta F(\beta;E)} \]
 

where  \( \beta = 1/k_{B}T \)  is inverse temperature and X denotes microscopic state. The extremal condition;  \( \partial F(\beta; E)/\partial E = 0 \) , gives the energy corresponding to the maximum or minimum probability in canonical ensemble at given  \( \beta \) . It is rewritten as

 \[ \beta=\frac{\partial S(E)}{\partial E}\qquad where\qquad S(E)=\ln g(E). \quad (1) \] 

When  \( \beta \)  is not monotonic function of E, there are multiple minima in canonical ensemble for given  \( \beta \)  indicating metastability and hysteresis. The things may be more clear to regard  \( \beta \)  in Eq. (1) as a response of thermodynamic function  \( S(E) \)  against the change of E in the microcanonical ensemble. In microcanonical ensemble, there are coexisting phase between two distinct pure phases. The phase transition between pure phase and coexisting phase has direct connection to the evaporation/condensation transition investigated in continuum and lattice gas system [8–11].

The q-state Potts model on square lattice takes a first order transition between the paramagnetic and ferromagnetic phases for q > 4 at  \( \beta_{c} = \ln(1 + \sqrt{q}) \) . We investigate the system with q = 8 but believe that qualitative behavior does not depend on q. Periodic boundary condition is imposed for  \( L \times L \)  square lattice. We perform parallel computation to treat large size system. The energy region is divided into some parts [12] and each part is associated to individual thread. In order to enhance the relaxation and guarantee the ergodicity, we make overlap energy region for neighboring threads, where the exchange of spin configuration is allowed satisfying a detailed balance condition,

 \[ \frac{W(\{X,Y\}\rightarrow\{Y,X\})}{W(\{Y,X\}\rightarrow\{X,Y\})}=\frac{g_{i}\left(E(Y)\right)g_{j}\left(E(X)\right)}{g_{i}\left(E(X)\big)g_{j}\left(E(Y)\right)}, \] 

in the same spirit with the parallel tempering method \( ^{[6]} \) . Here,  \( g_{i}/g_{j} \)  is a density of states calculated by i-th/j-th thread and  \( W(\{X,Y\} \to \{Y,X\}) \)  means the transition probability from the compound state, X for the i-th thread and Y for the j-th thread, to its exchanged state. The density of states is calculated for the system with L = 32 - 2048 by using 128 threads at most.

The left panel of Fig. 1 shows relation between  \( \beta \)  and E with various system size. For given  \( \beta \) , around  \( \beta_{c}=1.3424\cdots \) , there are two free energy minimal points and one maximum one between them. There are two spinodal points,  \( (E_{\mathrm{spi}}^{f},\beta_{\mathrm{spi}}^f) \)  and  \( (E_{\mathrm{spi}}^{p},\beta_{\mathrm{spi}}^p) \) , at the end of low-energy ferromagnetic branch and high-energy paramagnetic branch as saddle node bifurcation points where energy minimal and maximal points meet to annihilate together.
 
![](./images/867768223968264444_1.jpg)

![](./images/867768223968264444_2.jpg)

FIG. 1: (left) inverse temperature as a function of internal energy calculated from difference,  \( \ln g(E + 1) - \ln g(E) \) , averaged over four individual simulations. The horizontal line indicates  \( \beta = \beta_{c} = \ln(1 + \sqrt{8}) \) . (right) size-dependence of the deviation of spinodal temperature from the first order transition temperature.

The both spinodal points explicitly depend on the system size and approach  \( \beta_{c} \)  with increasing L, i.e., the hysteresis region,  \( \beta_{spi}^{f} < \beta < \beta_{spi} \) , tends to disappear in the thermodynamic limit. The difference is plotted as a function of L in right panel of Fig. 1, which indicates

 \[ \left|\beta_{\mathrm{s p i}}-\beta_{c}\right|\propto L^{-1/\nu}\qquad\mathrm{w i t h}\qquad\nu=1.4(1), \quad (2) \] 

both for  \( \beta_{spi}^{f} \)  and  \( \beta_{psi}^{p} \) .

In addition, the spinodal energy  \( E_{spi}^{f}/N \)  and  \( E_{sp}^{p}/N \)  approaches  \( E_{c}^{f}/N \approx 0.40 \)  and  \( E_{c}^{p}/N \approx 0.89 \) , respectively, with increasing L. These suggests a scaling behavior at the bistable point  \( \beta_{c} \) ;

 \[ \left|E_{\mathrm{s p i}}-E_{c}\right|\propto L^{d_{E}} \] 

and furthermore

 \[ F(\beta_{c};E)=E-\beta_{c}^{-1}\ln g(E)\approx F_{\min}+L^{d_{F}}\hat{V}\left((E-E_{c}^{f})/L^{d_{E}}\right), \] 

for  \( E_{c}^{f} < E \ll E_{c}^{p} \) . Hereafter we consider the scaling behavior around  \( E_{c}^{f} \)  but the same argument holds around  \( E_{c}^{p} \) . Scaled barrier function  \( \hat{V}(x) \)  rises for  \( x \ll 1 \)  and flat for  \( x \gg 1 \) . This leads that

 \[ \beta(E)=\frac{\partial\ln g(E)}{\partial E}=\beta_{c}\left[1-L^{-(d_{E}-d_{F})}\hat{V}^{\prime}(E/L^{d_{E}})\right]. \]
 
![](./images/867768223968264444_3.jpg)

![](./images/867768223968264444_4.jpg)

FIG. 2: finite size scaling of  \( \beta(E) \)  (left) and  \( F(\beta_{c}, E) \)  (right).

This reproduce Eq. (2) with  \( d_{E}-d_{F}=1/\nu \) . We perform scaling as shown in Fig. 2 to estimate  \( d_{E}=1.2(1) \)  and  \( d_{F}=d_{E}-1/\nu=0.5(1) \) . Good collapsing of data is obtained for  \( L\geq256 \) . Note that this finite size scaling does not hold for  \( E<E_{c}^{f} \) , where both internal energy and free energy are extensive, i.e.,  \( d_{E}=d_{F}=1 \) . The free energy well becomes more asymmetric as system size increasing.

Naive energetics of droplet excitation suggests  \( d_{E}=d-1=1 \) . The slight enhancement of the excitation energy is presumably due to the fractal roughness of the interface. On the other hand, the dimension of free energy barrier  \( d_{F}=0.5(1) \)  is smaller than 1. This deviates from the behavior of macroscopic phase separation,  \( d_{F}=1 \)  [13] and there should be another crossover for larger scale,  \( E-E_{c}^{f}\gg L^{0.5} \) .

## III. NONEQUILIBRIUM RELAXATION, ESCAPE FROM METASTABLE STATE

Next, we investigate transition dynamics from ferromagnetic state to para state at fixed temperature. The time evolution of the system is given by the Metropolis algorithm [3, 14]. The unit time is defined as the span in which all spins are updated one time in a sequential manner. All spins  \( \sigma_{i} \)  are set to the same state named 0 in the initial state at t = -1000. After the system is equilibrated at  \( \beta_{c} \) ,  \( \beta \)  is suddenly lowered to aimed value at t = 0.

We observe an order parameter  \( \langle m\rangle=(N^{-1}\langle\sum_{i}\delta_{\sigma_{i},0}\rangle-q^{-1})/(1-q^{-1}) \) , where  \( \langle\cdots\rangle \)  means
 
![](./images/867768223968264444_5.jpg)

![](./images/867768223968264444_6.jpg)

FIG. 3: (left) time evolution of order parameter for L=256 and 1024. The data are averaged over 16384/L samples. (right) temperature dependence of the time crossing m=0.4 for various system size. The vertical lines denote the equilibrium spinodal temperatures for various system size.

the average over independent random number realizations. Time evolution of  \( \langle m\rangle \)  for L=256 and 1024 is shown in the left panel of Fig. 3. For L=1024, there is almost no finite size effect in this data. The characteristic decay time tends to diverge as approaching  \( \beta_{c} \) . We plot the time  \( \tau_{0.4} \)  at which  \( \langle m(t)\rangle \)  crosses 0.40 as a function of  \( \beta \)  in right panel of Fig. 3. For sufficiently large L, size dependence is not observed and the divergence seems to be a little faster than a power-law type;  \( \tau \approx (1 - \beta/\beta_{c})^{-z\nu} \) . This implies that the dynamics is of thermal activation type, typically  \( \tau \propto \exp[\text{const.}/(\beta_{c} - \beta)] \) , although it is difficult to speculate its analytic expression.

On the other hand, finite size effect appears approaching  \( \beta_{c} \)  the earlier, the smaller L becomes. The inverse temperature above which  \( \tau_{0.4} \)  deviates from large size behavior agrees well with the finite-size spinodal point  \( \beta_{\mathrm{spi}}^{f}(L) \)  obtained by equilibrium simulations. Initially  \( \tau_{0.4} \)  overcomes the large size behavior, which presumably due to the backward transition from para phase to ferro phase, while  \( \tau_{0.4} \)  becomes smaller than large size behavior and saturates to a certain value increasing with L.
 

## IV. SUMMARY

In conclusion, we calculate the size-dependent spinodal points of the 8-state Potts model and perform finite size scaling to obtain fractal exponent for free energy barrier  \( d_{F} \approx 0.5 \)  and internal energy  \( d_{E} \approx 1.2 \) . These exponents can be compared with  \( (d^{2}-d)/(d+1) = 2/3 \)  and  \( d^{2}/(d+1) = 4/3 \)  in Ref. [10], where evaporation/condensation transition is discussed based on the Ising model in micromagnetic ensemble, by relating  \( \beta_{spi} - \beta_{c} \)  and  \( (E - E_{c})/N \)  to magnetic field  \( \tilde{H}_{t}^{(2)} \)  and magnetization  \( m_{t} - m_{coex} \) , respectively.

Additionally it is confirmed that size dependent spinodal temperature also gives the dynamical criterion in transition dynamics, which suggests some connection between equilibrium metastability and the nonequilibrium relaxation. Equation 2 implies that there is a diverging length scale in bulk

 \[ \ell_{\mathrm{s p i}}^{\mathrm{e q}}(\beta)\propto|\beta-\beta_{c}|^{-\nu}, \] 

with  \( \nu\approx1.4 \) . It is important to note that such critical like behavior is observed in the energy region of coexisting phase, which is not realized in the canonical ensemble. It will be very interesting if we can find any relation between these unphysical equilibrium state and the nonequilibrium transient state with corresponding energy. The exponent  \( \nu\approx1.4 \)  is larger than 1 which is expected for critical nucleus radius and  \( \ell_{spi}^{eq} \)  may mean the average distance between critical nuclei. The advanced study is required for the thermally activated nuclear growth, where typical distance of nuclei obtained here will give a useful hint.

## Acknowledgement

This work was partly supported by Award No. KUK-I1-005-04 made by King Abdullah University of Science and Technology (KAUST).

[1] H. Watanabe, M. Suzuki, N. Ito, Phys. Rev. E 82 (2010) 051604.

[2] J. W. Gibbs, The Collected Works of J. W. Gibbs. Vol. I, Longmans, 1928.

[3] P. A. Rikvold, H. Tomita, S. Miyashita, S. W. Sides, Phys. Rev. E 49 (1994) 5080.

[4] J. S. Langer, Phys. Rev. Lett. 21 (1968) 973.

[5] B. A. Berg, T. Neuhaus, Phys. Rev. Lett 68 (1992) 9.
 

[6] K. Hukushima, K. Nemoto, J. Phys. Soc. Jpn. 65 (1996) 1996.

[7] F. Wang, D. P. Landau, Phys. Rev. Lett. 86 (2001) 2050.

[8] M. Biskup, L. Chayes, Kotecký, Europhys. Lett. 60 (2002) 21.

[9] T. Neuhaus, J. S. Hager, J. Stat. Phys. 113 (2003) 1.

[10] K. Binder, Physica A 319 (2003) 99.

[11] A. Nußbaumer, E. Bittner, T. Neuhaus, W. Janke, Europhys. Lett. 75 (2006) 716.

[12] D. P. Landau, S.-H. Tsai, M. Exler, American J. Phys. 72 (2004) 1294.

[13] C. Borgs, W. Janke, J. Phys. I France 2 (1992) 2011.

[14] F. Krzakala, L. Zdeborová, J. Chem. Phys. 134 (2011) 034512.
 
