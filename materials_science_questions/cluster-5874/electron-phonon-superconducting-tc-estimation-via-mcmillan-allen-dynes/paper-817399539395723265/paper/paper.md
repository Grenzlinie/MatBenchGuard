PHYSICAL REVIEW B 101, 214518 (2020)

Editors' Suggestion

# Superconductivity and topological aspects of the rocksalt carbides NbC and TaC

T. Shang $\odot,^{1, *}$ J. Z. Zhao $\odot,^{2,3, \dagger}$ D. J. Gawryluk, $^{1}$ M. Shi, $^{4}$ M. Medarde, $^{1}$ E. Pomjakushina, $^{1}$ and T. Shiroka $\odot^{5,6}$

$^{1}$ Laboratory for Multiscale Materials Experiments, Paul Scherrer Institut, Villigen CH-5232, Switzerland
$^{2}$ Co-Innovation Center for New Energetic Materials, Southwest University of Science and Technology, Mianyang 621010, People's Republic of China
$^{3}$ Research Laboratory for Quantum Materials, Singapore University of Technology and Design, Singapore 487372, Singapore
$^{4}$ Swiss Light Source, Paul Scherrer Institut, Villigen CH-5232, Switzerland
$^{5}$ Laboratorium für Festkörperphysik, ETH Zürich, CH-8093 Zürich, Switzerland
$^{6}$ Paul Scherrer Institut, CH-5232 Villigen PSI, Switzerland

![](./images/817399539395723265_1.jpg)
(Received 27 April 2020; revised manuscript received 19 May 2020; accepted 3 June 2020; published 18 June 2020)

Superconducting materials with a nontrivial band structure are potential candidates for topological superconductivity. Here, by combining muon-spin rotation and relaxation ($\mu$SR) methods with theoretical calculations, we investigate the superconducting and topological properties of the rocksalt-type compounds NbC and TaC (with $T_c = 11.5$ and 10.3 K, respectively). At a macroscopic level, the magnetization and heat-capacity measurements under applied magnetic field provide an upper critical field of 1.93 and 0.65 T for NbC and TaC, respectively. The low-temperature superfluid density, determined by transverse-field $\mu$SR and electronic specific-heat data, suggest a fully gapped superconducting state in both NbC and TaC, with a zero-temperature gap $\Delta_0 = 1.90$ and 1.45 meV, and a magnetic penetration depth $\lambda_0 = 141$ and 77 nm, respectively. Band-structure calculations suggest that the density of states at the Fermi level are dominated by the Nb $4d$ (or Ta $5d$) orbitals, which are strongly hybridized with the C $p$ orbitals to produce large cylinderlike Fermi surfaces, similar to those of high-$T_c$ iron-based superconductors. Without considering the spin-orbit coupling (SOC) effect, the first Brillouin zone contains three closed node lines in the bulk band structure, protected by time-reversal and space-inversion symmetry. When considering SOC, its effects in the NbC case appear rather modest. Therefore, the node lines may be preserved in NbC, hence proposing it as a potential topological superconductor.

DOI: 10.1103/PhysRevB.101.214518

## I. INTRODUCTION

Recently, the binary transition-metal arsenide (TMA) materials have been widely studied due to their exotic physical properties. Here, TM represents an early transition metal (e.g., Cr, Nb, Mo, Ta, or W), while A represents a carbon-, pnictogen-, or chalcogen-group element (e.g., C, P, or As). Some TMA materials are believed to exhibit unconventional superconductivity (SC). For instance, originally CrAs and MnP exhibit antiferromagnetic and ferromagnetic long-range order below 264 and 290 K, respectively [1]. Under applied pressure, the magnetic order is suppressed and a domelike superconducting phase appears near the magnetic quantum critical point, suggesting an unconventional SC pairing in these materials [1–5]. Beyond superconductivity, TMAs are among the best candidate materials for studying topological phenomena. Weyl fermions, originally predicted in high-energy physics [6], were recently discovered as quasiparticles in Ta(As,P) and Nb(As,P) crystals via angle-resolved photoemission experiments [7–11]. Later on, three-component fermions were experimentally observed in MoP and WC [12,13]. Now, all the above-mentioned TMA materials are known as Weyl or topological semimetals.

The materials where superconductivity coexists with a nontrivial topological band structure may exhibit emergent phenomena, such as topological superconductivity and Majorana fermions [14,15]. By applying external pressure, the topological semimetal MoP becomes a superconductor, whose $T_c$ raises up to 4 K (above 90 GPa) [16], thus representing a candidate topological superconductor. In contrast to MoP, the orthorhombic WP is a superconductor already at ambient pressure (below 0.8 K) [17], but its topological nature is not yet known. In addition to MoP and WP, the transition-metal carbides (TMCs), too, can exhibit a large variety of band topologies in their different structural forms. The TMCs provide an exciting family of candidate materials for studying the rich physics of topological SC and Majorana bound states. Generally, TMCs with a 1:1 metal-carbon stoichiometric ratio adopt two types of crystal structures. One is the so-called $\delta$ phase, a centrosymmetric cubic structure with space group $Fm\overline{3}m$ (No. 225), also known as rocksalt phase. The other is the $\gamma$ phase, a noncentrosymmetric hexagonal structure with space group $P\overline{6}m2$ (No. 187). The above-mentioned topological MoP and WC semimetals crystallize in the $\gamma$ phase. In the case of MoC, although its SC has been reported in the 1970s [18], its physical properties have been overlooked due to difficulties in synthesizing clean samples. Only recently, the

*Corresponding author: tian.shang@psi.ch
†Corresponding author: jzzhao@swust.edu.cn

2469-9950/2020/101(21)/214518(11)
214518-1
©2020 American Physical Society

carbon-defective $\delta$ and $\gamma$ phase of $\text{MoC}_{1-x}$ (with $T_c = 14.3$ and 8.5 K) could be synthesized under high-temperature high-pressure conditions ($1700\ ^\circ\text{C}$, 6–17 GPa), and their crystal structures and physical properties be studied via different techniques [19–21]. Moreover, in both $\delta$ and $\gamma$ MoC, first-principles calculations could show the coexistence of SC with nontrivial band topology [22].

Other TMCs, such as $\delta$-type VC and CrC, are also predicted to be superconductors with nontrivial topological band structures and, therefore, are candidates for searching for topological superconductivity [23]. Although both VC and CrC should exhibit relatively high critical temperatures [24–27], to date experimental evidence is inconsistent. For VC, the experimentally reported value ($T_c \sim$ 2 K) is an order of magnitude less than the theoretically predicted one ($\sim$18 K) [27,28]. As for CrC, experimental evidence of SC is still missing. Besides MoC, also NbC and TaC show rocksalt-type structures [29] and become superconductors below 11 K [18,30,31]. Unlike MoP or MoC, where extremely high pressures are required to induce SC, either during synthesis or as an external tuning parameter [16,19–21], NbC and TaC are easy to synthesize and show SC already at ambient pressure. However, to the best of our knowledge, none of the early works had a follow-up regarding the microscopic investigation of their superconducting properties. Considering that $\delta$-type VC and CrC show nontrivial topological band structures, we expect the isostructural NbC and TaC, too, to exhibit similar features.

In this paper, we report on an extensive study of the superconducting properties of the NbC and TaC carbides, carried out via magnetization, heat-capacity, and muon-spin relaxation/rotation ($\mu$SR) measurements. In addition, we also present numerical density-functional-theory (DFT) band-structure calculations. We find that both NbC and TaC exhibit a fully gapped superconducting state, while their electronic band structures suggest that, without considering spin-orbit coupling (SOC), both compounds are nodal line semimetals. After taking SOC into account, the degenerate bands are gapped out, except for six Dirac points on the high-symmetry lines. Therefore, these two carbides are potential candidates for studying topological SC and its associated Majorana bound states.

## II. EXPERIMENTAL AND NUMERICAL METHODS

The samples consisted of high-purity NbC and TaC (99+%) powders acquired from ChemPUR. For the heat-capacity and $\mu$SR measurements the powders were pressed into small pellets, while for the magnetization measurements loose powders were used. Room-temperature x-ray powder diffraction (XRD) measurements were performed on a Bruker D8 diffractometer using $\text{Cu}\ K\alpha$ radiation. The magnetic susceptibility, and heat-capacity measurements were performed on a 7-T Quantum Design magnetic property measurement system (MPMS-7) and a 9-T physical property measurement system (PPMS-9). The $\mu$SR measurements were carried out at the general-purpose-surface-muon (GPS) spectrometer of the Swiss muon source at Paul Scherrer Institut, Villigen, Switzerland [32]. The $\mu$SR data were analyzed by means of the MUSRFIT software package [33].

![](./images/817399539395723265_2.jpg)

FIG. 1. Room-temperature x-ray powder diffraction pattern and Rietveld refinements for TaC. The open red circles and the solid black line represent the experimental pattern and the refinement profile, respectively. The blue line at the bottom shows the residuals, i.e., the difference between the calculated and the experimental data. The vertical bars mark the calculated Bragg-peak positions. The cubic crystal structure (unit cell) is shown in the inset.

The electronic band structures of NaC and TaC were calculated via the density functional theory, within the generalized gradient approximation of Perdew-Burke-Ernzerhof realization [34], as implemented in the Vienna ab initio Simulation Package (VASP) [35,36]. The projector augmented wave pseudopotentials were adopted for the calculation [37,38]. Electrons belonging to the outer atomic configuration were treated as valence electrons, here corresponding to 5 electrons in Ta ($5d^36s^2$), 11 electrons in Nb ($4p^64d^45s$), and 4 electrons in C ($2s^22p^2$). The kinetic energy cutoff was fixed to 550 eV. For the self-consistent calculation, the Brillouin zone integration was performed on a $\Gamma$-centered mesh of $20 \times 20 \times 20$ $k$ points. The spin-orbit coupling was taken into account by using a scalar relativistic approximation. In our calculations we used the lattice parameters and the atomic positions experimentally determined from the Rietveld refinements.

## III. RESULTS AND DISCUSSION

### A. Crystal structure

The phase purity and the crystal structure of NbC and TaC powders were checked via XRD at room temperature. Figure 1 shows the XRD pattern of TaC (with NbC showing a similar pattern), analyzed by means of the FULLPROF Rietveld-analysis suite [39]. Consistent with previous neutron-scattering results [29], we find that NbC and TaC powders crystallize in the simple fcc NaCl-type structure, with space group $Fm\overline{3}m$ (No. 225) (see crystal structure in the inset of Fig. 1). There are only two atomic positions in the unit cell: $4a$ (0,0,0) for the Nb/Ta atoms, and $4b$ (0.5,0.5,0.5) for the C atoms. The refined lattice parameters, $a = 4.4676(1)$ Å (NbC) and $a = 4.4557(1)$ Å (TaC), are consistent with the values determined from neutron scattering [29]. No impurity phases could be detected in either case, thus indicating a good sample quality.

![](./images/817399539395723265_3.jpg)

FIG. 2. (a) Magnetic susceptibility of NbC and TaC vs temperature, measured in an applied field of 5 mT using both ZFC and FC protocols. (b) Estimated lower critical field $\mu_0H_{c1}$ vs temperature for NbC and TaC. The solid lines are fits to $\mu_0H_{c1}(T) = \mu_0H_{c1}(0)[1 - (T/T_c)^2]$. Field-dependent magnetization recorded at various temperatures up to $T_c$ are shown in (c) for NbC and (d) for TaC. For each temperature, the lower critical field $\mu_0H_{c1}$ was determined as the value where $M(H)$ starts deviating from linearity (see dashed lines).

### B. Magnetization measurements

The superconductivity of the NbC and TaC powders was first characterized by magnetic susceptibility measurements, carried out in a 5-mT field, using both field-cooled (FC) and zero-field-cooled (ZFC) protocols. As indicated by the arrows in Fig. 2(a), a clear diamagnetic signal appears below the superconducting transition at $T_c = 11.5$ and 10.3 K for NbC and TaC, respectively. The $M(H)$ data for NbC and TaC are plotted in Figs. 2(c) and 2(d), respectively. In both cases, the field-dependent magnetization $M(H)$, collected at various temperatures up to $T_c$, allowed us to determine the lower critical field $\mu_0H_{c1}$. The estimated $\mu_0H_{c1}$ values as a function of temperature are summarized in Fig. 2(b). The solid lines represent fits to $\mu_0H_{c1}(T) = \mu_0H_{c1}(0)[1 - (T/T_c)^2]$ and yield a lower critical field of 10.3(3) and 29.3(3) mT for NbC and TaC, respectively.

### C. Upper critical fields

To estimate the upper critical field $\mu_0H_{c2}$ of NbC and TaC, temperature-dependent magnetization $M(T,H)$ and specific-heat $C(T,H)/T$ measurements, at various applied magnetic fields, as well as field-dependent magnetization $M(H,T)$ measurements, at various temperatures, were performed. As shown in Figs. 3(a) and 3(d), in both samples, the diamagnetic signal progressively disappears as the applied magnetic field exceeds the upper critical field. In Figs. 3(b) and 3(c) and in Figs. 3(e) and 3(f), the superconducting transition in both $M(T)$ and $C(T)/T$ datasets shifts towards lower temperatures as the applied field increases. In zero magnetic field, $T_c = 10.8$ and 10.2 K, determined from $C(T)/T$ for NbC and TaC, are consistent with the $T_c$ values determined from magnetic susceptibility data [Fig. 2(a)]. The upper critical fields determined from $M(H,T)$, $C(T,H)/T$, and $M(T,H)$ data are summarized in Figs. 4(a) and 4(b) as a function of the reduced superconducting transition temperature $T_c/T_c(0)$ for NbC and TaC, respectively. The $\mu_0H_{c2}(T)$ behavior was analyzed by means of the Werthamer-Helfand-Hohenberg (WHH) and Ginzburg-Landau (GL) models [40–42]. Both models describe the experimental data very well at low fields. However, at higher applied fields, the fits to the WHH model (dash-dotted lines) deviate significantly from the data, clearly providing underestimated $\mu_0H_{c2}$ values. Conversely, the GL model (solid lines) shows a remarkable agreement with the experimental data also at higher fields. Fits to the GL model, which reproduces the data very well across the full temperature range, provide $\mu_0H_{c2}^{\text{GL}}(0) = 1.93(1)$ and 0.65(1) T for NbC and TaC, respectively.

### D. Zero-field $\mu$SR

Zero-field (ZF) $\mu$SR measurements are quite suited for detecting possible magnetic order or magnetic fluctuations,

![](./images/817399539395723265_4.jpg)

FIG. 3. (a) Field-dependent magnetization $M(H,T)$ collected at various temperatures, (b) temperature-dependent magnetization $M(T,H)$, and (c) specific heat $C(T,H)/T$ measured in various applied magnetic fields for NbC. The analogous results for the TaC samples are presented in panels (d)-(f), respectively.

![](./images/817399539395723265_5.jpg)

FIG. 4. Summary of the upper critical field data $\mu_0H_{c2}$ vs reduced temperature $T_c/T_c(0)$, as determined from field-dependent magnetization $M(H,T)$, temperature-dependent magnetization $M(T,H)$, and specific heat $C(T,H)/T$ for (a) NbC and (b) TaC, respectively. For $M(H,T)$, the $H_{c2}$ value was determined as the field where the diamagnetic signal is suppressed. Two different models, including an effective GL (solid lines) and a WHH model (dash-dotted lines), were used to analyze the $\mu_0H_{c2}(T)$ data.

as well as time-reversal symmetry breaking in the superconducting state. Here, we performed ZF-$\mu$SR measurements in both the normal and the superconducting states of NbC and TaC, with representative spectra collected above and below $T_c$ being shown in Fig. 5. In either case, neither coherent oscillations nor fast decays could be identified, hence implying the lack of any magnetic order or fluctuations. The weak muon-spin relaxation detected in the absence of an external magnetic field is mainly due to the randomly oriented nuclear moments, which can be modeled by a Gaussian Kubo-Toyabe relaxation function $G_{\text{KT}}=\left[\frac{1}{3}+\frac{2}{3}(1-\sigma_{\text{ZF}}^2t^2)e^{-\sigma_{\text{ZF}}^2t^2/2}\right]$ [43,44]. Here, $\sigma_{\text{ZF}}$ is the zero-field Gaussian relaxation rate. The solid lines in Fig. 5 represent fits to the data by considering also an additional zero-field Lorentzian relaxation $\Lambda_{\text{ZF}}$, i.e., $A_{\text{ZF}}(t)=A_sG_{\text{KT}}e^{-\Lambda_{\text{ZF}}t}+A_{\text{bg}}$. Here $A_s$ and $A_{\text{bg}}$ represent the initial muon-spin asymmetries for muons implanted in the sample and sample holder (copper), respectively. In either carbide compound, the relaxations in both the normal and the superconducting states are almost identical, as demonstrated by the practically overlapping ZF-$\mu$SR spectra above and below $T_c$. This lack of evidence for an additional $\mu$SR relaxation below $T_c$ excludes a possible time-reversal symmetry breaking in the superconducting state of NbC or TaC and is supported also by the theoretical arguments discussed in Sec. III G. The larger Gaussian relaxation rate of NbC $(\sigma_{\text{ZF}}=0.432\ \mu\text{s}^{-1})$ compared to TaC $(\sigma_{\text{ZF}}=0.183\ \mu\text{s}^{-1})$ reflects the larger nuclear magnetic moment of $^{93}$Nb $(6.2\mu_n)$ compared to $^{181}$Ta $(2.4\mu_n)$, the two ratios (in the presence of similar structures) being almost the same, $\sim$2.5. Finally, both samples show a very small Lorentzian relaxation $(\Lambda_{\text{ZF}}\sim0.011\ \mu\text{s}^{-1})$. Unlike in pure Nb, where there is a clear muon hopping (with a mobility minimum at 50 K) and where a dynamic Kubo-Toyabe function describes the ZF-$\mu$SR spectra quite well [45], in the NbC and the TaC case, no dynamic features were observed.

![](./images/817399539395723265_6.jpg)

FIG. 5. ZF-$\mu$SR spectra of (a) NbC and (b) TaC, recorded in the superconducting and the normal states. Solid lines are fits using the equation described in the text. None of the datasets shows evident changes with temperature.

### E. Transverse-field $\mu$SR

To investigate the superconducting properties of NbC and TaC at a microscopic level, we carried out systematic transverse-field (TF) $\mu$SR measurements. Generally, performing such measurements on type-II superconductors requires an applied magnetic field which exceeds $\mu_0H_{c1}$, thus allowing one to quantify the additional field-distribution broadening due to the flux-line lattice (FLL). Ideally, the optimal field value for such measurements is determined experimentally, via field-dependent $\mu$SR depolarization-rate measurements in the superconducting state. To track the additional field-distribution broadening due to the FLL in the mixed superconducting state, a magnetic field (up to 780 mT) was applied in the normal state and then the sample was cooled down to 1.5 K, where the TF-$\mu$SR spectra were collected.

As an example, Fig. 6(a) shows the spectra collected in an applied field of 30 and 400 mT in NbC, with TaC showing similar features. The solid lines are fits using the same model as described in Eq. (2) below. The resulting superconducting Gaussian relaxation rates $\sigma_{\text{sc}}(H)$ are summarized in Fig. 6(b). For both NbC and TaC, the relaxation rate decreases continuously when the applied field is larger than the lower critical field $\mu_0H_{c1}$. Therefore, as indicated in Fig. 6(b), fields of

![](./images/817399539395723265_7.jpg)

FIG. 6. (a) TF-$\mu$SR time spectra collected in the superconducting state of NbC (at $T = 1.5$ K) in an applied field of 30 and 400 mT. Similar results were obtained for TaC. (b) Field-dependent Gaussian relaxation rate $\sigma_{\rm sc}(H)$ for NbC and TaC. Solid lines are fits to Eq. (1), as described in the text. The arrows indicate the field values used in the temperature-dependent TF-$\mu$SR studies of NbC and TaC, 50 and 60 mT, respectively.

50 and 60 mT were chosen as suitable for the temperature-dependent TF-$\mu$SR studies of NbC and TaC, respectively. The field-dependent Gaussian relaxation rate $\sigma_{\rm sc}(H)$ can be described by the expression [46,47]

$$
\sigma_{\rm sc}=0.172 \frac{\gamma_{\mu} \Phi_{0}}{2 \pi}(1-h)\left[1+1.21(1-\sqrt{h})^{3}\right] \lambda^{-2}, \quad(1)
$$

where $\lambda$ is the magnetic penetration depth, $\gamma_{\mu}=2 \pi \times 135.53$ MHz/T is the muon gyromagnetic ratio, and $h=H_{\rm appl}/H_{c2}$, with $H_{\rm appl}$ the applied magnetic field. The above expression is valid for type-II superconductors with $\kappa \geqslant 5$ in the $0.25/\kappa^{1.3} \lesssim h \leqslant 1$ field range. With $\kappa \sim 13$ and 5, and $h=0.026$ and 0.092 for NbC and TaC, both samples fulfill the above conditions. The solid lines in Fig. 6(b) are fits to Eq. (1). The derived $\mu_{0}H_{c2}=1.81(2)$ and 0.43(1) T and magnetic penetration depths $\lambda_{0}=134(2)$ and 67(1) nm for NbC and TaC are comparable with the measured upper critical field values (see Fig. 4) and those determined via temperature-dependent TF-$\mu$SR (see Fig. 8).

TF-$\mu$SR spectra were also collected at various temperatures up to $T_{c}$ in a fixed applied field. Figures 7(a) and 7(b) show representative TF-$\mu$SR spectra, collected below (1.5 K) and above $T_{c}$ (12 K), for both NbC and TaC. The additional field-distribution broadening due to FLL in the mixed state is clearly reflected in the enhanced muon-spin depolarization below $T_{c}$. To describe the field distribution, the asymmetry of TF-$\mu$SR spectra can be modeled using

$$
A_{\mathrm{TF}}(t)=\sum_{i=1}^{n} A_{i} \cos \left(\gamma_{\mu} B_{i} t+\phi\right) e^{-\sigma_{i}^{2} t^{2} / 2}+A_{\mathrm{bg}} \cos \left(\gamma_{\mu} B_{\mathrm{bg}} t+\phi\right).
$$

Here $A_{i}$ and $A_{\mathrm{bg}}$ are the same as in ZF-$\mu$SR, with the latter term not undergoing any depolarization. $B_{i}$ and $B_{\rm bg}$ are the local fields sensed by implanted muons in the sample and sample holder, $\phi$ is a shared initial phase, and $\sigma_{i}$ is the Gaussian relaxation rate of the $i$th component.

![](./images/817399539395723265_8.jpg)

FIG. 7. TF-$\mu$SR spectra collected in the (a) superconducting (1.5 K) and (b) normal state (12 K), in an applied field of 50 mT for NbC and 60 mT for TaC. Fast Fourier transforms of the relevant time spectra at (c) 1.5 K and (d) 12 K. The solid lines through the data are fits to Eq. (2); the vertical dashed lines mark the applied magnetic fields. Note the clear diamagnetic shift and the field broadening in (c), typical of the superconducting phase.

Figures 7(c) and 7(d) show the fast Fourier transform (FFT) of the TF-$\mu$SR spectra in Figs. 7(a) and 7(b), respectively. As can be seen in Fig. 7(c), the field distribution in TaC is much broader and asymmetric than in NbC, consistent with a larger muon-spin depolarization in TaC in Fig. 7(a). Solid lines represent fits to Eq. (2) using a single oscillation (i.e., $n=1$) or two oscillations (i.e., $n=2$) for NbC and TaC, respectively. The derived Gaussian relaxation rates as a function of temperature are summarized in the insets of Fig. 8, together with the diamagnetic shifts. Above $T_{c}$ the relaxation rate is small and temperature independent, but below $T_{c}$ it starts to increase due to the formation of the FLL and the increase in superfluid density. In addition, a diamagnetic field shift appears in both samples below $T_{c}$.

In the case of multicomponent oscillations, the first term in Eq. (2) describes the field distribution as the sum of $n$ Gaussian relaxations (here $n=2$ for TaC) [48]:

$$
P(B)=\gamma_{\mu} \sum_{i=1}^{2} \frac{A_{i}}{\sigma_{i}} \exp \left[-\frac{\gamma_{\mu}^{2}\left(B-B_{i}\right)^{2}}{2 \sigma_{i}^{2}}\right]. \quad(3)
$$

The first and the second moments of the field distribution can be calculated by [48]

$$
\langle B\rangle=\sum_{i=1}^{2} \frac{A_{i} B_{i}}{A_{\mathrm{tot}}}, \quad \text { and }
$$

$$
\left\langle B^{2}\right\rangle=\frac{\sigma_{\mathrm{eff}}^{2}}{\gamma_{\mu}^{2}}=\sum_{i=1}^{2} \frac{A_{i}}{A_{\mathrm{tot}}}\left[\frac{\sigma_{i}^{2}}{\gamma_{\mu}^{2}}+\left(B_{i}-\langle B\rangle\right)^{2}\right], \quad(4)
$$

where $A_{\rm tot}=A_{1}+A_{2}$. After subtracting the nuclear relaxation rate $\sigma_{\rm n}$, according to $\sigma_{\rm sc}=\sqrt{\sigma_{\rm eff}^{2}-\sigma_{\rm n}^{2}}$, the superconducting Gaussian relaxation rate $\sigma_{\rm sc}$ can be extracted. The $\sigma_{\rm n}$ is considered to be temperature independent, as confirmed also by the ZF-$\mu$SR data in Fig. 5.

![](./images/817399539395723265_9.jpg)

FIG. 8. Superfluid density vs temperature, as determined from TF-$\mu$SR measurements in an applied magnetic field of 50 mT for (a) NbC and 60 mT for (b) TaC. The insets show the temperature dependence of the muon-spin relaxation rate $\sigma(T)$ and of the diamagnetic shift $[\Delta B(T)=\langle B\rangle-B_{\text{appl.}}]$. Two $\sigma$ values are required to describe the TF-$\mu$SR data of TaC, while NbC requires only one $\sigma$ [see details in Fig. 7(c)].

For both NbC and TaC, the inverse square of the magnetic penetration depth $\lambda^{-2}(T)$ [proportional to the superfluid density $\rho_{\text{sc}}(T)$] is calculated by using Eq. (1) and shown in the main panels of Fig. 8 vs the reduced $T/T_{c}$. Below $T_{c}/3$, the superfluid density is almost constant, thus excluding the possibility of superconducting gap nodes and indicating a fully gapped SC in NbC and TaC. To gain more quantitative insights into the superconductivity of NbC and TaC, the superfluid density $\rho_{\text{sc}}(T)$ was further analyzed by means of a fully gapped $s$-wave model:

$$
\rho_{\text{sc}}(T)=1+2 \int_{\Delta(T)}^{\infty} \frac{E}{\sqrt{E^{2}-\Delta^{2}(T)}} \frac{\partial f}{\partial E} d E. \tag{5}
$$

Here $f=(1+e^{E/k_{\text{B}}T})^{-1}$ and $\Delta(T)$ are the Fermi and the superconducting-gap functions. The $\Delta(T)$ is assumed to follow $\Delta(T)=\Delta_{0}\tanh\{1.82[1.018(T_{\text{c}}/T-1)]^{0.51}\}$ [49], where $\Delta_{0}$ is the zero-temperature superconducting-gap value. The solid lines in the main panels of Fig. 8 are fits to the above model with a single gap, which yield zero-temperature gap values $\Delta_{0}=1.90(2)$ and $1.45(1)$ meV, and magnetic penetration depths $\lambda_{0}=141(2)$ and 77(1) nm for NbC and TaC, respectively. Since in NbC, the $H_{\text{appl}}/H_{c2} \ll 1$, the magnetic penetration depth can also be calculated using $\sigma_{\text{sc}}^{2}(T)/\gamma_{\mu}^{2}=0.00371\Phi_{0}^{2}/\lambda^{4}(T)$ [47], which gives a comparable $\lambda_{0}=162(2)$ nm.

According to the GL theory of superconductivity, the coherence length $\xi$ can be calculated by using $\xi=\sqrt{\Phi_{0}/2\pi H_{c2}}$, where $\Phi_{0}=2.07\times 10^{3}$ T nm$^{2}$ is the quantum of magnetic flux. With a bulk $\mu_{0}H_{c2}(0)=1.93(1)$ and 0.65(1) T, the calculated $\xi(0)$ are 13.1(1) and 22.5(1) nm for NbC and TaC, respectively. A GL parameter $\kappa=\lambda/\xi \sim 11$ (NbC) and 3.4 (TaC), much larger than the $1/\sqrt{2}$ threshold value, clearly confirms the type-II superconductivity in both NbC and TaC, consistent with the magnetization results in Sec. III B.

![](./images/817399539395723265_10.jpg)

FIG. 9. Normalized electronic specific heat $C_{e}/\gamma_{\text{n}}T$ vs reduced temperature $T/T_{c}$ for NbC (a) and TaC (b). Here $\gamma_{\text{n}}$ is the normal-state electronic specific-heat coefficient. The measured specific heat $C/T$ vs $T^{2}$ are shown in the insets. The dashed lines in the insets are fits to $C/T=\gamma_{n}+\beta T^{2}+\delta T^{4}$ for $T>T_{c}$, while the solid lines in the main panel represent the electronic specific heat calculated by considering a fully gapped $s$-wave model for $T \leqslant T_{c}$.

### F. Zero-field specific heat

The zero-field electronic specific-heat data were further analyzed. As shown by the dashed lines in the insets of Fig. 9, the normal-state specific heat was fitted to $C/T=\gamma_{n}+\beta T^{2}+\delta T^{4}$, where $\gamma_{\text{n}}$ is the normal-state electronic specific-heat coefficient, and the two other terms account for the phonon contribution to the specific heat. After subtracting the latter from the experimental data, the obtained electronic specific heat divided by the electronic specific-heat coefficient, i.e., $C_{e}/\gamma_{\text{n}}T$, is shown in the main panels of Fig. 9 vs the reduced temperature $T/T_{c}$. The solid lines in Fig. 9 represent fits with $\gamma_{\text{n}}=3.0(4)$ and 3.1(8) mJ/mol K$^{2}$ and a single isotropic gap $\Delta_{0}=1.73(2)$ and 1.54(2) meV for NbC and TaC, respectively. They reproduce very well the experimental data, while being comparable with the TF-$\mu$SR results (see Fig. 8).

The Debye temperature $\Theta_{\text{D}}$ can be calculated by using $\Theta_{\text{D}}=(12\pi^{4}Rn/5\beta)^{1/3}$, where $R=8.314$ J/mol K is the molar gas constant and $n=2$ is the number of atoms per formula unit. With $\beta=8.0(8)$ and 19(2) $\mu$J/mol K$^{4}$, the

estimated $\Theta_{\rm D}$ are 790(20) and 590(20) K for NbC and TaC, respectively. The density of states (DOS) at the Fermi level $N(\epsilon_{\rm F})$ were evaluated from the expression $N(\epsilon_{\rm F}) = 3\gamma_{\rm h}/(\pi^2k_{\rm B}^2) \sim$1.3 states/eV f.u. for both NbC and TaC [50], where $k_{\rm B}$ is the Boltzmann constant. The electron-phonon coupling constant $\lambda_{\rm ep}$ was estimated from the $\Theta_{\rm D}$ and $T_c$ values by using the semiempirical McMillan formula [51]:

$$
\lambda_{\rm ep} = \frac{1.04 + \mu^{\star}\ln(\Theta_{\rm D}/1.45T_c)}{(1 - 0.62\mu^{\star})\ln(\Theta_{\rm D}/1.45T_c) - 1.04}. \tag{6}
$$

The Coulomb pseudopotential $\mu^{\star}$, typically lying in the 0.09–0.18 range, was fixed here to 0.13, a commonly used value for transition metals. From the above expression, we obtain $\lambda_{\rm ep} = 0.60(1)$ and 0.65(3) for NbC and TaC, both consistent with theoretical values [24]. Finally, the band-structure density of states $N_{\rm band}(\epsilon_{\rm F})$ can be estimated from the relation $N_{\rm band}(\epsilon_{\rm F}) = N(\epsilon_{\rm F})/(1 + \lambda_{\rm ep})$ [50], which gives $N_{\rm band}(\epsilon_{\rm F}) \sim$ 0.8 states/eV f.u. for both compounds.

### G. Electronic band-structure calculations

To further understand the electronic properties of NbC and TaC, we also performed DFT calculations. The electronic band-structure results, as well as the DOS are depicted in Fig. 10. Since NbC and TaC adopt the same rocksalt structure (see Fig. 1), it is natural that their band structures and DOS profiles are quite similar. Close to the Fermi level the bands are dominated by the $d$ electrons of TMs (Nb or Ta), while the contribution from the C $p$ electrons is quite modest. The $d$ and $p$ electrons are highly hybridized. The bands which cross the Fermi level are mainly occupied by the $t_{2g}$ ($d_{xy}$, $d_{yz}$, and $d_{xz}$) orbitals of TM, with marginal contributions from the $e_g$ ($d_{x^2-y^2}$ and $d_{z^2}$) or the $p$ orbitals of C. The occupied $e_g$ bands are mainly located about 4.0 eV below the Fermi level, while the unoccupied bands extend from 0.5 to above 5.0 eV. In TaC, the sixfold-degenerate point at the $\Gamma$ point below the Fermi level is split into one doubly degenerate and one four-degenerate point by the spin-orbit coupling, as shown in the inset of Fig. 10(b). In the lighter NbC, the SOC splitting is less evident. Also the bands along the $\Gamma$-$X$ direction are split, the maximum band splitting $E_{\rm SOC}$ being about 400 meV in TaC, which is much larger than 130 meV in NbC. In both cases, the band splitting is caused by the dominant SOC of the Ta or Nb $d$ electrons. As shown in the right panels of Fig. 10, the estimated DOS at the Fermi level is $\sim$0.74 states/eV f.u. for NbC, slightly higher than 0.64 states/eV f.u. in TaC. Both values are comparable to the experimental value calculated from the electronic specific-heat coefficient (see Sec. III F and Table I).

There are three bands crossing the Fermi level, highlighted by different colors in Fig. 11(a) for the NbC case. We depict the Fermi surface (FS) of each of these bands in Figs. 11(b)–11(d), respectively. Since TaC exhibits a similar band structure, here we show only the Fermi-surface plots of NbC. The three bands form three distinct electron FSs, one of which consists of three large cylinders along the $k_x$, $k_y$, and $k_z$ directions [see Fig. 11(b)]. Such large cylinderlike FSs originate from the hybridization between the TM $t_{2g}$ orbitals and C $p$ orbitals. The cylinderlike FSs are known to play an important role in the superconductivity of high-$T_c$ iron-based materials [52–54]. This might be also the case of NbC and TaC carbides, both of which exhibit relatively high superconducting temperatures. The other two small FSs shown in Figs. 11(c) and 11(d) are more three-dimensional-like compared to the large FS in Fig. 11(b).

![](./images/817399539395723265_11.jpg)

FIG. 10. Electronic band structures of (a) NbC and (b) TaC, calculated by considering (solid colored lines) and by ignoring (dash-dotted gray lines) the spin-orbit coupling. The $d$ orbitals in Nd or Ta and the $p$ orbitals in C are presented in blue and red colors, respectively. The inset in (b) shows the detailed band structure around the $\Gamma$ point. The total and partial (Nb or Ta and C atoms) density of states with SOC are shown on the right side of the panel. The primitive cell Brillouin zone, including the high-symmetry points, is shown on the top panel.

After inspecting the band structure (without SOC) across the whole Brillouin zone, we could identify three closed nodal loops, lying in the $k_x=0$, $k_y=0$, and $k_z=0$ planes and centered at the $\Gamma$ point. These are shown in Fig. 12 for the NbC case, with TaC displaying similar features. We recall that NbC and TaC have the same rocksalt structure, with a space group $Fm\overline{3}m$ (No. 225), characterized by three mirror planes, i.e., $m_{xy}$, $m_{yz}$, and $m_{xz}$. According to a symmetry analysis [55], the nodal loops are protected by the three mirror symmetries, since the crossing bands belong to different mirror eigenvalues. When considering SOC, the nodal loops become gapped, except for the six Dirac points $(\pm k_x, 0, 0)$, $(0, \pm k_y, 0)$, and $(0, 0, \pm k_z)$, which are protected by the $C_4$ and the combined

<table>
<caption>Table I. Normal- and superconducting-state properties of NbC and TaC, as determined from magnetization, specific-heat, and $\mu$SR measurements, as well as from electronic band-structure calculations.</caption>
<thead>
<tr>
<th>Property</th>
<th>Unit</th>
<th>NbC</th>
<th>TaC</th>
</tr>
</thead>
<tbody>
<tr>
<td>$T_c^\chi$</td>
<td>K</td>
<td>11.5</td>
<td>10.3</td>
</tr>
<tr>
<td>$T_c^C$</td>
<td>K</td>
<td>10.6</td>
<td>10.2</td>
</tr>
<tr>
<td>$\mu_0H_{c1}^\chi$</td>
<td>mT</td>
<td>10.3(3)</td>
<td>29.3(3)</td>
</tr>
<tr>
<td>$\mu_0H_{c2}^{\chi,C}$</td>
<td>T</td>
<td>1.93(1)</td>
<td>0.65(1)</td>
</tr>
<tr>
<td>$\mu_0H_{c2}^{\mu\text{SR}}$ a</td>
<td>T</td>
<td>1.81(2)</td>
<td>0.43(3)</td>
</tr>
<tr>
<td>$\xi(0)^{\chi,C}$</td>
<td>nm</td>
<td>13.1(1)</td>
<td>22.5(1)</td>
</tr>
<tr>
<td>$\gamma_n^C$</td>
<td>mJ/mol K²</td>
<td>3.0(4)</td>
<td>3.1(8)</td>
</tr>
<tr>
<td>$\Theta_D^C$</td>
<td>K</td>
<td>790(20)</td>
<td>590(20)</td>
</tr>
<tr>
<td>$\lambda_{\text{ep}}^C$</td>
<td></td>
<td>$\sim$0.60(1)</td>
<td>$\sim$0.65(3)</td>
</tr>
<tr>
<td>$N(\epsilon_\text{F})^C$</td>
<td>states/eV f.u.</td>
<td>1.3(2)</td>
<td>1.3(3)</td>
</tr>
<tr>
<td>$N_{\text{band}}(\epsilon_\text{F})^C$</td>
<td>states/eV f.u.</td>
<td>0.8(1)</td>
<td>0.8(1)</td>
</tr>
<tr>
<td>$N(\epsilon_\text{F})^\text{DFT}$</td>
<td>states/eV f.u.</td>
<td>0.74</td>
<td>0.64</td>
</tr>
<tr>
<td>$E_{\text{SOC}}^\text{DFT}$</td>
<td>meV</td>
<td>130</td>
<td>400</td>
</tr>
<tr>
<td>$\Delta_0^{\mu\text{SR}}$</td>
<td>meV</td>
<td>1.90(2)</td>
<td>1.45(1)</td>
</tr>
<tr>
<td>$\Delta_0^C$</td>
<td>meV</td>
<td>1.73(2)</td>
<td>1.54(2)</td>
</tr>
<tr>
<td>$\lambda_0^{\mu\text{SR}}$ a</td>
<td>nm</td>
<td>134(2)</td>
<td>67(1)</td>
</tr>
<tr>
<td>$\lambda_0^{\mu\text{SR}}$</td>
<td>nm</td>
<td>141(2)</td>
<td>77(1)</td>
</tr>
</tbody>
</table>

$^{\text{a}}$Derived from a fit to Eq. (1) at 1.5 K.

space-time inversion $\mathcal{PT}$ symmetry. Clearly, this is consistent with the preserved time-reversal symmetry we find from the ZF-$\mu$SR results. Since Nb atoms exhibit a weaker intrinsic

![](./images/817399539395723265_12.jpg)

FIG. 11. (a) Close-up view of the NbC electronic band structure. The bands crossing the Fermi level are highlighted in red, green, and blue. (b)–(d) Representative Fermi surfaces of NbC using the same color code of the bands shown in (a). Very similar Fermi surfaces were found also in the TaC case.

![](./images/817399539395723265_13.jpg)

FIG. 12. Nodal loops around the $\Gamma$ point in NbC, with TaC showing similar features. The color coding reflects the energy scale, indicated by the colorbar at the bottom.

SOC, we propose that NbC could be a good candidate for studying the exotic two-dimensional surface states, as well as topological superconductivity [56].

### IV. DISCUSSION

The possibilities offered by topological superconductors, ranging from hosting Majorana fermion quasiparticles to potential applications in topological quantum computing [14,15], have spurred the researchers to explore different routes in the search for materials that can realize them. One approach consists in combining conventional $s$-wave superconductors with topological insulators to form heterostructures. The resulting proximity effect between the respective surface states can lead to a two-dimensional superconducting state with $p+ip$ pairing, known to support Majorana bound states at the vortices [57]. For instance, evidence of topological SC has been reported in $\text{NbSe}_2/\text{Bi}_2(\text{Se, Te})_3$ [58,59], where $\text{NbSe}_2$ represents a typical fully gapped superconductor, while $\text{Bi}_2(\text{Se, Te})_3$ are both well-known topological insulators. Regrettably, the complexity and difficulty of fabricating such heterostructures and their relatively low superconducting transition temperatures (typically below 4 K) limit further studies and possible applications. To achieve topological superconductivity, one can also consider introducing extra carries into a topological insulator, as, e.g., in Cu intercalated $\text{Bi}_2\text{Se}_3$ [60,61]. Again, doping-induced inhomogeneities and disorder effects hinder further investigations of these doped topological insulators.

A more attractive route to attain topological superconductivity is that of combining a nontrivial electronic band structure with superconductivity in the same compound. Clearly, it is of fundamental interest to be able to identify such new superconductors with nontrivial band topology, yet with a simple composition and high transition temperatures. For

example, topologically protected surface states have been found in superconducting $\beta$-PdBi$_2$ and PbTaSe$_2$ [62,63], both representing good platforms for studying topological SC. Unfortunately, their transition temperatures are still relatively low ($< 5$ K).

In this study, we found that both NaC and TaC could be potentially interesting materials, where a nontrivial topological band structure coexists with superconductivity. By using both macroscopic and microscopic techniques, we found that the rocksalt-type NbC and TaC exhibit relatively high superconducting transitions ($T_c = 11.5$ and $10.3$ K). The low-temperature superfluid density and electronic specific heat both suggest a fully gapped superconducting state in NbC and TaC. The numerical band-structure calculations indicate that without considering the SOC effect, the first Brillouin zone contains three closed node lines in the bulk band structure, protected by time-reversal and space-inversion symmetry, which is consistent with the ZF-$\mu$SR results (see Fig. 5). When considering SOC, this picture might change. However, since SOC effects in the NbC case are rather weak, it is highly probable that the node lines are still preserved. Should this be confirmed by future investigations, considering also its relatively high $T_c$, NbC would be a very interesting topological superconductor.

## V. CONCLUSION

To summarize, we studied the superconducting properties of the NbC and TaC superconductors by means of bulk- (magnetization and heat capacity) and local-probe ($\mu$SR) techniques, as well as via numerical band-structure calculations. The superconducting state of NbC and TaC is characterized by $T_c = 11.5$ and $10.3$ K, and upper critical fields $\mu_0 H_{c2} = 1.93$ and $0.65$ T, respectively. The temperature dependence of the superfluid density and the zero-field electronic specific heat reveal a nodeless superconducting state, which is well described by an isotropic $s$-wave model. The lack of spontaneous magnetic fields below $T_c$ indicates that time-reversal symmetry is preserved in the superconducting state of NbC and TaC. Electronic band-structure calculations suggest that the density of states at the Fermi level stems primarily from the Nb (or Ta) $d$ electrons and the C $p$ electrons. The strong hybridization between the C $p$ orbitals and Nb (or Ta) $t_{2g}$ orbitals produces large cylinderlike Fermi surfaces, resembling those of high-$T_c$ iron-based superconductors. Three closed node lines are found in the first Brillouin zone, which are protected by time-reversal and inversion symmetry in the band structure of the bulk. In particular, we show that NbC is a potential candidate for future studies of topological superconductivity.

## ACKNOWLEDGMENTS

This work was supported by the Schweizerische Nationalfonds zur Förderung der Wissenschaftlichen Forschung, SNF (Grants No. 200021_169455 and No. 206021_139082). The $\mu$SR experiments were performed at the $\pi$M3 beamline of the Paul Scherrer Institute. We thank the scientists of the GPS $\mu$SR spectrometer for their support.

[1] J. Cheng and J. Luo, Pressure-induced superconductivity in CrAs and MnP, J. Phys.: Condens. Matter 29, 383003 (2017).

[2] W. Wu, J. Cheng, K. Matsubayashi, P. Kong, F. Lin, C. Jin, N. Wang, Y. Uwatoko, and J. Luo, Superconductivity in the vicinity of antiferromagnetic order in CrAs, Nat. Commun. 5, 5508 (2014).

[3] H. Kotegawa, S. Nakahara, R. Akamatsu, H. Tou, H. Sugawara, and H. Harima, Detection of an Unconventional Superconducting Phase in the Vicinity of the Strong First-Order Magnetic Transition in CrAs using $^{75}$As-Nuclear Quadrupole Resonance, Phys. Rev. Lett. 114, 117002 (2015).

[4] J.-G. Cheng, K. Matsubayashi, W. Wu, J. P. Sun, F. K. Lin, J. L. Luo, and Y. Uwatoko, Pressure Induced Superconductivity on the Border of Magnetic Order in MnP, Phys. Rev. Lett. 114, 117001 (2015).

[5] S. Park, S. Shin, S.-I. Kim, S. Kim, C.-K. Park, J. D. Thompson, and T. Park, Tunable quantum critical point and detached superconductivity in Al-doped CrAs, npj Quantum Mater. 4, 1 (2019).

[6] H. Weyl, Elektron und Gravitation. I, Z. Phys. 56, 330 (1929).

[7] S.-Y. Xu, I. Belopolski, N. Alidoust, M. Neupane, G. Bian, C. Zhang, R. Sankar, G. Chang, Z. Yuan, C.-C. Lee, S.-M. Huang et al., Discovery of a Weyl fermion semimetal and topological Fermi arcs, Science 349, 613 (2015).

[8] S.-Y. Xu, N. Alidoust, I. Belopolski, Z. Yuan, G. Bian, T.-R. Chang, H. Zheng, V. N. Strocov, D. S. Sanchez, G. Chang et al., Discovery of a Weyl fermion state with Fermi arcs in niobium arsenide, Nat. Phys. 11, 748 (2015).

[9] B. Q. Lv, H. M. Weng, B. B. Fu, X. P. Wang, H. Miao, J. Ma, P. Richard, X. C. Huang, L. X. Zhao, G. F. Chen et al., Experimental Discovery of Weyl Semimetal TaAs, Phys. Rev. X 5, 031013 (2015).

[10] N. Xu, H. M. Weng, B. Q. Lv, C. E. Matt, J. Park, F. Bisti, V. N. Strocov, D. Gawryluk, E. Pomjakushina, K. Conder et al., Observation of Weyl nodes and Fermi arcs in tantalum phosphide, Nat. Commun. 7, 11006 (2016).

[11] S. Souma, Z. Wang, H. Kotaka, T. Sato, K. Nakayama, Y. Tanaka, H. Kimizuka, T. Takahashi, K. Yamauchi, T. Oguchi et al., Direct observation of nonequivalent Fermi-arc states of opposite surfaces in the noncentrosymmetric Weyl semimetal NbP, Phys. Rev. B 93, 161112(R) (2016).

[12] B. Q. Lv, Z.-L. Feng, Q.-N. Xu, X. Gao, J.-Z. Ma, L.-Y. Kong, P. Richard, Y.-B. Huang, V. N. Strocov, C. Fang et al., Observation of three-component fermions in the topological semimetal molybdenum phosphide, Nature (London) 546, 627 (2017).

[13] J.-Z. Ma, J.-B. He, Y.-F. Xu, B. Q. Lv, D. Chen, W.-L. Zhu, S. Zhang, L.-Y. Kong, X. Gao, L.-Y. Rong, Y.-B. Huang et al., Three-component fermions with surface Fermi arcs in tungsten carbide, Nat. Phys. 14, 349 (2018).

[14] X.-L. Qi and S.-C. Zhang, Topological insulators and superconductors, Rev. Mod. Phys. 83, 1057 (2011).

[15] A. Y. Kitaev, Unpaired Majorana fermions in quantum wires, Phys. Usp. 44, 131 (2001).

[16] Z. Chi, X. Chen, C. An, L. Yang, J. Zhao, Z. Feng, Y. Zhou, Y. Zhou, C. Gu, B. Zhang et al., Pressure-induced superconductiv- ity in MoP, npj Quantum Mater. 3, 28 (2018).

[17] Z. Liu, W. Wu, Z. Zhao, H. Zhao, J. Cui, P. Shan, J. Zhang, C. Yang, P. Sun, Y. Wei et al., Superconductivity in WP single crystals, Phys. Rev. B 99, 184509 (2019).

[18] R. H. Willens, E. Buehler, and B. T. Matthias, Superconductiv- ity of the transition-metal carbides, Phys. Rev. 159, 327 (1967).

[19] K. Yamaura, Q. Huang, M. Akaishi, and E. Takayama- Muromachi, Superconductivity in the hexagonal-layered molybdenum carbide $\beta$-Mo₃C₂, Phys. Rev. B 74, 184510 (2006).

[20] C. I. Sathish, Y. Guo, X. Wang, Y. Tsujimoto, J. Li, S. Zhang, Y. Matsushita, Y. Shi, H. Tian, H. Yang et al., Superconducting and structural properties of $\delta$-MoC₀.₆₈₁ cubic molybdenum carbide phase, J. Solid State Chem. 196, 579 (2012).

[21] C. I. Sathish, Y. Shirako, Y. Tsujimoto, H. L. Feng, Y. Sun, M. Akaogi, and K. Yamaura, Superconductivity of $\delta$-MoC₀.₇₅ synthesized at 17 GPa, Solid State Commun. 177, 33 (2014).

[22] A. Huang, A. D. Smith, M. Schwinn, Q. Lu, T.-R. Chang, W. Xie, H.-T. Jeng, and G. Bian, Multiple topological electronic phases in superconductor MoC, Phys. Rev. Mater. 2, 054205 (2018).

[23] R. Zhan and X. Luo, Topologically nontrivial phases in su- perconducting transition metal carbides, J. Appl. Phys. 125, 053903 (2019).

[24] E. I. Isaev, S. I. Simak, I. A. Abrikosov, R. Ahuja, Y. K. Vekilov, M. I. Katsnelson, A. I. Lichtenstein, and B. Johansson, Phonon related properties of transition metals, their carbides, and nitrides: A first-principles study, J. Appl. Phys. 101, 123519 (2007).

[25] H. M. Tütüncü, S. Bağcı, G. P. Srivastava, and A. Akbulut, Elec- trons, phonons and superconductivity in rocksalt and tungsten- carbide phases of CrC, J. Phys.: Condens. Matter 24, 455704 (2012).

[26] K. Kavitha, G. Sudha Priyanga, R. Rajeswarapalanichamy, and K. Iyakutti, Structural stability, electronic, mechanical and superconducting properties of CrC and MoC, Mater. Chem. Phys. 169, 71 (2016).

[27] N. J. Szymanski, I. Khatri, J. G. Amar, D. Gall, and S. V. Khare, Unconventional superconductivity in 3d rocksalt tran- sition metal carbides, J. Mater. Chem. C 7, 12619 (2019).

[28] W. T. Ziegler and R. A. Young, Studies of compounds for superconductivity, Phys. Rev. 90, 115 (1953).

[29] N. Kazumasa and Y. Masatomo, Crystal structure of NaCl-type transition metal monocarbides MC (M = V, Ti, Nb, Ta, Hf, Zr), a neutron powder diffraction study, Mater. Sci. Eng. B 148, 69 (2008).

[30] W. S. Williams, Transition-metal carbides, Prog. Solid State Chem. 6, 57 (1971), and reference therein.

[31] L. E. Toth, Transition Metal Carbides and Nitrides (Academic, New York, 1971).

[32] A. Amato, H. Luetkens, K. Sedlak, A. Stoykov, R. Scheuermann, M. Elender, A. Raselli, and D. Graf, The new versatile general purpose surface-muon instrument (GPS) based on silicon photomultipliers for $\mu$SR measurements on a continuous-wave beam, Rev. Sci. Instrum. 88, 093301 (2017).

[33] A. A. Suter and B. M. Wojek, Musrfit: A free platform- independent framework for $\mu$SR data analysis, Phys. Procedia 30, 69 (2012).

[34] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett. 77, 3865 (1996).

[35] G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169 (1996).

[36] G. Kresse and J. Furthmüller, Efficiency of ab-initio total en- ergy calculations for metals and semiconductors using a plane- wave basis set, Comput. Mater. Sci. 6, 15 (1996).

[37] G. Kresse and D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59, 1758 (1999).

[38] P. E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50, 17953 (1994).

[39] J. Rodríguez-Carvajal, Recent advances in magnetic struc- ture determination by neutron powder diffraction, Phys. B (Amsterdam, Neth.) 192, 55 (1993).

[40] N. R. Werthamer, E. Helfand, and P. C. Hohenberg, Tempera- ture and purity dependence of the superconducting critical field, $H_{c2}$. III. electron spin and spin-orbit effects, Phys. Rev. 147, 295 (1966).

[41] X. Zhu, H. Yang, L. Fang, G. Mu, and H.-H. Wen, Upper critical field, Hall effect and magnetoresistance in the iron- based layered superconductor LaFeAsO₀.₉F₀.₁−δ, Supercond. Sci. Technol. 21, 105001 (2008).

[42] M. Tinkham, Introduction to Superconductivity, 2nd ed. (Dover, Mineola, NY, 1996).

[43] R. Kubo and T. Toyabe, A stochastic model for low field resonance and relaxation, in Magnetic Resonance and Relax- ation, edited by R. Blinc (North-Holland, Amsterdam, 1967), pp. 810–823.

[44] A. Yaouanc and P. D. de Réotier, Muon Spin Rotation, Re- laxation, and Resonance: Applications to Condensed Matter (Oxford University Press, Oxford, 2011).

[45] A. Grassellino, C. Beard, P. Kolb, R. Laxdal, N. S. Lockyer, D. Longuevergne, and J. E. Sonier, Muon spin rotation studies of niobium for superconducting rf applications, Phys. Rev. ST Accel. Beams 16, 062002 (2013).

[46] W. Barford and J. M. F. Gunn, The theory of the measurement of the London penetration depth in uniaxial type II superconduc- tors by muon spin rotation, Phys. C (Amsterdam, Neth.) 156, 515 (1988).

[47] E. H. Brandt, Properties of the ideal Ginzburg-Landau vortex lattice, Phys. Rev. B 68, 054506 (2003).

[48] A. Maisuradze, R. Khasanov, A. Shengelaya, and H. Keller, Comparison of different methods for analyzing $\mu$SR line shapes in the vortex state of type-II superconductors, J. Phys.: Condens. Matter 21, 075701 (2009), and references therein.

[49] A. Carrington and F. Manzano, Magnetic penetration depth of MgB₂, Phys. C (Amsterdam, Neth.) 385, 205 (2003).

[50] C. Kittel, Introduction to Solid State Physics, 8th ed. (Wiley, Hoboken, NJ, 2005).

[51] W. L. McMillan, Transition temperature of strong- coupled superconductors, Phys. Rev. 167, 331 (1968).

[52] I. I. Mazin, D. J. Singh, M. D. Johannes, and M. H. Du, Uncon- ventional Superconductivity with a Sign Reversal in the Order

214518-10

Parameter of LaFeAsO$_{1-x}$F$_x$, Phys. Rev. Lett. **101**, 057003 (2008).

[53] K. Kuroki, H. Usui, S. Onari, R. Arita, and H. Aoki, Pnictogen height as a possible switch between high-$T_c$ nodeless and low-$T_c$ nodal pairings in the iron-based superconductors, Phys. Rev. B **79**, 224511 (2009).

[54] I. I. Mazin, M. Shimizu, N. Takemori, and H. O. Jeschke, Novel Fe-Based Superconductor LaFe$_2$As$_2$ in Comparison with Traditional Pnictides, Phys. Rev. Lett. **123**, 267001 (2019).

[55] M. Zeng, C. Fang, G. Chang, Y.-A. Chen, T. Hsieh, A. Bansil, H. Lin, and L. Fu, Topological semimetals and topological insulators in rare earth monopnictides, arXiv:1504.03492.

[56] J. Zhao, R. Yu, H. Weng, and Z. Fang, Topological node-line semimetal in compressed black phosphorus, Phys. Rev. B **94**, 195104 (2016).

[57] L. Fu and C. L. Kane, Superconducting Proximity Effect and Majorana Fermions at the Surface of a Topological Insulator, Phys. Rev. Lett. **100**, 096407 (2008).

[58] S.-Y. Xu, N. Alidoust, I. Belopolski, A. Richardella, C. Liu, M. Neupane, G. Bian, S.-H. Huang, R. Sankar, C. Fang *et al.*, Momentum-space imaging of Cooper pairing in a half-Dirac-gas topological superconductor, Nat. Phys. **10**, 943 (2014).

[59] J.-P. Xu, C. Liu, M.-X. Wang, J. Ge, Z.-L. Liu, X. Yang, Y. Chen, Y. Liu, Z.-A. Xu, C.-L. Gao *et al.*, Artificial Topological Superconductor by the Proximity Effect, Phys. Rev. Lett. **112**, 217001 (2014).

[60] Y. S. Hor, A. J. Williams, J. G. Checkelsky, P. Roushan, J. Seo, Q. Xu, H. W. Zandbergen, A. Yazdani, N. P. Ong, and R. J. Cava, Superconductivity in Cu$_x$Bi$_2$Se$_3$ and its Implications for Pairing in the Undoped Topological Insulator, Phys. Rev. Lett. **104**, 057001 (2010).

[61] S. Sasaki, M. Kriener, K. Segawa, K. Yada, Y. Tanaka, M. Sato, and Y. Ando, Topological Superconductivity in Cu$_x$Bi$_2$Se$_3$, Phys. Rev. Lett. **107**, 217001 (2011).

[62] S.-Y. Guan, P.-J. Chen, M.-W. Chu, R. Sankar, F. Chou, H.-T. Jeng, C.-S. Chang, and T.-M. Chuang, Superconducting topological surface states in the noncentrosymmetric bulk superconductor PbTaSe$_2$, Sci. Adv. **2**, e1600894 (2016).

[63] M. Sakano, K. Okawa, M. Kanou, H. Sanjo, T. Okuda, T. Sasagawa, and K. Ishizaka, Topologically protected surface states in a centrosymmetric superconductor $\beta$-PdBi$_2$, Nat. Commun. **6**, 8595 (2015).