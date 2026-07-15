As vacancies, Ga antisites and Au impurities in Zincblende and Wurtzite GaAs
nanowire segments from first principles

Yaojun A. Du, $^{1, \ast}$ Sung Sakong, $^{1}$ and Peter Kratzer$^{1}$

$^{1}$Fakultät für Physik and Center for Nanointegration (CENIDE), Lotharstraße 1, 47048 Duisburg, Germany

In this paper some specific issues related to point defects in GaAs nanowires are addressed with the help of density functional theory calculations. These issues mainly arise from the growth of nanowires under conditions different from those used for thin films or bulk GaAs, such as the co-existence of zincblende and wurtzite polytypes, the use of gold particles as catalyst, and the arsenic-limited growth regime. Hence, we carry out density-functional calculations for As vacancies, $Ga_{As}$ antisites, and Au impurities in ZB and WZ GaAs crystals. Our results show that As vacancies can diffuse within in a ZB GaAs crystal with migration barriers of $\sim$1.9 eV. Within WZ GaAs, As vacancy diffusion is found to be anisotropic, with low barriers of 1.60 up to 1.79 eV (depending on doping conditions) in the $ab$-plane, while there are higher barriers of 2.07 to 2.44 eV to diffuse along the $c$-axis. The formation energy of Au impurities is found to be generally much lower than those of arsenic vacancies or $Ga_{As}$ antisites. Thus, Au impurities will be the dominant defects formed in Au-catalyzed nanowire growth. Moreover, we find that it is energetically more favorable by 1 to 2 eV for an Au impurity to replace a lattice Ga atom than a lattice As atom in GaAs. An Au substitutional defect for a lattice Ga atom in ZB GaAs is found to create a charge transfer level in the lower half of the band gap. While our calculations locate this level at $E_{v} + 0.22$ eV, taking into account the inaccuracy of the density functional that ought to be corrected by a downshift of $E_{v}$ by about 0.2 eV results in good agreement with the experimental result of $E_{v} + 0.4$ eV.

PACS numbers:
Keywords: GaAs nanowire, vacancy diffusion, intrinsic defects, Au impurities, density-functional calculation

## I. INTRODUCTION

Semiconductor nanowires have been emerging as a promising building block for various nano-devices. $^{1}$ These potential applications include light emitters, $^{2}$ solar cells, $^{3}$ and microelectronics. $^{4,5}$ All these applications require such a prerequisite that it is possible to keep the concentration of intrinsic defects and impurities in the nanowires below a given threshold so as to enable long exciton lifetimes and to avoid unintentional doping due to electrically active impurities. In recent years, many experimental efforts$^{6-10}$ have been devoted to fast and controllable growth of nanowires that is desired for reliable devices; and a gold nanoparticle is often used as a catalyst to promote the growth of GaAs nanowires. However, an Au droplet that accelerates an underneath growing nanowire can also leave impurities within the GaAs nanowire. $^{11,12}$ Previous experimental efforts have focused on characterizing Au defect levels within a GaAs crystal, $^{13-15}$. Moreover, experimental studies employing X-ray energy-dispersive spectroscopy$^{7,11}$ indicate deviations from stoichiometry in the nanowires close to the growth zone, and thus point to the abundant intrinsic defects, in addition to Au impurities, in GaAs nanowires. While carrier lifetimes in core-shell nanowires from Au-free self-catalyzed growth$^{16,17}$ were found to be much longer than in nanowires from Au-catalyzed growth$^{12}$, they still fall short of the values reported for bulk samples by several orders of magnitude. This may indicate a higher level of growth-related intrinsic defects (as compared to bulk) even in Au-free nanowires.

The focus of our interest is the defects that could be formed in nanowire growth below the metal nanoparticle. While the most abundant defect in low-temperature grown bulk GaAs is the As antisite$^{18}$, we expect this defect not to play a role under the more Ga-rich growth conditions beneath a metal catalyst particle. It is known that near the melting point and under the conditions typical of liquid-phase epitaxy, As vacancies are the dominant defects in GaAs. $^{19}$ Furthermore, under As-deficient conditions, the As lattice site might remain unoccupied (As vacancy $V_{As}$), it could be occupied by gallium (Ga antisite $Ga_{As}$), or, in case of growth with a gold catalyst, may be occupied by an Au atom ($Au_{As}$). Since there is a general interest in possibly detrimental effects of Au on the properties of GaAs nanowires, we include $Au_{Ga}$ defects into our study.

In this context, one has to consider that the effective growth conditions for the nanowire material are probably very different from the moderately arsenic-rich conditions commonly used in GaAs thin film growth. This is due to the following reasons: In nanowire growth, material deposited from the vapor phase onto the substrate, the sidewalls and the metal nanoparticle can reach the interfacial area between the nanowire tip and the particle via surface diffusion$^{6,20-22}$ or diffusion through the liquid metal particle. $^{23}$ It is clear that sufficient Ga atoms can reach the interfacial growth zone at the nanowire tip, since the catalyst particle actually consists of a Au-Ga alloy. $^{8}$ The situation is less clear concerning the As supply, since the low-pressure solubility of As in gold is low (in Au-catalyzed growth), or a high high temperature leads to As loss (in self-catalyzed growth). In these cases, one would expect As-deficient growth conditions

at the nanowire–particle interface. One possible scenario is that additional arsenic can reach the growth zone via an As vacancy diffusion mechanism through the GaAs nanowire. Moreover, under As-deficient conditions, one would also expect that As vacancies could be left be- hind within the GaAs nanowire by the advancing inter- facial growth zone. A subsequent annealing process in arsenic vapor might be helpful to remove these vacan- cies. Therefore, it is important to understand $V_{As}$ diffu sion within GaAs bulk, in order to comprehensively un- derstand the As supply path during the growth process and to estimate a suitable annealing temperature for re- moving $V_{As}$ s in a nanowire. A previous theoretical study based on density functional theory (DFT) $^{24,25}$ calculated relatively high migration barriers of $\sim 2.4$ eV for a $V_{As}$ in zincblende GaAs. $^{26}$ This seemingly implies that As trans port through the nanowire could be inefficient. However, the convergence of the atomic-orbital basis sets employed in these DFT calculations has not been demonstrated.

While wurtzite GaAs cannot be obtained in bulk form by ordinary growth techniques, the GaAs nanowires grown with Au catalyst may exhibit both zincblende (ZB) and wurtzite (WZ) structures, or alternating seg- ments of these (and other) polytypes through stacking faults. $^{7,27-29}$ Hence, it is crucial to understand $V_{As}, Ga_{As}$ , and Au defects in both ZB and WZ GaAs crystals. There is considerable knowledge, both from experimental $^{19}$ and theoretical $^{30,31}$ sides, about intrinsic point defects in ZB GaAs. However, experimental data on point defects in WZ GaAs is still elusive. In this work, we will perform plane-wave DFT calculations to study various properties associated with $V_{As}, Ga_{As}$ , and Au defects in ZB and WZ GaAs crystals, and to investigate and compare $V_{As}$ dif fusion in both GaAs polytypes. This paper is organized as follows: The computational approach and supercell models are described in Sec. II. The formation energies of $V_{As}, Ga_{As}$ defects and Au impurities in ZB and WZ GaAs crystals are discussed in Sec. III. The diffusion of $V_{As}$ s in various charge states in ZB and WZ GaAs crys- tals are presented in Sec. IV. We summarize our work in Sec. V.

## II. METHODS OF CALCULATION

In this work, we have performed DFT calculations to study $V_{As}, Ga_{As}$ and substitutional Au impurities in ZB and WZ GaAs using the supercell method. The con- ventional unit cell for a ZB and a WZ GaAs crystal is shown in Fig. 1. Sufficiently large supercells of 216 atoms (ZB) or 96 atoms (WZ) are used to fully relax the strain induced by defects and impurities. We employ the projector augmented-wave (PAW) method $^{32,33}$ as imple mented in the VASP code $^{34,35}$ for all DFT calculations. The PAW potentials include 4s4p, 4s4p, and 5d6s elec- trons as valence electrons for As, Ga, and Au, respec- tively. The generalized-gradient approximation (GGA) is used for the exchange-correlation functional. $^{36}$ The Bril louin zone integration is performed using the Monkhorst- Pack $^{37}$ scheme over a $(2×2×2)$ k-point mesh (shifted with respect to the $\Gamma$ -point) for both ZB and WZ su percells. Then, the partition length is 0.06 Bohr $^{-1}$ or smaller in each direction. Spin-polarized calculations are performed for supercells that contain an odd num- ber of electrons. The optimized kinetic energy cutoff of $E_{cut}=250$ eV is used to compute the formation energies of various impurities and defects, whereas an $E_{cut}$ of 200 eV is used for studying $V_{As}$ diffusion in GaAs. The op timized parameters allow us to obtain a relative energy convergence of within 10 meV for all systems presented in this study. The method of a homogeneous background charge is used to model charge states of the defect within the supercell approach. We determined various diffusion paths for $V_{As}$ s within the As sublattice of both ZB and WZ GaAs crystals, employing the nudged-elastic band(NEB) method. $^{38-40}$ Here, the migration pathway is rep resented by several intermediate configurations between two fully relaxed end points and each image is relaxed until the perpendicular forces with respect to the mini- mum energy path are less than a given tolerance, which is set to be $0.03 eV/\AA$ in our calculations.

![](./images/867752545257259924_1.jpg)

FIG. 1: (Color online) The structure of ZB and WZ GaAs crystals. The conventional unit cell for a ZB and a WZ GaAs crystal is shown in (a) and (b), respectively. The As and Ga atoms are represented by large pink and small green spheres, respectively.

For ZB GaAs (space group $F\overline{4}3m$ ), we have obtained the optimized lattice constant of $a=5.76 \AA$ , in good agreement with the experimental value of $a=5.653 \AA.^{41}$ For WZ GaAs (space group $P_{6}3mc$ ), we have computed the lattice constant to be $a=4.05 \AA$ and $c=6.69$ Å, which compares well with previous GGA results of $a=4.050 \AA$ and $c=6.678 \AA.^{42}$ The calculated direct band gaps of GaAs are 0.17 eV and 0.22 eV in ZB and WZ crystals, respectively. These results reflect the well-known underestimation of the electronic band gap by semi-local DFT functionals, in particular, when the(too large) theoretical lattice constant is used. In addi- tion, we have performed DFT calculations with the same geometries as in GGA, but using the hybrid functional proposed by Heyd, Scuseria, and Ernzerhof (HSE). $^{43}$ Our calculations include $25\%$ of the exact exchange, and the screening parameter is set to be $0.2 \AA^{-1}$ . The band gaps,

that are computed to be 1.15 eV and 0.99 eV in ZB and WZ GaAs, respectively, are much closer to experimental values. Moreover, we conclude from these calculations that the valence band maximum experiences a down-shift of 0.48 eV in ZB GaAs (0.36 eV in WZ GaAs). These val- ues are in good agreement with recent literature $^{44}$ , and will be used as corrections when our computed results are compared to experiment. The orthorhombic Ga (space group Cmca) crystal and trigonal As (space group $R \overline{3} m$ ) crystal are used to compute the Ga and As chemical po- tentials.

Since ZB and WZ segments co-exist in GaAs nanowires, the band edges from ZB and WZ supercell calculations should be aligned accordingly. We have con- structed a 50 atom supercell of a heterostructure of WZ and ZB GaAs. The supercell consists of 13 ZB and 12 WZ bilayers that stack along $[\overline{1} \overline{1} \overline{1}]$ or [0001] for a ZB or a WZ segment, respectively. The constructed heterostructure is optimized for both the lattice constant and internal coordinates. Note that the lateral dimension of the het- erostructure happens to coincide with the average of the WZ and ZB lattice parameters. The valence band offset of the ZB and WZ segments can be computed $^{45}$ as

$$
\begin{aligned}
\Delta E_{V B}(\mathrm{GaAs})= & E_{v}^{\mathrm{ZB}}-E_{v}^{\mathrm{WZ}}-\left(E_{c o r e}^{\mathrm{ZB}}(\mathrm{As})-E_{c o r e}^{\mathrm{WZ}}(\mathrm{As})\right) \\
& +\left(E_{c o r e}^{\mathrm{ZB} \text { seg }}(\mathrm{As})-E_{c o r e}^{\mathrm{WZ} \text { seg }}(\mathrm{As})\right), \quad(1)
\end{aligned}
$$

where $E_{v}^{\mathrm{ZB}}$ and $E_{v}^{\mathrm{WZ}}$ are the valence band top en ergies at the $\Gamma$-point for ZB and WZ GaAs, respec tively, $E_{core }^{ZB}(As)$ and $E_{core }^{WZ}(As)$ are the core level ener gies of As atoms in bulk ZB and WZ GaAs, respectively, $E_{core }^{ZB seg }(As)$ and $E_{core }^{WZ seg }(As)$ are the core level energies of As atoms in ZB and WZ segments of the heterostruc- ture, respectively. We compute the band offset to be $\Delta E_{V B}(GaAs)=-0.0601 eV$ , in good agreement with the value of -0.0632 eV from a previous calculation. $^{46}$

## III. THE ENERGETICS OF DEFECTS AND Au IMPURITIES IN GaAs NANOWIRES

We start by calculating the formation energies of rel- evant intrinsic defects. The formation energy of a q- charged (q is an integer number) defect (or impurity) $X$ at site $Y$ as a function of the Fermi level $\varepsilon_{F}$ is defined by

$$
\begin{array}{r}
E_{f}\left[X_{Y}^{q}, \varepsilon_{\mathrm{F}}\right]=E\left[X_{Y}^{q}\right]-E_{h o s t}-\sum_{i} n_{i} \mu_{i}+q\left(\varepsilon_{\mathrm{F}}+E_{v}\right)+E_{c o r r}. \\
(2)
\end{array}
$$

Here, $E[X_{Y}^{q}]$ is the total energy of a $q$-charged supercell with a defect $X_{Y}$ and $E_{host }$ is the energy of a perfect GaAs bulk supercell with the same shape. $n_{i}$ and $\mu_{i}$ represent the change in the number of species $i$ in the supercell and the chemical potential for a species $i$ , re spectively. $\varepsilon_{F}$ is the Fermi level that depends on the doping condition, and $E_{v}$ is the valence band top en ergy of the corresponding bulk GaAs crystal. Due to the $(2 \times 2 \times 2)$ k-point mesh used for supercell calculations, the gap between the highest occupied (HOMO) and the low- est unoccupied (LUMO) orbitals is much higher in these supercell calculations compared to the gap at the $\Gamma$-point in GaAs bulk calculations. Even though this widened gap is a technical artifact of our method, it puts us in position to vary $\varepsilon_{F}$ in a rather wide range while still maintaining the physically correct charge distribution localized near the defect. The energy interval around $E_{v}$ in which our calculations can be expected to yield physically mean- ingful charge transfer levels, as a charged defect cannot transfer charge to the LUMO or from the HOMO, is indi- cated in the figures. The linear and quadratic correction term with respect to $q$ of $E_{corr }=\Delta V q+\alpha q^{2} / 2 \epsilon L$ ac counts for the spurious electrostatic interaction between periodic images of charged defects $^{47,48}$ . $\Delta V$ is a correc tion for the spurious potential off-set induced by the finite defect concentration in the calculation; it is calculated from the energy difference of atomic core levels between a neutral supercell with an $X_{Y}$ defect and a perfect bulk

![](./images/867752545257259924_2.jpg)

FIG. 2: (Color online) The formation energy of an As vacancy(a) and a Ga antisite (b) in various charge states in GaAs polytypes at different doping conditions, as a function of the Fermi level $\varepsilon_{F}$ . The formation energies of As vacancies in ZB GaAs and WZ GaAs are shown as dashed and solid lines, respectively. The thick lines represent stable charge states. The vertical lines indicate the HOMO and LUMO levels in the defect-free supercell and thus delimit the energy interval where the GGA total energies are considered reliable. The left and right $y$ -axes show the formation energies under As rich $(\mu_{As}^{upper })$ and Ga-rich $(\mu_{As}^{lower })$ conditions as described in the text. Here, one has the identity $\mu_{As}^{lower }=\mu_{As}^{upper }-0.7 eV$ .

supercell. The values for $\alpha$ and $\epsilon$, the Madelung constant and the static dielectric constant, respectively, are taken according to the ZB or WZ polytype of bulk GaAs, and $L$ is the supercell dimension used in the corresponding calculations. The values of $\alpha$, $\epsilon$, and $L$ are listed in Table III in the Appendix for the cases of ZB and WZ GaAs crystals, respectively. Our computed dielectric constant $\epsilon$ for ZB GaAs is 32% larger than the experimental value of $0.90\ \mathrm{\AA}^{-1}\mathrm{V}^{-1}.^{49}$ At the growth condition, the chemical potentials of Ga and As are in equilibrium with bulk GaAs. Thus, one has the identity $\mu_{\mathrm{Ga}}+\mu_{\mathrm{As}}=\mu_{\mathrm{GaAs}}$, where $\mu_{\mathrm{GaAs}}=-E_{\mathrm{GaAs}}^{bulk}$ is the cohesive energy per formula unit of a pertinent GaAs polytype. The range of the As chemical potential is specified in accordance with the growth condition, with the upper bound set to be at the equilibrium with bulk As, i.e., $\mu_{\mathrm{As}}^{upper}=-E_{\mathrm{As}}^{bulk}$. The lower bound is set to be at the equilibrium with bulk Ga as $\mu_{\mathrm{As}}^{lower}=-E_{\mathrm{GaAs}}^{bulk}+E_{\mathrm{Ga}}^{bulk}$. Disregarding the difference of the cohesive energies of GaAs of 20 meV in ZB and WZ crystals, we align the upper bound $\mu_{\mathrm{As}}^{upper}$ for ZB and WZ to the same value. We take the lower bound $\mu_{\mathrm{As}}^{lower}$ to be 0.7 eV below $\mu_{\mathrm{As}}^{upper}$, so that $\mu_{\mathrm{As}}^{lower}$ is very close to a Ga-rich condition for both ZB and WZ GaAs. The bulk energies of GaAs, Ga and As crystals are calculated using the optimized lattice parameters. Note that the upper and lower bounds of the As chemical potentials correspond to As- and Ga-rich growth conditions, respectively. In addition, the cohesive energy bulk Au per atom is inserted for the Au chemical potential, i.e., $\mu_{\mathrm{Au}}=-E_{\mathrm{Au}}^{bulk}$.

Figure 2(a) shows the $V_{\mathrm{As}}$ formation energies for various charge states $q$, indicating the formation energies of $V_{\mathrm{As}}$ in WZ are overall lower than those in ZB. The formation energies are computed using Eq. 2, and the potential off-sets $\Delta V$ associated with the $V_{\mathrm{As}}$s are listed in Table IV in the Appendix. Under an As-rich growth condition (left $y$-axis in Fig. 2(a)), the formation energies of neutral $V_{\mathrm{As}}$s are quite high (3.3 eV and 3.2 eV in ZB and WZ, respectively). Under a Ga-rich condition (right $y$-axis in Fig. 2(a)), the formation energies are lowered by 0.7 eV; however, the energies remain relatively high. Thus, the formation of As vacancies could be energetically unfavorable under usual GaAs nanowire growth conditions in both ZB and WZ segments. Our results show that $V_{\mathrm{As}}^{+}$ and $V_{\mathrm{As}}^{-}$ defects are stable at various doping conditions in ZB and WZ GaAs crystals. Deep $(+/-)$ levels are found at $E_{v}^{\mathrm{ZB}}+0.44$ and $E_{v}^{\mathrm{WZ}}+0.45$ eV in ZB and WZ, respectively. Since GaAs nanowires may have coexisting ZB and WZ segments, it is instructive to specify the charge transfer levels of defects in the WZ segments also with respect to the valence band edge of the ZB segments, using our results that the valence band maximum of ZB GaAs is 0.0601 eV lower than in WZ GaAs. Thus, one obtains the $(+/-)$ level in WZ to be $E_{v}^{\mathrm{ZB}}+0.51$ eV. We found that $V_{\mathrm{As}}^{2-}$ and $V_{\mathrm{As}}^{3-}$ in both ZB and WZ GaAs crystals are unstable, consistent with Ref. 30, because the structures relax to a GaAs antisite that is neighboring a Ga vacancy. As seen from Fig. 2, the neutral As vacancies are energetically unfavorable, indicating that a $V_{\mathrm{As}}$ in GaAs is a so-called 'negative $U$' system. Our results are consistent with a previous theoretical studies $^{30,50,51}$, although the quoted absolute positions of the $(+/-)$ levels in these studies are different from ours. For a quantitative comparison, it is important to realize that Schulz and von Lilienfeld $^{30}$ attempted to set $E_{v}$ to the true ionization potential, whereas we use the plain DFT-GGA value. Estimating the true valence band top from our HSE calculations, a down-shift of 0.4 eV (see Section II) should be applied to our $E_{v}$ value in order to compare to their work, or to experimental data. The same applies when comparing to the values of Komsa and Pasquarello, $^{51}$ who performed all their calculations with the HSE functional. With this in mind, our results are in much better agreement with these previous works. It is worth noting that the negative $U$ feature of a $V_{\mathrm{As}}$ disappears in their HSE calculations. This is due to the fact that the (negative) contribution of the electronic exchange energy, which is more pronounced in the hybrid functional, energetically favors spin-polarized solutions, e.g., the neutral $V_{\mathrm{As}}$ in the present case. Whether this stabilization of a $V_{\mathrm{As}}^{0}$ in a narrow range of the Fermi level is indeed a physical feature or not should be determined by future experiments.

The Ga antisite $\mathrm{Ga}_{\mathrm{As}}$ could be an another intrinsic defect within a growing GaAs nanowire under As-deficient conditions, and we show the formation energies of $\mathrm{Ga}_{\mathrm{As}}$ as a function of $\varepsilon_{\mathrm{F}}$ in Fig. 2(b). The formation energies are computed using Eq. 2, with the potential off-set $\Delta V$ associated with $\mathrm{Ga}_{\mathrm{As}}$ defects listed in Table IV in the Appendix. The formation energies are specified for both Ga-rich (right $y$-axis in Fig. 2(b)) and As-rich (left $y$-axis Fig. 2(b)) conditions, and formation energies are 1.4 eV lower in a Ga-rich condition than in an As-rich condition. In both ZB and WZ GaAs crystals, $\mathrm{Ga}_{\mathrm{As}}$s with charge states from $2+$ to $2-$ may be stable under certain doping conditions. The associated formation energies in WZ GaAs are overall lower than in ZB GaAs. The $\mathrm{Ga}_{\mathrm{As}}^{0}$ and $\mathrm{Ga}_{\mathrm{As}}^{+}$ defects are energetically more favorable by 0.13-0.14 eV in WZ than in ZB, whereas a $\mathrm{Ga}_{\mathrm{As}}^{-}$ defect is only 0.01 eV more stable in WZ. As a result, the charge transfer levels $(0/-)$ differ by 0.12 eV in ZB and WZ. It follows that, on an absolute scale, the charge transfer levels are located at $E_{v}^{\mathrm{ZB}}+0.21$ and 0.33 eV in ZB and WZ segments of a GaAs nanowire, respectively. We notice that both intrinsic defects of $V_{\mathrm{As}}$ and $\mathrm{Ga}_{\mathrm{As}}$ have deep charge transfer levels and they are deeper in WZ GaAs. Comparing Fig. 2(a) and (b), one may find that $V_{\mathrm{As}}$s are more stable than $\mathrm{Ga}_{\mathrm{As}}$s for the doping conditions of $\varepsilon_{\mathrm{F}}-E_{v}^{\mathrm{ZB}}<0.21$ (0.27) eV in ZB (WZ) under As rich conditions, while $\mathrm{Ga}_{\mathrm{As}}$s are more stable than $V_{\mathrm{As}}$s for the doping conditions of $\varepsilon_{\mathrm{F}}-E_{v}^{\mathrm{ZB}}>0.21$ (0.27) eV in ZB (WZ). When comparing to experiment, one should take into account that the "true" valence band top is lower than the $E_{v}$ resulting from our DFT-GGA calculations, such that the range of horizontal-axis values plotted in Fig. 2 approximately reflects the "true" band gap.

![](./images/867752545257259924_3.jpg)

FIG. 3: (Color online) The formation energies of a substitu-
tional Au defect in the ±1-charged, ±2-charged, and neutral
states in WZ and ZB GaAs crystals. The formation ener-
gies of a substitutional Au impurity for a lattice As atom
and a lattice Ga atom are shown in (a) and (b), respectively.
The formation energies of Au impurities in ZB GaAs and WZ
GaAs are shown as dashed and solid lines, respectively. The
thick lines represent stable charge states. The vertical lines
indicate the HOMO and LUMO levels in the defect-free su-
percell, same as Fig. 2. The left and right y-axes show the for-
mation energies under As-rich ($\mu_{\text{As}}^{upper}$) and Ga-rich ($\mu_{\text{As}}^{lower}$)
conditions as described in the text.

We also study the energetics of substitutional Au im-
purities in GaAs crystals, and the computed formation
energies of ${\text{Au}}_{\text{As}}$ and ${\text{Au}}_{\text{Ga}}$ as a function of $\varepsilon_{\text{F}}$ are shown
in Fig. 3. The formation energies of ${\text{Au}}_{\text{As}}$ and ${\text{Au}}_{\text{Ga}}$
are computed using Eq. 2, with the potential off-sets as-
sociated with ${\text{Au}}_{\text{As}}$ and ${\text{Au}}_{\text{Ga}}$ listed in Table IV in the
Appendix. Moreover, the formation energies are speci-
fied for both Ga-rich (right y-axis in Fig. 3) and As-rich
(left y-axis Fig. 3) conditions. It is found that under an
As-rich growth condition an ${\text{Au}}_{\text{Ga}}$ is energetically more
favorable than an ${\text{Au}}_{\text{As}}$ by about one to two eV both
in ZB GaAs and in WZ GaAs, depending on the dop-
ing conditions. However, under a Ga-rich growth condi-
tion, the formation energy of an ${\text{Au}}_{\text{Ga}}$ is 0.7 eV higher
than that under an As-rich condition, while the forma-
tion energy of an ${\text{Au}}_{\text{As}}$ becomes 0.7 eV lower. Therefore,
under a Ga-rich condition, the ${\text{Au}}_{\text{As}}$ defects turn out to
be more stable than ${\text{Au}}_{\text{Gas}}$. We expect that ${\text{Au}}_{\text{Ga}}$ de-
fects with charge states from 2+ to 2− may be stable
under certain doping conditions. An ${\text{Au}}_{\text{Ga}}$ has its charge
transfer levels mostly in the lower part of the band gap,
while the charge transfer levels of an ${\text{Au}}_{\text{As}}$ lie at some-
what higher energies. The ${\text{Au}}_{\text{As}}$ impurities occur pref-
erentially as 2+, + or neutral defects, while the levels
of negatively charged defects lie probably already above
the conduction band minimum of the host material. Fig-
ure 3(a) indicates the charge transfer levels of ${\text{Au}}_{\text{As}}$s are
deep, $E_{v}^{\text{ZB}}+0.78$ eV and $E_{v}^{\text{ZB}}+0.91$ eV for ZB and
WZ crystals, respectively. In contrast, an ${\text{Au}}_{\text{Ga}}$ impu-
rity switches from a neutral state to a 1− charged state
at $E_{v}^{\text{ZB}}$+0.22 eV and $E_{v}^{\text{ZB}}$+0.35 eV in ZB and WZ crys-
tals, respectively, as seen in Fig. 3(b). As stated before,
one should allow for a correction of about 0.4 eV to our
$E_{v}$ value when comparing to experiment. Experimen-
tal studies using deep-level transient spectroscopy and
photoluminescence spectroscopy13–15 have identified an
Au-related deep acceptor level of about 0.4 eV above the
valence band in bulk GaAs. Moreover, we find an ${\text{Au}}_{\text{Ga}}$
has a lower formation energy compared to an ${\text{Au}}_{\text{As}}$ under
the moderately As-rich growth conditions conventionally
used. Taking into account the down-shift of $E_{v}$ with re-
spect to the DFT-GGA value (see e.g., Ref. 44), it is
plausible that the experimentally observed defect level
at 0.4 eV above the valence band is indeed due to ${\text{Au}}_{\text{Ga}}$
defects.

We conclude this Section by discussing the energetics
of defects caused by a deficiency of arsenic under varying
growth conditions. In Fig. 4(a), we compare the forma-
tion energies of the lowest energy ${\text{V}}_{\text{As}}$, ${\text{Au}}_{\text{As}}$ and ${\text{Ga}}_{\text{As}}$
defects in p-type ZB and WZ GaAs crystals with the
condition of $\varepsilon_{\text{F}}-E_{v}^{\text{ZB}}=0$, as a function of As chemical
potential $\mu_{\text{As}}$. Our calculations show that ${\text{Au}}_{\text{As}}$ impu-
rities have the lowest formation energies, while ${\text{V}}_{\text{As}}$ and
${\text{Ga}}_{\text{As}}$ defects have clearly higher formation energies. Fig-
ure 4(b) shows the same comparison for n-type ZB and
WZ GaAs crystals with $\varepsilon_{\text{F}}=E_{v}^{\text{ZB}}+1.0$ eV. Here, a ${\text{Ga}}_{\text{As}}$
in the 2− charge state has the lowest formation energy,
followed by ${\text{Au}}_{\text{As}}$ and ${\text{V}}_{\text{As}}$. Consequently, when grow-
ing GaAs nanowires with a gold catalyst droplet, some
${\text{Au}}_{\text{As}}$ defects will be formed in the GaAs nanowire, in
particular for a p-doped material. The Au impurities
act as deep centers and are thus detrimental to the op-
tical properties of nanowires. In gold-free self-catalyzed
growth, ${\text{Ga}}_{\text{As}}$ and ${\text{V}}_{\text{As}}$ defects may exist in the nanowire,
albeit at much smaller concentration than the Au de-
fects if the material is p-doped. Out of these three de-
fect species, only the ${\text{V}}_{\text{As}}$ defect is expected to be mobile
via a hopping diffusion mechanism. The mobility of the
${\text{Ga}}_{\text{As}}$ and ${\text{Au}}_{\text{As}}$ defects will most probably be vacancy-
mediated, and thus require the ${\text{V}}_{\text{As}}$ presence. Moreover,
it is conceivable that ${\text{V}}_{\text{As}}$ hopping diffusion could play a
role in the nanowire growth process as a mechanism sup-
plying arsenic to the interfacial growth zone between the
nanowire tip and the catalyst droplet. Hence, we will in-
vestigate the detailed diffusion processes of ${\text{V}}_{\text{As}}$s in GaAs
crystals in the following Section.

### (a) $\varepsilon_{\mathrm{F}}=E_{v}^{\mathrm{ZB}}$
![](./images/867752545257259924_4.jpg)

### (b) $\varepsilon_{\mathrm{F}}=E_{v}^{\mathrm{ZB}}+1.0\mathrm{eV}$
![](./images/867752545257259924_5.jpg)

FIG. 4: (Color online) The formation energies of $V_{\mathrm{As}}$, $\mathrm{Au}_{\mathrm{As}}$ and $\mathrm{Ga}_{\mathrm{As}}$ defects in GaAs crystals as a function of $\mu_{\mathrm{As}}$. In (a) and (b), the Fermi energy is set to be at the calculated top of valence band and 1 eV above, respectively, to describe a $p$-type or an $n$-type material. Only the energetically most favorable charge states are shown.

## IV. As VACANCY DIFFUSION IN GaAs

Arsenic vacancies in GaAs have been characterized experimentally by positron annihilation $^{52}$ and by scanningtunneling microscopy $^{53}$. For ZB GaAs, a number of theoretical studies, using (semi-)local DFT $^{30,54,55}$ or hybrid functionals $^{31,51}$, have been carried out, and the diffusion pathway of the arsenic vacancy has been investigated $^{26}$. Interestingly, these calculations claimed the existence of a metastable interstitial state along the diffusion path in ZB GaAs, while this issue is unexplored for WZ GaAs.

We start by characterizing the geometry of $V_{\mathrm{As}}$ in GaAs crystals in more detail. As shown in Fig. 5, the neighboring Ga atoms with respect to a $V_{\mathrm{As}}$ define a Ga tetrahedron. To specify the local deformation of a crystal due to the $V_{\mathrm{As}}$ presence, we study the relaxation of the edge length $l$ of the tetrahedron and compare it to the equilibrium distance between two neighboring Ga atoms in the ZB (WZ) GaAs crystal of $l_{0}=4.07$ (4.05) Å. Similarly, the relaxed tetrahedron volume $V$ will be compared to the equilibrium tetrahedron volume in ZB (WZ) GaAs crystal of $V_{0}=7.97$ (7.93) $\mathring{\mathrm{A}}^{3}$.

![](./images/867752545257259924_6.jpg)

FIG. 5: (Color online) The geometry of $V_{\mathrm{As}}$ in GaAs crystals. The relaxations of $V_{\mathrm{As}}^{+}$ and $V_{\mathrm{As}}^{-}$ in ZB GaAs are illustrated in (a), while the relaxations of two sets of stable $V_{\mathrm{As}}^{+}$ and $V_{\mathrm{As}}^{-}$ in WZ GaAs are characterized in (b) and (c), respectively. We have found two stable $V_{\mathrm{As}}^{+}$s (M1 and M2) and two $V_{\mathrm{As}}^{-}$s (M1 and M2) in WZ GaAs. A $V_{\mathrm{As}}$ is highlighted by a big blue sphere, and its four neighboring Ga atoms are highlighted by A, B, C, and D labeled spheres. These neighboring Ga atoms form a tetrahedron. The other attached As and Ga atoms are represented by small pink red and large green spheres, respectively. The right panel indicates the relaxed edge length of the Ga tetrahedron. The upper and lower numbers refer to a $V_{\mathrm{As}}^{+}$ and a $V_{\mathrm{As}}^{-}$, respectively.

<table><tbody><tr><td></td><td>$V_{\mathrm{As}}^{+}$</td><td>$V_{\mathrm{As}}^{0}$</td><td>$V_{\mathrm{As}}^{-}$</td></tr><tr><td>ZB</td><td>$0.922V_{0}$</td><td>$0.757V_{0}$</td><td>$0.516V_{0}$</td></tr><tr><td>WZ-M1</td><td>$0.896V_{0}$</td><td>$0.696V_{0}$</td><td>$0.518V_{0}$</td></tr><tr><td>WZ-M2</td><td>$0.926V_{0}$</td><td></td><td>$0.512V_{0}$</td></tr></tbody></table>

TABLE I: Ga tetrahedron volumes of $V_{\mathrm{As}}$ in various charge states. $V_{0}$ represents the equilibrium tetrahedron volume in a ZB (WZ) GaAs crystal of $V_{0}=7.97(7.93)\ \mathring{\mathrm{A}}^{3}$.

For a $V_{\mathrm{As}}^{-}$ in ZB GaAs, the edge lengths of the Ga atom tetrahedron are all contracted (see the right panel of Fig. 5(a)), resulting in a significantly reduced volume of $V=0.516V_{0}$ (48.4% compression) as listed in Table I. Especially, the A-D and B-C edges are most contracted up to $l=0.702l_{0}$ (29.8 % compression), while other edges

are compressed by $\sim 11$ %. The deformation reduces the symmetry of the distorted Ga tetrahedron to $D_{2d}$ which is in accordance with previous studies. $^{54,55}$ In WZ GaAs, there exist two different, but energetically very similar structures (M1 and M2) for a relaxed $V_{\text{As}}^{-}$ (see Fig. 5(b) and (c)). The WZ-M2 configuration is slightly more stable than the WZ-M1 configuration in terms of energetics. Both WZ-M1 and WZ-M2 $V_{\text{As}}^{-}$ configurations exhibit similar deformations as a $V_{\text{As}}^{-}$ in ZB, and the relaxed tetrahedron volumes are reduced by 48.4 % to 48.8 %, respectively. This is comparable to the ZB case. The relaxed Ga tetrahedron for WZ-M1 and WZ-M2 $V_{\text{As}}^{-}$s possesses a $C_{2v}$ and a $C_{1}$ symmetry, respectively.

For a $V_{\text{As}}^{+}$, the tetrahedron of neighboring Ga atoms contracts in volume by only 7.8 % in ZB GaAs, whereas it contracts by 7.4 % to 11.4 % in WZ GaAs, as listed in Table I. In particular, $V_{\text{As}}^{+}$s have one edge compressed, while the other edges are slightly expanded. The WZ-M2 $V_{\text{As}}^{+}$ configuration has the A-C edge (within the $ab$ plane) compressed. In contrast, the WZ-M1 $V_{\text{As}}^{+}$ configuration has the A-D edge (out of the $ab$ plane) compressed. In other words, the deformation of $V_{\text{As}}^{+}$ in WZ GaAs is anisotropic, and hence the relaxed Ga tetrahedron for WZ-M1 and WZ-M2 $V_{\text{As}}^{+}$s possesses $C_{2v}$ or $C_{1}$ symmetry, respectively. In addition, despite the neutral state being unstable, we mention that the volumes of neutral As vacancies are $0.757V_{0}$ in ZB and $0.696V_{0}$ in WZ-M1, respectively. It is worth noting that the vacancy volume becomes smaller with increasing electronic charge. The physical reason for this general trend lies in the fact that the additional electrons in the vacancy allow for the filling of orbitals with bonding character that are formed by symmetry-adapted linear combinations of the Ga dangling-bond orbitals.

In the following, we assume that the $V_{\text{As}}$ diffusion proceeds via a neighboring As atom of the arsenic sublattice hopping into the vacancy. Schematically, an As atom hops out of an initial Ga-tetrahedron cage into an adjacent target Ga-tetrahedron cage that previously enclosed the As vacancy site. We refer to the tetrahedron that surrounds the migrating As atom as the initial tetrahedron, and refer to the adjacent Ga-tetrahedron that surrounds the target As vacancy site as the target tetrahedron. We note that the reverse process occurs with the same probability, with the role of initial and target tetrahedron interchanged. The diffusion process can be decomposed into an As escape from the initial tetrahedron, its interstitial motion between the two tetrahedra, and an entry into the target tetrahedron. Note that one of the Ga atoms is located at the common apex of both tetrahedra.

Since ZB GaAs is a cubic crystal, the four possible diffusion paths of a $V_{\text{As}}$ to four neighboring As sites are symmetrically equivalent. The diffusion path shown Fig. 6 is sufficient to describe As diffusion in ZB GaAs. Figure 6(a) illustrates the detailed diffusion process of a $V_{\text{As}}^{+}$ in ZB GaAs, indicating an overall migration barrier of 1.93 eV. The local minimum configurations ($i$ and $v$ in Fig. 6(a)) as well as the saddle point configurations ($ii$ and $iv$ in Fig. 6(a)) along the diffusion path are illustrated by the ball-and-stick models in the figure. In the target tetrahedron, the AG edge corresponds to the short edge (the AD in Fig. 5(a) ). By expanding the bond between As and Ga at the D-site, the diffusing As atom escapes from the initial tetrahedron. During the escape process, the initial tetrahedron is expanding, while the target tetrahedron is contracting. After passing through the ABC face of the tetrahedron, the diffusing As atom arrives at the first saddle point ($ii$) which represents the transition state for $V_{\text{As}}^{+}$ migration. In this configuration, the As-Ga bonds to the initial tetrahedron apexes are broken except for the A-site. The target tetrahedron volume is compressed from $0.922V_{0}$ to $0.719V_{0}$ which corresponds to the volume of a neutral As vacancy (see Table I). This observation implies that a positively charged

![](./images/867752545257259924_7.jpg)

FIG. 6: (Color online) The energy path of $V_{\text{As}}^{1+}$ (a) and $V_{\text{As}}^{1-}$ (b) diffusion in ZB GaAs. The structures of two ground state minima ($i$ and $v$), an interstitial state ($iii$), and transition states ($ii$ and $iv$) are illustrated. The As and Ga atoms are represented by lager pink and small green spheres, respectively.

As vacancy in the target tetrahedron attracts electrons ahead of the As migration. When migrating toward the target tetrahedron in the interstitial space, the diffusing As atom reaches an interstitial state (iii) with a shallow energy dip. At this moment, the diffusing As atom is located at an octahedral interstitial site in ZB GaAs. In this interstitial state, the migrating As creates two additional bonds to target tetrahedron apexes, indicating that the As atom starts to supply electrons to the target tetrahedron. Consequently, the target tetrahedron volume further contracts to $0.662V_0$. This volume is still a bit larger than for a negatively charged As vacancy, but notably smaller than for a neutral As vacancy. Passing through the AEF face of the target tetrahedron, the diffusing As atom enters the target vacancy. The diffusion process is thus completed. When the As atom diffuses into the target tetrahedron, it establishes the As-Ga bond to the G-site. The migration from the octahedral interstitial site to the final state has a shallow migration barrier of 0.19 eV which is 0.04 eV lower than the backward diffusion barrier. We note that the contraction of the AG edge of the empty target tetrahedron has moved over to the BC edge of the (finally empty) initial tetrahedron.

Figure 6(b) shows the $V_{\text{As}}^-$ diffusion path in ZB GaAs, which is similar to $V_{\text{As}}^+$ diffusion with a slightly lower migration barrier of 1.91 eV. Again, we find the escape barrier from the initial tetrahedron to be the rate-limiting step. In the interstitial space, there is also an interstitial As configuration located in a shallow dip, and it occupies an octahedral interstitial site in ZB GaAs. The associated initial and target tetrahedra at this stage have volumes of $1.102V_0$ and $0.673V_0$, respectively. We note that the tetrahedron volume expands while loosing an electron (see Table I). The diffusing As atom at the interstitial site has to overcome an entry barrier of 0.13 eV to migrate into the target tetrahedron, which is 0.19 eV lower than that of the reverse diffusion process. The initial tetrahedron volume is reduced to the $V_{\text{As}}^-$ value after the diffusing As passes through the second saddle point. We note that the two saddle points along the diffusion path have different energies. Although an oversimplified consideration solely based on the atomic positions suggests that a symmetric mechanism might exist, the observed symmetry breaking is physical because the charge balance between the two tetrahedra under the presence of the migrating As atom is non-symmetric. Therefore, it is meaningful to distinguish between the escape (first) saddle point or the entry (second) saddle point to be rate-limiting.

Our results qualitatively agree with the previous theoretical study $^{26}$, which reported migration barriers of 2.41 eV and 2.38 eV for $V_{\text{As}}^+$ and $V_{\text{As}}^-$ diffusion in ZB GaAs, respectively, using atomic orbital basis sets. Both in their and in our work, the computed diffusion barrier of a $V_{\text{As}}^-$ is slightly lower than that of a $V_{\text{As}}^+$. However, in our plane-wave-based calculations, diffusion barriers of $V_{\text{As}}^+$ and $V_{\text{As}}^-$ are computed to be 1.93 eV and 1.91 eV, respectively, which are about 0.5 eV lower in energy than the values reported in Ref. 26. We believe that these differences are due to the more complete basis set for the wave functions in our calculations, which allows for a more accurate description of the energetics, in particular at transition state geometries.

![](./images/867752545257259924_8.jpg)

Next, we perform analogous calculations for $V_{\text{As}}^+$ and $V_{\text{As}}^-$ diffusion in WZ GaAs. Due to the lower crystal symmetry of WZ, one needs to consider two pathways; i.e., an As vacancy can diffuse within the $ab$ plane by hopping from site 1 to site 2 or along the $c$ axis by hopping from site 2 to site 3, as illustrated in Fig. 1(b). First, we discuss the vacancy diffusion within the $ab$ plane. Figure 7 shows that $V_{\text{As}}^+$ and $V_{\text{As}}^-$ can diffuse in the $ab$ plane in WZ GaAs with migration barriers of 1.79 eV and 1.60 eV, respectively. As discussed above, there are two different minimum configurations for $V_{\text{As}}^+$ and $V_{\text{As}}^-$ defects, M1 and M2, in WZ GaAs. The transition from the more

hours. In WZ GaAs, the reduction of the energy barrier by 0.14 eV to 1.79 eV reduces the annealing time by a factor of 10 to 31.3 minutes. Thus, we conclude that the $V_{\text{As}}\text{s}$ introduced in a GaAs nanowire during As-deficient growth can be annealed within a reasonable time frame at a temperature of 700 K. We hereby summarize the diffusivities of $V_{\text{As}}^{+}$ and $V_{\text{As}}^{-}$ defects in ZB and WZ GaAs crystals for various diffusion processes in Table II.

## V. DISCUSSION AND SUMMARY

Using DFT calculations, we have characterized the $V_{\text{As}}$, $\text{Ga}_{\text{As}}$, and Au defects in GaAs crystals that may be introduced in GaAs nanowires grown with the help of metal droplets under As-deficient conditions at the interfacial growth zone. The substitutional $\text{Ga}_{\text{As}}$, $\text{Au}_{\text{As}}$, and $\text{Au}_{\text{Ga}}$ defects exhibit similar formation energies and defect levels in both ZB and WZ GaAs crystals. Moreover, a $V_{\text{As}}$ defect behaves as a 'negative $U$'-system, switching from a $V_{\text{As}}^{+}$ in a $p$-doped material to a $V_{\text{As}}^{-}$ in an $n$-doped material, for both GaAs crystals. In case that a Au droplet is used a catalyst for nanowire growth, the formation of substitutional Au defects is possible and is found to be energetically more favorable than the formation of $\text{Ga}_{\text{As}}$ or $V_{\text{As}}$ defects. Moreover, we have shown that it is energetically more favorable by about 1 to 2 eV for an Au substitutional defect to replace a lattice Ga atom than a lattice As atom in either ZB or WZ GaAs. Given that DFT-GGA calculations give a too small band gap, the calculated acceptor level of $\text{Au}_{\text{Ga}}$ at $E_{v} + 0.22$ eV is found to be in reasonable agreement with the experimental value of $E_{v} + 0.4$ eV in ZB GaAs.

In Au-free, self-catalyzed growth of nanowires that are grown at higher temperatures, $^{56}$ the formation of $\text{Ga}_{\text{As}}$ could be expected. In particular, for Ga-rich growth conditions and $n$-type material, the $\text{Ga}_{\text{As}}^{2-}$ species has a low formation energy. This could lead to growth of non-stoichiometric, Ga-enriched GaAs. $^{7,11}$ The incorporation of $\text{Ga}_{\text{As}}^{2-}$ will counteract the $n$-doping by deliberately added donor species. This may explain why it is rather difficult to obtain $n$-type conductivity in ZB GaAs nanowires, and only high concentrations of $\text{Sn}_{\text{Ga}}$ have proven successful so far. $^{57}$ Under less Ga-rich growth conditions, the formation of $V_{\text{As}}\text{s}$ could be expected, and their diffusion might even play a role for the material transport in the growth of a GaAs nanowire. We note that As interstitials, which could in principle also contribute to As mass transport, tend to have a higher formation energy than $V_{\text{As}}\text{s}$, apart from very As-rich conditions. $^{30}$ Since we are interested in the As-deficient growth conditions below the nanoparticle, we don't consider the As interstitial diffusion here. Our results show that i) $V_{\text{As}}\text{s}$ can diffuse within ZB GaAs with a migration barrier of about 1.9 eV; and ii) $V_{\text{As}}\text{s}$ diffuse favorably within the $ab$ plane in WZ GaAs with somewhat lower migration barriers of 1.6 to 1.8 eV. Based on these results, we estimate that it takes about five hours to anneal the $V_{\text{As}}\text{s}$ at 700 K in a ZB GaAs nanowire, but only 30 minutes in a WZ nanowire. Thus, an annealing of GaAs nanowires under an arsenic atmosphere could be useful to obtain samples with a longer lifetime for the charge carriers. However, the diffusivity of $V_{\text{As}}\text{s}$ in the nanowires is too low to contribute substantially to the arsenic supply at the nanowire growth zone, in particular in WZ GaAs, where the diffusion barrier along the $c$-axis is higher than in ZB GaAs.

TABLE III: The Madelung constants ($\alpha$), the dielectric constants ($\epsilon$) and the dimension of GaAs supercells ($L$) for computing the formation energy as described in Eq. 2. The values are listed for both ZB and WZ GaAs supercells. For convenience, $\epsilon$ is given in units of $e\mathrm{\AA}^{-1}\mathrm{V}^{-1}$. The dimensionless dielectric constant is obtained by multiplying this value with 14.4.

|     | $\alpha$ | $\epsilon$ | $L$ ($\mathrm{\AA}$) |
|-----|----------|------------|-----------------------|
| ZB  | 1.638    | 1.18       | 17.29                 |
| WZ  | 1.641    | 1.12       | 12.16                 |

TABLE IV: The values of the potential off-set corrections for $V_{\text{As}}$ ($\Delta V_{V@\text{As}}$), $\text{Au}_{\text{As}}$ ($\Delta V_{\text{Au}@\text{As}}$), $\text{Au}_{\text{Ga}}$ ($\Delta V_{\text{Au}@\text{Ga}}$), and $\text{Ga}_{\text{As}}$ ($\Delta V_{\text{Ga}@\text{As}}$) defects in WZ and ZB GaAs crystals. All numbers are given in units of eV.

|     | $\Delta V_{V@\text{As}}$ | $\Delta V_{\text{Au}@\text{As}}$ | $\Delta V_{\text{Au}@\text{Ga}}$ | $\Delta V_{\text{Ga}@\text{As}}$ |
|-----|---------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| ZB  | $-0.05$                   | $-0.01$                           | $-0.04$                           | $-0.05$                           |
| WZ  | $-0.09$                   | $-0.02$                           | $-0.02$                           | $-0.09$                           |

### Acknowledgments

We acknowledge Center for Computational Sciences and Simulation (CCSS) of University Duisburg-Essen for the computer time and the Deutsche Forschungsgemeinschaft DFG for the financial support through the project KR 2057/5-1.

### Appendix: Parameters for computing formation energies

The Madelung constants, the calculated dielectric constants, and the dimensions of ZB and WZ GaAs crystals are listed in Table III. $L$ represents the distance between the nearest neighbor defects within a supercell. It is taken to be length of the $a$-axis of a 216 atom ZB and a 96 atom WZ GaAs crystal as listed in Table III. The dielectric constants are the $\epsilon_{aa}$ components of pertinent dielectric tensors. They include both electronic and ionic contributions. The values of the potential off-set corrections for various defect and impurity calculations are listed in Table IV.

yaojun.du@uni-due.de

1 L. Samuelson, Materials Today 5, 22 (2003).
2 A. R. Guichard, D. N. Barsic, S. Sharma, T. I. Kamins,
and M. L. Brongersma, Nano Lett. 6, 2140 (2006).
3 J. R. Maiolo III, B. M. Kayes, M. A. Filler, M. C. Putnam,
M. D. Kelzenberg, H. A. Atwater, and N. S. Lewis, Journal
of American Chemical Society 129, 12346 (2007).
4 Y. Cui and C. M. Lieber, Science 291, 851 (2001).
5 C. Thelander, P. Agarwal, S. Brongersma, J. Eymery, L. F.
Feiner, A. Forchel, M. Scheffler, W. Riess, B. J. Ohlsson,
U. Gösele, et al., Materials Today 9, 28 (2006).
6 L. Jensen, M. Bjork, S. Jeppesen, A. Persson, B. Ohlsson,
and L. Samuelson, Nano Letters 4, 1961 (2004).
7 A. I. Persson, M. W. Larsson, S. Stenström, B. J. Ohlsson,
L. Samuelson, and L. R. Wallenberg, Nature Mat. 3, 677
(2004).
8 J. C. Harmand, G. Patriarche, N. Péré-Laperne, M.-N.
Mérat-Combes, L. Travers, and F. Glas, Appl. Phys. Lett.
87, 203101 (2005).
9 K. A. Dick, K. Deppert, L. S. Karlsson, L. R. Wallenberg,
L. Samuelson, and W. Seifert, Advanced Functional Mate-
rials 15, 1603 (2005).
10 K. Dick, K. Deppert, T. Martensson, B. Mandl, L. Samuel-
son, and W. Seifert, Nano Letters 5, 761 (2005).
11 M. J. Tambe, S. Ren, and S. Gradečak, Nano Letters 10,
4584 (2010).
12 S. Breuer, C. Pfüller, T. Flissikowski, O. Brandt, H. T.
Grahn, L. Geelhaar, and H. Riechert, Nano Letters 11,
1276 (2011).
13 P. Hiesinger, Physica Status Solidi (a) 33, K39 (1976).
14 Z. X. Yan and A. G. Milnes, J. Electrochem. Soc. 129,
1353 (1982).
15 V. Pandian, Y. N. Mohapatra, and V. Kumar, Japanese
Journal of Applied Physics 30, 2815 (1991).
16 F. Jabeen, G. Bulgarini, N. Akopian, G. Patriarche,
V. Zwiller, and J.-C. Harmand, in Proceedings of NWG-
06, edited by V. G. Dubrovskii (St. Petersburg Academic
University, 2012).
17 M. Bar-Sadan, J. Barthel, H. Shtrikman, and L. Houben,
Nano Letters 12, 2352 (2012).
18 J. Dabrowski and M. Scheffler, Phys. Rev. B 40, 10391
(1989).
19 D. T. J. Hurle, J. Appl. Phys. 107, 121301 (2010).
20 K. Haraguchi, K. Hiruma, K. Hosomi, M. Shirai, and
T. Katsuyama, J. Vac. Sci. Technol. B 15, 1685 (1997).
21 V. G. Dubrovskii, G. E. Cirlin, I. P. Soshnikov, A. A.
Tonkikh, N. V. Sibirev, Y. B. Samsonenko, and V. M. Usti-
nov, Phys. Rev. B 71, 205325 (2005).
22 V. Pankoke, S. Sakong, and P. Kratzer, Phys. Rev. B 86,
085425 (2012).
23 P. Kratzer, S. Sakong, and V. Pankoke, Nano Letters 12,
943 (2012).
24 P. Hohenberg and W. Kohn, Physical Review 136, B864
(1964).
25 W. Kohn and L. J. Sham, Physical Review 140, A1133
(1965).
26 F. El-Mellouhi and N. Mousseau, Applied Physics A 86,
309 (2007).
27 I. P. Soshnikov, G. E. Cirlin, A. A. Tonkikh, Y. B. Samso-
nenko, V. G. Dubrovskii, V. M. Ustinov, O. M. Gorbenko,
D. Litvinov, and D. Gerthsen, Physics of the Solid State
47, 2213 (2005).
28 D. Spirkoska, J. Arbiol, A. Gustafsson, S. Conesa-Boj,
F. Glas, I. Zardo, M. Heigoldt, M. H. Gass, A. L. Bleloch,
S. Estrade, et al., Phys. Rev. B 80, 245325 (2009).
29 U. Jahn, J. Lähnemann, C. Pfüller, O. Brandt, S. Breuer,
B. Jenichen, M. Ramsteiner, L. Geelhaar, and H. Riechert,
Phys. Rev. B 85, 045323 (2012).
30 P. A. Schultz and O. A. von Lilienfeld, Modelling Simul.
Mater. Sci. Eng. 17, 084007 (2009).
31 H.-P. Komsa and A. Pasquarello, Physica B 407, 2833
(2012).
32 P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).
33 G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).
34 G. Kresse and J. Hafner, Phys. Rev. B 47, 558(R) (1993).
35 G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169
(1996).
36 J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev.
Lett. 77, 3865 (1996), erratum – Phys. Rev. Let. 78, 1396
(1997).
37 H. J. Monkhorst and J. D. Pack, Phys. Rev. B 13, 5188
(1976).
38 H. Jónsson, G. Mills, and K. W. Jacobsen, in Classical
and Quantum Dynamics in Condensed Phase Simulations,
edited by B. J. Berne, G. Ciccotti, and D. F. Coker (World
Scientific, Singapore, 1998), pp. 385–404.
39 G. Henkelman, B. P. Uberuaga, and H. Jónsson, J. Chem.
Phys. 113, 9901 (2000).
40 G. Henkelman and H. Jónsson, J. Chem. Phys. 113, 9978
(2000).
41 O. Madelung, ed., Data in Science and Technology, Editor
in chief R. Poerschke, Semiconductors, Group IV Elements
and III-V Compounds (Springer-Verlag, Berlin, 1991).
42 T. Cheiwchanchamnangij and W. R. L. Lambrecht, Phys.
Rev. B 84, 035203 (2011).
43 J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys.
118, 8207 (2003).
44 W. Chen and A. Pasquarello, Phys. Rev. B 86, 035134
(2012).
45 A. Franciosi and C. G. V. de Walle, Surface Science Re-
ports 25, 1 (1996), ISSN 0167-5729.
46 A. De and C. E. Pryor, Phys. Rev. B 81, 155210 (2010).
47 C. G. Van de Walle and J. Neugebauer, J. Appl. Phys. 95,
3851 (2004).
48 G. Makov and M. C. Payne, Phys. Rev. B 51, 4014 (1995).
49 W. J. Moore and R. T. Holm, Journal of Applied Physics
80, 6939 (1996).
50 F. El-Mellouhi and N. Mousseau, Phys. Rev. B 71, 125207
(2005).
51 H.-P. Komsa and A. Pasquarello, Journal of Physics: Con-
densed Matter 24, 045801 (2012).
52 K. Saarinen, P. Hautojärvi, P. Lanki, and C. Corbel, Phys.
Rev. B 44, 10585 (1991).
53 J. Gebauer, R. Krause-Rehberg, C. Domke, P. Ebert,
K. Urban, and T. E. M. Staab, Phys. Rev. B 63, 045203
(2001).
54 K. Laasonen, R. M. Nieminen, and M. J. Puska, Phys.
Rev. B 45, 4122 (1992).
55 L. Gilgien, G. Galli, F. Gygi, and R. Car, Phys. Rev. Lett.
72, 3214 (1994).
56 F. Jabeen, V. Grillo1, S. Rubini, and F. Martelli, Nan-
otechnology 19, 275711 (2008).

$^{57}$ C. Gutsche, A. Lysov, I. Regolin, K. Blekker, W. Prost,
and F.-J. Tegude, Nanoscale Res. Lett. **6**, 65 (2011).
