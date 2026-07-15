ARTICLE
Received 9 Dec 2015 | Accepted 27 May 2016 | Published 30 Jun 2016
DOI: 10.1038/ncomms12067
OPEN

# Impeding $^{99}$Tc(IV) mobility in novel waste forms

Mal-Soon Lee$^{1}$, Wooyong Um$^{2,3}$, Guohui Wang$^{2}$, Albert A. Kruger$^{4}$, Wayne W. Lukens$^{5}$, Roger Rousseau$^{1}$
& Vassiliki-Alexandra Glezakou$^{1}$

Technetium ($^{99}$Tc) is an abundant, long-lived radioactive fission product whose mobility in the subsurface is largely governed by its oxidation state. Tc immobilization is crucial for radioactive waste management and environmental remediation. Tc(IV) incorporation in spinels has been proposed as a novel method to increase Tc retention in glass waste forms during vitrification. However, experiments under high-temperature and oxic conditions show reoxidation of Tc(IV) to volatile pertechnetate, Tc(VII). Here we examine this problem with *ab initio* molecular dynamics simulations and propose that, at elevated temperatures, doping with first row transition metal can significantly enhance Tc retention in magnetite in the order Co > Zn > Ni. Experiments with doped spinels at 700 °C provide quantitative confirmation of the theoretical predictions in the same order. This work highlights the power of modern, state-of-the-art simulations to provide essential insights and generate theory-inspired design criteria of complex materials at elevated temperatures.

$^{1}$Fundamental and Computational Sciences Directorate, Pacific Northwest National Laboratory, Richland, Washington 99352, USA. $^{2}$Energy and Environment Directorate, Pacific Northwest National Laboratory, Richland, Washington 99352, USA. $^{3}$Pohang University of Science and Technology, Pohang 37673, South Korea. $^{4}$United States Department of Energy, Office of River Protection, Richland, Washington 99352, USA. $^{5}$Lawrence Berkeley National Laboratory, Berkeley, California 94720, USA. Correspondence and requests for materials should be addressed to W.U. (email: Wooyong.Um@pnnl.gov) or to V.-A.G. (email: Vanda.Glezakou@pnnl.gov).

NATURE COMMUNICATIONS | 7:12067 | DOI: 10.1038/ncomms12067 | www.nature.com/naturecommunications

**ARTICLE**

T echnetium $(^{99}\text{Tc})$ is an abundant long-lived radioactive fission product present in used nuclear fuel and waste generated from nuclear fuel reprocessing. Owing to its long half-life $(2.1 \times 10^5$ years) and relatively high fission yield ($\sim 6\%$), $^{99}\text{Tc}$ can generate the greatest radiation dose in the vicinity of a waste repository, and for a much longer time compared with other fission products, such as $^{90}\text{Sr}$ and $^{137}\text{Cs}$ (with half-life $\sim 30$ years)$^{1,2}$. In addition, $\text{TcO}_4^-$ is highly soluble and weakly adsorbed in the near-field, while Tc(IV) is highly adsorbable to geological materials and clays$^3$. Thus, migration of Tc from a waste repository may be prevented by immobilizing Tc(IV) in durable waste forms, such as glass or ceramic materials$^{4-6}$. Although Tc(VII)$\text{O}_4^-$ is the most stable Tc species under aerobic conditions, it is highly volatile at glass vitrification temperatures ($\sim 1,200^\circ\text{C}$), leading to poor Tc retention in the final waste glass$^{4-7}$. Retention of Tc in the glass is generally improved by reducing conditions since Tc(IV) is less volatile$^{6,8,9}$. Tc(VII) may be effectively reduced to Tc(IV) by Fe(II) in oxide and sulfide minerals or by Fe(II) adsorbed to mineral surfaces such as iron oxides or aluminium oxides$^{9-17}$. However, retention of Tc is still limited because of re-oxidation of Tc(IV) back to Tc(VII) (refs 18–21). Consequently, simply reducing Tc(VII) to Tc(IV) before vitrification is unlikely to stabilize Tc and prevent its volatilization as Tc(VII). An alternative approach would be to trap Tc(IV) in the lattice of a metal oxide by co-precipitation. Spinels are attractive targets for Tc stabilization during vitrification because of their physical and chemical stability under the high temperatures used in preparing borosilicate glasses$^{4,6}$. In this respect, efficient incorporation and high retention of Tc by glass-incorporated spinels is very important for radioactive waste management and offers substantial economic benefit because of reduction in the amount of glass needed to immobilize $^{99}\text{Tc}$.

Magnetite $(\text{Fe}_3\text{O}_4)$ has a cubic inverse spinel structure, where the oxygen anions form a slightly distorted face-centred-cubic sublattice and the iron cations occupy tetrahedral and octahedral interstitial sites. In the [001] direction, two types of layer stacking occur: $A$ layers with tetrahedral Fe(III) and $B$ layers with O and octahedral Fe(II)/Fe(III) (see Fig. 1). Marshall et al.$^8$ showed that Tc(VII) can be reduced to Tc(IV) and incorporated into the magnetite structure under high pH conditions (pH 10.5 – 13.1). They also observed that Tc(IV) incorporation occurred at the octahedral sites and remobilization of Tc(IV) was limited during subsequent air oxidation. Kobayashi et al. observed Tc(IV) incorporation into the magnetite structure at pH 6 and pH 7.5 (ref. 22). However, magnetite oxidizes to maghemite $(\gamma-\text{Fe}_2\text{O}_3)$ in oxic conditions or under high temperature through maghemitization, where all the Fe(II) atoms oxidize to Fe(III), while the oxygen sublattice remains unchanged$^{23}$. When maghematization takes place, iron atoms diffuse towards the surface, leaving octahedral cation vacancies$^{23,24}$. As a result, maghematization could lead to re-oxidation of Tc(IV) because of the increase in Fe(III), a highly efficient oxidizing agent$^8$. Sidhu et al.$^{23}$ suggested that incorporation of trace elements into magnetite stabilizes Fe(II) and suppresses maghematization by decreasing electron mobility. The majority of experimental studies on Tc retention are conducted at low temperatures, while theoretical studies employ static structural models that neglect temperature effects. Under these conditions, these studies cannot address Tc volatilization during vitrification that leads to poor Tc retention in the glass waste form. Thus, elucidation of high-temperature effects is important for understanding Tc retention by magnetite at elevated temperatures. *Ab initio* molecular dynamics (AIMD) simulations can describe the temperature effects on the change in structure, bonding and associated change in the oxidation states of Tc and Fe, which ultimately affects Tc retention. Here our simulations indeed show that leaching of Tc is accompanied with re-oxidation of Tc(IV) to Tc(VII) at high temperatures, but it can be suppressed by doping. We propose that inclusion of first transition metal dopants (Co, Zn and Ni) significantly improves Tc retention in magnetite at high temperature. Quantitative confirmation is further provided by X-ray absorption near edge structure (XANES) measurements and gravimetric analysis.

## Results
Temperature effects on Tc(IV)-incorporated spinel. The $\text{Fe}_3\text{O}_4(001)$ surface has been studied extensively$^{25-30}$. Pentcheva et al.$^{28}$ compiled a phase diagram for the $\text{Fe}_3\text{O}_4(001)$ surface in an *ab initio* thermodynamics study showing that the most stable surface structure is a $B$-terminated surface with octahedral iron and oxygen atoms forming a wave-like structure along the (001) direction. On the basis of these results, we generated a $\text{Fe}_3\text{O}_4(001)$ model of a $B$-terminated surface (Fig. 1) that we let fully relax. Below the Verwey transition (125 K), the surface possesses a permanent dipole that has been shown to drive the formation of surface defects in these types of material$^{25}$. However, above this temperature, magnetite is metallic, and the surface dipole is quenched$^{31}$ and is not likely to affect surface charge defects. Details on the computational models and methods can be found in the Methods section.

To assess the temperature effects on Tc retention in magnetite, we replaced one octahedral Fe on the surface with Tc and performed AIMD simulations at two different temperatures, 25 and $600^\circ\text{C}$, representing the ambient and the lower-end temperature range of the vitrification process, respectively. Figure 2a shows the calculated atomic density profiles of the different species with Tc scaled by 5 for clarity. The dotted grey line denotes the edge of the magnetite surface defined by the average position of the topmost oxygen atoms. At $25^\circ\text{C}$, Tc stays within the top surface layer for the duration of the simulation ($\sim 20$ ps). Computation of pair distribution functions, $g(\text{R})$, reveals that, on average, surface-incorporated Tc has five nearest O neighbours with an average Tc–O distance $1.98\ \text{Å}$ (Fig. 2b upper panel, Supplementary Fig. 1 and Supplementary Table 1). Additional exploratory simulations with Tc in an inner lattice position show a $g(\text{R})$ maximum at $2.01\ \text{Å}$ for the Tc–O distance, compatible with the reduced Tc(IV) in magnetite (Supplementary Table 2). According to X-ray absorption fine structure (XAFS) analysis, the Tc(IV)–O distance is $\sim 2.0\ \text{Å}$ (see Supplementary Table 2 and (refs 22, 32) for addi-

![](./images/811259199311839233_1.jpg)

Figure 1 | The $B$-truncated (octahedral) $\text{Fe}_3\text{O}_4(001)$ structure. (a) Top view and (b) side view of surface structure. Red and cyan circles represent oxygen and iron, respectively. A (blue circle) can be either Fe or Tc and B (yellow circle) can be either Fe or an impurity atom (Ni/Zn/Co).

![](./images/811259199311839233_2.jpg)

Figure 2 | Structural properties and XANES spectra in the presence of Tc.
(a) Atomic-density profile showing atomic arrangement along the z-
direction at 25 and 600 °C obtained from AIMD simulations, where dotted
vertical line denotes the magnetite surface. (b) Pair distribution function
g(R) obtained from AIMD simulation trajectories at 25 and 600 °C.
(c) Snapshot of the structure at 600 °C from AIMD trajectories where a
blue circle represents Tc, red for O and cyan for Fe. The dotted vertical line
denotes the magnetite surface. (d) Normalized XANES spectra at 25 and
600 °C.

tional structural parameters). These observations imply that
(i) within the surface layer the oxidation state of Tc is essentially
Tc(IV) and (ii) at 25 °C (the glass-feed stage) reduced Tc(IV) is
the prevalent oxidation state. However, the completely opposite
picture emerges at high temperatures, 600 °C or higher. Tc
moves above the surface, dragging coordinating surface oxygens
along with it (see Supplementary Movie 1). The local Tc
geometry is consistent with a tetrahedral Tc(VII)O₄⁻ species,
with two or three of the coordinating oxygens dynamically
connected to Fe atoms on the surface (Fig. 2c). Analysis of g(R)
for Tc-O pairs shows a peak at 1.79 Å (Fig. 2b, lower panel),
an almost 10% reduction compared with the Tc(IV)-O distance
at 25 °C. This change is compatible with the shorter Tc(VII) – O
distances of ~1.75 Å as determined by XAFS (Supplementary
Table 2 and refs 22, 33). From this observation, we infer, that
beginning at 600 °C, Tc oxidation is in process, commensurate
with the tetrahedrally coordinated Tc transitioning to TcO₄⁻. In
addition to the system with Tc at the surface, we also examined a
system with Tc at an inner lattice site at 600 °C. The calculated
g(R) gives the distance between Tc and O as 2.01 Å, consistent
with the reduced Tc(IV) in magnetite. As shown in
Supplementary Fig. 2, Tc remains in the same layer throughout
the simulation timescale. When comparing the energetics of the
configurations with Tc below or at the surface layer, the energy
with Tc below the surface is 2.5 eV higher than when Tc is at the
surface. This implies that there is a thermodynamic driving
force that will eventually move Tc out to the surface.

Experimentally, Tc-magnetite samples, heated from room
temperature to 600 °C and then cooled back to room tempera-
ture, were analysed to determine the Tc oxidation state using
XANES as shown in Fig. 2d. In the figure, the grey diamonds and
black line indicate the measured data and a linear combination fit,
respectively, for Tc-magnetite samples, while the red and blue
lines represent the contribution from Tc(IV) and Tc(VII),
respectively. At 25 °C, the spectrum of the sample shows only
Tc(IV) (feed, red) but no Tc(VII) (blue), indicating that all Tc in
the sample is in its reduced form. In the sample heated to 600 °C,
however, the spectrum shows a mixture of both Tc(IV)
and Tc(VII). All these observations are compatible with the
simulations.

![](./images/811259199311839233_3.jpg)

Figure 3 | Atomic density and normalized XANES spectra with Co
dopant. (a) Atomic density profiles with and without Co dopant at 600 °C.
Red lines represent Tc, blue line for doped atom, grey lines for Fe and green
lines for O. (b) Normalized XANES spectra for the Co-doped magnetite at
25 °C as made and treated at 700 °C. Colour codes used are the same as
those shown in Fig. 2.

Effects of dopants on Tc retention. To simulate the effect of
dopants on the Tc redox chemistry and immobilization, we
modified the magnetite by substituting one surface Fe atom with
Ni, Zn or Co (~1% wt each) at a site close to Tc. This choice was
motivated by earlier experiments by Sidhu et al.²³, who observed
stabilization of Fe(II) and suppression of maghematization when
first row transition metal dopants were present in magnetite even
at concentrations ~1 wt %. The atomic density profiles along the
surface normal from AIMD at 600 °C in the presence of the
doping elements are shown in Fig. 3 (Co) and Supplementary
Fig. 3 (Ni and Zn), exhibiting an increase in Tc retention in the
order Co>Zn>Ni.

In the case of Ni, the Tc population is bi-modal where Tc
remains mostly on top of the surface with only a small
population within the top surface layer. In the case of Zn, the
bi-modal Tc distribution is shifted towards a larger Tc
population within the surface. Analysis of trajectories also
shows that the distance between Tc and the coordinating O
fluctuates between 1.71 and 1.92 Å, compatible with an
equilibrium between Tc(VII) and Tc(IV) oxidation states
(see Supplementary Fig. 4). This behaviour implies that Ni
and Zn only partially, and to a similar degree, hinder Tc
oxidation. Finally, in the presence of Co, Tc remains almost in
its entirety within the surface at all times indicative of a Tc(IV)
state. We examined Tc(IV) stabilization in the presence of
Co by conducting a simulation starting with TcO₄⁻ on top of the
surface. As shown in Supplementary Movie 2, Tc(VII) rapidly
migrates into the surface becoming Tc(IV), within 1.5 ps of
simulation time.

To validate these findings, we prepared three different
magnetite samples doped with ~10% wt of Ni, Zn and Co.
Details on the preparation of samples can be found in the
Methods section. The samples were heated at 700 °C in a furnace

for 1 h, and the remaining Tc was measured (see Supplementary Table 3). Gravimetric measurement showed that doping with Co resulted in the highest Tc retention (29% wt) compared with less than half that amount for Zn (12% wt) and ~1/8 of that for Ni (4% wt). No detectable amount of Tc was found in the Tc-magnetite sample prepared without dopant and treated at 700 °C. We also performed XANES measurements for the samples prepared at 25 and 700 °C (see Supplementary Methods for details) and confirmed our theoretical prediction of the highest Tc retention with Co dopant at high temperature, as shown in Supplementary Table 4 and Fig. 3b and Supplementary Fig. 5.

Equilibrium constants and free energy estimates. To best connect with the experimental observations, we determined the ratio of the equilibrium populations between the two different oxidation states of Tc(IV) ([Tcᵢₙ]) and Tc(VII) ([Tcₒᵤₜ]). This can be achieved by integrating the area under the atomic density profiles for Tc in Fig. 3. An equilibrium constant between the two populations, determined as the ratio $K_{\text{eq}} = [\text{Tc}_{\text{in}}]/[\text{Tc}_{\text{out}}]$, was used to calculate the Gibbs free energy for this equilibrium from the relation $\Delta G = -RT\ln K_{\text{eq}}$, where $R$ is the gas constant and $T$ is the absolute temperature. Negative values indicate that the equilibrium favours a higher population of Tc(IV). Table 1 summarizes the computed values of $K_{\text{eq}}$ and $\Delta G$, as well as the measured Tc retention for the different doping agents Ni, Zn and Co. These results show a remarkable agreement between the theoretical prediction and experimental validations, not only in terms of relative order but also in magnitude. The underlying reason is based on the increase in the reducing capacity of the Tc-containing spinels upon doping. This can be quantified by the difference in energy between the Fermi level, $E_{\text{F}}$, and the highest occupied molecular orbital (HOMO) of Tc $d$ states, $\Delta E_{\text{gap}}$, see last column in Table 1. The calculated total and projected density of states (DOS) of the $d$-band for Tc and dopant are shown in Supplementary Fig. 6. Whereas in the case of Ni only a marginal stabilization of the Tc $d$-states occurs (small $\Delta E_{\text{gap}}$), in the case of Zn and Co, a much higher stabilization takes place that ultimately hinders Tc re-oxidation.

Discussion
In conclusion, we propose that standard reduction potentials of transition metal ions relative to those of parent spinel, combined with their available oxidation states, can be a useful diagnostic tool for identifying appropriate additives. The reduction potential for magnetite ranges from +0.22 to +0.66 V (ref. 34), while those for $\text{Co}^{2+}$, $\text{Ni}^{2+}$ and $\text{Zn}^{2+}$ are $-$0.28, $-$0.26 and $-0.76\ \text{V}$, respectively³⁵, and in principle $\text{Co}^{2+}$ and $\text{Ni}^{2+}$ should have similar and limited effect upon Tc retention, while $\text{Zn}^{2+}$ should have a more pronounced influence. However, $\text{Co}^{2+}$ with a wide range of redox values towards $\text{Co}^{3+}$ (refs. 35, 36), it greatly increases the overall reducing capacity of the spinel material. This is reflected in the increased stabilization of the Tc $d$-states, see Table 1. Both simulations and experiment show that cobalt is by far the most effective additive for Tc retention compared with the undoped magnetite. We postulate that Tc retention, during the glass vitrification, can be controlled by balancing the redox capacity of oxide materials and doping agents. The current study underscores the impact of complex models incorporating both electronic structure and temperature effects that reveal the critical variables needed for predictive materials' design.

Methods
Density functional theory (DFT) parameters. Spin-polarized DFT simulations were performed with periodic boundary conditions (3D PBC) as implemented in the CP2K package³⁷. The Perdew, Burke and Ernzerhof (PBE) generalized gradient approximation was used for the exchange-correlation functional³⁸. The core electrons were described by the norm-conserving pseudopotentials³⁹, while the valence wave functions were expanded in terms of double-zeta quality basis sets optimized for condensed systems to minimize linear dependencies and superposition errors⁴⁰. An additional auxiliary plane wave basis set with a 500-Ry cutoff was used to calculate the electrostatic terms. The GGA + U scheme was used to provide more accurate electronic structure for the localized $d$-orbitals. The Hubbard parameter (U-J) of 3.5 eV was taken for the Fe $3d$ states, which results in a work function of 5.32 eV, in good agreement with that obtained by Pentcheva et al.²⁸ Owing to large supercell simulations, the $\Gamma$-point approximation was used for the Brillouin zone integration.

Computational models. To study Tc incorporation in magnetite with and without dopants, we used a $2\times2\times2$ supercell in all simulations to minimize periodic images. Optimization of the bulk structure of magnetite had a cell parameter of 8.391 Å, which agrees well with experimental data (8.390 Å (ref. 41)). Using this optimized cell parameter, we constructed a magnetite(001) surface model terminated at an octahedral Fe sublattice, since it is known to be the most stable surface structure in magnetite. A more recent surface model was also considered⁴², but was found not to have significant impact on the present problem, see SI. Our model system consisted of a symmetric slab with seven octahedral and six tetrahedral Fe sublattices (384 atoms) with a vacuum region of 12.5 Å between slabs. To study Tc incorporation, one surface octahedral Fe was replaced with Tc, followed by structural optimization. We also optimized a structure with one octahedral Fe in the third layer replaced by Tc. For the doping studies, we substituted a surface Fe atom with Co, Ni or Zn (~1 wt%) at a lattice position close to Tc. In all simulations, we fixed the atomic positions of the four bottom atomic layers.

AIMD simulations. AIMD simulations were performed with and without Tc at 25 °C and with the dopants Co/Ni/Zn at 600 °C, with the Nosé–Hoover thermostat for NVT ensemble and a time step of 1.0 fs. Each simulation was equilibrated for at least 20–28 ps, and the last 10–12 ps of the trajectories was used for the analysis. Owing to the big computational cost of high-temperature simulations, we chose lower range of vitrification temperatures (600 °C), while experiments were performed at somewhat higher temperatures (~700 °C).

Spinel synthesis and XAFS analysis. Ni-, Zn- or Co-doped Tc-incorporated magnetite was synthesized at high pH (>13). Three solutions of 0.05 M Ni, Zn and Co in distilled deionized water (DDI) were prepared using analytical-grade $\text{NiCl}_2$, $\text{ZnCl}_2$ and $\text{CoCl}_2$. Technetium solution (0.001 M) was prepared by spiking 10,000 p.p.m. $\text{NaTcO}_4$ stock solution into 1 M NaOH solution. Synthesized $\text{Fe(OH)}_2$ dry powder (0.09 g) was mixed with 5 ml of $\text{NiCl}_2$, $\text{ZnCl}_2$ or $\text{CoCl}_2$ solution in 20-ml poly vials and shaken on an orbital shaker (120 r.p.m.) for 24 h at room temperature (RT). After 24 h shaking, 15 ml of the Tc-spiked 1-M NaOH was added to each vial and heated in an oven at 75 °C for 72 h. After cooling to RT, the precipitates were separated using 0.45-μm filters and washed using ~120 ml DDI

<table>
<caption>Table 1 | Equilibrium constants and free energy estimates considering doping effects.</caption>
<thead>
<tr>
<th>Doping</th>
<th>$K_{\text{eq}}$</th>
<th>$\Delta G$ (kJ mol⁻¹)</th>
<th>Exp. retention (%wt)</th>
<th>$\Delta E_{\text{gap}}$(eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tc</td>
<td>0.15</td>
<td>14.2</td>
<td>–</td>
<td>0.15</td>
</tr>
<tr>
<td>Tc/Ni</td>
<td>0.56</td>
<td>4.3</td>
<td>4</td>
<td>0.35</td>
</tr>
<tr>
<td>Tc/Zn</td>
<td>2.79</td>
<td>−7.7</td>
<td>12</td>
<td>1.03</td>
</tr>
<tr>
<td>Tc/Co</td>
<td>21.80</td>
<td>−23.1</td>
<td>29</td>
<td>1.12</td>
</tr>
<tr>
<td colspan="5">Tc implies system without dopant. Relative populations determined as a ratio from the computed $K_{\text{eq}}$ values. Experimental values correspond to the amount of Tc remaining in the doped magnetite after exposure to 700 °C. $\Delta E_{\text{gap}}$ represents the energy difference between the Fermi level $E_{\text{F}}$ and the Tc HOMO energy from the projected DOS.</td>
</tr>
</tbody>
</table>

water immediately after filtering. The collected solid precipitates were air-dried at RT overnight and stored in glass vials. Strong microwave-assisted digestion with a solution consisting of 16 M HNO₃ (17%), 12 M HCl (72%), 32 M HF (3.3%), 0.5 g H₃BO₃ (1.5%) and DDI water (71.2%) on a volume basis was used to determine the total Tc concentration in the final solid samples. For the 600 °C XANES sample, ~5 g of Tc-magnetite was mixed with other basic glass feeds in a Pt crucible and heated in a furnace to 1,000 °C at 5 °C increase per minute. After air quenching, the final glass was pulverized and used for XANES analysis. Additional Tc XAFS samples were also prepared for Ni-, Zn- or Co-doped Tc-incorporated magnetite at room temperature without basic glass feeds and treated at 700 °C inside an oven. The XAFS spectra were collected at room temperature on Beamline 4-1 at the Stanford Synchrotron Radiation Laboratory. A Si(220) double-flat crystal mono- chromator was used, and the energy was calibrated by using the first inflection point of the Tc K edge spectrum of the Tc(VII) standard (KTCo₄) defined as 21.044 keV. The XAFS spectra of Tc standards and Tc-magnetite samples were collected in transmission and fluorescence mode, respectively, at RT using a 13- element germanium detector. Data reduction and analysis were performed using the software IFFEFIT and Athena/Artemis⁴³ after detector dead-time correction. The XANES spectra for Tc samples were fit using a linear combination of the XANES spectra of KTcO₄ as the Tc(VII) standard spectrum and TcO₂•2H₂O as the Tc(IV) standard spectrum, see Supplementary Fig. 7 and Supplementary Methods for more details.

Data availability. The authors declare that the data supporting the findings of this study are available within the article and its supplementary information files.

### References
1. Kotegov, K. V., Pavlov, O. N. & Shvedov, V. P. in *Advances in Inorganic Chemistry and Radiochemistry* (eds Emeléus, H. J. & Sharpe, A. G.) Vol. 11, 1–90 (Academic Press, 1968).
2. Luykx, F. in *Technetium in the Environment* (eds Desmet, G. & Myttenaere, C.) 21–27 (Springer, 1986).
3. Chen, F., Burns, P. C. & Ewing, R. C. Near-field behavior of ⁹⁹Tc during the oxidative alteration of spent nuclear fuel. *J. Nucl. Mater.* **278**, 225–232 (2000).
4. Childs, B., Poineau, F., Czerwinski, K. & Sattelberger, A. The nature of the volatile technetium species formed during vitrification of borosilicate glass. *J. Radioanal. Nucl. Ch.* **306**, 417–421 (2015).
5. Darab, J. G. & Smith, P. A. Chemistry of technetium and rhenium species during low-level radioactive waste vitrification. *Chem. Mater.* **8**, 1004–1021 (1996).
6. Muller, I. S., McKeown, D. A. & Pegg, I. L. Structural behavior of Tc and I ions in nuclear waste glass. *Proc. Mater. Sci.* **7**, 53–59 (2014).
7. Icenhower, J. P., Qafoku, N. P., Martin, W. & Zachara, J. M. *The Geochemistry of Technetium: a Summary of the Behavior of an Artificial Element in the Natural Environment*. PNNL-18139. (Pacific Northwest National Laboratory, Richland, Washington, USA, 2008).
8. Marshall, T. A. *et al.* Incorporation and retention of 99-Tc(IV) in magnetite under high pH conditions. *Environ. Sci. Technol.* **48**, 11853–11862 (2014).
9. Zachara, J. M. *et al.* Reduction of pertechnetate [Tc(VII)] by aqueous Fe(II) and the nature of solid phase redox products. *Geochim. Cosmochim. Acta* **71**, 2137–2157 (2007).
10. Cui, D. & Eriksen, T. E. Reduction of pertechnetate in solution by heterogeneous electron transfer from Fe(II)-containing geological material. *Environ. Sci. Technol.* **30**, 2263–2269 (1996).
11. Cui, D. & Eriksen, T. E. Reduction of pertechnetate by ferrous iron in solution: influence of sorbed and precipitated Fe(II). *Environ. Sci. Technol.* **30**, 2259–2262 (1996).
12. Fan, D. *et al.* Reductive sequestration of pertechnetate (⁹⁹TcO₄⁻) by nano zerovalent iron (nZVI) transformed by abiotic sulfide. *Environ. Sci. Technol.* **47**, 5302–5310 (2013).
13. Farrell, J., Bostick, W. D., Jarabek, R. J. & Fiedor, J. N. Electrosorption and reduction of pertechnetate by anodically polarized magnetite. *Environ. Sci. Technol.* **33**, 1244–1249 (1999).
14. Fredrickson, J. K. *et al.* Reduction of TcO₄⁻ by sediment-associated biogenic Fe(II). *Geochim. Cosmochim. Acta* **68**, 3171–3187 (2004).
15. Fredrickson, J. K. *et al.* Oxidative dissolution potential of biogenic and abiogenic TcO₂ in subsurface sediments. *Geochim. Cosmochim. Acta* **73**, 2299–2313 (2009).
16. Peretyazhko, T. *et al.* Heterogeneous reduction of Tc(VII) by Fe(II) at the solid-water interface. *Geochim. Cosmochim. Acta* **72**, 1521–1539 (2009).
17. Peretyazhko, T. *et al.* Reduction of Tc(VII) by Fe(II) sorbed on Al (hydr)oxides. *Environ. Sci. Technol.* **42**, 5499–5506 (2008).
18. Burke, I. T. *et al.* Reoxidation behavior of technetium, iron, and sulfur in estuarine sediments. *Environ. Sci. Technol.* **40**, 3529–3535 (2006).
19. Fan, D. *et al.* Oxidative remobilization of technetium sequestered by sulfide-transformed nano zerovalent iron. *Environ. Sci. Technol.* **48**, 7409–7417 (2014).
20. Szecsody, J. E., Jansik, D. P., McKinley, J. P. & Hess, N. J. Influence of alkaline co-contaminants on technetium mobility in vadose zone sediments. *J. Environ. Radioact.* **135**, 147–160 (2014).
21. Um, W. *et al.* Immobilization of 99-technetium (VII) by Fe(II)-goethite and limited reoxidation. *Environ. Sci. Technol.* **45**, 4904–4913 (2011).
22. Kobayashi, T., Scheinost, A. C., Gaona, X. & Altmaier, M. Redox behavior of Tc(VII)/Tc(IV) under various reducing conditions in 0.1 M NaCl solutions. *Radiochim. Acta* **101**, 323–332 (2013).
23. Sidhu, P. S., Gilkes, R. J. & Posner, A. M. Mechanism of the low temperature oxidation of synthetic magnetites. *J. Inorg. Nucl. Chem.* **39**, 1953–1958 (1977).
24. Jolivet, J. P. & Tronc, E. Interfacial electron transfer in colloidal spinel iron oxide. conversion of Fe₃O₄-γFe₂O₃ in aqueous medium. *J. Colloid Interf. Sci.* **125**, 701 (1988).
25. Bliem, R. *et al.* Subsurface cation vacancy stabilization of the magnetite (001). *Surf. Sci.* **346**, 1215–1218 (2014).
26. Chambers, S. A., Thevuthasan, S. & Joyce, S. A. Surface structure of MBE-grown Fe₃O₄(001) by X-ray photoelectron diffraction and scanning tunneling microscopy. *Surf. Sci.* **450**, L273–L279 (2000).
27. Gaines, J. M. *et al.* An STM study of Fe₃O₄(100) grown by molecular beam epitaxy. *Surf. Sci.* **373**, 275–297 (1997).
28. Pentcheva, R. *et al.* Jahn-Teller stabilization of a "polar" metal oxide surface: Fe₃O₄(001). *Phys. Rev. Lett.* **94**, 126101 (2005).
29. Stanka, B., Hebenstreit, W., Diebold, U. & Chambers, S. A. Surface reconstruction of Fe₃O₄(001). *Surf. Sci.* **448**, 49–63 (2000).
30. Tarrach, G., Bürgler, D., Schaub, T., Wiesendanger, R. & Güntherodt, H. J. Atomic surface structure of Fe₃O₄(001) in different preparation stages studied by scanning tunneling microscopy. *Surf. Sci.* **285**, 1–14 (1993).
31. Verwey, E. J. W. Electronic conduction of magnetite (Fe₃O₄) and its transition point at low temperatures. *Nature* **144**, 327–328 (1939).
32. Lukens, W. W., Bucher, J. J., Edelstein, N. M. & Shuh, D. K. Products of pertechnetate radiolysis in highly alkaline solution: structure of TcO₂·xH₂O. *Environ. Sci. Technol.* **36**, 1124–1129 (2002).
33. Allen, P. G. *et al.* Technetium speciation in cement waste forms determined by X-ray absorption fine structure spectroscopy. *Radiochim. Acta* **76**, 77–86 (1997).
34. Pang, S. C., Chin, S. F. & Anderson, M. A. Redox equilibria of iron oxides in aqueous-based magnetite dispersions: Effect of pH and redox potential. *J. Colloid Interf. Sci.* **311**, 94–101 (2007).
35. CRC. *Handbook of Chemistry and Physics* 75th edn (CRC Press, 1994–1995).
36. Hamdani, M., Singh, R. N. & Chartier, P. Co₃O₄ and Co-based spinel oxides bifunctional oxygen electrodes. *Int. J. Electrochem. Sci.* **5**, 556–577 (2010).
37. VandeVondele, J. *et al.* Quickstep: fast and accurate density functional calculations using a mixed gaussian and plane waves approach. *Comput. Phys. Commun.* **167**, 103–128 (2005).
38. Perdew, J. P., Burke, K. & Ernzerhof, M. Generalized gradient approximation made simple. *Phys. Rev. Lett.* **77**, 3865–3868 (1996).
39. Goedecker, S., Teter, M. & Hutter, J. Separable dual-space Gaussian pseudopotentials. *Phys. Rev. B* **54**, 1703–1710 (1996).
40. VandeVondele, J. & Hutter, J. Gaussian basis sets for accurate calculations on molecular systems in gas and condensed phases. *J. Chem. Phys.* **127**, 114105 (2007).
41. Wright, J. P., Attfield, J. P. & Radaelli, P. G. Charge ordered structure of magnetite Fe₃O₄ below the Verwey transition. *Phys. Rev. B* **66**, 214422 (2002).
42. Bliem, R. *et al.* Adsorption and incorporation of transition metals at the magnetite Fe₃O₄ (001) surface. *Phys. Rev. B* **92**, 075440 (2015).
43. Ravel, B. & Newville, M. ATHENA, ARTEMIS, HEPHAESTUS: data analysis for X-ray absorption spectroscopy using IFEFFIT. *J. Synchrotron Radiat.* **12**, 537–541 (2005).

### Acknowledgements
This work was supported by the US Department of Energy, Office of River Protection, Waste Treatment and Immobilization Plant Federal Project and the Office of Basic Energy Science, Division of Chemical Sciences, Geosciences and Biosciences (R.R. and V.-A.G.). PNNL is a multiprogramme national laboratory operated for DOE by Battelle. Computational resources were provided by PNNL's Platform for Institutional Com- puting (PIC), the W. R. Wiley Environmental Molecular Science Laboratory (EMSL), a national scientific user facility sponsored by the Department of Energy's Office of Biological and Environmental Research located at PNNL and the National Energy Research Scientific Computing Center (NERSC) at Lawrence Berkeley National Laboratory. Part of this work was supported by the US Department of Energy, Office of Science, Basic Energy Sciences, Chemical Sciences, Biosciences, and Geosciences Division, Heavy Element Chemistry Program (W.W.L.) and was performed at Lawrence Berkeley National Laboratory under contract No. DE-AC02-05CH11231. Tc K-edge XAFS spectra were obtained at the Stanford Synchrotron Radiation Lightsource, SLAC National Accelerator Laboratory, which is supported by the U.S. Department of Energy, Office of Science, Office of Basic Energy Sciences under Contract No. DE-AC02-76SF00515. We thank Dong-Sang Kim and Michael J. Schweiger of PNNL for their

constructive feedback and in-depth discussions associated with the development of this plan. The high-temperature experiments conducted by Steven A. Luksic and Chuck Z. Soderquist in PNNL are greatly appreciated. Nathan Johnson (PNNL) created the cover and feature images in collaboration with V.-A.G.

## Author contributions
All authors provided input for the manuscript. M.-S.L. contributed to the planning and executed the simulations and analysed the data, W.U., G.W. and W.W.L. performed the experiments and related data analysis. R.R. provided pseudopotentials for the calcula- tions and contributed to the analysis of the data. V.-A.G. planned and supervised the research. M.-S.L., R.R. and V.-A.G. jointly wrote the manuscript with input from all authors.

## Additional information
Supplementary Information accompanies this paper at http://www.nature.com/ naturecommunications

Competing financial interests: The authors declare no competing financial interests.

Reprints and permission information is available online at http://npg.nature.com/ reprintsandpermissions/

How to cite this article: Lee, M.-S. et al. Impeding $^{99}$Tc(IV) mobility in novel waste forms. *Nat. Commun.* 7:12067 doi: 10.1038/ncomms12067 (2016).

![](./images/811259199311839233_4.jpg)
This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/

© The Author(s) 2016
