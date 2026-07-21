
# Electronic structure and total energy of interstitial hydrogen in iron: Tight binding models

A. T. Paxton \( ^{1,2,3,*} \)  and C. Elsässer \( ^{1,2,\dagger} \) 

 \( ^{1} \) Fraunhofer Institut für Werkstoffmechanik IWM, Wöhlerstr. 11, 79108 Freiburg, Germany  
 \( ^{2} \) Karlsruher Institut für Technologie, Institut für Zuverlässigkeit von Bauteilen und Systemen (IZBS), Kaiserstr. 12, 76131 Karlsruhe, Germany  
 \( ^{3} \) Atomistic Simulation Centre, School of Mathematics and Physics, Queen's University Belfast, Belfast BT7 1NN, UK

An application of the tight binding approximation is presented for the description of electronic structure and interatomic force in magnetic iron, both pure and containing hydrogen impurities. We assess the simple canonical d-band description in comparison to a non orthogonal model including s and d bands. The transferability of our models is tested against known properties including the segregation energies of hydrogen to vacancies and to surfaces of iron. In many cases agreement is remarkably good, opening up the way to quantum mechanical atomistic simulation of the effects of hydrogen on mechanical properties.

PACS numbers: 71.20.Be 75.50.Bb 73.20.Hb 68.43.Fg

## I. INTRODUCTION

In this paper we demonstrate tight binding (TB) models for iron with and without interstitial hydrogen impurities at the concentrated and dilute limits. Although there is a large number of existing classical potentials which are certainly of great importance and usefulness, they all suffer from a particular drawback in that the underlying classical EAM-type models for pure Fe, with one apparent exception, \( ^{1} \)  fail to predict the known core structures of screw dislocations. \( ^{1,2} \)  On the other hand, tight binding models abstracted into bond order potentials correctly predict core structures in agreement with first principles calculations. \( ^{2} \)  Ultimately one of the many goals is to study how interstitials form atmospheres around dislocations and impede or enhance flow through mechanisms such as hydrogen enhanced local plasticity \( ^{3} \)  (HELP) and so it is essential that dislocation core structures are correctly predicted. A further slightly disturbing feature of the classical models is the truly vast number of parameters involved which have to be fitted to a very large training set of data. Here in common with the approach to classical model fitting, \( ^{1} \)  we first construct models for pure iron and then go on to make models for hydrides without further adjusting the Fe–Fe interaction parameters. But in contrast we try to keep the number of parameters and fitting targets to a minimum and focus on the ability of the models to predict those properties that are normally included in the training sets in the construction of classical potentials. We would argue that this is possible because the TB approximation comprises a correct quantum mechanical description of both magnetism and the metallic and covalent bond and so the correct physics is built in from the start. That being the case, we do not expect the theory to be over sensitive to the choice of parameters and indeed in the procedure we describe below a large number of equally useful models is thrown up.

The structure of this paper is as follows. In section II we revisit the tight binding approximation and discuss its parameters and their environment dependence, or screening. We describe two models for pure Fe in section III which are fitted to properties of bulk bcc  \( \alpha \) -Fe and used to predict properties of fcc  \( \gamma \) -Fe and hcp  \( \epsilon \) -Fe, as well as surface and vacancy formation energies in  \( \alpha \) -Fe. In section IV we augment one of these models with Fe–H interactions which we fit to the properties of four monohydride FeH phases, and test against adiabatic potential surfaces. We then proceed to the dilute limit of H in Fe in section V without further adjustment of parameters and use our model to predict segregation energies of H to interstitial sites, vacancies and surfaces of  \( \alpha \) -Fe. By and large, we find remarkable agreement with published experimental results and ab initio calculations. We discuss our models and conclude in section VI.

## II. THE TIGHT BINDING APPROXIMATION AND TRANSFERABILITY

## A. Distance scaling and range of the hopping integrals

There is no need to rehearse the tight binding approximation in any detail here. Recently Paxton and Finnis \( ^{4} \)  constructed tight binding models for magnetic Fe and Fe–Cr alloys and details can be found there as well as in many other publications. \( ^{5-9} \)  However we do wish to make some preliminary remarks. The scheme that we use is the self consistent Stoner model for itinerant ferromagnetism \( ^{8} \)  and goes beyond the fixed moment and rigid band approximations. The connection between tight binding theory and the first principles local spin density approximation (LSDA) to density functional theory (DFT) is now well established. \( ^{7,10,11} \)  TB is computationally several orders of magnitude faster than LSDA because the hamiltonian is constructed from a look-up table of parameterized hopping integrals, h, and possibly
 

FIG. 1. (color online) Energy bands for bcc Fe at its experimental lattice constant, 2.87 Å. The coloring is such that s character is green and d character is blue. The Fermi energy is indicated by a horizontal line. The upper panels are majority and the lower panels minority spin bands. Far left is the tight binding d-band model and in the center our non orthogonal sd model. To the right are bands calculated in the LSDA-GGA.

![](./images/867749575656473067_1.jpg)

![](./images/867749575656473067_2.jpg)

![](./images/867749575656473067_3.jpg)

![](./images/867749575656473067_4.jpg)

![](./images/867749575656473067_5.jpg)

![](./images/867749575656473067_6.jpg)

overlap integrals, s. These are conventionally written in Slater and Koster's notation \( ^{12} \)  as  \( ss\sigma \) ,  \( sd\sigma \) ,  \( dd\sigma \) ,  \( ddd\pi \) ,  \( ddb \) . Central to a tight binding model is the way in which these integrals scale with bond length. In this work we will use \( ^{4,13-15} \) 

 \[ h(r)=h_{0}\mathrm{e}^{-q r} \quad (1) \] 

and similarly for overlap integrals, when used,

 \[ s(r)=s_{0}\mathrm{e}^{-q r}. \quad (2) \] 

The alternative is to use the power law scaling,  \( h \sim r^{-n} \) , demanded by canonical band theory. \( ^{16-19} \)  There is no strong argument to prefer one over the other; in fact by equating \( ^{20} \)  logarithmic derivates of  \( h(r) \)  at, say first neighbors at a distance  \( r_{0} \) , we have  \( n = qr_{0} \)  and in the bcc structure of Fe  \( q \approx 1 \)  a.u. corresponds to the canonical n = 5 (see table I, below).

This brings us to a well known paradox of tight binding modeling namely that the decay of the hopping integrals is known a priori from band theory, which may render them longer ranged than is desirable. A well known example is the group IV semiconductors where by analogy with the free electron bands, to reproduce the volume dependence of the bandwidth the hopping integrals must scale with  \( n = 2.^{21} \)  This scaling is bound to lead to very long ranged hopping integrals; on the other hand it is known that the first neighbor approximation is the right one, and attempts to include further neighbors fail. \( ^{22} \)  For many purposes it is adequate simply to cut off the interactions between first and second neighbors, but this can lead to difficulties in work on complex defects or in molecular dynamics. An elegant solution was provided by Goodwin, Skinner, and Pettifor \( ^{23} \)  (GSP) which cuts off a power law exponentially beyond some chosen cut-off distance,  \( r_{c} \) . There are two drawbacks to this. (i) An exponential decay can still lead to discontinuities in molecular dynamics (as one still needs to impose a cut-off in the neighbor lists). (ii) The GSP form maintains the value but not the slope of the underlying power law at first neighbors. Therefore our preference is to retain the power or exponential scaling given by the canonical band theory and to choose two distances,  \( r_{1} \)  and  \( r_{c} \) , between which to smoothly augment the interaction to zero. This can be achieved by matching value, slope and curvature at  \( r_{1} \)  and at  \( r_{c} \)  with a fifth degree polynomial which replaces
 

the hopping integral in that range. \( ^{24} \)  We show our hopping integrals thus augmented at figure 8 in section IV below, where we discuss this matter further.

## B. The pair potential, transferability, and non-orthogonality

The hopping integrals provide an attractive force, which in the conventional tight binding models is balanced by a repulsive pair potential, which here may take the form

 \[ \phi(r)=B_{1}\mathrm{e}^{-p_{1}r}-B_{2}\mathrm{e}^{-p2r} \quad (3) \] 

in which, as suggested by Liu et al. \( ^{8} \) , both  \( B_{1} \)  and  \( B_{2} \)  are positive. This potential is expected to be repulsive at short range but is not positive for all r (see Fig. 4, below).

An additional non pairwise repulsion is provided if it is chosen to make the model basis non orthogonal. This may give a number of advantages. \( ^{4} \)  One is, that it is widely believed that non orthogonality confers a greater transferability to the model. \( ^{25} \)  By this is meant that a model constructed for a particular crystal structure is less likely to fail when transferred into a situation of different crystal structure or increased or reduced coordination. We will wish to focus critically on this aspect of our models below. It is instructive at this stage to recall that by its very construction the tight binding approximation discards all three center terms in the hamiltonian. \( ^{9} \)  On the one hand the canonical band theory shows that these, like non orthogonality, are of second order in the band width. \( ^{19,26,27} \)  On the other hand Tang et al. \( ^{28} \)  and Haas et al. \( ^{29} \)  took the important step of proposing environment dependent hopping integrals. In this empirical scheme the hopping integral between two atoms is modified in the close proximity of a third atom—in the extreme limit this third atom may approach the two center bond, generally speaking weakening or “screening” it, and eventually come in between the two atoms. Whereas the screening was first described by an empirical formula, Pettifor succeeded in deriving the Tang et al. \( ^{28} \)  expression from the Löwdin transformation of the non orthogonal hamiltonian. \( ^{30} \)  In particular he showed that sd overlap matrix elements in pure transition metals provide this “screening” of the two center bond. Therefore rather than adopting explicit environment dependence as is done in recent bond order potentials, \( ^{31,32} \)  we retain the two center approximation and employ non orthogonal models to account for the screening.

## C. The choice of parameters

A related and highly significant finding \( ^{30} \)  is that hopping integrals extracted from an LSDA hamiltonian calculated using the tight binding LMTO-ASA method \( ^{27} \)  are discontinuous between first and second neighbors in bcc transition metals. These discontinuities are described consequently by the screening—a feature of the geometry of the bcc lattice—leading to the analytic form of Tang et al. \( ^{28} \)  and Haas et al. \( ^{29} \)  The point we wish to raise here is that it became clear \( ^{30} \)  that transferable hopping integrals may be extracted from an LSDA hamiltonian thus avoiding the usual need for fitting. \( ^{9,30} \)  Of course there is no unique tight binding model for a given element since the LSDA hamiltonian is basis-set dependent. We do not adopt this approach here for two reasons. First, the hopping integrals deduced from the LMTO-ASA \( ^{9,30} \)  derive from a hamiltonian whose on-site matrix elements are strongly volume dependent whereas in the tight binding approximation these terms are volume independent and hence any volume dependence of the electronic structure must be taken up by the scaling law (1). Second, if the hopping integrals and their scaling are taken from ab initio bandstructures without permitting further adjustment, then essential properties such as elastic constants, lattice constants and structural energy differences may have to rely on the choice of pair potential placing a large burden on that part of the model which is the most ad hoc.

## III. MODELS OF PURE IRON

## A. Orthogonal d, and non orthogonal sd models

Construction of a tight binding model for transition metals is quite straight forward if it is not required to take the parameters from first principles bandstructure calculations. \( ^{4} \)  Given that the scaling should be close to canonical, as should the ratios, \( ^{19} \) 

 \[ d d\sigma:d d\pi:d d\delta\approx-6:4:-1 \] 

it is simple enough to guess a set of hamiltonian and overlap matrix elements and adjust these until the resulting energy bands match reasonably closely those from the LSDA. In fact, in all that follows we have used the LSDA with a generalized gradient correction (GGA) of Perdew et al. \( ^{33} \)  With the exception of data taken from the literature all our LSDA-GGA results are calculated using the full potential LMTO method. \( ^{34} \)  Energy bands calculated in this way are shown on the right in Fig. 1. A simple canonical d-band model produces the bands shown to the left of Fig. 1. In addition to the integrals already discussed, we require a Stoner parameter, I, which represents an on-site Coulomb integral, \( ^{4,6} \)  to achieve a splitting of the up and down spins. \( ^{4,8} \)  Furthermore since the canonical model omits the s-band which is occupied by roughly one electron \( ^{19} \)  it is necessary to fix a number of d electrons,  \( N_{d} \) . \( ^{8,15} \)  This is both the most simple and most reliable model for transition metals. \( ^{6,35-37} \)  Nevertheless for the present purposes we wish to extend this
 

TABLE I. Parameters of our tight binding models for pure Fe. The  \( \{h\} \)  and  \( \{s\} \)  are the  \( h_{0} \)  and  \( s_{0} \)  of equations (1) and (2). All quantities are given in atomic Rydberg units (1 bohr = 0.529 Å, 1 Ry = 13.61 eV). Note that in the minimal basis, orthogonal d model, the number of d-electrons,  \( N_{d} \)  is a parameter. \( ^{8} \)  Both hopping integrals and pair potentials are smoothly cut off between distances  \( r_{1} \)  and  \( r_{c} \) . These are shown in units of the bcc lattice constant, a. Both pair potentials are cut off with  \( r_{1} = 1.1 \)  and  \( r_{c} = 1.4 \) , that is, between second and third neighbors of the bcc lattice (see Fig. 4 below). By expressing  \( r_{1} \)  and  \( r_{c} \)  in units of a we imply that these scale with the lattice constant, for example in the calculation of the bulk modulus, so that in a perfect lattice first and second neighbors always see the “proper” pair potential (3) and hopping integrals. This also applies below (Fig. 6) to energy–volume curves in FeH, both for first and second bcc neighbors and first fcc neighbours.

<table><tr><td>model</td><td colspan="3">orthogonal d</td><td colspan="3">{</td></tr></table>

model. In the interests of transferability and to account for the bond screening without explicit environment dependent bond integrals, we explore here the addition of an s-orbital to the basis, including  \( sd\sigma \)  and  \( ss\sigma \)  non-orthogonality. We will also give arguments for this necessity when we come to the iron hydrides below. The resulting bands, again obtained by simple comparison by eye with the LSDA-GGA bands are shown in Fig. 1. Densities of states associated with the LSDA-GGA and tight binding models are shown in Fig. 2.

Having obtained two sets of bond integrals, we proceed to find parameters of the pair potential and we do this by adjusting the four parameters in (3) to the lattice constant and the three elastic constants of bcc Fe. This cannot be done exactly because of the restricted form of the pair potential. The parameter sets are given in table I and resulting properties are in good agreement with experiment or LSDA-GGA calculations as can be seen in table II. Calculations, written in italics in table II, have been done using the full potential LMTO FIG. 2. Densities of states of pure bcc Fe in the orthogonal d (a) and non-orthogonal sd (b) tight binding models compared to the LSDA-GGA (c). Majority and minority spin states are shown in the upper and lower panels of each. The zero of energy is shifted to the Fermi energy.

![](./images/867749575656473067_7.jpg)

method \( ^{34} \)  and elastic constants are all obtained at the theoretical lattice constants. Our calculated lattice and elastic constants are in general agreement with previous work. \( ^{43} \) 

## B. Predictions of the models

## 1. Magnetic moment and structural magnetic energy differences

It should be noted that the two models we have described are rather intuitively obtained and so, apart from the pair potential it cannot be said that these are “fitted” in the sense of a classical potential. Hence the properties shown in table II are in essence predictions of the model, validating the underlying correctness of the tight binding theory. These predictions can be discussed in more detail by reference to Fig. 3 which shows the structural energy–volume relation in bcc and hcp Fe broken down into bandstructure energy and magnetic energy contributions. \( ^{4} \)  Both models reproduce the essential features which are, (i) the rapid collapse of the hcp magnetic moment under pressure; (ii) the slow decline of the bcc moment and (iii) the stabilization of bcc over hcp being a result of the magnetism. The role of the pair poten-
 

FIG. 3. (color online) Contributions to the energy–volume relation in the orthogonal d (left) and non orthogonal sd (right) tight binding models. The lower panel shows the volume dependence of the magnetic moment. The dotted lines refer to the hcp crystal structure and show the rapid collapse of the moment under pressure. The solid line is the bcc moment and may be compared with the circles which are LSDA-GGA calculations. The upper panel shows the bandstructure energy (blue) and the magnetic energy (green) and their sum in red. Solid lines refer to bcc and dotted lines to hcp. The pair potential energy favors bcc in both models. A vertical line indicates the equilibrium volume in bcc Fe.

![](./images/867749575656473067_8.jpg)

![](./images/867749575656473067_9.jpg)

tial warrants explanation here. Fig. 4 shows equation (3) plotted using the parameters of our two models from table I. It might well be supposed that the stability of the bcc phase compared to the hcp is an artefact of the negative region of  \( \phi(r) \)  falling at the second neighbors of the bcc structure, while the 12 hcp nearest neighbor distances fall in a positive region. This would be a valid criticism of our and Liu et al.'s \( ^{8} \)  models but is misleading. In fact we find that we can easily make models that stabilize bcc employing a pair potential that is positive everywhere. In addition the stabilisation of the bcc structure can be amplified by choosing larger Stoner I parameter. We allow a larger moment in our orthogonal d model since it is known that the magnetic moment in bcc Fe would be closer to  \( 2.6\mu_{B} \)  in the absence of sd and pd hybridization. \( ^{44,45} \)  Therefore the LSDA-GGA bcc–hcp energy difference is better rendered in that model (table II) whereas we have chosen a value of I in our non orthogonal sd model that strikes a compromise between a smaller bcc–hcp energy difference having the benefit of a magnetic moment closer to the observed value. The real benefit of the form (3) is that it enables a sufficiently large value of the elastic constant  \( C' \)  which otherwise appears too small. It is well known that  \( C' \)  can become very soft in bcc metals and the values we obtain in table II are the best we can achieve after many trials with the other parameters and scalings in the models. Indeed in the model of Liu et al. \( ^{8} \) ,  \( C' \)  is significantly lower than ours.

The only solution we know of to fit the elastic constants exactly is to employ a spline form for the pair potential as is done in the fitting of bond order potentials, \( ^{24,31,32} \)  and we are rather reluctant to make such a departure from physical intuition.

## 2. fcc γ-Fe

Because our models were fitted to the bcc Fe lattice and elastic constants, it is important to focus on the lower part of table II which deals with the fcc phase of Fe. This is  \( \gamma \) -Fe which is the base for the austenitic steels and the crystal structure adopted by pure Fe above  \( 1185^{\circ} \) K. \( ^{46} \)  It is well known \( ^{47-50} \)  that  \( \gamma \) -Fe exists in a high spin ferromagnetic and a low spin (approximately non magnetic) modification and we show predictions for both phases in table II which we compare with LSDA-GGA calculations and experimental observations. It is a mark of transferability that both models give a good account of each of the two fcc phases. Neither model fully captures the large and negative  \( C' \)  or the softening of  \( c_{44} \)  of the LSDA-GGA in the high spin phase; although they are in better accord with experiment than the LSDA-GGA, the proper comparison is with the  \( 0^{\circ} \) K calculations. The elastic softening in  \( \gamma \) -Fe is consistent with the measured temperature dependence of  \( C' \)  in the Invar alloys, \( ^{51} \)  therefore it is encouraging that our models are able to describe this
 

TABLE II. Calculated properties using parameters from table I. They are compared in the right hand column to either experimental values or values calculated using LSDA-GGA, the latter written in italics. A proper comparison of the cohesive energy,  \( E_{coh} \) , with experiment should take account of the spin polarization energy of the free atom which is absent in the tight binding limit of infinite separation; this energy is as much as \( ^{38} \)  0.32 Ry so that the calculated  \( E_{coh} \)  should amount to 0.63 Ry. Hence the apparent better agreement of the orthogonal d model is misleading. Both ferromagnetic (FM) and non magnetic (NM) fcc Fe is included; we compare the experimental data to the FM calculations: the lattice constant is extrapolated to  \( 0^{\circ}K \) ; \( ^{39} \)  the elastic constants are taken from phonon dispersion curves \( ^{40} \)  measured at  \( 1428^{\circ}K \)  which is above the Curie temperature ( \( 1043^{\circ}K \) ) although local moments are expected to persist. \( ^{41} \)  LSDA-GGA NM values in parentheses refer to the low spin phase.

<table><tr><td></td><td></td><td>d</td><td>sd</td><td></td></tr><tr><td>bcc</td><td>a ( \( \textup{\AA} \) )</td><td>2.87</td><td>2.87</td><td>\( 2.87, 2.84 \)</td></tr><tr><td>bcc</td><td>K (GPa)</td><td>175</td><td>184</td><td>\( 170, 173 \)</td></tr><tr><td>bcc</td><td>C&#x27; (GPa)</td><td>48</td><td>43</td><td>\( 52, 62 \)</td></tr><tr><td>bcc</td><td>c_{44} (GPa)</td><td>118</td><td>108</td><td>\( 121, 109 \)</td></tr><tr><td>bcc</td><td>moment ( \( \mu_{B} \) )</td><td>2.7</td><td>2.2</td><td>\( 2.2 \)</td></tr><tr><td>bcc</td><td>E_{coh} (Ry)</td><td>0.36</td><td>0.51</td><td>0.31</td></tr><tr><td>hcp</td><td>a ( \( \textup{\AA} \) )</td><td>2.54</td><td>2.51</td><td>\( 2.54 \)</td></tr><tr><td>hcp</td><td>K (GPa)</td><td>164</td><td>171</td><td>\( 160 \)</td></tr><tr><td>hcp</td><td>moment ( \( \mu_{B} \) )</td><td>2.4</td><td>1.8</td><td>\( 2.4 \)</td></tr><tr><td>hcp</td><td>E_{mag} (mRy)</td><td>7.7</td><td>4.6</td><td>\( 7.7 \)</td></tr><tr><td>\( \Delta E_{coh} \)  hcp-bcc (mRy)</td><td>12</td><td>3</td><td>15</td><td></td></tr><tr><td>fcc (FM)</td><td>a ( \( \textup{\AA} \) )</td><td>3.68</td><td>3.60</td><td>\( 3.55, 3.64 \)</td></tr><tr><td>fcc (FM)</td><td>K (GPa)</td><td>223</td><td>187</td><td>\( 133, 191 \)</td></tr><tr><td>fcc (FM)</td><td>C&#x27; (GPa)</td><td>13</td><td>12</td><td>\( 16, -88 \)</td></tr><tr><td>fcc (FM)</td><td>c_{44} (GPa)</td><td>79</td><td>74</td><td>\( 77, 13 \)</td></tr><tr><td>fcc (NM)</td><td>a ( \( \textup{\AA} \) )</td><td>3.45</td><td>3.51</td><td>\( 3.46 (3.45) \)</td></tr><tr><td>fcc (NM)</td><td>K (GPa)</td><td>358</td><td>232</td><td>\( 294 (294) \)</td></tr><tr><td>fcc (NM)</td><td>C&#x27; (GPa)</td><td>96</td><td>72</td><td>\( 102 (102) \)</td></tr><tr><td>fcc (NM)</td><td>c_{44} (GPa)</td><td>227</td><td>151</td><td>\( 250 (249) \)</td></tr></table>

 \( ^{a} \)  from data extrapolated from  \( 3^{\circ} \) K to  \( 0^{\circ} \) K by Adams et al. \( ^{42} \) 

 \( ^{b} \)  Reference [39]

 \( ^{c} \)  Reference [40]

important physical phenomenon at least in principle. It has already been shown that elastic and phonon softening with increasing temperature in  \( \alpha \) -Fe is captured in the tight binding approximation. \( ^{52,53} \) 

## 3. Surface energies

The proper test of transferability is to carry the models into situations of over or under coordination. Here, we do this by addressing the surface energies of pure Fe. We have set up the (110), (001) and (111) surfaces of bcc Fe and relaxed the atom positions by energy minimization using the Hellmann–Feynman forces. \( ^{8,9,55} \)  The resulting energies are shown in table III in order of decreasing coordination, the most close packed surface being (110). We achieve modest, but satisfactory agreement with published LSDA-GGA calculations \( ^{54} \)  at least for the two most close packed surfaces. It is in fact notable that the LSDA-GGA predicts all the surfaces to have nearly the same energy with (111) being a little higher. This is not reflected in the tight binding models, indicating limits to their transferability. The orthogonal d model gives the greater spread in energies, demonstrating to some extent the greater transferability afforded by the inclusion of an s orbital. It is gratifying that both models give a qualitative account of surface energies without having been fitted, at least in the case of the (110) and (001) the latter being of most importance as it's the usual cleavage

![](./images/867749575656473067_10.jpg)

TABLE III. Calculated surface energies in J/m². Values in parentheses are for truncated bulk (unrelaxed) surfaces. LSDA-GGA calculations are taken from Spencer et al.⁵⁴

<table><tr><td>model</td><td>orthogonal  \( d \)</td><td>non orthogonal  \( sd \)</td><td>GGA</td></tr><tr><td>(110)</td><td>1.77 (1.77)</td><td>1.53 (1.56)</td><td>2.27 (2.27)</td></tr><tr><td>(001)</td><td>2.12 (2.15)</td><td>1.74 (1.79)</td><td>2.29 (2.32)</td></tr><tr><td>(111)</td><td>3.54 (3.85)</td><td>2.80 (3.34)</td><td>2.52 (2.62)</td></tr></table>
 

TABLE IV. Vacancy formation energy,  \( E_{v}^{f} \) , in eV, of pure Fe, calculated with the orthogonal d and non-orthogonal sd tight binding models and compared to published LSDA-GGA and experimental results.

<table><tr><td>model</td><td>d</td><td>sd</td><td>LSDA-GGA</td><td>expt.</td></tr><tr><td>relaxed</td><td>2.39</td><td>1.33</td><td>1.95, a 2.18b</td><td>1.61-1.75, d 1.59g</td></tr><tr><td></td><td></td><td></td><td>2.09c</td><td>2.0 ± 0.2f</td></tr><tr><td>unrelaxed</td><td>2.42</td><td>1.36</td><td>2.24, a 2.60b</td><td></td></tr></table>

 \( ^{a} \)  Reference [60]

 \( ^{b} \)  Reference [61]

 \( ^{c} \)  Reference [62]

 \( ^{d} \)  Muon spin rotation, \( ^{63,64} \) 

 \( ^{e} \)  Quenching-in and electrical resisitivity \( ^{64,65} \) 

 \( ^{f} \)  Positron annihilation, \( ^{66} \)  but Seeger \( ^{64} \)  asserts that  \( E_{v}^{f} \lessapprox 1.85 \)  eV

face. \( ^{46,56,57} \)  It is also significant in the present context that the effect of H on pure Fe and Fe–Si is to enable cleavage also on the (110) planes. \( ^{58} \) 

## 4. Vacancy formation energy

A further test of the transferability is to predict the formation energy of a vacancy. We do this by constructing 54 and 53 atom “supercells” of bcc Fe  \( (3\times3\times3 \)  cubic two-atom unit cells), one of which has an atom missing. The structure is relaxed by energy minimization; its resulting total energy is denoted  \( E(\mathrm{Fe}_{53}) \) . The energy of the 54 atom supercell is denoted  \( E(\mathrm{Fe}_{54}) \) . Then the vacancy formation energy, neglecting volume relaxation, is \( ^{59} \) 

 \[ E_{v}^{f}=E(\mathrm{Fe}_{53})-\frac{53}{54}E(\mathrm{Fe_{54}}). \] 

Our results are shown in table IV which also gives values for the “unrelaxed” vacancy. As for the surface energies,  \( E_{v}^{f} \)  is underestimated by the non orthogonal sd model and overestimated by the orthogonal d model. The likely error compared to experiment in the latter however is more than twice that of the non orthogonal sd model, again demonstrating some benefit in transferability of including the non orthogonal s-orbitals.

## IV. ADDING Fe–H INTERACTIONS

As emphasized before, we will keep the parameters of pure Fe unchanged as we seek a model for H in Fe. We will find such a model by comparison with properties of iron monohydrides of stoichiometry FeH, that is, the concentrated limit and then test our model's transferability into the dilute limit.

In a series of three papers, \( ^{[50,68,69]} \)  Elsässer et al. have made a comprehensive study of the compound FeH in the framework of density functional theory. One is interested in four putative phases, namely fcc and bcc Fe. (color online) To illustrate the tetrahedral (T) and octahedral (O) interstices in the bcc (upper figure) and fcc (lower figure) crystals. Note that in the bcc lattice the octahedral site is at the center of a distorted octahedron, unlike the fcc where it is regular. The distance to the two apical atoms, shown here as a horizontal bond, is shorter by a factor  \( 1/\sqrt{2} \)  than the distances to the equatorial atoms, two of which are shown here in the upper face. This leads in general to the well-known tetragonal distortion of the bcc lattice near octahedral interstitial atoms, for example in martensite. For details see refs [46 and 67]. Neither is the tetrahedral interstitial site in the bcc lattice regular—indeed both octahedral and tetrahedral bcc interstices have tetragonal symmetry. The fcc crystal structure with all the octahedral sites occupied becomes that of cubic rocksalt adopted by many transition metal carbides and nitrides. In fcc, the tetrahedral site is regular; when half these sites are occupied the resulting crystal structure is that of zincblende.

![](./images/867749575656473067_11.jpg)

![](./images/867749575656473067_12.jpg)

each having one H atom in either tetrahedral or octahedral sites. These are illustrated in Fig. 5; and Fig. 6 shows energy–volume curves for these four phases calculated using LSDA-GGA in the full potential LMTO method \( ^{34} \)  (see also Fig. 5 in ref [50]).

Examination of the upper sketch in Fig. 5 shows that the displacement of the tetrahedral interstitial atom in the bcc structure towards the octahedral site brings the impurity atom from above the second neighbor bond, at right angles until it finally rests at the bond center. This is precisely the situation envisaged by Haas et al. \( ^{29} \)  in their proposal of the screening function, and we therefore expect for a model to be transferable, we will require it to be non-orthogonal. There is also a strong argument for the retention of the Fe 4s orbital even though, as we have seen, it does not lead to a significantly better model for pure Fe than the orthogonal d. \( ^{15} \)  The argument for its inclusion follows from an examination of Fig. 7 which shows LSDA-GGA energy bands for bcc tetrahedral FeH. The bands are colored according to the eigenvector weights
 

FIG. 6. (color online) Cohesive energy and magnetic moment as a function of volume per Fe atom in the four FeH phases calculated within the LSDA-GGA (left). Dotted lines denote non magnetic phases. The cohesive energy is with respect to solid  \( \alpha \) -Fe and molecular  \( H_{2} \)  also calculated using the same energy functional and hence is an approximation to the heat of formation. Note that on this basis none of the phases is expected to exist. On the right we show the same quantities calculated in the non-orthogonal sd tight binding model. We expect that the almost exact degeneracy of bcc TET and fcc TET is accidental.

![](./images/867749575656473067_13.jpg)

![](./images/867749575656473067_14.jpg)

coming from LMTO's from H 1s (red) or Fe 3d (blue). The H 1s band is split off from the Fe 3d bands and has similar width. The Fe 4s band which in pure Fe has its bottom below the Fe 3d bands and which hybridizes with them (see Fig. 1) is pushed up above the top of the Fe 3d bands by repulsion of the H 1s band. This means that the Fermi energy remains near where it is in pure Fe. Roughly speaking one might say that the single 4s electron per atom in pure Fe is transferred to the hydrogen atom to complete its 1s shell, or rather to fill the H 1s band. At first glance it may seem natural to neglect the Fe 4s bands in FeH. But a difficulty will arise if we adapt a d-only model by adding just an extra H 1s orbital. Hydrogen brings one electron with it and to fill the split-off H 1s band an electron will be drawn down from the Fe 3d bands consequently lowering the Fermi level. If we were only interested in FeH then we could just adjust  \( N_{d} \) , the number of d electrons; but this will introduce an inconsistency in going to the dilute limit:  \( N_{d} \)  will somehow need to be continuously adjusted at Fe atoms successively further away from an impurity H. It is very hard to see how this problem could be overcome except possibly by allotting two electrons to the hydrogen impurity; while it is solved naturally by the Fe 4s falling back into place as an Fe atom finds itself remote from the influence of impurity. We emphasize that in the non-orthogonal sd model and its extension to impurities the number of electrons is not a parameter—as long as all occupied bands are included in the hamiltonian we can happily take the number of electrons from the periodic table.

Therefore we take over the pure Fe non-orthogonal sd model and we add parameters to account for the additional H s band. We need Fe-H sd \( \sigma \)  and ss \( \sigma \)  hopping and overlap parameters but we do not require H-H interaction parameters since even the closest approaching interstitial sites are distant more than three times the length of the H \( _{2} \)  molecular bond. The sd \( \sigma \)  and ss \( \sigma \)  integrals establish the width of the H s band while its position with respect to the d bands is set by the on-site energy,  \( \varepsilon_{s} \)  of the H s orbital. We also require Hubbard-
 

FIG. 7. (color online) Energy bands for bcc tetrahedral FeH, calculated at the lattice constant of pure bcc Fe. The upper panels show majority and the lower minority spin states. The coloring is such that H-s character is red and Fe-d character is blue. Fe-s bands are green. The Fermi energy is indicated by a horizontal line. Note that the Fe-4s band has been pushed above the d-bands. Bands on the left are from our tight binding model and on the right are bands calculated in the LSDA-GGA.

![](./images/867749575656473067_15.jpg)

![](./images/867749575656473067_16.jpg)

![](./images/867749575656473067_17.jpg)

![](./images/867749575656473067_18.jpg)

U parameters \( ^{7,70} \)  for H and Fe, but these are not critical and 1.2 Ry and 1 Ry are good choices. Essentially these lead to approximate charge neutrality as expected in metals and their alloys. \( ^{37} \)  For simplicity we take the Stoner parameter for H to be zero. Tetrahedral bcc FeH is ferrimagnetic, both in LSDA and in our tight binding model, the H atom carrying a small moment, less than  \( 1 \mu_{B} \)  (aligned opposite to that of the Fe atom cf., Fig. 8 in ref [50]).

To find the additional parameters we have resorted to fitting these to the four equilibrium atomic volumes and three cohesive energy differences marked with dashed lines on Fig. 6. We do this using Schwefel's multimembered evolution strategy. \( ^{71,72} \)  For the Fe–H pair potential we employ

 \[ \phi(r)=\frac{B}{r}\mathrm{e}^{-p r}. \] 

The resulting parameters are displayed in table V and the hopping integrals are shown graphically in Fig. 8 to illustrate their relative magnitudes and ranges. In the same figure we show the hopping integrals for Fe which are, of course, identical to those of our non orthogonal sd

TABLE V. H on-site, and Fe–H interaction parameters of our tight binding model. All quantities are given in atomic Rydberg units. For all these integrals we use  \( r_{1}=0.8 \)  and  \( r_{c}=2 \)  in units of the pure Fe bcc lattice constant,  \( a=2.87\ \AA \) ; for the pair potential we use  \( r_{1}=0.8 \)  and  \( r_{c}=0.95 \)  in the same units.

<table><tr><td>\( \varepsilon_{s}-\varepsilon_{d} \)</td><td>-0.085</td></tr><tr><td>\( U_{\text{Fe}} \)</td><td>1.0</td></tr><tr><td>\( U_{\text{H}} \)</td><td>1.2</td></tr><tr><td></td><td>q</td></tr><tr><td>\( h_{ss} \)</td><td>-0.35</td></tr><tr><td>\( h_{sd} \)</td><td>-0.14</td></tr><tr><td>\( s_{ss} \)</td><td>0.27</td></tr><tr><td>\( ss_{d} \)</td><td>0,22</td></tr><tr><td>B</td><td>299.6</td></tr><tr><td>p</td><td>2.6922</td></tr></table>
 

FIG. 8. (color online) Hopping and overlap integrals as functions of bond length, r, in the sd non orthogonal model. Except in the case of  \( dd\delta \)  the dotted lines are the overlap integrals corresponding to the hopping integrals of the same color. Vertical dotted lines indicate the Fe–H bond length in bcc tetrahedral FeH at equilibrium volume, and the Fe–Fe bond lengths of the first six neighbors in pure bcc Fe.

![](./images/867749575656473067_19.jpg)

model of section III. With reference to our remarks in section II A we note that all our hopping and overlap integrals have the simple exponential form up to the distance  \( r_{1} \)  beyond which they are augmented so as to go continuously and differentiably to zero at  \( r_{c} \) . These distances are not strictly parameters of the model and are not used in the fitting. They are chosen intuitively; for example one expects just first neighbors in hcp and fcc, and first plus second neighbors in the bcc structures to be interacting through dd hopping whereas the s electrons in pure Fe are essentially free electron like and hence “do not take kindly to being treated within a TB framework”. \( ^{19} \)  They are best represented by longer ranged interactions. These points are illustrated in Fig. 8 and the values of  \( r_{1} \)  and  \( r_{c} \)  can be found in tables I and V. The use of fifth degree polynomials to augment the tails is necessary to achieve a smooth join; it can lead to small kinks as seen in Fig. 8, but these are designed to fall in between neighbor shells and so minimize their effect. This is why the parameters  \( r_{0} \)  and  \( r_{c} \)  are made to scale with the lattice constant. The resulting energy bands are plotted in Fig. 7 for comparison with the LSDA-GGA bands. The resulting energy volume curves are shown in Fig. 6. The TB model does not reproduce the magnetic moments of the LSDA-GGA in Fig. 6 quantitatively since this is a sensitive function of the density of states at the Fermi level in the non magnetic crystal and our energy bands are only in qualitative agreement with the LSDA-GGA.

Table VI summarizes the equilibrium properties of the four hydride phases shown in Fig. 6. The question of site selectivity, especially in bcc Fe is important and we will TABLE VI. Equilibrium volumes per Fe atom and cohesive energies of the four FeH phases following evolution optimisation, compared to the target values. Cohesive energies are relative to the fcc octahedral (rocksalt) phase. The final column shows the radius of the interstitial site based on a lattice of hard spheres at the equilibrium volume of pure Fe and taken from Leslie. \( ^{46} \)  All quantities are given in atomic Rydberg units.

<table><tr><td></td><td colspan="3">TB</td><td colspan="2">Target</td><td>radius</td></tr><tr><td></td><td>\( E_{\text{coh}} \)</td><td>\( \Omega \)</td><td>\( E_{\text{coh}} \)</td><td>\( \Omega \)</td><td></td><td></td></tr><tr><td>fcc OCT</td><td>0.0</td><td>86.90</td><td>0.0</td><td>88.59</td><td>0.98</td><td></td></tr><tr><td>fcc TET</td><td>0.017</td><td>98.64</td><td>0.016</td><td>97.58</td><td>0.53</td><td></td></tr><tr><td>bcc TET</td><td>0.018</td><td>96.16</td><td>0.015</td><td>97.23</td><td>0.68</td><td></td></tr><tr><td>bcc OCT</td><td>0.035</td><td>101.75</td><td>0.038</td><td>101.28</td><td>0.36</td><td></td></tr></table>

revisit it in the dilute limit, below, in section V B 1.

## V. PREDICTIONS OF THE Fe–H MODEL

## A. Iron hydride

Our first test of the tight binding model is to compare the resulting adiabatic potential surface section with the results of calculations by Elsässer et al. \( ^{[69,73]} \)  which were made in the local density approximation (LDA) to DFT. In these calculations the H sublattice is displaced with respect to the Fe sublattice in both bcc and fcc FeH in a chosen set of directions so as to explore the curvatures and barriers of the potential energy landscape. For the case of the bcc structure, Fig. 9 shows some of the displacement paths. The potential sections from previous LDA \( ^{[69]} \)  and our present tight binding model are shown in Fig. 10. Whereas the relative energies of the tetrahedral and octahedral sites have been established by the fitting, the remainder of the these curves amount to predictions of the tight binding model. They turn out to be be in remarkable, quantitative agreement with the LDA calculations in the bcc and fcc case, the latter being shown in Fig. 11. These curves exploit to the full the notion discussed in section II B, above, of environment dependent screening of hopping integrals as the hydrogen approaches Fe–Fe first and second neighbor bonds and indeed penetrates the bond to lie directly in between the two atoms. It is exactly in this situation that one expects the Fe–Fe bond integrals to be strongly modified by screening, and clearly our model captures this well in a non orthogonal two center description. In particular note, in reference to Fig. 10 that the minimum energy (saddle) point along the  \( [101]_{o} \)  path lies to the left of the point “S” in both LDA and in our TB model. This implies that the  \( [101]_{t} \)  minimum energy diffusion path in reality is bowed slightly towards the center of Fig. 9. The strongest test of the environment dependence however is
 

FIG. 9. (color online) Illustrates the translations of the bcc interstitials in constructing our adiabatic potential surfaces, after the three dimensional drawing of Fig. 1 in Krimmel et al. \( ^{73} \)  The figure represents an (010) face of the bcc lattice with Fe atoms as black circles at each corner. The octahedral sites are shown as squares, the central, filled one being the one occupied in octahedral FeH. Of the four tetrahedral sites, shown as triangles, one is occupied in tetrahedral FeH and this is shown filled in here. The point, S, is midway between two tetrahedral sites—the expected diffusion path of H in  \( Fe^{74} \)  which is highlighted in red here and in Fig. 10. Those displacements which are in the (010) plane are indicated.

![](./images/867749575656473067_20.jpg)

in the fcc hydrides of Fig. 11. The energy barrier at the maximum of the  \( \langle110\rangle_{o} \)  path, coinciding with the maximum of the  \( \langle001\rangle_{t} \)  path is perfectly rendered by the TB model without having been fitted and this corresponds to the extreme instance of screening in which the H atom becomes positioned at the center of the first neighbor Fe–Fe bond (see Fig. 1, ref [75]).

## B. H in Fe—the dilute limit

We concentrate on three predicted properties of iron in this section. First is the dissolution energy \( ^{76} \)  or zero temperature heat of solution of hydrogen in Fe. Included in this study is the matter of the site selectivity. Second is the binding energy \( ^{1} \)  or  \( 0^{\circ} \) K segregation energy of H to the (001) surface of Fe. Third, and of great importance to the question of hydrogen embrittlement, is the binding of H atoms to a vacancy in Fe.
TABLE VII. Dissolution energy, in eV, of H in Fe in both tetrahedral (TET) and octahedral (OCT) interstices. Present results are marked TB, experimental and LSDA-GGA values are taken from Jiang and Carter. \( ^{76} \) 

<table><tr><td></td><td>TET</td><td>OCT</td></tr><tr><td>TB</td><td>0.273</td><td>0.354</td></tr><tr><td>expt.</td><td>0.296</td><td></td></tr><tr><td>GGA</td><td>0.19</td><td>0.32</td></tr></table>

## 1. Dissolution energy

Following Ramasubramaniam et al. \( ^{1} \)  we construct a 54 atom supercell as we did in section III B4 and whose total energy we denoted  \( E(\mathrm{Fe}_{54}) \) . We then place a hydrogen atom at either a tetrahedral or an octahedral site and minimize the total energy by relaxation. The resulting total energies are denoted  \( E(\mathrm{Fe}_{54}H) \) . We do not allow the volume to relax. Then the dissolution energy is \( ^{76} \) 

 \[ E_{\mathrm{d i s}}=E(\mathrm{F e}_{54}\mathrm{H})-E(\mathrm{F e}{}_{54})-\textstyle{\frac{1}{2}}E_{\mathrm{H}_{2}} \quad (4) \] 

Our model does not contain H–H interactions, but faux de mieux we may take  \( E_{H_{2}} = -4.75 \)  eV from experiment or from quantum chemistry. \( ^{[20,76]} \)  For each of the three calculations we employ a mesh of  \( 12 \times 12 \times 125 \)  points and use first order generalized Gaussian integration of the Brillouin zone with a width of 2.5 mRy. \( ^{[77]} \)  Results are shown in table VII. These are in remarkably good quantitative agreement with both observations and LSDA-GGA calculations. In particular we predict the tetrahedral site to be preferred over the octahedral, as is well established. \( ^{[74]} \)  We may point out here that this is not a trivial result: carbon in contrast, while preferring the tetrahedral site in the ficticious bcc-based carbide, transfers to the octahedral site in the dilute limit. \( ^{[78]} \)  In the effective medium theory, upon which the embedded atom potentials (EAM) are based, H prefers the octahedral site. \( ^{[79]} \) 

## 2. H segregation to the (001) surface of Fe

Three binding sites of H to the (001) surface of Fe have been identified. \( ^{1} \)  These are illustrated in Fig. 12. We have constructed supercells of  \( 2 \times 2 \times 5 \)  cubic two-atom unit cells with three layers of vacuum inserted along the long axis. The slab contains 40 Fe atoms and the total energy of the fully relaxed supercell is denoted  \( E^{\mathrm{surf}}(\mathrm{Fe}_{40}) \) . We place one H atom at one of the three adsorption sites in Fig. 12 and relax the structure by energy minimization. Allowing all atoms to relax we denote the total energy  \( E^{\mathrm{surf}}(\mathrm{Fe}_{40}H) \) . The associated “adsorption energy” is \( ^{1} \) 

 \[ E_{\mathrm{a d s}}=E(\mathrm{F e}_{54}\mathrm{H})-E(\mathrm{F e}{}_{54})-\textstyle{\frac{1}{2}}E_{\mathrm{H}_{2}} \]
 

FIG. 10. (color online) Adiabatic potential surface sections of bcc FeH: left LDA, \( ^{69} \)  right TB. These curves show the energy as a function of the displacement of the H sublattice relative to the Fe sublattice. The curves which start at the point “O” refer to displacements from the octahedral site phase; a H atom initially at position  \( \left[\frac{1}{2}0\frac{1}{2}\right] \)  translates in the directions indicated. Along the [001] direction it eventually falls into a vacant tetrahedral site (see Fig. 9). This curve hence represents the transition to the tetrahedral-site phase. Translation along [101] takes the H atom to a position midway between two, vacant, tetrahedral sites—this point is marked “S”. For a H atom initially occupying a tetrahedral site, translation along [101] moves it to an adjacent, unoccupied, tetrahedral site, the half-way point being the same point “S”. The translation labels are vectors referred to Fig. 9. For each case, LDA and TB, the calculations are at fixed atomic volume, namely the equilibrium volume of the bcc tetrahedral phase of FeH, see table VI;  \( a_{0} \)  is the corresponding equilibrium lattice constant.

![](./images/867749575656473067_21.jpg)

![](./images/867749575656473067_22.jpg)

and by combining the previous two equations the “binding energy” is \( ^{1} \) 

 \[ E_{\mathrm{b i n d}}=E_{\mathrm{d i s}}^{t}-E_{\mathrm{a d s}} \quad (5) \] 

in which the reference energy, or chemical potential, of gaseous  \( H_{2} \)  has canceled.  \( E_{dis}^{t} \)  is the dissolution energy (4) at a tetrahedral site (table VII). We have calculated the three quantities using a  \( 12 \times 12 \times 1 \)  k-point mesh and the same Brillouin zone integration as above. In table VIII we show our calculated binding energies, the displacement  \( \delta \)  in Fig. 12 and the height, h, from the (001) surface constructed as the difference in z-coordinates of the H atom and the average from the four topmost Fe atoms.

The predictions of our model are only in reasonable agreement with the LSDA-GGA. \( ^{1} \)  The heights above the surface are well rendered; the displacement,  \( \delta \) , is significantly larger, but is consistent with the preference for tetrahedral site occupancy. As we point out in the caption to Fig. 12,  \( \delta = 0.25a_{0} = 0.71 \)  Å puts the H atom into a surface tetrahedral site and our model does exactly that; in contrast the LSDA-GGA quite surprisingly results in a much smaller  \( \delta \) . In the same vein, the height

TABLE VIII. Predicted structure and energetics of H adsorbed on Fe (001). We show for the QT, hollow (H) and bridge (B) sites of Fig. 12 the displacent  \( \delta \)  and height, h, above the surface (all in Å) and the  \( 0^{\circ} \) K segregation or binding energy,  \( E_{bind} \) , in eV. In parentheses are the LSDA-GGA results of Ramasubramaniam et al. \( ^{1} \) 

<table><tr><td></td><td>\( \delta \)</td><td>h</td><td>\( E_{\text{bind}} \)</td></tr><tr><td></td><td>TB (GGA)</td><td>TB (G GA)</td><td>TB (GA)</td></tr><tr><td>QT</td><td>0.635 (0.19)</td><td>0.31 (0.38)</td><td>0.241 (0.768)</td></tr><tr><td>H</td><td></td><td>0.27 (0.38)</td><td>0.191 (0.775)</td></tr><tr><td>B</td><td></td><td>0.85 (1.20)</td><td>0.222 (0.655)</td></tr></table>

of the H atom above the bridge site, 0.85 Å, is close to  \( 0.25a_{0} \) , and we find another local minimum at 0.34 Å below the bridge site. Thus the strongest binding in the TB model is to surface tetrahedral sites and the surface octahedral site is indeed not a local energy minimum. In this way the binding energies are in poor agreement with the LSDA-GGA and may reflect the limitations in transferability (section II B) in that the model retains its bulk-like features at the surface.  \( E_{bind} \)  is in fact the  \( 0^{\circ}K \)  segregation energy, usually defined as the energy needed to remove the impurity from the surface and place it
 

FIG. 11. Adiabatic potential surface sections of fcc FeH: left LDA, \( ^{69} \)  right TB. At the point “O” we have the rocksalt phase, from which translation of the H sublattice along a  \( \langle111\rangle \)  direction transforms the structure to the zincblende phase in which tetrahedral sites are occupied. The energy maximum between “O” and “T” is located close to where the H atom squeezes between an equilateral triangle of Fe atoms in the  \( (111) \)  plane. At the maximum along  \( \langle110\rangle_{o} \) , and along  \( \langle001\rangle_{t} \) , the H is positioned mid-way between two nearest neighbor Fe atoms (see Fig. 1 of ref [75]). Note that both these two energy barriers are predicted by the TB model with quantitative accuracy. The calculations are at the calculated equilibrium volume of the fcc octahedral (rocksalt) phase of FeH, see table VI;  \( a_{0} \)  is the corresponding equilibrium lattice constant.

![](./images/867749575656473067_23.jpg)

![](./images/867749575656473067_24.jpg)

FIG. 12. (color online) Three possible binding sites of H on the  \( (001) \)  surface of Fe, after Ramasubramaniam et al. \( ^{1} \)  Four large circles represent the Fe atoms at the corners of a unit cell of the  \( (001) \)  face of the bcc lattice. At the center is the “hollow” site, a smaller circle; this may be displaced along  \( [100] \)  by an amount  \( \delta \)  to become the “quasi-threefold” (QT) site indicated by a triangle. The “bridge” site is shown as a square. It is important to recognize that the bridge and hollow sites in the plane of the truncated bulk surface are octahedral interstices, whereas the QT site at  \( \delta = 0.25a_{0} \)  is a tetrahedral site. If a H atom at the bridge site is displaced up or down by  \( 0.25a_{0} \)  then it comes to occupy a tetrahedral site. Here,  \( a_{0} = 2.87 \)  Å is the equilibrium pure  \( \alpha \) -Fe lattice constant.

![](./images/867749575656473067_25.jpg)

into the interior of the crystal. The LSDA-GGA shows the smallest adsorption energy (largest  \( E_{bind} \) ) to be at the hollow site; whereas we find it at the QT site and at this coverage this is not consistent with experiment which shows a transition at  \( 100^{\circ} \) K from hollow to QT site selectivity between about 0.3ML and 1ML, \( ^{80} \)  while our calculations and the LSDA-GGA \( ^{1} \)  are at 0.25ML.

Both the QT and bridge sites are at local minima in the potential energy in our model. This is consistent with the LSDA-GGA. \( ^{1} \)  However the hollow site is a local saddle point having an almost flat energy surface with respect to small displacements parallel to the surface; if we displace the H atom a sufficient amount then the structure relaxes into the QT site occupancy. This is inconsistent with the LSDA-GGA in which surprisingly, in view of there being another local minimum at QT just 0.19Å distant, the hollow site is at a local minimum. \( ^{1} \) 

To some extent our choice of chemical potential for  \( H_{2} \) ,  \( E_{H_{2}} \) , is arbitrary; however the observed bond energy leads to a very good rendering of the  \( 0^{\circ}K \)  heat of solution (dissolution energy) of H in Fe, table VII. On the other hand it leads to a positive, but small, adsorption energy,  \( E_{ads} \) , which means that in our model  \( H_{2} \)  will not dissociate on the (001) surface of Fe. In order to model the surface adsorption properly we could make an ad hoc adjustment of  \( E_{H_{2}} \) . This would be at the expense of less
 

accurate  \( E_{dis} \) . For example, if we used the Skinner and Pettifor tight binding model of hydrogen, \( ^{20} \)  then we'd have  \( E_{H_{2}} = -4.30 \)  eV rather than -4.75 eV. In that case our dissolution energy in the tetrahedral site becomes 0.05 eV (rather than 0.27 eV, cf table VII) but the adsorption energies are then negative as they should be. Of course the segregation energies (table VIII) remain unchanged by this redefinition of the hydrogen chemical potential.

## 3. H segregation to a vacancy in Fe

It is believed that the trapping of H to vacancies in Fe is of central importance in the effects of H on mechanical behavior. \( ^{[74,81,82]} \)  It is also known that dissolved hydrogen results in a dramatic increase in the vacancy concentration in several metals including Fe, \( ^{[83,84]} \)  caused through segregation induced lowering of the vacancy formation enthalpy. \( ^{[85]} \)  We can show that our model is able to demonstrate these facts by comparison with LSDA-GGA calculations of the  \( 0^{\circ} \) K segregation energy,  \( E_{\mathrm{bind}}^{v}(n) \) , of up to seven H atoms to a single vacancy in Fe. \( ^{[1,62]} \)  The principal result, which we also predict in our TB model is that up to five H atoms may bind to a vacancy with a positive segregation energy, but the sixth has a small negative  \( E_{\mathrm{bind}}^{v}(n) \) . Here we follow Tateyama and Ohno \( ^{[62]} \)  and Ramasubramaniam et al. \( ^{[1]} \)  and define  \( E_{\mathrm{bind}}^{v}(n) \)  as the  \( 0^{\circ} \) K segregation energy of a H atom from a bulk tetrahedral site to a vacancy to which  \( (n-1) \)  H atoms are already segregated. Hence we set up a 53 atom supercell as in section III B4; then in reference to figure 5 in Ramasubramaniam et al., \( ^{[1]} \)  if the vacant site is at  \( \left[\frac{1}{2}\frac{1}{2} \frac{1}{2}\) in the bcc supercell we add H atoms successively in (1)  \( \left[\frac{1}{2} \frac{1}{2}\right] \)  (2)  \( \left[\frac{1}{2} \frac{1}{2}\right] \) , (3)  \( \left[\frac{1}{2} \frac{1}{2}\right] \) , (4)  \( \left[\frac{1}{2} \frac{1}{2}\right] \) , (5)  \( \left[\frac{1}{2} \frac{1}{2}\right] \) , and (6)  \( \left[\frac{0}{2} \frac{1}{2} \frac{\gamma}{2}\right] \)  octahedral interstices—these are the centers of the six  \( \{001\} \)  faces bounding the vacant site. Finally a seventh H atom may be placed at the vacant site. These supercells are relaxed by energy minimization and we denote the total energy of the supercell by  \( E(\mathrm{Fe}_{53}\mathrm{H}_{n}) \) . Then we have \( ^{[1,62,86]} \)  in analogy with (5)

 \[ E_{\mathrm{b i n d}}^{v}(n)=E_{\mathrm{d i s}}^{t}-\left(E(\mathrm{F e}_{53}\mathrm{H}_{n})-E(\mathrm{F e}_{5}\mathrm{H}_{n-1})-\frac{1}{2}E_{\mathrm{H}_{2}}\right) \] 

which is independent of the chemical potential of H. Table IX shows our segregation energies, compared to LSDA-GGA. The relaxation pattern is very simple in all cases except n = 3 and n = 5. In the simple instances, each H atom relaxes perpendicularly to its  \( \{001\} \)  face, by an amount we denote  \( \delta_{\perp}^{\mathrm{even}}(n) \) , towards the vacant site. The displacement decreases as n increases both in LSDA-GGA \( ^{62} \)  and our TB model. In each of the cases n = 3 and n = 5 there is one H atom which follows this trend whereas the remaining  \( (n-1) \)  H atoms are displaced both towards the vacancy by  \( \delta_{\perp}^{\mathrm{odd}}(n) \)  and, by an amount  \( \delta_{\parallel}(n) \)  in a direction parallel to the  \( \{001\} \)  face containing the site where the H atom was originally placed, in a  \( \langle100\rangle \)  direction.
TABLE IX. Segregation of H atoms to a vacancy in Fe. We show our model's predicted  \( E_{\mathrm{bind}}^{\mathrm{v}}(n) \)  compared to LSDA-GGA results, \( ^{62} \)  quoted by Ramasubramaniam et al., \( ^{1} \)  in eV. Also shown are the displacements of the H atom towards the vacancy, and away from the octahedral site in the  \( \{001\} \)  plane in which it was originally placed. In cases of higher symmetry the displacement of all H atoms is an amount  \( \delta_{\perp}^{\mathrm{even}}(n) \)  normal to the  \( \{001\} \)  face and towards the vacant site. In the cases n = 3 and n = 5 one atom follows this displacement, while all those remaining move both perpendicular to the face—by an amount  \( \delta_{\perp}^{\mathrm{odd}}(n) \) —and parallel to the face in a  \( \langle100\rangle \)  direction by an amount  \( \delta_{\parallel}(n) \) , rather like the knight's move in chess. A displacement  \( \delta_{\parallel} = 0.25a_{0} = 0.71 \)  Å will take the H atom into a tetrahedral site. Displacements are given in Å.

<table><tr><td>n</td><td colspan="2">\( E_{\mathrm{bind}}^{\mathrm{v}}(n) \)</td><td>\( \delta_{\perp}^{\mathrm{even}}(n) \)</td><td>expt. \( ^{a} \)</td><td>\( \delta_{\perp}^{\mathrm{odd}}(n) \)</td><td>\( \underline{\delta}_{\parallel}(n) \)</td></tr><tr><td></td><td>TB</td><td>LSDA-GGA</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>0.319</td><td>0.559</td><td>0.25</td><td>0.4 \pm 0.1</td><td></td><td></td></tr><tr><td>2</td><td>0.330</td><td>0.612</td><td>0.27</td><td></td><td></td><td></td></tr><tr><td>3</td><td>0.263</td><td>0.399</td><td>0.19</td><td></td><td>0.27</td><td>0.35</td></tr><tr><td>4</td><td>0.160</td><td>0.276</td><td>0.28</td><td></td><td></td><td></td></tr><tr><td>5</td><td>0.144</td><td>0.335</td><td>0.13</td><td></td><td>0.26</td><td>0.25</td></tr><tr><td>6</td><td>-0.033</td><td>-0.019</td><td>0.19</td><td></td><td></td><td></td></tr><tr><td>7</td><td>-0.474</td><td>-2.68</td><td>0.14</td><td></td><td></td><td></td></tr></table>

 \( ^{a} \)  Reference [87]

Table IX shows very much better agreement with the LSDA-GGA than in the case of surface segregation. This probably reflects the better transferability into the less undercoordinated environment. Our absolute values of  \( E_{\mathrm{bind}}^{v}(n) \)  are no more than 50% underestimated while the trends are in perfect accord: we observe the increase in segregation energy going from n = 1 to n = 2 implying that a H atom segregates more readily to a vacancy that has already trapped a H atom. We also see that up to five H atoms will segregate exothermally to a vacancy, while the sixth segregates endothermically. The displacement patterns in the symmetric cases are consistent in magnitude with the LSDA-GGA \( ^{62} \)  and follow the trend of decreasing  \( \delta_{\perp}^{even} \)  with increasing n. For the case n = 1 we obtain  \( \delta_{\perp}^{even} = 0.25 \)  Å which agrees well with the LSDA-GGA calculated value of 0.22 Å. \( ^{62} \)  An experimental estimate of  \( 0.4 \pm 0.1 \)  Å was obtained for deuterium in Fe by ion channeling. \( ^{87} \)  Effective medium theory for n = 1 results in  \( \delta_{\perp}^{even} = 0.5 \pm 0.1 \)  Å in Fe \( ^{88} \)  and  \( 0.46 \pm 0.07 \)  Å in Nb. \( ^{89} \)  The octahedral sites in which the H atoms are originally placed correspond to the hollow sites at the (001) surface, and as in the surface case the atoms relax into the vacuum or vacancy and, symmetry permitting, laterally towards the tetrahedral positions. The interpretation of Tateyama and Ohno \( ^{62} \)  that there is an electrostatic repulsion between H atoms is unconvincing to us, since we imagine that this will be screened by the electrons in the vacant site. We note that in the highly endothermic segregation of a seventh H atom to
 

the vacancy there is still an inward relaxation, at least in our model, towards the vacant site, now occupied by a H atom. However our  \( E_{\mathrm{bind}}^{\nu}(7) \)  is more than five times smaller than in LSDA-GGA. \( ^{62} \) 

We should note, as Kirchheim has pointed out, \( ^{82} \)  that the reduction in enthalpy of the impurity by segregating to a defect is entirely equivalent to a reduction in the defect's enthalpy of formation. Hence ours and the LSDA-GGA binding energies of table IX are consistent with the observed “superabundant vacancy formation” in many metals subject to a high hydrogen fugacity \( ^{83,84} \)  (see Fig. 7, ref [62]).

## VI. DISCUSSION AND CONCLUSIONS

We have described simple and robust tight binding models for pure Fe, transferable from bcc into hcp and fcc structures and hence able to describe the common phases of Fe,  \( \alpha \) ,  \( \gamma \)  and  \( \epsilon \) . Furthermore we have included a description of the electronic structure of monohydrides and this model has been shown to be transferable into the dilute limit of interstitial H impurity in Fe. A simple orthogonal d-band model is expected to be most appropriate for the pure transition metals and their alloys \( ^{35-37} \)  and indeed the addition of s or p electrons does not usually result in better energetics. \( ^{4,15} \)  This is confirmed here (table II) in the case of bulk elastic constants and structural energy difference. The only improvement to bulk properties arising from the non orthogonal sd model is an improved cohesive energy. Vacancy formation and surface energies are somewhat improved in the non orthogonal sd model.

The focus on transferability is made in section IV where, while not permitting the parameters of the pure Fe model to be adjusted, we seek additional parameters to describe Fe–H interactions. We give reasons in section IV in addition to the transferability arguments for choosing to extend the non orthogonal sd rather than the orthogonal d model to the description of hydrogen. There are only few additional parameters needed (table V) and we emphasize that these were fitted to just seven fiducial points in the LSDA-GGA energy–volume curves for four putative iron hydrides (Fig. 6). Possibly as a consequence of our adoption of a non orthogonal model both for pure Fe and Fe–H, our resulting model predicts calculated adiabatic potential surfaces with quantitative accuracy. It is particularly notable that in these tests H atoms are brought perpendicularly towards Fe–Fe bonds to the point that the H atom comes between the two host atoms. This happens in both bcc and fcc hydrides; in the latter case a H atom also pushes through the triangle of nearest neighbour Fe atoms in the (111) plane and the matching to the LDA is excellent (figs. 10 and 11).

Our approach has been to find a model purely by reference to the concentrated limit of a stoichiometric monohydride, FeH, and then to test that model into the dilute limit of H in Fe. Therefore all the results in section V B are predictions. In contrast, in constructing a classical model Ramasubramaniam et al. \( ^{1} \)  needed to put all the properties that we describe in section V B into the training set for the potential. In consequence, the tight binding approach cannot hope to reproduce the quantitative accuracy that is achieved by a well fitted classical model. However, dissolution energies, site selectivity and vacancy segregation are very well rendered in the model. Its most obvious shortcoming is in the prediction of adsorption energies of H on the (001) surface of Fe. The absolute cohesive energy is problematic in LSDA, \( ^{38,90} \)  but even more so in tight binding (see the caption to table II). Possibly for this reason we find that  \( H_{2} \)  will not dissociate on the (001) surface if we use the known binding energy of the  \( H_{2} \)  molecule as our reference. In future work we will need to account for molecular hydrogen and this matter will be revisited. On the other hand, qualitatively the TB model gives a reasonable account of H adsorption which is certainly a subtle and complex problem in surface physics. In this way the TB model does not transfer faultlessly into the problem of surface energetics. Our predictions of segregation to a vacancy, in contrast, are in very good accord with the known theoretical LSDA-GGA results and experimental facts. In particular, we predict that a vacancy will bind up to five H atoms exothermically and that the segregation energy is somewhat larger to a vacancy at which one H atom is already bound. The trapping of vacancies is central to the mechanism of the action of H on the mechanical properties of Fe alloys. \( ^{74,81,82} \) 

In conclusion, the quantum mechanical tight binding approximation lies between the first principles LSDA and the atomistic classical approach to defect energetics in iron. Because the TB approximation is grounded in electronic structure theory it may be applied to this question rather easily and just a few parameters—adjustable within intuitive limits—are required. Because of this and because of its simplicity the TB approach may give rise to a better understanding than the LSDA, which after much labor produces a total energy and force, often without clear insight to their origins. In contrast the huge number of parameters and the rather opaque functional form of the interatomic interactions in the classical potentials, while able to model many properties quantitatively, must be at risk of failure once they are transferred into situations for which they were not fitted. Therefore we expect the TB approximation to provide a useful and complementary tool to the classical potentials, and once augmented with parameters to describe carbon, to become competitive in the atomistic simulation of the properties of iron and steel.

## ACKNOWLEDGMENTS

We thank Professor P. Gumbsch for enlightening discussions and comments on the manuscript.

We are grateful to the Royal Society for the award of
 

an International Joint Project, JP0872832.

A. T. P. is grateful to the German Research Foundation (DFG project Gu 367/30).

Financial support from the German Federal Ministry

 \( ^{*} \)  Tony.Paxton@iwm.fraunhofer.de

 \( ^{\dagger} \)  Christian.Elsaesser@iwm.fraunhofer.de

 \( ^{1} \)  A. Ramasubramaniam, M. Itakura, and E. A. Carter, Phys. Rev. B, 79, 174101 (2009).

 \( ^{2} \)  M. Mrovec, C. Elsässer, and P. Gumbsch, Phil. Mag., 89, 3179 (2009).

 \( ^{3} \)  S. P. Lynch, Acta Metallurgica, 36, 2639 (1988).

 \( ^{4} \)  A. T. Paxton and M. W. Finnis, Phys. Rev. B, 77, 024428 (2008).

 \( ^{5} \)  W. A. Harrison, Electronic structure and the properties of solids (W. H. Freeman, San Francisco, 1980).

 \( ^{6} \)  D. G. Pettifor, Bonding and structure of molecules and solids (Oxford University Press, Oxford, 1995).

 \( ^{7} \)  M. W. Finnis, Interatomic forces in condensed matter (Oxford University Press, Oxford, 2003).

 \( ^{8} \)  G. Liu, D. Nguyen-Manh, B.-G. Liu, and D. G. Pettifor, Phys. Rev. B, 71, 174115 (2005).

 \( ^{9} \)  A. T. Paxton, in “Multiscale Simulation Methods in Molecular Sciences,” (NIC series, vol 42, Jülich Supercomputing Centre) pp. 145–174. Available on-line at http://www.fz-juelich.de/nic-series/volume42.

 \( ^{10} \)  W. M. C. Foulkes and R. Haydock, Phys. Rev. B, 39, 12520 (1989).

 \( ^{11} \)  A. P. Sutton, M. W. Finnis, D. G. Pettifor, and Y. Ohta, Journal of Physics: Condensed Matter, 21, 35 (1988).

 \( ^{12} \)  J. C. Slater and G. F. Koster, Phys. Rev., 94, 1498 (1954).

 \( ^{13} \)  F. Ducastelle, J. Phys. France, 31, 1055 (1970).

 \( ^{14} \)  D. Spanjaard and M. C. Desjonquères, Phys. Rev. B, 30, 4822 (1984).

 \( ^{15} \)  A. T. Paxton, Journal of Physics D: Applied Physics, 29, 1689 (1996).

 \( ^{16} \)  V. Heine, Phys. Rev., 153, 673 (1967).

 \( ^{17} \)  O. K. Andersen, Solid State Communications, 13, 133 (1973).

 \( ^{18} \)  O. K. Andersen, Phys. Rev. B, 12, 3060 (1975).

 \( ^{19} \)  D. G. Pettifor, Journal of Physics F: Metal Physics, 7, 613 (1977).

 \( ^{20} \)  A. J. Skinner and D. G. Pettifor, Journal of Physics: Condensed Matter, 3, 2029 (1991).

 \( ^{21} \)  S. Froyen and W. A. Harrison, Phys. Rev. B, 20, 2420 (1979).

 \( ^{22} \)  A. T. Paxton, A. P. Sutton, and C. M. M. Nex, Journal of Physics C: Solid State Physics, 20, L263 (1987).

 \( ^{23} \)  L. Goodwin, A. J. Skinner, and D. G. Pettifor, Europhys. Lett., 9, 701 (1989).

 \( ^{24} \)  S. Znam, D. Nguyen-Manh, D. G. Pettifor, and V. Vitek, Phil. Mag. A, 83, 415 (2003).

 \( ^{25} \)  P. B. Allen, J. Q. Broughton, and A. K. McMahan, Phys. Rev. B, 34, 859 (1986).

 \( ^{26} \)  D. G. Pettifor, Journal of Physics F: Metal Physics, 5, 97 (1972).

 \( ^{27} \)  O. K. Andersen and O. Jepsen, Phys. Rev. Lett., 53, 2571 (1984).

 \( ^{28} \)  M. S. Tang, C. Z. Wang, C. T. Chan, and K. M. Ho, Phys. Rev. B, 53, 979 (1996).

for Education and Research (BMBF) to the Fraunhofer IWM for C. E. (grant number 02NUK009C) is gratefully acknowledged.

 \( ^{29} \)  H. Haas, C. Z. Wang, M. Fähnle, C. Elsässer, and K. M. Ho, Phys. Rev. B, 57, 1461 (1998).

 \( ^{30} \)  D. Nguyen-Manh, D. G. Pettifor, and V. Vitek, Phys. Rev. Lett., 85, 4136 (2000).

 \( ^{31} \)  M. Mrovec, D. Nguyen-Manh, D. G. Pettifor, and V. Vitek, Phys. Rev. B, 69, 094115 (2004).

 \( ^{32} \)  M. Mrovec, R. Gröger, A. G. Bailey, D. Nguyen-Manh, C. Elsässer, and V. Vitek, Phys. Rev. B, 75, 104119 (2007).

 \( ^{33} \)  J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett., 78, 1396 (1997).

 \( ^{34} \)  M. Methfessel, M. van Schilfgaarde, and R. A. Casali, "Electronic structure and physical properties of solids: the uses of the LMTO method," (Springer-Verlag, Berlin, 2000) pp. 114–147.

 \( ^{35} \)  D. G. Pettifor, Phys. Rev. Lett., 42, 846 (1979).

 \( ^{36} \)  A. R. Williams, C. D. Gelatt, and V. L. Moruzzi, Phys. Rev. Lett., 44, 429 (1980).

 \( ^{37} \)  D. G. Pettifor, Solid State Physics, 40, 43 (1987).

 \( ^{38} \)  P. H. T. Philipsen and E. J. Baerends, Phys. Rev. B, 54, 5326 (1996).

 \( ^{39} \)  I. Seki and K. Nagata, ISIJ International, 45, 1789 (2005).

 \( ^{40} \)  J. Zarestky and C. Stassis, Phys. Rev. B, 35, 4500 (1987).

 \( ^{41} \)  D. M. Edwards, Journal of Magnetism and Magnetic Materials, 36, 213 (1983).

 \( ^{42} \)  J. J. Adams, D. S. Agosta, R. G. Leisure, and H. Ledbetter, J. Appl. Phys., 100, 113530 (2006).

 \( ^{43} \)  G. Y. Guo and H. H. Wang, Chinese J. Phys., 38, 949 (2000).

 \( ^{44} \)  V. Heine, A. Holden, P. Lin-Chung, and M. You, Journal of Magnetism and Magnetic Materials, 15-18, 69 (1980).

 \( ^{45} \)  H. Hasegawa and D. G. Pettifor, Phys. Rev. Lett., 50, 130 (1983).

 \( ^{46} \)  W. C. Leslie, The Physical Metallurgy of Steels (Hemisphere, Washington, 1981).

 \( ^{47} \)  L. Kaufman, E. Clougherty, and R. J. Weiss, Acta Metallurgica, 11, 323 (1963).

 \( ^{48} \)  D. M. Roy and D. G. Pettifor, J. Phys. F: Metal Phys., 7, L183 (1977).

 \( ^{49} \)  N. E. Christensen, O. Gunnarsson, O. Jepsen, and O. K. Andersen, J. Phys. Colloques C8, 49, 17 (1988).

 \( ^{50} \)  C. Elsässer, J. Zhu, S. G. Louie, M. Fähnle, and C. T. Chan, Journal of Physics: Condensed Matter, 10, 5081 (1998).

 \( ^{51} \)  K. Tajima, Y. Endoh, Y. Ishikawa, and W. G. Stirling, Phys. Rev. Lett., 37, 519 (1976).

 \( ^{52} \)  H. Hasegawa, M. W. Finnis, and D. G. Pettifor, Journal of Physics F: Metal Physics, 15, 19 (1985).

 \( ^{53} \)  H. Hasegawa, M. W. Finnis, and D. G. Pettifor, Journal of Physics F: Metal Physics, 17, 2049 (1987).

 \( ^{54} \)  M. J. S. Spencer, A. Hung, I. K. Snook, and I. Yarovsky, Surf. Sci., 513, 389 (2002).

 \( ^{55} \)  M. W. Finnis, A. T. Paxton, M. Methfessel, and M. van Schilfgaarde, in Tight binding approach to computational materials science, MRS Symp. Proc. No. 491, edited by
 

P. E. A. Turchi, A. Gonis, and L. Colombo (Materials Research Society, Pittsburgh PA, 1998) pp. 265–74.

 \( ^{56} \)  N. P. Allen, B. E. Hopkins, and J. E. McLennan, Proc. R. Soc. Lond. A, 234, 221 (1956).

 \( ^{57} \)  R. Ayer, R. Mueller, and T. Neeraj, Materials Science and Engineering: A, 417, 243 (2006).

 \( ^{58} \)  F. Nakasato and I. M. Bernstein, Metallurgical Transactions A, 9A, 1317 (1978).

 \( ^{59} \)  M. J. Gillan, Journal of Physics: Condensed Matter, 1, 689 (1989).

 \( ^{60} \)  C. Domain and C. S. Becquart, Phys. Rev. B, 65, 024103 (2001).

 \( ^{61} \)  P. Söderlind, L. H. Yang, J. A. Moriarty, and J. M. Wills, Phys. Rev. B, 61, 2579 (2000).

 \( ^{62} \)  Y. Tateyama and T. Ohno, Phys. Rev. B, 67, 174105 (2003).

 \( ^{63} \)  K. Fürderer, K.-P. Döring, M. Gladisch, N. Haas, D. Herlach, J. Major, H.-J. Mundinger, J. Rosenkranz, W. Schäfer, L. Schimmele, W. Schwartz, and A. Seeger, Materials Science Forum, 15–18, 125 (1987).

 \( ^{64} \)  A. Seeger, phys. stat. sol. (a), 167, 289 (1998).

 \( ^{65} \)  O. Seydel, G. Frohberg, and H. Wever, phys. stat. sol. (a), 144, 69 (1994).

 \( ^{66} \)  L. De Schepper, D. Segers, L. Dorikens-Vanpraet, M. Dorikens, G. Knuyt, L. M. Stals, and P. Moser, Phys. Rev. B, 27, 5257 (1983).

 \( ^{67} \)  C. S. Barrett and T. B. Massalski, The Structure of Metals (McGraw-Hill, New York, 1966).

 \( ^{68} \)  C. Elsässer, J. Zhu, S. G. Louie, B. Meyer, M. Fähnle, and C. T. Chan, Journal of Physics: Condensed Matter, 10, 5113 (1998).

 \( ^{69} \)  C. Elsässer, H. Krimmel, M. Fähnle, S. G. Louie, and C. T. Chan, Journal of Physics: Condensed Matter, 10, 5131 (1998).

 \( ^{70} \)  M. W. Finnis, A. T. Paxton, M. Methfessel, and M. van Schilfgaarde, Phys. Rev. Lett., 81, 5149 (1998).

 \( ^{71} \)  H.-P. Schwefel, Numerische Optimierung von Computer-Modellen mittels der Evolutionsstrategie, Interdisciplinary Systems Research, Vol. 26 (Birkhäuser, Basle, 1977).

 \( ^{72} \)  H.-P. Schwefel, Evolution and Optimum Seeking: The Sixth Generation (John Wiley, New York, 1993).

 \( ^{73} \)  H. Krimmel, L. Schimmele, C. Elsässer, and M. Fähnle, Journal of Physics: Condensed Matter, 6, 7704 (1994).

 \( ^{74} \)  J. P. Hirth, Metallurgical Transactions A, 11, 1543 (1980).

 \( ^{75} \)  H. Krimmel, L. Schimmele, C. Elsässer, and M. Fähnle, Journal of Physics: Condensed Matter, 6, 7679 (1994).

 \( ^{76} \)  D. E. Jiang and E. A. Carter, Phys. Rev. B, 70, 064102 (2004).

 \( ^{77} \)  M. Methfessel and A. T. Paxton, Phys. Rev. B, 40, 3616 (1989).

 \( ^{78} \)  A. T. Paxton, (2010), unpublished.

 \( ^{79} \)  M. J. Puska and R. M. Nieminen, Phys. Rev. B, 29, 5382 (1984).

 \( ^{80} \)  P. B. Merrill and R. J. Madix, Surf. Sci., 347, 249 (1996).

 \( ^{81} \)  K. Takai, H. Shoda, H. Suzuki, and M. Nagumo, Acta Materialia, 56, 5158 (2008).

 \( ^{82} \)  R. Kirchheim, Scripta Materialia, 62, 67 (2010).

 \( ^{83} \)  M. Iwamoto and Y. Fukai, Materials Transactions, The Japan Inst. Metals (JIM), 40, 606 (1999).

 \( ^{84} \)  Y. Fukai, K. Mori, and H. Shinomiya, J. Alloys and Compounds, 348, 105 (2003).

 \( ^{85} \)  R. Kirchheim, Acta Materialia, 55, 5139 (2007).

 \( ^{86} \)  This is the quantity denoted  \( E_{\mathrm{trap}}(1,n) \)  in ref [62] and plotted in their fig. 3.

 \( ^{87} \)  S. M. Myers, S. T. Picaux, and R. E. Stoltz, J. Appl. Phys., 50, 5710 (1979).

 \( ^{88} \)  J. K. Nørskov, F. Besenbacher, J. Bøttiger, B. B. Nielsen, and A. A. Pisarev, Phys. Rev. Lett., 49, 1420 (1982).

 \( ^{89} \)  J. Čízek, I. Procházka, F. Bečvář, R. Kužel, M. Cieslar, G. Brauer, W. Anwand, R. Kirchheim, and A. Pundt, Phys. Rev. B, 69, 224106 (2004).

 \( ^{90} \)  M. I. Heggie, R. Jones, and A. Umerski, phys. stat. sol. (a), 138, 383 (1993).
 
