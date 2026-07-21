![](./images/813080752294985731_1.jpg)

Surface Science 395 (1998) L196-L200

![](./images/813080752294985731_2.jpg)

# Surface Science Letters

## Isotherms of ionic adsorption at metal electrodes with coverage dependent lateral interactions due to mutual depolarization

### Marc T.M. Koper *

Laboratory of Inorganic Chemistry and Catalysis, Eindhoven University of Technology, P.O.Box 513,
5600 MB Eindhoven, The Netherlands

Received 18 August 1997; accepted for publication 9 October 1997

### Abstract

Isotherms are calculated for a simple model describing ions absorbing onto a metal electrode, taking into account the effect of mutual depolarization. By mutual depolarization is meant the progressive discharge of the ions with increasing coverage, leading to weaker dipole-dipole lateral interactions. The mean-field isotherm predicts sigmoidal parts in the isotherm in the region of ionic discharge, which may even develop into hysteresis and first-order phase transitions. The qualitative predictions of the mean-field theory, in particular the first-order phase transition, are reproduced by Monte-Carlo simulations, but only if the lateral repulsive interactions are long ranged, as is expected for electrostatic interactions. © 1998 Elsevier Science B.V.

**Keywords**: Equilibrium thermodynamics and statistical mechanics; Ion-solid interactions; Ising models; Metal-electrolyte interfaces; Surface thermodynamics

---

## 1. Introduction

In the context of ionic adsorption at the metal-electrolyte interface, it is often argued that at finite surface excesses or coverages the effect of mutual depolarization causes an enhanced discharge of the adsorbed ions. Going from the low- to the high-coverage regime, the adsorbed ions are progressively discharged. The reason for this should be the minimization of the total lateral electrostatic interaction energy. Many authors have invoked this idea in their discussion of for example halide adsorption or the underpotential deposition of metal ions onto foreign metal substrates (see e.g. [1,2]).

There has not yet appeared a theoretical treatment which takes into account the effect of mutual depolarization in the calculation of the isotherm of ions adsorbing onto a metal electrode. In this short Letter, a simple lattice gas model is presented which treats, in a kind of mean-field manner, the effect of weakening lateral interactions with rising coverage. The statistical mechanics of this model is easily solved in the mean-field approximation, leading to an expression similar to the Frumkin (or Fowler) isotherm, but with a reinterpretation of the interaction parameter. Remarkably, the model predicts the possibility of first-order phase transitions and hysteresis, albeit perhaps under somewhat exotic conditions. Both the quantitative and qualitative predictions of the mean-field isotherm are tested by Monte-Carlo simulations.

---

* Fax: (+31) 40 455054; e-mail: tgtamk@chem.tue.nl

0039-6028/98/$19.00 © 1998 Elsevier Science B.V. All rights reserved.
PII S0039-6028(97)00804-2

### 2. The model potential

There are several interaction channels which contribute to the total lateral interaction energy that an adsorbed ion experiences due to the presence of other ions adsorbed onto neighboring sites. If the ion carries a (partial) charge, it is likely that the dominant interaction channel is the electrostatic Coulomb repulsion. For a metal-electrolyte interface, the *classical* interaction energy between two adsorbed ions a distance $R$ apart is [3]

$$
\epsilon_{i j}(R)=\epsilon_{\text {elec }} \frac{1}{x^{3}}(1+\kappa a x) \exp (-\kappa a x) \tag{1}
$$

where $x=R / a$, with $a$ the lattice constant and $\kappa$ the inverse Debye screening length, and

$$
\epsilon_{\text {elec }}=\frac{2 q^{2} d^{2}}{\epsilon_{\mathrm{s}} a^{3}} \tag{2}
$$

with $d$ the distance of the adsorption site from the surface and $\epsilon_{\mathrm{s}}$ the static dielectric constant of the solution. This interaction is often referred to as a dipole-dipole interaction, as it represents the interaction between two adsorbate dipoles with dipole moment $\mu=q d$, the dipole being made up of the ion and its image in the metal. Note that for $\kappa=0$ and $\epsilon_{\mathrm{s}}=1$, one recovers the well-known expression for interaction of two ionic adsorbates at the metal-vacuum interface, with the characteristic $1 / R^{3}$ dependence [4]. In addition to the electrostatic interaction, there are two main other lateral interaction channels that are usually discussed for adsorbates [5]. The first is due to the deformation of the substrate induced by the adsorbate; for two like ions this elastic interaction is repulsive and should also follow a $1 / R^{3}$ dependence, again according to a *classical* theory [6]. The second is a short-range electronic interaction, due to the finite possibility of electron hopping between the two adsorbates. The interaction may be both attractive and repulsive, and falls off much faster than the other two $(1 / R^{5})$ [7]. For further discussions the reader is referred to Desjonqueres and Spanjaard [5] and Ocko and Wandlowski [8].

The idea of this Letter is that $q$, the charge on the ion, depends on the surface coverage $\theta$ due to mutual depolarization. Kornyshev and Schmickler [9] have studied this phenomenon for an ion adsorbed at a metal-electrolyte interface in the Anderson-Newns model, by adding the lateral electrostatic interaction energy to the original Hamiltonian, and calculating the adsorbate charge self-consistently as a function of surface coverage by the ions. One finds that to a good approximation the adsorbate charge decreases linearly with increasing coverage [10], up to a critical coverage $\theta_{\mathrm{c}}$ where the adsorbate is completely discharged. We will take this result as our model for a coverage-dependent $\epsilon_{\text {elec }}(\theta)$, i.e.

$$
\begin{aligned}
\epsilon_{\text {elec }}(\theta) & =\frac{2 d^{2} q_{0}^{2}\left(1-\theta / \theta_{\mathrm{c}}\right)^{2}}{\epsilon_{\mathrm{s}} a^{3}} \\
& =\epsilon_{\text {elec }}^{\mathrm{o}}\left(1-\theta / \theta_{\mathrm{c}}\right)^{2} \text { for } \theta<\theta_{\mathrm{c}}, \\
\epsilon_{\text {elec }}(\theta) & =0 \quad \text { for } \theta>\theta_{\mathrm{c}}, \tag{3}
\end{aligned}
$$

where $q_{0}$ is the charge on the ion at zero coverage. Note that this expression has the desirable property of having a continuous first derivative. The model entails an important approximation, of course, in disregarding the influence of the local environment of the ion; rather the effect of all the other ions is smeared out in a kind of mean-field fashion. The long-range character of the electrostatic interaction may be used as an argument to partially justify this approximation.

Note that the progressive discharge of the adions with increasing coverage implies that the type of bond the adion forms to the metal substrate changes with coverage. At low coverage, where the adions still carry an appreciable charge, the bond is essentially ionic [11]. At higher coverage, when the adions no longer carry a charge, the bond is essentially covalent.

The total interaction is the sum of the above coverage-dependent electrostatic interaction, the elastic interaction, that we model by a $1 / R^{3}$ dependence, and a nearest-neighbor interaction, that may include more specific repulsive or attractive forces and the electronic interaction referred to above.

### 3. The isotherm

The isotherm is easily derived in the mean-field approximation (MFA). Writing the interaction

energy between two ions as

$$
\begin{aligned}
\epsilon_{\mathrm{tot}}=\epsilon_{\mathrm{elec}}(\theta) \frac{1}{x^{3}}(1+\kappa a x) \exp (-\kappa a)+\epsilon_{\mathrm{elas}} \frac{1}{x^{3}}+\epsilon_{\mathrm{nn}} \\
(4)
\end{aligned}
$$

where $E_{\text {elas }}$ is the elastic interaction energy between two ions occupying nearest-neighbor sites, and $E_{\mathrm{nn}}$ is the "residual" nearest-neighbor interaction, and following the usual procedure for deriving the MFA isotherm [5], one finds

$$
\Delta \mu=k_{\mathrm{B}} T \ln \left(\frac{\theta}{1-\theta}\right)-g(\theta) \theta
$$

where $\Delta \mu$ is the difference in electrochemical potential between an ion at the surface, at zero coverage, and an ion in the bulk solution. The parameter $g$ is given by

$$
\begin{aligned}
g(\theta)=\Sigma_{\mathrm{e}}(\kappa a) \epsilon_{\mathrm{elec}}(\theta) & +\frac{1}{2} \Sigma_{\mathrm{e}} \theta \frac{\mathrm{d} \epsilon_{\mathrm{elec}}(\theta)}{\mathrm{d} \theta} \\
+ & \Sigma \epsilon_{\mathrm{elas}}+Z \epsilon_{\mathrm{nn}}
\end{aligned}
$$

where $\Sigma_{\mathrm{e}}(\kappa a)$ is the so-called Zucker sum over all sites, given by

$$
\Sigma_{\mathrm{e}}(\kappa a)=\sum_{i} \frac{1}{x_{i}^{3}}\left(1+\kappa a x_{i}\right) \exp \left(-\kappa a x_{i}\right)
$$

and $\Sigma=\Sigma_{\mathrm{e}}(0) . Z$ is the number of nearest neighbors. For a square (100) lattice, that we will be considering in what follows below, $Z=4, \Sigma=$ 8.977 , and values for $\Sigma_{\mathrm{e}}$ vary from ca. 5 to 8 in the experimentally accessible base electrolyte concentration range [3]. Note that Eq. (5) is valid for any $\epsilon(\theta)$, regardless of its specific form. One may also restrict Eq. (5) to coverage dependent nearest-neighbor interactions, so that $g(\theta)=Z \epsilon_{\mathrm{nn}}(\theta)$ $+0.5 Z \mathrm{~d} \epsilon_{\mathrm{nn}} / \mathrm{d} \theta$. However, as will be seen below, the MFA is quite a poor approximation if only nearest-neighbor interactions are involved.

Eq. (5) is very similar to the Frumkin isotherm [12], but with a coverage dependent Frumkin parameter $g$. Note that $g(\theta)$ is not proportional to $\epsilon(\theta)$, as is sometimes erroneously assumed in the literature, but contains also the first derivative of the interaction energy. It is especially this latter quantity which determines some of the unusual properties of the isotherm, to be discussed below.

The electrochemical potential difference $\Delta \mu$ is related to the electrode potential through [13]

$$
\Delta \mu=\epsilon_{\mathrm{ads}}\left(E_{\mathrm{pzc}}\right)+k_{\mathrm{B}} T \ln C-e_{0} \gamma\left(E-E_{\mathrm{pzc}}\right)
$$

where $\epsilon_{\mathrm{ads}}\left(\epsilon_{\mathrm{pzc}}\right)$ is the single ion adsorption energy (at zero coverage) at the electrode potential of zero charge $E_{\mathrm{pzc}}, C$ is the bulk concentration of the ion, $\gamma$ is the electrosorption valency [14], and $k_{\mathrm{B}}, T$ and $e_{0}$ have their usual meaning. Because of the definition of the Grand-Canonical Hamiltonian, $H=\sum_{\langle i j\rangle} c_{i} c_{j} \epsilon_{i j}-\sum_{i} c_{i} \Delta \mu$, where $c_{i}$ is 0 or 1 depending on whether site $i$ is occupied or not, all lateral interactions are contained in the first summation over all pairs of sites, and hence $\Delta \mu$ is the local binding energy of the ion to the surface with respect to the free energy of the species in solution. Any effect due to discharging is incorporated in the first summation. The electrosorption valency in Eq. (8) is therefore the electrosorption valency at zero coverage, and as such coverage independent, though in principle (and in practice) it may depend on potential. Assuming this electrosorption valency does not depend on potential, the $x$-axis in Figs. 1 and $2(\Delta \mu / k T)$ is a linear function of the electrode potential $E$.

Fig. 1 shows some typical results for the MFA isotherm. The most conspicuous feature of the isotherm is the presence of the sigmoidal shape in the coverage region of discharge of the adion. If the difference between the interaction energies at zero

![](./images/813080752294985731_3.jpg)

Fig. 1. Mean-field isotherms predicted by Eqs. (3) and (5)-(7). Solid line: $\epsilon_{\text {elec }}^{\mathrm{o}}=0.1 \mathrm{eV}, \epsilon_{\mathrm{nn}}=0.02 \mathrm{eV}, \theta_{\mathrm{c}}=0.4$; Long-dashed line: $\epsilon_{\text {elec }}^{\mathrm{o}}=0.3 \mathrm{eV}, \epsilon_{\mathrm{nn}}=0.02 \mathrm{eV}, \theta_{\mathrm{c}}=0.4$; short-dashed line: $\epsilon_{\text {elec }}^{\mathrm{o}}=0.1 \mathrm{eV}, \epsilon_{\mathrm{nn}}=0.02 \mathrm{eV}, \theta_{\mathrm{c}}=0.2 . \epsilon_{\mathrm{elas}}=0, \kappa=0, T=300 \mathrm{~K}$.

![](./images/813080752294985731_4.jpg)

Fig. 2. Mean-field isotherms of Fig. 1 compared to Monte- Carlo isotherms (line with open circles). (a): $\epsilon_{\mathrm{elec}}^{\mathrm{o}}=0.3$ eV, $\epsilon_{\mathrm{nn}}=0.02$ eV, $\theta_{\mathrm{c}}=0.4$; (b): $\epsilon_{\mathrm{elec}}^{\mathrm{o}}=0.1$ eV, $\epsilon_{\mathrm{nn}}=0.02$ eV, $\theta_{\mathrm{c}}=0.4$; (c): $\epsilon_{\mathrm{elec}}^{\mathrm{o}}=0.1$ eV, $\epsilon_{\mathrm{nn}}=0.02$ eV, $\theta_{\mathrm{c}}=0.2$. Small differences at higher coverages are due to the fact that in the MC simulation the interactions with neighbors that are further than some critical distance are not included, rendering the total interaction energy somewhat smaller, and hence the MC isotherm slightly steeper than the MFA isotherms.

and critical coverage is large, the sigmoid may develop into hysteresis, i.e. a potential region in which a low-density and a high-density phase are predicted to coexist. This behavior is of course very similar to the MFA isotherm with attractive interactions, but we stress that the interaction in our model is still repulsive, though its strength is depending on the prevailing coverage.

It is of course a good idea to test this rather remarkable behavior by a model which goes beyond the MFA. The best test is the exact solution which may be easily calculated by a Grand- Canonical Monte-Carlo simulation (a quasi-chemical approximation to our model yields rather awkward implicit expressions that we did not attempt to solve). The simulation was carried out on a $30 \times 30$ lattice with periodic boundary conditions; at every potential the coverage was calculated from an averaging over 200 Monte-Carlo steps per site, after an initial equilibration of 200 Monte-Carlo steps per site. Longer simulations yield the same results.

The MC results are compared to the MFA predictions in Fig. 2. It is seen that the qualitative features of the MFA isotherms are confirmed by the MC simulations, but the quantitative agreement in the coverage region of discharge is quite poor. Most remarkable is, however, that the MC results indeed confirm the possibility of a first-order phase transition in the model (Fig. 2a). If shorter equilibration and averaging times are chosen in the MC simulation, the forward and backward scans indeed exhibit hysteresis. Of course, the parameter values for which the phase transition is obtained are not particularly realistic from the experimental point-of-view. Nevertheless, it may be noted that the MC isotherm shapes shown in Fig. 2b and c are quite remindfull of the isotherms for chloride and bromide adsorption on the $Au(111)$ electrode, as measured by Shi and Lipkowski [15,16].

Finally, it has to be remarked that the MC simulations only give rise to a first-order phase transition if the coverage-dependent lateral interaction in our model is sufficiently long ranged. If we would restrict the interaction to nearest neighbors, MFA would still predict the same isotherms, as MFA is insensitive to the range of the interactions. However, MC simulations no longer exhibit the phase transition, as for $\theta<0.5$ adsorbates will avoid occupying nearest-neighbor sites. This local ordering, which clearly gets more important with a shorter range of the interactions, is not accounted for in the MFA.

### 4. Conclusion
In this Letter, a simple model was suggested for the effect of mutual depolarization on the isotherm

of ions adsorbed onto a metal electrode. Both a mean-field approximation and exact Monte-Carlo simulations showed that the effect leads to new qualitative features in the isotherm, which under certain (extreme) conditions may lead to disconti- nuities and the possibility of a first-order phase transition in a system with solely repulsive lateral interactions. Although the effect of mutual depo- larization of ions adsorbed in the electric double layer is mentioned in nearly every experimental study of ionic adsorption, this seems to be the first theoretical study of its consequences on such an important experimental characteristic as the isotherm.

## Acknowledgements

Most of this work was carried out at the Department of Electrochemistry at the University of Ulm (Germany), where the author was sup- ported by a Marie Curie Fellowship of the European Commision in the framework of the Training and Mobility of Researchers (TMR) Programme. The author's research in Eindhoven is made possible by a fellowship from the Royal Netherlands Academy of Arts and Sciences (KNAW).

## References

[1] D.M. Kolb, in: H. Gerischer, C.W. Tobias (Eds.), Advances in Electrochemistry and Electrochemical Engi- neering, Wiley, New York, 1978, p. 125

[2] P.N. Ross, in: J. Lipkowski, P.N. Ross (Eds.), Structure of Electrified Interfaces, VCH Publishers, New York, 1993, p. 35.

[3] M.T.M. Koper, J. Electroanal. Chem., in press.

[4] W. Kohn, K.-H, Lau, Solid State Comm. 18 (1976) 553.

[5] M.C. Desjonqueres, D. Spanjaard, Concepts in Surface Physics, Springer, Berlin, 1996.

[6] K.-H. Lau, W. Kohn, Surf. Sci. 65 (1977) 607.

[7] T.L. Einstein, J.R. Schrieffer, Phys. Rev. B 7 (1973) 3629.

[8] B.M. Ocko, T. Wandlowski, in: P.C. Andricacos, S.C. Cor- coran, J.L. Delplancke, T.P. Moffat, P.C. Searson (Eds.), Materials Research Society Symposium Proceedings, vol. 451, 1997, p. 55.

[9] A.A. Kornyshev, W. Schmickler, J. Electroanal. Chem. 185 (1985) 253.

[10] M.T.M. Koper, Unpublished.

[11] P.S. Bagus, G. Pacchioni, M.R. Philpott, J. Chem. Phys. 90 (1989) 4287.

[12] A.J. Bard, L.R. Faulkner, Electrochemical Methods, Fun- damentals and Applications, Wiley, New York, 1980, p. 517.

[13] P.A. Rikvold, J. Zhang, Y.-E. Sung, A. Wieckowksi, Electrochim. Acta 41 (1996) 2175.

[14] K.J. Vetter, J.W. Schultze, Ber. Bunsenges. Phys. Chem. 76, 1972, 920, 927.

[15] Z. Shi, J. Lipkowksi, J. Electroanal. Chem. 403 (1996) 225.

[16] Z. Shi, J. Lipkowksi, S. Mirwald, B. Pettinger, J. Chem. Soc. Faraday Trans. 92 (1996) 3737.