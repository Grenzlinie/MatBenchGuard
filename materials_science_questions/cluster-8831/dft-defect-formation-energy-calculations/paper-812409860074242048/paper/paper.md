![](./images/812409860074242048_1.jpg)

Computational Materials Science 12 (1998) 309–318

# Ab initio pseudopotential calculations of dopant diffusion in Si

Jing Zhu $^{1}$

Lawrence Livermore National Laboratory, P.O. Box 808, L-417, Livermore, CA 94551, USA

## Abstract
The ab initio pseudopotential method is used to study transient enhanced diffusion (TED) related processes. The electronic degrees of freedom are included explicitly, together with the fully self-consistent treatment of the electron charge density. A large supercell and a fine $k$-point mesh are used to ensure numerical convergence. Such method has been demonstrated to give quantitative description of defect energetics. We will show that boron diffusion is significantly enhanced in the presence of the Si interstitial due to the substantial lowering of the migrational barrier through a kick-out mechanism. The resulting mobile boron can also be trapped by another substitutional boron, forming an immobile and electrically inactive two-boron pair. Similarly, carbon diffusion is also enhanced significantly due to the pairing with Si interstitials. However, carbon binds to Si interstitials much more strongly than boron does, taking away most Si interstitials from boron at sufficiently large carbon concentration, which causes the suppression of the boron TED. We will also show that Fermi level effect plays an important role in both Si interstitial and boron diffusion.
© 1998 Elsevier Science B.V. All rights reserved.

PACS: 66.30.-h; 61.72.Ji; 61.72.Tt; 73.20.Hb

Keywords: TED (transient enhanced diffusion); Boron dopant; Carbon dopant; Defect; ab initio pseudopotential method; Impurity cluster

---

## 1. Introduction

Implanted dopants such as B undergo transient enhanced diffusion (TED) during rapid thermal annealing (RTA) in Si [1]. In particular, B implantation followed by RTA at $T>700^\circ$C leads to broadening of the as-implanted B profile by several thousands Å in times as short as 15 min [2]. As the minimum feature size of Si-based semiconductor devices decreases and gradually approaches the dopant diffusion length during processing conditions, accurately modeling and therefore controlling TED are critical issues facing the semiconductor industry today.

Experimentally, dopant diffusion and TED can be studied by using dopant marker layers embedded in epitaxially grown Si superlattice structures. Excess Si interstitials can be injected from the surface by either surface oxidation or ion implantation. Excess vacancies can be generated using surface nitridation. The amount of dopant diffusion is monitored by measuring the dopant density profile using secondary ion mass spectroscopy or spread resistance measurements and comparing to reference samples. In the case of B dopant in Si, several phenomenon have been observed [3]. First, B diffusion of the marker layer is significantly

---

$^{1}$ Tel.: +1 925 422 2178; fax: +1 925 422 6594; e-mail: zhul@llnl.gov.

0927-0256/98/$ – see front matter © 1998 Elsevier Science B.V. All rights reserved.
PII: S0927-0256(98)00023-8

---

COMPUTATIONAL
MATERIALS
SCIENCE

enhanced under injection of Si interstitials and is initially suppressed under injection of vacancies, clearly demonstrating an interstitial assisted mechanism for the boron TED. Secondly, an im- mobile and electrically inactive B region at the peak of the B density profile is observed following oxidation or high dose implantation, even for B concentration below the solid solubility limit in Si, suggesting an interstitial assisted B clustering process. Thirdly, no boron TED is observed when a high concentration of C (up to $2 \times 10^{19} / cm^{3}$ ) is also epitaxially grown into the sample, suggesting C trapping of the Si interstitial.

Simulating such a macroscopic process clearly requires continuum process simulation tools such as SUPREM or the newly developed kinetic Monte Carlo methods [4,5]. However, for the model to be predictive, it is critical to understand energetics of single defects and impurities as well as their mutual interactions. Since experimental methods are mostly indirect, it is clearly beneficial to study such phenomenon using atomistically based theoretical methods in order to help under- stand those individual processes that are key to the defect dynamics.

Due to a series of breakthrough developments in theoretical methods and rapid increases in computational power, ab initio methods based on the density functional theory (DFT) and the local density approximation (LDA) have been devel- oped to the point that large systems with as many as a few hundreds of atoms can now be studied accurately. These calculations can then lead to a quantitative understanding of the energetics of single defects and impurities as well as their mu- tual interactions. Previously, Nichols et al. carried out the most complete studies of the substitutional $B$ and interstitial $Si$ pair $(B_{s}-Si_{i})$ , including the kick-out mechanism [6]. However, Lowding per- turbation theory was used to include plane waves from 10 to 20 Ry and in addition, not all atoms were fully relaxed in the search for the low energy configurations. Tarnow, on the other hand, has studied several configurations of interstitial andsubstitutional B pairs $(B_{i}-B_{s})$ in addition to $B_{s}-Si_{i}$  pairs [7]. However, small supercells together with small plane-wave cutoffs were used to determine the lowest energy configuration and no accurate values of the binding energies were provided. Capaz et al. [8] has performed the first LDA cal- culation related to $C$ interstitial migration using a32-atom supercell with three special $k$ point. However, no energetics of the interaction between C and Si interstitial was presented.

In this paper, we present ab initio studies of TED related defect processes using large supercells and well converged $k$ -point sampling. First, results of Si self-interstitial formation and migration will be presented, including the charged state effects. Self-diffusion in intrinsic $Si$ is also addressed. Secondly, self-interstitial assisted B diffusion and pairing are also studied to understand the origin of boron TED. Finally, we study $C$ diffusion and pairing with $Si$ interstitial in order to understand the $C$ trapping of the interstitials and therefore the suppression of boron TED.

## 2. Computational methods

The present calculations used the DFT with the LDA to determine quantitatively the energetics between point defects and impurities in $Si$ . The Ceperly and Alder [9] exchange correlation po-tential parameterized by Perdew and Zunger [10] was used. A nonlocal and norm conserving pseu- dopotential constructed using the scheme of Troullier and Martins [11] was used to describe the valance electron interactions with the atomic core. The nonlocal components of the pseudopotential were expressed in a separable form of Kleinman and Bylander [12]. Typically, the calculations were performed in 32- and 64-atom unit cell with a fixed volume corresponding the $Si-Si$ bond distance to be 4.443 a.u. in pure $Si$ , which is the experimental value of equilibrium distance (the theoretical equilibrium lattice constant is $1 \%$ less than the experimental value). We use a planewave basis set with cutoff energies of $20 Ry$ for $B$ and $40 Ry$ for $C$  to expand the electronic wave functions. This corresponds to a Hamiltonian matrix size of up to more than 36,500 in the case of 64-atom supercell. We have tested up to $60 Ry$ for the plane-wave energy cut off in 32-atom cells and found that the relative energies were all converged to within0.10-0.15 eV.

Two to eight special $k$ points in 32-atom supercell and one to four special $k$ points in 64-atom supercell were used to sample the first Brillouin zone. The exact number of special $k$ points used depended on the symmetry of the configurations and supercell sizes. Special care was taken to ensure that the $k$ points used were equivalent to a $2\times 2\times 2$ special $k$-point mesh [13] in the first Brillouin zone of a 64-atom supercell which allowed unambiguous analysis of effects of the supercell size. The $k$-point convergence was checked by using up to $4\times 4\times 4$ special $k$-point mesh in the 32-atom supercell, and the relative defect energy differences were found to be converged within 0.15 eV in all cases tested. The conjugate gradient iterative diagonalization scheme was used to obtain the self-consistent solutions of the one-electron Kohn-Sham equations [14]. The Hellmann- Feynman theorem was used to evaluate the forces on all atoms which were allowed to move freely. The quasi-Newton method was used to find the relaxed atomic positions. In the case of charged defects, a neutralizing uniform charged background was imposed to avoid energy divergence due to periodically reproduced charged supercells. Unless specifically noted, we will only report the results using 64-atom supercells.

## 3. Results and discussion

### 3.1. Si interstitial formation and migration

The lowest energy configuration for a neutral interstitial Si is the $\langle 1\ 1\ 0\rangle$ dumbbell configuration. In this configuration, two Si atoms displace along a $\langle 1\ 1\ 0\rangle$ direction by about one bond distance, sharing one single lattice site. The formation energy $E_{\mathrm{f}}(\mathrm{Si}_{\mathrm{i}})$ of such a Si interstitial can be defined as

$$
E_{\mathrm{f}}(\mathrm{Si}_{\mathrm{i}})=E(\mathrm{Si}_{65})-\frac{65}{64}E(\mathrm{Si}_{64}),
$$

where $E(\mathrm{Si}_{65})$ in 65-atom supercell total energy including one Si interstitial and $E(\mathrm{Si}_{64})$ is the 64 bulk atom total energy. The formation energy is 3.2 eV in LDA for the $\langle 1\ 1\ 0\rangle$ self-interstitial configuration [15]. The neutral Si interstitial at hexagonal (H) and tetrahedral (T) site is about 0.1 eV an 1.4 eV higher in energy than the $\langle 1\ 1\ 0\rangle$ interstitial. An extended form of $\langle 1\ 1\ 0\rangle$ self-interstitial configuration was also studied. This configuration, which was the lowest energy interstitial configuration using the Stilinger-Weber classical potential [16], is only metastable in the present calculation with energy to be 0.8 eV higher than the ab initio $\langle 1\ 1\ 0\rangle$ configuration.

We have also carried out the formation energy calculation using the GGA exchange correlation potential [17]. For $\mathrm{Si}_{\mathrm{i}}$, while the relative energies between different configurations are not changed, the absolute value for formation energy does change. The GGA formation energy for the neutral Si self-interstitial is 3.7 eV, about 0.5 eV higher than the LDA value. While GGA is known to give much better results than LDA for systems such as atoms, molecules, actinides as well as some of the transition metal elements, its overall effects on semiconductor defect system still remain to be seen.

For semiconductor materials such as Si, the electron Fermi level varies according to the dopant concentration and temperature. The properties of defects such as Si self-interstitials can change drastically when defects acquire additional charges depending on the Fermi level position. Therefore, it is quite essential to study the charged defects.

One of the effects of electron Fermi level position on charged defects is that the total energies of the charged defects change as a function of the Fermi level position $(E_{\mathrm{Fermi}})$. In order to compare total energies of different charge states, the chemical potential of the electrons needs to be taken into account, which is dictated by $E_{\mathrm{Fermi}}$. For charged defect with a charge of $+n$ and the energy to be compared with is

$$
E=E_{\text{supercell}}+nE_{\text{Fermi}}.
$$

In Fig. 1, the energy diagram of various interstitial configurations with total charges from +2 to -2 is plotted as a function of $E_{\mathrm{Fermi}}$ from valence band maximum $E_{\mathrm{vbm}}$ to conduction band minimum $E_{\mathrm{cbm}}$. In the case where the Fermi level is at $E_{\mathrm{vbm}}$, the lowest energy configuration is the T interstitial with +2 charge state. As the Fermi level

![](./images/812409860074242048_2.jpg)

Fig. 1. Si self-interstitial configuration formation energy dia- gram as a function of the Fermi level position. Energy zero for the configuration energy is arbitrarily set to be that of the $\langle 110\rangle$ configuration. The energy zero for the Fermi energy is that of the valence band maximum. where $E_{supercell}$ is the energy calculated from the supercell method.

sweeps from $E_{vbm}$ to $E_{cbm}$, the lowest configuration goes form T interstitial with +2 charge state to neutral $\langle 110\rangle$ interstitial. As the Fermi level gets close to $E_{cbm}$, the negatively charged $\langle 110\rangle$ interstitial has about the same energy as the neutral one or slightly lower. The reason for $T^{+2}$ to be lower in energy than $\langle 110\rangle$ at $p$-doped condition can be understood by the following argument. The neutral T interstitial has one shallow state close to the conduction band and is occupied by tow electrons. Therefore, these two electrons will be transferred to $E_{Fermi}$ in the case of +2 charge state, gaining almost twice the Si electronic energy gap or about 2.4 eV when the Fermi level is at $E_{vbm}$. This energy gain can more than offset the energy cost of 1.4 eV for converting a neutral $\langle 110\rangle$ interstitial to a T one. This is why the $T^{+2}$ interstitial becomes the lowest energy configuration for interstitials of $p$-doped materials.

The migrational mechanism of Si self-interstitial also depends strongly on the Fermi level position. Such mechanism is further complicated by the possibility of changing charge state during the migration. We discuss this possibility for the intrinsic Si material, leaving a more detailed and general discussion for a future publication.

The neutral $\langle 110\rangle$ is the lowest energy configuration for the intrinsic Si material, where the $E_{Fermi}$ is exactly at mid-gap. If the charge state stays neutral during migration, the lowest energy path will be from $\langle 110\rangle$ to T to $\langle 110\rangle$ with a migrational barrier of 1.4 eV, where the neutral T interstitial is the saddle point. However, the migrational energy can be lowered if the charge state is allowed to change during the migrational process. For example, if anytime during the migrational step, a hole is captured and the interstitial becomes singly positively charged. Then, the saddle point will be $T^{+1}$ with a migrational barrier of only 0.9 eV. Furthermore, if two holes can be captured during the process and the interstitial becomes doubly positively charged, the migrational barrier can be further reduced to only 0.7 eV. The saddle point, however, is no longer at $T^{+2}$. It will be somewhere in between $\langle 110\rangle$ and T configuration and the two holes have to be captured simultaneously at the saddle point to obtain the low migrational barrier. We believe that the simultaneous capture of two holes at exactly the saddle point position is too infrequent for this mechanism to be the dominant mechanism at relevant temperatures. On the other hand, the hole capture rate for Si interstitial during the migration is likely to be significant enough for the dominant migrational mechanism for Si interstitial to be through $T^{+1}$ with a migrational barrier of 0.9 eV. The change of charge state during self-interstitial migration is also consistent with the experimental findings of a thermal diffusion at liquid helium temperature under electron irradiation.

### 3.2. Si self-diffusion

With the formation and migration energy of Si self-interstitial, we can calculate the activation energy of Si self-diffusion due to the self-interstitial mechanism, where the self-diffusion is accomplished first by creating a Si self-interstitial and then by self-interstitial migration. The activation energy for this mechanism is thus the sum of the formation energy and migration energy of self-interstitial. Under the intrinsic condition, this works out to be $3.7+0.9=4.6$ eV for the self-diffusion activation energy using the GGA

formation energy for self-interstitial. An alternative mechanism for Si self-diffusion is the vacancy mechanism where a vacancy is first created and then migrate. The formation energy and the migration energy of vacancy from LDA (as well as GGA) are 3.65 and 0.3 eV, respectively, which yields 3.95 eV for the activation, about 0.65 eV smaller than that of the interstitial mechanism. This result tends to suggest that the vacancy mechanism will dominate Si self-diffusion due to the smaller activation energy. However, it is contrary to some of the results from self-diffusion experiment. For example, the metal diffusion experiments where only the self-interstitial mechanism contributes seem to give the same amount of self-diffusion as the Si tracer experiments do where all mechanisms contribute. These experimental results tend to suggest that the interstitial mechanism dominates Si self-diffusion.

It turns out that in order to compare the relative importance of two competing mechanisms, the activation energies are not the only things that are important. At elevated temperature, the prefactors will also become important. In the case of self-diffusion, if we only consider the vacancy and self-interstitial mechanism, the Si self-diffusivity $D$ at temperature $T$ can be written as

$$
D=D_{\mathrm{v}}+D_{\mathrm{i}}=c_{\mathrm{v} 0} \mathrm{e}^{-E_{\mathrm{v}} / k T}+c_{\mathrm{i} 0} \mathrm{e}^{-E_{\mathrm{i}} / k T},
$$

where $D_{\mathrm{v}}$ and $D_{\mathrm{i}}$ are the vacancy and interstitial components of the Si self-diffusivity with $c_{\mathrm{v} 0}$ and $c_{\mathrm{i} 0}$ the prefactors and $E_{\mathrm{v}}$ and $E_{\mathrm{i}}$ the activation energies respectively. The relative importance of those two mechanisms can be calculated by

$$
\frac{D_{\mathrm{v}}}{D_{\mathrm{i}}}=\frac{c_{\mathrm{v} 0}}{c_{\mathrm{i} 0}} \mathrm{e}^{\left(E_{\mathrm{i}}-E_{\mathrm{v}}\right) / k T}.
$$

From this formula, the vacancy mechanism will clearly dominate if $c_{\mathrm{v} 0}>c_{\mathrm{i} 0}$. However, in the case where $c_{\mathrm{v} 0}<c_{\mathrm{i} 0}$, there will be two temperature regimes separated by a critical temperature.

$$
T_{\mathrm{c}}=\frac{E_{\mathrm{i}}-E_{\mathrm{v}}}{k \ln \left(c_{\mathrm{i} 0} / c_{\mathrm{v} 0}\right)}.
$$

When $T<T_{\mathrm{c}}$, the vacancy mechanism will still dominate due to its smaller activation energy. However, at $T>T_{\mathrm{c}}$, the interstitial mechanism will become dominate due to its larger prefactor.

While the ab initio method is arguably the most accurate theoretical tools for defect energetics, it is also computationally very intensive. A tight-binding simulation is therefore carried out in order to calculate the diffusion pre-factors [18]. The tight-binding method, which still explicitly includes electronic degrees of freedom, is computationally much less demanding than the ab initio method at a cost of less accuracy. The prefactors of self-interstitial and vacancy diffusion are directly calculated from tight-binding molecular dynamics. The self-interstitial formation entropy is then fitted to the metal diffusion experiment at high temperature while the vacancy formation entropy is simply taken from ab initio calculations. Both the formation entropy and the migration pre-factors are then combined to derive the prefactors for Si self-diffusion. It is shown that the interstitial mechanism pre-factor is orders of magnitude larger than the vacancy one which then yields a $T_{\mathrm{c}}$ to be around $1080^{\circ} \mathrm{C}$, in good agreement with the recent experimental findings [19].

### 3.3. B interstitial and its migration

As discussed above, B diffusion in Si is enhanced in the presence of excess self-interstitials, which leads to TED. Therefore, it is important to study the complexes formed by a $\mathrm{B}_{\mathrm{s}}$ atom and a $\mathrm{Si}_{\mathrm{i}}$ atom close together. In fact, a true B interstitial configuration $\left(\mathrm{B}_{\mathrm{i}}\right.$ which is a B atom that stays in the interstitial region of the Si lattice, such as the hexagonal or tetrahedral site) or a B-Si interstialcy configuration (B and Si atom sharing one single site) is also a possible configuration formed by a $\mathrm{B}_{\mathrm{s}}$ and $\mathrm{Si}_{\mathrm{i}}$ pair. It is found that similar to $\mathrm{Si}_{\mathrm{i}}$, the lowest energy configuration for the $\mathrm{B}_{\mathrm{s}}$ and $\mathrm{Si}_{\mathrm{i}}$ pair is also strongly dependent on its charge state. The $+1,-1$ and neutral state configurations are likely to be important and are therefore studied in the present work.

In the case of positively charged state, the lowest energy B-I configuration is a substitutional B and interstitial Si pair configuration with the B atom staying substitutionally and the Si atom staying near an interstitial T site which is a nearest neighbour to the substitutional B atom. This configuration is essentially a $\mathrm{B}_{\mathrm{s}}^{-}$and $\mathrm{Si}_{\mathrm{i}}^{+2}$ pair as

the $B_s$ is likely in $-1$ charge state and the $S_i$ in tetrahedral site is likely in $+2$ charge state. The binding energy of such a configuration relative to well separated $B_s^{-1}$ and $S_i^{+2}$ defects is defined by

$$
\begin{aligned}
E_{\mathrm{b}}\left(\mathrm{Si}_{\mathrm{i}}-\mathrm{B}_{\mathrm{s}}\right) & =E\left(\mathrm{Si}_{65}^{+2}\right)+E\left(\mathrm{Si}_{63} \mathrm{~B}^{-1}\right) \\
& -E\left(\mathrm{Si}_{64} \mathrm{~B}^{+1}\right)-E\left(\mathrm{Si}_{64}\right),
\end{aligned}
$$

Where $\mathrm{Si}_{63} \mathrm{~B}^{-1}$ is the substitutional B configuration at $-1$ charge state in a 64-atom supercell and $\mathrm{Si}_{64} \mathrm{~B}^{+1}$ is the B-Si complex at $+1$ charge state in a 65-atom supercell. The binding energy is calculated to be $0.22$ eV. The present result concerns charged state and is therefore different from the result of Ref. [15] where neutral configurations are used for both the initial and final state of the reaction. The energy gain is primarily due to electrostatic interaction between $B_s^{-1}$ and $S_i^{+2}$ and to stress compensation.

In the case of $-1$ charged state, the lowest energy B-I configuration is the hexagonal B interstitial configuration where the B atom stays at the hexagonal interstitial site. As discussed later, this configuration is stable for $n$-doped Si. The binding energy can be similarly derived using the above formula. In this case, however, the reference configuration for $\mathrm{Si}_{\mathrm{i}}$ should be the neutral $\langle 110\rangle$-split configuration which is the lowest energy configuration for the $n$-doped material. With neutral $\mathrm{Si}_{\mathrm{i}}$ interstitial and $-1$ charged $B_s$ to be the reference energies, the binding energy is calculated to be $0.16$ eV.

In the case of the neutral B-I configuration, the situation is complex and is still controversial. Our minimum energy search resulted in a configuration similar to that of $+1$ charge state configuration where the B atom stays substitutionally and the Si atom stays near an interstitial T site which is a nearest neighbor to the substitutional B atom. However, this configuration is not stable if the charge state is allowed to change, i.e., at almost any Fermi level position, the positively charged configuration is always lower in energy than the neutral configuration. For the neutral system, both Tarnow [7] and Watkins et al. [20] have proposed several configurations. All of them are either metastable or unstable with the current calculation. It is possible, however, that one or more of those configurations are observed experimentally [20] due to kinetics, even though they are only metastable.

We have also studied the Fermi level dependence for the $B_s$-$S_i$ pair. The result is illustrated in Fig. 2 where the total energies of various configurations and charge states of $B_s$-$S_i$ pairs are shown as a function of the Fermi level position. The energy of the $B_s$ in the $-1$ charge state is used as a reference energy and is substracted from the energy plotted in order to reflect the formation energy change due to $E_{\text{Fermi}}$. Therefore, the $-1$ charged states have a constant energy, which is shown in Fig. 2. This is different from the case of the Si self-interstitial where only the bulk Si atom energy (which is neutral) is used as the reference energy. In the case of $p$-doped situation, the $+1$ charged $B_s$-$S_i$ pair configuration is the lowest energy configuration whereas in the case of $n$-doped situation, the $-1$ charged hexagonal $\mathrm{B}_{\mathrm{i}}$ has the lowest energy. As discussed previously, the neutral configuration is not stable in any Fermi level position and therefore is not shown in this figure.

The tetrahedral B interstitial configuration is always higher in energy than the lowest energy configuration at any Fermi level position. However, it does play an important role in B interstitial

![](./images/812409860074242048_3.jpg)

Fig. 2. B interstitial configuration formation energy diagram as a function of the Fermi level position. Energy zero for the configuration energy is arbitrarily set to be that of the hexagonal interstitial in the $-1$ charge state. The energy zero for the Fermi energy is that of the valence band maximum.

migration. We will discuss the result for $p$-doped materials, leaving a more general case for a future publication. In $p$-doped materials, the migrational path is a little complex due to the fact that the lowest energy configuration for $p$-doped material is that of the positively charged $\text{B}_\text{s}$–$\text{S}_\text{i}$ complex. The $\text{B}_\text{s}$ atom is first being kicked out into the interstitial region with a kick-out barrier of 1.1 eV. Then, the B interstitial can migrate along the tetrahedral–hexagonal–tetrahedral path with a much smaller migrational barrier of about 0.2 eV, even though the T and H boron interstitial is about 0.7 and 0.9 eV higher than the $\text{B}_\text{s}$–$\text{S}_\text{i}$ complex described above. The reverse kick-out barrier for it to revert back to a $\text{B}_\text{s}$–$\text{S}_\text{i}$ complex is about 0.4 eV.

Regardless of actual mechanisms for interstitial B migration, compared to nearly 5-eV migrational barrier for a concerted exchange mechanism without Si interstitials [6], the presence of excess interstitial flux greatly reduces the migrational barrier for B and increases B diffusivities which is the primary cause for boron TED. The enhancement of B diffusivity should increase with increasing Si interstitial density, which is why the enhancement is the largest near the surface or implanted region and steadily decreases as the position of the B marker layer is deeper inside the bulk [3].

The activation energy for B diffusion at equilibrium condition for the self-interstitial mechanism is calculated to be 4.3 eV for intrinsic Si, using the GGA self-interstitial formation energy. This energy is higher than the experimental range of 3.4–3.8 eV. In this case, the use of GGA formation energy makes the comparison with experiment worse since the LDA formation energy is 0.5 eV lower. The vacancy mechanism, on the other hand, has an activation energy of about 5.9 eV, clearly unfavorable for the B diffusion. The pre-factors are hardly an issue here since the activation energy difference is large and the pre-factor of the interstitial mechanism is usually larger than that of the vacancy mechanism.

### 3.4. Boron pair

At higher B concentration and therefore heavily $p$-doped, B dopant clusters will aslo become important, especially in the presence of a large excess of self-interstitials, which leads to a large number of mobile B atoms. Therefore, we have also carried out a study of a mobile $\text{B}_\text{i}$ bound to a $\text{B}_\text{s}$. This is likely the first step for B clustering. We have identified the lowest-energy configuration to be two B atoms displaced along a $\langle 0\ 0\ 1\rangle$ direction occupying one lattice site. The B–B pair forms a very strong bond of length about 68% of ideal Si–Si bond length. We note that in this configuration, each B has three nearest neighbors while all Si atoms have four nearest neighbors. This is nearly the ideal coordination for both B and Si atom in a covalent bonding environment. The pairing process in $p$-doped material can be described by the following reaction:
$$
\text{B}_\text{s}\text{Si}_\text{i}^{+1} + \text{B}_\text{s}^{-1} \to \text{B}_\text{i}^{+1} + \text{B}_\text{s}^{-1} \to \text{B}_\text{i}\text{B}_\text{s},
$$
i.e., a positively charged $\text{B}_\text{s}$–$\text{S}_\text{i}$ complex becomes mobile likely through a “kick-out” mechanism and then binds with a substitutional B, forming a neutral $\text{B}_\text{i}$–$\text{B}_\text{s}$ pair. Using the lowest energy for each configuration , we found that this reaction has an energy gain of 0.9 eV. Combined with 0.2-eV binding energy for the pairing of interstitial Si and substitutional B, the total energy gain for the reaction
$$
\text{Si}_\text{i}^{+2} + \text{B}_\text{s}^{-1} + \text{B}_\text{s}^{-1} \to \text{B}_\text{s}\text{Si}_\text{i}^{+1} + \text{B}_\text{s}^{-1} \to \text{B}_\text{i}\text{B}_\text{s}
$$
is 1.1 eV. This reaction is limited by the density of free Si interstitials as well as the B density and can only go significantly forward on the condition of both a large enough local B density and large amount of mobile Si interstitials. The resulting $\text{B}_\text{i}$–$\text{B}_\text{s}$ pair is relatively immobile due to its binding energy as well as its strong bonding with its neighboring Si atoms. It is impossible to find a migration path that only breaks one or two bonds while still keeping two B atoms together. Moreover, this $\text{B}_\text{i}$–$\text{B}_\text{s}$ pair is also found to be electrically inactive.

The current results are consistent with recent TED experiment using $\delta$-doped super-lattices, which found immobile and electrically inactive B regions [3]. These immobile B regions were found in the B marker layers closest to the surface where the Si interstitial flux is the highest, and also in the B implanted region where large implant doses

provided both the large interstitial flux and large local B concentration required for the reaction to go forward. However, the 0.9 eV binding energy is not consistent with the high temperature dissolv- ing rate of the immobile B region, suggesting the presence of larger B clusters. Our preliminary re- sults indicate that much larger binding energies can be obtained by having three or four possibly more B atoms in a single B cluster. There are aslo experimental limits on how many B atoms can be in a single cluster as the B clusters were not de- tectable in high resolution cross-section TEM, suggesting that the clusters only contain a few B atoms.

The B clustering results also imply that a Si interstitial is trapped during the process of forming a B-B pair. We have also looked at the possibility that a Si interstitial is ejected back to the Si lattice while forming a B-B pair. In this case, both B atoms should be substitutional and the formation process can be expressed as

$$\mathrm{B}_{\mathrm{s}} \mathrm{S}_{\mathrm{i}}^{+1}+\mathrm{B}_{\mathrm{s}}^{-1} \rightarrow \mathrm{B}_{\mathrm{s}} \mathrm{B}_{\mathrm{s}}^{-2}+\mathrm{Si}_{\mathrm{i}}^{+2}.$$

We have found that the lowest energy configu- ration for a $B_s$-$B_s$ pair is two B atoms occupying neighboring lattice site relaxing towards each other to form a strong B-B bond. Another con- figuration with these two B atoms relaxing away from each other, therefore unbonded, is also metastable when it is neutral. However, it becomes unstable when it traps additional electrons which quickly go to the bonded configuration with -2 charge state. Our calculations show that the above reaction will have a energy cost of 0.8 eV, com- pared to an energy gain of 0.9 eV if the Si inter- stitial is trapped in the $B_i$-$B_s$ pair. Furthermore, the resulting $B_s$-$B_s$ pair is still electrically active, contrary to the experimental finding. Therefore, the present calculation does not favour the im- portance of reejecting all Si interstitials during the B clustering process. Our prelimary results for larger-sized clusters also confirm this trend.

### 3.5. Interstitial C and its diffusion

We now turn to the effect of C impurity on boron TED. Under equilibrium conditions and the dilute limit, carbon atoms are at substitutional sites in the Si diamond crystal lattice and are electrically inactive at their neutral charge state. In our calculation with a supercell containing 63 Si atoms and one substitutional C atom, we have found that the nearest neighbour Si atom relaxes towards the substitutional C atom by about 14.6% of the ideal Si-Si bond length which is still 6% longer than the ideal C-Si bond length such as in silicon carbide. The four C-Si bonds are highly stretched, which allows the possibility for the C atom to share the same lattice site with another atom to shorten the C-Si bond length and reduc- ing the strain to the surrounding lattice, therefore lowering the energy. It is indeed true in the case of C interstitial.

The lowest energy configuration formed by a C interstitial in Si has been studied both experimen- tally [21,22] and theoretically [8]. In this configu- ration, both the C and Si atoms displace along a [0 0 1] direction sharing one single lattice site. The C-Si bond is relaxed due to the additional Si atom, lowering the total energy. The binding energy of this $C_i$ relative to well separated neutral $Si_i$ and $C_s$ is 1.45 eV and can be calculated by

$$E_{\mathrm{b}}\left(\mathrm{C}_{\mathrm{i}}\right)=E\left(\mathrm{Si}_{65}\right)+E\left(\mathrm{Si}_{63} \mathrm{C}\right)-E\left(\mathrm{Si}_{64} \mathrm{C}\right)-E\left(\mathrm{Si}_{64}\right),$$

where $Si_{63}C$, $Si_{64}C$, $Si_{65}$ and $Si_{64}$ are the C substi- tutional, $\langle 0\ 0\ 1\rangle$ C interstitial, $\langle 1\ 1\ 0\rangle$ Si interstitial and bulk Si energies in their respective 64-atom supercells.

The C interstitial can migrate under a migration mechanism [8] which goes through an intermediate configuration of $C_2$ symmetry where the C atom is bonded to four Si atoms. Three of the Si atoms are neighbors from the initial configuration with the remaining Si atom from the final configuration. Since the orientation of the split C-Si pair also changes after one migrational step, both the re- orientation and migration processes should over- come the same energy barrier for this mechanism. Furthermore, during the migrational process of such as C-Si pair, the Si atom remains in its original lattice site while the C atom changed its lattice position. Therefore, the C interstitial diffu- sion does not affect Si self-diffusion under equi- librium conditions.

Using a 65-atom supercell, we have found the intermediate configuration is 0.5 eV higher in

energy than the $\langle 0\ 0\ 1\rangle$ C interstitial, resulting a migrational barrier of at least 0.5 eV. This result agrees with the 32-atom supercell atom result of 0.51 eV [8], but it still 0.2–0.4 eV lower than the 0.73–0.88 eV experimental range. It is noted that the above C interstitial migration mechanism is different from the standard kick-out mechanism, which played an important role in B diffusion, where the dopant atom is kicked out by the $\text{Si}_i$ and then migrate within the interstitial region through the T and H sites. However, in the case of C, the B type kick-out mechanism will have a migration barrier of at least 2.3 eV which is the energy difference between T and $\langle 0\ 0\ 1\rangle$ interstitial calculated using a 32-atom supercell.

With those energetics, we can also calculate the total activation energy for the interstitial assisted C diffusion under equilibrium conditions. The activation energy can be calculated by
$$
E_{\mathrm{a}}=E_{\mathrm{f}}\left(\mathrm{Si}_{\mathrm{i}}\right)-E_{\mathrm{b}}\left(\mathrm{C}_{\mathrm{i}}\right)+E_{\mathrm{m}}\left(\mathrm{C}_{\mathrm{i}}\right).
$$

If we use the GGA formation energy of the Si self-interstitial and the experimental $\text{C}_i$ migration energy of 0.8 eV, the above formular gives 3.05 eV as compared to the 3.04 eV activation energy measured experimentally [23]. Clearly, in this case, the use of GGA formation energy improves the agreement between the theory and experiment.

### 3.6. Interstitial C and substitutional C pair

At high C concentration with enough mobile $\text{C}_i$, a substantial amount of $\text{C}_i$–$\text{C}_s$ pair may also be formed. The $\text{C}_i$–$\text{C}_s$ impurity is a bi-stable system with two configurations of similar energies. Their structures have been identified experimentally [24]. The low energy one for the neutral state (Configurations A) ia an off-axis bond center configuration with the two C atoms on the lattice sites and one Si atom sitting in between. The other configuration (Configuration B), with only 0.15 eV higher in energy, is the same as a $\langle 0\ 0\ 1\rangle$ $\text{C}_i$ except that a C atom replaces one of the Si atom bonds to the Si atom in the C–Si pair. A simple bond switching differentiates between Configuration A and B. The barrier to convert B to A is calculated to be only 0.15 eV, very small considering the theoretical errorbar of the similar amount.

The binding energy of the $\text{C}_i$–$\text{C}_s$ pair relative to a neutral $\text{C}_i$ and a $\text{C}_s$ well seperated is 1.0 eV and can be calculated by
$$
\begin{aligned}
E_{\mathrm{b}}\left(\mathrm{C}_{\mathrm{i}} \mathrm{C}_{\mathrm{s}}\right)= & E\left(\mathrm{Si}_{64} \mathrm{C}\right)+E\left(\mathrm{Si}_{63} \mathrm{C}\right) \\
& -E\left(\mathrm{Si}_{63} \mathrm{C}_{2}\right)-E\left(\mathrm{Si}_{64}\right),
\end{aligned}
$$
where $\text{Si}_{64}\text{C}$, $\text{Si}_{63}\text{C}$, $\text{Si}_{63}\text{C}$ and $\text{Si}_{64}$ are the $\langle 0\ 0\ 1\rangle$ C interstitial, C substitutional, C interstitial and C substitutional pair and bulk Si energies in their respective 64-atom supercells. The binding energy of 1.0 eV is in addition to the 1.45 eV binding energy when $\text{C}_s$–$\text{Si}_i$ is formed from a $\text{C}_s$ and a free $\text{Si}_i$. Therefore, the total energy gain from the following reaction
$$
\mathrm{Si}_{\mathrm{i}}+\mathrm{C}_{\mathrm{s}}+\mathrm{C}_{\mathrm{s}} \rightarrow \mathrm{C}_{\mathrm{i}}+\mathrm{C}_{\mathrm{s}} \rightarrow \mathrm{C}_{\mathrm{i}} \mathrm{C}_{\mathrm{s}}
$$
is 2.45 eV. Clearly, with a large C concentration, the above reaction will contribute to Si interstitial trapping.

Another possible mechanism which will compete with Si interstitial trapping is for the $\text{C}_i$–$\text{C}_s$ pair to release Si interstitial, leaving behind a $\text{C}_s$–$\text{C}_s$ pair. We have also studied such a possibility. Similar to $\text{B}_s$ pairs, the $\text{C}_s$ pairs can also have two configurations when the two $\text{C}_s$ atoms are within nearest neighbor distance. The two C atoms can either relax toward each other which forms a strong C–C bond and each of the two C atoms are 4-fold coordinated or, relax away from each other which forms no C–C bond and therefore each of the two C atoms are 3-fold coordinated. We found that both configurations are at least metastable with the 4-fold coordinated configuration has the lower energy. However, if we compare this configuration with two $\text{C}_s$ atom seperated well apart, we find that it actually cost 1.6 eV to bring two $\text{C}_s$ atoms to the nearest neighbor distance. Furthermore, the energy cost of the reaction
$$
\mathrm{C}_{\mathrm{i}} \mathrm{C}_{\mathrm{s}} \rightarrow \mathrm{Si}_{\mathrm{i}}+\mathrm{C}_{\mathrm{s}} \mathrm{C}_{\mathrm{s}}
$$
is an almost prohibitive 4.0 eV, if the nearest neighbor $\text{C}_s$–$\text{C}_s$ pair energy is used. Therefore, it is also highly unlikely for the $\text{C}_i$–$\text{C}_s$ pair to form a $\text{C}_s$–$\text{C}_s$ pair and free the Si interstitial back into the bulk, preventing the interstitial to participate in the TED.

### 3.7. Suppression of B transient enhanced diffusion

We now try to understand the effects of C on the TED using the above ab initio results. It is clear that the key for the suppression of TED is the reduction of the free Si interstitiaa concentration. We believe that several factors will play important roles in this respect. The free Si interstitial can be first trapped by a C substitutional to form a C interstitial with a binding energy of 1.45 eV. This should be one of the primary reasons that free interstitial concentration is reduced in the presence of C. Additionally, the C interstitial is very mobile with an experimentally measured migrational barrier of about 0.8 eV. Compared to a fixed trap, the C interstitial, which is a mobile trap for Si interstitials, has the additional effect which allows the transport of interstitials from high concentra- tion to low concentration region, further reducing the free Si interstitial concentration at the higher concentration region (where TED is significant). Furthermore, the mobile C interstitial can bind to another C substitutional at high C concentration with a binding energy of 1.0 eV, providing addi- tional trapping of the Si interstitial. C clusters in- volving more C atoms are also possible at high C concentrations and may affect Si interstitial trap- ping. Of course, other impurities may also be im- portant in trapping the C interstitial.

### Acknowledgements

The author would like to acknowledge Dr. M. Tang and Dr. L. Colombo for carrying out the tight-binding calculation. Additionally the collab- orations with Dr. T. Diaz de la Rubia, Dr. L.H. Yang, Dr. G.H. Gilmer and Dr. C. Mailhiot in the above work are also gratefully acknowledged. This work was performed under the auspices of the US Department of Energy by the Lawrence Livermore National Laboratory under contract No. W-7405- ENG-48.

### References

[1] P.M. Fahey, P.B. Griffin, J.D. Plummer, Rev. Mod. Phys. 61 (1989) 289.

[2] A.E. Mitchel, Nucl. Instr. Meth. B 37/38 (1989) 379.

[3] P.A. Stolk, D.J. Eaglesham, H.J. Gossmann, J.M. Poate, Appl. Phys. Lett. 66 (1995) 1370.

[4] L. Pelaz, G.H. Gilmer, M. Jaraiz, H.J. Gossmann, C.S. Rafferty, D.J. Eaglesham, J.M. Poate, Mat. Res. Soc. Symp. Proc. 469 (1997) 341.

[5] M. Caturla, T. Diaz de la Rubia, J. Zhu, M. Johnson, Mat. Res. Soc. Symp. Proc. 469 (1997) 335.

[6] C.S. Nichols, C.G. Van de Walle, S.T. Pantelides, Phys. Rev. Lett. 62 (1989) 1049; Phys. Rev. B 40 (1989) 5484.

[7] E. Tarnow, Europhys. Lett. 16 (1991) 449; E. Tarnow, J. Phys.: Condens. Matter 4 (1992) 5405.

[8] R.B. Capaz, A. Dal Pino, Jr., J.D. Joannopoulos, Phys. Rev. B 50 (1994) 7439.

[9] D.M. Ceperley, B.J. Alder, Phys. Rev. Lett. 45 (1980) 566.

[10] J.P. Perdew, A. Zunger, Phys. Rev. B 23 (1981) 5048.

[11] N. Troullier, J.L. Martins, Phys. Rev. B 43 (1991) 1993.

[12] L. Kleinman, D.M. Bylander, Phys. Rev. Lett. 48 (1982) 1425.

[13] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.

[14] W. Kohn, L.J. Sham, Phys. Rev. 140 (1965) A1133.

[15] J. Zhu, T. Diaz de la Rubia, L.H. Yang, C. Mailhiot, G.H. Gilmer, Phys. Rev. B 54 (1996) 4741.

[16] H.R. Schober, Phys. Rev. B 39 (1989) 13013.

[17] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Perderson, D.J. Singh, C. Fiolhais, Phys. Rev. B 46 (1992) 6671; 48 (1993) 4978.

[18] M. Tang, L. Colombo, J. Zhu, T. Diaz de la Rubia, Phys. Rev. B 55 (1997) 14279.

[19] U. Gösele, A. Plößl, T.Y. Tan, in: G.R. Srinivasan, C.S. Murthy, S.T. Dunham (Eds.), Process Physics and Modeling in Semiconductor Technology, Electrochemical Society, Pennington, NJ, 1996, p. 309.

[20] G.D. Watkins, Phys. Rev. B 12 (1975) 5824; G.D. Watkins, private communication.

[21] G.D. Watkins, K.L. Brower, Phys. Rev. Lett. 36 (1976) 1329.

[22] L.W. Song, G.D. Watkins, Phys. Rev. B 42 (1990) 5759.

[23] F. Rollert, N.A. Stolwijk, H. Mehrer, Proceedings of 15th International Conference on Defects in Semiconductors, Budapest, 1998.

[24] L.W. Song, X.D. Zhan, B.W. Benson, G.D. Watkins, Phys. Rev. B 42 (1990) 5765.