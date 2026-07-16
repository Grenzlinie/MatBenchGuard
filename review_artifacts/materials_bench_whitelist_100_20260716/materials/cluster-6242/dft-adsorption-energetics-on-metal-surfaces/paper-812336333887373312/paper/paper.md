# The Steady State of Heterogeneous Catalysis, Studied by First-Principles Statistical Mechanics

Karsten Reuter, $^{1,2}$ Daan Frenkel, $^{2}$ and Matthias Scheffler $^{1}$

$^{1}$ Fritz-Haber-Institut der Max-Planck-Gesellschaft, Faradayweg 4-6, D-14195 Berlin, Germany
$^{2}$ FOM Institute AMOLF, Kruislaan 407, SJ1098 Amsterdam, The Netherlands
(Received 20 January 2004; published 10 September 2004)

The turnover frequency of the catalytic oxidation of CO at $RuO_2(110)$ was calculated as a function of temperature and partial pressures using *ab initio* statistical mechanics. The underlying energetics of the gas-phase molecules, dissociation, adsorption, surface diffusion, surface chemical reactions, and desorption were obtained by all-electron density-functional theory. The resulting $CO_2$ formation rate [in the full $(T, p_{CO}, p_{O_2})$ space], the movies displaying the atomic motion and reactions over times scales from picoseconds to seconds, and the statistical analyses provide insight into the concerted actions ruling heterogeneous catalysis and open thermodynamic systems in general.

DOI: 10.1103/PhysRevLett.93.116105
PACS numbers: 82.65.+r, 68.43.Bc, 68.43.De, 82.20.Db

Under realistic conditions, material surfaces are in contact with a rich environment [1]. Often, the resulting surface composition and surface-actuated material function are determined by equilibrium thermodynamics. A first-principles description is then possible with the "*ab initio* atomistic thermodynamics" approach that has been successfully applied to various systems (see, e.g., Refs. [1–5], and references therein). However, under many conditions, equilibrium thermodynamics does not provide the appropriate description, and heterogeneous catalysis is a particularly interesting and important example. Here one is dealing with an open system, i.e., a supply of gases or liquids comes into contact with a solid surface where a chemical reaction produces a new substance that is then transported away. The entire concert of the various underlying, interlinked atomistic processes is in this case determined by kinetics. Still, the temperature and partial pressures of the reactants must be set such that the system runs under *steady-state* conditions. Only then is the catalyst not getting destroyed, but is stably enhancing the rate of the desired chemical reaction. An *ab initio* description of the full steady-state situation of heterogeneous catalysis has not been achieved so far, and a microscopic understanding of the competing and concerting actions of the various atomistic processes is lacking.

The present Letter describes the "*ab initio* statistical mechanics" methodology appropriate for an open thermodynamic system with a continuous conversion of chemicals $A$ and $B$ into $C$, using the oxidation of CO at a $RuO_2$ model catalyst as example. We employ density-functional theory (DFT) to obtain the energetics of all relevant processes, as there are the following: motion of the gas-phase molecules, dissociation, adsorption, surface diffusion, surface chemical reactions, and desorption. These calculations use the all-electron, full-potential linear augmented plane wave (FP-LAPW) approach [6,7]. The only notable approximations are the generalized gradient approximation (GGA) for the exchange-correlation functional [8], and the assumption that transition-state theory (TST) [9] is applicable. In fact, both approximations are well justified for the present study, and we will particularly address the GGA below when analyzing the results. A combination of DFT with TST, and subsequently solving the statistical mechanics problem by the kinetic Monte Carlo (kMC) approach [9,10], has been employed before (see, e.g., Refs. [9,11–13]). Distinct from (by now standard) "empirical kMC" calculations that use just a few *effective parameters* which have only limited (if any) microscopic meaning, these "*ab initio* kMC" calculations include an extended set of elementary processes with full and direct physical meaning. And describing an open system with a continuous conversion of chemicals $A$ and $B$ into $C$ implies additional complexity. For the example, discussed below (the catalytic oxidation of CO), we will solve the statistical mechanics problem, gaining microscopic insight into the full dynamics from picoseconds to microseconds and even to seconds. The reported results demonstrate the new quality of and the novel insights gained by such description. We will also compare the results to those obtained by "constrained thermodynamics" [3]. Although (as expected) noticeable differences occur for certain environmental conditions, we will confirm that the much simpler "constrained thermodynamics" approach can provide important guidance as to where in $(T, p)$ space high reaction rates are likely to be expected, and when results obtained for certain $(T, p)$ conditions can be extrapolated to others.

The now obtained turnover frequencies (TOFs) of the catalytic oxidation of CO are in unexpected and unprecedented agreement with the experimental results of Peden and Goodman [14] and *Wang et al.* [15]. This is found to be a consequence of the fact that the high reaction conditions are not just ruled by a singular chemical reaction pathway. Instead, for the steady-state high TOF conditions it is necessary that various processes play together in a most efficient manner. For the present example, one crucial point is to realize an optimum disordered and dynamic "phase" at the surface. Modest errors due to the approximate treatment of the exchange-

correlation functional (e.g., the GGA) are then not cru- cial, as long as the trends of the energetics of the various interplaying processes are described correctly. In this sense, the frequently requested chemical accuracy for the description of individual processes appears to be a misleading concept. At least for the present system, a careful combination of DFT and statistical mechanics is more important.

The methodology will be used to study CO oxidation over $RuO_{2}(110)$ [the surface is sketched in Fig. 1(a)], as this system has recently received considerable attention as a highly active model catalyst (see Ref. [15] and ref- erences therein). In fact, this was previously called the Ru catalyst, but recent experimental and theoretical work has shown that at realistic $O_{2}$ pressure, the $Ru(0001)$ surface is transformed into an epitaxial $RuO_{2}(110)$ film (see Ref. [16] and references therein). It is by now also estab- lished that this $RuO_{2}(110)$ surface actuates the catalytic reaction, and, although domain boundaries and steps are present, their influence is not significant [17]. The surface unit cell is rectangular and contains two adsorption sites [3]: bridge (br) and coordinatively unsaturated (cus) sites [cf. Fig. 1(a)]. Either of them can be empty or occupied by O or CO, and adsorbate diffusion can go br to br, br to cus, cus to cus, or cus to br. Since this comprises the possibility of missing $O^{br}$ atoms, we note that our treat ment implicitly includes the effect of O surface vacancies. A total of 26 different elementary processes are possible on this lattice, and all were carefully analyzed by DFT to obtain their pathways and energy barriers [3,18]. Table I summarizes the adsorption energies and the diffusion and reaction energy barriers used for the kMC study, as obtained from DFT calculations with a $(1 \times 2)$ surface unit cell. In a systematic study of CO and O (co)adsorp- tion at various coverages, we found adsorbate-adsorbate interaction to be always smaller than 150 meV. Thus, lateral interactions in this system are small (compared to the other energies), and will therefore be neglected.

![](./images/812336333887373312_1.jpg)

FIG. 1 (color online). (a) Perspective view of the $RuO_{2}(110)$ surface, illustrating the two prominent adsorption sites in the rectangular surface unit cell. These sites are labeled as the br (bridge) and the cus (coordinatively unsaturated) site, and both are occupied in the example with oxygen atoms. This is the "high $p_{O_{2}}$ termination" [2,3]. (b) Time evolution of the site occupation numbers from the thermodynamic surface termi- nation shown in (a) to the steady state of catalysis [cf. snapshot (c)]. The temperature is $T=600 ~K$ and the $CO$ and $O_{2}$ partial pressures are that of the optimum reaction conditions: $p_{CO}=$ 20 atm; $p_{O_{2}}=1$ atm. (c) Snapshot (top view of the $RuO_{2}(110)$ surface) from movies [19] displaying the dynamics of the surface under realistic catalytic conditions. Though the full atomic structure is considered in the calculations, for clarity we have marked here the substrate bridge sites only by gray stripes and the cus sites by white stripes. Oxygen adatoms are drawn as (light) red circles and adsorbed CO molecules as (dark) blue circles. Movies are also available for various pressure conditions for runtimes of 500 ns, as well as 1 s [19].

CO adsorption into vacant cus or bridge sites is non- dissociative, while oxygen adsorption is dissociative and requires two vacant neighboring sites, i.e., a br-br, cus- cus, or br-cus pair. The adsorption rate per free site is given by the local sticking coefficient, $\tilde{S}$ , and the kinetic impingement: $\Gamma_{ad}=\tilde{S} p / \sqrt{2 \pi m k_{B} T}$ . Here $m$ is the mass of the gas-phase molecule, and $k_{B}$ is the Boltzmann constant. The rate of the time reversed process (desorp- tion) then follows from the relation: $\Gamma_{des} / \Gamma_{ad}=$ $\exp [(F_{b}-\mu) /(k_{B} T)]$ , where $F_{b}$ is the free energy of the adsorbed species (approximated by $E_{b}$ ), and $\mu(T, p)$ is the chemical potential of the gas-phase molecule [2]. The $\tilde{S}(T)$ are thus obtained from the calculated total energy surfaces of desorption together with detailed balance. The only uncertainty here arises from the vibrational proper- ties of the transition state which translates into uncer- tainties in the desorption rate by a factor of 10 (at most100). For the diffusion processes we use a prefactor of1012 Hz, which has an uncertainty of a factor of 10. We carefully checked that these uncertainties do not affect our below reported results and conclusions. Details of the employed new methodology and of the various test cal- culations will be published elsewhere [18]. A detailed balance of the scenario was carefully checked by con- firming that the earlier results obtained by "atomistic thermodynamics" [3] are exactly reproduced by the present statistical mechanics treatment, if surface reac- tions are not allowed to occur.

Kinetic Monte Carlo runs were performed for about1000 different $(T, p_{CO}, p_{O_{2}})$ conditions covering the tem perature range $300 ~K<T<800 ~K$ and partial pressures

<table>
<caption>TABLE I. DFT binding energies, $E_{b}$ , for CO and O (with respect to $(1 / 2) O_{2}$ ) at br and cus sites [cf. Fig. 1(a)], diffusion energy barriers, $\Delta E_{diff }^{b}$ , to neighboring br and cus sites, and reaction energy barriers, $\Delta E_{reac }^{b}$ , of neighboring species at br and cus sites. All values are in eV.</caption>
<thead>
  <tr>
    <th></th>
    <th rowspan="2">$E_{b}$</th>
    <th colspan="2">$\Delta E_{diff }^{b}$</th>
    <th colspan="2">$\Delta E_{reac }^{b}$</th>
  </tr>
  <tr>
    <th></th>
    <th>to br</th>
    <th>to cus</th>
    <th>with $CO^{br}$</th>
    <th>with $CO^{cus}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$CO^{br}$</td>
    <td>-1.6</td>
    <td>0.6</td>
    <td>1.6</td>
    <td>$\cdots$</td>
    <td>$\cdots$</td>
  </tr>
  <tr>
    <td>$CO^{cus}$</td>
    <td>-1.3</td>
    <td>1.3</td>
    <td>1.7</td>
    <td>$\cdots$</td>
    <td>$\cdots$</td>
  </tr>
  <tr>
    <td>$O^{br}$</td>
    <td>-2.3</td>
    <td>0.7</td>
    <td>2.3</td>
    <td>1.5</td>
    <td>1.2</td>
  </tr>
  <tr>
    <td>$O^{cus}$</td>
    <td>-1.0</td>
    <td>1.0</td>
    <td>1.6</td>
    <td>0.8</td>
    <td>0.9</td>
  </tr>
</tbody>
</table>

from $10^{-10}$ to $10^3$ atmospheres. Several calculations were done on a system with $(30 \times 30)$ surface sites (450 bridge plus 450 cus sites), but the vast amount of calculations was done for a 400 sites system. The results for both system sizes were identical. The kMC simulations were run until steady state is reached [cf. Fig. 1(b)]. Then the movies [19] were recorded [cf. Fig. 1(c)] and the statistical analyses of the frequencies of the various elementary processes were performed. The latter also gives the total TOFs of the $\text{CO}_2$ formation.

The results show that catalytic reaction conditions are only established when both $\text{CO}$ and $\text{O}_2$ partial pressures exceed certain values below which the surface is in a thermodynamic equilibrium phase of $\text{RuO}_2(110)$, characteristic for low oxygen pressures and routinely observed under ultrahigh vacuum (UHV) conditions: all bridge sites are occupied by oxygen atoms and all cus sites are empty. For higher pressures, three surface conditions are worth mentioning, which are, e.g., obtained for $T = 600$ K, $p_{\text{O}_2} = 1$ atm, and $p_{\text{CO}} = 10^{-2}, 20$, and $10^3$ atm.

(i) At the low $p_{\text{CO}}$, all bridge and all cus sites are covered with oxygen atoms [cf. Fig. 1(a)]. This is essentially the thermodynamic high $p_{\text{O}_2}$ phase [2,3]. There is a noticeable desorption/adsorption dynamics, i.e., about every $40\ \mu\text{s}$, two of the 900 O adatoms of the $(30 \times 30)$ simulation cell desorb (mainly from cus sites) as $\text{O}_2$. The resulting vacancies are then rapidly filled again (within 1 ns), most of the time with oxygen. Only rarely $\text{CO}$ adsorbs, and even if it does, it rather desorbs again than initiates a reaction. The overall $\text{CO}_2$ formation rate under these conditions is with $0.9 \times 10^{12}\ \text{cm}^{-2}\ \text{s}^{-1}$ very low.

(ii) For $p_{\text{CO}} = 20$ atm, the situation corresponds to what was previously suggested to be that of high chemical activity [3], and this suggestion is now confirmed. The time to reach the steady state is remarkably long, in particular when compared to the picosecond time scale of the underlying atomistic processes [cf. Fig. 1(b)]. Finally, an interesting mix of $\text{CO}$ molecules and O atoms at both bridge and cus sites is established [a typical snapshot is shown in Fig. 1(c)], with average occupation numbers $N_{\text{CO}}^{\text{br}} = 0.11$, $N_{\text{CO}}^{\text{cus}} = 0.70$, $N_{\text{O}}^{\text{br}} = 0.89$, and $N_{\text{O}}^{\text{cus}} = 0.29$. The dynamics of this surface is extremely fast. It is mainly due to $\text{CO}$ desorption and adsorption. The rate of $\text{CO}_2$ formation is a factor of 0.0004 lower, but truly significant, namely $4.6 \times 10^{18}\ \text{cm}^{-2}\ \text{s}^{-1}$. It is dominated by the reaction $\text{CO}^{\text{cus}} + \text{O}^{\text{cus}} \longrightarrow \text{CO}_2$. The $\text{CO}^{\text{br}} + \text{O}^{\text{cus}} \longrightarrow \text{CO}_2$ and $\text{CO}^{\text{cus}} + \text{O}^{\text{br}} \longrightarrow \text{CO}_2$ reactions also contribute, though their rates are by a factor of 0.30 and 0.01 lower than the first one. The $\text{CO}^{\text{br}} + \text{O}^{\text{br}} \longrightarrow \text{CO}_2$ reaction is insignificant. This result is different from what one would expect from the reaction energy barriers (cf. Table I), which would give the lead to $\text{CO}^{\text{br}} + \text{O}^{\text{cus}}$, demonstrating the importance of the proper mix of surface-site occupations.

(iii) When the $\text{CO}$ pressure is increased further, to $p_{\text{CO}} = 10^3$ atm, the surface becomes fully covered with CO. This result is at variance with the "constrained thermodynamics" study in which the $\text{CO}_2$ formation was forbidden. Now we find that catalysis is practically poisoned by adsorbed CO. The encountered situation is in fact close to that where the $\text{RuO}_2$ catalyst will be reduced by $\text{CO}$ to the pure Ru metal.

Figure 2 summarizes the results by showing the various steady-state surface structures as well as a map of the TOFs in $(p_{\text{CO}}, p_{\text{O}_2})$ space. The highest activity is found to be in very good agreement with the early experimental results by Peden and Goodman [14], and occurs whenever the environmental conditions lead to the dynamic coexistence phase described above under (ii). Recently, Wang *et al.* [15] have also measured the TOFs for the $\text{RuO}_2(110)$ surface at $T = 350$ K for various pressures, and in Fig. 3 we compare their results with ours. The agreement is again far better than one would have expected: the theoretical and experimental TOF values at the optimum pressures are practically identical, and also the optimum pressure conditions (when the "dynamic phase" is realized) agree very well. Because the errors due to the GGA are in the range of 0.1-0.3 eV, this good agreement between theory and experiment, seen in Fig. 3, may seem fortuitous. However, it is worth noting that the position of the optimum catalytic efficiency in $(T, p)$ space and to some extent also the value of the TOF are not determined by the energetics of a singular process alone, but by the action of many players. Apparently, the DFT-GGA calculations describe the differences between the various surface processes better than the individual absolute values. In this respect, it is important to realize that a combination of different calculations (employing different approximations) or of theory and experiment could have spoiled the description. The consistent treatment of all participating processes implies that the *optimum mix* of O and $\text{CO}$ at the surface is described well: the abundance of

![](./images/812336333887373312_2.jpg)

FIG. 2 (color online). (a) Steady-state surface structures obtained by *ab initio* kMC calculations at $T = 600$ K and various $\text{CO}$ and $\text{O}_2$ partial pressures. In all nonwhite areas, the average site occupation is dominated ($>90\%$) by one species, i.e., either O, CO, or empty sites ($-$). (b) Map of the corresponding turnover frequencies (TOFs) in $\text{cm}^{-2}\ \text{s}^{-1}$: white areas have a $\text{TOF} < 10^{11}\ \text{cm}^{-2}\ \text{s}^{-1}$, and each increasing gray level represents 1 order of magnitude higher activity. Thus, the darkest region corresponds to a TOF higher than $10^{17}\ \text{cm}^{-2}\ \text{s}^{-1}$.

![](./images/812336333887373312_3.jpg)

FIG. 3 (color online). Rate of $CO_2$ formation at $T=350$ K. The experimental steady-state results of Wang et al. [15] are presented as dotted lines, and the theoretical results are shown as solid lines. Rates given as function of $p_{O_2}$ at $p_{CO}=10^{-10}$ atm (left), and as function of $p_{CO}$ at $p_{O_2}=10^{-10}$ atm (right).

$CO^{cus}$-$O^{cus}$ nearest neighbor pairs (as well as $CO^{br}$-$O^{cus}$ nearest neighbor pairs) is apparently playing a role of similar importance as the energy barriers. Particularly at the optimum TOF conditions, there is also an effective compensation, e.g., when too high adsorption energies result in enhanced adsorption, but also in reduced reaction barriers, etc. Away from the optimum TOF conditions, such compensation effects become less effective, and modest differences between the theoretical and experimental results arise. Here DFT-GGA errors are more influential, and for the experimental data we expect that contributions from surface imperfections may play a bigger role.

In summary, we computed the surface kinetics of CO oxidation catalysis at $RuO_2(110)$. The TOFs are presented in $(T, p_{CO}, p_{O_2})$ space, clearly identifying a narrow region of highest catalytic activity. In this region, kinetics builds an adsorbate composition that is not found anywhere in the thermodynamic surface phase diagram. The statistical analysis of the surface dynamics and of the various processes reveals several surprising results. For example, the chemical reaction with the most favorable energy barrier happens a factor of 0.30 less frequently than the energetically second favorable reaction.

The results also clarify how and when a bridging of the pressure gap between UHV studies and realistic pressure conditions is possible. The considered system has in fact two important components to this issue: at first, an $O_2$-rich environment changes the material from Ru to $RuO_2$. Thus, earlier high pressure studies on the Ru catalyst were actually looking at $RuO_2$. Second, after $RuO_2$ has been formed, it is important to know how to set the pressure conditions correctly, as also on $RuO_2(110)$ there is a low-pressure surface phase [the $O^{br}$ region in Fig. 2(a)], that has little in common with the catalytically active situation. The obtained agreement between the theoretical results and experimental data confirms furthermore (cf. also Ref. [15]) that $CO_2$ is primarily formed from adsorbed CO and O, and that the metal oxide, once it was created, does not play an active role, i.e., there is no indication of significant bulk diffusion. Thus, the catalysis is explained in terms of a Langmuir-Hinschlwood mechanism. Some contributions via the Eley-Rideal mechanism (e.g., scattering of gas-phase CO at $O^{cus}$) may play a minor role, but this process requires further calculations and experiments. With the advent of first-principles TOF maps obtained from DFT calculations [cf. Fig. 2], a more detailed database is in general becoming available for comparison with experiments, which will eventually advance the microscopic understanding of catalysis.

[1] C. Stampfl et al., Surf. Sci. 500, 368 (2002).
[2] K. Reuter and M. Scheffler, Phys. Rev. B 65, 035406 (2002).
[3] K. Reuter and M. Scheffler, Phys. Rev. Lett. 90, 046103 (2003); Phys. Rev. B 68, 045407 (2003).
[4] A. Michaelides et al., Chem. Phys. Lett. 367, 344 (2003).
[5] Z. Łodzianan and J. K. Nørskov, J. Chem. Phys. 118, 11179 (2003).
[6] P. Blaha, K. Schwarz, and J. Luitz, computer code WIEN97, Techn. Univ. Wien, Austria, 1999.
[7] The FP-LAPW approach is one of the most accurate DFT methods for describing polyatomic systems. Basis set, super cell setup, and the transition-state location procedure by mapping relevant reaction coordinates have been described before [3].
[8] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).
[9] P. Ruggerone, C. Ratsch, and M. Scheffler, in The Chemical Physics of Solid Surfaces, edited by D. A. King and D. P. Woodruff (Elsevier Science, Amsterdam, 1997), Vol. 8.
[10] D. P. Landau and K. Binder, A Guide to Monte Carlo Simulations in Statistical Physics (Cambridge University Press, Cambridge, England, 2000).
[11] S. Ovesson, A. Bogicevic, and B. I. Lundqvist, Phys. Rev. Lett. 83, 2608 (1999).
[12] P. Kratzer and M. Scheffler, Phys. Rev. Lett. 88, 036102 (2002).
[13] E. W. Hansen and M. Neurock, J. Catal. 196, 241 (2000); Surf. Sci. 464, 91 (2000).
[14] C. H. F. Peden and D. W. Goodman, J. Phys. Chem. 90, 1360 (1986).
[15] J. Wang et al., J. Phys. Chem. B 106, 3422 (2002).
[16] K. Reuter et al., Chem. Phys. Lett. 352, 311 (2002).
[17] K. Jacobi and G. Ertl (private communication); H. Over and M. Muhler, Prog. Surf. Sci. 72, 3 (2003).
[18] K. Reuter et al. (to be published).
[19] See EPAPS Document No. E-PRLTAO-93-006438 for movies displaying the dynamics of the surface under realistic catalytic conditions. A direct link to this document may be found in the online article's HTML reference section. The document may also be reached via the EPAPS homepage (http://www.aip.org/pubservs/epaps.html) or from ftp.aip.org in the directory/epaps. See the EPAPS homepage for more information. They can be found at http://w3.rz-berlin.mpg.de/~reuter/movies/movies.html.