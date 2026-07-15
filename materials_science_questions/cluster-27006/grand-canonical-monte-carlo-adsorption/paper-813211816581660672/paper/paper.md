# Adsorption of $CO_2$ and $N_2$ in Na-ZSM-5: effects of $Na^+$ and Al content studied by Grand Canonical Monte Carlo simulations and experiments

David Newsome · Sofranita Gunawan ·
Gino Baron · Joeri Denayer · Marc-Olivier Coppens

Received: 10 February 2013 / Accepted: 29 June 2013
© Springer Science+Business Media New York 2013

**Abstract** Zeolite crystals with cations present, such as ZSM-5, are widely used for gas sequestration, separations, and catalysis. One possible application is as an adsorbent to separate $CO_2$ from $N_2$ in flue gas mixtures. Typically, the zeolite framework is of a $SiO_2$ composition, but tetravalent Si atoms can be replaced with trivalent Al atoms. This change in valence creates a charge deficit, requiring cations to maintain the charge balance. Experimental studies have demonstrated that cations enhance adsorption of polar molecules due to strong electrostatic interactions. While numerous adsorption studies have been performed for silicalite-1, the all-silica form of ZSM-5, fewer studies on ZSM-5 have been performed. Grand Canonical Monte Carlo simulations were used to study adsorption of $CO_2$ and $N_2$ in Na-ZSM-5 at $T=308$ K, which is ZSM-5 with $Na^+$ counter-ions present. The simulations suggest that a lower Si/Al ratio (or higher $Na^+$ and Al content) substantially increases adsorption at low pressures. At high pressures, however, the effect of the Al substitutions is minor, because the $Al^-/Na^+$ sites are saturated with guest molecules. Similarly, a lower Si/Al ratio also increases the isosteric heat of adsorption at low loading, but the isosteric heats approach the silicalite-1 reference values at higher loadings. Comparison of simulations and experimental measurements of the adsorption isotherms and isosteric heats points to the importance of carefully considering the role of charge on the $Na^+$ cations, and suggest that the balancing cations in ZSM-5, here $Na^+$, only have partial charges.

**Keywords** Carbon dioxide · Nitrogen · Zeolite ·
Adsorption · Grand Canonical Monte Carlo · Sodium cations

---

Electronic supplementary material The online version of this article (doi:10.1007/s10450-013-9560-1) contains supplementary material, which is available to authorized users.

D. Newsome · S. Gunawan · M.-O. Coppens
Delft University of Technology, DelftChemTech,
Julianalaan, 136, 2628 BL Delft, The Netherlands

Present Address:
D. Newsome
CFD Research Corporation, 215 Wynn Drive,
Huntsville, AL, USA

G. Baron · J. Denayer
Department of Chemical Engineering, Vrije Universiteit Brussel,
Pleinlaan 2 B, 1050 Brussels, Belgium

M.-O. Coppens
Howard P. Isermann Department of Chemical and Biological
Engineering, Rensselaer Polytechnic Institute, Troy, NY 12180,
USA

Present Address:
M.-O. Coppens (⊗)
Department of Chemical Engineering, University College
London, Torrington Place, London WC1E 7JE, UK
e-mail: m.coppens@ucl.ac.uk

---

## 1 Introduction

The development of efficient methods to sequester $CO_2$ resulting from combustion and other industrial processes is gaining importance, as $CO_2$ is a major greenhouse gas and should be removed from emissions to prevent release into the atmosphere. Zeolites possess favourable energetic interaction properties for sequestering and adsorbing $CO_2$ from flue gases, which are primarily mixtures of $CO_2$ with $N_2$ and light hydrocarbons, like $CH_4$. Some zeolites occur in nature, while other ones, such as ZSM-5 studied in this paper, can be synthesized industrially or in the laboratory.

Published online: 11 July 2013

![](./images/813211816581660672_1.jpg)

They can be applied as the active layer in membrane separations, pressure swing adsorption, ion exchange and other methods of separating and removing components from gases and liquids, as well as in catalysis (Bonenfant et al. 2008; Kärger and Ruthven 1992; Keil et al. 2000; Smit and Maesen 2008).

Zeolites are crystalline aluminosilicates composed mainly of Si surrounded by four O atoms, have well-defined nanoporous topologies, and are stable at high temperatures. A net negative charge of $-1e$ develops in the zeolite when a tetravalent Si atom is replaced by a trivalent Al atom. A cation from Groups I or II, such as $H^+$, $Na^+$, $Ca^{2+}$ or $Mg^{2+}$ is needed to counter-balance these charge deficits (Bonenfant et al. 2008; Dunne et al. 1996b; Katoh et al. 1998, 2000; Kusakabe et al. 1998; Pillai et al. 2010; Walton et al. 2006; Wirawan and Creaser 2006a, b; Yamazaki et al. 1993). ZSM-5 is known to accommodate a wide range of Si to Al atomic ratios, Si/Al. When $\text{Si/Al} = \infty$, ZSM-5 is referred to as silicalite-1, the Al-free form. A lower Si/Al ratio means that there are more Al and cations present, so that the zeolite manifests higher energetic heterogeneity and the capability to adsorb larger quantities of polarizable molecules such as $CO_2$ and $N_2$.

The ZSM-5 pore network topology consists of straight channels in the $y$ direction and zigzag, or sinusoidal, channels in the $x$–$z$ plane, which are joined at regular intersections every $10$ Å. The channel pore diameter is $\sim5.5$ Å, which permits accessibility of small gas molecules such as $CO_2$, $N_2$, and alkanes as long as $C_{10}H_{22}$. The ZSM-5 pore network topology is schematically presented in Fig. 1.

Membranes have been synthesized from several zeolites and similar materials, including ZSM-5, faujasite, DDR, SAPO-34, and the metal–organic framework UMCM-1. Experimental membrane separation studies have focused on light gas mixtures, including $CO_2$, $CO$, $N_2$, $CH_4$, $C_2H_6$, and $O_2$ (Bernal et al. 2004; Bowen et al. 2003; Himeno et al. 2007; Kusakabe et al. 1998; Mu et al. 2010; Noack et al. 2000; Zhou et al. 2007; Zhu et al. 2006). Many other experimental studies have focused on the adsorption properties of zeolites. These concerned adsorption in a wide range of zeolites and other nanoporous materials (silicalite-1, Na–ZSM-5, H–ZSM-5, Na–X, 13X, 4A, activated carbon) for many guest adsorbates ($CO_2$, $CO$, $N_2$, $H_2$, $SF_6$, $CH_4$–$C_4H_{10}$), at temperatures typically around 300 K (overall range of 277–473 K) and pressures below 20 bar. Many of these zeolites contained cations such as $Na^+$, $H^+$, $Li^+$, $K^+$, $Ba^+$, and $Cs^+$, which affects their adsorption properties (Calleja et al. 1998; Dunne et al. 1996a, b; Harlick and Tezel 2002, 2003, 2004; Siriwardane et al. 2001; Sun et al. 1998; Walton et al. 2006; Wirawan and Creaser 2006a, b).

![](./images/813211816581660672_2.jpg)

Fig. 1 Channel structure of ZSM-5, having an orthorhombic MFI framework with $a=20.1$ Å, $b=19.9$ Å, $c=13.4$ Å

These experimental adsorption studies all demonstrate that cations play a very important role, as in all of the above cases the amount of adsorbed $CO_2$ increased with lower Si/Al and greater cation content due to the strong electrostatic interactions. $Na^+$ and other cations could improve the adsorption selectivity of $CO_2$ over $N_2$, $H_2$, $CH_4$, etc. Also considered in these studies were the effects of pore topology, pore volume, and the role of the shape and size of the guest molecules, i.e., confinement effects. Molecular simulations complement experimental studies, providing a link between the molecular scale features of the zeolite and guest molecules to experimentally observed macroscopic properties, such as diffusivities, adsorption isotherms, and isosteric heats of adsorption. Fundamental understanding of adsorption and diffusion processes is beneficial for a priori understanding and rational design of unit operations applying zeolites. The determination of the adsorption isotherms, from either experiments or Grand Canonical Monte Carlo (GCMC) simulations, is a crucial step to correlate operating pressures to the amounts adsorbed in a zeolite sample, which is a prerequisite to calculate membrane permeation rates.

Prior GCMC studies have been successfully compared to experiments. June et al. (1990) considered the adsorption of various light alkanes adsorbed in silicalite-1, showing reasonable agreement with experimental measurements of Henry’s constants and isosteric heats of adsorption at low loading. Skoulidas and Sholl (2002, 2003) studied the adsorption of various light gases in ZSM-5, ZSM-12, ITQ-3, and ITQ-7, such as $CH_4$, $CF_4$, Xe, and $SF_6$ at $T=300$ K. Makrodimitris et al. (2001) studied both $CO_2$ and $N_2$ adsorption in silicalite-1 at $T=300$ K, showing consistent agreement with a range of experimental sources (Papadopoulos et al. 2004). Also other GCMC studies have considered the adsorption of a range of guest molecules ($CO_2$, $N_2$, $CH_4$, $CF_4$, $H_2$, $NH_3$, $H_2O$, and various alkanes) in various zeolites (silicalite-1, ITQ-3, ITQ-7, ETS-10, Na-4A). Simulation results were in excellent agreement with experiments, giving confidence that simulations can be a quantitative predictive tool (Beerdsen et al. 2002, 2003; Gallo et al. 2006; Garcia-Perez et al. 2007;

Adsorption

Goj et al. 2002; Heuchel et al. 1997; Jaramillo and Chan- dross 2004; Selassie et al. 2008). Though some of these simulations did consider the role of cations, most of them applied GCMC to model light-gas adsorption in all-silica zeolites only and did not consider the effects of cations, such as $Na^+$, on the adsorption of quadrupolar molecules such as $CO_2$ and $N_2$.

Our study considers the adsorption of $CO_2$ and $N_2$ in the zeolite ZSM-5 impregnated with $Na^+$ cations. ZSM-5 was chosen due to its widespread interest for membrane sepa- rations and gas storage, and serves as a good case study to better understand how cations can play a role in comparing simulations to experiment. The key issues are the impact of Si/Al on enhancing $CO_2$ and $N_2$ adsorption, especially at low pressures, and the influence of the effective charge of $Na^+$ on adsorption. GCMC simulations were used to pre- dict adsorption isotherms and isosteric heats of adsorption for a range of Si/Al. Analogous experimental measure- ments for $CO_2$ and $N_2$ in Na-ZSM-5 at Si/Al = 13 are compared to the GCMC simulations to estimate the effective charge of the $Na^+$ cations.

The following section discusses the methodology of the GCMC simulations to determine the adsorption isotherms and isosteric heats of adsorption, which are calculated for Si/Al $=\infty$, 95, 47, 31, 23, and 13. The second section explains the experimental methodology. The simulation results are next presented for $CO_2$ and $N_2$ at $T=308$ K and then compared to experimental measurements.

## 2 Methodology

### 2.1 Grand Canonical Monte Carlo (GCMC)

GCMC samples the $\mu VT$ ensemble, in which the chemical potential $\mu$, the volume $V$, and the temperature $T$ are held constant, but the number of molecules $N$ is allowed to fluctuate. GCMC is suitable for adsorption studies, since the number of adsorbed molecules increases as a function of pressure $P$, which is related to $\mu$. In thermodynamic and thermal equilibrium the chemical potential and the tem- perature of the gas inside and outside the adsorbent must be equal. The gas that is in contact with the adsorbent can be considered as the bulk gas that imposes the temperature and chemical potential on the adsorbed molecules. Thus, when the temperature and the chemical potential (or pressure) of the bulk gas are specified, the equilibrium concentration inside the adsorbent is directly determined (Frenkel and Smit 2002; Vlugt et al. 2008).

The partition function cannot be exactly calculated in a given ensemble due to the extremely large number of possible states (Frenkel and Smit 2002; Vlugt et al. 2008). However, ensemble averages can still be computed without calculating the partition function itself by invoking importance sampling. Many of the system states have a Boltzmann weight close to zero, so that they do not make a meaningful contribution to the ensemble average. This observation is the basis for generating a Markov chain of ensemble states $S$, where $S=1,2,3,...$, with a probability proportional to their Boltzmann factor $\exp[-\beta U(j)]$ ($\beta=1/k_bT$) for any state $j$ with total potential energy $U(j)$. The objective of the Monte Carlo method is to efficiently sample a Markov chain, so that ensemble averages can be determined, via the requirement of detailed balance. This condition says that if an old configuration $S=o$ is moved to a new configuration $S=n$, the overall equilibrium dis- tribution of configuration states $S=j$ should not be changed. That is, the probability to leave a configuration $S=o$ must be balanced by the probability to return to this same state from any given new configuration $S=n$. Acceptance probabilities, $acc(o\rightarrow n)$, can be derived for various types of stochastic moves to propagate the Markov chain of ensemble configuration states. The reader is referred to Frenkel and Smit (2002), and Vlugt et al. (2008) for further details behind the derivations of these accep- tance probabilities. A Monte Carlo simulation algorithm consists of two stages. First, a random trial move is per- formed from the old configuration $S=o$ to the new con- figuration $S=n$. The next step is to decide whether this trial move is accepted or rejected. In order to decide to accept or reject a trial move, a random number, $Ranf$, is generated in the range [0, 1], with a uniform distribution (Frenkel and Smit 2002; Vlugt et al. 2008). If $Ranf < acc(o\rightarrow n)$ the trial move is accepted; otherwise it is rejected. This will guarantee that the probability to accept a trial move from $o$ to $n$ is equal to $acc(o\rightarrow n)$.

In standard GCMC four types of stochastic moves can be performed: particle displacement translation moves, inser- tion moves, deletion moves, and identity exchanges for the case of mixtures (Frenkel and Smit 2002; Vlugt et al. 2008). In a translation move a molecule is randomly chosen and then randomly displaced to a new location. The change in potential energy is evaluated via the Boltzmann weight. In an insertion move a molecule from the gas phase is randomly inserted into the simulation box. If it overlaps with the zeolite lattice, the Boltzmann weight is extremely low and the move is rejected. If it is inserted into the free volume of the pore and away from the lattice walls, then it is most likely accepted. In a deletion move a molecule is randomly selected and removed. If the change in potential energy is favourable, this move is accepted. In an identity swap, a random molecule is chosen and its identity is changed from one species to the other one. This move is necessary to properly model competitive adsorption. The analytical forms of the acceptance rules for these four types of moves have been described in detail by Frenkel and Smit (2002).

![](./images/813211816581660672_3.jpg)

Every one of the simulations consists of $50 \times 10^6$ moves, with $30 \times 10^6$ moves for equilibration to account for the large number of insertion rejections from overlaps with the zeolite lattice. The temperature in the simulations were set at $T = 308$ K, as this was the temperature of many experimental studies. The pressure typically ranges from $P = 10^{-5}$ to 20 bar of total pressure. For $\text{CO}_2$ when $\text{Si/Al} = 31$, 23, and 13, pressures as low as $P = 10^{-9}$ bar were simulated. These extremely low pressures were applied for those situations since a significant number of $\text{CO}_2$ molecules were adsorbed even at these very low pressures. The simulation box consists of 27 unit cells, three in each direction, to ensure a large enough box for the short-range cut-off radius and also to gather enough statistical contributions. Periodic boundary conditions were applied in all three directions.

### 2.2 Adsorption isotherms

An adsorption isotherm is a function that represents the adsorption of guest molecules into a host solid material, such as a zeolite, at a constant temperature, over a range of pressures, due to the favorable energetic interactions of the guest molecules with the host. At low pressures the guest molecules will tend to find the sites with the lowest potential energy and space themselves apart. At higher pressures all sites of the host material will be filled by guest molecules, leading to a saturation plateau.

### 2.3 Isosteric heat of adsorption

The energetic response to adsorption by the adsorbate molecules within the host adsorbent are best described by the isosteric heat of adsorption (Myers 2002; Myers and Prausnitz 1965), $Q_{st}$, which can be defined as

$$
Q_{st} = \Delta H_{ads} \equiv H_{ads} - H_{gas} = RT^2 \left( \frac{\partial \ln P}{\partial T} \right)_N , \tag{1}
$$

where $\Delta H_{ads}$ is the change in enthalpy due to adsorption (kJ/mol), $H_{ads}$ is the enthalpy of the molecules while adsorbed in the zeolite, $H_{gas}$ is the enthalpy in the ideal gas phase, $R = 8.314$ J/mol K is the gas constant, $T$ is the temperature (K), $P$ is pressure (bar), and $N$ is the adsorbate loading (molecules/Unit Cell) (Gallo et al. 2006; Goj et al. 2002; Heuchel et al. 1997; Myers 2002; Myers and Prausnitz 1965; Yun et al. 2002). The isosteric heat defines the change in enthalpy due to guest molecules leaving the ideal gas bath and entering into the host material. This enthalpy of adsorption is interpreted as due to a phase change; hence, the Clausius–Clapeyron equation can be used, as in Eq. 1 (Myers 2002; Myers and Prausnitz 1965). A higher isosteric heat of adsorption indicates a more favourable energetic preference of the host environment to the guest molecules, implying a higher adsorption capacity at a given lower pressure. This quantity can be used to screen and compare trial host materials (Dunne et al. 1996a, b; Düren et al. 2004; Gallo et al. 2006; Goj et al. 2002; Heuchel et al. 1997; Pan et al. 2004; Yun et al. 2002). $Q_{st}$ can be obtained by taking the derivative of the pressure that imposes a specified loading $N$ over a range of temperatures, but this technique can lead to systematic noise due to imperfectly fitting multiple isotherms at a particular loading. Rather, the fluctuation theorem gives a more stable measurement of $Q_{st}$ from a single simulation and a specified $P$ and $T$. This alternative formulation uses the fluctuations in the total potential energy (Düren et al. 2004; Goj et al. 2002), $U$ (kJ/mol), so that

$$
Q_{st} = RT - \frac{\langle UN \rangle - \langle U \rangle \langle N \rangle}{\langle N^2 \rangle - \langle N \rangle^2} . \tag{2}
$$

### 2.4 Atomistic description

ZSM-5 is modeled as a crystalline solid of a nominal $\text{SiO}_2$ composition with orthorhombic structure, where many $\text{SiO}_2$ tetrahedrons periodically arrange themselves to form porous crystal lattices. The lattice coordinates from van Koningsveld et al. (1987) were used to construct the defect-free ZSM-5 framework, as shown in Fig. 2. This zeolite has the general stoichiometric formula $\{\text{Na}_x\text{Al}_x\text{Si}_{(96-x)}\text{O}_{192}\}$. Al substitutions were subsequently made in the range of $X = 0$, 1, 2, 3, 4, and 7 ($\text{Na}^+ + \text{Al}$)/Unit Cell, or $\text{Si/Al} = \infty$, 95, 47, 31, 23, and 13. $\text{Na}^+$ cations were assumed to be frozen in space and treated as an extra framework species close to the Al framework substitutions, as done in prior GCMC simulations (Liu and Yang 2006; Pillai et al. 2007). Molecular dynamic simulations that were performed of this system showed that the $\text{Na}^+$ cations did not diffuse away from their initial locations, only slightly vibrating and were essentially tethered to the Al atom site. Keeping the cations fixed is therefore a reasonable assumption for the GCMC simulations discussed in this paper. The $\text{Al}$ and $\text{Na}^+$ atomic pairs were placed in the intersections, as to match the cation siting pattern assumed in prior dynamic Monte Carlo studies that analyzed the impact of cation-based energetic heterogeneity (Coppens et al. 1998, 1999; Coppens and Iyengar 2005; Liu et al. 2009). In contrast, Beerdsen et al. (2002, 2003) have shown how the cations can be assumed to also be located in the channels, partially blocking the transport space, while the cations in intersections would have a relatively mild blocking effect. It is expected that the adsorption results will be a function of the exact locations of the cations, in terms of steric hindrance and amount of exposed charge on the cations. A prior DFT and experimental study by

![](./images/813211816581660672_4.jpg)

![](./images/813211816581660672_5.jpg)

Fig. 2 Atomistic perspective of ZSM-5; silicon atoms are in yellow, oxygen atoms in red (Color figure online)

Sklenak et al. (2009) has shown that the cation locations vary due to synthesis conditions. Comparison of the simulation results to experimental data later in this study indicates that locating cations in the intersections gives reasonable agreement.

CO₂ and N₂ molecules were both modeled as linear triatomic molecules, with carbon dioxide containing a C atom in the center and two O atoms at both ends; and nitrogen containing a zero-mass atom in the center and two N atoms at both ends. Though N₂ is actually a diatomic molecule, a fictional zero-mass site (m_z) is added to the molecule so that a quadrupole could be modeled with overall charge neutrality. This type of charge distribution allows inclusion of Coulombic interactions for both N₂ and CO₂ molecules with the zeolite framework. The two molecules are depicted in Fig. 3, in which q depicts the partial charge of each atom. The three point charges together create the quadrupole moment due to their spatial arrangement. CO₂ has two bonds with length of 1.16 Å and a quadrupole moment of $\mu_{\mathrm{CO}_{2}}=-13.67 \times 10^{-40} \mathrm{C} \mathrm{m}^{2}$. N₂ has a single bond of length of 1.10 Å and a quadrupole moment of $\mu_{\mathrm{N}_{2}}=-4.67 \times 10^{-40} \mathrm{C} \mathrm{m}^{2}$ (Makrodimitris et al. 2001).

### 2.5 Interatomic interactions

In GCMC the acceptance rules only require calculations of changes in total potential energy. There are two types of potentials that describe the interaction between atomic sites: the short-range dispersion potential, and the long-range electrostatic (or Coulombic) potential. These interactions occur between the atomic sites of the zeolite and the atomic sites of the guest molecule, and amongst atomic sites between the guest molecules (Frenkel and Smit 2002).

The short-range potential energy $U_{S R}(r)$ is described by a pair-wise Lennard-Jones potential,

$$
U_{S R}(r)=4 \varepsilon\left[\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^{6}\right], \tag{3}
$$

where $r$ is the distance between the atoms (Å), $\varepsilon$ is the depth of the energy well (kJ/mol), and $\sigma$ is the characteristic length at which the interatomic potential becomes zero (Å). The term $\left(\frac{\sigma}{r}\right)^{12}$ represents the interatomic site-to-site repulsions between different molecules, while the term $\left(\frac{\sigma}{r}\right)^{6}$ represents the interatomic attraction due to London dispersion. A cut-off radius of 13 Å is used (Makrodimitris et al. 2001; Skoulidas and Sholl 2002). The energy parameters are listed in Table 1 and are taken from literature (Beerdsen et al. 2002, 2003; Hirotani et al. 1997). The Lorentz-Berthelot rules are used to estimate the interaction parameters for the cross-site-guest interactions and the zeolite oxygen atom and guest-site interactions.

![](./images/813211816581660672_6.jpg)

Fig. 3 Three-site atomic description of CO₂ and N₂ molecules

The long-range potential energy $U_{L R}(r)$ describes the electrostatic interactions (Frenkel and Smit 2002;

<table>
<caption>Table 1 Potential parameters used to represent the zeolite framework and guest molecules</caption>
<thead>
<tr>
<th>
</th>
<th colspan="2">LJ parameters</th>
<th>
</th>
<th>Partial<br>charges,<br>q (e)</th>
</tr>
<tr>
<th>
</th>
<th>$\varepsilon/k_B$ (K)</th>
<th>$\varepsilon$ (kJ/mol)</th>
<th>$\sigma$ (Å)</th>
<th>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zeolite</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Si</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>+2/+2.05</td>
</tr>
<tr>
<td>O_z</td>
<td>89.6</td>
<td>0.745</td>
<td>2.806</td>
<td>−1/−1.025</td>
</tr>
<tr>
<td>Al</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>+1.75</td>
</tr>
<tr>
<td>O_Al</td>
<td>89.6</td>
<td>0.745</td>
<td>2.806</td>
<td>−1.2</td>
</tr>
<tr>
<td>CO₂</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>C</td>
<td>27.0</td>
<td>0.22</td>
<td>2.80</td>
<td>+0.7</td>
</tr>
<tr>
<td>O_g</td>
<td>79.0</td>
<td>0.65</td>
<td>3.05</td>
<td>−0.35</td>
</tr>
<tr>
<td>N₂</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>N</td>
<td>36.0</td>
<td>0.30</td>
<td>3.31</td>
<td>−0.404</td>
</tr>
<tr>
<td>m_Z</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>+0.81</td>
</tr>
<tr>
<td>Cation</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Na</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>+1</td>
</tr>
<tr>
<td>Na–C</td>
<td>20.44</td>
<td>0.17</td>
<td>2.72</td>
<td>N/A</td>
</tr>
<tr>
<td>Na–O_g</td>
<td>34.88</td>
<td>0.29</td>
<td>2.83</td>
<td>N/A</td>
</tr>
<tr>
<td>Na–N</td>
<td>105.8</td>
<td>0.88</td>
<td>2.82</td>
<td>N/A</td>
</tr>
</tbody>
</table>

Second charge is for Si and O_Z when Al is present. Parameters taken from Beerdsen et al. (2002, 2003), and Hirotani et al. (1997)

![](./images/813211816581660672_7.jpg)

Makrodimitris et al. 2001), as defined by Coulomb's law, which takes the form

$$
U_{L R}(r)=\frac{1}{4 \pi \varepsilon_{0}} \frac{q_{1} q_{2}}{r}, \tag{4}
$$

where $q_{1}$, and $q_{2}$ are the partial charges on atomic sites 1 and 2 (e), and $\varepsilon_{0}$ is the permittivity of the vacuum. The contributions of the electrostatic potential energy between the adsorbate molecules are calculated through the Ewald summation method, which is a well-known numerical technique to take into account long-range forces described by Eq. 4 (Frenkel and Smit 2002). A long-range cut-off radius of $20 \AA$ is used. Table 1 lists the charges used (Beerdsen et al. 2002, 2003).

Due to the long-range nature of Coulomb's law, the numerical implementation of Eq. 4 is computationally burdensome when accounting for all of the interactions between the zeolite atoms and the guest molecules. To reduce this effort, the electrostatic interactions between the adsorbate and the zeolite are calculated on the basis of a one-time calculation to pretabulate the electrostatic potential (Goj et al. 2002; June et al. 1990; Makrodimitris et al. 2001; Skoulidas and Sholl 2002, 2003), making the assumption that the zeolite atoms are rigid. Prior studies have shown that this assumption is reasonable for relatively small guest molecules (Makrodimitris et al. 2001; Papadopoulos et al. 2004; Skoulidas and Sholl 2002). Equation 4 was solved for each zeolite atom in each unit cell, where the unit cell is replicated in space for ten surrounding layers in three dimensions. This leads to a large number of zeolite unit cells, but this is necessary to take into account the long-range nature of Coulomb's law. A ghost atom of charge 1e is placed on a grid of spacing $\sim 0.2 \AA$, allowing pre-calculation of the potential energy and its derivatives at each point. Once the values have been tabulated in a massive grid, they are then read into the GCMC algorithm. An interpolation scheme is implemented to get specific values of the potential energy, as described by Makrodimitris et al. (2001) and Skoulidas and Sholl (2002).

### 2.6 Experimental methodology

Two Na-ZSM-5 samples, one with $\mathrm{Si} / \mathrm{Al}=13$ and a second one with $\mathrm{Si} / \mathrm{Al}=45$, were provided by Dr. Ernst Köhler from Süd-Chemie AG (München, Germany). Low-coverage adsorption properties of $\mathrm{CO}_{2}$ and $\mathrm{N}_{2}$ were determined by pulse chromatography for the Na-ZSM-5 zeolite with $\mathrm{Si} / \mathrm{Al}=13$ (Couck et al. 2010; Duerinck et al. 2012). Powder of this zeolite was shaped into binderless pellets by pressing the powder to a disk at a pressure of 600-700 bar, crushing this disk and sieving the fragments to the $500-630 \mu \mathrm{m}$ range. Pellets were packed in stainless steel columns with a length of 0.3 m and an internal diameter of 0.216 cm. The material in the column was activated by heating the column under constant helium flow to 623 K at a rate of 1 K/min and maintaining this temperature overnight. A trace amount of the compounds (20-50 $\mu$ l of gas) was injected in the inlet of an HP-4890 gas chromatograph and carried through the column with helium as inert carrier gas. The response curve was measured at the outlet of the column with a thermal conductivity detector. Experiments were performed at temperatures between 373-473 K for $\mathrm{CO}_{2}$ and 303-333 K for $\mathrm{N}_{2}$. Henry constants $K^{\prime}$ were calculated from the first-order moment of the chromatogram. Adsorption enthalpies, $\Delta H_{a d s}$, and pre-exponential factors, $K_{0}^{\prime}$, were calculated from the temperature dependency of the Henry constants using the van't Hoff equation. These results are also presented in the online supplementary data.

Adsorption isotherms for $\mathrm{CO}_{2}$ and $\mathrm{N}_{2}$ were measured for both Na-ZSM-5 samples at temperatures of 273, 283, 293, and 308 K and pressures up to 1 bar with a Quantasorb AS-1 surface area analyser. Materials were activated in situ at 623 K before the measurements. The adsorption data at the four temperatures were then fitted to the virial equation and interpolated at fixed adsorbed amount to determine the heat of adsorption as a function of loading by using the final form of Eq. 1. For some loadings the fitting of the virial equation was of poor quality, so that no estimate of the isosteric heat was made at that loading.

## 3 Results and discussion

### 3.1 Isosurface plots

The GCMC algorithm implements a stochastic sampling of the molecular positions in a given potential energy landscape. These positions are therefore a sampling of the most probable configurations of the $\mathrm{CO}_{2}$ or $\mathrm{N}_{2}$ molecules. This procedure gives insight into where the molecules preferentially locate themselves over a range of pressures. The shape and locations of the stable basins can be determined by making isosurface plots at increasing levels of a minimum threshold density, $\rho_{Min}$. The density is defined as the local count of molecules in a small volume unit $(0.2 \AA)^{3}$ divided by this volume. It is proportional to the Boltzmann weight of the local potential landscape and therefore directly samples the energy landscape. A larger threshold density indicates deeper energy levels and hence shows the more populated (and energetically preferred) local regions in the zeolite.

To improve the statistics, the results from all 27 unit cells are averaged together, since they are periodic structures. In the first case study of silicalite-1, three values of

![](./images/813211816581660672_8.jpg)

$\rho_{Min}$ are considered: $10^{-4}$, 25, and $50\ \text{nm}^{-3}$, as presented in Fig. 4a–c. For comparison, the density of bulk liquid $\text{CO}_2$ at 1 bar is $\rho \approx 13.7\ \text{nm}^{-3}$, so that the stable basins are denser than the $\text{CO}_2$ liquid phase. In the case of $\rho_{Min}=10^{-4}\ \text{nm}^{-3}$, nearly all accessible space is shown, indicating the entire pore topology. At $\rho_{Min}=25\ \text{nm}^{-3}$ a large volume of the regions at the intersections has vanished, since this region is less preferred by the $\text{CO}_2$ molecules, while the channel basins are still intact. At the highest density of $\rho_{Min}=50\ \text{nm}^{-3}$, the intersections have essentially vanished, yet the channel basins are still intact. The same pattern was observed for $\text{N}_2$.

The isosurface results for the case study of $\text{Si/Al}=95$ are presented in Fig. 5a, b, at two of the same $\rho_{Min}$ levels as for silicalite-1. The overall topological pattern is the same as for silicalite-1, but now each $\text{Na}^+$ cation imposes on a void space, while allowing molecules to remain nearby it. This allows the overall concentration to go from 8.87 to $12.74\ \text{CO}_2/\text{Unit Cell}$ at $P=1$ bar, comparing silicalite-1 to $\text{Si/Al}=95$. By studying the isosurface plot for $\rho_{Min}=10^{-4}$ and $50\ \text{nm}^{-3}$, the $\text{CO}_2$ molecules are observed to congregate around the $\text{Na}^+$ cation in the intersection regions, which helps to visually explain the increase of $\sim 4\ \text{CO}_2/\text{Unit Cell}$.

![](./images/813211816581660672_9.jpg)

Fig. 4 The isosurface plots of pure $\text{CO}_2$ in silicalite-1 at $T=308\ \text{K}$ and $P=1$ bar. a $\rho_{Min}=10^{-4}\ \text{nm}^{-3}$, b $\rho_{Min}=25\ \text{nm}^{-3}$, and c $\rho_{Min}=50\ \text{nm}^{-3}$, looking down along the $z$ axis

![](./images/813211816581660672_10.jpg)

![](./images/813211816581660672_11.jpg)

Fig. 5 The isosurface plots of pure $CO_{2}$ in ZSM-5 with $Si/Al=95$ at $T=308$ K and $P=1$ bar. a $\rho_{Min}=10^{-4}\ nm^{-3}$ and b $\rho_{Min}=50\ nm^{-3}$

The analogous results for the case study of $Si/Al=47$ are presented in Fig. 6a, b, where a second cation has now been inserted into a second intersection. The $CO_{2}$ molecules spread themselves amongst the two $Na^{+}$ cations, as seen in the topology images for $\rho_{Min}=50\ nm^{-3}$, Fig. 6b. At $P=1$ bar the overall loading for $Si/Al=47$ is actually very close to the loading for $Si/Al=95$, changing from 12.74 to $12.27\ CO_{2}/$Unit Cell. Since there are $2\ Na^{+}/$Unit Cell for $Si/Al=47$, the $CO_{2}$ molecules that adsorb from the pore space at lower pressures interact with these $Na^{+}$ cations, competing with the cations (per Unit Cell) and, hence, diminishing the influence of the $Na^{+}$ cations.

### 3.2 Adsorption isotherms
Adsorption isotherms for pure $CO_{2}$ at $T=308$ K within the pressure range from $P=10^{-9}$ to 20 bar are shown in Fig. 7, and for pure $N_{2}$ from $10^{-6}$ to 300 bar in Fig. 8. Work by Makrodimitris et al. (2001) and Goj et al. (2002) produced similar adsorption isotherms for silicalite-1, which are both very similar to the simulation results in this study. Both Figs. 7 and 8 show that Na-ZSM-5 adsorbs more than silicalite-1, as the $Na^{+}$ cations favourably interact with the quadrupolar molecules. The adsorption isotherms of Na-ZSM-5 show a two-step pattern with

![](./images/813211816581660672_12.jpg)

Fig. 6 The isosurface plots of pure $CO_{2}$ in ZSM-5 with $Si/Al=47$ at $T=308$ K and $P=1$ bar. a $\rho_{Min}=10^{-4}\ nm^{-3}$ and b $\rho_{Min}=50\ nm^{-3}$

![](./images/813211816581660672_13.jpg)

respect to pressure. At low pressures the guest molecules adsorb to the cations due to the lower potential energy (i.e., stronger electrostatic interactions), reaching a first plateau. At higher pressures, the silicalite-1 type regions of higher potential energy begin to populate, showing a more rapid increase due to more accessible pore space. $CO_2$ is able to reach the second plateau around 20 bar, while the amount of $N_2$ adsorbing is still increasing even at 300 bar.

At $P \leq 10^{-1}$ bar there are only a few $CO_2$/Unit Cell and essentially no $N_2$ adsorbed in silicalite-1, while a meaningful amount is present in Na-ZSM-5. At lower pressures loading shows a clearly increasing trend (at a given pressure) with decreasing Si/Al, as more $Na^+$ cations are present and freely exposed. Table 2 contains the pressures where approximately 1 guest molecule/Unit Cell is observed, showing how a lower Si/Al roughly corresponds to lower pressures where a substantial amount is adsorbed. For example, at very low pressures, say $P = 10^{-3}$ bar, there is no meaningful presence of $CO_2$ or $N_2$ in silicalite-1. In contrast, the loading for $CO_2$ in Na-ZSM-5 is 1–5 $CO_2$/Unit Cell for all Si/Al ratios, while for $N_2$ it is $\sim 2$ $N_2$/Unit Cell for Na-ZSM-5 at Si/Al = 31, 23, and 13. At $P = 10^{-1}$ bar, there is 1 $CO_2$/Unit Cell in silicalite-1, but still no meaningful presence of $N_2$. In contrast, the loading for $CO_2$ in Na-ZSM-5 is 5–15 $CO_2$/Unit Cell for all Si/Al, while for $N_2$ it is $\sim 1$ to 2.5 $N_2$/Unit Cell for all Si/Al. The pressures for $CO_2$ and $N_2$ for Si/Al = 13, 23, and 31 are close but do not follow a perfect trend, presumably because the cations have different interaction energies due to the different locations relative to the nearby lattice atoms. The adsorption pressures therefore reflect the sampling of these different adsorption energy regions. The isosteric heats discussed later support this conclusion.

For $CO_2$ at $P > 1$ bar the adsorption isotherms for the six case studies of Si/Al consistently get closer to each other due to increased local saturation of the $Na^+$ cations. The first few $CO_2$ molecules that adsorb into the ZSM-5 pore space locally saturate and effectively compete with the attractive electrostatic interactions with the $Na^+$ cations. Even though the $Na^+$ cations maintain an attractive interaction with the guest molecules, the effect becomes substantially weaker since the guest molecules nearby the cation tend to counterbalance these favourable interactions due to the negative partial charge at the ends of the guest molecule. At higher pressures, say $P > 5$ bar, the adsorption isotherms for $CO_2$ in Na-ZSM-5 reach their saturation loadings. These saturation values are rather close to the silicalite-1 saturation loading, since at high enough pressures all the accessible space must be occupied, but the presence of the $Na^+$ cations increases the saturation loading over silicalite-1 by $\sim 1$ to 4 $CO_2$ molecules/Unit Cell. The $N_2$ adsorption isotherms have not yet reached saturation even at $P = 20$ bar. For this molecule the saturation loading is also systematically higher than the silicalite-1 reference value by $\sim 1$ to 4 $N_2$ molecules/Unit Cell at higher pressures.

![](./images/813211816581660672_14.jpg)

Fig. 7 Amount of adsorbed $CO_2$ as a function of pressure for a large pressure range at $T = 308$ K for six Si/Al ratios

![](./images/813211816581660672_15.jpg)

Fig. 8 Amount of adsorbed $N_2$ as a function of pressure for a large pressure range at $T = 308$ K for six Si/Al ratios

<table>
<caption>Table 2 List of pressures where the guest molecules reach a loading of 1 molecule/Unit Cell</caption>
<thead>
<tr>
<th>Si/Al</th>
<th>$P_{CO_2}$ (bar)</th>
<th>$P_{N_2}$ (bar)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\infty$ (silicalite-1)</td>
<td>0.025</td>
<td>1.75</td>
</tr>
<tr>
<td>95</td>
<td>$5(10^{-4})$</td>
<td>0.15</td>
</tr>
<tr>
<td>47</td>
<td>$1(10^{-4})$</td>
<td>0.015</td>
</tr>
<tr>
<td>31</td>
<td>$1(10^{-7})$</td>
<td>$2.5(10^{-5})$</td>
</tr>
<tr>
<td>23</td>
<td>$3(10^{-9})$</td>
<td>$5(10^{-7})$</td>
</tr>
<tr>
<td>13</td>
<td>$2(10^{-7})$</td>
<td>$7.5(10^{-5})$</td>
</tr>
</tbody>
</table>

A key trend observed in Figs. 7 and 8 is the near-equality or crossover of adsorption isotherms of Na-ZSM-5 for several pairs of Si/Al ratios, especially for $N_2$. At lower pressures, the $Na^+$ cations are not saturated and adsorption tends to be higher at lower pressures for lower Si/Al, for both $CO_2$ and $N_2$, though the loading amounts to only 1 or 2

![](./images/813211816581660672_16.jpg)

molecules/Unit Cell. For $CO_2$ the adsorption isotherms for Si/Al = 95 and 47 are very similar at $P = 10^{-1}$ bar and 6.5 $CO_2$/Unit Cell, with the loading for Si/Al = 95 and 47 remaining close for higher pressure. The simulated adsorption isotherm of $CO_2$ for Si/Al = 23 shows a very broad plateau of $\sim$2 to 2.5 $CO_2$/Unit Cell from $P = 10^{-8}$-$10^{-3}$ bar; it crosses the isotherms for Si/Al = 31 and 13 around $P = 10^{-5}$ bar. The adsorption isotherm for Si/Al = 23 is systematically higher, though close, to the adsorption isotherm for Si/Al = 31 over the entire pressure range. However, the adsorption isotherm for Si/Al = 23 is higher by $\sim$1 $CO_2$/Unit Cell compared to the adsorption isotherm for Si/Al = 13 for $P \leq 10^{-5}$ bar. At higher pressures, the adsorption isotherm for Si/Al = 13 is substantially higher than all other adsorption isotherms with higher Si/Al ratio due to the higher surface area associated to cations. Presumably, the crossover at low pressure between the adsorption isotherms of Si/Al = 13 and 23 is due to slightly different interaction strengths. The presence of the second cation in the intersections was observed to effectively create a second stable basin nearby the stable basin at the first cation, but of weaker strength. The $CO_2$ molecules sample between these various stable basins and its average adsorption becomes weaker, so that the adsorption isotherms for Si/Al = 13 will be slightly lower than for Si/Al = 23 at low pressures, which agrees with the trend in Table 2. At higher pressures, the greater surface area of cations for Si/Al = 13 becomes more relevant, so that the adsorption isotherm for Si/Al = 23 becomes lower compared to the adsorption isotherm of Si/Al = 13.

Competition between the cations and adsorbed $N_2$ molecules causes similar crossovers in the $N_2$ adsorption isotherms, similar to the trends observed for $CO_2$. Like $CO_2$, at low pressure, the $N_2$ adsorption isotherms show the intuitive trend of higher loadings at lower Si/Al ratio. However, the adsorption isotherm for Si/Al = 95 crosses the adsorption isotherms for both Si/Al = 47 and 23 at $P = 0.7$–1 bar and 2.6–3 $N_2$/Unit Cell, while the adsorption isotherms for Si/Al = 31 and 13 also cross and then exceed the adsorption isotherm for Si/Al = 23 at $P = 10^{-3}$ bar and 2.5 $N_2$/Unit Cell. After the crossover points, Na–ZSM-5 for Si/Al = 95 adsorbs more $N_2$ than Si/Al = 47 and 23 by $\sim$1 to 2 $N_2$/Unit Cell, but consistently less than for Si/Al = 31 ($\sim$1 $N_2$/Unit Cell difference). The adsorption isotherm for Si/Al = 13 remains $\sim$2 to 4 $N_2$/Unit Cell higher than the other adsorption isotherms after the crossover point, so that the overall much higher concentration of cations better competes with the adsorbed $N_2$.

Counterintuitive as these crossover trends seem, they highlight the importance of molecular simulations to gain understanding in the fundamental mechanisms. The observed trends result from a subtle balance between various interactions among cations and guest molecules. Since $Na^+$ cations also take up part of the pore space, they could hinder adsorption of guest molecules. At increasing pressures the guest molecules have a higher chance of overlap with the cations. To test this hypothesis, calculations for $N_2$ were also performed with the electrostatic charge of the cations set to zero, so that only the steric hindrance of the cations would have an effect; the results showed that all Si/Al case studies had similar adsorption loadings compared to silicalite-1, indicating that the $Na^+$ cations are not large enough to block out the $N_2$ molecules. Therefore, it is postulated that the trends are mainly due to electrostatic effects and that the presence of already adsorbed $N_2$ molecules counter-balances the attractive electrostatic interactions between the cations and newly added $N_2$ molecules. The $N_2$ molecules for Si/Al = 47 and 23 tend to adsorb in a region between adjacent cations, especially at higher pressures and loadings, which diminishes the attraction of other $N_2$ molecules that are subsequently inserted. For Si/Al = 47 and 23, there are two and four cations in each unit cell, respectively, while for Si/Al = 95 and 31 there are one and three cations in each unit cell, respectively. For Si/Al = 13 there are seven cations in each unit cell. For the two case studies of Si/Al = 95 and 31, there is one cation that tends to be relatively more isolated, and for Si/Al = 13 there are two cations in three of the four intersections, per unit cell. At Si/Al = 13 the $N_2$ molecules are less effective in neutralizing the attractive effect of the larger number of cations, so that the cations are more attractive and adsorb an overall higher loading of $N_2$ at any given higher pressure. Compared to $CO_2$, $N_2$ has a weaker quadrupole moment, which means that it is inherently less attracted to the zeolite framework and cations. It becomes easier for already adsorbed $N_2$ molecules to block out other $N_2$ molecules. Hence, only a few $N_2$ molecules are needed to sufficiently counter-balance the attractive effect of the cations and prevent a monotonic trend as a function of the Si/Al ratio (for Si/Al >13) over the range of loading.

Overall, compared to the adsorption isotherms in silicalite-1, the presence of the $Na^+$ cations dramatically increases the adsorption of both $CO_2$ and $N_2$ molecules, especially at lower pressures. Even when a $Na^+$ cation is locally saturated by guest molecules, it still has an attractive effect compared to silicalite-1, especially for $CO_2$. This feature makes the inclusion of $Al^{(-)}$ and (counter-)cations such as $Na^+$ a useful method to enhance the adsorption of $CO_2$ and $N_2$, especially at low pressures.

### 3.3 Comparison of simulated adsorption isotherms with experimental measurements

A set of experimental adsorption isotherm measurements was performed for $CO_2$ and $N_2$ at 308 K in Na–ZSM-5 with Si/Al = 13, so as to directly compare the experimental

![](./images/813211816581660672_17.jpg)

Adsorption

results to the simulated adsorption isotherms. Prior studies have shown that the charge on $\text{Na}^+$ cations may not always be 1e, but will likely be a partial charge, substantially less than 1e (Jaramillo and Chandross 2004; Lachet et al. 1997; Maurin et al. 2005; Pillai et al. 2007, 2010; Sanchez et al. 2009). Modulating the charge on the cations is a way to roughly model partial electron transfer from the zeolite lattice and onto the cations, partially shielding them. To examine the role of partial charges on the $\text{Na}^+$ cations, a set of GCMC adsorption isotherms at $\text{Si/Al}=13$ were performed for three charges on $\text{Na}^+$: 1e, 0.7e, and 0.4e, as presented in Fig. 9 for $\text{CO}_2$ and in Fig. 10 for $\text{N}_2$.

The adsorbed amounts simulated by GCMC at a given pressure systematically decrease with reduced charge on the $\text{Na}^+$ cations, since the electrostatic interactions become weaker. Experimental measurements are also presented as green diamonds, showing good agreement over the pressure range of $10^{-3}$–1 bar for $\text{CO}_2$ and $10^{-2}$–1 bar for $\text{N}_2$. For $\text{CO}_2$ there is good agreement with the GCMC adsorption isotherm for a charge of 0.7e, while for $\text{N}_2$ the agreement is best around 0.4e. This agreement indicates that partial electron transfer most likely occurs from the framework onto the $\text{Na}^+$ cations, reducing the relative charge impact of these cations (Maurin et al. 2005; Pillai et al. 2007; Sanchez et al. 2009). The need for two different charges could be due to the set of force field interaction parameters not being simultaneously adjusted to fit the separate experimental data sets for $\text{CO}_2$ and $\text{N}_2$, so as to achieve an optimal comparison; in principle, the same amount of cation charge transfer should occur regardless of either guest molecule. Another possibility is that the guest molecules themselves may affect the charges, leading to possible charge transfer and hence a loading-dependent partial charge on the cations. However, the comparison does indicate that careful attention needs to be paid on the exact amount of electron shielding around the cation. As shown in Figs. 7 and 8, the adsorption loading is very sensitive to a larger charge of 1e around the cations, suggesting that low-pressure adsorption should occur with Group II cations, which should carry a larger charge even with partial electron shielding from the zeolite lattice.

![](./images/813211816581660672_18.jpg)

Fig. 9 Amount of adsorbed $\text{CO}_2$ molecules at $T=308$ K for three partial charges on the Na cation: 1e, 0.7e, and 0.4e. Experimental measurements are the green diamonds (Color figure online)

![](./images/813211816581660672_19.jpg)

Fig. 10 Amount of adsorbed $\text{N}_2$ molecules at $T=308$ K for three partial charges on the Na cation: 1e, 0.7e, and 0.4e. Experimental measurements are the green diamonds (Color figure online)

### 3.4 Isosteric heats of adsorption

The isosteric heat of adsorption, $Q_{st}$, was computed using Eq. 4. The results for the isosteric heats in silicalite-1, $\text{Si/Al}=95, 47, 31, 23$, and 13 at $T=308$ K are depicted for pure $\text{CO}_2$ in Fig. 11 and for pure $\text{N}_2$ in Fig. 12. The key observation observed in both Figs. 11 and 12 is that the cations increase the isosteric heat of adsorption at low loadings, which is the range where the cations have the most impact. Here the isosteric heats of $\text{CO}_2$ are very high at low loadings, $Q_{st}=50$–80 kJ/mol, for Na–ZSM-5 due to the exposed partial charges of the cations, while the results for silicalite-1 are at $Q_{st}=22$ kJ/mol, since the

![](./images/813211816581660672_20.jpg)

Fig. 11 Isosteric heats as a function of the amount of adsorbed $\text{CO}_2$ molecules at $T=308$ K for six Si/Al ratios

![](./images/813211816581660672_21.jpg)

![](./images/813211816581660672_22.jpg)

Fig. 12 Isosteric heats as a function of the amount of adsorbed $N_2$ molecules at $T=308$ K for six Si/Al ratios

only partial charges are in the zeolite lattice and no particular atom is better exposed to the guest molecules. Since the cations become locally saturated with guest molecules at higher loadings and become less effective in attracting guest molecules, the isosteric heats for all five cases of Na-ZSM-5 substantially decrease with increased loadings, approaching the silicalite-1 values at very high loading. For most of the loading range, the isosteric heats for Si/Al = 13 are consistently larger due to the much lower Si/Al, so that, despite the competition from $CO_2$ molecules, the cations still have some impact at higher loading, compared to the case studies for higher Si/Al, which is also consistent with the trend observed in the adsorption isotherms.

The isosteric heats for $N_2$ show similar trends as $CO_2$, where the results for Na-ZSM-5 are very large compared to silicalite-1 at low loading; $Q_{st}=30$–65 kJ/mol for Na-ZSM-5, while $Q_{st}=14$ kJ/mol for silicalite-1. The same crossover effects observed for the adsorption isotherms are noticed for the $N_2$ isosteric heats. The isosteric heat curve of Si/Al = 47 crosses the curve for Si/Al = 95 at $2~N_2$/Unit Cell and comes close to the silicalite-1 curve at $4~N_2$/Unit Cell. The isosteric heat for Si/Al = 95 remains larger in the intermediate loading range of 2–6 $N_2$/Unit Cell, approaching $Q_{st}=20$ kJ/mol, which is larger than the silicalite-1 value at higher loading, $Q_{st}=14$ kJ/mol. The isosteric heat for Si/Al = 23 has the largest value at low loading, $Q_{st}=65$ kJ/mol, but precipitously drops at 2–3 $N_2$/Unit Cell. Beyond $2.5~N_2$/Unit Cell the isosteric heat for Si/Al = 23 drops below the isosteric heat for Si/Al = 95, 31, and 13, closely matching the isosteric heat for Si/Al = 47 at higher loading. The isosteric heat for Si/Al = 13 again remains substantially larger than the other isosteric heats until very high loading, at which point all isosteric heats are essentially at the silicalite-1 value.

![](./images/813211816581660672_23.jpg)

Fig. 13 Isosteric heats for $CO_2$ and $N_2$ at $T=308$ K measured from experimental adsorption isotherms at two cation levels, Si/Al = 13 and 45

### 3.5 Comparison of simulated isosteric heats with experiment

The experimental isosteric heats as a function of loading for $CO_2$ and $N_2$ on samples with Si/Al = 13 and 45 are presented in Fig. 13. The experimental results show a marked difference between $CO_2$ and $N_2$ adsorption in the two zeolite samples. In particular, the isosteric heats for $CO_2$ and $N_2$ remain consistently larger at Si/Al = 13 than at Si/Al = 45 over a larger loading range. The isosteric heats were determined using GCMC for Si/Al = 13 and three charges on $Na^+$: 1e, 0.7e, and 0.4e, analogous to the adsorption isotherms, and are presented in Fig. 14 for $CO_2$ and Fig. 15 for $N_2$. For a lower charge on the cations, the isosteric heats systematically decrease, especially at lower loading, where the relative energetic importance of the cations becomes less significant. The experimental measurements for isosteric heats were compared to the GCMC results to further assess the predictive capability of the simulations. Two sets of results are presented. One data point corresponds to both $CO_2$ and $N_2$ at very low loading using pulse chromatography (designated “Low Loading”, with a single, large green diamond), in order to fully measure any impact that the cations have on the guest molecules. The second set shows the same isosteric heats for $CO_2$ and $N_2$ at Si/Al = 13 from Fig. 13 (designated “Experiment” and smaller green diamonds). Comparison with the low-loading measurement for $CO_2$ shows excellent agreement between 0.4e and 0.7e, with an experimental value of 49 kJ/mol, while the same comparison for $N_2$ shows excellent agreement at 0.4e, with an experimental value of 22 kJ/mol. A lower charge on the cations increases the potential energy available for adsorption due to the reduced interaction strength, consistent with the reduced loading observed in the adsorption isotherms. At

![](./images/813211816581660672_24.jpg)

![](./images/813211816581660672_25.jpg)

Fig. 14 Isosteric heats of $CO_2$ at $T=308$ K for three cation charges: 1e, 0.7e, and 0.4e. Experimental measurements are included as green diamonds (Color figure online)

![](./images/813211816581660672_26.jpg)

Fig. 15 Isosteric heats of $N_2$ at $T=308$ K for three cation charges: 1e, 0.7e, and 0.4e. Experimental measurements are included as green diamonds (Color figure online)

higher loadings, the GCMC predictions become only semi-quantitative, with a difference of 7–10 kJ/mol below the experimental predictions. Both GCMC and experiment indicate that the isosteric heats decrease with loading due to the local saturation of guest molecules, but GCMC shows the saturation effect at a lower loading of 3 molecules/Unit Cell. This disagreement might result from the cations in experimental samples being more randomly distributed compared to the assumed regular structure in the GCMC simulations, as fewer guest molecules may be needed to locally solvate the cations. However, since the disagreement amounts to only a few $k_bT$, GCMC simulations allow us to make excellent predictions for these experimental samples by only making a reasonable assumption of partial charge transfer.

## 4 Conclusions

The adsorption isotherms and isosteric heats from the GCMC simulations consistently predict that greater cation content in Na–ZSM-5 increases the adsorption capacity of the zeolite, especially at low pressures. At higher pressures the adsorption capacity in these zeolites becomes more comparable, as the cations in the pore space become locally saturated and the finite amount of free pore space in the lattice topology must control adsorption, since more space is taken over by the guest molecules. The isosteric heats of adsorption are quite large compared to silicalite-1 at low loadings, but substantially decrease with increased loading. From the isosurface plots it is clearly seen that the molecules are preferably adsorbed in the zigzag and straight channels of ZSM-5, rather than in the intersections, unless cations are present in those intersections, though all regions of the pore space are easily accessible due to the small molecular size. Comparisons with experiments were successful for adjusted partial charges.

Additional steps should be performed to better understand molecular adsorption in cationic zeolites. In the current study, as suggested by prior work, the partial charges on the $Na^+$ cations are empirically adjusted to improve the agreement of the GCMC simulations with experimental measurements of adsorption loading and isosteric heats (Lachet et al. 1997; Maurin et al. 2005; Pillai et al. 2007, 2010). Using a charge of 1e is evidently too large for Group I cations, though it may be a reasonable representation of Group II cations. A prior experimental study of CO adsorption in Ca-Y zeolite has shown that $Ca^{2+}$ cations interact more strongly with the guest molecules compared to $Na^+$ cations (Egerton and Stone 1970). If the charges on the cations are only 0.4–0.6e, then those zeolite samples do not offer much improvement in terms of increasing the amounts of captured $CO_2$ or $N_2$, as they only slightly differ from silicalite-1, unless the Si/Al is very low, leading to a higher total charge. Future studies should focus on quantum chemical calculations of Groups I and II cations in ZSM-5, such as $Na^+$ and $Ca^{2+}$ (Alvarado-Swaisgood et al. 1991; Bobuatong and Limtrakul 2003; Danilczuk et al. 2009; Mikosch et al. 2005; Stave and Nicholas 1995; Xu et al. 2004; Yang et al. 2005), so as to rationally determine the partial charges on these cations. This type of approach would also assist force field parameter optimizations due to their inherent complexity (Sanchez et al. 2009). DFT calculations would also provide an understanding of how the charge transfer process occurs. Additional GCMC studies should also consider how effective Group II cations in ZSM-5 at various Si/Al may be in attracting $CO_2$ and $N_2$ molecules, as these cations should carry higher partial charges and hence induce stronger electrostatic interactions. It would also be

![](./images/813211816581660672_27.jpg)

worthwhile to model the zeolite synthesis process and use spectroscopic methods to directly observe where the cat- ions are located, taking into account that the partial charge on each cation may be different depending on its location (Sklenak et al. 2009).

Acknowledgments D. Newsome and M.-O. Coppens gratefully acknowledge funding from the European Union via STREP Project 014032, FUSION (Fundamental Studies of Transport in Inorganic Nanostructures), discussions with T. Vlugt (Delft University of Technology) and F. Siperstein (University of Manchester), and computational time at Delft University of Technology and at the Computational Center for Nanotechnology Innovations (CCNI) of Rensselaer Polytechnic Institute.

References

Alvarado-Swaisgood, A., Barr, M.K., Hay, P.J., Redondo, A.: Ab initio quantum chemical calculations of aluminum substitution in zeolite ZSM-5. J. Phys. Chem. 95, 10031–10036 (1991)

Beerdsen, E., Dubbeldam, D., Smit, B., Vlugt, T.J.H., Calero, S.: Simulating the effect of nonframework cations on the adsorption of alkanes in MFI-type zeolites. J. Phys. Chem. B 107, 12088–12096 (2003)

Beerdsen, E., Smit, B., Calero, S.: The influence of non-framework sodium cations on the adsorption of alkanes in MFI- and MOR-type zeolites. J. Phys. Chem. B 106, 10659–10667 (2002)

Bernal, M.P., Coronas, J., Menendez, M., Santamaria, J.: Separation of $CO_2/N_2$ mixtures using MFI-type zeolite membranes. AIChE J. 50, 127–135 (2004)

Bobuatong, K., Limtrakul, J.: Effects of the zeolite framework on the adsorption of ethylene and benzene on alkali-exchanged zeolites: an ONIOM study. Appl. Catal. A 253, 49–64 (2003)

Bonenfant, D., Kharoune, M., Niquette, P., Mimeault, M., Hausler, R.: Advances in principal factors influencing carbon dioxide adsorption on zeolites. Sci. Technol. Adv. Mater. 9, 013007–013114 (2008)

Bowen, T.C., Li, S., Noble, R.D., Falconer, J.L.: Driving force for pervaporation through zeolite membranes. J. Membr. Sci. 225, 165–176 (2003)

Calleja, G., Pau, J., Calles, J.A.: Pure and multicomponent adsorption equilibrium of carbon dioxide, ethylene, and propane on ZSM-5 zeolites with different Si/Al ratios. J. Chem. Eng. Data 43, 994–1003 (1998)

Coppens, M.-O., Bell, A.T., Chakraborty, A.K.: Dynamic Monte Carlo and mean field study of the effect of strong adsorption sites on self-diffusion in zeolites. Chem. Eng. Sci. 54, 3455–3463 (1999)

Coppens, M.-O., Bell, A.T., Chakraborty, A.K.: Effects of topology and molecular occupancy on self-diffusion in lattice models of zeolites—Monte-Carlo simulations. Chem. Eng. Sci. 53, 2053–2061 (1998)

Coppens, M.-O., Iyengar, V.: Testing the consistency of the Maxwell- Stefan formulation when predicting self-diffusion in zeolites with strong adsorption sites. Nanotechnology 16, 442–448 (2005)

Couck, S., Remy, T., Baron, G.V., Gascon, J., Kapteijn, F., Denayer, J.: A pulse chromatographic study of the adsorption properties of the amino-MIL-53 (Al) metal–organic framework. Phys. Chem. Chem. Phys. 12, 9413–9418 (2010)

Danilczuk, M., Pogocki, D., Lund, A.: Interaction of $(CH_2OH)$ with silver cation in $Ag-A/CH_3OH$ zeolite: a DFT study. Chem. Phys. Lett. 469, 153–156 (2009)

Duerinck, T., Couck, S., Vermoortele, F., De Vos, D.E., Baron, G.V., Denayer, J.: Pulse gas chromatography study of adsorption of substituted aromatics and heterocyclic molecules on MIL-47 at zero coverage. Langmuir 28, 13883–13891 (2012)

Dunne, J.A., Mariwals, R., Rao, R., Sircar, S., Gorte, R.J., Myers, A.L.: Calorimetric heats of adsorption and adsorption isotherms. 1. $O_2$, $N_2$, $Ar$, $CO_2$, $CH_4$, $C_2H_6$, and $SF_6$ on silicalite. Langmuir 12, 5888–5895 (1996a)

Dunne, J.A., Rao, R., Sircar, S., Gorte, R.J., Myers, A.L.: Calori- metric heats of adsorption and adsorption isotherms. 2. $O_2$, $N_2$, $Ar$, $CO_2$, $CH_4$, $C_2H_6$, and $SF_6$ on NaX, HZSM-5, and NaZSM-5 zeolites. Langmuir 12, 5896–5904 (1996b)

Düren, T., Sarkisov, L., Yaghi, O.M., Snurr, R.Q.: Design of new materials for methane storage. Langmuir 20, 2683–2689 (2004)

Egerton, T.A., Stone, F.S.: Adsorption of carbon monoxide by calcium-exchanged zeolite Y. Trans. Faraday Soc. 66, 2364–2377 (1970)

Frenkel, D., Smit, B.: Understanding Molecular Simulation: From Algorithms to Applications, vol. 2. Academic Press, London, UK (2002)

Gallo, M., Nenoff, T.M., Mitchell, M.C.: Selectivities for binary mixtures of hydrogen/methane and hydrogen/carbon dioxide in silicalite and ETS-10 by Grand Canonical Monte Carlo tech- niques. Fluid Phase Equilib. 247, 135–142 (2006)

Garcia-Perez, E., Parra, J.B., Ania, C.O., Garcia-Sanchez, A., van Baten, J.M., Krishna, R., Dubbeldam, D., Calero, S.: A computational study of $CO_2$, $N_2$, and $CH_4$ adsorption in zeolites. Adsorption 13, 469–476 (2007)

Goj, A., Sholl, D., Akten, E.D., Kohen, D.: Atomistic simulations of $CO_2$ and $N_2$ adsorption in silica zeolites: the impact of pore size and shape. J. Phys. Chem. B 106, 8367–8375 (2002)

Harlick, P.J.E., Tezel, F.H.: Adsorption of carbon dioxide, methane, and nitrogen: pure and binary mixture adsorption by ZSM-5 with $SiO_2/Al_2O_3$ ratio of 30. Sep. Sci. Technol. 37, 33–60 (2002)

Harlick, P.J.E., Tezel, F.H.: Adsorption of carbon dioxide, methane and nitrogen: pure and binary mixture adsorption for ZSM-5 with $SiO_2/Al_2O_3$ ratio of 280. Sep. Purif. Technol. 33, 199–210 (2003)

Harlick, P.J.E., Tezel, F.H.: An experimental adsorbent screening study for $CO_2$ removal from $N_2$. Microporous Mesoporous Mater. 76, 71–79 (2004)

Heuchel, M., Snurr, R.Q., Buss, E.: Adsorption of $CH_4–CF_4$ mixtures in silicalite: simulation, experiment, and theory. Langmuir 13, 6795–6804 (1997)

Himeno, S., Tomita, T., Suzuki, K., Nakayama, K., Yajima, K., Yoshida, S.: Synthesis and permeation properties of a DDR-type zeolite membrane for separation of $CO_2/CH_4$ gaseous mixtures. Ind. Eng. Chem. Res. 46, 6989–6997 (2007)

Hirotani, A., Mizukami, K., Miura, R., Takaba, H., Miya, T., Fahmi, A., Stirling, A., Kubo, M., Miyamoto, A.: Grand Canonical Monte Carlo simulation of the adsorption of $CO_2$ on silicalite and Na–ZSM-5. Appl. Surf. Sci. 120, 81–84 (1997)

Jaramillo, E., Chandross, M.: Adsorption of small molecules in LTA zeolites. 1. $NH_3$, $CO_2$, and $H_2O$ in zeolite 4A. J. Phys. Chem. B 108, 20155–20159 (2004)

June, R.L., Bell, A.T., Theodorou, D.: Prediction of low occupancy sorption of alkanes in silicalite. J. Phys. Chem. 94, 1508–1516 (1990)

Kärger, J., Ruthven, D.: Diffusion in Zeolites and Other Microporous Materials. Wiley, New York (1992)

Katoh, M., Yamazaki, T., Ozawa, S.: IR spectroscopic study of adsorption of binary gases over ion-exchanged ZSM-5 zeolites. J. Colloid Interface Sci. 203, 447–455 (1998)

Katoh, M., Yoshikawa, T., Tomonari, T., Katayama, K., Tomida, T.: Adsorption characteristics of ion-exchanged ZSM-5 zeolites for $CO_2/N_2$ mixtures. J. Colloid Interface Sci. 226, 145–150 (2000)

Keil, F.J., Krishna, R., Coppens, M.-O.: Modeling of diffusion in zeolites. Rev. Chem. Eng. 16, 71–197 (2000)

Kusakabe, K., Kuroda, T., Morooka, S.: Separation of carbon dioxide from nitrogen using ion-exchanged faujasite-type zeolite

![](./images/813211816581660672_28.jpg)

membranes formed on porous support tubes. J. Membr. Sci. **148**, 13–23 (1998)

Lachet, V., Boutin, A., Tavitian, B., Fuchs, A.: Grand Canonical Monte Carlo simulations of adsorptions of mixtures of xylene molecules in faujasite zeolites. Faraday Discuss. **106**, 307–323 (1997)

Liu, S., Yang, X.: Gibbs ensemble Monte Carlo simulation of supercritical $CO_2$ adsorption on NaA and NaX zeolites. J. Chem. Phys. **124**, 244705-1–244705-10 (2006)

Liu, X., Newsome, D., Coppens, M.-O.: Dynamic Monte Carlo simulations of binary self-diffusion in ZSM-5. Microporous Mesoporous Mater. **125**, 149–159 (2009)

Makrodimitris, K., Papadopoulos, G.K., Theodorou, D.: Prediction of permeation properties of $CO_2$ and $N_2$ through silicalite via molecular simulations. J. Phys. Chem. B **105**, 777–788 (2001)

Maurin, G., Llewellyn, Ph., Poyet, Th., Kuchta, B.: Influence of extraframework cations on the adsorption properties of X-faujasite systems: microcalorimetry and molecular simulations. J. Phys. Chem. B **109**, 125–129 (2005)

Mikosch, H., Uzunova, E.L., Nikolov, G.S.: Interaction of molecular nitrogen and oxygen with extraframework cations in zeolites with double six-membered rings of oxygen-bridged silicon and aluminum atoms: a DFT study. J. Phys. Chem. B **109**, 11119–11125 (2005)

Mu, B., Schenecker, P.M., Walton, K.S.: Gas adsorption study on mesoporous metal-organic framework UMCM-1. J. Phys. Chem. C **114**, 6464–6471 (2010)

Myers, A.L.: Thermodynamics of adsorption in porous materials. AIChE J. **48**, 145–160 (2002)

Myers, A.L., Prausnitz, J.M.: Thermodynamics of mixed-gas adsorption. AIChE J. **11**, 121–126 (1965)

Noack, M., Kölsch, P., Caro, J., Schneider, M., Toussaint, P., Sieber, I.: MFI membranes of different Si/Al ratios for pervaporation and steam permeation. Microporous Mesoporous Mater. **35-36**, 253–265 (2000)

Pan, L., Sander, M.B., Huang, X.Y., Li, J., Smith, M., Bittner, E., Bockrath, B., Johnson, J.K.: Microporous metal organic materials: promising candidates as sorbents for hydrogen storage. J. Am. Chem. Soc. **126**, 1308–1309 (2004)

Papadopoulos, G.K., Jobic, H., Theodorou, D.: Transport diffusivity of $N_2$ and $CO_2$ in silicalite: coherent quasielastic neutron scattering measurements and molecular dynamics simulations. J. Phys. Chem. B **108**, 12748–12756 (2004)

Pillai, R.S., Peter, S.A., Jasra, R.V.: Correlation of sorption behavior of nitrogen, oxygen, and argon with $Ca^{2+}$ locations in zeolite A: a Grand Canonical Monte Carlo simulation study. Langmuir **23**, 8899–8908 (2007)

Pillai, R.S., Sethia, G., Jasra, R.V.: Sorption of $CO$, $CH_4$, and $N_2$ in alkali metal ion exchanged zeolite-X: Grand Canonical Monte Carlo simulation and volumetric measurements. Ind. Eng. Chem. Res. **49**, 5816–5825 (2010)

Sanchez, A.G., Ania, C.O., Parra, J.B., Dubbeldam, D., Vlugt, T.J.H., Krishna, R., Calero, S.: Transferable force field for carbon dioxide adsorption in zeolites. J. Phys. Chem. C **113**, 8814–8820 (2009)

Selassie, D., Davis, D., Dahlin, J., Feise, E., Haman, G., Sholl, D., Kohen, D.: Atomistic simulations of $CO_2$ and $N_2$ diffusion in silica zeolites: the impact of pore size and shape. J. Phys. Chem. C **112**, 16521–16531 (2008)

Siriwardane, R.V., Shen, M.S., Fisher, E.P., Poston, J.A.: Adsorption of $CO_2$ on molecular sieves and activated carbon. Energy Fuels **15**, 279–284 (2001)

Sklenak, S., Dedecek, J., Li, C., Wichterlova, B., Gabova, V., Sierka, M., Sauer, J.: Aluminum siting in the ZSM-5 framework by combination of high resolution $^{27}$Al NMR and DFT/MM calculations. Phys. Chem. Chem. Phys. **11**, 1237–1247 (2009)

Skoulidas, A.I., Sholl, D.: Molecular dynamics simulations of self-diffusivities, corrected-diffusivities, and transport-diffusivities of light gases in four silica zeolites to assess influences of pore shape and connectivity. J. Phys. Chem. A **107**, 10132–10141 (2003)

Skoulidas, A.I., Sholl, D.S.: Transport diffusivities of $CH_4$, $CF_4$, He, Ne, Ar, Xe, and $SF_6$ in silicalite from atomistic simulations. J. Phys. Chem. B **106**, 5058–5067 (2002)

Smit, B., Maesen, T.L.M.: Molecular simulations of zeolites: adsorption, diffusion, and shape selectivity. Chem. Rev. **108**, 4125–4184 (2008)

Stave, M.S., Nicholas, J.B.: Density functional studies of zeolites. 2. Structure and acidity of [T]-ZSM-5 models (T = B, Al, Ga, Fe). J. Phys. Chem. **99**, 15046–15061 (1995)

Sun, M.S., Shah, D.B., Xu, H., Talu, O.: Adsorption equilibria of $C_1$ to $C_4$ alkanes, $CO_2$, and $SF_6$ on silicalite. J. Phys. Chem. B **102**, 1466–1473 (1998)

van Koningsveld, H., van Bekkum, H., Jansen, J.C.: On the location and disorder of the tetrapropylammonium (TPA) ion in zeolite ZSM-5 with improved framework accuracy. Acta. Crystallogr. **B43**, 127–132 (1987)

Vlugt, T.J.H., van der Eerden, J.P.J.M., Dijkstra, M., Smit, B., Frenkel, D.: Introduction to Molecular Simulation and Statistical Thermodynamics, vol. 2. Technical University of Delft, Delft, The Netherlands (2008). http://homepage.tudelft.nl/v9k6y/imssr/book-15-6-2009.pdf

Walton, K.S., Abney, M.B., LeVan, D.: $CO_2$ adsorption in Y and X zeolites modified by alkali metal cation exchange. Microporous Mesoporous Mater. **91**, 78–84 (2006)

Wirawan, S.K., Creaser, D.: $CO_2$ Adsorption on silicalite-1 and cation exchanged ZSM-5 zeolites using a step change method. Microporous Mesoporous Mater. **91**, 196–205 (2006a)

Wirawan, S.K., Creaser, D.: Multicomponent $H_2/CO/CO_2$ adsorption on BaZSM-5 zeolite. Sep. Purif. Technol. **52**, 224–231 (2006b)

Xu, J., Mojet, B.L., van Ommen, J.G., Lefferts, L.: Effect of $Ca^{2+}$ position in zeolite Y on selective oxidation of propane at room temperature. J. Phys. Chem. B **108**, 15728–15734 (2004)

Yamazaki, T., Katoh, M., Ozawa, S., Ogino, Y.: Adsorption of $CO_2$ over univalent cation-exchanged ZSM-5 zeolites. Mol. Phys. **80**, 313–324 (1993)

Yang, G., Wang, Y., Zhou, D., Liu, X., Han, X., Bao, X.: Density functional theory calculations on various M/ZSM-5 zeolites: interaction with probe molecule $H_2O$ and relative hydrothermal stability predicted by binding energies. J. Mol. Catal. A **237**, 36–44 (2005)

Yun, J.H., Düren, T., Keil, F.J., Seaton, N.A.: Adsorption of methane, ethane, and their binary mixtures on MCM-41: experimental evaluation of methods for their prediction of adsorption equilibrium. Langmuir **18**, 2693–2701 (2002)

Zhou, Z., Yang, J., Zhang, Y., Chang, L., Sun, W., Wang, J.: NaA zeolite/carbon nanocomposite thin films with high permeance for $CO_2/N_2$ separation. Sep. Purif. Technol. **55**, 392–395 (2007)

Zhu, W.D., Hrabanek, P., Gora, L., Kapteijn, F., Moulijn, J.A.: Role of adsorption in the permeation of $CH_4$ and $CO_2$ through a silicalite-1 membrane. Ind. Eng. Chem. Res. **45**, 767–776 (2006)

![](./images/813211816581660672_29.jpg)