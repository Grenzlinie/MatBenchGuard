# Competition between folding and aggregation in a model for protein solutions

Moumita Maiti¹, Madan Rao²,³ and Srikanth Sastry¹

¹Theoretical Sciences Unit, JNCASR, Jakkur, Bangalore 560065, India
²Raman Research Institute, C.V. Raman Avenue, Bangalore 560080, India
³National Centre for Biological Sciences (TIFR), Bellary Road, Bangalore 560065, India

We study the thermodynamic and kinetic consequences of the competition between single-protein folding and protein-protein aggregation using a phenomenological model, in which the proteins can be in the unfolded (U), misfolded (M) or folded (F) states. The phase diagram shows the coexistence between a phase with aggregates of misfolded proteins and a phase of isolated proteins (U or F) in solution. The spinodal at low protein concentrations shows non-monotonic behavior with temperature, with implications for the stability of solutions of folded proteins at low temperatures. We follow the dynamics upon "quenching" from the U-phase (cooling) or the F-phase (heating) to the metastable or unstable part of the phase diagram that results in aggregation. We describe how interesting consequences to the distribution of aggregate size, and growth kinetics arise from the competition between folding and aggregation.

Many proteins aggregate under certain conditions; some, such as Amyloid $\beta$ and prion, are associated with debilitating and possibly fatal human diseases[1, 2]. This has motivated a number of biophysical studies on the nature and dynamics of aggregates at different scales[3, 4]. It is widely held that proteins within an aggregate are typically misfolded; further, that protein aggregation is initiated by misfolded structures.

This immediately suggests an interplay between the dynamics of folding and aggregation, especially at large concentrations (as in the cell interior [5]), where intra-protein interactions compete with inter-protein interactions. Here, we explore the thermodynamic landscape of steady states arising from this competition, using a phenomenological model. A number of theoretical and experimental studies suggest the possible utility of such an approach [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18].

To apply to a diverse range of proteins, our model needs to be reasonably generic, and therefore incorporate only a minimal number of features common to all aggregating proteins. Consider $N$ proteins of molecular weight $L$ in a solvent of volume $V$ and temperature $T$; we represent the complex folding internal-energy landscape by a coarse-grained one with just three states – unfolded or random coil (U), a folded or native state (F) and a misfolded or intermediate state (M). These single-protein states differ in their internal energies and configurational entropy: U is taken to have zero internal energy (or defines the zero of energy) and finite entropy per site $(\ln W)$, F is the unique global energy minimum $(-\epsilon_0 < 0)$, while M is often taken to be an intermediate energy $(-\epsilon_m)$ with finite entropy per site $(\ln w)$. Note that the degeneracies $W \gg w \sim O(e^L)$.

This single-particle picture gets modified as soon as we include inter-protein interactions. In general, the specific and nonspecific contributions to the inter-protein attraction result in short-range, anisotropic interactions; however to make the analysis simple, we will at present only consider short-range attractive interactions between proteins in the M-state, represented by a square well of range $a$ and strength $J$.

We work with a three-dimensional (3D) lattice-gas model, where a fraction $\rho = N\sigma^3/V$ proteins occupy the sites of a cubic lattice with coordination number $q = 6$ (we take $\sigma = 1$). We define occupancy variables $n_i = \{0,1\}$ at each lattice site and state variables $d_i = \{-1(F),0(M),1(U)\}$ at each occupied site. The lattice Hamiltonian (in which we include the on-site free energy) is given by (setting $k_B = 1$),

$$
\begin{aligned}
H =& \sum_i\left[-T\ln W n_i\left(\frac{d_i + d_i^2}{2}\right) - (\epsilon_m + T\ln w)n_i(1 - d_i^2)\right.\\
&\left.-\epsilon_0 n_i\left(\frac{d_i^2 - d_i}{2}\right)\right] - \sum_{\langle ij \rangle} J_{ij}n_in_j(1 - d_i^2)(1 - d_j^2), \ (1)
\end{aligned}
$$

where $J_{ij} = J$.

The three states are characterised by concentrations of the unfolded $(\rho_u)$, misfolded $(\rho_m)$ and folded $(\rho_f)$ proteins, with $\rho = \rho_f + \rho_m + \rho_u$. It is convenient to follow the thermodynamic behaviour in the $(T, \rho, \rho_m)$ space, and write $\rho_u = (\rho - \rho_m)x$ and $\rho_f = (\rho - \rho_m)(1 - x)$. We start with mean-field theory: the energy density $e = -T\ln W \rho_u - (\epsilon_m + T\ln w)\rho_m - \epsilon_0\rho_f - \frac{Jq}{2}\rho_m^2$, and entropy density $s = (1-\rho)\ln(1-\rho)+\rho_u\ln\rho_u+\rho_m\ln\rho_m+\rho_f\ln\rho_f$, can be combined to obtain the grand potential density $\frac{\Omega}{V} \equiv -P = e - Ts - \mu\rho$, where $\mu$ is the chemical potential.

Upon minimisation, we get $x = \frac{W}{W+e^{\epsilon_0/T}}$, and the constitutive relations,

$$
\begin{aligned}
\rho &= \rho_m\left[1 + \left(W + e^{\frac{\epsilon_0}{T}}\right)e^{-(\epsilon_m+T\ln w+Jq\rho_m)/T}\right]\\
\mu &= T\left[\ln(\rho - \rho_m) - \ln(1 - \rho) - \ln\left(W + e^{\frac{\epsilon_0}{T}}\right)\right] \ (2)
\end{aligned}
$$

Fixing $\mu$ and $T$, these equations may be solved to obtain solutions for $\rho$ and $\rho_m$. Below $T = qJ/4 \equiv T_c$, one has two locally stable solutions in an intermediate $\mu$ range signaling a phase transition, with the phase coexistence being given by values of $(\mu, T)$ for which the two solutions will have equal $\Omega$ (i. e., the same pressure). The two

phases correspond to a low density phase where the fraction of misfolded proteins is low and a high density phase with a large fraction of misfolded proteins. We identify the latter with protein aggregation. Note that $x$ denotes the fraction of proteins that are unfolded, out of those that are not in the misfolded state. Thus, the temperature at which $x=0.5$ marks a pseudo-transition point to the folded state. The limit of stability or spinodal lines are obtained by setting the determinant of the Hessian, $|\partial^{2}\Omega(\rho,\rho_{m})|=0$, are given by $\rho_{m}=\frac{1\pm\sqrt{1-\frac{4}{\beta aJ}}}{2}$ and meet smoothly at the critical point. The critical temperature $k_{B}T_{c}=3J/2$, and the pseudo-transition temperature between folded and unfolded states at low concentrations is $k_{B}T_{f}=0.3257J$.

In our calculations, we assume parameters $W=10000, w=1000, \epsilon_{0}=3J, \epsilon_{m}=0.35J$. We choose the energy scale $J$ by using experimental values at $T=298K$ [21] for the free energy difference between monomers in the U and F states $(4.4\pm0.3kcal/mole)$, U and M states $(1.6\pm0.7kcal/mole$ (U being the stable state), and free energy of formation from monomers in the U state [22] of trimers $(14.9kcal/mole)$ and tetramers $(21.6kcal/mole)$. Assuming that trimers have 3 and tetramers 6 interactions, we obtain $J$ to be $2.7kcal/mole$. This yields $T_{f}=441K$ [23]. We use a value $2.2nm$, the estimated diameter of $A\beta(1 - 42)$ [26], as the lattice spacing, and report densities in molar (the fully occupied lattice corresponds to $156.67mM$). The time unit is fixed by equating each Monte Carlo sweep (MCS) to $\tau=a^{2}/6D=4\ ns$, where $a=2.2nm$, is the step size by which particles are moved each $MCS$ and $D$ is the diffusion coefficient in water obtained from the Stokes-Einstein relation for the assumed particle radius of $1.1nm$.

In Figure 1 we show the phase diagram in different projections. It must be noted that both in the $\rho,T$ and $\rho_{m},T$ projections, the coexistence and spinodals on the low density show a change in slope near $T_{f}$. In particular, the spinodal density in the $\rho,T$ projection retraces to higher values at temperatures below $T_{f}$.

The scenario described by our approximate mean field is confirmed by Monte Carlo simulations. We determine the coexistence line (Fig.2) by the histogram reweighting grand canonical Monte Carlo technique and evaluation of the global free energy [19, 20]. We locate the spinodal lines by identifying chemical potential values at which the configuration probability distribution changes from a bimodal to a single peak distribution. The non-monotonicity and the bend in the spinodal are reproduced in the Monte Carlo simulation. We note that the phase behavior we obtain straight-forwardly explains the presence of a critical concentration to aggregation, that has been seen in experiments [15].

We now study the kinetics of transformation following a "quench" from an initial equilibrium phase, using a dynamic Monte Carlo simulation, where in addition to the state changing Metropolis moves, we also move particles into neighbouring vacant sites with probability $p$, related to its diffusion coefficient. We have chosen 8 qualitatively different protocols, marked (1)-(8) in Fig. 2, to study the kinetics from a homogeneous U state ('folding' pathway) or a homogeneous F state ('unfolding' pathway), into the metastable $((1),(2);(3),(4))$ and unstable $((5),(6);(7),(8))$ regions, for a temperature above $T_{f}$ and one below $T_{f}$. The data reported are from simulations on a $64\times64\times64$ lattice, with typically 150 independent runs. Figure 3 shows the aggregate size distribution and mean aggregate size of misfolded proteins for protocol 3, where we quench the system to a metastable state from the unfolded state.

The interplay of diffusion, detachment-attachment, and state change from $U/F\rightarrow M$, results in multiple growth regimes and crossovers, which depend on the quench protocol. We will highlight those features that are generic to the aggregation dynamics in the presence of competing energy minima. The first surprise is that the aggregate size distribution at early times is $P(n,t)\sim n^{-3.5\pm0.05}$ for small aggregates (Fig.3), a power law (with an exponential cutoff) rather than an exponential distribution expected from detailed balance dynamics. The dynamics in the subspace of misfolded configurations, mimics the dynamics of an open system with sources and sinks, arising from state changes to and from U/F, for which power law distributions are expected [27, 28]. We leave the analytical derivation of this power law to a later study. Together with the robust power-law distribution, there is a finite n peak, indicating a large aggregate which grows with time. At later times, when the fraction of U/F proteins has reached steady state (no

![](./images/867764690908873100_1.jpg)

FIG. 1: Mean-field phase diagram, panels (a) - (d) show projections corresponding to $\rho-T$, $\mu-T$, $\rho_{m}-T$ and $P-T$ respectively. The pseudo-transition temperature between native and random coil states at low concentration is indicated in panel (a) by a cross.

![](./images/867764690908873100_2.jpg)

FIG. 2: Simulation phase diagram in (a) the $\rho-T$ plane, and (b) the $\rho_m-T$ plane. The coexistence and spinodal lines have been obtained using the histogram reweighting tech- nique. Also indicated by arrows in (a) are protocols (1) -(8) by which the protein solution is either quenched down from the high temperature unfolded (U) phase (protocols 1,3, 5, 7), or heated up from the low temperature folded (F)phase (protocols 2,4,6,8), into metastable (protocols 1 - 4) $(\rho=15.67 mM)$ or unstable (protocols $5-8)(\rho=78.35 mM)$  parts of the phase diagram. The final $(\rho, T)$ values for these protocols are indicated by open circles.

'source' ), $P(n, t)$ goes over to the expected exponential distribution (Fig. 3 (b)), together with a growing peak at large n.

The dynamics of the mean aggregate size $\langle n\rangle=$ $\sum_{n} n P(n, t) / \sum_{n} P(n, t)$ shows multiple growth regimes - at very early times the growth is dominated by theconversion of isolated (or clusters of) U proteins into M; growth via diffusion of M kicks in later. This is generi- cally followed by a growth plateau (which becomes less clearly defined at high $\rho$ , high $T$ ), where the largest ag gregate, which can be as large as 30 monomers, does not grow appreciably. These intermediate structures are probably stabilised by a cloud of U/F proteins shielding it. Such stable intermediates have been reported in re- cent studies of amyloid aggregation [15]. We note that a clear plateau is present when we study the system un- der metastable conditions, whereas no clear pleateau is visible when the kinetics is observed in the unstable part of the phase diagram. This feature, and the observation of a spinodal line that is reentrant, and occurs as higher densities for lower temperatures (a special feature of the phase diagram we evaluate), can help explain the inter- esting kinetics seen in [29].

![](./images/867764690908873100_3.jpg)

FIG. 3: (a) Early time aggregate size distribution P(n,t) dis- plays power law behavior for small aggregates, and an emerg- ing finite size peak indicating the onset of aggregation. (b) At late times, the distribution is exponential, and a large peak at large sizes is seen corresponding to the formation of large aggregates. Mean cluster size of misfolded proteins, vs. time(c) for protocol 1 (PI), (d) for protocol 3 (P3), showing the intermediate time plateau, and the power law growth phase.

The late time growth depends on which dynamical mechanism - diffusion, detachment-attachment or state conversion - is dominant. Diffusion dominated growth[30], likely at high $T$ , low $\rho$ , gives rise to a $\langle n\rangle \sim t$ or $R \sim t^{1 / 3}$ , since aggregates are compact (Fig.3c). On the other hand, the state conversion dynamics, which domi- nates at low $T$ , leads to $\langle n\rangle \sim t^{3}$ or $R \sim t$ (Fig.3d). Fi nally, detachment dominated dynamics (at high $T$ , high $\rho$ ) should result in $\langle n\rangle \sim t^{3 / 2}$ or $R \sim t^{1 / 2}[31]$ (though this is hard to ascertain unambiguously from available numerical data).

Figure 4 shows the onset times for the growth phase, r, defined as the time of departure from the intermedi- ate structure plateau for $\rho=15.67 mM$ . We quench from the high temperature, unfolded phase ("cooling"; with initial condition where all proteins are unfolded), and the low temperature, folded phase ("heating"; with ini- tial condition where all proteins are folded) respectively, to temperatures at which the system is in the metastable phase. While for high temperatures (above $T=744.7 K$ ), we see that the crossover times for heating and cooling runs are roughly the same, for low temperatures (below T = 270.8K), the onset of the growth phase is substan-

![](./images/867764690908873100_4.jpg)

FIG. 4: Onset times for the growth phase: Inset shows $\tau_h$ vs T and $\tau_c$ vs T. $\tau$ is the MC step defined as the time of departure from the intermediate structure plateau in Fig.3 (c) to the growth regime. The subscript of $\tau$ refers to the protocol (heating vs cooling). (b) $\tau_h/\tau_c$ vs $T$, inset shows $\tau_h$ vs $T$ and $\tau_c$ vs $T$. The density is $\rho=15.67$ mM. Independent runs vary from 25 to 75 in each case.

tially delayed when we heat up from the folded phase, indicating the relative difficulty of nucleating the misfolded aggregate from a solution of folded proteins. The onset time of aggregation thus depends on the initial state of proteins in solution, a fact which must therefore be taken into account in interpreting experimental data.

An instructive way of describing the results of the dynamics of transformation is by Time-Temperature-Transformation (TTT) curves, where each curve is a plot of the time required to obtain a fraction $x$ when quenched to a temperature $T$, and may be viewed as a kinetic phase diagram. Fig. 5 shows the TTT curves for quenches from the high temperature U-phase, and from initial conditions in the low temperature F-phase. Between 25 and 75 independent runs are performed at each temperature for a system of size $64\times64\times64$. We note that in both the heating and cooling cases, there is a greater spread in times at the high temperature end for transformation fractions between $20\%$ to $60\%$, as compared to the lower temperature range, where rapid transformation occurs following a longer lag time. Further, we note that when the system is heated from the low temperature F-phase, the transformation times at low temperatures are no- ticeably longer. A more detailed study of the various growth phases and the manner in which the competition between the global thermodynamic stability of the aggregate phase and the local stability of the folded state determine the kinetics and morphology of aggregation is under way.

In this paper we have studied the thermodynamics of the competition between folding and aggregation of proteins using a phenomenological lattice model. There are many interesting extensions that we plan to explore in future. For instance, including attractive interactions between UU and UM, would dramatically alter the nature of aggregates, such as producing small U aggregates, and aggregates containing mixtures of M and U. These mixed aggregates would be more flexible because the U insertions would provide flexible hinges. Another extension is to include changes in configurational entropy and internal energy of the M-state upon aggregation, a feature related to domain swapping. Including anisotropy in the inter-protein interactions would naturally give rise to linear and 'sheet'-like aggregates. Most importantly, by introducing explicit intra-protein interactions to describe the $\text{U}\rightarrow\text{F}$ transition, we will be able to study the effect of aggregation on the dynamics of folding. Finally, the effect of charge interactions is expected to induce effective anisotropy in the aggregate morphology[32, 33, 34], and indeed, the role of charges in the formation of ordered aggregates has been previously noted[32, 34]. The approach presented here allows for these effects to be studied systematically.

![](./images/867764690908873100_5.jpg)

FIG. 5: (a) TTT (time-temperature transformation) plot for cooling protocol. (density $=15.67$ mM) $\%=100\times$(no of M-proteins/ total proteins). All cooling protocols (initialised with U-phase, quenched from high T). (b) TTT (time-temperature transformation) plot for all heating protocols (density $=15.67$ mM) ( initialsed with F phase, "quenched" from low T).

MR acknowledges HFSP and IFCPAR 3504-2 grants, SS and MM acknowledge computational facilities at JN- CASR. We thank T. Head-Gordon, S. Maiti, D. Thirumalai, T. M. Truskett, J. B. Udgaonkar and B. Urbanc for very useful discussions and comments on the manuscript.

[1] C. A. Ross and M. A. Poirier, Nature Medicine 10, S10 (2004).
[2] J. D. Harper and P. T. Lansbury Jr., Ann. Rev. Biochem. 66, 385 (1997).
[3] C. M. Dobson, Nature 426, 884 (2003).
[4] F. E. Cohen and J. W. Kelly, Nature 426, 905 (2003).
[5] B. van den Berg, R. Wain, C. M. Dobson and R. J. Ellis, EMBO Journal 19, 3870 (2000).
[6] R. I. Dima and D. Thirumalai, Protein Sci. 11, 1036 (2002).

[7] M. S. Li, et al, J. Chem. Phys. 129, 175101 (2008).

[8] N. Combe and D. Frenkel, J. Chem. Phys. 118, 9015 (2003).

[9] A. Slepoy, et al, Phys. Rev. Lett. 87, 058101 (2001).

[10] J. K. Cheung and T. M. Truskett, Biophys. J. 89, 2371 (2005).

[11] J. K. Cheung, V. K. Shen, J. R. Errington and T. M. Truskett, Biophys. J. 92, 4316 (2007).

[12] S. Peng, et al, Phys. Rev. E 69, 041908 (2004).

[13] B. Urbanc, et, Proc. Natl. Acad. Sci. (USA) 101, 17345 (2004).

[14] H. D. Nguyen and C. K. Hall, Biophys. J. 87, 4122 (2004).

[15] P. Sengupta et al., Biochemistry 42, 10506 (2003).

[16] S. Kumar et. al, J. Mol. Biol 367, 1186 (2007).

[17] S. Jain and J. B. Udgaonkar, J. Mol. Biol. 382, 1228 (2008).

[18] J. Zhang and M. Muthukumar, J. Chem. Phys. 130, 135102 (2009).

[19] A. Z. Panagiotopoulos, J. Phys.: Condens. Matter 12, R25 (2000).

[20] A. M. Ferrenberg and R. H. Swendsen, Phys. Rev. Lett. 63, 1195 (1989).

[21] Y. Fezoui and D. B. Teplow, J. Biol. Chem. 277, 36948 (2002).

[22] Y. Chen and C. G. Glabe, J. Biol. Chem. 281, 24414 (2006).

[23] This value is higher than expected, as experimentally the peptide is in the U state at $298K$. Based on the degeneracy estimates for 27 [24] $(\sim O(10^{5}))$ , and 36-mers [25] $(\sim O(10^{7}))$ , we can rationalize this difference as arising from our choice of $W=1000$ being an underestimate for A$\beta$(1-42).

[24] E. Shakhnovich and A. Gutin, J. Chem. Phys. 93, 5967 (1990).

[25] H. Cejtin, et al J. Chem. Phys. 116, 352 (2002).

[26] G. Reddy, J. E. Straub and D. Thirumalai, J. Phys. Chem. B 113, 1162 (2009); S. Maiti (Private communication).

[27] F. Leyvraz, Phys. Rep. 383, 95 (2003).

[28] S. N. Majumdar, S. Krishnamurthy and M. Barma, Phys. Rev. Lett. 81, 3691 (1998).

[29] K. Skerget et. al, Proteins 74, 425 (2009).

[30] A. J. Bray, Adv. Phys. 43, 357 (1994).

[31] F. D. A. Aarão Reis and R. B. Stinchcombe, Phys. Rev. E 70, 036109 (2004).

[32] L. de la Paz, et al, Proc. Natl. Acad. Sci. (USA) 99, 16052 (2002).

[33] A. Yethiraj and A. V. Blaaderen, Nature 421, 514 (2003).

[34] N. Byrne and C. A. Angell, J. Mol. Biol. 378, 707 (2008).