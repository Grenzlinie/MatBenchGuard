# Surface Energy Evolution in Pharmaceutical Powder Micronization Using Compressed Gas Antisolvent (Re-)Precipitation
Daniel E. Rosner*,† and Manuel Arias-Zugasti‡

Department of Chemical & Environmental Engineering, Sol Reaction Engineering Group, Yale University, New Haven, Connecticut 06520-8286, United States

## ABSTRACT:
We illustrate the importance of environment-dependent surface energy changes in predicting the micronization of active pharmaceutical ingredients (APIs) in gas antisolvent precipitation (GASP) processes. This size-reduction scheme exploits compressed $CO_{2}(g)$ as antisolvent (AS) at near-ambient temperatures. Ordinary API-loaded solvents (often sprays) are contacted with dense $CO_{2}$, and during $CO_{2}$ uptake in an evolving expanding liquid API + solvent + $CO_{2}$ solution droplet, particle nucleation $(N)$ sets in, continuing along with growth $(G)$ and, ultimately, coagulation. A rational method [due to Nielsen and Sohnel (J. Cryst. Growth 1971, 11, 233) and Mersmann (J. Cryst. Growth 1990, 102, 841)) is used to estimate the changing embryonic solid/ternary solution interfacial energy, $\gamma$. We demonstrate the dramatic yield and crystal size distribution (CSD) consequences of surface energy evolution (SEE) by carrying out $N/G$ calculations for the surrogate organic API: phenanthrene dissolved in representative well-mixed micrometer-sized toluene droplets (sprayed into $298$ K $CO_{2}$ for $p < 60$ bar). To solve the population balance partial differential equation, we exploit the method of characteristics. Our results demonstrate that assuming constant surface energy, sometimes reasonable for API precipitation via the rapid expansion of supercritical-$CO_{2}$ solvent (i.e.: relatively dilute rapid expansion of a supercritical solution conditions), fails for GASP-process modeling. When the crystal growth kinetics are sufficiently rapid, SEE also modifies performance via the Gibbs−Kelvin reduction of small particle growth rates. Rational yet tractable methods to incorporate both systematic effects in future design/optimization/parameter estimation calculations are suggested.

## 1. INTRODUCTION AND OBJECTIVES
An emerging and versatile process for the size reduction of pharmaceutically active powders under mild processing conditions exploits compressed $CO_{2}$ gas as an antisolvent (AS), into which a convenient active pharmaceutical ingredient (API)-containing liquid solvent is injected. $^{1-7}$ This results in API reprecipitation as an ultrafine powder. Often abbreviated with the acronym GASP (for gas(-induced) antisolvent precipitation) or PCA (for precipitation via compressed antisolvent), this process presents many thermodynamic, kinetic (nucleation, growth), and convective-diffusion transport challenges to the theorist seeking a realistic yet tractable process model. $^{8-11}$ The present contribution $^{12}$ focuses on relaxing some of the troubling assumptions of relevant earlier work and is intended to ultimately improve the ability of process engineers to predict performance and select optimum GASP operating conditions−i.e., to produce, at higher yields, active pharmaceutical ingredients of desired mean particle size with narrow population spread.

Previous work on modeling near-critical $CO_{2}$ antisolventinduced precipitation of "micronized" pharmaceuticals $^{9,10}$ has made extensive use of "classical nucleation theory" (CNT) to estimate particle birth rates. $^{13,14}$ This convenient (yet much maligned!) theory, in which the creation of interfacial energy appears as an activation barrier that must be overcome, eliminates the need to perform a separate population balance on small embryonic precursor particles. However, as is now well-known, it introduces the effective surface free energy, $\gamma$, as a decisive "material property" appearing in the nucleation rate expression cubed in the dimensionless argument of the exponential function (see section 2.2). For example, in so-called RESS applications, $^{1,15}$ in which an API "surrogate", phenanthrene, particles are precipitated from dilute solutions in dense $CO_{2}$ which is rapidly expanded, this effective interfacial energy has been estimated to be only about $19$ $mJ/m^{2,13,14}$ and, of particular concern here, treated as a constant. We demonstrate below that while this latter assumption may be acceptable in some (RESS-type) applications, it is inappropriate to realistically describe API-particle inception and growth in the more flexible GASP process−which starts with nondilute API solutions in conventional (effective) liquid solvents. The need to include surface energy evolution (SEE) for nucleation was apparently first recognized by Dodds et al. $^{16}$ in their modeling of a semibatch GASP process for the anti-inflammatory corticosteroid BDP dissolved in liquid acetone. However, these authors did not focus on this particular effect and also treated the small particle growth process as unmodified by SEE. By exploiting our present well-mixed-droplet (WMD) GASP model, along with the $N/G$ laws subsequently described, we are able to unambiguously demonstrate here the expected role of SEE in dramatically modifying product yield and powder size distributions. However, more detailed experiments and analysis will probably be necessary to establish the adequacy of this present approach and/or point the way to further systematic improvements. In this regard, one possible alternative route to

Received: August 7, 2013
Revised: December 26, 2013
Accepted: February 7, 2014
Published: February 17, 2014

![](./images/813161692035809281_1.jpg)
© 2014 American Chemical Society
4489
dx.doi.org/10.1021/ie4025853 | Ind. Eng. Chem. Res. 2014, 53, 4489−4498

anticipate/incorporate SEE effects¹⁷ is briefly considered in section 4.3.

Historically, especially in the field of industrial crystallization, effective constant surface energies have been "back-calculated" based on direct or indirect measurements of sparingly soluble particle homogeneous nucleation rates. But, in the ASP applications of interest here, the API solute is initially often present in an effective organic solvent, implying the likelihood (if not desirability) of initial nondiluteness prior to extensive CO₂ addition. For example, near 300 K the presently considered API surrogate phenanthrene (C₁₄H₁₀) exhibits a saturation mole fraction in toluene (or benzene) of about 20%, corresponding to a saturation mass fraction near 1/3. With the introduction of the antisolvent (here CO₂) we demonstrate in later text that the effective surface energy of the solid/fluid interface will necessarily "evolve", increasing more than enough to dramatically reduce the predicted particle birth rate: $\dot{B}'''$, in the time-dependent supersaturated "expanding liquid" solution. This reduction will diminish with the additional uptake of antisolvent (CO₂), as shown in section 2.2. These expectations, along with significant, if less dramatic, effects on recently nucleated particle growth rates, motivated the following analysis to provide a rational yet tractable way to anticipate the $N + G$ consequences of such effective surface energy evolution.

## 2. METHODS: QUASI-STEADY ESTIMATION OF RELEVANT TIME-DEPENDENT SURFACE ENERGY IN GASP PROCESSES

Our premise is that while there is some intrinsic API (surrogate phenanthrene) crystal surface energy (relative to a vacuum or its own low sublimation pressure at its triple point), the effective value, $\gamma_{\text{eff}}$ (when "wetted" by a liquidlike solution containing the solvent (T), the solute (Ph), and the antisolvent (CO₂)), will be reduced significantly, in accord with the equations developed below. For simplicity, in what follows we neglect the presence of contaminants (e.g., solvent) in the solid phase.

### 2.1. Estimation of Evolving Effective Surface Energy.
A useful precedent and starting point is provided by the laboratory-scale semibatch GASP-process study of Dodds et al.,¹⁶ who recognized the existence of SEE in modeling GASP nucleation rates. They incorporated a Nielsen–Sohnel–Mersmann (NSM) correlation of the following form:¹⁸,¹⁹

$$
\Gamma \propto \ln \left( \frac{n_{\text{API}}^{\text{s}}}{n_{\text{API}}^{\text{L}}} \right)^{1/3}
\tag{1}
$$

(where $\Gamma \equiv \gamma v_{\text{m}}^{2/3}/(k_{\text{B}}T)$ is the dimensionless surface energy, $n_{\text{API}}$ is the number density of API in the droplet [superscript L] or crystal [superscript s], $v_{\text{m}}$ is the molecular volume of API in the solid state, and $k_{\text{B}}T$ is the Boltzmann constant times absolute temperature) to evaluate local nucleation rates via classical nucleation theory (CNT) while leaving their assumed crystal growth rate law unaltered in their numerical analysis of the relevant univariate population balance.

Because of its simplicity and our present goals, we also adopt this NSM correlation (eq 1). We also suggest (section 2.4) a method to incorporate SEE in a more appropriate law for crystal growth kinetics in transcritical environments.²⁰ For the present we select the "constant" (proportional to $k_{\text{B}}T/v_{\text{m}}^{2/3}$) in eq 1 to agree with previous estimates of $\gamma$ for the Ph/CO₂ system (e.g., 19 mJ/m² at $T = 343$ K and $p = 260$ bar,²¹ in the absence of the solvent toluene—obtaining the value 1.06 in this manner). Then, exploiting our convenient idealized mathematical model for an isobaric GASP process,²⁰ we can compare crystal size distribution (CSD) predictions using either constant surface energy or eq 1. In this way it is possible to unambiguously and economically demonstrate the role of SEE in modifying product powder distributions and precipitate yield. While instructive, more detailed experiments and analysis will probably be necessary to either establish the adequacy of our present approach, and/or point the way to further systematic improvements (see, also, section 4.3).

### 2.2. Surface Energy Evolution for CO₂-Saturated Solvent + API Solutions.
As a useful preliminary exercise, consider a saturated CO₂ + T + Ph solution at 1 bar, 298 K. We now ask, how would $\Gamma$ (computed using the method of section 2.1) change if the VSE level of Ph decreased as this liquid became saturated with the antisolvent CO₂ at higher pressures (here up to 64 bar) while disallowing solvent evaporation or Ph precipitation? Using our thermodynamic model (section 3), the results for this reference state $\Gamma$ are shown in Figure 1—also including the effects of initial Ph undersaturation. While these $\Gamma$-values are found to be less than 0.6 below ca. 40 bar, a rapid rise is observed above ca. 50 bar, with values well above unity when the pressures are such that the expanded liquid has a CO₂ mole fraction above ca. 0.8, with a corresponding reduction in the saturation number density $n_{\text{API}}^{\text{L}}$ (see eq 1).

![](./images/813161692035809281_2.jpg)

Figure 1. Dimensionless surface energy vs $p$ for an initially vapor–liquid-equilibrium (VLE) CO₂ + T + Ph mixture at $p = 1$ bar and $T =$ 298.15 K, with $x_{\text{Ph}}/x_{\text{Ph}}^{\text{sat}} = 1$ (lower dotted curve) and 0.1 (upper dotted curve). Solid curves show the corresponding $\Gamma$ found for this API-dilute mixture after CO₂ addition up to the saturation level, but without Ph/T precipitation or vaporization. The gray curve corresponds to vapor–liquid–solid-equilibrium (VLSE) conditions.

### 2.3. Effects of Surface Energy Evolution on both Nucleation and Growth Kinetics.
Because classical nucleation theory (CNT) predicts an API-particle "birth" rate, $\dot{B}'''$ (particles per unit time and volume), proportional to

$$
\dot{B}''' \propto \Gamma^{1/2} \exp\left( \frac{-16\pi\Gamma^{3}}{3 \ln^{2} S} \right)
\tag{2}
$$

where $S$ is the prevailing (activity-based) supersaturation,¹³⁻¹⁵,²¹,²² the preliminary results of section 2.2 immediately lead us to expect dramatic modifications in the expected output particle number densities and mean sizes. This is confirmed when allowance is made (section 2.4) for the simultaneous evolution of supersaturation using appropriate solute mass balance equations—and we provide comparable

results (shown dashed) when $\Gamma$ is (unrealistically) forced to remain constant (at its initial value at the outset of $\mathrm{CO}_{2}$ influx). The reader may have noticed that many published descriptions of classical nucleation theory refer to $\gamma$ as the "surface energy of the new (precipitated) phase"—as if this were a property of the new phase alone—independent of the host environment. This view is quite misleading, as convincingly illustrated in this study.

2.3.1. Remarks on "Secondary" Nucleation and Heterogeneous Nucleation. Several earlier treatments of GASP/PCA processes have explicitly included what is called "secondary" nucleation and its parametrization. This class of mechanisms, associated with nuclei formation from existing particles, is deliberately omitted here for simplicity. Dependent upon the solvent/antisolvent contacting scheme, their relative importance is indeed often "secondary". However, when such mechanisms cannot be neglected (see, e.g., Jarmer et al. $^{23}$ ), SEE remains likely to play an important role. [Note: For example, in the "mixed suspension mixed product removal" (MSMPR) study of poly(lactic acid) (PLLA) precipitation from methylene chloride in liquid $\mathrm{CO}_{2}$ (see Jarmer et al. $^{23}$ ), the rate of secondary nucleation was empirically inferred to be nearly linear in the product of the single particle growth rate, $\dot{G}$, and the suspension mass density (their $M_{T}$ ). But in section 2.4 we show how SEE can influence monomer-based growth rates via a particle-size-dependent $S_{\text {eff. }}$ Keeping in mind that $M_{T}$ is proportional to our particle volume fraction, $\phi_{\mathrm{p}}$ (section 3.1), then our Figure 3 suggests how SEE would modify this contribution to secondary nucleation. On this basis alone we are led to expect that when AS/S contacting conditions are such that secondary nucleation is important, SEE (section 2.1) is also likely to be consequential.] This should also be true if foreign nanoparticle nuclei were present in the initial solution sprayed into the $\mathrm{CO}_{2}$-containing chamber. Here we simply assume that any such preexisting nuclei cannot compete with the embryos formed by homogeneous nucleation of the nondilute solute.

2.4. Effects of Surface Energy Evolution on Particle Growth Kinetics. Coupled component balance equations that enable the actual AS-initiated supersaturation "history" to be calculated must include the growth of previously nucleated particles by API (supersaturated solute) "monomer scavenging" as well as current homogeneous nucleation. Thus, another systematic effect of surface energy evolution, surprisingly omitted in all earlier GASP modeling, is that associated with the reduced growth rate of recently born particles. In our present GASP-process model (described more completely in ref 20) we incorporate this additional effect by introducing a Gibbs-Kelvin-Ostwald factor, $F_{\mathrm{GKO}}$, presuming that the volumetric growth rate of a particle of volume $v$ will be approximately proportional to $v^{2 / 3}\left(1-\left(v_{*} / v\right)^{1 / 3}\right)$, where $v_{*}$ is the CNT critical volume at the prevailing instantaneous supersaturation, $S$; i.e.,

$$
\frac{v_{*}}{v_{\mathrm{m}}}=\frac{32 \pi}{3}\left(\frac{\Gamma}{\ln S}\right)^{3}
$$

(3)

More explicitly, we have implemented a droplet growth rate law ( $2 \dot{G}=\mathrm{d} d_{\mathrm{p}} / \mathrm{d} t$, where $d_{\mathrm{p}}$ is the instantaneous particle diameter and $t$ is time) of the factorable form

$$
\dot{G}=v_{\mathrm{m}, \mathrm{API}} \dot{Z}_{\mathrm{API}}^{\prime \prime} k_{\mathrm{G}}(T, \ldots)\left(\ln ^{n-1} S\right) \frac{F_{\mathrm{GKO}}}{S} \ln \left(\frac{S}{F_{\mathrm{GKO}}}\right)
$$

where the grouping $k_{\mathrm{G}}(T, \ldots) \ln ^{n-1} S$, containing the phenomenological coefficients $k_{\mathrm{G}}(T, \ldots)$ and $n$, plays the role of an overall incorporation probability $(\varepsilon), \dot{Z}_{\mathrm{API}}^{\prime \prime}$ is the prevailing API molecular impingement flux, and $F_{\mathrm{GKO}} \simeq S^{\left(v_{*} / v\right)^{1 / 3}}$. [Note: Here, and in eq 6 in subsequent text, we make use of a rational interpolation formula between the ideal gas limit (for $\phi / \phi_{\mathrm{L}} \ll$ 1) and liquid environments using a normalized molecular volume fraction: $\phi / \phi_{\mathrm{L}}$, where $\phi_{\mathrm{L}} \approx 0.62$. For details, see ref 20.] Note that, for $v \gg v_{*}$, this law reduces to the frequently observed behavior: $\dot{G} \sim \ln ^{n} S$ in liquid solvents. ${ }^{24}$ It is also noteworthy that when $n=1$, the dimensionless rate constant $k_{\mathrm{G}}(T, \ldots)$ and the corresponding overall incorporation probability, $\varepsilon$, become identical. Further details of these rate laws and our mathematical/numerical methods, beyond the scope of this present work, are contained in ref 20.

Because of the CNT self-consistency requirement $v_{*}>v_{\mathrm{m}}$, an interesting corollary of eq 2 is that CNT will no longer be self-consistent if the local supersaturation $S$ exceeds $\exp (3.224 \Gamma)$. This necessary condition was satisfied (see Figure 2) for the simulations discussed in sections 4.1 and 4.2.

![](./images/813161692035809281_3.jpg)

Figure 2. Time history of dimensionless critical particle volume, $v_{*}$, for an initially VLE $\mathrm{CO}_{2}+\mathrm{T}+\mathrm{Ph}$ mixture at $p=1$ bar and $T=298.15 \mathrm{~K}$, after instantaneous compression to $p=56$ bar and subsequent $\mathrm{CO}_{2}$ addition. The solid curve shows results based on prevailing dimensionless surface energy $\Gamma$ given by eq 1 . The dotted curve shows corresponding results when $\Gamma$ is assumed to be constant. Present results are based on a constant AS-uptake rate assumption, which becomes inaccurate toward the end of our numerical calculations, when droplet AS saturation level is reached. As a consequence the plateau followed by a sharp variation observed toward the end of the present calculations (constant $\Gamma$ case), and incipient leveling-off of $v_{*}$ (variable- $\Gamma$ case), are not expected to be seen in a real experiment.

### 3. GASP-PROCESS MODEL TO INVESTIGATE "SEE" CONSEQUENCES

3.1. Well-Mixed Droplet Model. As a tractable "platform" for examining the GASP-process consequences of surface energy evolution, we have adopted a well-mixed (single) droplet (WMD) model in which we focus on crystal size distributions resulting from homogeneous nucleation and interface-controlled particle growth during the stage in which isobaric $\mathrm{CO}_{2}$ uptake at constant (impingement-controlled) rate occurs with negligible loss of solvent from the swelling droplet. As indicated previously, we make use of classical nucleation theory for the birth rate, and, for the growth kinetics in these transcritical environments, we introduce a collision theory

<table>
<caption>Table 1. Pure Component Properties (AS, S, and API Surrogate)<sup>a</sup></caption>
<thead>
<tr>
<th>component</th>
<th>M (kg/kmol)</th>
<th>$T_c$ (K)</th>
<th>$p_c$ (bar)</th>
<th>$V_c$ (m³/kmol)</th>
<th>$\omega$</th>
<th>$Z_c$</th>
</tr>
</thead>
<tbody>
<tr>
<td>CO₂ (AS)</td>
<td>44.01</td>
<td>304.2</td>
<td>73.8</td>
<td>0.0940</td>
<td>0.225</td>
<td>0.274</td>
</tr>
<tr>
<td>toluene (S)</td>
<td>92.14</td>
<td>591.8</td>
<td>41.1</td>
<td>0.3155</td>
<td>0.257</td>
<td>0.263</td>
</tr>
<tr>
<td>phenanthrene (API surrogate)</td>
<td>178.23</td>
<td>869.3</td>
<td>29.0</td>
<td>0.554</td>
<td>0.495</td>
<td>0.222</td>
</tr>
</tbody>
</table>

<sup>a</sup>The value used here for the sublimation enthalpy of phenanthrene at the triple point ($T_{\text{API,tp}} = 372.4$ K) was $\Delta H_{\text{sublim}} = 90.34$ MJ/kmol, and the corresponding saturation pressure was $p_{\text{tp}} = 24.04$ Pa.

perspective (see ref 25 and preceding section 2.4). For the relevant solution thermodynamics already implicit in the results shown in Figure 1, we adopted a Peng−Robinson cubic EOS incorporating binary interaction coefficients (for the $a$ and $b$ parameters) specific to the ternary $\text{Ph} + \text{T} + \text{CO}_2$ system²⁶⁻²⁸ (see Table 1). Thus, the $a$ and $b$ parameters were computed according to the usual mixing rules, $a = \sum_i \sum_j x_i x_j a_{ij}$ and $b = \sum_i \sum_j x_i x_j b_{ij}$, with

$$
a_{ij} = \left(1 - k_{ij} \right) \left(a_i a_j \right)^{1/2}, \quad b_{ij} = \left(1 - l_{ij} \right) \frac{b_i + b_j}{2} \tag{5}
$$

where the values of the binary interaction parameters $k_{ij}$ and $l_{ij}$ are as follows: for $\text{CO}_2\text{−T}$, $k_{ij} = 0.090$ and $l_{ij} = 0.0$; for $\text{CO}_2\text{−Ph}$, $k_{ij} = 0.078$ and $l_{ij} = -0.030$; for $\text{T−Ph}$, $k_{ij} = -0.004$ and $l_{ij} = -0.059$.

Molar balance equations²⁵ are written for each of the solution components, and a population balance equation (a linear PDE containing the above-mentioned rate laws and host fluid properties²⁹) is written to track the univariate particle number density distribution function $n(v,t)$—assuming negligible "growth" by Brownian coagulation.²⁰ This latter approximation, defended *a posteriori*, enables our use of the method of characteristics (MOC) to numerically generate complete particle size distributions (PSD), free of any imposed PSD-"shape" constraints (see section 3.3 and refs 29 and 30). While several volume-based moments of $n(v,t)$ are of practical and theoretical interest,²⁹ we focus subsequent discussion on a dimensionless Sauter mean diameter, SMD, and a dimensionless relative spread parameter, $\sigma/\text{SMD}$ (where $\sigma$ is the particle diameter standard deviation of the precipitated phase), when evaluated at times which are specified multiples of the characteristic uptake time:

$$
t_{\text{AS}} \equiv \frac{d_0 x_{\text{AS}}^{\text{sat}}}{6 V_{\text{L}}^{\text{sat}} \dot{Z}_{\text{AS,w}}''} \frac{\mathcal{V}^{\text{sat}}(p,T)}{\mathcal{V}_0} \tag{6}
$$

where $\mathcal{V}_0 = (\pi/6)d_0^3$ is the initial droplet volume, superscript sat refers to saturation conditions, subscript 0 refers to initial conditions, $x_{\text{AS}}$ is the AS mole fraction, and $V_{\text{L}}$ is the molar volume of the liquid phase.

In text that follows (sections 4.1 and 4.2), using this WMD physical model, we illustrate the predicted dramatic consequences of surface energy evolution on the crystal size distribution function, as well as the corresponding dimensionless API powder mean diameter—i.e., $\text{SMD}/d_{\text{ref}}$ and dimensionless powder population spread (i.e., $\sigma/\text{SMD}$) for initially Ph-saturated toluene droplets of 1 μm diameter sprayed into $\text{CO}_2$ at 56 bar. While the effects of SEE on particle nucleation rates *via* CNT are decisive (eq 2 and section 4.3), we also incorporate (sections 2.3 and 4.2) the significant effects of SEE on growth rate reductions for recently "born" particles—but these growth rate effects are expected to be secondary under these particular conditions for a substance such as phenanthrene near 298 K.²⁰

We consider here the individual component balance equations appropriate to our present GASP mathematical model. Recall that we focus on the stage of isobaric, isothermal antisolvent AS uptake with negligible loss of solvent S or solute API—treating the hypothetical expanding liquid droplet as well-mixed at each instant.

For the solvent S (toluene) we impose the condition of negligible loss during $\text{CO}_2$ uptake; i.e.,

$$
\frac{\text{d}}{\text{d}t} \left[ \frac{x_{\text{S}} (1 - \phi_{\text{p}})}{V(x;\ p,\ T)} \mathcal{V} \right] = 0 \tag{7}
$$

where $V(x;p,T)$ is the molar volume of the prevailing ternary fluid mixture of composition $x \equiv \{x_{\text{S}},\ x_{\text{API}},\ x_{\text{AS}}\}^T$, $\mathcal{V}$ is the present value of the (expanded) droplet total volume (see subsequent text), and $\phi_{\text{p}}$ is the present value of the API particle volume fraction (initially zero).

For the antisolvent (AS) we consider the molar inflow rate ($\dot{N}_{\text{AS}}$) to be constant at the initial value:

$$
\dot{N}_{\text{AS}} = \dot{N}_{\text{AS,0}} = \pi d_0^2 \dot{Z}_{\text{AS}}'' \tag{8}
$$

In that case the AS-component balance ODE can be written

$$
\frac{\text{d}}{\text{d}t} \left[ \frac{x_{\text{AS}} (1 - \phi_{\text{p}})}{V(x;\ p,\ T)} \mathcal{V} \right] = \dot{N}_{\text{AS}} \tag{9}
$$

Perhaps most interesting is the balance equation for the component API which is ultimately distributed between the initial solute (monomer in solution) and the precipitated particles. Thus, we can impose the condition of constancy of $N_{\text{API}}$, where

$$
N_{\text{API}} = \left[ \frac{x_{\text{API}} (1 - \phi_{\text{p}})}{V(x;\ p,\ T)} + \frac{\phi_{\text{p}}}{N_{\text{A}} v_{\text{m}}} \right] \mathcal{V} = N_{\text{API,0}} \tag{10}
$$

noting that $\phi_{\text{p,0}} = 0$, where $N_{\text{A}}$ is Avogadro's number ($0.6023 \times 10^{27}$ molecules/(kg-mol)).

By assumption, in the expanded solvent all mole fractions will sum to unity at any instant, and the total "droplet volume" $\mathcal{V}$ must satisfy the overall molar balance:

$$
\frac{\text{d}}{\text{d}t} \left[ \left( \frac{1 - \phi_{\text{p}}}{V(x;\ p,\ T)} + \frac{\phi_{\text{p}}}{N_{\text{A}} v_{\text{m}}} \right) \mathcal{V} \right] = \dot{N}_{\text{AS}} \tag{11}
$$

where $V(x;p,T)$ is fixed by the prevailing composition and the Peng−Robinson EOS. Of course, the initial value of $\mathcal{V}$ is simply the (specified) value of $(\pi/6)d_0^3$.

3.2. Particle Population Balance Equation. Before the onset of appreciable Brownian coagulation, the univariate²⁹ population balance equation (PBE) for the condensate API population (particles per unit droplet volume $n(v,t)$) is³¹

$$
\frac{\partial n}{\partial t}+\frac{\partial}{\partial v}(\dot{v} n)=\dot{B}^{\prime \prime \prime} \delta\left(v-v_{*}\right)-n \frac{\mathrm{d}}{\mathrm{d} t} \ln \left[\left(1-\phi_{\mathrm{p}}\right) \mathcal{V}\right]
\tag{12}
$$

where $\dot{v}$ is the single particle growth rate law in terms of particle volume,
$$
\dot{v}=a(v) \dot{G}=(36 \pi)^{1 / 3} v^{2 / 3} \dot{G}
\tag{13}
$$
and $\delta\left(v-v_{*}\right)$ is the Dirac $\delta$ function centered at the critical size $v_{*}$.

The first term on the right-hand side (RHS) of eq 12 represents the time variation of $n(v, t)$ as a consequence of homogeneous nucleation (see eq 4), and the second term represents the time variation due to changes in the available droplet volume $\left(1-\phi_{\mathrm{p}}\right) \mathcal{V}$. We note that (when $\left(1-\phi_{\mathrm{p}}\right) \mathcal{V}$ is increasing) this term has the character of a first-order homogeneous sink of particles, with a size-independent effective rate constant $(\mathrm{d} / \mathrm{d} t) \ln \left[\left(1-\phi_{\mathrm{p}}\right) \mathcal{V}\right]$.

While the former PBE (eq 12) is clearly coupled to the (time-dependent) environment conditions through the relevant quantities $S, \Gamma, v_{*}, \dot{B}^{\prime \prime \prime}$, and $\dot{G}$, the environment evolution equations (given by eqs 7−11), together with the Peng−Robinson EOS, are coupled to the particle number density distribution function $n(v, t)$ only through the particle volume fraction $\phi_{\mathrm{p}}$, given in terms of $n$ by
$$
\phi_{\mathrm{p}}=\int_{0}^{\infty} v n(v, t) \mathrm{d} v
\tag{14}
$$

The evolution equation for $\phi_{\mathrm{p}}$ is found by integrating $(v \times$ eq 12). Thus we find
$$
\frac{\mathrm{d} \phi_{\mathrm{p}}}{\mathrm{d} t}=\int_{0}^{\infty} \dot{v} n(v, t) \mathrm{d} v+v_{*} \dot{B}^{\prime \prime \prime}-\phi_{\mathrm{p}} \frac{\mathrm{d}}{\mathrm{d} t} \ln \left[\left(1-\phi_{\mathrm{p}}\right) \mathcal{V}\right]
\tag{15}
$$
which, together with eq 12, eqs7−11, and the Peng−Robinson EOS, closes the system of evolution equations that define our mathematical model of this physical system.

### 3.3. Numerical Methods Employed: Method of the Characteristics Formulation.
The first-order linear PDE for $n(v, t)$ allows for a formal solution *via* the MOC, using the particle volume as the coordinate along the characteristic paths. The characteristic path $v=v(t)$ is considered, given by the solution of the first-order ODE $\mathrm{d} v / \mathrm{d} t=\dot{v}, v\left(t_{0}\right)=v_{0}$ (where the starting time $t_{0}$ and the initial value $v_{0}$ have arbitrary values). As long as the characteristic path $v(t)$ does not cross the timedependent value of $v_{*}$, the particle nucleation term is identically zero, allowing for the following formal quadrature of eq 12:
$$
\begin{aligned}
n[v(t), t]= & n\left[v_{0}, t_{0}\right] \frac{\left(1-\phi_{\mathrm{p}}\left(t_{0}\right)\right) \mathcal{V}\left(t_{0}\right)}{\left(1-\phi_{\mathrm{p}}(t)\right) \mathcal{V}(t)} \exp \left[-\\
& \left.\int_{t_{0}}^{t} \frac{\mathrm{d} \dot{v}}{\mathrm{d} v}\right|_{v(t)} \mathrm{d} t\right]
\end{aligned}
\tag{16}
$$

On the other hand, if at a certain value of time (say $t_{*}$) this characteristic line crosses the time-dependent critical volume $\left(v\left(t_{*}\right)=v_{*}\left(t_{*}\right)\right)$, then the nucleation term sets in. In this case integration of eq 12 over the infinitesimal time interval $\left(t_{*}-\right.$ $\mathrm{d} t, t_{*}+\mathrm{d} t$ ) leads to the following boundary (i.e., "jump") condition $^{25}$ that connects the values of $n[v(t), t]$ before $\left[n\left[v_{*}\right.\right.$, $\left.\left.t_{*-}\right]=n_{-}\right)$and after $\left(n\left[v_{*}, t_{*+}\right]=n_{+}\right)$the crossing
$$
n_{+}=n_{-}+\frac{\dot{B}^{\prime \prime \prime}\left(t_{*}\right)}{\left|\dot{v}-\left.\dot{v}_{*}\right|_{t_{*}}\right.}
\tag{17}
$$

Hence, whenever a characteristic line crosses the nucleation size, the corresponding value of $n[v(t), t]$ undergoes a discontinuity, with intensity given by $\dot{B}^{\prime \prime \prime}\left(t_{*}\right) /\left|\dot{v}-\left.\dot{v}_{*}\right|_{t_{*}}\right.$.

Although the former quadrature (eq 16) and boundary condition (eq 17) provide a formal solution of the PBE, it is not straightforward to extract numerical information from this solution without further simplifications. This is because the numerical evaluation of eqs 16 and 17 needs to be carried out along with the numerical integration of the system of ODEs that determine the evolution of the environment and the integro-ODE that determines the value of $\phi_{\mathrm{p}}$. The solution of this last equation (eq 15), or alternatively the immediate result eq 14, is difficult to evaluate in a numerically accurate way using the information provided by eqs 16 and 17, partly because of the discontinuous nature of $n[v(t), t]$ at each crossing time $t_{*}$, which forces one to consider relatively large numbers of characteristic paths to get acceptable results.

In the present work this difficulty has been solved by means of a perturbation scheme, in which particle growth acts as a small correction to the time evolution dictated by droplet swelling and particle nucleation. This perturbation scheme is based on the large disparity observed, under present conditions, between the characteristic growth and nucleation times, both of them determined by an order of magnitude analysis of the former system of evolution equations (eqs 7−11, eq 12).

In the results shown as follows, we have used the following dimensionless variables. The dimensionless particle volume is given by $w \equiv v / v_{\text {ref }}$, where $v_{\text {ref }}=6.44 v_{\mathrm{m}}$ is defined as the critical nucleation size corresponding to reference values of surface tension and supersaturation. In the present work these reference values have been defined as the corresponding $\Gamma$ and $S$ found at current pressure (56 bar) and temperature (298 K), and reference droplet composition. The latter has been defined as that corresponding to instantaneous compression up to 56 bar of a 1 bar-saturated VLE mixture, after addition of $\mathrm{CO}_{2}$ up to the saturation level $x_{\mathrm{CO}_{2}}^{\text {sat }}(56$ bar, $298 \mathrm{~K})$, assuming the (hypothetical) absence of precipitation despite saturation with the antisolvent $\mathrm{CO}_{2}$, and negligible solvent loss. This convenient reference state has also been used to define the corresponding reference values of the particle nucleation and growth rates. Finally, a dimensionless particle number distribution function $f$ has been defined by $f \equiv n v_{\text {ref }} / n_{\text {ref }}$, where the reference particle number density is $n_{\text {ref }} \equiv \phi_{\mathrm{p}, \infty} / v_{\text {ref }}$, with $\phi_{\mathrm{p}, \infty}$ being the limiting API precipitate volume fraction, found by assuming complete precipitation of API above $x_{\mathrm{Ph}}^{\text {sat }}$ after the AS-uptake stage
$$
\phi_{\mathrm{p}, \infty}=\frac{x_{\mathrm{Ph}, 0}\left(1-x_{\mathrm{CO}_{2}}^{\text {sat }}\right)-x_{\mathrm{Ph}}^{\text {sat }}}{x_{\mathrm{Ph}, 0}+\left(V_{\mathrm{L}}^{\text {sat }} / V_{\mathrm{Ph}, \mathrm{s}}\right)}
\tag{18}
$$

To facilitate comparison between the constant- and variable-$\Gamma$ results, the same dimensionless units (based on variable $\Gamma$) have been used in both cases.

## 4. RESULTS: EFFECTS OF SURFACE ENERGY EVOLUTION USING THE WELL-MIXED-DROPLET MODEL

Illustrative results will be displayed as a function of $t / t_{\mathrm{AS}}$, for the typical cases: $n=2, k_{\mathrm{G}}(298 \mathrm{~K})=10^{-4}, t_{\mathrm{AS}}=0.0056 \mathrm{~ms}$, and $d_{0}=$

![](./images/813161692035809281_4.jpg)

Figure 3. Precipitated API volume fraction, $\phi_{\mathrm{p}}$ (left), and fraction of API precipitated, $\xi$ (right), vs dimensionless time. Dotted curves correspond to constant surface energy; solid curves correspond to $\Gamma$ given by eq 1. $(T=298 \mathrm{~K}, p=56$ bar, and $d_{0}=1 \mu \mathrm{m}$.)

![](./images/813161692035809281_5.jpg)

Figure 4. Predicted dimensionless particle Sauter mean diameter (SMD, left) and particle-diameter-based standard deviation $(\sigma)$ divided by the population SMD (right) vs $t$. Dotted curves correspond to constant surface energy; solid curves correspond to $\Gamma$ given by eq 1. ( $T, p$, and $d_{0}$, as in Figure 3.)

![](./images/813161692035809281_6.jpg)

Figure 5. Dimensionless precipitated particle number density distribution function (NDDF) $w f$ vs $w \equiv v / v_{\text {ref }}$ (log scale) for 10 equispaced values of time between 0 and $0.2 t_{\mathrm{AS}}$. The left plot corresponds to constant surface energy, and the right plot corresponds to $\Gamma$ given by eq 1. ( $T, p$, and $d_{0}$, as in Figure 3.) The peaks that can be seen in the NDDF for values of time close to the final time are motivated by the behavior of $v_{*}$ in that limit (see Figure 2) and are beyond the domain of applicability of our present simplified constant AS-uptake assumption, and as a consequence are not expected to be accurate.

1 $\mu \mathrm{m}$ : however, we remark that our present WMD theoretical model also leads to the identification of a potentially useful rate-based dimensionless scaling (similitude or correlation) parameter for this class of GASP processes. $^{20}$ [Note: With regard to our choice of (only) a $1 \mu \mathrm{m}$ diameter toluene solvent droplet, used for illustration purposes, there are two reasons for this. The first one is the self-consistency of our WMD mathematical model. Second, there is an incentive to move

toward smaller injector droplet sizes to minimize crystal growth effects, and, perhaps, also delay the importance of Brownian coagulation. $^{32}$]

### 4.1. Crystal Size Distribution Consequences of Surface Energy Evolution.
The main consequence of SEE, due to AS-induced reduction in the local API concentration (via eq 1) is a significant reduction (over 50%) in the nucleation- kinetics-limited amount of precipitated material. This result is illustrated in Figure 3, where the precipitated API volume fraction is shown (left), together with the relative amount of precipitated API (right), as compared to the initial inventory in the droplet. Figure 3 clearly shows that the surface energy increase resulting from the time evolution of the droplet composition produces a remarkable reduction in the total amount of precipitated (as a fraction of the maximum possible extent of precipitation) material (solid curves), as compared to the results found when $\Gamma$ is assumed to remain equal to its initial value (dotted lines).

Because of the dependence on $\Gamma$ of the critical nucleation size (see Figure 2), surface energy evolution also affects the shape of the CSD. This is shown in Figure 4 (left), where it canbe seen that SMD corresponding to constant $\Gamma$ is about $20 \%$ higher than the SMD computed retaining SEE effects. Figure 4(right) shows that the constant $\Gamma$ assumption leads to narrower CSDs, which could have also been anticipated by inspection of the time dependence of $v_{*}$ (Figure 2). The CSDs of the precipitated API are shown in Figure 5 (see Figure 5 (left) for constant $\Gamma$ and Figure 5 (right) for SEE). Because under present conditions particle growth has been found to play a minor role, the shape of $n(v, t)$ responds primarily to the time history of $v_{*}$ , which depends strongly on $\Gamma$ . As a consequence the results for $n(v, t)$ based on the constant $\Gamma$ assumption show a "plateau" at small values of $v(v / v_{ref }$ between 6 and 7 $)$ , which corresponds to the corresponding (near-)plateau of $v_{*}$ during a considerable interval of time. This plateau is absent in the results found when taking into account environment-dependent SEE. On the other hand, also because under present conditions particle growth is weak, $n(v, t)$ shows a strong peak at the values of $v$ where $v_{*}$ reaches a relative extremum (either minimum or maximum). As a consequence we may find in both cases a strong peak reached at values close to the minimum $v_{*}$ as a function of time (see Figure 5 and Figure 2). For times close to the final time we may also find a strong peak in $n$ at intermediate values of $v$ , which corresponds to the maximum reached by $v_{*}$ as a function of time when the droplet mixture becomes transcritical-at which point the numerical integration is stopped. In this regard, the very last portion of our numerically computed time-history results (for times close to the final time) serves the purpose of illustrating the correspondence between the $v_{*}$ time history and precipitate NDDF. However, it is important to remark that these results are based on our constant AS-uptake rate assumption, which is expected to become inaccurate as the droplet AS level approaches the saturation level. According to our numerical results, this condition is met toward the end of our present numerical integrations, and as a consequence the last portion of our present numerical results will not be observed in a real experiment.

### 4.2. Effects of Surface Energy Evolution on Particle Growth.
Because, in principle, the incorporation probability, $\varepsilon$ , for phenanthrene crystal growth could be as high as $1 / 2$ (see also ref 33), rather than our present $298 ~K$ expectation of onlyca. $1 ppm$ , and our previous generous assignment of $k_{G}=100$ ppm (Figure 5), we have also formally run this (upper limit) case to illustrate the consequences of SEE via the Gibbs- Kelvin-Ostwald effect on embryonic particle growth rates.[Note: In practice, size-dependent fluid phase diffusion wouldinsert itself to limit the $Ph(s)$ growth rate in such cases.]

### 4.3. Improved Quasi-Steady Methods To Anticipate/ Incorporate Surface Energy Evolution.
Hopefully, to successfully model future GASP processes it will not be necessary to introduce a much more detailed (e.g., selective, nonquasi-steady adsorption-based) computational method. However, it may very well prove necessary to go beyond thepresently employed Nielsen-Sohnel-Mersmann (NSM) correlation (eq 1), which has the remarkable property that the only relevant property of the multicomponent "solvent" is its ability to alter the saturation number density of the solute.

An interesting possible alternative will be the Girifalco- Good relationship, $^{17}$ which relates the free energy $\gamma_{\alpha \beta}$ of a unit area of the $\alpha \beta$ interface to the individual liquid adjacent phase energies $\gamma_{\alpha}$ and $\gamma_{\beta}$ , allowing for phases $\alpha$ and $\beta$ to have unequal molar volumes. In the present case $\gamma_{\alpha}$ would presumably be the surface free energy of phenanthrene solid and $\gamma_{\beta}$ the surfacetension of the prevailing ternary host fluid, i.e., here $T+Ph+$  CO2-perhaps estimated via the constituent pure saturated fluid surface tensions (at the prevailing temperature $T$ and molar composition $x_{i}$ ) via a semiempirical "parachor-based" mixing rule. While under investigation, this route to estimating SEE is understandably quite sensitive to the choice of individual surface energies-which must also be fully self-consistent. With these sensitivities in mind, the simpler, yet remarkably successful, NSM correlation was considered to be adequate for our present purposes.

Of course, in retrospect, "solvent effects" on crystal morphology (via relative [crystal face] growth rates in supersaturated liquid solvents) are quite familiar, $^{34}$ so the importance of evolving surface energy we find for GASP- process modeling is not without precedents. Ultimately, surface energy anisotropy could be introduced, opening the door touseful predictions of precipitated crystal shape. $^{35}$

## 5. CONCLUSION AND RECOMMENDATIONS
### 5.1. "Particle Design" Implications of Surface Energy Evolution for GASP Modeling.
While each of our present property estimation methods (sections 2 and 3) may require refinement in the light of new GASP-performance data, it seems clear from the well-mixed-droplet idealized examples selected above that useful predictions of API yield, mean particle size, and API powder population spread will have to be made by allowing for an environment-dependent effective surface energy. This API solid/local fluid "surface energy evolution" (SEE) dramatically alters the instantaneous particle nucleation rates and also reduces the growth rates of newly born API particles in the prevailing supersaturated solutions. Apparently, with the notable exception (for nucleation) of ref16, neither of these systematic effects has been accounted for in earlier GASP modeling studies, calling into question the use of "constant- $\gamma$ " models to infer meaningful physicochemical parameters (such as $\gamma, k_{G}$ , and $n$ ) from laboratory scale GASP experiments, and probably also compromising theirability to predict the performance of scaled-up GASP systems. $^{36}$  Experiments needed to more directly test our present isobaric, small solvent droplet predictions are not readily available, but the lessons learned here should facilitate presently needed extensions (section 5.2).

### 5.2. Necessary Extensions and Work in Progress.
Unless internal circulation and/or liquid-phase turbulence "come to the rescue", the well-mixed-droplet-based GASP- process model exploited here is probably not realistic for the $(\gg 10\ \mu\text{m})$ solvent droplet sizes that were actually used in the earliest laboratory-scale experiments—i.e., the characteristic intradroplet antisolvent-diffusion time: $d_0^2/(4D_{\text{AS-mix}})$ is not much smaller than the AS-uptake time, $t_{\text{AS}}$, above (see, also, Chavez et al.³⁷). However, this convenient WMD theoretical platform has been shown here to provide access to rate-limited precipitate yields, unusual precipitate particle size distributions (including SMD and spread information), and sensitivity to important modeling approximations (e.g., surface energy evolution, $\dot{G}$ law, ...). In our more recent studies (ref 20), we have exercised this mathematical model to include predicted sensitivity to initial solvent droplet size, $d_0$ (and DSD), and also propose scaling (similitude) parameter(s). We view these as useful steps toward a much-needed, more comprehensive rate- based GASP-process model—a "holy grail" which has now proven to be elusive for well over 1 decade (see refs 2, 7, 36, and 37.). Such a model should not only account for intradroplet concentration nonuniformities and surface energy evolution but also ultimately include surface energy aniso- tropy—opening the possibility of also predicting precipitate particle morphology.

### AUTHOR INFORMATION
#### Corresponding Author
*E-mail: daniel.rosner@yale.edu

#### Notes
The authors declare no competing financial interest.
†D.E.R. is the L. W. Jones Professor of Chemical Engineering, Director of the Yale Sol Reaction Engineering Group.
‡M.A.-Z. is a visiting Associate Professor. Permanent address: Departamento Física Matemática y de Fluidos, UNED, Apdo 60141, 28080 Madrid, Spain.

### ACKNOWLEDGMENTS
This work was supported by Industrial Affiliates of the Sol Reaction Engineering Research Group at Yale, Yale ChE graduate alumni, and the Yale School of Engineering and Applied Science. Much of the text was prepared while the senior author (D.E.R.) enjoyed the hospitality of Stanford University/HTGL during his Fall 2012 academic leave. M.A.-Z. also acknowledges the support of Ministerio de Ciencia e Innovación (Grant Nos. CSD2010-00011 and ENE2011- 26868) and Comunidad de Madrid (Grant No. S2009/ENE- 1597) at UNED (Madrid).

### NOMENCLATURE
|  |  |
|--|--|
| $\dot{B}'''$ | birth rate of particles per unit volume and time |
| $d$ | diameter (of particle or droplet) |
| $D$ | Fick molecular diffusion coefficient |
| $F(\text{GK})$ | correction factor due to interface curvature |
| $\dot{G}$ | linear growth rate of particle or crystal |
| $k_{\text{B}}$ | Boltzmann constant |
| $k_{\text{G}}(T,...)$ | dimensionless growth rate constant |
| $k_{ij}$ | binary interaction parameter for mixture $a$ in Peng–Robinson EOS |
| $l_{ij}$ | binary interaction parameter for mixture b in Peng–Robinson EOS |
| $m_i$ | molecular mass of component $i$ |
| $M_i$ | molar mass of component $i$ (e.g., kg/kmol) |
| $n$ | kinetic "order" parameter in $\dot{G}(S)$ expression |
| $n$ | total number (or molar) density of mixture |
| $n(v,t)$ | particle number density distribution function |
| $N_{\text{A}}$ | Avogadro's number $(0.6023 \times 10^{27}$ molecules/(kg-mol)) |
| $n_i$ | number density of component $i$ (molar or molecular) |
| $N_i$ | number of moles of component $i$ |
| $\dot{N}_i$ | molar flow rate of component $i$ |
| $N_{\text{p}}'''$ | particle number density |
| $p$ | pressure (bar) |
| $R$ | universal gas constant |
| $S$ | supersaturation |
| $t$ | time (reckoned from the onset of AS addition) |
| $t_{\text{AS}}$ | characteristic time associated with antisolvent $(\text{CO}_2)$ addition rate |
| $T$ | absolute temperature (K) |
| $T_{\text{c}}$ | critical temperature |
| $v$ | volume of an individual precipitate particle |
| $V$ | molar volume of mixture |
| $V_{\text{c}}$ | critical molar volume |
| $V_i$ | molar volume of component $i$ |
| $v_{\text{m}}$ | molecular volume (for API in solid state) |
| $V$ | total volume of droplet (containing $S + \text{API} + \text{AS}$) |
| $\mathbf{x}$ | composition vector $\{x_1,x_2,x_3\}^T$ |
| $x_i$ | mole fraction of component $i$ (liquid phase) |
| $y_i$ | mole fraction of component $i$ (vapor phase) |
| $Z$ | compression factor $(Z \equiv pV/(RT))$ |
| $Z_{\text{c},i}$ | critical value of compression factor for component $i$ |
| $\dot{Z}_i''$ | molar (or molecular) impingement flux of component $i$ |

#### Greek Letters
|  |  |
|--|--|
| $\alpha$ | pertaining to phase $\alpha$ |
| $\alpha\beta$ | pertaining to interfacial phase $\alpha\beta$ |
| $\beta$ | pertaining to phase $\beta$ |
| $\gamma$ | prevailing surface free energy (environment-dependent) |
| $\Gamma$ | dimensionless surface energy $(\gamma v_{\text{m}}^{2/3}/(k_{\text{B}}T))$ |
| $\varepsilon$ | incorporation probability for growth species (API) |
| $\xi$ | fraction of API precipitated (compared to VSE maximum) |
| $\phi_p$ | API precipitate volume fraction (first volume moment of $n(v, t)$) |
| $\omega$ | component acentric factor |

#### Subscripts and Superscripts
|  |  |
|--|--|
| $*$ | pertaining to CNT critical size |
| $0$ | initial value (subscript) |
| $\infty$ | final value |
| $\text{AS}$ | antisolvent (here $\text{CO}_2$) |
| $\text{API}$ | active pharmaceutical ingredient (here $\text{Ph}$ (surrogate)) |
| $\text{G}$ | growth |
| $i,j$ | components $i,j$ |
| $\text{L}$ | liquid phase |
| $\text{N}$ | nucleation |
| $\text{Ph}$ | phenanthrene (API surrogate) |
| $\text{ref}$ | reference value |
| $\text{s}$ | solid phase |
| $\text{S}$ | solvent (here toluene) |
| $\text{T}$ | toluene $(\text{C}_7\text{H}_8)$ |

#### Acronyms/Abbreviations
|  |  |
|--|--|
| $\text{API}$ | active pharmaceutical ingredient (or $\text{Ph}$ surrogate) |
| $\text{AS}$ | antisolvent (here $\text{CO}_2$) |
| $\text{ASP}$ | antisolvent precipitation |

BDP beclonemethasone-17,21-diproportionate (anti-inflammatory)
CNT classical nucleation theory
CSD crystal size distribution (function)
EOS equation of state
G growth
GASP gas(-induced) antisolvent precipitation
GKO Gibbs-Kelvin-Ostwald
IGKT ideal gas kinetic theory
MOC method of characteristics
N nucleation
NDDF number density distribution function
N/G nucleation/growth
NSM Nielsen-Sohnel-Mersmann (eq 1)
ODE ordinary differential equation
PDE partial differential equation
Ph phenanthrene ($\mathrm{C_{14}H_{10}}$; surrogate API)
PR Peng-Robinson (EOS)
PSD particle size distribution (function)
RESS rapid expansion of a supercritical solution
S solvent (for API or API surrogate)
SASP supercritical (vapor) antisolvent precipitation
SEE surface energy evolution (see eq 1)
SMD Sauter mean diameter
T toluene ($\mathrm{C_7H_8}$) solvent for API or API surrogate
VLSE vapor-liquid-solid equilibrium
WMD well-mixed droplet$^{20,37}$

### REFERENCES

(1) Chang, C. J.; Randolph, A. D. Precipitation of microsize organic particles from supercritical fluids. AIChE J. 1989, 35, 1876−1882.

(2) Fages, J.; Lochard, H.; Letourneau, J.-J.; Sauceau, M.; Rodier, E. Particle generation for pharmaceutical application using supercritical fluid technology. Powder Technol. 2004, 141, 219−226.

(3) Gallagher, P. M.; Coffey, M. P.; Krukonis, V. J.; Klasutis, N. Gas anti-solvent recrystallization: New process to recrystallize compounds insoluble in supercritical fluids. In Supercritical Fluid Science and Technology, American Chemical Society, 1989; Chapter 22, pp. 334−356.

(4) Chang, S.-C.; Lee, M.-J.; Lin, H.-M. Role of phase behavior in micronization of lysozyme via a supercritical anti-solvent process. Chem. Eng. J. 2008, 139, 416−425.

(5) Kikic, I.; Sist, P. Applications of supercritical fluids to pharmaceuticals: Controlled drug release systems. In Supercritical Fluids: Fundamentals and Applications; Kiran, E., Debenedetti, P. G., Peters, C. J., Eds.; NATO Science Series; Kluwer: Dordrecht, The Netherlands, 2000; Vol. E366, pp 291−306.

(6) Jung, J.; Perrut, M. Particle design using supercritical fluids: Literature and patent survey. J. Supercrit. Fluids 2001, 20, 179−219.

(7) Martin, A.; Cocero, M. J. Micronization Processes with Supercritical Fluids: Fundamentals and Mechanisms. Adv. Drug Delivery Rev. 2008, 60, 339−350.

(8) Werling, J.; Debenedetti, P. G. Numerical modeling of mass transfer in the supercritical anti-solvent process. J. Supercrit. Fluids 1999, 16, 167−181.

(9) Elvassore, N.; Cozzi, F.; Bertucco, A. Mass Transport Modeling in a Gas Antisolvent Process. Ind. Eng. Chem. Res. 2004, 43, 4935−4943.

(10) Muhrer, G.; Lin, C.; Mazzotti, M. Modeling the Gas Antisolvent Recrystallization Process. Ind. Eng. Chem. Res. 2002, 41, 3566−3579.

(11) Bakhbakhi, Y.; Rohani, S.; Charpentier, P. A. Micronization of Phenanthrene Using the Gas Antisolvent Process: Part 2. Theoretical Study. Ind. Eng. Chem. Res. 2005, 44, 7345−7351.

(12) This paper is based, in part, on the following: 12th European Aerosol Conference, Paper No. WG10S1O, Granada, Spain, Sep. 6, 2012. A more recent account of this work was presented at the following: Fundamentals Session, 13th European Aerosol Conference, Prague, Czech Republic, Sep. 1, 2013; AIChE Annual Meeting, Paper/Poster No. 394c, San Francisco, CA, USA, Nov. 5, 2013.

(13) Debenedetti, P. G. Homogeneous nucleation in supercritical fluids. AIChE J. 1990, 36, 1289−1298.

(14) Kwauk, X.; Debenedetti, P. G. Mathematical modeling of aerosol formation by rapid expansion of supercritical solutions in a converging nozzle. J. Aerosol Sci. 1993, 24, 445−469.

(15) Turk, M. Influence of thermodynamic behaviour and solute properties on homogeneous nucleation in supercritical solutions. J. Supercrit. Fluids 2000, 18, 169−184.

(16) Dodds, S.; Wood, J. A.; Charpentier, P. A. Modeling of the Gas-Antisolvent (GAS) Process for Crystallization of Beclomethasone Dipropionate using Carbon Dioxide. Ind. Eng. Chem. Res. 2007, 46, 8009−8017.

(17) Girifalco, L. A.; Good, R. J. A Theory for the Estimation of Surface and Interfacial Energies. 1. Derivation and Application to Interfacial Tension. J. Phys. Chem. 1957, 61, 904−909.

(18) Nielsen, A. E.; Sohnel, O. Interfacial Tensions Electrolyte Crystal-Aqueous Solution, from Nucleation Data. J. Cryst. Growth 1971, 11, 233−242.

(19) Mersmann, A. Calculation of Interfacial-Tensions. J. Cryst. Growth 1990, 102, 841−847.

(20) A more comprehensive account of this mathematical model of the isobaric GASP process and its consequences is: Rosner, D. E.; Arias-Zugasti, M. Theory of Pharmaceutical Powder "Micronization" Using Compressed Gas Anti-solvent (Re-)precipitation. J. Supercrit. Fluids 2014, submitted for publication. In this connection, an overview of our reformulation of crystal growth laws for application to transcritical environments was presented: AIChE Annual Meeting, Paper No. 300f, San Francisco, CA, USA, Nov. 5, 2013, submitted for publication in Cryst. Growth Des.

(21) Weber, M.; Russell, L. M.; Debenedetti, P. G. Mathematical modeling of nucleation and growth of particles formed by the rapid expansion of a supercritical solution under subsonic conditions. J. Supercrit. Fluids 2002, 23, 65−80.

(22) Kashchiev, D. Nucleation: Basic Theory with Applications; Butterworth-Heinemann: Boston MA, USA, 2000.

(23) Jarmer, D. J.; Lengsfeld, C. S.; Randolph, T. W. Nucleation and growth rates of poly(l-lactic acid) microparticles during precipitation with a compressed-fluid antisolvent. Langmuir 2004, 20, 7254−7264.

(24) Mahajan, A. J.; Kirwan, D. J. Nucleation and growth-kinetics of biochemicals measured at high supersaturations. J. Cryst. Growth 1994, 144, 281−290.

(25) Rosner, D. E. Transport Processes in Chemically Reacting Flow Systems; DOVER: Mineola, NY, USA, 2000.

(26) de la Fuente Badilla, J.; Peters, C. J.; de Swaan Arons, J. Volume Expansion in Relation to the Gas-Antisolvent Process. J. Supercrit. Fluids 2000, 17, 13−23.

(27) Dixon, D. J.; Johnston, K. P. Molecular Thermodynamics of Solubilities in Gas Antisolvent Crystallization. AIChE J. 1991, 37, 1441−1449.

(28) Reverchon, E.; Caputo, G.; De Marco, I. Role of phase behavior and atomization in the supercritical anti-solvent precipitation. Ind. Eng. Chem. Res. 2003, 42, 6406−6414.

(29) Rosner, D. E.; McGraw, R.; Tandon, P. Multivariate population balances via moment and Monte Carlo simulation methods: An important sol reaction engineering bivariate example and "mixed" moments for the estimation of deposition, scavenging, and optical properties for populations of nonspherical suspended particles. Ind. Eng. Chem. Res. 2003, 42, 2699−2711.

(30) Rosner, D. E.; Arias-Zugasti, M. Bi-variate Population Balance Model of Ethanol-Fueled Spray Combustors. AIChE J. 2011, 57, 3534−3554.

(31) Hulburt, H. M.; Katz, S. Some Problems in Particle Technology. A Statistical Mechanical Formulation. Chem. Eng. Sci. 1964, 19, 555−574.

(32) Rosner, D. E.; Arias-Zugasti, M. Coupling between homoge- neous rate processes and fluid deformation rate: Brownian particle coagulation in a rapidly dilating solvent. AIChE J. 2011, 57, 307−318.

(33) Cammenga, H. K.; Petrick, H. J.; Schulze, F. W. Sublimation Kinetics of Organic Molecular-Crystals. J. Cryst. Growth 1981, 55, 351−362.

(34) Mullin, J. W. Crystal Growth. Crystallization, 4th ed.; Elsevier/ Butterworth-Heinemann: Oxford, U.K., 2001; Chapter 6, pp 224−296.

(35) Snyder, R. C.; Doherty, M. F. Predicting crystal growth by spiral motion. Proc. R. Soc., A 2009, 465, 1145−1171.

(36) Thiering, R.; Dehghani, F.; Foster, N. R. Current issues relating to anti-solvent micronisation techniques and their extension to industrial scales. J. Supercrit. Fluids 2001, 21, 159−177.

(37) Chavez, F.; Dibenedetti, P. G.; Luo, J. J.; Dave, R. N.; Pfeffer, R. Estimation of the characteristic time scales in the supercritical anti- solvent process. Ind. Eng. Chem. Res. 2003, 42, 3156−3162.