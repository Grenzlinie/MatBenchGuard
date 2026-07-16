# First-principles prediction of point defect energies and concentrations in the tantalum and hafnium carbides

I. Khatri, R. K. Koju, and Y. Mishin

July 9, 2024

Department of Physics and Astronomy, MSN 3F3, George Mason University, Fairfax, Virginia 22030, USA

## Abstract
First-principles calculations are combined with a statistical-mechanical model to predict the equilibrium point-defect concentrations in the refractory carbides TaC and HfC as a function of temperature and chemical composition. Several different types of point defects (vacancies, interstitials, antisite atoms) and their clusters are treated in a unified manner. The defect concentrations either strictly follow or can be closely approximated by Arrhenius functions with parameters predicted by the model. The model is general and applicable to other carbides, nitrides, borides, or similar chemical compounds. Implications of this work for understanding the diffusion mechanisms in TaC and HfC are discussed.

Keywords: Refractory carbides; density-functional-theory; statistical mechanics; point defects; atomic diffusion.

## 1 Introduction
The refractory carbides TaC and HfC belong to the class of ultra-high temperature ceramics (UHTCs), which includes several other transition metal carbides, nitrides, and borides. UHTCs are characterized by a high melting temperature, large elastic moduli, large hardness, good thermal resistance, and relatively low chemical reactivity. The TaC and HfC carbides have the highest melting temperatures $T_{\rm m}$ among all UHTCs. In fact, HfC has

the highest melting temperature (about 3942°C) of all materials known today, with TaC's $T_{\text{m}}$ being only slightly lower (about 3900°C) [1].

Both carbides have the B1-ordered (NaCl prototype) crystal structure with significant deviations from the 50-50 stoichiometry towards carbon-deficient compositions. This off-stoichiometry is accommodated by constitutional (structural) vacancies on the carbon sublattice. The chemical bonding in TaC and HfC combines three contributions: metallic bonding due to the presence of the metallic atoms, covalent metal-carbon bonds, and some degree of ionic bonding caused by partial metal-carbon charge transfer [2]. The covalent bonds are the strongest, making both carbides mechanically strong, hard and brittle, leading to the high melting temperatures.

The TaC and HfC carbides are notoriously difficult to sinter due to the extremely small diffusion coefficients. The rate of pore healing during the sintering is kinetically controlled by diffusive mass transport. Thus, the knowledge of diffusion coefficients in TaC and HfC is essential for optimizing the synthesis and processing routes. Experimental information about the diffusivity of either carbon or the metallic atoms in these carbides is scarce and indirect. Diffusion measurements are highly challenging as they must be conducted at temperatures exceeding 2000-2800°C to generate reliable concentration curves from which to extract the diffusion coefficients. Carbon diffusion in TaC was estimated by back-calculation from the growth rate of an oxide layer [3, 4] or carbide layer [5]. Interdiffusion coefficients in TaC and HfC were extracted from evaporation data [6]. No experimental data is available for metal self-diffusion in TaC or HfC.

Under the circumstances, calculations offer the only realistic option for obtaining the diffusivities in these carbides (and perhaps all other carbides of the UHTC family). Point-defect concentrations constitute an essential ingredient for the diffusion calculations. Density-functional theory (DFT) calculations have been performed for vacancies and vacancy clusters in TaC [2, 7–15] and HfC [14, 15]. Based on these and other calculations [7–11, 14, 16], it is assumed that both carbon and metallic atoms in TaC and HfC diffuse by vacancy-atom exchanges on the respective sublattices. Among other findings, it was predicted that the binding energy between the carbon and metal vacancies in HfC is much stronger than in TaC, leading to the formation of vacancy clusters in which a Hf vacancy is surrounded by several carbon vacancies [15]. However, thermodynamically consistent calculations of the point-defect (and point-defect cluster) formation energies and equilibrium concentrations have been challenging. Such calculations must consider that point defects can only appear and disappear by pairs or clusters that preserve the chemical composition. Furthermore, different defect clusters must be in equilibrium with each other with respect to composition-conserving dissociation-recombination reactions. The only consistent treatment known to

us was for vacancies and antisite defects in the Ti, Zr and Hf carbides and nitrides [16].

This paper aims to predict point-defect concentrations in TaC and HfC as a function of temperature and deviation from stoichiometry. To this end, we develop a methodology that combines DFT calculations with statistical mechanics accounting for the point-defect energies and entropies, including both configurational and orientational entropy contribu- tions. This allows us to predict the equilibrium concentrations of single point defects and point-defect clusters of any complexity. The methodology is general enough to apply to other B1-ordered carbides, nitrides, or borides in the future.

## 2 Methodology

The point defect energies were obtained by DFT calculations using the Vienna Ab initio Simulation package (VASP) [17, 18]. The calculations were carried out using six different cubic or orthorhombic supercells containing 96, 144, 216, 288, 384, and 512 atoms, ob- tained by replicating the conventional 8-atom unit cell of the B1 structure. Using large supercell sizes with up to 512 atoms ensured size convergence, which was especially impor- tant for large defect clusters creating strong elastic strain fields. The convergence plots are presented in the Supplementary Information file accompanying this article. The projected augmented wave [19] method was utilized with exchange-correlation interactions treated in the generalized gradient approximation in the Perdew-Burke-Ernzerhof formalism [20, 21]. The semi-core $p$ electrons were included as valence states for both Ta and Hf. Following convergence test, the energy cutoffs of 780 eV and 860 eV were applied to HfC and TaC, respectively. The k-point grid convergence tests were conducted for all supercells; see the Supplementary Information file. A Gaussian smearing of width 0.05 eV was chosen to perform electron minimization with the convergence criterion of $10^{-8}$ eV/atom. For ionic relaxations, we used a conjugate-gradient algorithm with the 0.001 eV/Å force criterion, followed by a quasi-Newton algorithm to further improve accuracy. Before introducing defects, each supercell was subjected to volumetric relaxation while preserving its original shape. The point defects were created by adding, removing, or changing the species of an atom or a group of atoms, and the structures were relaxed with respect to local atomic displacements.

Prior to the point-defect calculations, perfect lattice properties of both carbides were computed to demonstrate the reliability of the DFT methodology. Table 2 shows that the lattice parameter $a$ and elastic constants $c_{ij}$ obtained by our calculations compare well with the available experimental [22-24] and theoretical [11, 14, 25, 26] values. The elastic constants were computed by the energy-strain method using second order polynomial fits

for strains below 6%.

The obtained energies of the perfect and defected supercells served as input to the statistical-mechanical model for calculating the equilibrium point-defect concentrations as explained below.

## 3 Point-defect energies

The B1 structure of the TaC and HfC carbides consists of two penetrating face-centered cubic (FCC) sublattices occupied by metallic and carbon atoms. In the perfectly stoichio- metric carbides at zero temperature, the two sublattices are filled with the respective atoms without vacancies. At finite temperatures, a stoichiometric carbide develops thermal dis- order in the form of vacancies on both sublattices, antisite defects, interstitial atoms, and clusters of these defects. Deviations from the perfect stoichiometry are accommodated by additional point defects called constitutional (or structural). Depending on the chemical composition and temperature, the disorder is dominated by either thermal or constitutional defects. At low temperatures, the defects are primarily constitutional and can be different on either side of the stoichiometric composition. They can also be different between TaC and HfC.

To analyze the point defects in both carbides in a unified manner, we will consider a generic carbide AB, in which the element A is either Ta or Hf and the element B is carbon. The respective FCC sublattices are denoted $\alpha$ and $\beta$. This generalized notation will allow us to apply the present analysis to other binary carbides or any ordered compound with the AB stoichiometry in the future.

There can be six types of elementary (single) point defects:

$V_\alpha =$ vacancy on sublattice $\alpha$

$V_\beta =$ vacancy on sublattice $\beta$

$A_\beta =$ antisite atom A on sublattice $\beta$

$B_\alpha =$ antisite atom B on sublattice $\alpha$

$I_A =$ interstitial metallic atom

$I_B =$ interstitial carbon atom

An antisite defect is obtained by replacing a metallic atom with carbon on the metallic sublattice $(B_\alpha)$ or a carbon atom with a metallic atom on the carbon sublattice $(A_\beta)$. Interstitial atoms are inserted in a tetrahedral position.

The elementary defects can form dynamic clusters. The simplest cluster is a pair of elementary defects separated by a nearest-neighbor distance $r_0$. Examples include divacancies $V_\alpha V_\beta$, antisite pairs $A_\beta B_\alpha$, and vacancy-antisite pairs such as $V_\alpha B_\alpha$ and $V_\beta A_\beta$. In the divacancy and the antisite pairs, the elementary defects are nearest neighbors on different sublattices ($r_0 = a/2$), whereas in the vacancy-antisite pairs $V_\alpha B_\alpha$ and $V_\beta A_\beta$, they are nearest neighbors on the same sublattice ($r_0 = a/\sqrt{2}$). Another defect pair, called a Frenkel pair, is composed of a vacancy and interstitial atom. This defect is obtained by moving an atom from its sublattice to an interstitial position. Defect clusters can be composed of three or more elementary defects and can have several geometric configurations.

DFT calculations produce a set of "raw" energies [27-30] of point defects, both elementary and clustered. The "raw" energy of a point defect is *defined* as the energy difference between a relaxed supercell containing the defect and a perfect supercell containing the same number of sites. Specifically, the "raw" energy $\varepsilon_d$ of a defect $d$ is calculated by the formula

$$
\varepsilon_d = E_d(N) - E_0(N), \tag{1}
$$

where $E_d(N)$ and $E_0(N)$ are the total energies of an $N$-site supercell with and without the defect, respectively. Since the two supercells can have different chemical compositions, the "raw" energy generally depends on the reference atomic energy used in the DFT calculations. Exceptions include the antisite pairs $A_\beta B_\alpha$, Frenkel defects such as $V_\alpha I_A$ and $V_\beta I_B$, and other defects obtained by displacing atoms from their perfect lattice positions without changing the chemical composition. In all other cases, the "raw" energy of the defect is not a physically meaningful quantity by itself. However, it can be shown [27-30] that a complete set of "raw" energies, together with the cohesive energy $\varepsilon_0$ of the perfect crystal (potential energy per atom relative to ideal gas) uniquely defines the equilibrium point-defect concentrations. Such concentrations are calculated using the statistical-mechanical model discussed in section 4, which uses the "raw" energies as input.

Table 3 summarizes the "raw" energies of the elementary defects and several defect clusters in both carbides. The "raw" energy of each defect was determined by linear extrapolation to zero of the values obtained in different supercells when plotted against the reciprocal of the number of sites, as proposed in Ref. [31]. The plots are shown in the Supplementary Information file. Some of the geometrically possible defect clusters are mechanically unstable and are not included in Table 3. For example, the vacancy-antisite pair $V_\alpha A_\beta$ is unstable in both carbides: during the relaxation, the antisite atom $A_\beta$ fills the vacancy and the pair transforms into a carbon vacancy $V_\beta$. The vacancy-antisite pair $V_\beta B_\alpha$ in TaC is also unstable and relaxes into a metallic vacancy $V_\alpha$. However, in HfC, the same pair survives relaxation and transforms into a linear structure consisting of a di-

vacancy $V_{\alpha}V_{\alpha}$ and a carbon interstitial dumbbell $I_{B}$ aligned parallel to the [110] direction (Fig. 1(a)). As another example, the metallic Frenkel pair $V_{\alpha}I_{A}$ comprising a vacancy and a tetrahedral interstitial is unstable in both carbides: during the relaxation, the interstitial atom fills the vacancy, recovering the perfect crystal. The carbon Frenkel pair $V_{\beta}I_{B}$ is likewise unstable in TaC but remains stable in HfC.

In some of the defect pairs, the relaxation is accompanied by small atomic displacements preserving the initial elementary defects. For example, the relaxed divacancies $V_{\alpha}V_{\beta}$ in both carbides are composed of two distinct vacancies. In other cases, the defect pair undergoes a significant reconstruction. For example, during the relaxation of the $V_{\alpha}B_{\alpha}$ pair, the antisite carbon atom $B_{\alpha}$ shifts into an interstitial position, leaving a metallic vacancy behind.¹ As a result, the initial defect pair relaxes into a linear structure comprising a metallic divacancy $V_{\alpha}V_{\alpha}$ and a carbon interstitial $I_{B}$ in between (Fig. 1(b)). The antisite pair $A_{\beta}B_{\alpha}$ also reconstructs upon relaxation: the antisite carbon atom $B_{\alpha}$ relaxes toward a nearby carbon site while the antisite metallic atom $A_{\beta}$ relaxes toward a metallic site, creating a linear structure consisting of a metallic vacancy and a carbon interstitial dumbbell with the [110] orientation (Fig. 1(c)). As yet another example, the $V_{\beta}A_{\beta}$ pair in TaC relaxes into a carbon divacancy $V_{\beta}V_{\beta}$ and a chain of three metallic atoms in a criss-cross configuration (Fig. 1(d)).

In addition to the divacancy $V_{\alpha}V_{\beta}$, Table 3 includes the "raw" energies of vacancy clusters $V_{\alpha}V_{\beta}^{n}$, $n=2,...,6$, obtained by adding up to six carbon vacancies as nearest neighbors of the metallic vacancy. The structures with $n=2$, 3 and 4 can have several symmetrically non-equivalent configurations with different energies. The $V_{\alpha}V_{\beta}^{2}$ cluster can have a triangular (T) or linear (L) configuration described in Ref. [15]. In the $V_{\alpha}V_{\beta}^{3}$ cluster, the carbon vacancies can form an in-plane (IP) or off-plane (OP) configuration [15]. In the $V_{\alpha}V_{\beta}^{4}$ cluster, the two occupied nearest-neighbor carbon sites of $V_{\alpha}$ can be in either L or T configuration. Accordingly, the four carbon vacancies can form an IP or an OP configuration [15]. By contrast, all configurations of the $V_{\alpha}V_{\beta}^{5}$ and $V_{\alpha}V_{\beta}^{6}$ clusters are symmetrically equivalent. In the latter case, all nearest-neighbor sites of $V_{\alpha}$ are vacant.

The binding energies of the elementary defects into the clusters were also calculated. The binding energy is defined as the "raw" energy difference between the cluster and a system of isolated elementary defects forming the cluster. This energy can be calculated using a supercell containing the cluster and a set of supercells containing the elementary defects. The respective supercell energies must be appropriately scaled to ensure the con- servation of the total number of sites [16]. In contrast to the "raw" energies, the binding

---
¹This interstitial position is at the midpoint of the nearest-neighbor C-C bond in the B1 structure and cannot be classified as either tetrahedral or octahedral. It is unique to this reconstructed structure.

energy is a well-defined physical quantity independent of reference energies. A negative binding energy indicates that the elementary defects attract each other when forming the cluster.

The binding energies obtained by the DFT calculations are reported in Table 4. Note that the divacancy and the antisite pair are bound much stronger in HfC than in TaC. In TaC, the vacancies are weakly bound into $V_\alpha V_\beta^n$ clusters when $n \leq 3$ and unbound (positive binding energy) in $V_\alpha V_\beta^4$, $V_\alpha V_\beta^5$ and $V_\alpha V_\beta^6$. The most stable vacancy cluster is $V_\alpha V_\beta^2$ with the linear configuration (binding energy $-0.26$ eV). In other words, a metallic vacancy in TaC is most likely bound to two carbon vacancies but this binding is relatively weak. The same conclusion was previously reached in Refs. [16, 32]. In contrast, in HfC, the vacancy binding into $V_\alpha V_\beta^n$ clusters is strong and increases in magnitude with $n$, reaching the most negative value of $-5.49$ eV in $V_\alpha V_\beta^6$. Thus, the metallic vacancies in HfC are likely to be surrounded by up to six carbon vacancies as first neighbors. This conclusion is consistent with previous reports [16, 32].

As discussed by Razumovskiy et al. [16, 32], the vacancy binding into $V_\alpha V_\beta^n$ clusters results from competition between the attraction of carbon vacancies to the metallic vacancy and their repulsion from each other. Indeed, Fig. 2 shows the interaction energy between carbon vacancies as a function of separation. In both carbides, the interaction between the first and second neighbors is repulsive, and the repulsion between second neighbors is much stronger in HfC than in TaC. Nevertheless, this repulsion is overpowered by the attraction to the metallic vacancy, resulting in the strongly bound $V_\alpha V_\beta^n$ clusters in HfC.

It was shown [15] that in the $V_\alpha V_\beta^n$ clusters, a nearby C atom can jump into an intersti- tial position and leave a new carbon vacancy behind. In other words, a Frenkel pair $V_\beta I_B$ can form next to the $V_\alpha V_\beta^n$ cluster. In TaC, the energy increases in this process, indicating that the new Frenkel pair is energetically unfavorable. But in HfC, the energy decreases for certain Frenkel pair orientations. Thus, the $V_\alpha V_\beta^n$ clusters in HfC are unstable with respect to Frenkel pair formation in their vicinity. Further investigation of the $V_\alpha V_\beta^n - I_B$ structures in HfC was not pursued in this work.

## 4 Point-defect concentrations

This section discusses a statistical model of point defects in binary carbides with the B1 structure. As before, we consider a general carbide AB, where element A is a transition metal and element B is carbon. Off-stoichiometric carbides are described by the formula $\mathrm{A}_{1+x}\mathrm{B}_{1-x}$, where $x$ measures the deviation from the perfect stoichiometry. We consider slight deviations accommodated by small concentrations of point defects. Under this as-


sumption, interactions among the point defects can be neglected.

Several methods were proposed for calculating the equilibrium point-defect concen- trations in ordered compounds [27-30, 33]. Here, we follow the quasi-chemical method [27, 29], which gives the same results as all other methods but is more straightforward and transparent. The method was previously applied to compounds dominated by antisite disorder [27, 29] and vacancy disorder [16]. Here, we provide a general treatment without the presumption of a particular disorder mechanism.

The point defects are treated as an ideal gas mixture of several "chemical components" representing the different types of elementary point defects or their clusters. The equilib- rium defect concentrations at a temperature $T$ are calculated from two conditions:

- Equilibrium with respect to chemical reactions in the gas mixture
- Material balance preserving the given off-stoichiometry $x$

If the model considers $M$ defect types, then $(M-1)$ independent reactions must be chosen, with the material balance condition providing another equation.

The defects are assigned the chemical potentials
$$
\mu_{d}=\varepsilon_{d}+k_{B} T \ln \frac{X_{d}}{\sigma_{d}},\qquad(2)
$$
while the formula unit $AB$ is assigned the chemical potential $\mu_{A B}=2 \varepsilon_{0}$ ($k_B$ is Boltz- mann's constant). For single vacancies and antisite defects, $X_d$ denotes their fraction of the respective sublattice. For single interstitial atoms, $X_d$ is the occupied fraction on the available interstitial positions (interstices). Each defect cluster is assumed to contain at least one vacancy or one antisite. Let us call this vacancy/antisite the cluster center. The configurational entropy of the cluster considers all possible locations of its center on the respective sublattice. The cluster concentration is then defined as the fraction $X_d$ of the sublattice sites occupied by the cluster centers. In addition, for a given center location, the relaxed cluster structure can have $\sigma_d$ different orientations relative to the lattice with the same energy. This additional degeneracy of the micro-states contributes the orientational entropy $k_{B} \ln \sigma_{d}$ per cluster. This explains the appearance of the symmetry factor $\sigma_d$ in Eq.(2). For example, the vacancy-antisite pair $V_{\beta} B_{\alpha}$ in HfC shown in Fig. 1(a) can have six different orientations with equal energy, thus $\sigma_{d}=6$. In this case, either $V_{\beta}$ or $B_{\alpha}$ can be taken as the cluster center. For elementary defects $\sigma_{d}=1$. The symmetry factors for all defect clusters considered in this work are summarized in Table 4.

Although the chemical potentials of the defects are expressed through the "raw" energies, it can be shown [29] that all reference energies cancel out and do not affect the defect


concentrations predicted by this method. We emphasize that the model only includes the configurational and orientational micro-states and neglects the vibrational, electronic, and all other forms of free energy.

Although any choice of the $(M-1)$ reactions is equally legitimate, we find the following set of reactions most intuitive. For reactions among the six elemental defects, we choose

$$
V_{\alpha}+V_{\beta}=-A B,\tag{3}
$$

$$
B_{\alpha}+A_{\beta}=0,\tag{4}
$$

$$
V_{\alpha}=B_{\alpha}+V_{\beta},\tag{5}
$$

$$
V_{\alpha}+I_{A}=0,\tag{6}
$$

$$
V_{\beta}+I_{B}=0.\tag{7}
$$

In reaction (3), a vacancy pair is created by removing one formula unit of the carbide. In reaction (4), a pair of antisite defects is created without adding or removing atoms. In reaction (5), an atom B fills the vacancy $V_{\alpha}$, creating an antisite defect $B_{\alpha}$ and leaving a vacancy $V_{\beta}$ behind. Again, the system remains closed. Finally, reactions (6) and (7) describe the Frenkel pair formation by atoms A and B, respectively. For every cluster $d$ composed of elementary defects $d_{i}$, we write the dissociation-recombination reaction

$$
d=\sum_{i} d_{i}.\tag{8}
$$

It is assumed that the point defects participating in the reactions are separated well enough to neglect their interaction.

The equations describing dynamic equilibrium with respect to the defect reactions are obtained by replacing the defect symbols by the respective chemical potentials. The equations obtained have the form of the mass action law known from chemistry. In particular, reactions (3)-(7) yield the equations

$$
X_{V_{\alpha}} X_{V_{\beta}}=\exp \left(-\frac{\varepsilon_{V_{\alpha}}+\varepsilon_{V_{\beta}}+2 \varepsilon_{0}}{k_{B} T}\right),\tag{9}
$$

$$
X_{B_{\alpha}} X_{A_{\beta}}=\exp \left(-\frac{\varepsilon_{B_{\alpha}}+\varepsilon_{A_{\beta}}}{k_{B} T}\right),\tag{10}
$$

$$
\frac{X_{V_{\alpha}}}{X_{B_{\alpha}} X_{V_{\beta}}}=\exp \left(-\frac{\varepsilon_{V_{\alpha}}-\varepsilon_{B_{\alpha}}-\varepsilon_{V_{\beta}}}{k_{B} T}\right),\tag{11}
$$

$$
X_{V_{\alpha}} X_{I_{A}}=\exp \left(-\frac{\varepsilon_{V_{\alpha}}+\varepsilon_{I_{A}}}{k_{B} T}\right),
\tag{12}
$$

$$
X_{V_{\beta}} X_{I_{B}}=\exp \left(-\frac{\varepsilon_{V_{\beta}}+\varepsilon_{I_{B}}}{k_{B} T}\right).
\tag{13}
$$

Similarly, each cluster dissociation-recombination reaction (8) gives the equation

$$
\frac{X_{d}}{\prod_{i} X_{d_{i}}}=\sigma_{d} \exp \left(-\frac{\varepsilon_{d}-\sum_{i} \varepsilon_{d_{i}}}{k_{B} T}\right),
\tag{14}
$$

where the numerator $\varepsilon_{d}-\sum_{i} \varepsilon_{d_{i}}$ in the right-hand side has the meaning of the binding energy of the cluster. For example, for a vacancy cluster $V_{\alpha} V_{\beta}^{n}$ we have

$$
\frac{X_{V_{\alpha} V_{\beta}^{n}}}{X_{V_{\alpha}}\left(X_{V_{\beta}}\right)^{n}}=\sigma_{V_{\alpha} V_{\beta}^{n}} \exp \left(-\frac{\varepsilon_{V_{\alpha} V_{\beta}^{n}}-\varepsilon_{V_{\alpha}}-n \varepsilon_{V_{\beta}}}{k_{B} T}\right).
\tag{15}
$$

It is easy to see that the number of equations obtained is $(M-1)$.

The mass balance equation is generally nonlinear [29] with respect to the defect concentrations. However, a linear approximation can be applied considering that the defect concentrations are small. This approximation neglects all terms quadratic in the defects concentrations, i.e., terms representing products of different concentrations or their squares. The following linear equation can be derived:

$$
\begin{aligned}
x & =\frac{1}{4}\left(X_{V_{\beta}}-X_{V_{\alpha}}\right)+\frac{1}{2}\left(X_{A_{\beta}}-X_{B_{\alpha}}\right)-\frac{1}{2} \nu\left(X_{I_{B}}-X_{I_{A}}\right) \\
& +\frac{1}{4} \sum_{d} X_{d}\left[L_{V_{\beta}}^{d}-L_{V_{\alpha}}^{d}+2\left(L_{A_{\beta}}^{d}-L_{B_{\alpha}}^{d}\right)+\left(L_{I_{B}}^{d}-L_{I_{A}}^{d}\right)\right].
\end{aligned}
\tag{16}
$$

Here, the first line represents the deviation from the stoichiometry due to the elementary defects, $\nu$ being the number of interstitial positions per lattice site. We only consider tetrahedral interstitials, for which $\nu=8$. The second line is the contribution of the defect clusters $d$, where $L_{d_{i}}^{d}$ is the number of elementary defects $d_{i}$ in the cluster $d$. For example, for the vacancy cluster $V_{\alpha} V_{\beta}^{n}$ we have $L_{V_{\alpha}}^{V_{\alpha} V_{\beta}^{n}}=1, L_{V_{\beta}}^{V_{\alpha} V_{\beta}^{n}}=n$, and $L_{B_{\alpha}}^{V_{\alpha} V_{\beta}^{n}}=L_{A_{\beta}}^{V_{\alpha} V_{\beta}^{n}}=0$. The complete list of the $L-$numbers is provided in the Appendix, along with Eq.(16) specialized for the chosen set of defect clusters.

Note that the divacancy, the antisite pair, and the Frenkel pairs do not affect the material balance. Accordingly, the terms representing these pairs mutually cancel in Eq.(16). This is true for any composition-conserving defect cluster. The formation of such clusters is accompanied by addition or removal of $m$ formula units AB or does not require any addition

or removal ($m = 0$). It is easy to show that the concentration of composition-conserving clusters is

$$
X_{d}=\sigma_{d} \exp \left(-\frac{\varepsilon_{d}+2 m \varepsilon_{0}}{k_{B} T}\right). \tag{17}
$$

For example, $m = 1$ for divacancies and $m = 0$ for antisite pairs and Frenkel pairs. This concentration is independent of the off-stoichiometry and can be immediately calculated at any given temperature without solving any equations.

Eqs.(9)-(14) and (16) (less the equations for the composition-conserving clusters) constitute a complete set of equations that must be solved for the defect concentrations numerically.

Figures 3(a) and (b) present the computed composition dependencies of the defect concentrations in TaC and HfC, respectively. The temperature is fixed at 2500 K, but results for other temperatures are qualitatively similar. The Supplementary Information file shows the plots for 3500 K. The plots in Fig. 3 only include the stoichiometric and metal-rich compositions ($x \geq 0$) because carbon-rich compositions ($x < 0$) are unstable according to the phase diagram [34, 35]. In the plots, the chemical compositions are measured by the fraction of metallic atoms $c_A = 1 + x$ (A = Ta or Hf).

From Figs. 3(a) and (b), it is evident that thermal disorder in the stoichiometric carbides is dominated by Ta and C vacancies in TaC and by carbon vacancies and carbon interstitials in HfC. This difference reflects the different energetics of the point defects and, ultimately, the difference in the chemical bonding in the two carbides. The Hf vacancy concentration in stoichiometric HfC is extremely small relative to the carbon defects. As the off-stoichiometry increases, so does the carbon vacancy concentration, showing that the carbon vacancies are the constitutional defects on the metal-rich side in both carbides. As expected from the mass action law, the carbon vacancies suppress the metallic vacancies and carbon interstitials. In off-stoichiometric $\text{Ta}_{1+x}\text{C}_{1-x}$ with $x < 0.04$, the metallic sublattice is dominated by single vacancies $V_{\text{Ta}}$. At larger deviations from the stoichiometry ($x > 0.04$), the Ta vacancies start forming divacancies $V_{\text{Ta}}V_{\text{C}}$ and tri-vacancies $V_{\text{Ta}}V_{\text{C}}^2$, whose concentrations eventually become comparable to that of single vacancies. In off-stoichiometric $\text{Hf}_{1+x}\text{C}_{1-x}$, the dominant metallic defects likewise depend on the chemical composition. At small deviations from the stoichiometry ($x < 0.001$), the leading metallic defects are single vacancies $V_{\text{Hf}}$. As the off-stoichiometry increases, the concentrations of vacancy clusters $V_{\text{Hf}}V_{\text{C}}^n$ rapidly grow and at $x > 0.001$ they exceed the $V_{\text{Hf}}$ concentration. The six-vacancy clusters $V_{\text{Hf}}V_{\text{C}}^5$ have the highest concentration, although the clusters with smaller $n$ come close.

## 5 Effective defect formation energies

Figures 4 and 5 present the Arrhenius diagrams, $\log X_d$ versus $1/T$, of the defect concentrations in TaC and HfC, respectively. The chemical compositions are fixed at $x=0$ (stoichiometry) and $x=0.02$ (representative off-stoichiometric state). Recall that the composition-conserving defect clusters strictly follow the Arrhenius law, see Eq.(17). As a result, their plots are represented by perfect straight lines on the Arrhenius diagrams and perfect horizontal lines in the composition plots (Fig. 3). The single defects and non-conserving defect clusters do not follow the Arrhenius law exactly but their plots still look fairly straight. As a good approximation, all defect concentrations can be represented in the Arrhenius form

$$
X_d = X_d^0 \exp\left(-\frac{\overline{\varepsilon}_d}{k_B T}\right) \tag{18}
$$

with appropriate prefactors $X_d^0$ and effective formation energies $\overline{\varepsilon}_d$. Although not exact, Eq.(18) is useful for applications and comparison with experiments.

As discussed in Ref. [29], Eq.(18) works best in two limiting cases: when one defect concentration is much higher than all other concentrations and when the compound is stoichiometric with thermal disorder strongly dominated by two defect types. In the first case, the right-hand side of Eq.(16) can be represented by a single term, so the respective defect concentration is proportional to $x$. In the second case, the right-hand side of Eq.(16) is represented by two terms while the left-hand side is zero; thus the two defect concentrations are equal up to a numerical factor. In both cases, the material balance equation is simplified, and Eqs.(9)-(14) can be solved analytically with solutions in the form of Eq.(18).

The first case is realized in the off-stoichiometric carbides dominated by constitutional carbon vacancies. In our notation, $X_{V_\beta}$ is much greater than all other concentrations $X_d$. Accordingly, the balance equation (16) is simplified to $x = \frac{1}{4}X_{V_\beta}$, from which $X_{V_\beta}=4x$. Thus, $X_{V_\beta}$ is temperature-independent and proportional to the off-stoichiometry parameter $x$. Inserting this $X_{V_\beta}$ in Eq.(9), we obtain the metal vacancy concentration

$$
X_{V_\alpha} = \frac{1}{4x} \exp\left(-\frac{\varepsilon_{V_\alpha} + \varepsilon_{V_\beta} + 2\varepsilon_0}{k_B T}\right). \tag{19}
$$

Next, we find the concentrations of the vacancy clusters $V_\alpha V_\beta^n$ using Eq.(15):

$$
X_{V_\alpha V_\beta^n} = \sigma_{V_\alpha V_\beta^n} (4x)^{n-1} \exp\left(-\frac{\varepsilon_{V_\alpha V_\beta^n} - (n-1)\varepsilon_{V_\beta} + 2\varepsilon_0}{k_B T}\right). \tag{20}
$$

For the interstitial concentrations we use Eqs.(12) and (13) to obtain

$$
X_{I_A} = 4x \exp\left(-\frac{\varepsilon_{I_A} - \varepsilon_{V_\beta} - 2\varepsilon_0}{k_B T}\right). \tag{21}
$$

$$
X_{I_{B}}=\frac{1}{4 x} \exp \left(-\frac{\varepsilon_{I_{B}}+\varepsilon_{V_{\beta}}}{k_{B} T}\right).\tag{22}
$$

This chain of calculations can be continued to obtain all other defect concentrations. Note that they all have the Arrhenius form (18). The respective effective formation energies and prefactors are summarized in Table 5. Equations (19) and (22) confirm the trend mentioned above: deviations from stoichiometry with $x>0$ suppress the metallic vacancies and carbon interstitials. At the same time, such deviations promote the formation of the vacancy clusters $V_{\alpha} V_{\beta}^{n}$ and metallic interstitials $I_{A}$.

The second case is realized in stoichiometric carbides. The leading thermal defects in the two carbides are different. In TaC, such defects are the vacancies $V_{\alpha}$ and $V_{\beta}$. The balance equation (16) gives $V_{\alpha}=V_{\beta}$, which we combine with Eq.(9) to obtain

$$
X_{V_{\alpha}}=X_{V_{\beta}}=\exp \left(-\frac{\varepsilon_{V_{\alpha}}+\varepsilon_{V_{\beta}}+2 \varepsilon_{0}}{2 k_{B} T}\right).\tag{23}
$$

The interstitial concentrations are then obtained by inserting Eq.(23) into Eqs.(12) and (13):

$$
X_{I_{A}}=\exp \left(-\frac{2 \varepsilon_{I_{A}}-2 \varepsilon_{0}+\varepsilon_{V_{\alpha}}-\varepsilon_{V_{\beta}}}{2 k_{B} T}\right),\tag{24}
$$

$$
X_{I_{B}}=\exp \left(-\frac{2 \varepsilon_{I_{B}}-2 \varepsilon_{0}+\varepsilon_{V_{\beta}}-\varepsilon_{V_{\alpha}}}{2 k_{B} T}\right).\tag{25}
$$

The concentrations of the vacancy clusters $V_{\alpha} V_{\beta}^{n}$ are readily calculated by inserting the single vacancy concentrations from Eq.(23) into Eq.(15), which gives

$$
X_{V_{\alpha} V_{\beta}^{n}}=\sigma_{V_{\alpha} V_{\beta}^{n}} \exp \left(-\frac{2 \varepsilon_{V_{\alpha} V_{\beta}^{n}}+(n-1)\left(\varepsilon_{V_{\alpha}}-\varepsilon_{V_{\beta}}\right)+2(n+1) \varepsilon_{0}}{2 k_{B} T}\right).\tag{26}
$$

The remaining defect concentrations are calculated similarly, and the Arrhenius parameters obtained are summarized in Table 6.

In stoichiometric HfC, the leading thermal defects are carbon vacancies $V_{\beta}$ and carbon interstitials $I_{B}$. The balance equation (16) gives $X_{V_{\beta}}=2 \nu X_{I_{B}}$ (recall that $\nu=8$ in the B1 structure). Using Eq.(13) we have

$$
X_{V_{\beta}}=\sqrt{2 \nu} \exp \left(-\frac{\varepsilon_{I_{B}}+\varepsilon_{V_{\beta}}}{2 k_{B} T}\right).\tag{27}
$$

$$
X_{I_{B}}=\frac{1}{\sqrt{2 \nu}} \exp \left(-\frac{\varepsilon_{I_{B}}+\varepsilon_{V_{\beta}}}{2 k_{B} T}\right).\tag{28}
$$

Next, the metal vacancy concentration is obtained from Eq.(9):

$$
X_{V_{\alpha}}=\frac{1}{\sqrt{2 \nu}} \exp \left(-\frac{2 \varepsilon_{V_{\alpha}}+\varepsilon_{V_{\beta}}-\varepsilon_{I_{B}}+4 \varepsilon_{0}}{2 k_{B} T}\right),\tag{29}
$$

while Eq.(12) gives

$$
X_{I_{A}}=\sqrt{2 \nu} \exp \left(-\frac{2 \varepsilon_{I_{A}}-\varepsilon_{V_{\beta}}+\varepsilon_{I_{B}}-4 \varepsilon_{0}}{2 k_{B} T}\right). \tag{30}
$$

The vacancy cluster concentrations are obtained from Eq.(15), which gives

$$
X_{V_{\alpha} V_{\beta}^{n}}=\sigma_{V_{\alpha} V_{\beta}^{n}}(2 \nu)^{(n-1) / 2} \exp \left(-\frac{2 \varepsilon_{V_{\alpha} V_{\beta}^{n}}+(n-1)\left(\varepsilon_{I_{B}}-\varepsilon_{V_{\beta}}\right)+4 \varepsilon_{0}}{2 k_{B} T}\right). \tag{31}
$$

Continuing the calculations, we derive the Arrhenius parameters of all other defects summarized in Table 6.

Table 7 reports the numerical values of the Arrhenius parameters of the point defects in TaC and HfC obtained from the first-principles raw energies. Inserting these values in Eq.(18), the Arrhenius lines obtained closely approximate the numerical solutions shown in Figs. 4 and 5.

## 6 Discussion

The goal of this work was to understand and predict the point defects in the binary carbides TaC and HfC by DFT calculations. To this end, a statistical-mechanical model has been developed capable of predicting point-defect concentrations in binary compounds with the AB stoichiometry. The model applies to both single defects and defect clusters of any complexity. Although our primary interest is in the particular carbides TaC and HfC, the the model is general enough to be applied to other binary carbides, nitrides, and borides with the AB stoichiometry. It can also be generalized to ordered compounds with different crystal structures and stoichiometries [29].

The model generalizes the previous treatment of point defects in intermetallic compounds [29]. Thermal and compositional disorder in intermetallic compounds is also governed by point defects and has been studied by similar DFT statistical mechanics methods [27-30]. However, intermetallics do not usually support interstitial defects, and vacancies display a weak clustering trend. Thus, the point-defect system is much simpler than in the carbides.

In the present model, the free energy of the point defects includes the configurational and orientational effects but neglects other contributions, such as atomic vibrations. This is not a severe limitation. As discussed previously [29], the effect of vibrations can be included by replacing the "raw" defect energy $\varepsilon_{d}$ by the "raw" free energy $f_{d}=\varepsilon_{d}-T s_{d}$, where $s_{d}$ is the change in the vibrational entropy due to the defect formation in a perfect crystal. DFT-based calculations of $s_{d}$ are challenging, especially for defect clusters, but calculations with

interatomic potentials (traditional or machine-learning type [36]) are straightforward. The effect of applied pressure on the point-defect concentrations can also be included, provided the defect formation volumes can be computed.

As mentioned in Section 1, our primary motivation for calculating the point-defect concentrations is that they constitute a required ingredient for diffusion calculations. We will briefly discuss the possible diffusion mechanisms suggested by the present results, focusing on the most realistic case of carbon-deficient chemical compositions $\mathrm{Ta}_{1+x} \mathrm{C}_{1-x}$ ($x > 0$). As evident from the calculations, deviations from the stoichiometry towards carbon-deficient compositions are accommodated by carbon vacancies. The carbon vacancy concentration is virtually temperature-independent and can reach a few percent (recall that $X_{V_{\beta}} \approx 4x$), dominating over all other point defects. The fraction of carbon vacancies bound into clusters is orders of magnitude smaller. Thus, it is highly probable that carbon diffusion is mediated by single vacancy jumps on the carbon sublattice. Interactions among the carbon vacancies can hardly affect their diffusion given their repulsion as first and second neighbors (Fig. 2). To a good approximation, carbon diffusion can be treated as occurring by the simple vacancy mechanism on the FCC sublattice with the geometric correlation factor. The same reasoning applies to carbon diffusion in $\mathrm{Hf}_{1+x} \mathrm{C}_{1-x}$ ($x > 0$).

Diffusion of the metallic atoms is more complex. In TaC, single Ta vacancies have a slightly higher concentration than the divacancies $V_{\mathrm{Ta}} V_{\mathrm{C}}$ and trivacancies $V_{\mathrm{Ta}} V_{\mathrm{C}}^{2}$. However, the literature data [7, 14] indicate that Ta vacancies have a lower jump barrier when bound with carbon vacancies. Thus, divacancies and possibly $V_{\mathrm{Ta}} V_{\mathrm{C}}^{2}(\mathrm{T})$ clusters (triangular configuration) should also be considered. The linear clusters $V_{\mathrm{Ta}} V_{\mathrm{C}}^{2}(\mathrm{L})$ have a lower concentration and are in a locked configuration: the Ta vacancy cannot make a jump without breaking away from this cluster. One complication is that atomic diffusion mediated by divacancies and trivacancies is accompanied by jump correlation effects, which can be significant. Approximate semi-analytical methods exist for calculating the jump correlation factors in the B1 structure under the divacancy mechanism [37, 38]. However, more accurate calculations utilize kinetic Monte Carlo (KMC) simulations [38]. For trivacancies, KMC is the most viable option.

In HfC, Hf diffusion is mediated by the $V_{\mathrm{Hf}} V_{\mathrm{C}}^{n}$ clusters. The size of the dominant cluster depends on temperature and chemical composition. Fig. 5 shows that at the off-stoichiometry of $x = 0.02$, the clusters having the highest concentration are $V_{\mathrm{Hf}} V_{\mathrm{C}}^{3}(\mathrm{IP})$ above $\sim 2500$ K and $V_{\mathrm{Hf}} V_{\mathrm{C}}^{5}$ below $\sim 2500$ K. The transition temperature depends on the off-stoichiometry. Note, however, that in both cases, the Hf vacancy cannot make a jump without destroying the cluster. In $V_{\mathrm{Hf}} V_{\mathrm{C}}^{3}(\mathrm{IP})$, such a jump causes one of the dissociation reactions $V_{\mathrm{Hf}} V_{\mathrm{C}}^{3}(\mathrm{IP}) \rightarrow V_{\mathrm{Hf}} V_{\mathrm{C}}^{2}(\mathrm{T})+V_{\mathrm{C}}$ or $V_{\mathrm{Hf}} V_{\mathrm{C}}^{3}(\mathrm{IP}) \rightarrow V_{\mathrm{Hf}} V_{\mathrm{C}}+2 V_{\mathrm{C}}$. The

isolated carbon vacancies produced by these reactions repel each other and are unlikely to recombine into the original cluster. In $V_{\text{Hf}}V_{\text{C}}^{5}$, a Hf vacancy jump causes one of the dissociations $V_{\text{Hf}}V_{\text{C}}^{5} \rightarrow V_{\text{Hf}}+5V_{\text{C}}$, $V_{\text{Hf}}V_{\text{C}}^{5} \rightarrow V_{\text{Hf}}V_{\text{C}}+4V_{\text{C}}$, or $V_{\text{Hf}}V_{\text{C}}^{5} \rightarrow V_{\text{Hf}}V_{\text{C}}^{2}(\text{T})+3V_{\text{C}}$, which again produces isolated carbon vacancies repelling each other. This behavior reflects the general trend that vacancy cluster migration by single jumps is subject to severe geometric constraints and strong correlation effects.

Three alternatives can be considered. One is to allow the vacancy clusters to evolve by a chain of dissociation-recombination reactions among all possible clusters [7]. One should then resort to KMC simulations as analytical treatment of the atomic transport caused by such chains of reactions could be impractical. A second approach is to consider collective (simultaneous) jumps of a group of atoms filling the vacant sites and shifting the entire vacancy cluster to a new position. Such mechanisms were discussed in Ref. [32] for the TiC and ZrC carbides and seem plausible. For simple clusters such as divacancies, calculating the minimum-energy path is straightforward, but multi-vacancy clusters present a challenge. One can test a set of *a priori* chosen atomic trajectories and select one with the lowest barrier [32]. A more general treatment should use a saddle-point search algorithm not relying on *a priori* assumptions about which atom will land in which position. Yet another approach is to use molecular dynamics to discover the migration mechanisms. This approach is appealing but will likely require a surrogate model such as a machine-learning potential. It should also be noted that comparison of different vacancy clusters cannot be made solely from their equilibrium concentration and migration barrier. The attempt frequency also matters. The latter depends on the total mass $m$ of the collectively jumping atoms (approximately as $1/\sqrt{m}$) and cluster-specific vibrational modes.

## 7 Conclusions

We have combined DFT calculations with a statistical-mechanical model to predict point-defect concentrations $X_d$ in the TaC and HfC carbides as a function of temperature and chemical composition. For each defect type $d$, the function $X_d(c_A, T)$ can be conveniently and accurately represented by two parameters: an Arrhenius prefactor $X_d^0$ and effective formation energy $\overline{\varepsilon}_d$. Our results complement the previous work [7, 15, 16, 32, 39] and can be summarized as follows:

- Atomic mechanisms of thermal and constitutional disorder in TaC and HfC are complex and involve multiple types of point defects occurring simultaneously.

- The strong short-range binding among the elementary point defects, especially in


HfC, leads to persistent point-defect clusters. The dominant type of defect cluster depends on the chemical composition and temperature and is different between TaC and HfC.

- The presence of relatively large concentrations of defect clusters is one of the hall- marks of these carbides distinguishing them from other ordered phases such as inter- metallic compounds.

- The diversity of the point defects suggests that the mechanisms of metal atom dif- fusion are complex and may involve chains of point-defect reactions and collective atomic rearrangements. Their computational studies require new methods.

The mode developed here is general enough to be applied to other binary B1-ordered compounds and can be further generalized to compounds with other crystal structures and different stoichiometries.

### Acknowledgments
This research was supported by the Office of Naval Research under Award No. N00014-22-1-2645.

## Appendix: The $L$-numbers and the material balance equation

The table below presents the complete list of the $L$-numbers for all defect clusters considered in this work. These numbers appear in Eq.(16) for the material balance.

Table 1: $L$-numbers for the defect clusters considered in this work.

<table>
  <thead>
    <tr>
      <th>Cluster</th>
      <th colspan="6">Elementary defect</th>
    </tr>
    <tr>
      <th></th>
      <th>$V_\alpha$</th>
      <th>$V_\beta$</th>
      <th>$A_\beta$</th>
      <th>$B_\alpha$</th>
      <th>$I_A$</th>
      <th>$I_B$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$V_\alpha V_\beta$</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$A_\beta B_\alpha$</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$V_\alpha B_\alpha$</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$V_\beta A_\beta$</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$V_\beta B_\alpha$</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$V_\beta I_B$</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^2$ (T)</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^2$ (L)</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^3$ (IP)</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^3$ (OP)</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^4$ (IP)</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^4$ (OP)</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^5$</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^6$</td>
      <td>1</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

For the set of defect clusters considered in this work, the material balance equation is

$$
\begin{aligned}
x & = \frac{1}{4} \left( X_{V_\beta} - X_{V_\alpha} \right) + \frac{1}{2} \left( X_{A_\beta} - X_{B_\alpha} \right) - \frac{1}{2} \nu \left( X_{I_B} - X_{I_A} \right) \\
& + \frac{1}{4} \left( 3X_{V_\beta A_\beta} - 3X_{V_\alpha B_\alpha} - X_{V_\beta B_\alpha} \right) \\
& + \frac{1}{4} \left( X_{V_\alpha V_\beta^2(T)} + X_{V_\alpha V_\beta^2(L)} + 2X_{V_\alpha V_\beta^3(IP)} + 2X_{V_\alpha V_\beta^3(OP)} \right) \\
& + \frac{1}{4} \left( 3X_{V_\alpha V_\beta^4(IP)} + 3X_{V_\alpha V_\beta^4(OP)} + 4X_{V_\alpha V_\beta^5} + 5X_{V_\alpha V_\beta^6} \right) .
\end{aligned} \tag{32}
$$

This equation contains 17 defect concentrations. Their calculation requires solving this equation simultaneously with 16 equations representing the reactions among the elementary defects and the formation of non-conserving defect clusters.

## References

[1] O. Cedillos-Barraza, D. Manara, K. Boboridis, T. Watkins, S. Grasso, D. D. Jayaseelan, R. J. M. Konings, M. J. Reece, W. E. Lee, Investigating the highest melting

temperature materials: A laser melting study of the TaC-HfC system, Scientific Re- ports 6 (2016) 37962.

[2] F. Viñes, C. Sousa, P. Liu, J. A. Rodriguez, F. Illas, A systematic density functional theory study of the electronic structure of bulk and (001) surface of transition-metals carbides, The Journal of Chemical Physics 122 (2005) 174709.

[3] R. Resnick, R. Steinitz, L. Seigle, Diffusion of carbon in tantalum monocarbide, Trans. Metall. Soc. AIME 236 (1966) 1732-1738.

[4] W. F. Brizes, Diffusion of carbon in the carbides of tantalum, Journal of Nuclear Materials 26 (1968) 227-231.

[5] D. Rafaja, W. Lengauer, H. Wiesenberger, Non-metal diffusion coefficients for the Ta-C and Ta-N systems, Acta Materialia 46 (1998) 3477-3483.

[6] T. C. Wallace, D. P. Butt, Review of diffusion and vaporization of Group 4 and 5 transition metal carbides, Springer Netherlands, Dordrecht, 1996, pp. 53-90. URL: https://doi.org/10.1007/978-94-009-1565-7.

[7] X. Tang, R. Salehin, G. B. Thompson, C. R. Weinberger, Statistical study of vacancy diffusion in TiC and TaC, Physical Review Materials 4 (2020) 093602.

[8] M. Jubair, A. M. M. T. Karim, M. Nuruzzaman, M. A. K. Zilani, Comparison of structural, mechanical and optical properties of tantalum hemicarbide with tantalum monocarbide: Ab initio calculations, Journal of Physics Communications 3 (2019) 055017.

[9] W. Sun, X. Kuang, H. Liang, X. Xia, Z. Zhang, C. Lu, A. Hermann, Mechanical properties of tantalum carbide from high-pressure/high-temperature synthesis and first-principles calculations, Physical Chemistry Chemical Physics 22 (2020) 5018-5023.

[10] N. De Leon, X. Yu, H. Yu, C. Weinberger, G. Thompson, Bonding effects on the slip differences in the B1 monocarbides, Physical Review Letters 114 (2015) 165502.

[11] X. Yu, C. R. Weinberger, G. B. Thompson, Ab initio investigations of the phase stability in tantalum carbides, Acta Materialia 80 (2014) 341-349.

[12] W.-L. Yan, M. Sygnatowicz, G.-H. Lu, F. Liu, D. K. Shetty, First-principles study on surface stability of tantalum carbides, Surface Science 644 (2016) 24-28.

[13] J. M. Rimsza, S. Foiles, J. Michael, W. Mackie, K. Larson, Role of defects on the surface properties of HfC, Applied Surface Science 495 (2019) 143500.

[14] X.-X. Yu, G. B. Thompson, C. R. Weinberger, Influence of carbon vacancy forma- tion on the elastic constants and hardening mechanisms in transition metal carbides, Journal of the European Ceramic Society 35 (2015) 95-103.

[15] R. Salehin, X. Tang, G. B. Thompson, C. R. Weinberger, Vacancy-cluster and off- lattice metal-atom diffusion mechanisms in transition metal carbides, Computational Materials Science 199 (2021) 110713.

[16] V. I. Razumovskiy, M. N. Popov, H. Ding, J. Odqvist, Formation and interaction of point defects in group IVB transition metal carbides and nitrides, Computational Materials Science 104 (2015) 147-154.

[17] G. Kresse, J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mat. Sci. 6 (1996) 15.

[18] G. Kresse, J. Furthmueller, Efficient iterative schemes for ab initio total-energy cal- culations using a plane-wave basis set, Phys. Rev. B 54 (1996) 11169-11186.

[19] P. E. Blochl, Projector augmented-wave method, Phys. Rev. B 50 (1994) 17953-17979.

[20] J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, C. Fiolhais, Atoms, molecules, solids, and surfaces: Applications of the generalized gradient approximation for exchange and correlation, Phys. Rev. B 46 (1992) 6671-6687.

[21] J. P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865-3868.

[22] H. L. Brown, P. E. Armstrong, C. P. Kempter, Elastic properties of some polycrys- talline transition-metal monocarbides, The Journal of Chemical Physics 45 (1966) 547-549.

[23] W. Weber, Lattice dynamics of transition-metal carbides, Physical Review B 8 (1973) 5082.

[24] C. Zhang, A. Gupta, S. Seal, B. Boesl, A. Agarwal, Solid solution synthesis of tantalum carbide-hafnium carbide by spark plasma sintering, Journal of the American Ceramic Society 100 (2017) 1853-1862.

[25] L. He, Z. Lin, J. Wang, Y. Bao, Y. Zhou, Crystal structure and theoretical elastic properrty of two new ternary ceramics ${\rm Hf_3Al_4C_6}$ and ${\rm Hf_2Al_4C_5}$, Scripta Materialia 58 (2008) 679-682.

[26] Y. Guo, J. Chen, W. Song, S. Shan, X. Ke, Z. Jiao, Electronic, mechanical and ther- modynamic properties of ZrC, HfC and their solid solutions studied by first-principles calculation, Solid State Communications 338 (2021) 114481.

[27] Y. Mishin, D. Farkas, Atomistic simulation of point defects and diffusion in B2 NiAl .1. Point defect energetics, Philosophical Magazine A 75 (1997) 169-185.

[28] Y. Mishin, D. Farkas, Atomistic simulation of point defects and diffusion in B2 NiAl .2. Diffusion mechanisms, Philosophical Magazine A 75 (1997) 187-199.

[29] Y. Mishin, C. Herzig, Diffusion in the Ti-Al system, Acta Mater. 48 (2000) 589-623.

[30] A. Y. Lozovoi, Y. Mishin, Point defects in NiAl: The effec of lattice vibrations, Phys. Rev. B 68 (2003) 184113.

[31] Y. Mishin, M. R. Sørensen, A. F. Voter, Calculation of point defect entropy in metals, Philos. Mag. A 81 (2001) 2591-2612.

[32] V. I. Razumovskiy, A. V. Ruban, J. Odqvist, P. A. Korzhavyi, Vacancy-cluster mech- anism of metal-atom diffusion in substoichiometric carbides, Physical Review B 87 (2013) 054203.

[33] C. Woodward, M. Asta, G. Kresse, J. Hafner, Density of constitutional and thermal point defects in $L1_2$ $Al_3$sc, Physical Review B 63 (2001) 094103.

[34] B. Mehdikhan, G. H. Borhani, S. R. Bakhshi, H. R. Baharvandi, Effect of milling and sintering temperature of ${\rm TaC-TaB_2}$ composite on lattice parameter and C/Ta ratio, Refractories and Industrial Ceramics 57 (2017) 507-512.

[35] I. L. Shabalin, Hafnium monocarbide, in: I. L. Shabalin (Ed.), Ultra-High Temperature Materials II: Refractory Carbides I. (Ta, Hf, Nb and Zr Carbides), Springer Netherlands, Dordrecht, 2019, pp. 145-248. URL: https://doi.org/10.1007/978-94-024-1302-1.

[36] Y. Mishin, Machine-learning interatomic potentials for materials science, Acta Mater. 214 (2021) 116980.

[37] R. E. Howard, Random-walk method for calculating correlation factors: Tracer diffu- sion by divacancy and impurity-vacancy pairs in cubic crystals, Phys. Rev. 144 (1966) 650–661.

[38] I. V. Belova, D. Shaw, G. E. Murch, Limits of the ratios of tracer diffusivities for diffusion by vacancy pairs: Application to compound semiconductors, Journal of Applied Physics 106 (2009) 113707.

[39] C. J. Smith, M. A. Ross, N. De Leon, C. R. Weinberger, G. B. Thompson, Ultra-high temperature deformation in TaC and HfC, Journal of the European Ceramic Society 38 (2018) 5319–5332.

[40] R. He, L. Fang, T. Han, G. Yang, G. Ma, J. Liu, X. Chen, L. Xie, L. Liu, Q. Li, et al., Elasticity, mechanical and thermal properties of polycrystalline hafnium carbide and tantalum carbide at high pressure, Journal of the European Ceramic Society 42 (2022) 5220–5228.

[41] C. J. Smith, X.-X. Yu, Q. Guo, C. R. Weinberger, G. B. Thompson, Phase, hardness, and deformation slip behavior in mixed ${\text{Hf}}_{x}{\text{Ta}}_{1-x}\text{C}$, Acta Materialia 145 (2018) 142–153.

[42] M. Singh, H. Wiedemeier, Estimation of thermal expansion behaviour of some refrac- tory carbides and nitrides, Journal of materials science 32 (1997) 5749–5751.

Table 2: Lattice parameter $a$, cohesive energy $\varepsilon_0$, elastic constants $c_{ij}$, and bulk modulus $B$ obtained by the present DFT calculations. The experimental and calculated values from the literature are shown in the round and square brackets, respectively.

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>TaC</th>
      <th>HfC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$a$ (Å)</td>
      <td>$4.478$ $[4.471]^{a}$, $(4.450)^{b}$</td>
      <td>$4.646$ $[4.642]^{a}$, $[4.647]^{f}$, $(4.631)^{g}$</td>
    </tr>
    <tr>
      <td>$\varepsilon_0$ (eV)</td>
      <td>$-11.10$</td>
      <td>$-10.53$</td>
    </tr>
    <tr>
      <td>$c_{11}$ (GPa)</td>
      <td>$759.8$ $[737]^{a,c}$, $[674]^{d}$</td>
      <td>$509.9$ $[577]^{h}$, $[540]^{a,d}$, $(500)^{i}$</td>
    </tr>
    <tr>
      <td>$c_{12}$ (GPa)</td>
      <td>$118.0$ $[141]^{a,c}$, $[172]^{d}$</td>
      <td>$111.5$ $[117]^{h}$, $[112]^{a,d}$</td>
    </tr>
    <tr>
      <td>$c_{44}$ (GPa)</td>
      <td>$170.8$ $[175]^{a,c}$, $[167]^{d}$</td>
      <td>$159.2$ $[171]^{h}$, $[171]^{a,d}$</td>
    </tr>
    <tr>
      <td>$B$ (GPa)</td>
      <td>$331.9$, $(332)^{e}$, $(355.9)^{b}$, $[340]^{a,c}$, $[339]^{d}$</td>
      <td>$244.3$, $(242)^{j}$, $(272)^{b}$, $[253]^{a,d}$</td>
    </tr>
  </tbody>
</table>

$^{a}$Ref. [14], $^{b}$Ref. [40], $^{c}$Ref. [11] , $^{d}$Ref. [41], $^{e}$Ref. [24], $^{f}$Ref. [26]
$^{g}$Ref. [42], $^{h}$Ref. [25], $^{i}$Ref. [23], $^{j}$Ref. [22]

Table 3: "Raw" energies (in eV) of point defects in TaC and HfC obtained by DFT calcu-
lations. The defect pairs are considered to have the shortest defect separation. L, T, IP,
and OP are vacancy cluster configurations explained in the main text. *Unstable config-
uration.

<table>
 <thead>
  <tr>
   <th>Defect type</th>
   <th>Symbol</th>
   <th>TaC</th>
   <th>HfC</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>Metal vacancy</td>
   <td>$V_{\alpha}$</td>
   <td>$15.30$</td>
   <td>$19.30$</td>
  </tr>
  <tr>
   <td>Carbon vacancy</td>
   <td>$V_{\beta}$</td>
   <td>$9.45$</td>
   <td>$10.20$</td>
  </tr>
  <tr>
   <td>Antisite on carbon sublattice</td>
   <td>$A_{\beta}$</td>
   <td>$7.59$</td>
   <td>$9.13$</td>
  </tr>
  <tr>
   <td>Antisite on metal sublattice</td>
   <td>$B_{\alpha}$</td>
   <td>$11.78$</td>
   <td>$13.80$</td>
  </tr>
  <tr>
   <td>Metal interstitial</td>
   <td>$I_{A}$</td>
   <td>$- 0.27$</td>
   <td>$- 0.31$</td>
  </tr>
  <tr>
   <td>Carbon interstitial</td>
   <td>$I_{B}$</td>
   <td>$- 2.71$</td>
   <td>$- 3.99$</td>
  </tr>
  <tr>
   <td>Divacancy</td>
   <td>$V_{\alpha}V_{\beta}$</td>
   <td>$24.61$</td>
   <td>$27.90$</td>
  </tr>
  <tr>
   <td>Antisite pair</td>
   <td>$A_{\beta}B_{\alpha}$</td>
   <td>$5.45$</td>
   <td>$5.00$</td>
  </tr>
  <tr>
   <td>Antisite-vacancy pair on metal sublattice</td>
   <td>$V_{\alpha}B_{\alpha}$</td>
   <td>$22.63$</td>
   <td>$25.86$</td>
  </tr>
  <tr>
   <td>Antisite-vacancy pair on carbon sublattice</td>
   <td>$V_{\beta}A_{\beta}$</td>
   <td>$15.62$</td>
   <td>$18.27$</td>
  </tr>
  <tr>
   <td>Antisite-vacancy pair on different sublattices</td>
   <td>$V_{\beta}B_{\alpha}$</td>
   <td>*</td>
   <td>$20.46$</td>
  </tr>
  <tr>
   <td>Nearest-neighbor Frenkel defect</td>
   <td>$V_{\beta}I_{B}$</td>
   <td>*</td>
   <td>$4.30$</td>
  </tr>
  <tr>
   <td>Vacancy cluster (T)</td>
   <td>$V_{\alpha}V_{\beta}^{2}$</td>
   <td>$34.08$</td>
   <td>$36.80$</td>
  </tr>
  <tr>
   <td>Vacancy cluster (L)</td>
   <td>$V_{\alpha}V_{\beta}^{2}$</td>
   <td>$33.94$</td>
   <td>$37.03$</td>
  </tr>
  <tr>
   <td>Vacancy cluster (IP)</td>
   <td>$V_{\alpha}V_{\beta}^{3}$</td>
   <td>$43.60$</td>
   <td>$46.01$</td>
  </tr>
  <tr>
   <td>Vacancy cluster (OP)</td>
   <td>$V_{\alpha}V_{\beta}^{3}$</td>
   <td>$43.62$</td>
   <td>$46.17$</td>
  </tr>
  <tr>
   <td>Vacancy cluster (IP)</td>
   <td>$V_{\alpha}V_{\beta}^{4}$</td>
   <td>$53.16$</td>
   <td>$55.39$</td>
  </tr>
  <tr>
   <td>Vacancy cluster (OP)</td>
   <td>$V_{\alpha}V_{\beta}^{4}$</td>
   <td>$53.13$</td>
   <td>$55.75$</td>
  </tr>
  <tr>
   <td>Vacancy cluster</td>
   <td>$V_{\alpha}V_{\beta}^{5}$</td>
   <td>$62.6$</td>
   <td>$65.19$</td>
  </tr>
  <tr>
   <td>Vacancy cluster</td>
   <td>$V_{\alpha}V_{\beta}^{6}$</td>
   <td>$72.13$</td>
   <td>$75.01$</td>
  </tr>
 </tbody>
</table>

Table 4: Binding energies and symmetry factors $\sigma$ of defect clusters in TaC and HfC obtained by DFT calculations. L, T, IP, and OP are vacancy cluster configurations explained in the main text. *Unstable configuration. The values in square brackets refer to previous calculations.

<table>
 <thead>
  <tr>
   <th>Cluster type</th>
   <th colspan="2">TaC</th>
   <th colspan="2">HfC</th>
  </tr>
  <tr>
   <th></th>
   <th>$\sigma$</th>
   <th>Energy (eV)</th>
   <th>$\sigma$</th>
   <th>Energy (eV)</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>$V_{\alpha}V_{\beta}$</td>
   <td>6</td>
   <td>$-0.14$ [$-$0.16]$^{a}$</td>
   <td>6</td>
   <td>$-1.60$ [$-$1.54]$^{a}$, [$-$1.49]$^{b}$,</td>
  </tr>
  <tr>
   <td>$A_{\beta}B_{\alpha}$</td>
   <td>6</td>
   <td>$-13.92$</td>
   <td>6</td>
   <td>$-17.93$</td>
  </tr>
  <tr>
   <td>$V_{\alpha}B_{\alpha}$</td>
   <td>6</td>
   <td>$-4.45$</td>
   <td>6</td>
   <td>$-7.24$</td>
  </tr>
  <tr>
   <td>$V_{\beta}A_{\beta}$</td>
   <td>6</td>
   <td>$-1.42$</td>
   <td>12</td>
   <td>$-1.06$</td>
  </tr>
  <tr>
   <td>$V_{\beta}B_{\alpha}$</td>
   <td></td>
   <td>*</td>
   <td>6</td>
   <td>$-3.54$</td>
  </tr>
  <tr>
   <td>$V_{\beta}I_{B}$</td>
   <td></td>
   <td>*</td>
   <td>8</td>
   <td>$-1.91$</td>
  </tr>
  <tr>
   <td>$V_{\alpha}V_{\beta}^{2}$ ($T$)</td>
   <td>12</td>
   <td>$-0.12$</td>
   <td>12</td>
   <td>$-2.90$</td>
  </tr>
  <tr>
   <td>$V_{\alpha}V_{\beta}^{2}$ (L)</td>
   <td>3</td>
   <td>$-0.26$</td>
   <td>3</td>
   <td>$-2.67$</td>
  </tr>
  <tr>
   <td>$V_{\alpha}V_{\beta}^{3}$ (IP)</td>
   <td>12</td>
   <td>$-0.05$</td>
   <td>12</td>
   <td>$-3.89$</td>
  </tr>
  <tr>
   <td>$V_{\alpha}V_{\beta}^{3}$ (OP)</td>
   <td>8</td>
   <td>$-0.03$</td>
   <td>8</td>
   <td>$-3.73$</td>
  </tr>
  <tr>
   <td>$V_{\alpha}V_{\beta}^{4}$ (IP)</td>
   <td>3</td>
   <td>$0.06$</td>
   <td>3</td>
   <td>$-4.71$</td>
  </tr>
  <tr>
   <td>$V_{\alpha}V_{\beta}^{4}$ (OP)</td>
   <td>12</td>
   <td>$0.03$</td>
   <td>12</td>
   <td>$-4.35$</td>
  </tr>
  <tr>
   <td>$V_{\alpha}V_{\beta}^{5}$</td>
   <td>6</td>
   <td>$0.05$</td>
   <td>6</td>
   <td>$-5.11$</td>
  </tr>
  <tr>
   <td>$V_{\alpha}V_{\beta}^{6}$</td>
   <td>1</td>
   <td>$0.13$</td>
   <td>1</td>
   <td>$-5.49$ [$-$5.52]$^{b}$</td>
  </tr>
 </tbody>
</table>

$^{a}$Ref. [15], $^{b}$Ref. [16]

Table 5: Equations for the Arrhenius parameters (prefactors $X_d$ and effective formation energies $\overline{\varepsilon}_d$) of point defects in metal-rich carbides ($x > 0$) with constitutional defects $V_\beta$.

<table>
  <thead>
    <tr>
      <th>Defect</th>
      <th>$X_d^0$</th>
      <th>$\overline{\varepsilon}_d$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$V_\alpha$</td>
      <td>$\dfrac{1}{4x}$</td>
      <td>$\varepsilon_{V_\alpha} + \varepsilon_{V_\beta} + 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$V_\beta$</td>
      <td>$4x$</td>
      <td>$0$</td>
    </tr>
    <tr>
      <td>$A_\beta$</td>
      <td>$(4x)^2$</td>
      <td>$\varepsilon_{A_\beta} - 2\varepsilon_{V_\beta} - 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$B_\alpha$</td>
      <td>$\dfrac{1}{(4x)^2}$</td>
      <td>$\varepsilon_{B_\alpha} + 2\varepsilon_{V_\beta} + 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$I_A$</td>
      <td>$4x$</td>
      <td>$\varepsilon_{I_A} - \varepsilon_{V_\beta} - 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$I_B$</td>
      <td>$\dfrac{1}{4x}$</td>
      <td>$\varepsilon_{I_B} + \varepsilon_{V_\beta}$</td>
    </tr>
    <tr>
      <td>$A_\beta B_\alpha$</td>
      <td>$\sigma_{A_\beta B_\alpha}$</td>
      <td>$\varepsilon_{A_\beta B_\alpha}$</td>
    </tr>
    <tr>
      <td>$V_\alpha B_\alpha$</td>
      <td>$\dfrac{\sigma_{V_\alpha B_\alpha}}{(4x)^3}$</td>
      <td>$\varepsilon_{V_\alpha B_\alpha} + 3\varepsilon_{V_\beta} + 4\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$V_\beta A_\beta$</td>
      <td>$\sigma_{V_\beta B_\beta}(4x)^3$</td>
      <td>$\varepsilon_{V_\beta B_\beta} - 3\varepsilon_{V_\beta} - 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$V_\beta B_\alpha$</td>
      <td>$\dfrac{\sigma_{V_\beta B_\alpha}}{4x}$</td>
      <td>$\varepsilon_{V_\beta B_\alpha} + \varepsilon_{V_\beta} + 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$V_\beta I_B$</td>
      <td>$\sigma_{V_\beta I_B}$</td>
      <td>$\varepsilon_{V_\beta I_B}$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta$</td>
      <td>$\sigma_{V_\alpha V_\beta}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta} + 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^2$</td>
      <td>$\sigma_{V_\alpha V_\beta^2}(4x)$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^2} - \varepsilon_{V_\beta} + 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^3$</td>
      <td>$\sigma_{V_\alpha V_\beta^3}(4x)^2$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^3} - 2\varepsilon_{V_\beta} + 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^4$</td>
      <td>$\sigma_{V_\alpha V_\beta^4}(4x)^3$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^4} - 3\varepsilon_{V_\beta} + 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^5$</td>
      <td>$\sigma_{V_\alpha V_\beta^5}(4x)^4$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^5} - 4\varepsilon_{V_\beta} + 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^6$</td>
      <td>$\sigma_{V_\alpha V_\beta^6}(4x)^5$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^6} - 5\varepsilon_{V_\beta} + 2\varepsilon_0$</td>
    </tr>
  </tbody>
</table>

Table 6: Equations for the Arrhenius parameters (prefactors $X_d$ and effective formation energies $\overline{\varepsilon}_d$) of point defects in stoichiometric carbides ($x=0$). Two mechanisms of thermal disorder are considered with the leading defects $V_\alpha$ & $V_\beta$ and $V_\beta$ & $I_B$.

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">Leading defects $V_\alpha$ & $V_\beta$</th>
      <th colspan="2">Leading defects $V_\beta$ & $I_B$</th>
    </tr>
    <tr>
      <th>Defect</th>
      <th>$X_d^0$</th>
      <th>$\overline{\varepsilon}_d$</th>
      <th>$X_d^0$</th>
      <th>$\overline{\varepsilon}_d$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$V_\alpha$</td>
      <td>$1$</td>
      <td>$\dfrac{\varepsilon_{V_\alpha} + \varepsilon_{V_\beta} + 2\varepsilon_0}{2}$</td>
      <td>$\dfrac{1}{\sqrt{2\nu}}$</td>
      <td>$\varepsilon_{V_\alpha} + 2\varepsilon_0 + \dfrac{\varepsilon_{V_\beta} - \varepsilon_{I_B}}{2}$</td>
    </tr>
    <tr>
      <td>$V_\beta$</td>
      <td>$1$</td>
      <td>$\dfrac{\varepsilon_{V_\alpha} + \varepsilon_{V_\beta} + 2\varepsilon_0}{2}$</td>
      <td>$\sqrt{2\nu}$</td>
      <td>$\dfrac{\varepsilon_{V_\beta} + \varepsilon_{I_B}}{2}$</td>
    </tr>
    <tr>
      <td>$A_\beta$</td>
      <td>$1$</td>
      <td>$\varepsilon_{A_\beta} - \varepsilon_{V_\beta} + \varepsilon_{V_\alpha}$</td>
      <td>$2\nu$</td>
      <td>$\varepsilon_{A_\beta} - \varepsilon_{V_\beta} + \varepsilon_{I_B} - 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$B_\alpha$</td>
      <td>$1$</td>
      <td>$\varepsilon_{B_\alpha} + \varepsilon_{V_\beta} - \varepsilon_{V_\alpha}$</td>
      <td>$\dfrac{1}{2\nu}$</td>
      <td>$\varepsilon_{B_\alpha} + \varepsilon_{V_\beta} - \varepsilon_{I_B} + 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$I_A$</td>
      <td>$1$</td>
      <td>$\varepsilon_{I_A} - \varepsilon_0 + \dfrac{\varepsilon_{V_\alpha} - \varepsilon_{V_\beta}}{2}$</td>
      <td>$\sqrt{2\nu}$</td>
      <td>$\varepsilon_{I_A} - 2\varepsilon_0 + \dfrac{\varepsilon_{I_B} - \varepsilon_{V_\beta}}{2}$</td>
    </tr>
    <tr>
      <td>$I_B$</td>
      <td>$1$</td>
      <td>$\varepsilon_{I_B} - \varepsilon_0 + \dfrac{\varepsilon_{V_\beta} - \varepsilon_{V_\alpha}}{2}$</td>
      <td>$\dfrac{1}{\sqrt{2\nu}}$</td>
      <td>$\dfrac{\varepsilon_{V_\beta} + \varepsilon_{I_B}}{2}$</td>
    </tr>
    <tr>
      <td>$A_\beta B_\alpha$</td>
      <td>$\sigma_{A_\beta B_\alpha}$</td>
      <td>$\varepsilon_{A_\beta B_\alpha}$</td>
      <td>$\sigma_{A_\beta B_\alpha}$</td>
      <td>$\varepsilon_{A_\beta B_\alpha}$</td>
    </tr>
    <tr>
      <td>$V_\alpha B_\alpha$</td>
      <td>$\sigma_{V_\alpha B_\alpha}$</td>
      <td>$\varepsilon_{V_\alpha B_\alpha} + \varepsilon_0 + \dfrac{3(\varepsilon_{V_\beta} - \varepsilon_{V_\alpha})}{2}$</td>
      <td>$\dfrac{\sigma_{V_\alpha B_\alpha}}{(2\nu)^{3/2}}$</td>
      <td>$\varepsilon_{V_\alpha B_\alpha} + 4\varepsilon_0 + \dfrac{3(\varepsilon_{V_\beta} - \varepsilon_{I_B})}{2}$</td>
    </tr>
    <tr>
      <td>$V_\beta A_\beta$</td>
      <td>$\sigma_{V_\beta B_\beta}$</td>
      <td>$\varepsilon_{V_\beta B_\beta} + \varepsilon_0 + \dfrac{3(\varepsilon_{V_\alpha} - \varepsilon_{V_\beta})}{2}$</td>
      <td>$(2\nu)^{3/2}\sigma_{V_\beta B_\beta}$</td>
      <td>$\varepsilon_{V_\beta A_\beta} - 2\varepsilon_0 - \dfrac{3(\varepsilon_{V_\beta} - \varepsilon_{I_B})}{2}$</td>
    </tr>
    <tr>
      <td>$V_\beta B_\alpha$</td>
      <td>$\sigma_{V_\beta B_\alpha}$</td>
      <td>$\varepsilon_{V_\beta B_\alpha} + \varepsilon_0 + \dfrac{\varepsilon_{V_\beta} - \varepsilon_{V_\alpha}}{2}$</td>
      <td>$\dfrac{\sigma_{V_\beta B_\alpha}}{\sqrt{2\nu}}$</td>
      <td>$\varepsilon_{V_\beta B_\alpha} + 2\varepsilon_0 + \dfrac{\varepsilon_{V_\beta} - \varepsilon_{I_B}}{2}$</td>
    </tr>
    <tr>
      <td>$V_\beta I_B$</td>
      <td>$\sigma_{V_\beta I_B}$</td>
      <td>$\varepsilon_{V_\beta I_B}$</td>
      <td>$\sigma_{V_\beta I_B}$</td>
      <td>$\varepsilon_{V_\beta I_B}$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta$</td>
      <td>$\sigma_{V_\alpha V_\beta}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta} + 2\varepsilon_0$</td>
      <td>$\sigma_{V_\alpha V_\beta}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta} + 2\varepsilon_0$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^2$</td>
      <td>$\sigma_{V_\alpha V_\beta^2}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^2} + 3\varepsilon_0 + \dfrac{\varepsilon_{V_\alpha} - \varepsilon_{V_\beta}}{2}$</td>
      <td>$\sqrt{2\nu}\sigma_{V_\alpha V_\beta^2}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^2} + 2\varepsilon_0 + \dfrac{\varepsilon_{I_B} - \varepsilon_{V_\beta}}{2}$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^3$</td>
      <td>$\sigma_{V_\alpha V_\beta^3}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^3} + (\varepsilon_{V_\alpha} - \varepsilon_{V_\beta}) + 4\varepsilon_0$</td>
      <td>$2\nu\sigma_{V_\alpha V_\beta^3}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^3} + 2\varepsilon_0 + \varepsilon_{I_B} - \varepsilon_{V_\beta}$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^4$</td>
      <td>$\sigma_{V_\alpha V_\beta^4}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^4} + 5\varepsilon_0 + \dfrac{3(\varepsilon_{V_\alpha} - \varepsilon_{V_\beta})}{2}$</td>
      <td>$(2\nu)^{3/2}\sigma_{V_\alpha V_\beta^4}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^4} + 2\varepsilon_0 + \dfrac{3(\varepsilon_{I_B} - \varepsilon_{V_\beta})}{2}$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^5$</td>
      <td>$\sigma_{V_\alpha V_\beta^5}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^5} + 2(\varepsilon_{V_\alpha} - \varepsilon_{V_\beta}) + 6\varepsilon_0$</td>
      <td>$(2\nu)^2\sigma_{V_\alpha V_\beta^5}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^5} + 2\varepsilon_0 + 2(\varepsilon_{I_B} - \varepsilon_{V_\beta})$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^6$</td>
      <td>$\sigma_{V_\alpha V_\beta^6}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^6} + 7\varepsilon_0 + \dfrac{5(\varepsilon_{V_\alpha} - \varepsilon_{V_\beta})}{2}$</td>
      <td>$(2\nu)^{5/2}\sigma_{V_\alpha V_\beta^6}$</td>
      <td>$\varepsilon_{V_\alpha V_\beta^6} + 2\varepsilon_0 + \dfrac{5(\varepsilon_{I_B} - \varepsilon_{V_\beta})}{2}$</td>
    </tr>
  </tbody>
</table>


Table 7: Arrhenius parameters (prefactors $X_d$ and effective formation energies $\bar{\varepsilon}_d$) of point defects in TaC and HfC with stoichiometric ($x=0$) and metal-rich ($x>0$) compositions. The values in square brackets were computed from the literature reports.

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="4">TaC</th>
      <th colspan="4">HfC</th>
    </tr>
    <tr>
      <th></th>
      <th colspan="2">$x=0$, $V_C$ &amp; $V_{Ta}$</th>
      <th colspan="2">$x>0$, $V_C$</th>
      <th colspan="2">$x=0$, $V_C$ &amp; $I_C$</th>
      <th colspan="2">$x>0$, $V_C$</th>
    </tr>
    <tr>
      <th>Defect</th>
      <th>$X_d^0$</th>
      <th>$\bar{\varepsilon}_d$ (eV)</th>
      <th>$X_d^0$</th>
      <th>$\bar{\varepsilon}_d$ (eV)</th>
      <th>$X_d^0$</th>
      <th>$\bar{\varepsilon}_d$ (eV)</th>
      <th>$X_d^0$</th>
      <th>$\bar{\varepsilon}_d$ (eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$V_\alpha$</td>
      <td>1</td>
      <td>1.28</td>
      <td>$\dfrac{1}{4x}$</td>
      <td>2.55 [2.65]$^b$</td>
      <td>$\dfrac{1}{\sqrt{2\nu}}$</td>
      <td>5.34</td>
      <td>$\dfrac{1}{4x}$</td>
      <td>8.44 [8.57]$^a$</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>[8.64]$^b$</td>
    </tr>
    <tr>
      <td>$V_\beta$</td>
      <td>1</td>
      <td>1.28</td>
      <td>$4x$</td>
      <td>0.00</td>
      <td>$\sqrt{2\nu}$</td>
      <td>3.11</td>
      <td>$4x$</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>$A_\beta$</td>
      <td>1</td>
      <td>13.44</td>
      <td>$16x^2$</td>
      <td>10.90</td>
      <td>$2\nu$</td>
      <td>16.00</td>
      <td>$16x^2$</td>
      <td>9.79</td>
    </tr>
    <tr>
      <td>$B_\alpha$</td>
      <td>1</td>
      <td>5.93</td>
      <td>$\dfrac{1}{16x^2}$</td>
      <td>8.48</td>
      <td>$\dfrac{1}{2\nu}$</td>
      <td>6.93</td>
      <td>$\dfrac{1}{16x^2}$</td>
      <td>13.14 [13.51]$^a$</td>
    </tr>
    <tr>
      <td>$I_A$</td>
      <td>1</td>
      <td>13.76</td>
      <td>$4x$</td>
      <td>12.48</td>
      <td>$\sqrt{2\nu}$</td>
      <td>13.66</td>
      <td>$4x$</td>
      <td>10.55</td>
    </tr>
    <tr>
      <td>$I_B$</td>
      <td>1</td>
      <td>5.47</td>
      <td>$\dfrac{1}{4x}$</td>
      <td>6.74</td>
      <td>$\dfrac{1}{\sqrt{2\nu}}$</td>
      <td>3.11</td>
      <td>$\dfrac{1}{4x}$</td>
      <td>6.21</td>
    </tr>
    <tr>
      <td>$A_\beta B_\alpha$</td>
      <td>6</td>
      <td>5.45</td>
      <td>6</td>
      <td>5.45</td>
      <td>6</td>
      <td>5.00</td>
      <td>6</td>
      <td>5.00</td>
    </tr>
    <tr>
      <td>$V_\alpha B_\alpha$</td>
      <td>6</td>
      <td>2.76</td>
      <td>$\dfrac{6}{64x^3}$</td>
      <td>6.58</td>
      <td>$\dfrac{6}{(2\nu)^{3/2}}$</td>
      <td>5.03</td>
      <td>$\dfrac{6}{64x^3}$</td>
      <td>14.34</td>
    </tr>
    <tr>
      <td>$V_\beta A_\beta$</td>
      <td>6</td>
      <td>13.30</td>
      <td>$384x^3$</td>
      <td>9.47</td>
      <td>$12(2\nu)^{3/2}$</td>
      <td>18.05</td>
      <td>$384x^3$</td>
      <td>8.73</td>
    </tr>
    <tr>
      <td>$V_\beta B_\alpha$</td>
      <td>*</td>
      <td>*</td>
      <td>*</td>
      <td></td>
      <td>$\dfrac{6}{\sqrt{2\nu}}$</td>
      <td>6.50</td>
      <td>$\dfrac{6}{4x}$</td>
      <td>9.60</td>
    </tr>
    <tr>
      <td>$V_\beta I_B$</td>
      <td>*</td>
      <td>*</td>
      <td>*</td>
      <td></td>
      <td>8</td>
      <td>4.30</td>
      <td>8</td>
      <td>4.30</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta$</td>
      <td>6</td>
      <td>2.41</td>
      <td>6</td>
      <td>2.41 [2.49]$^b$</td>
      <td>6</td>
      <td>6.84</td>
      <td>6</td>
      <td>6.84 [7.08]$^a$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^2$ (T)</td>
      <td>12</td>
      <td>3.71</td>
      <td>$48x$</td>
      <td>2.43 [2.50]$^b$</td>
      <td>$12\sqrt{2\nu}$</td>
      <td>8.65</td>
      <td>$48x$</td>
      <td>5.54 [5.85]$^b$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^2$ (L)</td>
      <td>3</td>
      <td>3.57</td>
      <td>$12x$</td>
      <td>2.29 [2.36]$^b$</td>
      <td>$3\sqrt{2\nu}$</td>
      <td>8.88</td>
      <td>$12x$</td>
      <td>5.77 [6.05]$^b$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^3$ (IP)</td>
      <td>12</td>
      <td>5.05</td>
      <td>$192x^2$</td>
      <td>2.50</td>
      <td>$24\nu$</td>
      <td>10.76</td>
      <td>$192x^2$</td>
      <td>4.55 [4.31]$^b$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^3$ (OP)</td>
      <td>8</td>
      <td>5.07</td>
      <td>$128x^2$</td>
      <td>2.52 [2.55]$^b$</td>
      <td>$16\nu$</td>
      <td>10.92</td>
      <td>$128x^2$</td>
      <td>4.71 [5.00]$^b$</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^4$ (IP)</td>
      <td>3</td>
      <td>6.44</td>
      <td>$192x^3$</td>
      <td>2.61 [2.65]$^b$</td>
      <td>$3(2\nu)^{3/2}$</td>
      <td>13.05</td>
      <td>$192x^3$</td>
      <td>3.73</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^4$ (OP)</td>
      <td>12</td>
      <td>6.41</td>
      <td>$768x^3$</td>
      <td>2.58</td>
      <td>$12(2\nu)^{3/2}$</td>
      <td>13.41</td>
      <td>$768x^3$</td>
      <td>4.10 [4.18]$^b$,</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^5$</td>
      <td>6</td>
      <td>7.70</td>
      <td>$1536x^4$</td>
      <td>2.60 [2.70]$^b$</td>
      <td>$6(2\nu)^2$</td>
      <td>15.75</td>
      <td>$1536x^4$</td>
      <td>3.33 [3.45]$^b$,</td>
    </tr>
    <tr>
      <td>$V_\alpha V_\beta^6$</td>
      <td>1</td>
      <td>9.06</td>
      <td>$1024x^5$</td>
      <td>2.68 [2.78]$^b$</td>
      <td>$(2\nu)^{5/2}$</td>
      <td>18.47</td>
      <td>$1024x^5$</td>
      <td>2.95 [2.95]$^b$</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>[3.05]$^a$</td>
    </tr>
  </tbody>
</table>

$^a$Ref. [16] , $^b$Ref. [15]

![](./images/1229502265828573199_1.jpg)

Figure 1: Initial (left column) and relaxed (right column) structures of selected point-defect pairs undergoing structural reconstructions. (a) $V_\beta B_\alpha$ pair in HfC (b) $V_\alpha B_\alpha$ pair in TaC and HfC. (c) $A_\beta B_\alpha$ antisite pair in TaC and HfC. (d) $V_\beta A_\beta$ pair in TaC . The structures are viewed along a $\langle 100 \rangle$ direction. The metal atoms, carbon atoms, metal vacancies, and carbon vacancies are shown in green, yellow, purple, and light gray, respectively. Some atoms are encircled in red for tracking.

![](./images/1229502265828573199_2.jpg)

Figure 2: Interaction energy between carbon vacancies in the TaC and HfC carbides as a function of vacancy separation. The literature data from $^a$Ref. [15] shows similar trends.

![](./images/1229502265828573199_3.jpg)

Figure 3: Composition dependence of point defect concentrations in (a) TaC and (b) HfC at 2500 K.

![](./images/1229502265828573199_4.jpg)

Figure 4: Arrhenius plots of point defect concentrations in TaC at (a) stoichiometric composition and (b) Ta-rich composition of $c_{\text{Ta}} = 0.52$ ($x=0.02$).

![](./images/1229502265828573199_5.jpg)

Figure 5: Arrhenius plots of point defect concentrations in HfC at (a) stoichiometric composition and (b) Hf-rich composition of $c_{\text{Hf}}=0.52$ ($x=0.02$).

$\boldsymbol{32}$

**SUPPLEMENTARY INFORMATION**

First-principles prediction of point defect energies and concentrations
in the tantalum and hafnium carbides

I. Khatri, R. K. Koju, and Y. Mishin

Department of Physics and Astronomy, MSN 3F3, George Mason
University, Fairfax, Virginia 22030, USA

![](./images/1229502265828573199_6.jpg)

Figure 1: Initial (left column) and relaxed (right column) structures of point-defects undergoing structural reconstructions. (a) $V_\alpha$ (b) $V_\beta$, (c) $V_\alpha V_\beta$, and (d) $A_\beta$ in TaC and HfC. The structures are viewed along a $\langle 100 \rangle$ direction. The metal atoms, carbon atoms, metal vacancy and carbon vacancy are shown in green, yellow, purple, and light gray, respectively. Some atoms are encircled in red for tracking.

![](./images/1229502265828573199_7.jpg)

Figure 2: Initial (left column) and relaxed (right column) structures of point-defects undergoing structural reconstructions. (a) $B_\alpha$ in TaC and HfC, (b) $I_B$ in TaC and HfC, (c) $I_A$ in TaC and HfC, and (d) $V_\beta I_B$ in HfC. The structures are viewed along a $\langle 100 \rangle$ direction. The metal atoms, carbon atoms, metal vacancy and carbon vacancy are shown in green, yellow, purple, and light gray, respectively. Some atoms are encircled in red for tracking.

![](./images/1229502265828573199_8.jpg)

Figure 3: Initial (left column) and relaxed (right column) structures of point-defect clusters undergoing structural reconstructions. (a) $V_\alpha V_\beta^2(L)$, (b) $V_\alpha V_\beta^2(T)$ (c) $V_\alpha V_\beta^3(OP)$, and (d) $V_\alpha V_\beta^3(IP)$ in TaC and HfC. The structures are vie wed along a $\langle 100 \rangle$ direction. The metal atoms, carbon atoms, metal vacancies and carbon vacancies are shown in green, yellow, purple, and light gray, respectively.

![](./images/1229502265828573199_9.jpg)

Figure 4: Initial (left column) and relaxed (right column) structures of point-defect clusters undergoing structural reconstructions. (a) $V_\alpha V_\beta^4(IP)$, (b) $V_\alpha V_\beta^4(OP)$, (c) $V_\alpha V_\beta^5$, and (d) $V_\alpha V_\beta^6$ in TaC and HfC. The structures are viewed along a $\langle 100 \rangle$ direction. The metal atoms, carbon atoms, metal vacancy and carbon vacancy are shown in green, yellow, purple, and light gray, respectively.

![](./images/1229502265828573199_10.jpg)

Figure 5: Raw energy of metal vacancy ($\epsilon_{V_{\alpha}}$) as the function of reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure.

![](./images/1229502265828573199_11.jpg)

Figure 6: Raw energy of antisite on metal sublattice ($\epsilon_{B_{\alpha}}$) as the function of reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure.

![](./images/1229502265828573199_12.jpg)

Figure 7: Raw energy of carbon vacancy ($\epsilon_{V_{\beta}}$) and antisite on carbon sublattice ($\epsilon_{A_{\beta}}$) as a function of the reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure. Open and closed circles of carbon vacancy ($V_{\beta}$) are for HfC and TaC respectively.

![](./images/1229502265828573199_13.jpg)

Figure 8: Raw energy of metal interstitial ($\epsilon_{I_{\alpha}}$) in tetrahedral position as a function of the reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure.

![](./images/1229502265828573199_14.jpg)

Figure 9: Raw energy of carbon interstitial $(\epsilon_{I_{\beta}})$ in tetrahedral position as a function of the reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure. Open and closed triangles are for HfC and TaC respectively.

![](./images/1229502265828573199_15.jpg)

Figure 10: Raw energy of Frenkel pair $(\epsilon_{V_{\beta}I_{\beta}})$ in HfC and antisite pair $(\epsilon_{B_{\alpha}A_{\beta}})$ in HfC and TaC as a function of the reciprocal of the number of atoms prior to any defects in rocksalt crystal structure.

![](./images/1229502265828573199_16.jpg)

Figure 11: Raw energy of divacancy ($\epsilon_{V_\alpha V_\beta}$) as a function of the reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure.

![](./images/1229502265828573199_17.jpg)

Figure 12: Raw energy of three vacancies cluster ($\epsilon_{V_\alpha V_\beta^2}$) in Linear (L) and Triangular (T) configurations as a function of the reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure.

![](./images/1229502265828573199_18.jpg)

Figure 13: Raw energy of four vacancies cluster ($\epsilon_{V_\alpha V_\beta^3}$) with three carbon vacancies are off-plane (OP) and in-plane (IP) configurations, as a function of the reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure.

![](./images/1229502265828573199_19.jpg)

Figure 14: Raw energy of five vacancies cluster ($\epsilon_{V_\alpha V_\beta^4}$) with four carbon vacancies are off-plane (OP) and in-plane (IP) configurations, as a function of the reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure.

![](./images/1229502265828573199_20.jpg)

Figure 15: Raw energy of six vacancies cluster ($\epsilon_{V_{\alpha}V_{\beta}^5}$) as a function of the reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure.

![](./images/1229502265828573199_21.jpg)

Figure 16: Raw energy of seven vacancies cluster ($\epsilon_{V_{\alpha}V_{\beta}^6}$) as a function of the reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure.

![](./images/1229502265828573199_22.jpg)

Figure 17: Raw energy of vacancy antisite pair on metal sublattice $(\epsilon_{V_{\alpha}B_{\alpha}})$ as a function of the reciprocal of the number of atoms prior to any defects for TaC and HfC in rocksalt crystal structure.

![](./images/1229502265828573199_23.jpg)

Figure 18: Raw energy of vacancy antisite pair on carbon sublattice $(\epsilon_{V_{\beta}A_{\beta}})$ and carbon vacancy and antisite pair on metal sublattice $(\epsilon_{V_{\beta}B_{\alpha}})$ in HfC as a function of the reciprocal of the number of atoms prior to any defects in rocksalt crystal structure.

![](./images/1229502265828573199_24.jpg)

Figure 19: Raw energy of vacancy antisite pair on carbon sublattice $(\epsilon_{V_{\beta}A_{\beta}})$ in TaC as a function of the reciprocal of the number of atoms prior to any defects in rocksalt crystal structure.

![](./images/1229502265828573199_25.jpg)
![](./images/1229502265828573199_26.jpg)

Figure 20: Composition dependence of point defect concentrations in (a) TaC and (b) HfC at 3500 K.


Table 8: The k-points used for raw energy calculations of various defects within the su-
percells of HfC and TaC obtained through the repetition of the relaxed conventional 8-
atom unit cell of the B1 crystal structure.

<table>
  <thead>
    <tr>
      <th>Supercell Size (atoms)</th>
      <th>K-points in TaC</th>
      <th>K-points in HfC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$2 \times 2 \times 3$ (96)</td>
      <td>$11 \times 11 \times 7$</td>
      <td>$2 \times 2 \times 1$</td>
    </tr>
    <tr>
      <td>$3 \times 3 \times 2$ (144)</td>
      <td>$7 \times 7 \times 11$</td>
      <td>$1 \times 1 \times 2$</td>
    </tr>
    <tr>
      <td>$3 \times 3 \times 3$ (216)</td>
      <td>$7 \times 7 \times 7$</td>
      <td>$3 \times 3 \times 3$</td>
    </tr>
    <tr>
      <td>$3 \times 3 \times 4$ (288)</td>
      <td>$6 \times 6 \times 4$</td>
      <td>$2 \times 2 \times 1$</td>
    </tr>
    <tr>
      <td>$4 \times 4 \times 3$ (384)</td>
      <td>$4 \times 4 \times 6$</td>
      <td>$1 \times 1 \times 2$</td>
    </tr>
    <tr>
      <td>$4 \times 4 \times 4$ (512)</td>
      <td>$5 \times 5 \times 5$</td>
      <td>$1 \times 1 \times 1$</td>
    </tr>
  </tbody>
</table>