Chemical Science

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: J. He, W. Fang and R. Long, *Chem. Sci.*, 2019, DOI: 10.1039/C9SC02353D.

![](./images/812736478948884480_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the Information for Authors.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the Ethical guidelines still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/812736478948884480_2.jpg)
rsc.li/chemical-science

# Unravelling the Effects of Oxidation State of Interstitial
Iodine and Oxygen Passivation on Charge Trapping and
Recombination in $\text{CH}_3\text{NH}_3\text{PbI}_3$ Perovskite: A Time-Domain
Ab Initio Study

Jinlu He, Wei-Hai Fang, Run Long*

College of Chemistry, Key Laboratory of Theoretical & Computational
Photochemistry of Ministry of Education, Beijing Normal University, Beijing, 100875,
P. R. China

ABSTRACT: Understanding of nonradiative charge recombination mechanisms is prerequisites for advancing perovskite solar cells. By performing time-domain density functional theory combined with nonadiabatic (NA) molecular dynamics simulations, we show that electron-hole recombination in perovskites strongly depends on the oxidation state of interstitial iodine and oxygen passivation. The simulations demonstrate that electron-hole recombination in $\text{CH}_3\text{NH}_3\text{PbI}_3$ occurs on several nanoseconds, agreeing well with experiment. The negative interstitial iodine delays charge recombination by a factor of 1.3. The deacceleration is attributed to the fact that interstitial iodine anion forms chemical bond with its nearest lead atoms, eliminates trap state, and decreases the NA electron-phonon coupling. The positive interstitial iodine attracts its neighbouring lattice iodine anions, resulting in formation of a I-trimer and producing an electron trap. Electron trapping proceeds on very fast time scale, tens of

* Corresponding author, E-mail: runlong@bnu.edu.cn

picoseconds, and captures majority of free electron for recombining with free hole directly while inhibits the recombination of free electron and hole, delaying the recombination by a factor of 1.5. However, the positive interstitial iodine easily converts to a neutral iodine defect by capturing an electron, giving rising to a singly occupied state above the valence band maximum, and acting as a hole trap. Photoexcitation valence band hole gets trapped by hole trap state very rapidly, follows by acceleration in recombination with conduction band free electron by a factor of 1.6. Surprisingly, molecular oxygen interacting with interstitial iodine anion forms a stable $IO_3^{-1}$ species, which inhibits ion migration, stabilizes perovskites, and suppresses the electron-hole recombination by a factor of 2.7. Our simulations reveal the microscopic effects of oxidation state of interstitial iodine defects and oxygen passivation in perovskites, suggesting an effective way to improve perovskite photovoltaic and optoelectronic devices.

Keywords: hybrid organic-inorganic perovskites; interstitial iodine defect; oxidation state; oxygen doping; charge trapping and recombination; nonadiabatic molecular dynamics; time-dependent density functional theory

### 1. Introduction

Lead halide perovskites (LHPs) $APbX_3$ ( $A = CH_3NH_3$, $CH(NH_2)_2$; $X = Cl$, $Br$, $I$) have received numerous attention in the past decades due to their outstanding electronic and optical properties,¹ including excellent optical absorption,² long minority carrier lifetimes and diffusion lengths,³⁻⁵ and appropriate optical band gaps.⁶ These fascinating properties make the LHPs possess great potential in a broad range of applications, such as solar cells,⁷⁻¹⁰ photodetector,¹¹ optically pumped lasers,¹² light-emitting diodes¹³ and photocatalytic water-splitting assemblies¹⁴ Utilization as a s solar cell attracts particular concern arising due to the rapid growing power conversion efficiencies (PCEs) from $3.8\%^{15}$ to certified $24.2\%$ within ten years,¹⁶ showing a comparable value to the commercial silicon solar cells.¹⁷ However, the PCEs are still lower than the Shockley-Queisser limit¹⁸ of a single p-n junction solar cell due to the presence of channels for nonradiative charge and energy losses causing by various intrinsic and extrinsic defects.¹⁹⁻²¹

Intrinsic defects are inevitable in low-temperature solution processed LHPs due to the low stability against thermal- and light-irradiation.²² Dozens of experimental and theoretical works have explored the roles played by a large number of native point defects in LHPs,²⁰, ²³⁻³⁰ and found those defects have significant impact on the performance of perovskite solar cells by control of the quality of films and carrier dynamics.³¹⁻³⁴ The sample quality can be directly detected by advanced experimental techniques, such as atomic force microscopy and scanning electron microscopy. However, photoinduced charge dynamics can be only measured via indirect

spectroscopy methods while remains their nature largely elusive. $^{35,36}$

Interstitial iodine defects are common and active deep traps in $MAPbI_{3},^{37}$ which easily form in the presence of excess iodine conditions. $^{37}$ The impacts of interstitial iodine defects on the electronic structure and charge dynamics of perovskites are under active research and debate. Petrozza and coauthors have shown that a neutral interstitial iodine defect can trap a conduction band (CB) electron followed by subsequently recombining with valence band (VB) hole on a surprising long time scale using photoluminescence spectroscopy, leading to a significantly increased carrier lifetime and an enhanced open circuit voltage of $MAPbI_{3}$ perovskite solar cells. $^{32}$ However, Yang et al. have demonstrated that excess iodine can suppress the formation of interstitial iodide defects and extend the carriers lifetimes. $^{38}$ On the contrary, Wang et al. have demonstrated that interstitial iodine defects notably decrease carrier lifetimes and lower the photovoltaic performance of $MAPbI_{3}$ perovskite solar cells. $^{39}$ The positive and negative effects of interstitial iodine defects on the excited charge carriers' lifetimes of $MAPbI_{3}$ perovskite may be related with their oxidation state. First-principles calculations have predicted that positive interstitial iodine $(I_{i}^{+1})$ is unstable under light irradiation condition $^{37}$ because which tends to trap an electron resulting in formation of an neutral interstitial iodine $(I_{i})$ that acts as a deep trap state, $^{25}$ accelerating electron-hole recombination. $^{28,38,40}$ In addition, the interstitial iodine defects have low migration activation energies (0.1 eV) and they easily diffuse in perovskites, which constitutes the main factor resulting in perovskite materials degradation. $^{41,42}$ In contrast, negative interstitial iodine $(I_{i}^{-1})$ is relatively stable. $^{37}$ While the ion migration, including

both MA+ and I-, leads to notable current–voltage hysteresis of a perovskite solar cell. $^{43}$

Interestingly, theoretical calculations have illustrated that oxygen preferentially interacts with the interstitial iodine anion rather than lattice iodine atom, forming thermodynamically stable $IO_3^-$ species, $^{44}$ potentially stabilizes the $MAPbI_3$ perovskite$^{44}$ and rationalizes the improved perovskite solar cell performance as well as clarifies the enhanced reversible photoluminescence quantum yield upon material exposure to oxygen in experiments. $^{45-49}$ In order to understand the underlined mechanisms for the impact of oxidation state of interstitial iodine and oxygen passivation effect on the excited-state lifetimes of $MAPbI_3$ perovskite, it calls a time-domain study of nonradiative electron-hole recombination in the real time and at the atomistic level.

![](./images/812736478948884480_3.jpg)

Fig. 1 Investigated charge trapping and electron-hole recombination processes in (a) pristine $MAPbI_3$, $I_i^{-1}$, and $IO_3^{-1}$, (b) $I_i$, and (c) $I_i^{+1}$. ① photoexcitation generates electrons and holes across the band gap. ② Nonradiative electron-hole recombination between CMB and VBM. ③ hole trapping from VBM to trap state. ④ Recombination of trapped holes with electrons in the CBM. ⑤ electron trapping from CBM to trap state. ⑥

# Recombination of trapped electrons with holes in the VBM.

Motivated by both the experimental³², ³⁸, ³⁹, ⁴⁵⁻⁴⁹ and theoretical works²⁵, ³⁷, ⁴⁴ showing that positive and negative effects of interstitial iodine on photoexcitation carrier lifetimes of MAPbI₃ as well as the role plays by oxygen passivation, we have investigated the charge trapping and nonradiative electron-hole recombination processes (depicted in Fig. 1) of MAPbI₃ in the presence of interstitial iodine defects with different oxidation state Iᵢ, Iᵢ⁻¹, and Iᵢ⁺¹ as well as oxygen passivation with the stable species IO₃⁻¹,⁴⁴ using a combination of real-time time-dependent density functional theory (TD-DFT)⁵⁰, ⁵¹ and nonadiabatic molecular dynamics (NAMD).⁵²⁻⁵⁵ Our simulations show that the electron–hole recombination across the conduction band minimum (CBM) and valence band maximum (VBM) (Fig. 1a) in pristine MAPbI₃ occurs on several nanoseconds, agreeing well with experimental data.⁵⁶ The neutral Iᵢ acts as an electron donor, creates a hole trap above the VBM (Fig. 1b), increases NA coupling, and accelerates the electron–hole recombination by a factor of 1.6. The negatively charged Iᵢ⁻¹ defect eliminates the trap state (Fig. 1a) and decreases the electron-hole recombination across the CBM-VBM energy gap by a factor of 1.3 compared to the pristine MAPbI₃, arising due to reduced NA electron-phonon coupling. The Iᵢ⁺¹ defect introduces an electron trap below the CBM (Fig. 1c), acts an electron acceptor. The CB free electrons are highly captured by the trap state, followed by recombining with the holes locating in VBM. The trap-assisted electron-hole recombination between the VBM and the trap state delays by a factor of 1.5 relative to the pristine MAPbI₃. While positively charged interstitial iodine is easily to convert to

a neutral defect by capturing an electron, accelerating electron-hole recombination.

Molecular oxygen interacting with $I_i^{-1}$ defect forms a stable $IO_3^{-1}$ that inhibits ion migration and reduce current-voltage hysteresis. At the same time, oxygen passivation decreases the NA electron-phonon coupling further, and suppresses electron-hole recombination across the band gap (Fig. 1a) by a factor of 2.7. This study reveals the impact of oxidation state of interstitial iodine defects on charge dynamics and rationalizes the phenomenon observed in the experiment that oxygen can be responsible for the enhanced perovskite solar cells performance and PLQY$^{45-49}$ and reduced hysteresis, $^{57}$ providing valuable guidelines for design of high-performance perovskite photovoltaic devices.

### 2. Theoretical Methodology

We have performed the NAMD with the decoherence induced surface hopping (DISH) technique$^{58}$ implemented within TD-DFT in Kohn-Sham representation, $^{50,59}$ to simulate the charge carrier trapping and recombination processes in $MAPbI_3$, $I_i$, $I_i^{-1}$, $I_i^{+1}$, and $IO_3^{-1}$ systems. Since the nuclei are heavier and slower than electrons, thus we describe the nuclei and electrons with (semi)classical and quantum mechanics, respectively. The DISH algorithm provides the physical mechanism for the trajectory branching, and surface hops occur at decoherence events. Because phonon-induced loss of quantum coherence time is greatly shorter than electron-hole recombination time, and therefore it is needed to incorporate the effect of decoherence into the NAMD simulations. $^{60-62}$ The decoherence time is analogy to the pure-dephasing time in the

optical response theory that can be obtained by the second-order cumulant approximation.⁶³ The approach has been used to study the photoexcitation charge dynamic in a broad range of systems,⁶⁴⁻⁷² including perovskites,⁶⁴⁻⁶⁹,⁷¹ TiO₂ contacting with graphene quantum dot interface,⁷² and black phosphorus.⁷⁰ A detailed description of the approach can be found in the references.⁵²,⁵³

A 192-atom $2 \times 2 \times 1$ tetragonal⁷³ supercell to represent the pristine MAPbI₃. The neutral $I_i$ structure is obtained by adding an iodine atom colored in green into pristine MAPbI₃ system. The $I_i^{-1}$ and $I_i^{+1}$ systems are created via adding and removing an electron into/from the $I_i$ structure. Introducing $3/2$ O₂ into the $I_i^{-1}$ structure, we obtain the $IO_3^{-1}$ system. Geometry optimization, adiabatic MD, and NA coupling calculations are carried out with the Vienna ab initio Simulation Package (VASP)⁷⁴. The electron exchange-correlation effect is described with the Perdew–Burke–Ernzerhof (PBE) functional,⁷⁵ and the electron-ion cores interactions are treated with the projected-augmented wave (PAW) method.⁷⁶ The energy cutoff of 400 eV is used to converge the total energy during geometry optimization with a $\Gamma$-centered $2\times2 \times2$ Monkhorst-Pack k-mesh.⁷⁷ The adiabatic MD trajectory and NA couplings are obtained at $\Gamma$-point because the direct bandgaps for all of five systems are at the $\Gamma$-point. In order to capture the weak van der Waals interactions interactions within the perovskites, Grimme's DFT-D3 correction approach is used.⁷⁸

After the geometry is optimized at 0 K, the five systems are heated to 300 K via velocity rescaling to 2 ps. Then, we obtained 6 ps adiabatic MD trajectories within the microcanonical ensemble simulations with a 1 fs atomic time step. In order to study the

charge carrier trapping and recombination dynamics in the five systems, the first 4000 geometries of the 6 ps adiabatic MD trajectories were chosen as initial configurations for the NAMD simulations. During the NAMD simulations, the calculated energy gap 1.65 eV of pristine MAPbI₃ is scaled to experimental value of 1.61 eV⁷⁹ by subtracting a constant. The energy gaps of Iᵢ, Iᵢ⁻¹, Iᵢ⁺¹ and IO₃⁻¹ systems are subtracted the same constant. Because electron-hole recombination in perovskites occurs typically ranging from several nanoseconds to microseconds, it is a consumed task to solve the time-dependent Schrödinger equation on these time scales. Therefore, we run short-time NAMD simulations for each pair of states, obtain rate constant for in each process depicted in Fig. 1. Then, we construct the coupled equations and which are shown in Supporting Information (SI), solve these equations using the obtained the rate constants and get the long time-evolution populations of each state participated in the carrier relaxation. The details of the coupled kinetics equations and their solutions are presented in SI.

## 3. Results and Discussion
We firstly focus on MAPbI₃, and MAPbI₃ containing interstitial iodine defects with all charged states (-1, 0, +1). The discussion starts with geometric structure and thermal fluctuations, follows by electronic structures, electron-vibrational interactions, and ends on charge trapping and recombination dynamics. Then, we investigate the effect of oxygen passivation on the geometry and charge dynamics of IO₃⁻¹ system and find oxygen passivation can simultaneously inhibit ion migration and charge

recombination.

### 3.1 Geometric Structure and Thermal Fluctuations

The optimized geometries of pristine $MAPbI_3$ and $MAPbI_3$ containing $I_i$, $I_i^{-1}$ and $I_i^{+1}$ are shown in Fig. 2a-d. The interstitial iodine atom and its nearest iodine and lead atoms are highlighted by green, red, and yellow spheres, and corresponding I-I and I-Pb distance of the optimized geometry (number in parentheses) and their canonically averaged distances (number outside) as well as whose time-evolution distances along the 6 ps trajectory are shown in Fig. 2 e and f. The inorganic I-Pb lattices are relatively rigid, while the MA cations are soft. In pristine $MAPbI_3$, the MA cations are orderly arranged. Interstitial iodine atom gives rise to a small distortion of the I-Pb octahedrons around it and most of the MA cations have rotated by different angles in the $I_i$, $I_i^{-1}$ and $I_i^{+1}$ systems. Neutral $I_i$ forms an I-Pb chemical bond that pulls the interstitial iodine away from the lattice iodine, increasing the I-I distance to 3.291 Å at 0 K and 3.954 Å at 300 K (Fig. 2e). Negative $I_i^{-1}$ repels the lattice iodine anion because they carry same charge with an increased I-I distance of 3.928 Å at 0 K and 4.002 Å at 300 K, while attracts lattice lead cation forms a I-Pb bond. On the contrary, positive $I_i^{+1}$ repels the neighboring lead atom while tends to attract lattice iodine anions resulting in formation of a I-trimer. The bond lengths between the interstitial iodine and two adjacent iodides are close to each other at both 0 K and 300 K. Shown in Fig. 2f, the I-Pb distance is 3.229 Å in the $I_i$ system while decreases slightly to 3.075 Å in the $I_i^{-1}$ system and increases notably to 4.511 Å in the $I_i^{+1}$ system at 0 K. The canonically averaged I-Pb distances become 3.147 Å, 3.137 Å and 4.526 Å in the $I_i$, $I_i^{-1}$ and $I_i^{+1}$ systems,

respectively. The I-Pb distance of the $I_i^{-1}$ system is shorter than that in the $I_i$ system
because the negatively charged interstitial iodine defect attracts the Pb cation.

Alternatively, the I-Pb distance of the $I_i^{+1}$ system is longer than that in the $I_i$ system,
arising due to the positively interstitial iodine defect pushing away the Pb cation in the
presence of repulsive force between them.

In addition to the reported I-I and I-Pb distances, we computed the root-mean-
square displacement velocity of atoms in the four systems to investigate the influence
of oxidation state of interstitial iodine defect on atomic fluctuations with thermal impact,
by separating the atoms into organic (MA) and combined inorganic species (Pb and I).
In order to explore further the effect of the defects, we differentiate the interstitial iodine
atom from lattice Pb and I atoms in the defective systems (Table 1). The computed data
show that interstitial iodine defect in all charged states accelerate the motion of all
atoms in the order $I_i^{+1} > I_i^{-1} > I_i$ compared to pristine $MAPbI_3$. The sequence of the
motions of both organic MA atoms and inorganic Pb/I atoms retains same to all atoms,
attributed to the correlated motions of organic and inorganic parts. The stronger motion
in the defective systems than the pristine $MAPbI_3$ indicates that the interstitial iodine
defects lower the stability of perovskites, in particular the instability primarily
originates from the distortion of the inorganic I-Pb octahedrons due to their notably
increased motions compared to the organic MA cations. The situation becomes stronger
in the charged systems ($I_i^{+1}$, $I_i^{-1}$) compared to the neutral interstitial iodine system ($I_i$),
rationalizing the larger migrations of iodine ions than iodine atoms.⁴¹, ⁴³, ⁸⁰⁻⁸² The
analysis provides an excellent explanation for that interstitial iodine defects

significantly degrade perovskite films exposure to light- or thermal-irradiation.

**Table 1. Root-Mean-Square Velocity (Å/fs) of Atomic Positions in Pristine MAPbI₃,
Iᵢ, Iᵢ⁻¹, Iᵢ⁺¹ and IO₃⁻¹ Systems.**

<table>
  <thead>
    <tr>
      <th></th>
      <th>totalᵃ</th>
      <th>MAᵇ</th>
      <th>Pb-Iᶜ</th>
      <th>Pb-Iᵈ</th>
      <th>Iᵉ</th>
      <th>Oᶠ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MAPbI₃</td>
      <td>0.0342</td>
      <td>0.0469</td>
      <td>0.0128</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Iᵢ</td>
      <td>0.0352</td>
      <td>0.0481</td>
      <td>0.0141</td>
      <td>0.0142</td>
      <td>0.0059</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Iᵢ⁻¹</td>
      <td>0.0356</td>
      <td>0.0487</td>
      <td>0.0140</td>
      <td>0.0141</td>
      <td>0.0066</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Iᵢ⁺¹</td>
      <td>0.0374</td>
      <td>0.0509</td>
      <td>0.0152</td>
      <td>0.0153</td>
      <td>0.0060</td>
      <td>-</td>
    </tr>
    <tr>
      <td>IO₃⁻¹</td>
      <td>0.0300</td>
      <td>0.0409</td>
      <td>0.0130</td>
      <td>0.0131</td>
      <td>0.0055</td>
      <td>0.0061</td>
    </tr>
  </tbody>
</table>

![](./images/812736478948884480_4.jpg)

Fig. 2 Optimized geometry of (a) pristine $MAPbI_3$, (b) $I_i$, (c) $I_i^{-1}$ and (d) $I_i^{+1}$. The interstitial iodine atom and its nearest iodine and lead atoms are colored in green, red and yellow, respectively. (e) Evolution of the interested I-I distances in the $I_i$, $I_i^{-1}$ and $I_i^{+1}$ systems. The number outside and inside parentheses denotes canonically averaged distance between the interstitial iodine and its nearest iodine along the 6 ps MD trajectory, as well as in the optimized structure, respectively. (f) Interested I-Pb distances at 0 K and 300 K as depicted in (e).

### 3.2 Electronic Structure

Part a-d of Fig. 3 shows the projected density of states (PDOS) of the pristine

$MAPbI_3$, $I_i$, $I_i^{-1}$ and $I_i^{+1}$ systems, reflecting how the oxidation state of interstitial iodine affects the electronic structure. The charge densities of the key states involving charge trapping and recombination are displayed in the insets of Fig. 3. The PDOSs are split into MA, iodine and lead species. Apparently, VBM and CBM are mainly supported by iodine orbitals and lead orbitals, respectively. This situation favors weak NA coupling due to small overlap between electron and hole wave functions according to the definition of NA electron-phonon coupling:

$$
d_{i j}=-i \hbar\left\langle\left|\phi_{i}\right| \nabla_{\boldsymbol{R}}\left|\phi_{j}\right\rangle \cdot \dot{\boldsymbol{R}}=-i \hbar\left\langle\phi_{i}\left|\frac{\partial}{\partial t}\right| \phi_{j}\right\rangle\right. \tag{1}
$$

NA electron-phonon coupling arises due to the interaction between electronic and nuclear vibrational motions. The mixing of two wave functions of initial and final states directly determines the strength of NA coupling, $d_{ij}$. It is because inorganic iodine and lead atoms primarily create the electron-phonon coupling, leading to low electron-hole recombination rate. The organic MA species do not contribute to the band edges while they simultaneously affect NA coupling in an indirect way and stabilize the perovskite structure by filling the inorganic cages. The calculated bandgap of pristine $MAPbI_3$ is 1.65 eV (Fig. 3a), agreeing well with the experimental data$^{79}$ and DFT calculated values.$^{83, 84}$ Introduction of interstitial iodine for all charged states (0, -1, +1) into the pristine $MAPbI_3$ has little influence on the bandgaps of the defective systems (Fig. 3b-d).

The neutral $I_i$ defect creates a half-occupied trap state that is close to the VBM (Fig. 3b). Thus, it can trap holes or electrons but the two processes cannot happen simultaneously due to Pauli exclusion principle. Since the trap state is near the VBM

that has strong NA coupling between the trap state and VBM due to a small energy gap,
resulting in hole trapping is a major process. The trapped hole is populated resulting in
that the $I_i$ acts as a p-type dopant and introduces positive charge carriers near the VBM.
As a result, photoexcited CB electrons can recombine with holes residing in both the
VB and the trap state. The gap state is mainly localized on the interstitial iodine defect
(inset of Fig. 3b). The increased charge density of VBM enhances the overlap between
the VBM and CBM, strengthening the NA coupling between them compared to that in
the pristine system.

The negatively charged iodine anion creates no gap state in the $I_i^{-1}$ system (Fig.
3c). The interstitial iodine anion and lead cation form a strong I-Pb chemical bond,
eliminating the unsaturated dangling bonds and moving the gap states into the VB.
Iodine anion decreases the electron wave functions around itself while leaves the hole
wave functions largely unchanged (inset of Fig. 3c), and therefore, reducing their
overlap, lowering NA electron-phonon coupling.

The positively charged iodine cation creates a trap state below the CBM in the $I_i^{+1}$
system (Fig. 3d). The unoccupied trap state can play as an electron acceptor, leading to
that the $I_i^{+1}$ act as a n-type dopant, and produces negative charge carriers near the CBM.
Because interstitial iodine cation and lattice iodine anions attract each other and form a
I-trimer, and therefore, producing the electron trap state. Apparently, the I-trimer
localizes the charge density on itself (inset of Fig. 3d), and which also notably disturbs
the I-Pb octahedrons and simultaneously decrease the charge densities of VBM and
CBM (inset of Fig. 3d), and in particular for the CBM, lowering NA coupling between

them further with respect to the pristine and $I_i^{-1}$ systems. Consequently, the photoexcited holes can recombine with the electrons locating on both the CB and trap state. Because the energy gap between the trap state and the CBM is small, the electron trapping is expected to proceed very fast.

The analysis derived from Fig. 3 demonstrates that iodine chemistry has a significant influence on the electronic structure, and thus, on the charge trapping and recombination dynamics in perovskites.

![](./images/812736478948884480_5.jpg)

Fig. 3 PDOSs of (a) pristine MAPbI₃, (b) $I_i$, (c) $I_i^{-1}$ and (d) $I_i^{+1}$ systems. The insets show the charge densities of the key electronic states involve in the charge trapping and recombination.

### 3.3 Electron-Vibrational Interactions

In order to identify the phonon modes that couple to electronic subsystem and induce quantum transitions between the key pairs of states, we compute the influence

spectrum by performing Fourier transforms (FTs) of the fluctuations of energy gaps.

The intensity of each peak in the FTs marks the strength of electron-vibrational coupling at a given phonon frequency. Fig. 4 shows that low-frequency modes dominate spectral density because they come from the slow lead and iodine atoms that contribute to the CBM, trap state, and VBM. The major peaks around $100\ \text{cm}^{-1}$ and below can be attributed to the I-Pb stretching and bending motions that create the majority of NA electron-phonon coupling.⁸⁵ ⁸⁶ The phonon modes at $130$–$170\ \text{cm}^{-1}$ can be interpreted as the librations of the organic cations. The peak around $200\ \text{cm}^{-1}$ can be contributed to the torsional mode of the MA cations.⁸⁶ It is reasonable that phonon modes originating from the MA cations are presented because they can indirectly influence the electron-phonon coupling though electrostatic interactions. Interstitial iodine defects break lattice symmetry, produce localized state, and create high frequency modes.

The pure-dephasing times, summarized in Table 2, are computed using the second-order cumulant approximation of the optical response theory.⁶³ Quantum transition between a pair of states requires formation of coherent superposition states via NA electron-phonon coupling. Short-lived superpositions facilitate slow dynamics, which can be interpreted by quantum Zeno effect in the limit of infinitely fast of loss of coherence.⁸⁷ The around 10 fs decoherence times are significantly shorter than the electron-hole recombination times that take place on several nanoseconds in the $\text{MAPbI}_3$ perovskite.⁵⁶ Thus, it is essential to consider the decoherence effect during the NAMD simulation.⁸⁸ The short pure-dephasing times provide a reasonable explanation

for the fact that perovskite materials have long excited state lifetimes, rationalizing the high performance of perovskite solar cells.

![](./images/812736478948884480_6.jpg)

Fig. 4 Spectral density obtained from Fourier transforms of the autocorrelation functions for the energy gap fluctuation of pair of electronic states in (a) pristine MAPbI₃, (b) Iᵢ, (c) Iᵢ⁻¹ and (d) Iᵢ⁺¹ systems.

### 3.4 Charge Trapping and Recombination
Next, we analyze the charge trapping and recombination processes depicted in Fig. 1 for the pristine MAPbI₃, Iᵢ, Iᵢ⁻¹ and Iᵢ⁺¹ systems. The time-evolution populations of key states are shown in Fig. 5. The time scales reported in Fig. 5 are obtained by fitting the data with an exponential function, $P(t) = exp\left(-\frac{t}{\tau}\right)$. The rise and decay components in the populations of trap states are fitted separately. The rate constants summarized in Table 2 are obtained by fitting the data shown in the SI with short-time NAMD simulations for each pair of states. The data presented in Fig. 5 are solutions of kinetics

equations (SI) with the rate constants given in Table 2. The calculated time scales show that oxidation state of interstitial iodine has strong influence on the charge trapping and recombination time scales in perovskites. In particular, charge carrier lifetime decreases as a sequence: $I_{i}^{+1}>I_{i}^{-1}>MAPbI_{3}>I_{i}$.

![](./images/812736478948884480_7.jpg)

Fig. 5 Evolution of populations of the key states for charge trapping and recombination in (a) pristine $MAPbI_{3}$, (b) $I_{i}$, (c) $I_{i}^{-1}$ and (d) $I_{i}^{+1}$ systems.

The electron-hole recombination in the pristine $MAPbI_{3}$ occurs on several nanoseconds (Fig. 5a), agreeing well with the experimental data.⁵⁶ The long lifetime is attributed to the small NA coupling (1.02 meV) and short pure-dephasing time (10.8 fs). The electron-phonon coupling is small because the CBM and VBM are supported by lead and iodine atoms, Fig. 3a. The neutral $I_{i}$ accelerates electron-hole recombination

because trap state provides new relaxation pathways (Fig. 5b). The trap state is across the Fermi level and above the VBM and is capable of trapping a photoexcited VB hole on tens of picoseconds due to a strong NA coupling of 3.10 meV. Once tapped, the hole can recombine with a CB electron on one nanosecond. Overall, the electron-hole recombination in the $I_i$ system is accelerated by a factor of 1.6 compared with the pristine system. On the other hand, the occurrence of electron trapping is unlikely because the trap state is away from the CBM and the NA coupling between the states is small, 1.16 meV, leading to the event of CB electrons directly recombining with the VB holes is highly impossible to take place because the process is 15 times slower than the hole trapping, Figure S14 in SI. Therefore, neutral interstitial iodine accelerates the charge recombination via hole trap-assisted carrier relaxation pathways.

The negatively charged $I_i^{-1}$ and positively charged $I_i^{+1}$ defect suppress the electron-hole recombination by a factor of 1.3 (Fig. 5c) and 1.5 (Fig. 5d), respectively, operating by different mechanism. The $I_i^{-1}$ does not produce mid-gap state (Fig. 3c), and possesses smaller NA electron-phonon coupling (0.83 meV) and comparable pure-dephasing time with respect to the pristine MAPbI₃. Decrease in NA coupling because the negatively interstitial iodine induces local geometry distortion and lowers electron wave functions, inset of Fig. 3c. The positively charged $I_i^{+1}$ creates a trap state below the CBM, and which can rapidly trap a CB electron on tens of picoseconds due to large NA coupling, 2.12 meV. Once trapped, the VB hole can recombine with the trapped electron and a CB electron on similar time scale of sub-3 nanoseconds. One should note that a direct electron-hole recombination between the CBM and VBM is negligible in the presence

of $I_{i}^{+1}$ defect because most of electrons are trapped by the defect, followed by electron-hole recombination between the trap state and VBM. The deacceleration in recombination is because the NA coupling (0.56 meV) reduces and pure-dephasing accelerates (Fig. 3 and Table 2). As a result, both negative and positive interstitial iodine can inhibit charge recombination and extend excited charge carriers' lifetimes. However, previous calculations show that $I_{i}^{+1}$ is easily to capture an electron and converts to a neutral interstitial iodine, $^{37}$ accelerating charge recombination and decreasing excited-state lifetime. $^{38,40}$ As a result, $I_{i}^{-1}$ is the most possible interstitial iodine defect responsible for an extended excited-state lifetime and an enhanced solar cell performance. $^{32}$ However, the mobile MA and I ions lead to unusual phenomena in LHP materials and optoelectronic/photovoltaic devices, such as current-voltage hysteresis and switchable photovoltaic effect, and degenerate the performance of devices. $^{43}$

### 3.5 Oxygen Passivation Effect
Finally, we consider the effect of oxygen passivated negatively charged interstitial iodine that forms stable $IO_{3}^{-1}$ species. $^{44}$ The optimized geometry (Fig. 6a) shows that the interstitial iodine atom forms three I-O chemical bonds with the three surrounded oxygen atoms carrying almost identical bond length. The I-O(1)/(2)/(3) bond length is 1.843, 1.834, and 1.842 Å at 0 K, respectively. The averaged bond length of the 6 ps MD trajectory almost remains unchanged at 300 K, corresponding to 1.842, 1.828, and 1.847 Å. The change in bond length is smaller than that in the interstitial iodine defects for all charged states (0, -1, +1) indicates the $IO_{3}^{-1}$ system becomes stable upon thermal

fluctuations. The increased stability originates from the fact that the symmetric manner of three I-O chemical bonds has little impact to the I-Pb octahedron. This observation is further supported by the calculated root-mean-square displacement velocity of atoms (Table 1). In addition to the grouped atoms discussed previously, we also present the data of the oxygen atoms. First, the obtained data show that $IO_{3}^{-1}$ defect suppresses the motions of MA, Pb, and I, responsible for a decreased the NA coupling and reduced current-voltage hysteresis.⁵⁷ Second, oxygen passivation also slows the motion of interstitial iodine atom compared to which in the defective perovskites. Third, the root-mean-square displacement velocity of oxygen atoms themselves is smallest. Overall, oxygen passivation can inhibit ion migration and stabilize the perovskite.⁴⁴

![](./images/812736478948884480_8.jpg)

Fig. 6 (a) Optimized $IO_{3}^{-1}$ geometry. The interstitial iodine and oxygen atoms are colored in green and red. (b) PDOS and charge densities of CBM and VBM, (c) Spectral density obtained from Fourier transforms of the autocorrelation functions for the energy

gap fluctuation, and (d) evolution of populations of the key states in $IO_3^{-1}$.

The PDOS shows that $IO_3^{-1}$ defect creates no mid-gap state (Fig. 6b). Oxygen passivation does not change the components of the band edges while decreases the electron wave functions and remains the hole wave functions unchanged (inset of Fig. 6b) compared to the $I_{i}^{-1}$ system (inset of Fig. 3c), reducing the NA coupling further (0.73 meV). Fig. 6c shows FTs that low-frequency modes dominate the spectral density, in agreement with the Fig. 4. The dominant peak at $67\ \mathrm{cm}^{-1}$ can be assigned to the I-Pb bending. $^{86}$ The peak at $155\ \mathrm{cm}^{-1}$ can be attributed to the librations of the organic cations. $^{86}$ The frequencies in the $200$-$400\ \mathrm{cm}^{-1}$ range can be associated with the modes of oxygen/iodine product, $^{44}$ agreeing with the fact that oxygen passivation stabilizes the perovskites reflecting by the almost unchanged I-O chemical bond lengths. Light and fast oxygen generates high-frequency modes and results in short dephasing time compared to the pristine and $I_{i}^{-1}$ systems. Fig. 6d shows the time-evolution populations of the CBM and VBM whose dynamics are depicted in Fig. 1a. The time scales are obtained by fitting the data to an exponent, $P(t)=exp\left(-\frac{t}{\tau}\right)$. The recombination is delayed by a factor of 2.7 and 1.8 compared to the pristine and $I_{i}^{-1}$ system, respectively. The deacceleration is attributed to the weak NA electron-phonon coupling and short pure-dephasing time. In particular, the NA coupling and pure-dephasing time are 0.73 meV and 7.0 fs in the present case while which are 1.02 meV/10.8fs and 0.83 meV/10.1fs for the pristine and $I_{i}^{-1}$ systems, respectively. Smaller electron-phonon coupling and shorter dephasing time favor longer electron-hole recombination time.

In addition to the above reported NA coupling, reorganization energy, $\lambda$, is another

important parameter to reflect charge transfer rate, which characterizes the energy cost due to geometry change experiencing a neutral to a charge system and vice versa. In general, the lower the reorganization energy, the smaller the geometry relaxation and higher the charge transfer rate. Therefore, we calculated the reorganization energy using constrained DFT because this approach can well describe the unpaired electron, according to the equation:

$$\lambda=E(M)-E\left(M^{*}\right) \quad (2)$$

where $E(\mathrm{M})$ and $E(\mathrm{M}^{*})$ are the total energies of the equilibrium structures of both reactant (intial state) and product (final state) states for each charge trapping or recombination process presented in the pristine $MAPbI_{3}, I_{i}, I_{i}^{-1}, I_{i}^{+1}$ and $IO_{3}^{-1}$ systems. The electronic configurations for the reactant and product states are defined in the SI. The calculated reorganization, summarized in Table 2, are small, below 0.11 eV, reflecting that the reactant and product geometries are very similar upon photoexcitation. Paying attention to charge trapping and recombination in particular $I_{i}$ system, the reorganization energy $\lambda$ for hole trapping is smaller than electron trapping, demonstrating that the occurrence possibility of hole trapping is higher than electron trapping, in consistent with the obtained results shown in Fig. 5b and Figure S14. In case of the $I_{i}^{+1}$ system, the reorganization energy $\lambda$ of electron trapping (trap/CBM) is lower than that VBM/CBM and VBM/trap, showing that most of electrons are firstly trapped by the electron trap state, then recombine with the free holes on VBM. The analysis agrees well with the simulated evolution of populations shown in Fig. 5d.

Table 2. Canonically Averaged Energy Gap, Absolute Averaged Value of NA

# Coupling, Pure-Dephasing Time, Rate Constant and Reorganization Energy ($\lambda$) for
Pairs of Electronic States in Pristine MAPbI₃, Iᵢ, Iᵢ⁻¹, Iᵢ⁺¹ and IO₃⁻¹ Systems.

<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2"></th>
      <th>Energy</th>
      <th>NA</th>
      <th rowspan="2">Dephasing<br>(fs)</th>
      <th rowspan="2">Rate<br>($\times 10^{-3}$ ps⁻¹)</th>
      <th rowspan="2">$\lambda$<br>(eV)</th>
    </tr>
    <tr>
      <th>gap<br>(eV)</th>
      <th>coupling<br>(meV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Pristine</td>
      <td>CBM $\rightarrow$ VBM</td>
      <td>1.61</td>
      <td>1.02</td>
      <td>10.8</td>
      <td>0.64</td>
      <td>0.071</td>
    </tr>
    <tr>
      <td rowspan="5">Iᵢ</td>
      <td>CBM $\rightarrow$ VBM</td>
      <td>1.70</td>
      <td>2.09</td>
      <td>8.7</td>
      <td>1.85</td>
      <td>0.063</td>
    </tr>
    <tr>
      <td>VBM $\rightarrow$ trap</td>
      <td>0.09</td>
      <td>3.10</td>
      <td>8.5</td>
      <td>30.33</td>
      <td>0.051</td>
    </tr>
    <tr>
      <td>CBM $\rightarrow$ trap</td>
      <td>1.61</td>
      <td>1.16</td>
      <td>9.3</td>
      <td>1.00</td>
      <td>0.020</td>
    </tr>
    <tr>
      <td>hole trapping</td>
      <td>--</td>
      <td>--</td>
      <td>--</td>
      <td>--</td>
      <td>0.083</td>
    </tr>
    <tr>
      <td>electron trapping</td>
      <td>--</td>
      <td>--</td>
      <td>--</td>
      <td>--</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>Iᵢ⁻¹</td>
      <td>CBM $\rightarrow$ VBM</td>
      <td>1.66</td>
      <td>0.83</td>
      <td>10.1</td>
      <td>0.49</td>
      <td>0.110</td>
    </tr>
    <tr>
      <td rowspan="3">Iᵢ⁺¹</td>
      <td>CBM $\rightarrow$ VBM</td>
      <td>1.65</td>
      <td>1.95</td>
      <td>8.2</td>
      <td>0.92</td>
      <td>0.051</td>
    </tr>
    <tr>
      <td>trap $\rightarrow$ VBM</td>
      <td>1.21</td>
      <td>0.56</td>
      <td>2.6</td>
      <td>0.44</td>
      <td>0.031</td>
    </tr>
    <tr>
      <td>CBM $\rightarrow$ trap</td>
      <td>0.44</td>
      <td>2.12</td>
      <td>3.4</td>
      <td>23.81</td>
      <td>0.020</td>
    </tr>
    <tr>
      <td>IO₃⁻¹</td>
      <td>CBM $\rightarrow$ VBM</td>
      <td>1.69</td>
      <td>0.73</td>
      <td>7.0</td>
      <td>0.24</td>
      <td>0.011</td>
    </tr>
  </tbody>
</table>

The above discussions illustrate that the excited charge carriers' lifetimes can be significantly modulated by oxidation state of interstitial iodine defects. Despite positive interstitial iodine can suppress electron-hole recombination but which easily tends to attract an electron to become a neutral defect that accelerates charge recombination. In turn, negative interstitial iodine favors to extend charge carriers' lifetime while the

significant ion migrations in the present case induce significant current-voltage hysteresis. The disadvantage is harmful to perovskite solar cells and even is a common problem in real applications because ion migration degrades perovskite films and devices. Oxygen can passivate negatively changed iodine defect and inhibit ion migration, and reduce hysteresis and nonradiative charge and energy losses, providing a mechanistic understanding for the prolonged excited charge carrier's lifetime in the presence of iodine defects and suggesting rational strategies to improve the photovoltaic performance of perovskite solar cells.

## 4. Conclusions
Using a combination of time dependent density functional theory and nonadiabatic molecular dynamics, we have established the mechanisms responsible for charge trapping and recombination in $MAPbI_3$ perovskites influencing by the oxidation state of interstitial iodine and oxygen doping. The calculated electron-hole recombination in pristine $MAPbI_3$ occurs on several nanoseconds, in good agreement with the experiment. Negative interstitial iodine reduces charge recombination by a factor of 1.3 without creating trap states due to the absence of unsaturated chemical bonds. Positive interstitial iodine produces an unoccupied trap below the CBM that can trap an electron. The trap state arises from that the interstitial iodine cation forms a I-trimer with adjacent lattice iodine anions. Surprisingly, conduction band free electron gets trapped extremely fast, leading to a delayed recombination of the trapped electron with valence band hole by a factor of 1.5. In turn, the direct band-to-band recombination of free

electron and hole is highly excluded although this process operates on a similar time scale. Unfortunately, a positive interstitial iodine defect easily tends to convert to a neutral iodine defect by capturing an electron, forming a singly occupied state above the VBM. Because of strong NA coupling between the trap state and VBM, the photoexcited hole proceeds rapidly trapped by the hole trap. Then, the recombination between the conduction band free electron and trapped hole is accelerated by a factor of 1.6. Consequently, negative interstitial iodine is responsible for slowing charge recombination while suffers from notable hysteresis phenomenon due to ion migration. The instability of interstitial iodine defects under light and/or thermal irradiation can be compensated by oxygen doping, because charged interstitial iodine defects with oxygen passivation forms stable $IO_{3}^{-1}$ species, which inhibit ion migration and stabilize perovskites. At the same time, oxygen passivation reduces the NA electron-phonon coupling due to diminishing overlap of electron and hole wave functions, and shortens coherence time because light and fast oxygen atoms active higher frequencies, resulting in reduction of the band-to-band recombination of free electron and hole by a factor of 2.7. The nonradiative charge trapping is promoted by low frequency Pb-I vibrations. Neutral and positive interstitial iodine defects produce higher frequencies, due to the creation of localized states, and generate stronger electron-phonon coupling between the band edges and the trap states.

The study advances our understanding of oxidation state of interstitial iodine and role of oxygen played in charge dynamics of perovskites, providing valuable insights for development of high-performance perovskite photovoltaic and optoelectronic

devices.

## Notes
The authors declare no competing financial interests.

## ACKNOWLEDGMENTS
This work was supported by the National Natural Science Foundation of China, grant Nos. 21573022, 51861135101, 21688102, 21590801, and 21703222. R. L. acknowledges financial support by the Fundamental Research Funds for the Central Universities, the Recruitment Program of Global Youth Experts of China, and the Beijing Normal University Startup.

Supporting Information Available: Coupled kinetics equations and their solutions; data fitting for the state-to-state transition rates; and time-evolution populations of the electron trap-assisted electron-hole recombination in $I_i$ system; and the electronic configurations for reactant (initial) and product (final) states of each dynamics process.

The material is available free of charge via the Internet at http://pubs.rsc.org.

# REFERENCES

1 D. P. Tabor, L. M. Roch, S. K. Saikin, C. Kreisbeck, D. Sheberla, J. H. Montoya, S. Dwaraknath, M. Aykol, C. Ortiz and H. Tribukait, *Nat. Rev. Mater.*, 2018, **3**, 5-20.

2 W. S. Yang, J. H. Noh, N. J. Jeon, Y. C. Kim, S. Ryu, J. Seo and S. I. Seok, *Science*, 2015, **348**, 1234-1237.

3 D. Shi, V. Adinolfi, R. Comin, M. Yuan, E. Alarousu, A. Buin, Y. Chen, S. Hoogland, A. Rothenberger and K. Katsiev, *Science*, 2015, **347**, 519-522.

4 G. Laurita, D. H. Fabini, C. C. Stoumpos, M. G. Kanatzidis and R. Seshadri, *Chem. Sci.*, 2017, **8**, 5628-5635.

5 W.-W. Wang, J.-S. Dang, R. Jono, H. Segawa and M. Sugimoto, *Chem. Sci.*, 2018, **9**, 3341-3353.

6 X. Lü, W. Yang, Q. Jia and H. Xu, *Chem. Sci.*, 2017, **8**, 6764-6776.

7 D. Li, C. Sun, H. Li, H. Shi, X. Shai, Q. Sun, J. Han, Y. Shen, H.-L. Yip and F. Huang, *Chem. Sci.*, 2017, **8**, 4587-4594.

8 E. T. Hoke, D. J. Slotcavage, E. R. Dohner, A. R. Bowring, H. I. Karunadasa and M. D. McGehee, *Chem. Sci.*, 2015, **6**, 613-617.

9 B. Yang, O. Dyck, J. Poplawsky, J. Keum, S. Das, A. Puretzky, T. Aytug, P. C. Joshi, C. M. Rouleau and G. Duscher, *Angew. Chem. Int. Ed.*, 2015, **54**, 14862-14865.

10 H. Sun, K. Deng, Y. Zhu, M. Liao, J. Xiong, Y. Li and L. Li, *Adv. Mater.*, 2018, **30**, 1801935.

11 H. Sun, W. Tian, F. Cao, J. Xiong and L. Li, *Adv. Mater.*, 2018, **30**, 1706986.

12 H. Zhu, Y. Fu, F. Meng, X. Wu, Z. Gong, Q. Ding, M. V. Gustafsson, M. T. Trinh,

S. Jin and X. Y. Zhu, *Nat. Mater.*, 2015, **14**, 636-642.

13 S. Kumar, J. Jagielski, T. Tian, N. Kallikounis, W.-C. Lee and C.-J. Shih, *ACS Energy Lett.*, 2018, **4**, 118-125.

14 Y.-S. Chen, J. S. Manser and P. V. Kamat, *J. Am. Chem. Soc.*, 2015, **137**, 974-981.

15 A. Kojima, K. Teshima, Y. Shirai and T. Miyasaka, *J. Am. Chem. Soc.*, 2009, **131**, 6050-6051.

16 NREL. Efficiency chart. https://www.nrel.gov/pv/assets/pdfs/best-reserch-cell-efficiencies.20190411.pdf (2019).

17 K. Masuko, M. Shigematsu, T. Hashiguchi, D. Fujishima, M. Kai, N. Yoshimura, T. Yamaguchi, Y. Ichihashi, T. Mishima and N. Matsubara, *IEEE J. Photov.*, 2014, **4**, 1433-1435.

18 S. Rühle, *Sol. Energy*, 2016, **130**, 139-147.

19 J. Kim, S.-H. Lee, J. H. Lee and K.-H. Hong, *J. Phys. Chem. Lett.*, 2014, **5**, 1312-1317.

20 J. M. Ball and A. Petrozza, *Nat. Energy*, 2016, **1**, 16149.

21 G. Gordillo, C. Otálora and A. Ramirez, *Phys. Chem. Chem. Phys.*, 2016, **18**, 32862-32867.

22 A. B. Djurišić, F. Liu, A. M. C. Ng, Q. Dong, K. W. Man, A. Ng and C. Surya, *Phys. Status Solidi-R*, 2016, **10**, 281-299.

23 W. J. Yin, T. Shi and Y. Yan, *Appl. Phys. Lett.*, 2014, **104**, 6050-1429.

24 R. Long, W. Fang and A. V. Akimov, *J. Phys. Chem. Lett.*, 2016, **7**, 653-659.

25 M. H. Du, *J. Phys. Chem. Lett.*, 2015, **6**, 1461-1466.

26 M. H. Du, *J. Mater. Chem. A*, 2014, **2**, 9091-9098.

27 A. Buin, P. Pietsch, J. Xu, O. Voznyy, A. H. Ip, R. Comin and E. H. Sargent, *Nano Lett.*, 2014, **14**, 6281-6286.

28 M. L. Agiorgousis, S. Yi-Yang, Z. Hao and Z. Shengbai, *J. Am. Chem. Soc.*, 2014, **136**, 14570-14575.

29 A. Buin, R. Comin, J. Xu, A. H. Ip and E. H. Sargent, *Chem. Mater.*, 2015, **27**, 4405-4412.

30 H. Uratani and K. Yamashita, *J. Phys. Chem. Lett.*, 2017, **8**, 742-746.

31 S. D. Stranks, V. M. Burlakov, T. Leijtens, J. M. Ball, A. Goriely and H. J. Snaith, *Phys. Rev. Appl.* 2014, **2**, 034007.

32 T. Leijtens, G. Eperon, A. Barker, G. Grancini, Z. Wei, J. Ball, A. R. S. Kandada, H. Snaith and A. Petrozza, *Energy Environ. Sci.*, 2016, **9**, 3472-3481.

33 X. Wen, Y. Feng, S. Huang, F. Huang, Y.-B. Cheng, M. Green and A. Ho-Baillie, *J. Mater. Chem. C*, 2016, **4**, 793-800.

34 G. J. A. H. Wetzelaer, M. Scheepers, A. M. Sempere, C. Momblona and H. J. Bolink, *Adv. Mater.*, 2015, **27**, 1837-1841.

35 M. Z. Bellus, M. Mahjouri-Samani, S. D. Lane, A. D. Oyedele, X. Li, A. A. Puretzky, D. Geohegan, K. Xiao and H. Zhao, *ACS Nano*, 2018, **12**, 7086-7092.

36 L. Wang, C. Xu, M.-Y. Li, L.-J. Li and Z.-H. Loh, *Nano Lett.*, 2018, **18**, 5172-5178.

37 D. Meggiolaro and F. De Angelis, *ACS Energy Lett.*, 2018, **3**, 2206-2222.

38 W. S. Yang, B.-W. Park, E. H. Jung, N. J. Jeon, Y. C. Kim, D. U. Lee, S. S. Shin, J. Seo, E. K. Kim and J. H. Noh, *Science*, 2017, **356**, 1376-1379.

39 S. Wang, Y. Jiang, E. J. Juarez-Perez, L. K. Ono and Y. Qi, *Nat. Energy*, 2017, **2**, 16195.

40 R. J. Stewart, C. Grieco, A. V. Larsen, G. S. Doucette and J. B. Asbury, *J. Phys. Chem. C*, 2016, **120**, 12392-12402.

41 J. M. Azpiroz, E. Mosconi, J. Bisquert and F. De Angelis, *Energy Environ. Sci.*, 2015, **8**, 2118-2127.

42 A. M. A. Leguy, J. M. Frost, A. P. Mcmahon, V. G. Sakai, W. Kockelmann, C. H. Law, X. Li, F. Foglia, A. Walsh and B. C. O'Regan, *Nat. Commun.*, 2015, **6**, 7124.

43 Y. Yuan and J. Huang, *Acc. Chem. Res.*, 2016, **49**, 286-293.

44 D. Meggiolaro, E. Mosconi and F. D. Angelis, *Acs Energy Lett.*, 2017, **2**, 2794-2798.

45 J. F. Galisteo-López, M. Anaya, M. E. Calvo and H. Míguez, *J. Phys. Chem. Lett.*, 2015, **6**, 2200-2205.

46 Y. Tian, M. Peter, E. Unger, M. Abdellah, K. Zheng, T. Pullerits, A. Yartsev, V. Sundström and I. G. Scheblykin, *Phys. Chem. Chem. Phys.*, 2015, **17**, 24978-24987.

47 S. G. Motti, M. Gandini, A. J. Barker, J. M. Ball, A. R. S. Kandada and A. Petrozza, *ACS Energy Lett.*, 2016, **1**, 726-730.

48 R. Brenes, C. Eames, V. Bulović, M. S. Islam and S. D. Stranks, *Adv. Mater.*, 2018, **30**, 1706208.

49 H.-H. Fang, S. Adjokatse, H. Wei, J. Yang, G. R. Blake, J. Huang, J. Even and M. A. Loi, *Sci. Adv.*, 2016, **2**, e1600534.

50 C. F. Craig, W. R. Duncan and O. V. Prezhdo, *Phys. Rev. Lett.*, 2005, **95**, 163001.

51 S. A. Fischer, B. F. Habenicht, A. B. Madrid, W. R. Duncan and O. V. Prezhdo, *J.

*Chem. Phys.*, 2011, **134**, 024102.

52 A. V. Akimov and O. V. Prezhdo, *J. Chem. Theory Comput.*, 2013, **9**, 4959-4972.

53 A. V. Akimov and O. V. Prezhdo, *J. Chem. Theory Comput.*, 2014, **10**, 789-804.

54 A. E. Sifain, J. A. Bjorgaard, T. R. Nelson, B. T. Nebgen, A. J. White, B. J. Gifford,
D. W. Gao, O. V. Prezhdo, S. Fernandez-Alberti and A. E. Roitberg, *J. Chem. Theory
Comput.*, 2018, **14**, 3955-3966.

55 S. Huang, T. M. Inerbaev and D. S. Kilin, *J. Phys. Chem. Lett.*, 2014, **5**, 2823-2829.

56 J. R. Klein, O. Flender, M. Scholz, K. Oum and T. Lenzer, *Phys. Chem. Chem. Phys.*,
2016, **18**, 10800-10808.

57 L. Yang, M. Wu, F. Cai, P. Wang, R. S. Gurney, D. Liu, J. Xia and T. Wang, *J.
Mater. Chem. A*, 2018, **6**, 10379-10387.

58 H. M. Jaeger, S. Fischer and O. V. Prezhdo, *J. Chem. Phys.*, 2012, **137**, 22A545.

59 W. Kohn and L. J. Sham, *Phys. Rev.*, 1965, **140**, A1133--A1138.

60 E. R. Bittner and P. J. Rossky, *J. Chem. Phys.*, 1995, **103**, 8130-8143.

61 B. J. Schwartz, E. R. Bittner, O. V. Prezhdo and P. J. Rossky, *J. Chem. Phys.*, 1996,
**104**, 5942-5955.

62 Z. Chaoyuan, N. Shikha, A. W. Jasper and D. G. Truhlar, *J. Chem. Phys.*, 2004, **121**,
7658-7670.

63 S. Mukamel, *Principles of nonlinear optical spectroscopy*, Oxford university press
New York, 1995.

64 Z. Zhang, W. H. Fang, M. V. Tokina, R. Long and O. V. Prezhdo, *Nano Lett.*, 2018,
**18**, 2459-2466.

65 J. He, W. H. Fang and R. Long, *J. Phys. Chem. Lett.*, 2018, **9**, 4834-4840.

66 L. Liu, W. H. Fang, R. Long and O. V. Prezhdo, *J. Phys. Chem. Lett.*, 2018, **9**, 1164-1171.

67 R. Long, J. Liu and O. V. Prezhdo, *J. Am. Chem. Soc.*, 2016, **138**, 3884-3890.

68 Z. Zhang, R. Long, M. V. Tokina and O. V. Prezhdo, *J. Am. Chem. Soc.*, 2017, **139**, 17327-17333.

69 J. He, M. Guo and R. Long, *J. Phys. Chem. Lett.*, 2018, **9**, 3021-3028.

70 Y. Wei and R. Long, *J. Phys. Chem. Lett.*, 2018, **9**, 3856-3862.

71 W. Li, Y.-Y. Sun, L. Li, Z. Zhou, J. Tang and O. V. Prezhdo, *J. Am. Chem. Soc.*, 2018, **140**, 15753-15763.

72 R. Long, D. Casanova, W. H. Fang and O. V. Prezhdo, *J. Am. Chem. Soc.*, 2017, **139**, 2619-2629.

73 C. C. Stoumpos, C. D. Malliakas and M. G. Kanatzidis, *Inorg. Chem.*, 2013, **52**, 9019-9038.

74 G. Kresse and J. Furthmüller, *Phys. Rev. B*, 1996, **54**, 11169.

75 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865-3868.

76 B. PE, *Phys. Rev. B Condens Matter.*, 1994, **50**, 17953-17979.

77 H. J. Monkhorst and J. D. Pack, *Phys. Rev. B*, 1976, **13**, 5188-5192.

78 S. Grimme, J. Antony, S. Ehrlich and H. Krieg, *J. Chem. Phys.*, 2010, **132**, 154104.

79 C. Quarti, E. Mosconi, J. M. Ball, V. D'Innocenzo, C. Tao, S. Pathak, H. J. Snaith, A. Petrozza and F. De Angelis, *Energy Environ. Sci.*, 2016, **9**, 155-163.

80 D. Meggiolaro, E. Mosconi and F. De Angelis, *ACS Energy Lett.*, 2018, **3**, 447-451.

81 J.-H. Yang, W.-J. Yin, J.-S. Park and S.-H. Wei, *J. Mater. Chem. A*, 2016, **4**, 13105-13112.

82 W. Ming, S. Chen and M.-H. Du, *J. Mater. Chem. A*, 2016, **4**, 16975-16981.

83 G. Giorgi, J.-I. Fujisawa, H. Segawa and K. Yamashita, *J. Phys. Chem. C*, 2014, **118**, 12176-12183.

84 C.-J. Yu, U.-G. Jong, M.-H. Ri, G.-C. Ri and Y.-H. Pae, *J. Mater. Sci.*, 2016, **51**, 9849-9854.

85 A. M. Leguy, A. R. Goñi, J. M. Frost, J. Skelton, F. Brivio, X. Rodríguezmartínez, O. J. Weber, A. Pallipurath, M. I. Alonso and M. Campoyquiles, *Phys. Chem. Chem. Phys.*, 2016, **18**, 27051.

86 C. Quarti, G. Grancini, E. Mosconi, P. Bruno, J. M. Ball, M. M. Lee, H. J. Snaith, A. Petrozza and F. D. Angelis, *J. Phys. Chem. Lett.*, 2014, **5**, 279-284.

87 S. V. Kilina, A. J. Neukirch, B. F. Habenicht, D. S. Kilin and O. V. Prezhdo, *Phys. Rev. Lett.*, 2013, **110**, 180404.

88 J. Liu, A. J. Neukirch and O. V. Prezhdo, *J. Phys. Chem. C*, 2014, **118**, 20702-20709.

TOC Graphic

![](./images/812736478948884480_9.jpg)

Oxidation state of interstitial iodine and oxygen passivation control the electron-hole
recombination in $CH_3NH_3PbI_3$ perovskite.