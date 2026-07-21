
# Inversion symmetric two-level systems and the low temperature universality in disordered solids

M. Schechter \( ^{1} \)  and P. C. E. Stamp \( ^{2,3} \) 

 \( ^{1} \) Department of Physics, Ben-Gurion University of the Negev, Beer-Sheva 84105, Israel

 \( ^{2} \) Department of Physics and Astronomy, University of British Columbia,

Vancouver, British Columbia, Canada V6T 1Z1 and

 \( ^{3} \) Pacific Institute for Theoretical Physics, University of British Columbia,

Vancouver, British Columbia, Canada V6T 1Z1

(Dated: today)

The low temperature universal properties in disordered and amorphous solids are considered. We introduce a model that includes two types of two level systems (TLSs), which, based on their local symmetry, interact weakly or strongly with the phonon field. This accounts well for the experimental results, and addresses some long-standing questions: the nature of the TLSs; the smallness and universality of the phonon attenuation, and the energy scale of 3K below which universality is observed. Our model describes disordered lattices; we also discuss its application to amorphous solids.

## I. INTRODUCTION

Amorphous solids, and many disordered lattices, display remarkably similar characteristics at low temperatures, which are very different from those of ordered lattices  \( [1] \) . Below a rather universal temperature  \( T_{U} \approx 3K \) , their specific heat  \( C_{v}(T) \)  is nearly linear in temperature T, the thermal conductivity  \( \kappa(T) \)  is roughly  \( \propto T^{2} \)  (both quantities behave as  \( T^{3} \)  in ordered lattices), and their internal friction Q is independent of T and of the phonon wavelength  \( \lambda \) . Moreover, the thermal conductivity and internal friction vary little between materials whose microscopic structure ranges from impurities in ordered crystals to completely disordered amorphous glasses. This implies a rather universal ratio between the phonon mean free path l and the phonon wavelength  \( \lambda \) , so that  \( l/\lambda \approx 150 \)  [1-4], and suggests that a fundamental mechanism may dictate the low-T behavior of disordered solids. What this mechanism might be is the 'universality problem', which has emerged as one of the outstanding unsolved mysteries in condensed matter physics [3, 5].

Most theoretical analyses begin with the influential "Standard Tunneling" (ST) model [6, 7]. In this model the low-energy modes are described by a single set of noninteracting localized two-level systems (TLSs), which interact weakly with phonons. These TLSs are characterized by two parameters, viz.;  \( \epsilon \)  (the energy bias between the wells), and  \( \Delta_{o} \)  (the tunneling amplitude between the wells). For an ensemble of such TLSs, the ST model assumes a broad joint probability distribution for  \( \epsilon \)  and  \( \Delta_{o} \)  [6, 7], given by  \( P(\epsilon, \Delta_{o}) = P_{o}/\Delta_{o} \) , where  \( P_{o} \)  is a constant. The central dimensionless parameter of the ST model is the "tunneling strength"  \( C_{o} = P_{o}\gamma^{2}/\rho c^{2} \) , where  \( \gamma \)  is the defect-phonon coupling,  \( \rho \)  the mass density, and c the phonon velocity. The ST model gives results agreeing well with the temperature dependence of  \( C_{V}(T) \) ,  \( \kappa(T) \) ,  \( Q(T) \) , and  \( l(T) \)  [6–8], if  \( C_{o} \)  is assumed to be an adjustable parameter. Universality would then be found if one assumed that  \( C_{o} \approx 10^{-3} \)  for the wide range of amorphous and disordered systems.
The ST model leaves some central questions open, viz.: (i) What is the nature of the TLSs? (ii) Why is  \( C_{o} \)  so small and universal? (iii) What dictates the energy scale of 3K below which universality is observed? (iv) what about inter-defect interactions, which are not small? Thus, the ST model has been widely questioned, and the problem of universality has been the subject of thorough theoretical investigation [5, 9–16].

In disordered lattices universal properties have also been observed in the ferroelectric phase  \( [17, 18] \) , and recent experiments on mixed crystals suggest that strong random strain fields acting on tunneling defects may be responsible for universality  \( [19–21] \) . Furthermore, experiments on ion-implanted crystalline Si show that universality is not related to amorphicity \( [22] \) . This has led to the argument  \( [23] \)  that experimental and theoretical studies on universality should focus on disordered crystals, rather than on amorphous systems.

In this paper, we present an approach to the problem, relating the universality to the symmetry of TLS states under local inversion. We will begin by considering a strongly-disordered crystal (not yet fully amorphous) possessing off-center or rotational impurities, each having 2N local states between which it can tunnel. This system has 2 kinds of low-energy excitations (symmetric and asymmetric under inversion), coupling very differently to phonons. At low energies we find that only the symmetric excitations are active, and that a quantitative understanding of universality can then be obtained. We also argue that this model has a natural generalization to fully amorphous systems, also leading to universality.

The paper is organized as follows: in Sec.II the model is introduced. In Sec.III we show how our model leads to universality, and explains other long-standing experimental observations. We conclude in Sec.IV. The technical derivation of our model from microscopic considerations is detailed in App. A. In App. B we describe in detail the derivation of the density of states of the symmetric and asymmetric TLSs, in the absence and presence of random fields.
 
![](./images/867747341635944606_1.jpg)

(a)

![](./images/867747341635944606_2.jpg)

(b)

![](./images/867747341635944606_3.jpg)

(c)

![](./images/867747341635944606_4.jpg)

(d)

FIG. 1: S- and  \( \tau \) -spins, and their interaction with elastic strain. (a) A 2-dimensional system in which the impurity can occupy one of four positions shown by the red and yellow circles; states of the same color are related by inversion symmetry and form a " \( \tau \) -pair". Different colors correspond to different S-supaces, between which transitions are asymmetric with respect to inversion. Distortion by a passing phonon breaks the degeneracy between states of different colors (i.e., couples to the S-excitations) but not between states of the same color (i.e., does not couple to the  \( \tau \) -excitations). (b) The  \( \tau \)  pair degeneracy is broken in a system with finite strain created by strong lattice disorder or amorphousness. This results in a finite but small  \( \tau \) -TLS lattice interaction  \( \gamma_{\tau} \) . (c) We show 2N = 8 states of an impurity, initially assumed degenerate, which are then split in a disordered crystal. The splitting between states in the same  \( \tau \)  pair is small. (d) A specific example: the 3-dimensional alkali halide KBr with two CN impurities, which, in strong disorder, align along one of the three crystal axes (distorting the nearby lattice). Different  \( \tau \)  states are connected by 180° CN flips, whereas different S states are connected by 90° rotations.

## II. THE MODEL

Many disordered crystals showing universal low-T properties have defects that can be modeled as TLs that are either symmetric or asymmetric under local inversion. Some examples are (i) CN flips and rotations in KBr:CN (Fig. 1(d)); (ii) F tunneling between interstitial states and between a lattice position and a vacant interstitial position in  \( CaF_{2}:LaF_{3} \)  [24]; and (iii) double N2 rotations and single N2 rotations in  \( ArN_{2} \) [25, 26].

## A. Effective Hamiltonian

Consider first a single off-center or rotational impurity at lattice site j. In an otherwise pure lattice this impurity can occupy an even number 2N of states at different points in the lattice cell - pairs or 'doublets' of states related by inversion symmetry are classically degenerate (this degeneracy being weakly lifted by tunneling between sites [27]). We model the impurity or defect by treating each doublet as a 'pseudo-spin'  \( \hat{\tau}_{jn} \) , where  \( n = 1, 2, \ldots N \)  labels the different doublets, and the Ising variable  \( \hat{\tau}_{jn}^{z} = |jn \uparrow \rangle \langle jn \uparrow| - |jn \downarrow \rangle \langle j n \downarrow| \)  describes the 'polarization' between the pseudospin states. We likewise define an Ising variable  \( \hat{S}_{jnn'}^{z} = |jn \rangle \langle jn| - |jn' \rangle \langle j n'| \) , describing the polarization between different doublets  \( |jn \rangle \)  and  \( |jn' \rangle \)  at site j (compare Fig. 1(a)). Note that any given doublet couples very weakly to phonons (only to the gradient of the strain field [28]), because of the inversion symmetry.

Now consider a system with some concentration x of randomly distributed impurities, so that the typical distance between impurities is  \( R_{o} = a_{o}x^{-1/3} \)  where  \( a_{o} \)  is the interatomic distance. The lattice strain generated by the impurities break the inversion symmetry, and scramble
 

the states at each site (Fig. 1(b), 1(c)). The effective low energy Hamiltonian of the disordered defect system can then be written as [28, 29]

 \[ \begin{align*}H_{S\tau}\ =&\ \sum_{j}[h_{j}^{S}S_{j}^{z}+h_{j}^{\tau}\tau_{j}^{z}]\\+&\ \sum_{ij}[J_{i j}^{S S}S_{i}^{z}S_{j}^{z}+J_{i j}^{S\tau}S_{i}^{z}\tau_{j}^{z}+J_{i j}^{\tau\tau}\tau_{i}^{z}\tau_{j}^{z}]\end{align*} \quad (1) \] 

where the interaction strengths  \( h^{a} \) ,  \( J^{ab} \)  (with a, b = S,  \( \tau \) ) are random variables, and only the two low energy pairs are considered, (see details in App. A).

The size of the random couplings follows a simple rule, according to which

 \[ J_{i j}^{a b}=\frac{c_{i j}^{a\underline{{b}}}\gamma_{a}\gamma_{b}}{\rho c^{2}(R_{i j}^{3}+\tilde{a}^{3})} \quad (2) \] 

where  \( R_{ij} \)  is the inter-defect distance,  \( \tilde{a} \)  is a short distance cutoff for the interaction,  \( \gamma_{S} \)  and  \( \gamma_{\tau} \)  are the phonon couplings to the S and  \( \tau \)  defects in the presence of the disorder, and the randomness in the magnitude and angular dependence [28, 29] of these couplings are absorbed into the random variables  \( c_{ij}^{ab} \sim O(1) \) . Thus the three interactions have the same radial dependence; however their energy scales are quite different. At a distance  \( R_{ij} = R_{0} \) , one finds typical interaction strengths  \( J_{o} \equiv JS^{S} \propto \gamma_{S}^{2} \sim 500K \) ,  \( JS^{\tau} \propto \gamma_{S} \gamma_{\tau} \sim gJ_{o} \sim 10K \)  and  \( J^{\tau\tau} \propto \gamma_{\tau}^{2} \sim g^{2}J_{o} \sim 0.2K \) . The random field strengths are also governed by  \( J_{o} \)  and g; their typical strengths [28] are  \( h^{S} \lesssim J_{o} \)  and  \( h^{\tau} \lesssim gJ_{o} \) .

A key feature of these results is the role of the coupling  \( \gamma_{\tau} \)  to the phonons. Unlike the situation in the absence of disorder, where the inversion symmetric  \( \tau \) -TLSs couple only to the strain gradient, strong disorder destroys inversion symmetry, and results in a finite coupling  \( \gamma_{\tau} \)  to the strain (see Eq. (A23) and the following derivation of Eq. (1) in App. A2). Since the coupling  \( \gamma_{\tau} \)  is a result of the rather small deviations from inversion symmetry, it is much smaller than the coupling of the asymmetric S-TLSs to the strain. The ratio  \( g = \gamma_{\tau}/\gamma_{S} \)  can be determined microscopically (see App. A2) and also estimated by simple dimensional arguments: in strongly disordered systems the typical displacement of a lattice site due to the random lattice strain will be  \( \delta a \approx a_{o}(E_{\Phi}/E_{C}) \) , where  \( E_{\Phi} \)  is the Debye energy characteristic of acoustic phonons, and  \( E_{C} \)  is the typical Coulombic correlation energy in the solid. Thus we expect  \( g \approx \delta a/a_{o} \approx E_{\Phi}/E_{C} \sim 0.02 \)  (see also Refs. \( ^{[25, 30]} \) ).

A mean-field (MF) treatment of (1) yields a picture of independent S and  \( \tau \)  variables, acted upon by the random couplings in the Hamiltonian (1). This spreads out the states, resulting in Gaussian mean field densities of states  \( n_{S}^{o}(E) \) ,  \( n_{\tau}^{o}(E) \( , of width  \) J_{o} \( ,  \) gJ_{o} \(  and peak height  \) \propto 1/J_{o} \( ,  \) 1/gJ_{o} \( , for the S and  \) \tau $  excitations respectively (see Fig. 2(a)). In this MF picture  \( n_{\tau}^{o}(E) \gg n_{S}^{o}(E) \)  for  \) E \ll gJ_{o} \( , by a factor 1/g; nevertheless, the S-spins dominate the phonon scattering even at low energies, because their scattering rate is  \) \propto \gamma_{S}^{2} \( , and thus far higher (by a factor  \) 1/g^{2} \( ) than that for  \) \tau $  spins.

Thus the model of S and  \( \tau \)  pseudospins gives a nice simple picture in MF theory. However, MF theory is misleading - it neglects correlations between the S and  \( \tau \)  variables, which radically change the low-energy physics.

## B. S-τ Correlations

The correct way to handle these correlations is using an Efros-Shklovskii treatment [31], adapted here for the case of two types of interacting TLSs and the Hamiltonian (1). The details are technical (see App. B), but the physics of the result is straightforward (Fig. 2(a)). Level repulsion between the 2 sets of variables has a radical effect on  \( n_{S}(E) \) , but little effect on  \( n_{\tau}(E) \) , simply because the MF level density  \( n_{\tau}(E) \)  is much higher. Thus,  \( n_{S}(E) \)  shows a slow fall-off for  \( gJ_{o} < E < J_{o} \) , but a precipitous drop for  \( E < gJ_{o} \sim 10K \) , so that when  \( E \ll gJ_{o} \) , the S-states have essentially disappeared. However  \( n_{\tau}(E) \)  only shows a weak dip below the much lower energy  \( J_{\tau}^{\sigma\tau} \sim g^{2}J_{o} \sim 0.2K \) , caused by  \( J_{\tau}^{\sigma\tau} \) . The phonon spectrum is only weakly altered. These results, shown in more detail in Fig. 2(b)-2(d), are also found in Monte Carlo calculations for the Hamiltonian in Eq.(1) [32] and in a hybrid molecular statics and Monte Carlo calculation for the KBr:CN system using only bare interatomic potentials [33].

This abrupt switch in the DOS, from S-states to  \( \tau \) -states, has a crucial consequence - there is a crossover in the system properties at a temperature  \( T_{U} \)  (defined by the condition  \( \gamma_{\tau}^{2}n_{\tau}(T_{U})=\gamma_{S}^{2}n_{S}(T_{U}) \) ). The crossover temperature  \( T_{U}\approx0.2gJ_{o} \) , and is only weakly dependent on  \( \tilde{a} \)  for typical values  \( \tilde{a}/a_{o}\sim1-6 \) . Above  \( T_{U} \) , the S-pseudospins predominate, along with a plentiful supply of phonons, to which they couple strongly, thereby dominating the phonon attenuation. In contrast, below  \( T_{U} \)  the S spins are frozen and exert on the  \( \tau \)  TLSs a random field much larger than the  \( \tau\tau \)  interaction  \( J^{\tau\tau} \) . The  \( \tau \) -pseudospins then behave like a set of non-interacting TLS states in strong disorder; However, they now couple more strongly to phonons than the S pseudospins, and dominate the phonon attenuation. In the fairly narrow crossover regime around  \( T_{U} \) , the  \( S-\tau \)  interactions determine the detailed shape of the crossover.

## III. RELATION TO EXPERIMENTS

Our model above, microscopically derived for the disordered lattices, results in the dominant TLSs at low temperatures having a nearly homogenous DOS at low energies, and a TLS-TLS interaction which is much smaller than their random energies. Furthermore, the fact that these tunneling systems consist of two levels, assumed in
 
![](./images/867747341635944606_5.jpg)

(a)

![](./images/867747341635944606_6.jpg)

(b)

![](./images/867747341635944606_7.jpg)

(c)

![](./images/867747341635944606_8.jpg)

(d)

FIG. 2: Densities of states (DOS) of  \( \tau \)  and S TLSs. (a) We show  \( n_{\tau}(E) \)  in red (it is hardly changed by  \( S-\tau \)  interactions) and  \( n_{S}(E) \)  in blue (the non-correlated DOS  \( n_{S}^{o}(E) \)  is shown in green for comparison). In (b), (c), (d) we show the reduction factor  \( P(E) \equiv n_{S}(E)/n_{S}(E) \) , where  \( \bar{E} \)  is an energy a few times larger than  \( gJ_{o} \) ; essentially  \( n_{S}(E) \)  is the S-spin DOS obtained if one includes S-S correlations but ignores  \( S-\tau \)  correlations, so  \( P(E) \)  measures the effect of  \( S-\tau \)  correlations. Numerical results are shown for  \( \tilde{a}=0 \) ; 1.5; 3; 4.5; 6, for an impurity concentration x=0.2 and sample size  \( 18^{3} \)  cells (i.e.,  \( \sim4650 \)  TLSs), in the 3 cases (b)  \( h^{\tau}=0 \) ; (c)  \( h^{\gamma}/\langle E_{\tau}\rangle \approx 0.3 \) ; and (d)  \( h^{\tau}/\langle E_{\tau}\rangle \approx 1 \) .  \( T_{U} \)  is defined by the energy at which  \( n_{\tau}(E)\gamma_{\tau}^{2}=n_{S}(E)\gamma_{S}^{2} \) , i.e., by  \( P(E) \approx 5g \) . Similar results for x=0.5 are shown in Fig. 4. For both concentrations we find  \( T_{U} \approx 0.2\langle E_{\tau}\rangle \)  for  \( 1 < a_{o} < 6 \) , i.e.,  \( T_{U} \approx 0.2gJ_{o} \) .

the ST model, and later observed experimentally \( ^{[2]} \) , is intrinsic in our model, a result of inversion symmetry. In that, our model is similar to the ST model. However, the central advance in our model with respect to the ST model is that within our model there exists a generic relation between the coupling of the TLSs to the strain and their low energy DOS. This, along with the smallness of the coupling of the  \( \tau \) -TLSs to the strain, and the fact that they are not gapped at low energies, allows us to explain some long standing experimental results, above all the universality and smallness of phonon attenuation, and the energy scale of 3K below which universality is observed.

## A. Universality

The universality is an immediate consequence of the above results, and is found by simply adapting the original ST model analysis to the system of S and  \( \tau \)  spins. Let's first consider the strong disorder regime, where  \( x \sim O(1) \) . The DOS of the  \( \tau \) -TLSs is then given by  \( n_{\tau} \approx (1/g J_{o} R_{0}^{3}) = \rho c^{2}/\gamma_{\tau} \gamma_{S} \) . At the same time, by integrating  \( P(\epsilon, \Delta_{o}) \)  over  \( \Delta_{o} \)  one obtains  \( P_{o} = \kappa n_{\tau} \) , with  \( \kappa^{-1} \equiv ln(\Delta_{o}^{u}/\Delta_{o}^{l}) \) , where  \( \Delta_{o}^{1}, \Delta_{o}^{u} \)  are the lower and upper cutoffs for the 'tunneling amplitudes' of the  \( \tau \)  TLSs. We thus find

 \[ C_{o}=\frac{\kappa n_{\tau}\gamma_{\mathrm{w}}^{2}}{\rho c^{2}}\approx\frac{\kappa\gamma_{\tau}}{\gamma_{S}}\approx\kappa g, \quad (3) \] 

This relation is a direct result of the fact that the phonon scattering rate of  \( \tau \) -TLSs is  \( \propto \gamma_{\tau}^{2} \) , but their DOS is  \( \propto 1/\gamma_{S}\gamma_{\tau} \) , as it is dictated by the coupling to the S-TLSs.
 

(or, in the absence of S-TLSs, to the strong disorder, see discussion of mixed crystals in Sec. III B).

Assuming the usual value  \( \kappa\approx0.1 \) , we then find that  \( C_{o}\approx10^{-3} \) . This small and universal value for  \( C_{o} \)  derives from its dependence on g, which is also small and varies little between different strongly disordered materials. Notice that g also dictates the universal crossover energy  \( T_{U}\approx0.2gJ_{o} \)  consistent with the observed energy scale of  \( \approx3K \) . Although glassiness and the mechanism leading to it are not required by our theory, for glassy systems  \( T_{G}\approx J_{o} \) , i.e.  \( T_{U}\approx0.2gT_{G} \) ,  \( \gamma_{\tau}^{2}\propto T_{G} \) , and  \( P_{o}\propto T_{C}^{-1} \) , in agreement with experiments \( ^{[34,35]} \) .

## B. Further experimental consequences

Strong dilution: The low temperature universal phenomena are observed in both amorphous solids and disordered lattices. One advantage of the latter is the ability to control the identity of the host ions and the concentrations of the tunneling impurities. For example, in KBr:CN, experiments find that phenomena such as the temperature independence of the internal friction and  \( T^{2} \)  dependence of the thermal conductivity exist below 3K for CN concentrations  \( 0.2 < x < 0.7 \) , but not for x < 0.2. However, once CN impurities are added to the mixed crystal  \( KBr_{0.5}KCl_{0.5} \) , then the above mentioned phenomena are observed also at  \( x \ll 1 \) , only with a tunneling strength which is proportional to x. These experimental results [19, 20] were argued to support the notion that the loss of universality at  \( x \ll 1 \)  is a result of the reduction of the strain. Our analysis supports this notion.

Let us consider first the dilute case in a pure crystal, e.g.  \( KBr_{1-x}CN_{x} \)  with  \( x \ll 1 \) . In this system the strain at each CN impurity site is caused solely by the presence of the other CN impurities. This does not change the typical value of  \( \gamma_{S} \) , but  \( \gamma_{\tau} \sim x^{4/3} \) , see Eq.(A21). As a result, the typical energy for an S excitation  \( J^{SS} \propto x \) , whereas the typical energy for a  \( \tau \)  excitation  \( J^{S\tau} \propto x^{7/3} \) . Furthermore, the magnitude of the  \( \tau \) -TLS energy at site j and its coupling to the phonon field are strongly correlated, as both are dictated by the proximity of the nearest neighbor impurity.

For strongly disordered systems we have argued that universal properties appear below  \( T_{U} \)  since at this energy scale  \( \tau \) -TLSs behave as noninteracting TLSs with a roughly constant DOS, and with an interaction with the phonon field which is not correlated with their energy. At  \( x \ll 1 \)   \( T_{U}(x) \propto x^{7/3} \ll 3K \) . Furthermore, even at  \( T < T_{U}(x) \)  it is not clear that universality exists, as it may well be violated by the above mentioned correlations.

Let us now consider the case of dilute tunneling impurities in a mixed crystal, as were realized by CN impurities added to  \( KBr_{0.5}Cl_{0.5} \)  [19, 20]. In this case the strain at the CN impurity sites is dictated by the mixed lattice itself, and is comparable to the strain in  \( KBr_{1-x}:CN_{x} \)  with 0.2 < x < 0.7. The typical S and  \( \tau \)  energies are now dictated by the random field terms  \( h^{S} \) ,  \( h^{\tau} \)  arising from the interaction of the CNs with the Br and Cl ions through the volume term in Eq.(A7) (or its simplified form, Eq. (A23) in App. A 2), see also Ref.[28].  \( \gamma_{\tau} \)  can be derived similarly to the derivation in Sec.A 2. Thus, all energy scales are the same as in the strongly disordered KBr:CN. The only effect of having small x is the reduction in  \( n(\tau) \) , and we therefore find that universal properties exist in the mixed crystals, albeit with a tunneling strength  \( C \approx 0.1gx/x_{c} \) . This result is in agreement with experiments [19, 20].

Electric dipole interactions: Both  \( \tau \)  and S defects may have electric dipole moments, leading to electric dipole mediated interactions whose strength at the nearest impurity distance is  \( J_{ee} \) . Thus,  \( J_{o} > J_{ee} \)  almost always, but the ratio  \( J_{ee}/J_{o}^{S\tau} = J_{ee}/gJ_{o} \)  can be small or large, and typically  \( J_{ee} > J_{o}^{\tau\tau} = g^{2}J_{o} \) . If  \( J_{ee} < gJ_{o} \) , then all the arguments above go through, but now the  \( \tau - \tau \)  interaction strength is  \( J_{ee} \) ; the energy at which the very weak dipole 'depression' appears in  \( n_{\tau}(E) \)  then becomes  \( J_{ee} \) . Such dipole depressions in the DOS are seen in some experiments [36] below 1K. If  \( J_{ee} > gJ_{o} \) , electric dipole interactions also change the  \( S - \tau \)  interactions. This does not change the basic picture, but now one finds  \( T_{U} \sim J_{ee} \) , and  \( C_{o} \)  is reduced to  \( C_{o}' \sim g^{2}J_{o}/J_{ee} \) .

Amorphous systems and glasses: Experimentally, there is overwhelming support to the notion that the universal phonon attenuation at low temperatures is equivalent in disordered lattices and amorphous solids. This strongly suggests that the mechanism leading to universality is intrinsic to the disordered state of matter, and is the same in both systems. One can therefore expect that one model would be relevant to both disordered lattices and amorphous solids. Our model is derived microscopically for the disordered lattices. We argue here that although amorphous solids lack long range order, and exact symmetries on any scale, it is plausible that our model describes well their low temperature characteristics.

While amorphous materials do not show long range order, local order with a lattice bond coordination number does exist, except at defect sites, and inter-site distances are hardly altered from lattice values. For example, in amorphous Si,  \( \delta a/a_{o} \sim 0.03(0.1) \)  for nearest (next nearest) neighbors [37], and the nearest-neighbor bond angle differs by a maximum of 10%. Now, our results depend essentially on the distinction between S and  \( \tau \)  defects and rely on local properties of the system (contributions to  \( \gamma_{\tau} \) , resulting from deviations from inversion symmetry, are random and decrease as  \( 1/r^{4} \) , see App. A 2). Thus, neither  \( J_{o} \)  nor g is strongly affected by amorphicity.

This allows us to make some clear predictions for amorphous systems. First, if nearly inversion-symmetric TLSs do exist therein, then our model predicts that amorphous systems will also show universality with similar values of  \( T_{U} \)  and  \( C_{o} \) . Second, we predict that in addition to the TLSs responsible for the universal properties, there exists a second type of TLS with much higher (by a factor  \( \sim\cdot10^{2} \) ) coupling to phonons and with a DOS given in
 

Fig. 2. This prediction could in principle be checked by using the powerful technique of phonon echo  \( [38–40] \) , adjusted to fit the above characteristics of the asymmetric excitations.

## IV. CONCLUSIONS

We find that the low temperature universal properties in disordered solids result from inversion symmetric TLSs. Such TLSs interact weakly with phonons, yet gap other non-symmetric TLSs at energies lower than 3K. Quantitative universality and the energy scale of 3K below which universality is observed are both dictated by the rather universal value of the ratio of strain to interatomic distance in strongly disordered solids. This is because this value dictates both the relation between the DOS of the TLSs and their coupling to the phonon field, and the ratio between the universality temperature and the glass transition temperature. Various additional experimental observations, some of which are long unaccounted for, are naturally explained within our theory. Our results are derived from the microscopic properties of disordered lattices, and their applicability to amorphous solids needs to be checked.

Acknowledgments — We thank A. Aharony, A. Burin, O. Entin-Wohlman, A. Gaita-Ariño, and A. J. Leggett for discussions. The work was supported by NSERC in Canada, PITP, and the ISF.

## Appendix A: Derivation of Model, and mapping to interacting S and  \( \tau \) -spins

In the main text we use a model of interacting S and  \( \tau \)  spins to describe the low-energy excitations in the system. In this section we give more details of how this model is derived, starting from a microscopic model of the systems we are interested in.

## 1. Microscopic Model: Single Impurity

Consider first a single impurity or defect sitting in an otherwise perfect lattice, on site j at position  \( r_{j} \) . We assume the lattice itself is inversion-symmetric, and that the system is insulating. We model the system by a Hamiltonian  \( \hat{H} = \hat{H}_{latt} + \hat{H}_{imp} + \hat{V} \) , where  \( H_{latt} \)  is the bare lattice Hamiltonian,  \( \hat{H}_{imp} \)  is the impurity Hamiltonian, and  \( \hat{V} \)  is their mutual interaction. One can then write the impurity Hamiltonian as  \( \hat{H}_{imp} = \hat{H}_{imp}^{o} + \hat{H}_{imp}^{\tau} \) , where the first bare or 'potential' term takes the form

 \[ \hat{H}_{i m p}^{o}(\mathbf{r}_{j})=\sum_{n=1}^{N}\sum_{\sigma}^{\pm}\epsilon_{j n}c_{j n\sigma}^{\dagger}c_{j n\sigma} \quad (A1) \] 

and the second kinetic or 'tunneling' term is written as

 \[ \hat{H}_{i m p}^{T}(\mathbf{r}_{j})=\sum_{n n^{\prime}}\sum_{\sigma\sigma^{\prime}}t_{n n^{\prime},\sigma\sigma^{\prime}}c_{j n\sigma}^{\dagger}c_{j n^{\prime}\sigma^{\prime}} \quad (A2) \] 

We will drop this second tunneling term, for reasons explained below.

In these equations,  \( c_{jn\sigma}^{\dagger} \) ,  \( c_{jn\alpha} \)  create/destroy an impurity or defect state labeled by (i) the impurity site j, (ii) the pair index n for the N different excitation pairs on the j-th site, and (iii) the internal pair quantum number  \( \sigma = \pm \) . Thus we are assuming a set of N pairs (often called 'two-level systems, or TLS's) of 'internal states' for the impurity/defect, to give a total of 2N states. That they come in degenerate pairs, with energy  \( \epsilon_{jn} \) , follows from the assumed inversion symmetry. The number and physical nature of these states depends on the system of interest. Thus, e.g., a light Halide defect like a Li atom, which substitutes for Na or K in a KCl or NaCl lattice, can rattle around inside a 'cage' formed by the original lattice. The 8 lowest energy Li impurity states comprise 4 degenerate pairs of states; each pair is degenerate with the other 3 pairs, and each state is quasi-localized around potential minima at the < 111 > sites. The same is found if we substitute in CN impurities. Those states quasi-localized around other 'cage' sites (e.g., the < 100 > sites) are higher in energy. However, if we substitute in  \( OH^{-} \) impurities, we find 6 degenerate lowest states localized around 3 pairs of minima at the < 100 > sites; whereas if we substitute in F or Ag impurities into a  \( NaBr \)  lattice, we find 6 pairs of degenerate low-energy states localized around the < 110 > sites. In all these cases, the set of energies  \( \epsilon_{jn} \)  divides into several degenerate groups, one of which is lowest in energy. Typically each such group of degenerate states contains more than one pair of states, simply because there are other symmetries at the impurity site apart from inversion symmetry. The number of impurity states that we consider in our Hamiltonian depends on the UV cutoff we assume for the impurity effective Hamiltonian. Thus, in the case of, say, CN impurities in a KBr or KCl lattice, we might want to consider both the lowest set of 4 pairs at the < 111 > sites, and the set of 3 pairs of < 100 > sites which are at somewhat higher energy. This then makes for a total of 14 states in our impurity Hilbert space.

In more general cases the physical locations of the TLS states may not be obvious - the inversion-symmetric pairs of states may refer more complicated defects, or to some kind of rotation. Finally, whereas for systems with only one kind of defect the energy  \( \epsilon_{jn} \)  is independent of site index j, we can also consider a lattice having several different kinds of impurity or defect at different sites. The same model Hamiltonian still applies; but the energy  \( \epsilon_{jn} \)  will then depend on j.

As a simple example of this physics we consider a 4-site 'toy' model. This model was already introduced in Fig.
 

1(a) of the main paper. It has the site Hamiltonian

 \[ \hat{H}_{i m p}^{o}=\sum_{\mu=1}^{4}\epsilon_{\mu}c_{\mu}^{\dagger}c_{\mu} \quad (A3) \] 

in which, because of inversion symmetry,  \( \epsilon_{1} = \epsilon_{2} = \epsilon_{A} \) , and  \( \epsilon_{3} = \epsilon_{4} = \epsilon_{B} \) , where A, B label the two different inversion-symmetric pairs. We can thus also write this Hamiltonian as

 \[ \begin{align*}\hat{H}_{imp}^{o}=&\sum_{\sigma}\epsilon_{A}c_{A\sigma}^{\dagger}c_{A\sigma}+\epsilon_{B}c_{B\sigma}^{\dagger}c_{B\sigma}\\=&E_{AB}^{o}+\Delta_{AB}^{o}\sum_{\sigma}(\epsilon_{A}c_{A\sigma}^{\dagger}c_{A\sigma}-\epsilon_{B}c_{B\sigma}^{\dagger}c_{B\sigma})(A4)\end{align*} \] 

where  \( E_{AB}^{o} \)  is the mean or 'midpoint' energy of the A and B states, and  \( \Delta_{AB}^{o} \)  is the difference in energy between them.

We have ignored any tunneling between the different states in this toy model, just as we did in (A2), because the tunneling amplitudes - typically  \( |t_{nn',\sigma\sigma'}| \sim O(1\ K) \)  or less, are small, in strong disorder, compared with the bias energies of the S TLSs - typically  \( \approx 500K \)  and the bias energies of the  \( \tau \)  TLSs, typically  \( \approx 10K \) , as is discussed in Sec. A2. Thus, the effect of tunneling on the distribution of biases of the symmetric and asymmetric TLSs is negligible. Once the latter is established, tunneling resumes a role identical to its role in the ST model. The differences  \( \Delta\epsilon_{nn'} = |\epsilon_{jn} - \epsilon_{jn'}| \)  will vary greatly between different systems, but as discussed below, we will only be interested in states for which  \( \Delta\epsilon_{nn'} \)  is less than a few hundred Kelvin, since only such states can be shifted by the strain to low energies.

Consider now the defect-phonon interaction, which arises because the defect distorts the lattice (since the system is neutral, we ignore electron transfer terms). It is helpful to work this out first for the toy model. We have an interaction

 \[ \hat{V}_{j}=\sum_{\mu=1}^{4}V_{j\mu}(u_{\alpha\beta})c_{j\mu}^{\dagger}c_{j\mu} \quad (A5) \] 

at the j-th site, where  \( V_{j\mu}(u_{\alpha\beta}) \)  is some function of the lattice strain tensor  \( u_{\alpha\beta}(\mathbf{r}_{j}) \)  at site j. We now introduce the Ising variables  \( \hat{S}^{z} \)  and  \( \hat{\tau}^{z} \)  as follows (compare main text, Fig. 1(b)). Define (i) the change  \( \bar{\eta}_{AB} = E_{AB} - E_{AB}^{o} \)  in the midpoint energy of the 4 states caused by the defect-phonon coupling; (ii) the change  \( \bar{\Gamma}_{AB} = \Delta_{AB} - \Delta_{AB}^{o} \)  in the splitting between the A and B states, and (iii) the splitting energy  \( \bar{\zeta}_{n} = \epsilon_{n\uparrow} - \epsilon_{n\downarrow} \) , opened up by defect-phonon coupling, between the internal states of the n-th pair (here n = A, B).
In terms of phonon variables,  \( \bar{\eta}_{AB} = \eta_{AB}\delta^{\alpha\beta}u_{\alpha\beta} \) , where  \( \eta_{AB} \)  is just an isotropic energy shift, and  \( \bar{\Gamma}_{AB} = \Gamma_{AB}^{\alpha\beta}u_{\alpha\beta} \) ; the lattice strain is sensitive to the difference between the A and B states because these are not related to each other by inversion. However, the 2 internal states of a given pair are related by inversion, and so only

![](./images/867747341635944606_9.jpg)

FIG. 3: Interaction of the symmetric TLSs with the gradient of the strain. The degeneracy of states related by inversion symmetry is broken by the second derivative of the phonon displacement.

the gradient  \( \partial_{\gamma}u_{\alpha\beta} \)  of the lattice strain can cause a splitting between them (see Fig. 3). The splitting energy is  \( \tilde{\zeta}_{n} = \zeta_{n}^{\alpha\beta\gamma}\partial_{\gamma}u_{\alpha\beta} \) .

Thus we see that the interaction for the toy model, with an impurity at the j-th site, is (here we use the Einstein summation convention for spin indices  \( \alpha,\beta \) , etc.):

 \[ \begin{align*}\hat{V}_{j}=[\eta_{AB}\delta^{\alpha\beta}+\Gamma_{AB}^{\alpha\beta}\hat{S}_{AB}^{z}]u_{\alpha\beta}(\mathbf{r}_{j})\\+\sum_{n}^{A,B}\zeta_{n}^{\alpha\beta\gamma}\hat{\tau}_{n}^{z}\partial_{\gamma}u_{\alpha\beta}(\mathbf{r}_{j})\end{align*} \quad (A6) \] 

We have defined  \( \hat{S}_{AB}^{z} = (|A\rangle\langle A| - |B\rangle\langle B|) \) , and likewise  \( \hat{\tau}_{n}^{z} = (|n\uparrow\rangle\langle n\uparrow| - |n\downarrow\rangle\langle n\downarrow|) \) , in terms of the site operators given above. We emphasize here that (i) we should not think of  \( \hat{S}_{z} \)  as the z-component of a spin variable - we are treating it purely as an Ising variable; and (ii) we can if we wish define a spin-half operator  \( \hat{\tau}_{n} \) , for a specific pair n, with the transverse terms  \( \hat{\tau}_{n}^{\pm} \)  describing tunneling processes between internal states of a given pair. However, since we ignore such tunneling processes in this paper, we only consider  \( \hat{\tau}_{n}^{z} \) , and treat it as an Ising variable as well.

Generalizing to an arbitrary number of levels on the impurity site we get the final Hamiltonian for a lattice system with a single impurity at site j:

 \[ \hat{H}_{i m p}=\hat{H}_{p h}+\hat{H}_{i m_{p}}^{o}(\mathbf{r}_{j})+\sum_{n n^{\prime}}\sum_{\alpha\beta}\left\{[\eta_{j n n^{\prime}}\delta^{\alpha\beta}+\Gamma_{j n n^{\ell}}^{\alpha\beta\gamma}\hat{S}_{j n n^{\prime}}^{z}]u_{\alpha\beta}(\mathbf{r}_{j})+\delta_{n n^{\prime}}\zeta_{j n}^{\alpha\beta\gamma}\hat{\tau}_{j n}^{z}\partial_{\gamma}u_{\alpha\beta}(\mathbf{r}_{j})\right\} \quad (A7) \]
 

where  \( \hat{H}_{imp}^{\sigma}(\mathbf{r}_{j}) \)  is just the bare impurity term in (A1), and  \( \hat{H}_{ph} \)  is the acoustic phonon Hamiltonian, which we write as

 \[ \hat{H}_{p h}=\sum_{j}C_{\alpha\beta\gamma\delta}(\mathbf{r}_{j})u_{j}^{\alpha\beta}u_{j}^{\gamma\delta} \quad (A8) \] 

where the form of  \( C_{\alpha\beta\gamma\delta} \)  depends on the symmetry of the lattice.

## 2. TLS-phonon interactions and the random strain field

We now consider a system with a finite concentration of impurities/defects at random sites  \( \{r_{j}\} \) . The key point we address here is the way in which the random strain fields in the system then modify the interactions between the defects, and generate a new effective Hamiltonian (the one given in Eq.(1) of the main text).

The phonon-generated interaction between a pair of defects has been discussed in many papers  \( [28, 29] \) . The strength of the interactions  \( J^{ab} \)  (where a, b label either S or  \( \tau \) ) can be found microscopically from the direct phonon exchange between them  \( [28, 29] \) , 2nd-order in the defect-phonon interaction. One finds, for a pair of defects at sites i and j in an otherwise perfect crystal, that

 \[ J_{i j}^{a b}\sim\frac{f(\theta_{i j})\Gamma_{a}\Gamma_{b}}{\rho c^{2}R_{i j}^{3+\alpha}} \quad (A9) \] 

where  \( R_{ij} \)  is the inter-defect distance, and this formula is only valid for distances  \( \gg a_{o} \) , the lattice parameter. All of the very complicated angular dependence of these interactions [28, 29] is incorporated into the angular factor  \( f(\theta_{ij}) \) , where  \( \theta_{ij} \)  is the polar angle between the defects. The parameter  \( \alpha = 0, 1, 2 \) , for  \( \{ab\} = \{SS\}, \{S\tau\} \) , and  \( \{\tau, \tau\} \)  respectively; and we write  \( \Gamma_{S} = \Gamma \)  and  \( \Gamma_{\tau} = \zeta \) , where  \( \Gamma = |\Gamma_{n'}^{\alpha\beta}| \)  and  \( \zeta = |\zeta_{n}^{\alpha\beta\gamma}| \) , and we have suppressed the pair indices in these constants because we won't need them in what follows. We note that  \( J_{ij}^{S\tau} \)  and  \( J_{ij}^{\tau\tau} \)  fall off like  \( R_{ij}^{-4} \)  and  \( R_{ij}^{-\tau} \)  respectively, and so at long ranges can be neglected compared to  \( J_{ij}^{SS} \sim R_{ij}^{-3} \) . The more rapid fall-off occurs because the phonons couple to the  \( \tau \) -defects via the gradient of the phonon strain rather than the strain itself, adding extra powers of  \( 1/R_{ij} \)  to the interaction [28].

However, when we have a finite random concentration of defects, things change in two important ways, viz. (i) a set of random strain fields is generated [28] in the system, which has the effect of breaking the inversion symmetry randomly at each site - this radically modifies the coupling of the  \( \tau \) -spins to the phonons; and (ii) because of this, the strength of the interactions  \( J_{ij}^{S\tau} \)  and  \( J_{ij}^{\tau\tau} \)  is changed, and this is crucial for the universality.

To deal with this physics is quite subtle. In ref. [28], this was done by simply summing independently the random strain fields generated by each impurity. However, this is not quite correct, because as the strain fields increase in strength, they alter the defect-phonon coupling to the  \( \tau \) -defects themselves. Thus the results in ref. [28] are valid only in the regime where the concentration of defects  \( x \ll 1 \) , whereas here we are interested in strong disorder, where x is not small, and a new calculation is required.

The key to the physics in this strong disorder regime is to realize that we are dealing with a 3-body effect - we must recalculate the 2-defect interaction (A9) in the presence of a 3rd defect [41]. Without this 3rd defect, as we have seen, the effective  \( \tau_{i}^{z}S_{j}^{z} \)  interaction is  \( \propto 1/R^{4} \) . We thus recalculate the effective  \( \tau_{i}^{z}S_{j}^{z} \)  interaction, but now in third order in the defect-phonon coupling. We will also assume that the 3rd impurity k is close to impurity i. This is because (a) the  \( 1/R_{ik}^{4} \)  dependence of the interaction, and (b) the dependence of its sign, on the angle between sites i and k, means that such close '3rd party' configurations will dominate all sums over k, and the deviation from inversion symmetry at the  \( \tau \)  impurity.

We start again from the bare defect-phonon coupling in (A7), now written as a sum over defects, so that we have

 \[ \hat{V}=\sum_{\{j\}}\left[\eta_{j}u_{j}^{\alpha\alpha}+\Gamma_{j}^{\alpha\beta}u_{j}^{\alpha\beta}S_{j}^{z}+\zeta_{j}^{\alpha\beta\gamma}\partial_{\gamma}u_{j}^{\alpha\beta}\tau_{j}^{z}\right]. \quad (A10) \] 

where we have dropped the pair indices  \( n, n' \)  since they play no role in what follows. We write the Fourier transform of the lattice displacement field as

 \[ X_{\alpha}(x)=\frac{1}{\sqrt{N}}\sum_{q,\mu}X_{q\mu}\mathbf{e}_{q\mu,\alpha}e^{i q x} \quad (A11) \] 

where  \( e_{q,\mu,\alpha} \)  is a phonon polarization index. We then minimise the total potential energy, i.e. the sum of the bare phonon potential energy plus the interaction term above, to find the resulting distortion in the lattice[28]. This distortion is then found to be

 \[ \delta X_{\alpha}(x)=\frac{1}{2}\sum_{q\mu}(\delta X_{q\mu}\mathbf{e}_{q\mu\alpha}e^{i q x}+H.c.), \quad (A12) \] 

where we have
 

 \[ \delta X_{q\mu}=\frac{1}{\sqrt{N}M\omega_{q\mu}^{2}}\left(\sum_{\gamma,\delta,\eta}\zeta_{i}^{\gamma\delta\eta}\mathbf{e}_{q\mu\gamma}q_{\delta}q_{\mu}e^{-i q x_{i}}\tau_{i}^{z}+i\sum_{\alpha\beta}\gamma_{j}^{\alpha\beta}\mathbf{e}_{q\mu\alpha}q_{\beta}e^{-i q x_{j}}S_{j}^{z}\right). \quad (A13) \] 

and we have restored the sums over spin indices to make clearer what is being summed.

The effect of this distortion on the 3rd impurity k comes only from the phonon term (A8), which we write in terms of the lattice displacement as

 \[ \hat{H}_{p h}=\sum_{\rho\phi\chi\psi}C_{\rho\phi\chi\bar{\psi}}(\mathbf{r}_{k})\frac{\partial\delta X_{k\rho}}{\partial x_{k\phi}}\frac{\partial\delta X_{\kappa\chi}}{\partial x_{k\psi}} \quad (A14) \] 

where

 \[ \frac{\partial\delta X_{k\rho}}{\partial x_{k\phi}}=\sum_{q\mu}\frac{1}{N M\omega_{q\mu}^{2}}\left(\sum_{\gamma\delta\eta}\zeta_{i}^{\gamma\delta\eta}\mathbf{e}_{q\mu\gamma}q_{\delta}q_{\eta}\sin q(x_{k}-x_{i})\tau_{i}^{z}+\sum_{\alpha\beta}\gamma_{j}^{\alpha\beta}\mathbf{e}_{q\mu\alpha}q_{\beta}\cos q(x_{k}-x_{j})S_{j}^{z}\right)\mathbf{e}_{q\mu\rho}q_{\phi}. \quad (A15) \] 

We now evaluate the term in Eq.(A14) proportional to  \( \tau_{i}^{z}S_{j}^{z} \) , in order to find the change  \( \delta J_{ij}^{S\tau}(k) \)  in the  \( \tau_{i}^{z}S_{j}^{z} \)  interaction caused by the impurity at site k. Defining

 \[ A_{q\mu}\equiv\sum_{\gamma\delta\eta}\zeta_{i}^{\gamma\delta\eta}\mathbf{e}_{q\mu\gamma}q_{\delta}q_{\eta}\tau_{i}^{z} \quad (A16) \] 

 \[ D_{q\mu}\equiv\sum_{\alpha\beta}\Gamma_{j}^{\alpha\beta}\mathbf{e}_{q\mu\alpha}q_{\beta}S_{j}^{z}, \quad (A17) \] 

we find the shift in the  \( S\tau \)  interaction caused by the impurity at site k to be

 \[ \delta J_{i j}^{S\tau}(k)=2\sum_{\rho\phi\chi\psi}C_{\rho\phi\chi\bar{\psi}}(\mathbf{r}_{k})\sum_{q\mu}\frac{\mathbf{e}_{q\mu\rho}q_{\phi}}{N M\omega_{q\mu}^{2}}A_{q\mu}\sin\left[q(x_{k}-x_{i})\right]\sum_{q^{\prime}\mu^{\prime}}\frac{\mathbf{e}_{q^{\prime}\mu^{^{\prime}}\chi}q_{\psi}^{\prime}}{N M\omega_{q^{\prime}\mu^{\prime}}^{2}}D_{q^{\prime}\nu^{\prime}}\cos\left[q^{\prime}(x_{k}-x_{j})\right]. \quad (A18) \] 

In the acoustic approximation for the phonon spectrum we get, after similar integrations to those discussed in ref. \( [28] \) , the result

 \[ \delta J_{i j}^{S\tau}(k)=\frac{c_{i j}\zeta_{i}\Gamma_{j}C_{k}}{\rho^{2}c^{4}R_{i k}^{4}R_{j k}^{3}} \quad (A19) \] 

where  \( \zeta_{i}=|\zeta_{i}^{\alpha\beta\gamma}| \) , and similarly for  \( \Gamma_{j}, C_{k} \) , and all angular dependence has been absorbed in  \( c_{ij} \sim O(1) \) . This is a complicated function of angle, which depends on the position of the impurities and takes either sign. It can then be treated as a random variable.

Actually here the acoustic approximation is not valid, because it is easily seen, as stated above, that when we sum over all the different impurities at positions  \( r_{k} \)  to find the total change  \( \Delta J_{ij}^{S\tau} \)  in  \( J_{ij}^{S\bar{\tau}} \) , the dominant configurations will have  \( R_{ik} \approx a_{o} \) . However, since we are only interested in an estimate, we make the following assumptions:

(i) we assume a defect concentration x which is not small, which means that the probability that a defect, at some site i, will have a "3rd-party" defect on a neighbouring site  \( k \in x^{1/3} \) .
(ii) this implies that  \( R_{ik} \sim a_{o}x^{-1/3} \ll R_{jk} \) , and so we find

 \[ \Delta J_{i j}^{S\tau}\approx\frac{\gamma S\gamma_{\tau}}{\rho c^{2}R_{i j}^{3}} \quad (A20) \] 

where

 \[ \gamma_{\tau}\approx\frac{\bar{\zeta}\bar{C}x^{4/3}}{\rho c^{2}a_{o}^{4}}. \quad (A21) \] 

and where

 \[ \gamma_{S}\approx\bar{\Gamma}. \quad (A22) \] 

Here overbars on the various quantities indicate typical values.

Let us now estimate the magnitude of  \( \gamma_{\tau} \) . First,  \( \bar{C} \cdot (\delta a/a_{o})^{2} \approx \delta M\omega^{2}(\delta a)^{2} \) , where  \( \delta a \)  denotes a typical strain, and the latter expression is the difference in kinetic energy of the impurity compared to the host ion. Approximating  \( \delta M \approx M \)  and  \( \omega \approx c/a_{o} \)  we obtain  \( C \approx Mc^{2} \) , and thus we get  \( \gamma_{\tau} \approx x^{4/3}\zeta/a_{o} \) .
 

Let us now estimate  \( \bar{\zeta} \) . Since  \( \zeta \)  is the coefficient of the second derivative of the displacement (see Fig. 3), we have  \( \bar{\zeta} \cdot \delta a/a_{o}^{2} \approx E_{C} \cdot (\delta a/a_{o})^{2} \) , where  \( E_{C} \)  is the typical (Coulombic) electronic energy involved in charge displacement in the solid. Similarly,  \( \bar{\Gamma}\delta a/a_{o} \approx E_{C}\delta a/a_{O} \) , i.e.  \( \gamma_{S} \approx E_{C} \) . Thus, for  \( x \approx 1 \)  we find  \( \gamma_{\tau} \approx \gamma_{S}\delta a/a_{o} \) . The parameter  \( g \equiv \gamma_{\tau}/\gamma_{S} \approx \delta a/a_{o} \)  is the small parameter of our model. Since  \( E_{\Phi}/E_{C} \approx \delta a/a_{o} \) , where  \( E_{\Phi} \)  is the characteristic energy of elastic deformations in the solid (ie., roughly the Debye energy), we also have  \( g \sim E_{\Phi}/E_{C} \) .

Thus, in strongly disordered systems, deviations from inversion symmetry result in a finite interaction between the  \( \tau \) -TLSs and the phonon field, and the TLS-phonon interaction Hamiltonian is changed from Eq.(A10) to

 \[ \hat{V}_{d i s}=\sum_{\{j\}}\left[n_{j}u_{j}^{\alpha\alpha}+\Gamma_{j}^{\alpha\beta}u_{j}^{\alpha\beta}S_{j}^{z}+\gamma_{j}^{\alpha\beta}u_{j}^{\alpha\beta}\tau_{j}^{z}\right]. \quad (A23) \] 

with  \( |\gamma^{\alpha\beta}|\equiv\gamma_{\tau} \) , and  \( \gamma_{\tau}\approx g\gamma_{S} \) . This change in the form of the interaction Hamiltonian upon the introduction of disorder has been recently confirmed by molecular static calculations \( ^{[30]} \) . Starting from the interaction Hamiltonian in Eq.(A23), one readily obtains the effective Hamiltonian for the system of the form

 \[ \begin{align*}H_{S\tau}=&\sum_{j}[h_{j}^{S}S_{j}^{z}+h_{j}^{\tau}\tau_{j}^{z}]\\&+\sum_{ij}[J_{ij}^{SIS}S_{i}^{z}S_{j}^{z}+J_{ij}^{S\tau}S_{i}^{\tau}\tau_{j}^{z}+J_{ij}^{\tau\tau}\tau_{i}^{z}\tau_{j}^{z}]\end{align*} \quad (A24) \] 

where the interaction strengths  \( h_{a}, J_{ab} \) , are now random variables. If we write the size of the random couplings in terms of  \( R_{o} \sim a_{o}x^{-1/3} \) , the mean distance between the defects, one has

 \[ J_{ij}^{ab}=\frac{c_{ij}^{ab}\gamma_{a}\gamma_{b}}{\rho c^{2}(R_{ij}^{3}+\tilde{a}^{3})}\equiv J^{ab}\frac{R_{o}^{3}}{R_{ij}^{3}+\tilde{a}^{3}} \quad (A25) \] 

where again  \( c_{ij}^{ab} \sim O(1) \) , where we introduce  \( \tilde{a} \)  as a short distance cutoff for the interaction, and where

 \[ \begin{align*}J^{SS}&\sim J_{o}\equiv\frac{\gamma_{S}^{2}}{\rho c^{2}}\sim500K\\J^{S\tau}&\sim gJ_{o}\sim10K\quad;\quad J^{\tau\tau}\sim g^{2}J_{o}\sim0.2K\end{align*} \quad (A26) \] 

The numerical values for the energies assume typical values for the parameters in disordered insulators. The random fields are governed by the same parameters; their typical strengths are  \( h^{S} \lesssim J_{o} \)  and  \( h^{\tau} \lesssim g J_{o} \) , as was found earlier [28].

The value of  \( J_{o} \)  denotes the typical energy for an asymmetric excitation of a single impurity in the static lattice, whereas  \( gJ_{o} \)  denotes the typical energy for a symmetric excitation. Thus, the energy spectrum of a single impurity is as shown in Fig.1(c) in the main text. Our approximation here of suppressing the indices  \( n, n' \)  is equivalent to considering for each impurity the lowest two pairs of levels, which is justified at low temperatures.

The Hamiltonian (A24) is the one quoted in Eq. (1) of the main text. Its form was already discussed in Ref. \( [28] \) ; what is new here is the calculation of the renormalization of  \( J_{ij}^{S\tau} \)  by the disorder, using the 3-body technique described above.

## Appendix B: Densities of states for the interacting S- \( \tau \)  system

As discussed in the text, the interaction between the S and  \( \tau \)  pseudospins has a drastic effect on the densities of states of the excitations in the system. What we wish to do here is find the densities of states (DOS) for the S and  \( \tau \)  excitations.

## 1. DOS of  \( \tau \)  impurities

Let us start from the effective Hamiltonian in (A24), but for the moment ignore the random fields, and just work with the interaction terms. We begin with the mean field DOS introduced in the main text, viz., the S-defect DOS  \( n_{S}^{o}(E) \)  and the  \( \tau \) -defect DOS  \( n_{\tau}^{o}(E) \) , having widths  \( J_{o}, gJ_{o} \)  and peak heights  \( \propto 1/J_{o}, 1/gJ_{o} \) , respectively. Now we consider the effect on these two DOSs of the  \( S\tau \)  interaction  \( J^{S\tau} \) .

Consider first the effect exerted by the S spins on the  \( \tau \)  spins, neglecting the very small  \( \tau - \tau \)  interaction  \( J^{\tau\tau} \) . Following Efros and Shklovskii [31], we can argue that the new DOS is given by

 \[ \begin{align*}n_{\tau}(E)=&n_{\tau}^{o}(E)\prod_{j}\Theta(E+E_{S_{j}}-2U_{j})\\ \equiv&n_{\tau}^{o}(E)P_{\tau}(E).\end{align*} \quad (B1) \] 

which defines the reduction factor  \( P_{\tau}(E) \)  in the DOS; here we define  \( U_{j} \)  as the interaction between the given  \( \tau \)  spin and the j-th S spin, and  \( E_{S_{j}} \)  as the unperturbed energy of this S spin. We would like to show that there is no appreciable reduction of the  \( \tau \)  DOS by this interaction, at least outside a window which is exponentially small in g. We proceed by assuming a series of simplifying conditions, all leading to a reduction of  \( P_{\tau}(E) \)  below its actual value, and obtain our final result in form of an inequality.

We first overestimate  \( n_{S}(E)=1/J_{o} \)  for all  \( E<J_{o} \) , neglecting the reduced DOS at low energies. We then enumerate the S spins according to their distance from the  \( \tau \)  impurity. Since there are j impurities within a volume  \( (r_{j})^{3} \) , the maximum interaction of the given  \( \tau \)  TLS with the j'th S-TLS is given by  \( U_{j}^{max}=gJ_{o}/j \) . We assume that all interactions have this maximum value, taking the short distance cutoff to be  \( \tilde{a}=0 \)  and taking  \( c_{ij}^{S\tau}=1 \) . Under these assumptions, for a given E and a given j-th S-TLS we have  \( \Theta(E+E_{S_{j}}-2U_{j})=1 \)  if
 
![](./images/867747341635944606_10.jpg)

(a)

![](./images/867747341635944606_11.jpg)

(b)

FIG. 4: The true S-spin density of states  \( n_{S}(E) \) , as a function of energy for different short-distance behaviors of the interaction. Details are as in Figure 2 in the main text, only here x=0.5 and lattice size is  \( 13^{3} \)  cells (ie.,  \( \sim4400 \)  TLSs).

and only if  \( E_{S_{i}} > 2gJ_{o}/j - E \) , with a probability  \( 1 - (2gJ_{o}/j - E)/J_{o} \)  for  \( E < 2gJ_{o}/j \)  (i.e.  \( j < 2gJ_{o}/E \) ) and unity otherwise. Thus, for  \( E \ll gJ_{o} \)  we obtain

 \[ P_{\tau}(E)=\prod_{j}^{2g J_{o}/E}\left(1-\frac{2g J_{o}/\jmath-E}{J_{o}}\right). \quad (B2) \] 

Defining  \( \epsilon\equiv E/2gJ_{o} \)  we obtain

 \[ \begin{aligned}P_{\tau}(\epsilon)&=\prod_{j}^{1/\epsilon}\left[1-2g\left(\frac{1}{j}-\epsilon\right)\right]&>\\ >\prod_{j}^{1/\epsilon}\left(1-\frac{2g}{j}\right)&>\prod_{j}^{1/\epsilon}1/\left(1+\frac{4g}{j}\right).\end{aligned} \quad (B3) \] 

Multiplying the denominators, and expanding in a series in g, we see that

 \[ \prod_{j}^{1/\epsilon}\left(1+\frac{4g}{j}\right)<1+\sum_{k}(4g\ln1/\epsilon)^{k}. \quad (B4) \] 

and therefore

 \[ P_{\tau}(\epsilon)>1-4g\ln1/\epsilon. \quad (B5) \] 

i.e.  \( P_{\tau}(\epsilon) \approx 1 \)  for  \( \epsilon > \exp(-1/8g) \) .

Below we will argue that the S impurities are strongly gapped themselves, so that the above small correction at  \( g^{2}J_{o} < E_{\tau} < gJ_{o} \)  is probably an overestimate.

Now consider the effect on  \( n_{\tau}(E) \)  of the much weaker  \( \tau\tau \)  interactions. By repeating the same arguments as above, with  \( J_{o}^{SS} \equiv J_{o} \)  replaced by  \( J_{o}^{S\tau} \equiv gJ_{o} \)  and  \( J_{o}^{S\tau} \)  replaced by  \( J_{o}^{\tau\tau} \equiv g^{2}J_{o} \) . Then Eq.(B5) is thus reproduced as an inequality. However, since the  \( \tau \)  impurities are not strongly gapped, one can follow through the same line of arguments with  \( \approx \)  instead of  \( > \) , and conclude that there is a further reduction in the  \( \tau \) -spin DOS by a factor

 \[ \delta P_{\tau}(\epsilon^{\prime})\approx1-c\ln1/\epsilon^{\prime}. \quad (B6) \] 

where  \( \epsilon^{\prime}\equiv E/g^{2}J_{o} \)  and  \( c\approx g \) . Thus, the correction to the DOS appears at  \( E<g^{2}J_{o} \) , and is reduced by the small parameter g, which is the ratio between the  \( \tau-\tau \)  interaction and their energy disorder, and is also the relevant small parameter in our theory. Experimentally, the dipole gap is indeed seen at energy scales comparable to the  \( \tau-\tau \)  interactions[42], and its magnitude is indeed considerably reduced.

## 2. DOS of S impurities

The calculation of the DOS of the S impurities is more subtle, since there is no small parameter, and the result is of order unity. Furthermore, the correlation between the interaction and  \( \tau \)  energies is crucial, and must be taken into account. We therefore solve the problem using a numerical simulation. We begin by neglecting the  \( J^{\tau\tau} \)  in Eq. (1), since the values of  \( E_{\tau} \)  are dictated by the  \( J^{S\tau} \)  interaction. We are interested in the reduction of the S-TLSs resulting from the correlations with the  \( \tau \) -TLSs which we denote by  \( P_{S}(E) \)  and define by

 \[ \begin{align*}n_{S}(E)&=n_{S}(\bar{E})\prod_{j}\Theta(E+E_{\tau_{j}}-2U_{j})\\&\equiv n_{S}(\bar{E})P_{S}(E).\end{align*} \quad (B7) \] 

Here  \( \bar{E} \)  is an energy a few times larger than  \( T_{U} \)  and  \( U_{j} \)  is the interaction between a given S-TLS and  \( \tau_{j} \) . We therefore use the following algorithm:

We consider a three dimensional cubic lattice with a given size and concentration, and randomly distribute the impurities in the lattice. Each impurity has an S spin and a  \( \tau \)  spin. For a given  \( \bar{a} \) , the interaction is given by  \( U_{ij} = c_{ij} S_{i}^{z} \tau_{j}^{z} J_{0}^{S\tau} / (R_{ij}^{3} + \bar{a}^{3}) \) . We define  \( c_{ij}^{\prime} \equiv c_{ij} S_{i}^{z} \) .
 

where  \( c_{ij} \)  is chosen randomly from a Gaussian distribution of width unity and zero mean. We thus obtain  \( U_{ij} \)  and  \( E_{\tau_{j}} \equiv \sum_{i} U_{ij} \)  with their essential dependence, but with no reference to the spin configuration of the S TLSs. We then flip the  \( \tau \)  spins where  \( E_{\tau} < 0 \) , to have a positive excitation energy. The  \( U_{ij} \) 's are accordingly redefined. For each  \( S_{i} \)  we then calculate  \( E_{S_{i}}^{min} \) , the minimal E satisfying  \( \prod_{j} \Theta(E + E_{\tau_{j}} - 2U_{ij}) > 0 \) . We then obtain  \( P_{S}(E) = N(E_{S_{i}}^{min} < E)/N(S) \) , the ratio between the number of spins with  \( E_{S_{i}}^{min} < E \)  to the total number of spins. The results for x = 0.2 are given in Fig. 2 in the main text, and for x = 0.5 in Fig. 4.

## 3. random fields

In the derivation above we neglected the explicit random fields  \( h^{\tau}, h^{S} \) . This requires special attention when

[1] R. C. Zeller and R. O. Pohl, Phys. Rev. B 4, 2029 (1971).

[2] S. Hunklinger and A. K. Raychaudhuri, Prog. Low. Temp. Phys. 9, 265 (1986).

[3] R. O. Pohl, X. Liu, and E. Thompson, Rev. Mod. Phys. 74, 991 (2002).

[4] J. J. Freeman and A. C. Anderson, Phys. Rev. B 34, 5684 (1986).

[5] C. C. Yu and A. J. Leggett, Comments Cond. Mat. Phys. 14, 231 (1988).

[6] P. W. Anderson, B. I. Halperin, and C. M. Varma, Phil. Mag. 25, 1 (1972).

[7] W. A. Phillips, J. Low Temp. Phys. 7, 351 (1972).

[8] J. Jackle, Z. Phys. B 257, 212 (1972).

[9] M. W. Klein, B. Fischer, A. C. Anderson, and P. J. Anthony, Phys. Rev. B 18, 5887 (1978).

[10] J. P. Sethna and K. S. Chow, Phase Trans. 5, 317 (1985).

[11] M. P. Solf and M. W. Klein, Phys. Rev. B 49, 12703 (1994).

[12] D. A. Parshin, Phys. Rev. B 49, 9400 (1994).

[13] A. L. Burin, D. Natelson, D. D. Osheroff, and Y. Kagan, in Tunneling Systems in Amorphous and Crystalline Solids (ed Esquinazi P.) 223 (Springer, 1998).

[14] V. Lubchenko and P. G. Wolynes, Phys. Rev. Lett. 87, 195901 (2001).

[15] R. Kuhn, Europhys. Lett. 62, 313 (2003).

[16] D. A. Parshin, H. R. Schober, and V. L. Gurevich, Phys. Rev. B 76, 064206 (2007).

[17] M. Meissner et al., Phys. Rev. B 32, 6091(R) (1985).

[18] J. J. De Yoreo, W. Knaak, M. Meissner, and R. O. Pohl, Phys. Rev. B 34, 8828 (1986).

[19] S. K. Watson, Phys. Rev. Lett. 75, 1965 (1995).

[20] K. A. Topp, E. Thompson, and R. O. Pohl, Phys. Rev. B 60, 898 (1999).

[21] K. A. Topp and R. O. Pohl, Phys. Rev. B 66, 064204 (2002).

[22] X. Liu, P. D. Vu, R. O. Pohl, F. Schiettekatte, and S. Roorda, Phys. Rev. Lett. 81, 3171 (1998).

[23] R. O. Pohl, X. Liu, and R. S. Crandall, Current Opin. Sol. St. Mat. Sci. 4, 281 (1999).

[24] D. G. Cahill and R. O. Pohl, Phys. Rev. B 39, 10477

calculating the DOS,  \( n_{\tau}(E) \) ,  \( n_{S}(E) \) . In principle, the random fields add to the energies while keeping the interactions unchanged, thus making the two particle stability condition easier to fulfil, reducing the dipolar gap. Specifically, for  \( n_{\tau}(E) \)  our argument above follows through directly, and therefore the inequality in Eq. (B5) stays unchanged. For  \( n_{S}(E) \)  we have carried out the numerical calculations as described above in the presence of random fields  \( h^{\tau}/\langle E_{\tau}\rangle \approx 0.3 \)  and  \( h^{\tau}/\langle E_{\tau}\rangle \approx 1 \)  (where  \( \langle E_{\tau}\rangle \)  is the typical energy of a  \( \tau \)  TLS in the absence of a random field). The dipolar gap of the S TLSs indeed becomes smaller, for  \( h^{\tau}/\langle E_{\tau}\rangle \approx 1 \)  the results are changed only slightly, whereas for  \( h^{\tau}/\langle E_{\tau}\rangle \approx 0.3 \)  the quantitative change is appreciable, but the qualitative behavior is unchanged, as can be seen in Fig. 2 of the main text.

(1989).

[25] A. Gaita-Arino and M. Schechter, Phys. Rev. Lett. 107, 105504 (2011).

[26] A. Gaita-Arino, V. F. González-Albuixech, and M. Schechter, in preparation.

[27] Tunneling is neglected in the calculation of the energy biases for symmteric and asymmetric TLSs because it is much smaller than the typical bias induced by the strong disorder, see discussion in App. A 1.

[28] M. Schechter and P. C. E. Stamp, J. Phys.: Condens. Matter 20, 244136 (2008).

[29] J. L. Black and B. I. Halperin, Phys. Rev. B 16, 2879 (1977).

[30] A. Churkin, D. Barash, and M. Schechter, arXiv:1303.2955.

[31] A. L. Efros and B. I. Shklovskii, J. Phys. C 8, L49 (1975).

[32] A. Churkin, I. Gabdank, A. Burin, and M. Schechter, arXiv:1307.0868.

[33] A. Churkin, D. Barash, and M. Schechter, in preparation.

[34] A. K. Raychaudhuri and R. O. Pohl, Solid State Commun. 37, 105 (1980).

[35] P. Doussineau, M. Matecki, and W. Schön, J. Physique 44, 101 (1983).

[36] S. Rogge, D. Natelson, and D. D. Osheroff, Phys. Rev. Lett. 76 3136 (1996).

[37] M. M. J. Treacy and K. B. Borisenko, Science 335, 950 (2012).

[38] B. Golding and J. E. Graebner, Phys. Rev. Lett. 37, 852 (1976).

[39] B. Golding, M. v. Schickfus, S. Hunklinger, and K. Dransfeld, Phys. Rev. Lett. 43, 1817 (1979).

[40] P. Nagel, A. Fleischmann, S. Hunklinger, and C. Enss, Phys. Rev. Lett. 92, 245511 (2004).

[41] The idea to calculate the interactions in the presence of strong disorder in this manner came up in a discussion with A. Burin.

[42] D. J. Salvino, S. Rogge, B. Tigner, and D. D. Osheroff, Phys. Rev. Lett. 73, 268 (1994).
 
