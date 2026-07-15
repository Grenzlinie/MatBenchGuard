First Principles Study of Intrinsic and Extrinsic Point Defects in Monolayer WSe₂

Yujie Zheng$^{1,2}$ and Su Ying Quek$^{1,2,*}$

$^{1}$Department of Physics, National University of Singapore, 2 Science Drive 3, 117542, Singapore

$^{2}$Centre for Advanced 2D Materials, National University of Singapore, Block S14, Level 6, 6 Science Drive 2, 117546, Singapore

* To whom correspondence should be addressed: phyqsy@nus.edu.sg

Abstract

We present a detailed first principles density functional theory study of intrinsic and extrinsic point defects in monolayer (ML) WSe₂. Among the intrinsic point defects, Se vacancies (Se$_{\text{vac}}$) have the lowest formation energy (disregarding Se adatoms that can be removed with annealing). The defects with the next smallest formation energies (at least 1 eV larger) are Se$_{\text{W}}$ (Se substituting W atoms in an antisite defect), W$_{\text{vac}}$ (W vacancies) and 2Se$_{\text{vac}}$ (Se divacancies). All these intrinsic defects have gap states that are not spin-polarized. The presence of a graphite substrate does not change the formation energies of these defects significantly. For the extrinsic point defects, we focus on O, O₂, H, H₂ and C interacting with perfect WSe₂ and its intrinsic point defects. The preferred binding site in perfect WSe₂ is the interstitial site for atomic O, H and C. These interstitial defects have no gap states. The gap states of the intrinsic defects are modified by interaction with O, O₂, H, H₂ and C. In particular, the gap states of Se$_{\text{vac}}$ and 2Se$_{\text{vac}}$ are completely removed by interaction with O and O₂. This is consistent with the significantly larger stability of O-related defects compared to H- and C-related defects. The preferred binding site for O is Se$_{\text{vac}}$, while that for H is Se$_{\text{W}}$. H bonded to Se$_{\text{W}}$ results in spin-polarized gap states, which may be useful in defect engineering for spintronics applications. The charge transition levels and ionization energies of these defects are also computed. H in the interstitial site is an effective donor, while all the other defects are deep donors or acceptors in isolated WSe₂ ML.

### I. INTRODUCTION

The field of two-dimensional (2D) materials has expanded rapidly since the first isolation of graphene [1-5]. It is now experimentally possible to synthesize monolayers of a wide range of 2D materials, using mechanical and chemical exfoliation, chemical vapor deposition (CVD) or molecular beam epitaxy techniques [2-5]. These monolayers are of interest in a wide range of applications, such as in flexible electronics, photonics, optoelectronics, catalysis and sensing [2-5]. To this end, a thorough fundamental understanding of the physical and chemical properties of these 2D materials is critical.

Despite rapid experimental advancements, synthesizing defect-free 2D materials is still far from reach. Compared to bulk materials, defects in 2D materials are expected to have a more significant impact on their electronic properties, especially for semiconducting 2D materials, where defects may introduce states in the band gap [6-8] or serve as dopants [9,10]. The high surface-to-volume ratio in 2D materials also makes them more susceptible to unintentional reactions with chemicals in the environment, giving rise to extrinsic defects. For example, gases may interact with intrinsic defects in 2D materials, such as vacancy sites, changing their optical properties [11,12]. Some of the most interesting properties of 2D materials arise from the presence of defects. For example, single photon emission has recently been observed in 2D materials such as WSe₂ [13-17] and hexagonal boron nitride [18-20], and the single photons are believed to come from localized defect states, the nature of which were largely unknown.

Transition metal dichalcogenides (TMDs) are among the most common of the semiconducting 2D materials. MoS₂ is a prototypical TMD material that has been widely studied for applications in next-generation electronics [21-24]. Consistent with first principles predictions [7,8], sulfur vacancies (Sᵥₐc) are the most commonly observed defects in MoS₂ [25-29]. These Sᵥₐc defects were found experimentally to play a large role in reducing the

mobility of MoS₂ [28,30]. On the other hand, the threshold voltage of MoS₂ field-effect transistors can be tuned by controlling the density of S<sub>vac</sub> through surface treatments [31]. S<sub>vac</sub> are predicted to be deep acceptors in isolated MoS₂ monolayers [7]. Recent ionization dynamics experiments have found that S<sub>vac</sub> in MoS₂ monolayers on Au substrates are neutral or negatively charged [32]. The negative charge in these S<sub>vac</sub> comes not from MoS₂, but from the Au substrates, and results in the pinning of the Fermi level at the S<sub>vac</sub> gap states near the conduction band minimum (CBM), thus explaining the typical n-type characteristics of supported MoS₂ monolayers [32]. In contrast to MoS₂, WSe₂ was the first monolayer TMD discovered to have ambipolar and p-type characteristics [33-36]. WSe₂ has also attracted much recent attention because of the discovery of single photon emission from WSe₂ monolayers, [13-17] which arise from localized electronic states [37,38]. Thus far, single photon emission has not been reported in MoS₂. Taken together, these distinct properties of WSe₂ found experimentally underscore the importance of a systematic study of defects in this material.

Point defects are the most common and simple defect structures in TMDs. First principles density functional theory (DFT) studies on intrinsic point defects in TMDs have provided much useful information on the formation energies and possible charge states of these defects [6-8]. The prediction that S<sub>vac</sub> is the most likely point defect in MoS₂ has been verified experimentally, by a combination of scanning transmission electron microscopy (STEM) [25,27] and scanning tunneling microscopy (STM) [26,29]. Researchers have also enhanced the mobility of MoS₂ by using thiol chemistry to heal the S<sub>vac</sub> [28], thus indirectly showing that S<sub>vac</sub> are prevalent in MoS₂ samples. However, even though Se vacancies (Se<sub>vac</sub>) were predicted to be the most likely point defect in WSe₂ [8], it was recently suggested based on scanning tunneling microscopy (STM) images, that W vacancies (W<sub>vac</sub>) are instead the most abundant point defect in WSe₂ monolayers on graphite [39]. Using a combination of

DFT calculations as well as STM and scanning transmission electron microscopy (STEM) experiments, we have shown that $W_{vac}$ are not present in WSe₂. The most abundant point defect in WSe₂ monolayers is found to be an extrinsic defect, with an O atom substituting a Se atom ($O_{Se}$).[40] These $O_{Se}$ defects are very stable and arise from the dissociation of $O_2$ at $Se_{vac}$ sites, which can take place easily at room temperature [40]. As discussed above, extrinsic defects can play a significant role in 2D materials because of the high surface-to-volume ratio, increasing the possibility of intrinsic defects reacting with gases and chemicals in the environment. Several extrinsic defects in 2D TMDs, such as naturally found Re impurities in MoS₂ [41] and Cr impurities in WS₂ [42], have also been discussed in the literature. Besides metal impurities and O-related defects, it is also important to consider H- and C-related extrinsic defects, because of the presence of hydrocarbons and reducing agents such as $H_2$ gas during the CVD growth process [34,43-46].

In this work, we explore, using first principles DFT calculations, the atomic and electronic structure, and the formation energies of intrinsic point defects found in monolayer WSe₂ supported on graphite substrates, as well as O, C and H-related extrinsic point defects in monolayer WSe₂. The ionization energies (charge states) of the most stable point defects in each category are also studied. $Se_{vac}$ has the lowest formation energy among all the intrinsic point defects considered. The $Se_{vac}$ gap states are passivated by O and $O_2$. The interstitial (hollow) site is the favored binding site for atomic O, H and C in perfect WSe₂ ML, and these defects have no gap states. $H_{ins}$ (H at the interstitial site) acts as a donor. H adsorbs stably at $W_{vac}$ and $Sew$ (antisite defect with Se substituting a W site), giving rise to defects with spin-polarized gap states. Thus, interesting magnetic properties may be induced if these H-related defects can be engineered, e.g., by exposing WSe₂ ML to atomic H [47]. Besides $H_{ins}$, all the other defects considered here have ionization energies that are larger than 0.6 eV, indicating that the defects are not effective dopants in isolated WSe₂ monolayers. However, $W_{vac}$ and

Sew may become acceptors if the Fermi level (E_F) is positioned close to mid-gap by a substrate.

## II. METHODS

The DFT calculations were performed using projector augmented wave (PAW) [48] potentials with the generalized gradient approximation GGA-PBE [49] for the exchange-correlation functional, as implemented in the VASP code [50,51]. Van der Waals interactions were included by adding Grimme's D2 corrections [52]. Spin-polarization was included for all neutral defect structures and for O₂. The atoms are all relaxed with a force convergence criteria of 0.01 eV/Å for WSe₂ monolayers (ML), and 0.05 eV/Å for the WSe₂ ML supported on graphite. A kinetic energy cutoff of 400 eV is used for the plane wave basis set. We have tested that the total energy of bulk WSe₂ is converged for this value of the energy cutoff, as well as with a Monkhorst Pack k-grid sampling of 10 x 10 x 4 in the bulk WSe₂ unit cell. The relaxed lattice parameters for bulk WSe₂ compare well to the experimental values (theory: a = 3.327 Å, c = 12.788 Å; experiment [53]: a = 3.282 Å, c = 12.96 Å). The formation energies and densities of states (DOS) of defects in isolated WSe₂ ML were obtained with a 5 x 5 supercell with a vacuum height of larger than 20 Å to separate periodic slabs. A 2 x 2 k-mesh was used for geometry optimization in this 5 x 5 supercell, while a 6 x 6 k-mesh was used for the DOS calculations. The graphite lattice constant obtained theoretically is also close to experiment (theory: a = 2.464 Å, c = 6.432 Å; experiment [54]: a = 2.461 Å, c = 6.709 Å), with a converged k-mesh of 16 x 16 x 6 in the graphite unit cell. WSe₂ ML on graphite was modeled using 3 layers of graphite, with a 3 x 3 WSe₂ supercell on top of a 4 x 4 supercell of graphite and 13 Å of vacuum. In this supercell, the strain on WSe₂ was 0.61 % and the strain on graphite was - 0.65 %. For this supercell, we used a k-mesh of 6 x 6 x 1 for geometry optimization and 10 x 10 x 1 for DOS calculations. Defects in WSe₂ ML on graphite were studied with an even larger

cell, consisting of a $2 \times \sqrt{3} R 30^{\circ}$ supercell of the WSe₂/graphite supercell described above. Here,
we used a k-mesh of 2 x 2 x 1 for geometry optimization and 4 x 4 x 1 for DOS calculations.

The formation energies $E_{f}(x, q)$ for the defects $(x)$ in charge state $q$ are defined as [55]

$$
E_{f}(x, q)=E(x, q)-E_{\text {pristine }}-\sum_{i} n_{i} \mu_{i}+q\left(E_{v}+E_{F}\right) \tag{1}
$$

where $E(x, q)$ and $E_{\text {pristine }}$ are the total energies of the WSe₂/graphite supercell with and
without the defect, respectively. $n_{i}$ denotes the number of atoms of element $i$ that have been
added $(n_{i}>0)$ or removed $(n_{i}<0)$, and $\mu_{i}$ is the chemical potential of element $i$. $E_{F}$ is the
Fermi energy relative to valance band maximum $E_{v}$ of WSe₂ ($E_{F}$ values range from 0 to the
size of the band gap). We elaborate on the determination of $E_{v}$ below.

The chemical potentials of W and Se are linked by the stability of WSe₂, *i.e.*

$$
\mu_{\mathrm{WSe}_{2}}=\mu_{W}+2 \mu_{\mathrm{Se}} \tag{2}
$$

$\mu_{\mathrm{WSe}_{2}}$ is the total energy per formula unit of bulk WSe₂ (the conclusions are unchanged if we
use instead the total energy per formula unit of monolayer WSe₂). $\mu_{W}^{\max }$ and $\mu_{Se}^{\max }$ are total
energies per atom of bcc W metal and the molecular crystal ( $R \overline{3}$ phase) of Se₆ molecules,
respectively. The minimum of the Se chemical potentials can be derived from formula (2), *i.e.*,
$\mu_{Se}^{\min }=(\mu_{\mathrm{WSe}_{2}}-\mu_{W}^{\max }) / 2$. The chemical potentials of O and H are half of the total energies of
O₂ and H₂ gas, respectively. The chemical potential of C is the total energy per atom of graphite.

For charge neutral intrinsic point defects, equation (1) reduces to

$$
E_{f}(x)=E(x)-E_{\text {pristine }}-\sum_{i} n_{i} \mu_{i} \tag{3}
$$

For charged defects, the transition energy is defined as [55]

$$
\varepsilon\left(q / q^{\prime}\right)+E_{v}=\left[E(x, q)-E\left(x, q^{\prime}\right)\right] /\left(q^{\prime}-q\right) \tag{4}
$$

where $q$ and $q'$ are two different charge states of the same defect ($x$). However, for charged defects in a 2D system, the Coulomb interaction energy between a charged defect and its periodic images diverges as $L_z \to \infty$ [55]. The ionization energies (IE) of a defect are special cases of the defect transition energies, i.e $\varepsilon(q,q')$ relative to the band edges [55]. $\varepsilon(+/0)$ relative to conduction band minimum (CBM) defines a donor IE, and $\varepsilon(0/-)$ relative to valance band maximum (VBM), defines an acceptor IE [55]. The IE for a defect in a 2D material with a supercell of x-y area $S$ and height $L_z$ takes the asymptotic form [55]

$$
IE(S,L_z)=IE_0+\frac{\alpha}{\sqrt{S}}+\frac{\beta}{S}L_z \tag{5}
$$

where $IE(S,L_z)$ is a supercell-size-dependent quantity and $IE_0$ (converged) is the true and size-independent $IE$. $\alpha$ and $\beta$ are constants for each defect. According to equation (5), finding $IE(S,L_z)$ at different $S$ and $L_z$ will allow us to find $IE_0$ in 2D systems. If the supercell size is large enough, $IE(S,L_z)$ at a given fixed $S$ should be linear with respect to $L_z$. The intercept at $L_z=0$, $IE_0+\frac{\alpha}{\sqrt{S}}$, is found for each $S$. This intercept should be linear with respect to $\frac{1}{\sqrt{S}}$, and the intercept in this plot will be $IE_0$. We use this method (Method 1) with the dimensions of the supercell varying from 20 to $40\ \mathring{A}$ for $L_z$ and $7 \times 7$ to $9 \times 9$ supercells for $S$. A $3 \times 3 \times 1$ k-grid is used for these calculations.

The defect itself affects the band structure including the value $E_v$ in the calculation [56]. In order to obtain the value that $E_v$ would be for a larger supercell, a two-step procedure was used. First, $E_v$ is calculated for the perfect isolated WSe₂ ML by performing a band-structure calculation at the K point for each $L_z$. Next, the 1s core level of the perfect isolated WSe₂ ML

is aligned with the 1s core level of W in the supercell, furthest from the defect site; this alignment procedure is used to give the value of $E_v$ in the supercell.

Although the above method can calculate the IEs correctly, it requires many calculations. Komsa *et al.* [57] reported that different types of defects in a given 2D material have similar errors in the IE for fixed cell size and shape. Thus, using Method 1 as a benchmark, these errors can be estimated. We have found that a "special" cell (9×9 supercell with a vacuum height of 30 Å, corresponding to $L_z = 33.4$ Å) gives IEs that are within 0.2 eV of the converged $IE_0$ obtained using Method 1. Using this "special" cell, we thus estimate the IE of a larger set of defects. We call this Method 2.

## III. RESULTS AND DISCUSSION

### A. Intrinsic defects

#### 1. Atomic structure and Formation Energies

Graphite is a flat conducting substrate that is used for direct CVD growth of WSe₂ ML and for characterization of WSe₂ ML in STM [40,58]. Haldar *et al.* has studied in detail several intrinsic defects in isolated WSe₂ ML, in particular Se and W single and double vacancies, as well as interstitial defects [8]. Here, we study these and other intrinsic defects in WSe₂ ML on graphite. Fig. 1 shows the side view of the 13 different intrinsic point defects considered for WSe₂ ML on graphite. Se atoms in the upper and lower planes are labeled Se1 and Se2, respectively. Se1$_{\text{vac}}$ (Fig. 1a) refers to a defect where Se1 is missing, and Se2$_{\text{vac}}$ (Fig. 1b) refers to that where Se2 is missing. W$_{\text{vac}}$ (Fig. 1c) refers to a W vacancy, and 2Se$_{\text{vac}}$ (Fig. 1d) refers to a Se divacancy, where both Se1 and Se2 are missing (one on top of the other). In addition to vacancy sites, we have also considered antisite defects, adatoms, and interstitial defects where the Se and W atoms are in between the WSe₂ ML and the graphite substrate (Fig. 1l: Se$_{\text{int}}$; Fig. 1m: W$_{\text{int}}$). Se adatom and W adatom defects are shown in Fig. 1j (Se$_{\text{ad}}$)

and 1k (Wₐd), respectively. For the antisite defects, the nomenclature is as follows. Xᵧ implies that element X has substituted element Y. 2Sew refers to two Se atoms substituting a W atom, while W₂ₛₑ refers to one W atom substituting two Se atoms. Sew (Fig. 1e), Wₛₑ₁ (Fig. 1f), Wₛₑ₂ (Fig. 1g), 2Sew (Fig. 1h) and W₂ₛₑ (Fig. 1i) are considered here. Of these 13 defects, only 2Sew (Fig. 1h), W₂ₛₑ (Fig. 1i), Wₐd (Fig. 1k), Sₑᵢₙₜ (Fig. 1l) and Wᵢₙₜ (Fig. 1m) lead to significant changes in the atomic positions of WSe₂. In the Wᵥₐc structure, the Se-W bonds next to the defect site shorten by 1.6%, while in the Sₑᵥₐc and 2Sₑᵥₐc structures, the adjacent Se-W bnods lengthen by 0.4%. In Sew, the Se atom sits in the three-fold site occupied by W, forming three Se-Se bonds of equal bond length, 3.2% larger than a Se-W bond in perfect WSe₂ ML. Interestingly, the W adatom drops into the WSe₂ layer and bonds with a W atom and three neighboring Se atoms (Fig. 1k).

The formation energies of these intrinsic defects are shown in Fig. 2a for a range of chemical potentials ranging from the W-rich to the Se-rich limits. Se1ᵥₐc and Se2ᵥₐc have very similar formation energies and DOS. Thus, henceforth, we shall refer to them both as Sₑᵥₐc. Sₑₐd has the lowest formation energy regardless of the chemical potential. However, the formation energy is still positive, which indicates that the Se adatom can desorb or diffuse away during the high temperatures of CVD growth or subsequent annealing processes. Similarly, the interstitial Se atom between WSe₂ and graphite (Sₑᵢₙₜ) may also diffuse away. However, the vacancies and antisite defects, once formed, are less likely to be removed. Of all the vacancies and antisite defects, Sₑᵥₐc has the lowest formation energy even under Se-rich conditions. The formation energy of Sₑᵥₐc ranges from 2.2 eV (W-rich) to 2.8 eV (Se-rich). The defects with the next smallest formation energies are Se divacancy 2Sₑᵥₐc, Sew antisite defect, and Wᵥₐc, which all have very similar ranges of formation energies, between ~3.7-3.9 eV and ~5.1-5.5 eV (Fig. 2a; Table I). These formation energies are significantly larger than that of Sₑᵥₐc, indicating that Sₑᵥₐc is by far the most abundant intrinsic point defect

in WSe₂ monolayers on graphite. Of the three defects, 2Seᵥₐc, Seᵥ and Wᵥₐc, Seᵥ has the lowest formation energy under Se-rich conditions, while 2Seᵥₐc has the lowest formation energy under W-rich conditions. Most CVD growth conditions take place in the Se-rich limit, due to the low sublimation temperature of Se, and the abundance of Se vapor.[34,36,43,59] In this limit, our calculations predict that the most likely intrinsic defects for WSe₂ ML on graphite are Seᵥₐc, followed by Seᵥ, Wᵥₐc and 2Seᵥₐc (disregarding adatoms and interstitials), in that order. To investigate the effect of the graphite substrate on the formation energies, we also compute the formation energies of selected intrinsic defects in isolated WSe₂ ML (Fig. 2b; Table I). In general, the energy differences caused by the graphite substrate are small, compared to the actual formation energies of the defects. The relative formation energies are also unchanged by the graphite substrate. STEM experiments [40] have identified Seᵥₐc to be the most abundant defect in WSe₂ ML. Seᵥ and 2Seᵥₐc were also detected, but interestingly, no Wᵥₐc were found. It is possible that the 2Seᵥₐc defects were created due to electron bombardment during the STEM imaging process. We note that the electron beam could also knock away O atoms that we predict to be substituted in the Seᵥₐc sites [40].

## 2. Electronic Structure

The DOS projected onto the defect sites are plotted in Fig. 3 for the intrinsic defects in WSe₂ ML on graphite. Except for Seₐd, all the other intrinsic defects here have defect states in the band gap of WSe₂. The absence of gap states in Seₐd is consistent with the fact that it is the most energetically favorable defect. Spin polarized calculations were performed for these intrinsic defects in isolated WSe₂. None of these defects is spin polarized, except for Wₛₑ. Since Wₛₑ has a very large formation energy, the details are omitted here.

Two commonly used experimental methods to identify defects in 2D materials are STM and STEM studies. STEM is sensitive to relative atomic numbers in the sample, the

intensity of the image being approximately proportional to the square of the atomic number.

However, it will be difficult to detect atoms with much smaller atomic numbers relative to the other atoms in the sample, and damage to the sample can occur from the transmitting electron beam. STM images result from the tunneling of electrons between an STM metallic tip and the sample; these electrons are not energetic enough to create defects in the sample. Within the Tersoff-Hamann approximation [60], the STM image intensity is proportional to the local density of states that are available to contribute to the tunneling current, evaluated at the tip position. The relative voltage difference between the tip and the sample in turn determine the energy range of states available to contribute to the current. Thus, STM does not image the atoms directly, but rather the electronic states in an energy range that depends on the applied bias and the Fermi level. DFT calculations of electronic states are therefore very valuable to facilitate the identification of point defects observed in STM images.

Fig. 4 shows the STM images for a perfect WSe₂ ML on graphite (a commonly used substrate for STM studies of 2D materials). It is interesting to note that the bright spots in these images do not necessarily correspond to the positions of the Se atoms (which are located on the top surface). Bright spots are located at the Se atoms for images at -0.8 V and 1.2 V (sample bias), which respectively probe states 0.4 eV into the valence band, and 0.1 eV into the conduction band. However, for the image at -0.6 V sample bias (states 0.2 eV into the valence band), the bright spots are at the hollow sites. For the image at 1.3 V sample bias (states 0.2 eV into the conduction band), the bright spots are located at both the hollow sites and the Se sites. Generally, STM images can also be affected by other factors such as the tip-sample distance [61,62] and tip condition.

We next simulate the STM images of all the thirteen intrinsic defects considered in this work, as shown in Fig. 5. The bias-dependent STM images for these defects are all distinct, and reflect the local density of states of the defects near the band edges. The STM

image for $Se_{ad}$ has a much brighter spot at the Se adatom for both positive and negative bias voltages; this is expected because the Se adatom is much closer to the STM tip than the $WSe_2$ ML. Other atomic adsorbates would also result in very similar images. For the other point defects, it is possible that STM images can act as a "fingerprint" to help identify the point defect, but it is clear that multiple images acquired at different bias voltages for the same defect will greatly help to reduce the uncertainty in assigning the defect type. Since $Se_{vac}$ has the lowest formation energy among these defects, we discuss in particular the STM images of $Se_{vac}$. These images are similar to those predicted for $S_{vac}$ in $MoS_2$ [26], including simulations that include the STM tip explicitly [61]. The image for occupied states has a dark triangular depression that extends over several atomic positions, while that for unoccupied states has a dark circle surrounded by a bright circular shape. Experimentally, STM images for $MoS_2$ ML on graphite and on Au have uncovered point defects that resemble these images [26,29].

However, the STM images for $WSe_2$ ML on graphite contain other point-like defects that do not resemble the simulated STM images for $Se_{vac}$ [39,40]. Bias-dependent STM images for the most commonly observed point defect in the $WSe_2$ ML shows that the occupied states have a gray triangular area or a dark three-point star shape surrounded by a bright triangle [39,40]. On the other hand, the image corresponding to the unoccupied states has dark depressions but does not have the bright circle that is seen in the $Se_{vac}$ image [39,40]. We show in Reference [40] that the most commonly observed defect observed in these STM images corresponds to $Se_{vac}$ passivated by a strongly bound O atom $(O_{Se})$.

## B. Extrinsic defects

### 1. Atomic structure and Formation Energies

Extrinsic defects arising from contaminant transition metal atoms have been studied in the past for TMD ML [63,64]. Here, we focus on extrinsic point defects involving

elements that are present in a typical CVD growth process, i.e. O, H and C. O-related defects can also be formed due to exposure to O₂ in ambient conditions. We consider O, O₂, H, H₂ and C atoms interacting with perfect WSe₂ ML as well as with the more stable intrinsic point defects (Seᵥₐc, Sₑw, Wᵥₐc and 2Sₑᵥₐc). The relaxed structures of the O-, H-, and C-related point defects are shown in Figs. 6, 7 and 8, respectively, and the formation energies are given in Table II, together with the bond lengths of O₂ and H₂ where applicable. The nomenclature of defects follows the following conventions: (a) ad: adatom; (b) ins: insertion; (c) Xₛₑ/ω: X on Se/Wᵥₐc; (d) X-Y: X adsorbed on intrinsic defect Y. The formation energy is defined in two ways:

$$
E_{f 1}=E_{defect}-E_{pristine}-\sum_{i} n_{i} \mu_{i} \tag{6}
$$

where $E_{defect}$ and $E_{pristine}$ are the total energy with and without defects, respectively.

$$
E_{f 2}=E_{defect}-E_{intrinsic-defect}-\sum_{i} n_{i} \mu_{i} \tag{7}
$$

where $E_{defect}$ and $E_{intrinsic-defect}$ are the total energy of the supercell with the intrinsic defect, with and without impurity atom, respectively. In both formula, $n_{i}$ indicates the number of atoms of element $i$ and $\mu_{i}$ is the corresponding chemical potential. The chemical potentials of W and Se are those corresponding to Se-rich conditions. The chemical potentials of O, H and C are the total energy per atom of O₂, H₂ and graphite, respectively. The formation energies relative to atomic O, H and C are also indicated in brackets for selected defects, computed using the experimental gas phase bond dissociation energies of O₂ and H₂ [65] and the computed binding energy per C atom in graphite. The computed bond dissociation energy for H₂ is 4.5 eV (same as the experimental value), but that for O₂ is different (see Table III below). $E_{f1}$ depends on the chemical potential of Se and W if an intrinsic defect is involved.

$E_{f1}$ can be regarded as the formation energy of extrinsic point defects during the CVD growth, whereas $E_{f2}$ can be regarded as the formation energy of the extrinsic point defect after CVD growth, and is generally much smaller (more negative) than the corresponding value of $E_{f1}$. On the other hand, the formation energies given relative to atomic O, H or C are a better estimate for the stability of the isolated O, H or C atom related extrinsic defects after formation. This is because there is usually no atomic O, H or C nearby to recombine with the O, H or C that is released from the defect site, which would then be released as atoms initially. Zero point energies are not included in the formation energies in Table II. We computed zero point energy corrections to the formation energies for O₂-Sevac and H₂-Sevac, and found that the formation energies changed from -2.80 eV to -2.72 eV for O₂-Sevac and from -0.77 eV to -0.64 eV for H₂-Sevac. These corrections are quite small and will not change the conclusions of the manuscript. Formation energies as defined above will take on a more negative value for more stable defects, and a positive value for unstable defects. For convenience, we also use the term binding energy below, for the binding of impurity atoms to the WSe₂ lattice or intrinsic defect sites. The binding energy has the opposite sign as the formation energy (the more positive the binding energy, the stronger the impurity binds).

(a) O-related defects. The interaction of oxygen with 2D materials is an important problem because oxidation is often the cause of material degradation in these systems. For example, the dissociative chemisorption of O₂ on phosphorene leads to its decomposition [66]. On the other hand, the reversible passivation of sulphur vacancies in MoS₂ with O₂ can tune its optical properties [12]. Fig. 6 shows the relaxed atomic structures of the O-related point defects in WSe₂ ML. Except for O-Sew (O adsorbed at the Sew defect; Fig. 6h) where the Se atom at the antisite is pushed away from O, O and O₂ do not induce significant distortion of the lattice (Fig. 6). The O atom can form three bonds with W atoms at Sevac (Fig.

6a), while it forms two bonds to Se in O-Sew and Ow defects. The oxygen adatom forms one bond to the Se atom. At $O_{ins}$, O sits in a hollow site. $O_2$ dissociates into two O atoms at the $2Se_{vac}$ site (Fig. 6g), with an O-O distance of about twice the bond length in $O_2$ (Table II).

The $O_2$ bond length is only slightly lengthened when adsorbed at the Sew and $W_{vac}$ sites, but is lengthened by about 20% at the $Se_{vac}$ site (Table II). It is not energetically favorable for $O_2$ to bind to $W_{vac}$ and Sew. However, $O_2$ binds strongly to $Se_{vac}$ and $2Se_{vac}$. The strength of interaction between $O_2$ and the defect sites can be directly correlated with the amount of electron transfer from the defect site to $O_2$ (Table V). There is significant electron transfer from $Se_{vac}$ and $2Se_{vac}$ to $O_2$. The electron charge enters the antibonding orbital of $O_2$ and weakens the O=O bond, thus facilitating the dissociation of $O_2$ [40]. Similar observations have been made for $O_2$ on Au catalysts [67]. The $Se_{vac}$ is the most stable binding site for atomic O. O binds at $Se_{vac}$ to form $O_{Se}$, with a binding energy of 7.05 eV relative to atomic O. Thus, $O_{Se}$ is a very stable defect, and once formed, O is unlikely to be removed from the $Se_{vac}$ site. O can also bind stably to a $W_{vac}$ defect, forming Ow. However, since $O_2$ cannot bind to $W_{vac}$, Ow can only form if atomic O is available from some other source. The same applies to O-Sew. In perfect $WSe_2$, the most stable binding site for O corresponds to $O_{ins}$, followed by $O_{ad}$.

It is noted that DFT with standard exchange-correlation functionals, such as PBE-D2 used here, may not be able to predict quantitatively the absolute adsorption energies of O and $O_2$, because the predicted value of the bond dissociation energy of gas phase $O_2$ deviates significantly from the experimental value (Table III). However, we are more interested in qualitative results such as the relative adsorption energies, and it has been shown that both PBE and RPBE [68] functionals give qualitatively similar results for the sticking curves of $O_2$ on Al(111), even though the $O_2$ bond dissociation energy computed with RPBE is one of the closest to experiment among the gradient corrected functionals [69]. To obtain an idea of the

magnitude of the error in absolute adsorption energies, we show in Table III the binding energies of $O_2$ to $S_{evac}$ using different exchange-correlation functionals (PBE-D2, RPBE , RPBE with Grimme's D3 correction [70], and BEEF-vdW [71]). RPBE has been used successfully to describe the activation of $O_2$ on metal surfaces [69,72], RPBE-D3 reproduces the properties of liquid water [73], while BEEF-vdW was developed for surface science and catalysis studies. BE1, the binding energy relative to the energy of $O_2$, is 2.80 eV using PBE-D2, and ~1.9-2.2 eV using the other functionals. Thus, in comparison, PBE-D2 overbinds the $O_2$ molecule at the $S_{evac}$ defect site by about 0.6-0.9 eV. If we assume conservatively that $O_2$ overbinds by 0.9 eV and O overbinds by 0.45 eV relative to the energy per atom in $O_2$, we see that all the formation energies for O-related defects in Table II are still very negative (stable), except for O-Sew which was marginally stable (with a formation energy of -0.01 eV). It is also instructive to obtain the binding energy relative to atomic O, as this is important for the O atom related defects. We also compute the binding energy, BE2, of $O_2$ on $S_{evac}$, relative to the energy of two O atoms. However, as noted above, the bond dissociation energy of $O_2$ is overestimated with the functionals, when compared to experiment. If instead the $O_2$ bond dissociation energy from experiment is used to compute the binding energy of $O_2$ to $S_{evac}$, relative to the energies of two O atoms (BE3), we find that BE3 corresponding to PBE-D2 is larger than BE3 from other functionals, but is close to the values of BE2 obtained by RPBE and RPBE-D3 (Table III). In Table II, we have used the $O_2$ bond dissociation energy from experiment [65] to compute the formation energies relative to atomic O.

(b) *H-related defects.* Hydrogen is a commonly found impurity in many materials, with hydrogen embrittlement [74] being a serious problem in metals, such as aluminium and titanium. Hydrogen has been used to create n-doped contacts in TMDs ($MoS_2$), by using hydrogen silsesquioxane (HSQ) as a photoresist coupled with low electron beam dosages to destroy the Si-H bonds in HSQ and release H atoms into the TMD [47,75]. $H_2$ gas is also

used as a reducing agent to obtain better quality TMD films during CVD growth [34]. Table II shows that generally, the binding energies of H and H₂ in WSe₂ ML and its intrinsic defect sites are much smaller than those of O and O₂. Using the atomic energy in H₂ as a chemical potential, the formation energies $E_{f1}$ of all H-related defects considered here are positive, indicating that H-related defects are unlikely to form in WSe₂ during the natural CVD growth process involving H₂. If H atoms are available for reaction with perfect WSe₂ (e.g. from HSQ), the most stable defect structure is $H_{ins}$, where H is inserted into the hollow site (Table II; Fig. 7b). Similar to O-related defects, the hollow site is preferred to the Se atop site (in $O_{ad}$ and $H_{ad}$). However, the binding energy for H at $H_{ins}$ is only 0.88 eV (relative to atomic H). Thus, these H atoms can be removed by annealing. $H_{ins}$ is an effective donor in WSe₂ ML (Table IV below), consistent with the effectiveness of H for creating n-doped contacts in TMDs. The small binding energy for H implies that the TMD should be covered with a contact or protective layer to prevent the H dopants from being removed with annealing.

H and H₂ bind favorably to several of the intrinsic defect sites. H atoms bind to $Se_{vac}$, $W_{vac}$ and $Sew$. The formation energy for H-Sew is the smallest (-0.43 eV relative to atomic energy in H₂), followed by Hw and $H_{Se}$ (-0.27 eV relative to atomic energy in H₂). Interestingly, there is more lattice distortion in Hw and H-Sew than in $H_{Se}$ (Fig. 7i, h, a). Yet, the formation energy for $H_{Se}$ is the largest (least stable). On the other hand, H₂ binds to $Se_{vac}$ with a formation energy of -0.77 eV. This implies that for the defect concentrations considered here, it is thermodynamically more favorable (by 0.23 eV) for H₂ to bind to a single $Se_{vac}$ site, leaving another $Se_{vac}$ empty, than it is for one H atom to bind to each $Se_{vac}$ site, forming two copies of $H_{Se}$. Examining the structure for $H_{2}$-$Se_{vac}$ (Fig. 7d), it can be seen that H₂ dissociates without any energy barrier at $Se_{vac}$ to form two H atoms which both bind at the $Se_{vac}$ site. One of the H atoms forms a single bond with a neighboring W atom, while the other forms two bonds with the other two nearest neighbor W atoms. H₂ has also

dissociated in H₂-2Sevac (Fig. 7g), but the binding energy there is much smaller (0.39 eV).

This is unlike O₂, which binds much more strongly to 2Sevac than to Sevac. The local bonding configuration of each O (H) atom in O(H)₂-2Sevac is similar to that of O(H)se. Thus, the difference in relative binding energies between O₂ and H₂ at 2Sevac is consistent with the strong binding of O in Oₛₑ and weak binding of H in Hₛₑ. The weak binding of H in Hₛₑ may in turn be related to the long H-W bond lengths in Hₛₑ, compared to those in H₂-Sevac (H, with a very small atomic radius, favors short bonds). Similar to O₂, H₂ does not bind to Wvac. In contrast to O₂, it is energetically favorable for H₂ to bind at Sew, with a formation energy of -0.67 eV. The adsorption of H₂ at Sew is accompanied by a significant distortion in the lattice, with one of the Se-Se bonds being broken (Fig. 7e). Likewise, a Se-Se bond is broken when H binds to Sew (its most stable binding site), where H is inserted into a Se-Se bond (Fig. 7h).

(c) *C-related defects.* None of the C-related defects studied here is thermodynamically stable when the chemical potential for C is the energy per atom in graphite. Thus, it may be less likely to form these C-related defects. However, once the defects are created, they are stable in the absence of reactants with C (Table II, formation energies using the chemical potential of atomic C). The most favorable binding site for C atoms is Sevac (Table II; Fig. 8a). In perfect WSe₂ ML, the C atom prefers the interstitial site to the Se adatom site (just like H and O). The introduction of C leads to significant lattice distortions in Cw (C at a Wvac site) and C-Sew (Fig. 8e-f). Otherwise, no significant lattice distortion is seen in Cₛₑ, Cᵢₙₛ, Cₐd and 2C-2Sevac (Fig. 8a-d).

### 2. Electronic structure

The spin-polarized densities of states (DOS) for O, H and C-related defects in WSe₂ ML are shown in Figs. 9, 10 and 11, respectively. Of all the different species interacting with

intrinsic defects in WSe2 ML, we find that only O and O₂ interacting with Sᵥₐc and 2Sᵥₐc fully passivate the gap states of the intrinsic defects (Sᵥₐc and 2Sᵥₐc in this case) (Fig. 9 a, d, g). In the literature [12], it has been shown that O₂ passivates the gap states of Sᵥₐc in MoS₂ ML, so that the photoluminescence of MoS₂ ML can be tuned by exposure to O₂ and subsequent annealing, which removes the O₂ from Sᵥₐc. We show in reference [40] that O₂ can dissociate at room temperature at Sᵥₐc sites in WSe₂ ML, giving Oₛₑ. This is not possible for Sᵥₐc sites in MoS₂ ML [40]. The binding energy of atomic O to Sᵥₐc (7.05 eV) is much larger than that of O₂ to Sᵥₐc (computed to be 2.02 eV with PBE-D2, with a possible overestimate of ~0.6-0.9 eV according to the analysis in Table III). Thus, O at Sᵥₐc is very stable and will not be removed by annealing, in contrast to O₂ at Sᵥₐc sites [12].

For H, H₂ and C interacting with Sᵥₐc and 2Sᵥₐc, the gap states are modified rather than removed (Fig. 10a, f; Fig. 11a). This is consistent with the much stronger interaction between O and O₂ with Sᵥₐc and 2Sᵥₐc, compared to H, H₂ or C. On the other hand, despite the reasonably strong interaction between O and Wᵥₐc, O_w still has gap states (Fig. 9i). The gap states in Wᵥₐc and S_ew are modified by interaction with O, O₂, H, H₂ and C. The difficulty in removing gap states for Wᵥₐc and S_ew may be related to the fact that there are multiple discrete levels in the band gap for these intrinsic defects (Fig. 3e, f). In perfect WSe₂ ML, O, H and C all prefer to bind in the interstitial site. The resulting defect geometries (Oᵢₙₛ, Hᵢₙₛ and Cᵢₙₛ) have no gap states (Fig. 9b, 10b, 11b). O in the adatom site (Oₐd) also has no gap states, but Hₐd and Cₐd both have spin polarized gap states.

Figures 9 to 11 show that the following extrinsic point defects are spin-polarized: O₂-S_ew (Fig. 9e), O₂-Wᵥₐc (Fig. 9f), Hₛₑ (Fig. 10a), Hₐd (Fig. 10c), H-S_ew (Fig. 10d), H_w (Fig. 10e), and Cₐd (Fig. 11c). O₂-S_ew and O₂-Wᵥₐc are not stable, while Hₐd has a very small binding energy of 0.05 eV (Table II). Thus, we focus on Hₛₑ, H_w and H-S_ew. These three defects all have multiple spin-polarized defect states in the band gap, and may be interesting

from the point of view of defect engineering for spin-related applications. Fig. 12 shows the isosurface contour plots of the difference between the spin up and spin down charge densities for these defects. All these defects have regions of net spin up charge densities that extends at least one lattice spacing around the defect site, while $H_W$ and $H_{Se}$ also have net spin down charge densities localized near the H atoms. Earlier, we had shown that it is more energetically favorable for two H atoms to bind to a single $Se_{vac}$ site, leaving one $Se_{vac}$ empty, than it is for the H atoms to bind to each $Se_{vac}$ site, separately. Thus, $H_{Se}$ is not likely to form. Besides, the $Se_{vac}$ sites should instead be passivated by strongly bound O, once exposed to ambient conditions [40]. On the other hand, $Se_W$ has been observed in STEM experiments [40]. $Se_W$ does not bind $O_2$, but is the preferred binding site for H (Table II). Thus, H-$Se_W$ is a promising candidate for spin-polarized point defects, and may be engineered by exposing WSe₂ ML to atomic H [47].

### C. Charge transition levels and ionization energies

The creation of charge carriers in semiconductors is essential for their use in electronic applications. Unlike MoS₂ which is typically n-type, WSe₂ ML has p-type or ambipolar transport characterisitics [33-36]. The nature and origin of these charge carriers are fundamental questions in semiconductor physics. Typically, the charge carriers are made available by ionization of defects within the semiconductor [76]. The large surface-to-volume ratio in 2D materials also makes the effects of the substrate and adsorbates particularly important. For example, surface charge transfer effects [77] induced by adsorbing donor or acceptor organic molecules on TMDs can induce doping in the TMD. The nature of the charge carriers is also directly related to the Schottky barrier heights when the electrode comes into contact with the 2D material. Many factors influence the Schottky barrier heights. These include vacuum work function alignment, and Fermi level pinning by metal-induced gap states [78,79], or by defect states [32]. Dielectric screening from the substrate has been

found to change the exciton binding energy in MoS₂ ML [80]. Likewise, it should be expected that the same substrate screening effect can change the ionization energies of the defects in 2D materials.

Experimentally, it is very challenging to relate measured charge state transition levels to specific defect structures [76]. First principles calculations therefore have a major role to play in studying defect physics, in particular the possibility of inducing doping by ionizing point defects. In bulk materials, the extent of doping caused by point defects is typically analyzed by computing the charge state transition levels and ionization energies (IE), both of which have been defined in Section II. Fig. 13a also presents a schematic explaining these quantities. While the nature and origin of charge carriers in 2D materials are influenced by many factors, we first examine the possibility of ionization of the point defects in WSe₂ ML, similar to the way defect-induced doping is studied in the bulk. Previous studies have shown that substrate screening effects on the charge transition levels are quite small in supported MoS₂ ML [81]. Thus, to reduce computational complexity, we have computed the charge transition levels in isolated WSe₂ ML. The effect of the substrate is then to provide the position of the Fermi level, which can be used to infer the stable charge state of each defect (Fig. 13).

Since the IE are obtained by computing the transition level energies with respect to the band edges, the fact that PBE underestimates the band gap would lead to quantitatively inaccurate IE. Hybrid exchange correlation functionals, such as HSE06 [7], or many-electron GW calculations [82], have in the past been used to obtain more quantitatively accurate charge transition levels. Here, we are more interested in the qualitative features of the IE of various defects. For point defects in MoS₂, it has been found that PBE with Grimme's corrections, and HSE06 functionals give qualitatively similar results for the charge transition levels [7]. Thus, we proceed to use PBE-D2 for our calculations. As discussed in Section II,

the IE is a quantity that depends on the supercell size, and we have used two different methods to approximate the converged IE in WSe₂ ML. In Method 1, we use the asymptotic formula for the IE (equation 5) and obtain the converged IE from the intercepts of linear fits to the data, as shown in Fig. 14 for Seᵥₐc. The IEs thus computed are used to choose a suitable "special" supercell size for WSe₂ ML, to obtain the IE using Method 2 for a larger number of defects. The results are shown in Table IV. Here, we focus on the most stable intrinsic defects (Seᵥₐc, Wᵥₐc and Sew), as well as the most stable O- and H-related defects.

### 1. Intrinsic defects

The IE for Seᵥₐc are > 1 eV. For Wᵥₐc and Sew, the donor IE are ~1.5-1.6 eV while the acceptor IE are ~0.8-0.9 eV. These are all deep donors and acceptors and these defects would all be charge neutral in isolated WSe₂ ML. For WSe₂ ML on graphite, scanning tunneling spectroscopy experiments show that the Fermi level is close to mid-gap, ~1.0 eV from the VBM [58]. Depending on the self-energy corrections for the energy levels, and the alignment of the Fermi level with respect to the VBM for different substrates, it is possible that Wᵥₐc and Sew can act as acceptors in supported WSe₂ ML. (Note that this assumes that the transition levels are not affected by the substrate.)

### 2. O-related defects

The O-related defects considered here all have large donor and acceptor IE (> 1.5 eV). However, O is well-known to be a very electronegative atom which should behave as an acceptor. Indeed, a Bader charge analysis [83] for the charge neutral states shows that O atoms take 0.9-1.0 electrons from WSe₂ ML in Oₐd, Oᵢₙₛ and Oₛₑ, while O in Ow and O-Sew take 0.8 electrons (Table V). In Oₛₑ and Ow, the O atom substitutes a Se and W atom, respectively. While O takes 0.98 electrons from its surrounding atoms in Oₛₑ, Se would also normally take 0.445 electrons (coming from W). Thus, compared to Se, O in Oₛₑ takes an

additional 0.54 electrons, as indicated in brackets in Table V. On the other hand, O at W<sub>vac</sub> takes an additional 1.73 electrons compared to W (which normally gives electrons). The O₂ molecule has dissociated at 2Se<sub>vac</sub>, so the results for O₂-2Se<sub>vac</sub> are similar to those for O<sub>Se</sub>. O₂ also takes an average of 0.57 electrons per atom from Se<sub>vac</sub>. On the other hand, O₂ takes an average of 0.26 and 0.15 electrons, respectively, when adsorbed on W<sub>vac</sub> and Se<sub>W</sub>, significantly less than at other binding sites (Table V). This smaller extent of charge transfer correlates with the fact that O₂ does not bind favorably to W<sub>vac</sub> and Se<sub>W</sub> (Table II), thus suggesting that electron transfer to O₂ is important for stabilizing the interaction between O₂ and the defect sites. Taken together, the Bader charge analysis for O-related defects shows that O atoms in various stable defect geometries do take a considerable amount of electron charge from WSe₂. The large acceptor IE computed for these defects may arise from the fact that it is energetically unfavorable to add more electron charge to these O-related defects, which already have some negative charge in the neutral state.

The transfer of electrons to O in the neutral state brings to mind the surface charge transfer doping methods in 2D materials, where donor/acceptor molecules are adsorbed on 2D materials to dope them [77]. However, the concentration of the O-related defects is generally much lower than the density of deposited donor/acceptor molecules. It is not clear if the O atom takes electrons only from its nearest neighbors, leading to local charge rearrangements, or if the O atom also takes electrons from atoms far away; the latter would be required to induce doping in the 2D material. To gain insight into this question, we compute the charge difference Δρ, between the amount of Bader charge on a WSe₂ unit in a supercell with the defect, and that in perfect WSe₂ (equal to 18 valence electrons). The Bader charge on the WSe₂ unit is defined as the sum of the charge on W and half of the charges on all six nearest neighboring Se atoms. The quantity Δρ is plotted as a function of the distance r of the WSe₂ unit from the defect site, starting from r = 2.6 Å (Fig. 15). Where Δρ is negative,

the electron charge in the WSe₂ unit there is smaller than that in perfect WSe₂, and vice versa.

This analysis is done for the three most likely O-related defects, Oₛₑ, Oᵢₙₛ and Oₐd (Ow and O-Sew have very low densities due to the scarcity of Wᵥₐc and Sew defects). Fig. 15a shows that the charge rearrangement at Oₛₑ is very localized. Beyond r = 2.6 Å, we do not see much electron charge being depleted from the WSe₂ units, and a random distribution of Δρ around 0.0 is obtained. This may be related to the fact that O is at a substitutional site, and O in Oₛₑ takes an additional 0.54 electrons only when compared to Se. Oᵢₙₛ and Oₐd seem to be more effective acceptors, with Δρ remaining generally negative for larger r values (Fig. 15b-c).

When the graphite substrate is included for Oᵢₙₛ and Oₐd, Δρ starts to take random values around 0.0 for r larger than 4.4 and 4.0 Å, respectively (not shown), although the average amount of charge lost per WSe₂ unit remains approximately the same with or without the graphite substrate. Thus, it is not clear whether Oᵢₙₛ and Oₐd will be effective acceptors in the presence of the graphite substrate. We note here that graphite does not donate charge to O in these structures. This is in contrast to C₆₀F₄₈ deposited on WSe₂ ML supported on graphite, where it was predicted that graphite contributed a significant amount of charge to C₆₀F₄₈ [84]. The differing amounts of charge transfer from graphite may be related to the fact that C₆₀F₄₈ is a much stronger acceptor than O.

### 3. H-related defects

Of all the defects studied here, Hᵢₙₛ stands out as having the smallest ionization energy (0.29 eV for the donor IE). This indicates that Hᵢₙₛ is an effective donor in WSe₂ ML. As discussed above, the interstitial site in Hᵢₙₛ is also the most stable binding site for H in perfect WSe₂ ML, although the binding energy for the H atom is quite small. This finding indicates that H atoms can be introduced into the WSe₂ lattice to induce n-doping, but these H atoms may be removed with annealing unless special precautions are taken. Hw has an acceptor IE

of 0.71 eV, slightly lower than that of $W_{vac}$ (0.78 eV). All the other IEs for H-related defects are > 0.9 eV.

## IV. CONCLUSION

In conclusion, we have presented a detailed DFT study of the intrinsic defects in WSe₂ ML, supported on graphite, as well as O, H and C-related defects in WSe₂ ML. We have considered the interaction of O, O₂, H, H₂ and C with perfect WSe₂ ML as well as with its intrinsic defects. The presence of the graphite substrate does not change the formation energies of the intrinsic defects significantly. When O, O₂, H, H₂ and C interact with the intrinsic defects, the gap states of the intrinsic defects are modified. In the particular case of O and O₂ interacting with Se vacancies and divacancies, the gap states are completely removed. We show that Se vacancies have the lowest formation energy among the intrinsic defects in ML WSe₂, and that among all the extrinsic defects studied here, O-related defects (O₂ substituting 2Se atoms, O substituting Se and O interstitials in WSe₂) are the most stable ones. In reference [40], we further study the optical properties of the most stable defects and comment on the origin of single photon emission from WSe₂. H-related impurities are interesting because of the possibility of engineering spin-polarized point defects, such as H bonded to Sew antisite defects. H also behaves as a donor in its most stable adsorption site in perfect WSe₂. All other defects considered here are deep acceptors or donors in isolated WSe₂ ML. O defects in their neutral state take electron charge from WSe₂, but the charge rearrangement may be too localized for them to be effective acceptors at low densities.

Acknowledgements: SYQ acknowledges support from the Singapore NRF, Prime Minister's Office, under its medium-sized centre program, and from grant NRF-NRFF2013-07. Computations were performed on the CA2DM cluster and the National Supercomputing Centre (NSCC) in Singapore.

### References

[1] K. S. Novoselov, D. Jiang, F. Schedin, T. J. Booth, V. V. Khotkevich, S. V. Morozov, and A. K. Geim, Proceedings of the National Academy of Sciences of the United States of America **102**, 10451 (2005).

[2] Q. H. Wang, K. Kalantar-Zadeh, A. Kis, J. N. Coleman, and M. S. Strano, Nat. Nanotechnol. **7**, 699 (2012).

[3] C. Tan *et al.*, Chemical reviews **117**, 6225 (2017).

[4] S. Z. Butler *et al.*, ACS Nano **7**, 2898 (2013).

[5] D. Akinwande, N. Petrone, and J. Hone, Nat. Commun. **5**, 12, 5678 (2014).

[6] J. Y. Noh, H. Kim, and Y. S. Kim, Phys. Rev. B **89**, 12, 205417 (2014).

[7] H. P. Komsa and A. V. Krasheninnikov, Phys. Rev. B **91**, 17, 125304 (2015).

[8] S. Haldar, H. Vovusha, M. K. Yadav, O. Eriksson, and B. Sanyal, Phys. Rev. B **92**, 12, 235408 (2015).

[9] Y. C. Lin, D. O. Dumcenco, H. P. Komsa, Y. Niimi, A. V. Krasheninnikov, Y. S. Huang, and K. Suenaga, Adv. Mater. **26**, 2857 (2014).

[10] S. McDonnell, R. Addou, C. Buie, R. M. Wallace, and C. L. Hinkle, ACS Nano **8**, 2880 (2014).

[11] S. Tongay *et al.*, Sci. Rep. **3**, 5, 2657 (2013).

[12] P. K. Gogoi *et al.*, Phys. Rev. Lett. **119**, 077402 (2017).

[13] Y. M. He *et al.*, Nat. Nanotechnol. **10**, 497 (2015).

[14] A. Srivastava, M. Sidler, A. V. Allain, D. S. Lembke, A. Kis, and A. Imamoglu, Nat. Nanotechnol. **10**, 491 (2015).

[15] C. Chakraborty, L. Kinnischtzke, K. M. Goodfellow, R. Beams, and A. N. Vamivakas, Nat. Nanotechnol. **10**, 507 (2015).

[16] M. Koperski, K. Nogajewski, A. Arora, V. Cherkez, P. Mallet, J. Y. Veuillen, J. Marcus, P. Kossacki, and M. Potemski, Nat. Nanotechnol. **10**, 503 (2015).

[17] P. Tonndorf *et al.*, Optica **2**, 347 (2015).

[18] T. T. Tran, K. Bray, M. J. Ford, M. Toth, and I. Aharonovich, Nat. Nanotechnol. **11**, 37 (2016).

[19] T. T. Tran *et al.*, ACS Nano **10**, 7331 (2016).

[20] R. Bourrellier, S. Meuret, A. Tararan, O. Stephan, M. Kociak, L. H. G. Tizei, and A. Zobelli, Nano Lett. **16**, 4317 (2016).

[21] Z. Y. Yin *et al.*, ACS Nano **6**, 74 (2012).

[22] G. H. Lee *et al.*, ACS Nano **7**, 7931 (2013).

[23] O. Lopez-Sanchez, D. Lembke, M. Kayci, A. Radenovic, and A. Kis, Nat. Nanotechnol. **8**, 497 (2013).

[24] W. S. Leong, X. Luo, Y. D. Li, K. H. Khoo, S. Y. Quek, and J. T. L. Thong, ACS Nano **9**, 869 (2015).

[25] J. H. Hong *et al.*, Nat. Commun. **6**, 8, 6293 (2015).

[26] P. Vancso, G. Z. Magda, J. Peto, J. Y. Noh, Y. S. Kim, C. Hwang, L. P. Biro, and L. Tapaszto, Sci. Rep. **6**, 7, 29726 (2016).

[27] W. Zhou *et al.*, Nano Lett. **13**, 2615 (2013).

[28] Z. Yu *et al.*, Nat Commun **5**, 5290 (2014).

[29] X. Liu, I. Balla, H. Bergeron, and M. C. Hersam, J. Phys. Chem. C **120**, 20798 (2016).

[30] H. Qiu *et al.*, Nat. Commun. **4**, 6, 2642 (2013).

[31] W. S. Leong, Y. Li, X. Luo, C. T. Nai, S. Y. Quek, and J. T. L. Thong, Nanoscale **7**, 10823 (2015).

[32] S. H. Song, M.-K. Joo, M. Neumann, H. Kim, and Y. H. Lee, Nat. Commun. **8**, 2121 (2017).

[33] S. Das and J. Appenzeller, Appl. Phys. Lett. **103**, 103501 (2013).

[34] J. K. Huang *et al.*, ACS Nano **8**, 923 (2014).

[35] H. Schmidt, F. Giustiniano, and G. Eda, Chem. Soc. Rev. **44**, 7715 (2015).

[36] B. L. Liu, M. Fathi, L. Chen, A. Abbas, Y. Q. Ma, and C. W. Zhou, ACS Nano **9**, 6119 (2015).

[37] J. S. Ross *et al.*, Nat. Nanotechnol. **9**, 268 (2014).


[38] A. Hogele, C. Galland, M. Winger, and A. Imamoglu, Phys. Rev. Lett. **100**, 217401 (2008).

[39] S. Zhang, C.-G. Wang, M.-Y. Li, D. Huang, L.-J. Li, W. Ji, and S. Wu, Phys. Rev. Lett. **119**, 046101 (2017).

[40] Y. J. Zheng *et al.*, arXiv:1811.00221 (2018).

[41] Y. C. Lin, D. O. Dumcenco, H. P. Komsa, Y. Niimi, A. V. Krasheninnikov, Y. S. Huang, and K. Suenaga, Adv. Mater. **26**, 2857 (2014).

[42] Y. C. Lin, S. S. Li, H. P. Komsa, L. J. Chang, A. V. Krasheninnikov, G. K. Eda, and K. Suenaga, Advanced Functional Materials **28**, 1704210 (2018).

[43] Y. Gao *et al.*, Adv. Mater. **29**, 1700990 (2017).

[44] J. X. Liu *et al.*, Small **12**, 5741 (2016).

[45] S. M. Eichfeld, V. O. Colon, Y. F. Nie, K. Cho, and J. A. Robinson, 2D Mater. **3**, 025015 (2016).

[46] S. M. Eichfeld *et al.*, ACS Nano **9**, 2080 (2015).

[47] M. M. Perera, M. W. Lin, H. J. Chuang, B. P. Chamlagain, C. Y. Wang, X. B. Tan, M. M. C. Cheng, D. Tomanek, and Z. X. Zhou, ACS Nano **7**, 4449 (2013).

[48] P. E. Blochl, Phys. Rev. B **50**, 17953 (1994).

[49] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

[50] G. Kresse and J. Furthmüller, Phys. Rev. B **54**, 11169 (1996).

[51] G. Kresse and J. Furthmüller, Comput. Mater. Sci. **6**, 15 (1996).

[52] S. Grimme, Journal of Computational Chemistry **27**, 1787 (2006).

[53] W. J. Schutte, J. L. Deboer, and F. Jellinek, Journal of Solid State Chemistry **70**, 207 (1987).

[54] H. W. King, CRC Handbook of Chemistry and Physics **83**, 19 (2002).

[55] D. Wang, D. Han, X. B. Li, S. Y. Xie, N. K. Chen, W. Q. Tian, D. West, H. B. Sun, and S. B. Zhang, Phys. Rev. Lett. **114**, 5, 196801 (2015).

[56] C. G. Van de Walle and J. Neugebauer, J. Appl. Phys. **95**, 3851 (2004).

[57] H. P. Komsa, N. Berseneva, A. V. Krasheninnikov, and R. M. Nieminen, Phys. Rev. X **4**, 7, 031044 (2014).

[58] Y. L. Huang *et al.*, Nano Lett. **16**, 3682 (2016).

[59] J. Chen *et al.*, Adv. Mater. **27**, 6722 (2015).

[60] J. Tersoff and D. R. Hamann, Phys. Rev. B **31**, 805 (1985).

[61] C. González, B. Biel, and Y. Dappe, Nanotechnology **27**, 105702 (2016).

[62] A. Altibelli, C. Joachim, and P. Sautet, Surf. Sci. **367**, 209 (1996).

[63] P. M. Coelho, H.-P. Komsa, H. Coy Diaz, Y. Ma, A. V. Krasheninnikov, and M. Batzill, ACS Nano **12**, 3975 (2018).

[64] Y. C. Lin, S. S. Li, H. P. Komsa, L. J. Chang, A. V. Krasheninnikov, G. Eda, and K. Suenaga, Adv. Funct. Mater. **28**, 1704210 (2018).

[65] S. W. Benson, Journal of Chemical Education **42**, 502 (1965).

[66] Y. Huang *et al.*, Chem. Mat. **28**, 8330 (2016).

[67] G. Mills, M. S. Gordon, and H. Metiu, J. Chem. Phys. **118**, 4198 (2003).

[68] B. Hammer, L. B. Hansen, and J. K. Norskov, Phys. Rev. B **59**, 7413 (1999).

[69] J. Behler, B. Delley, S. Lorenz, K. Reuter, and M. Scheffler, Phys. Rev. Lett. **94**, 036104 (2005).

[70] S. Grimme, J. Antony, S. Ehrlich, and H. Krieg, J. Chem. Phys. **132**, 154104 (2010).

[71] J. Wellendorff, K. T. Lundgaard, A. Mogelhoj, V. Petzold, D. D. Landis, J. K. Norskov, T. Bligaard, and K. W. Jacobsen, Phys. Rev. B **85**, 235149 (2012).

[72] M. Ramos, C. Diaz, A. E. Martinez, H. F. Busnengo, and F. Martin, Phys. Chem. Chem. Phys. **19**, 10217 (2017).

[73] K. Forster-Tonigold and A. Gross, J. Chem. Phys. **141**, 064501 (2014).

[74] P. Sofronis and I. M. Robertson, in *Hydrogen in Matter*, edited by G. R. Myneni, and B. Hjorvarsson2006), p. 64.

[75] Z. Hu, Z. Wu, C. Han, J. He, Z. Ni, and W. Chen, Chem. Soc. Rev., 10.1039/C8CS00024G (2018).

[76] C. Freysoldt, B. Grabowski, T. Hickel, J. Neugebauer, G. Kresse, A. Janotti, and C. G. Van de Walle, Reviews of Modern Physics **86** (2014).

[77] Y. L. Huang, Y. J. Zheng, Z. Song, D. Chi, A. T. S. Wee, and S. Y. Quek, Chem. Soc. Rev., 10.1039/C8CS00159F (2018).

[78] C. Gong, L. Colombo, R. M. Wallace, and K. Cho, Nano Lett. **14**, 1714 (2014).

[79] C. Kim *et al.*, ACS Nano **11**, 1588 (2017).

[80] M. M. Ugeda *et al.*, Nat. Mater. **13**, 1091 (2014).

[81] M. H. Naik and M. Jain, arXiv:1710.09569 (2018).

[82] A. Malashevich, M. Jain, and S. G. Louie, Phys. Rev. B **89**, 075205 (2014).

[83] R. F. W. Bader, Accounts Chem. Res. **18**, 9 (1985).

[84] Z. B. Song *et al.*, ACS Nano **11**, 9128 (2017).

![](./images/867762514702631331_1.jpg)

FIG. 1. Side view of the intrinsic point defects in WSe₂ ML on graphite. Blue: W, Green: Se, Gray: C. See main text for description of defects.

![](./images/867762514702631331_2.jpg)

FIG 2. Formation energies of intrinsic defects (a) with and (b) without graphite substrate.

Solid lines denote vacancies, dashed lines substitutional (antisite) defects, dotted lines
adatoms, and dotted-dashed lines intercalated atoms.

<table>
  <thead>
    <tr>
      <th>Defect</th>
      <th colspan="2">W-rich conditions</th>
      <th colspan="2">Se-rich conditions</th>
    </tr>
    <tr>
      <th></th>
      <th>Isolated</th>
      <th>Supported</th>
      <th>Isolated</th>
      <th>Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Se<sub>vac</sub></td>
      <td>2.31</td>
      <td>2.20</td>
      <td>2.92</td>
      <td>2.82</td>
    </tr>
    <tr>
      <td>W<sub>vac</sub></td>
      <td>5.01</td>
      <td>5.09</td>
      <td>3.78</td>
      <td>3.87</td>
    </tr>
    <tr>
      <td>Se<sub>W</sub></td>
      <td>5.34</td>
      <td>5.51</td>
      <td>3.49</td>
      <td>3.66</td>
    </tr>
    <tr>
      <td>2Se<sub>vac</sub></td>
      <td>3.86</td>
      <td>3.78</td>
      <td>5.09</td>
      <td>5.01</td>
    </tr>
  </tbody>
</table>

Table I. Formation energies in eV of selected intrinsic defects in isolated WSe₂ ML and in
WSe₂ ML supported on graphite.

![](./images/867762514702631331_3.jpg)

FIG. 3. PDOS on the intrinsic defect sites in WSe₂ ML on graphite. Gray shading: PDOS of perfect WSe₂ on graphite. The PDOS with and without defects are aligned by the 1s core level of W furthest from the defect site. The Fermi level refers to the Fermi level of WSe₂ ML with defects on graphite.

![](./images/867762514702631331_4.jpg)

FIG. 4: Perfect WSe₂ ML on graphite. a) Atomic structure (Blue: W; Green: Se; Gray: C) b) PDOS on WSe₂ c) Simulated STM images at different sample bias voltages with atoms overlain in the images.

![](./images/867762514702631331_5.jpg)

FIG. 5. Simulated STM images of the intrinsic defects in WSe₂ ML on graphite. The energy ranges are chosen to probe occupied and unoccupied states that are 0.3 eV away from the band edges. Atomic positions are overlain on the images. Blue: W, Green: Se.

Table II. Formation energies in eV of extrinsic point defects related to O, O₂, H, H₂ and C. The formation energies $E_{f1}$ and $E_{f2}$ are defined in the main text. Numbers highlighted in bold are

the formation energies that are much more negative (more stable) than other extrinsic defects listed here. The chemical potentials of O, H and C are total energy per atom of O₂, H₂ and graphite, respectively. For numbers in brackets, the chemical potentials of O, H and C are the total energies of gas phase O, H and C atoms, respectively. The O-O or H-H distances are given. For comparison, the bond lengths of gas phase O₂ and H₂ are 1.23Å and 0.74Å, respectively. Spin polarization: defects in red, italic font have spin-polarized DOS, while all others have no spin polarization.

<table>
  <tbody>
    <tr>
      <td></td>
      <td>O<sub>ad</sub></td>
      <td>O<sub>ins</sub></td>
      <td>O<sub>Se</sub></td>
      <td>O<sub>W</sub></td>
      <td>O-Se<sub>W</sub></td>
      <td>O₂-Se<sub>vac</sub></td>
      <td><i>O₂-W<sub>vac</sub></i></td>
      <td><i>O₂-Se<sub>W</sub></i></td>
      <td>O₂-2Se<sub>vac</sub></td>
    </tr>
    <tr>
      <td>E<sub>f1</sub></td>
      <td>0.22<br>(-2.36)</td>
      <td>-0.31<br>(-2.89)</td>
      <td>-1.56</td>
      <td>2.56</td>
      <td>3.48</td>
      <td>0.13</td>
      <td>4.13</td>
      <td>4.61</td>
      <td>-3.47</td>
    </tr>
    <tr>
      <td>E<sub>f2</sub></td>
      <td>-</td>
      <td>-</td>
      <td>-4.47<br>(-7.05)</td>
      <td>-1.22<br>(-3.80)</td>
      <td>-0.01<br>(-2.59)</td>
      <td>-2.80</td>
      <td>0.34</td>
      <td>1.12</td>
      <td>-8.56</td>
    </tr>
    <tr>
      <td>O-O(Å)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>1.481</td>
      <td>1.276</td>
      <td>1.267</td>
      <td>2.372</td>
    </tr>
    <tr>
      <td></td>
      <td><i>H<sub>ad</sub></i></td>
      <td>H<sub>ins</sub></td>
      <td><i>H<sub>Se</sub></i></td>
      <td><i>H<sub>W</sub></i></td>
      <td><i>H-Se<sub>W</sub></i></td>
      <td>H₂-Se<sub>vac</sub></td>
      <td><i>H₂-W<sub>vac</sub></i></td>
      <td><i>H₂-Se<sub>W</sub></i></td>
      <td>H₂-2Se<sub>vac</sub></td>
    </tr>
    <tr>
      <td>E<sub>f1</sub></td>
      <td>2.21<br>(-0.05)</td>
      <td>1.38<br>(-0.88)</td>
      <td>2.65</td>
      <td>3.49</td>
      <td>3.06</td>
      <td>2.15</td>
      <td>4.17</td>
      <td>2.82</td>
      <td>4.70</td>
    </tr>
    <tr>
      <td>E<sub>f2</sub></td>
      <td>-</td>
      <td>-</td>
      <td>-0.27<br>(-2.53)</td>
      <td>-0.29<br>(-2.55)</td>
      <td>-0.43<br>(-2.69)</td>
      <td>-0.77</td>
      <td>0.39</td>
      <td>-0.67</td>
      <td>-0.39</td>
    </tr>
    <tr>
      <td>H-H(Å)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>1.828</td>
      <td>0.971</td>
      <td>0.752</td>
      <td>2.027</td>
    </tr>
    <tr>
      <td></td>
      <td><i>C<sub>ad</sub></i></td>
      <td>C<sub>ins</sub></td>
      <td>C<sub>Se</sub></td>
      <td>C<sub>W</sub></td>
      <td>C-Se<sub>W</sub></td>
      <td></td>
      <td></td>
      <td></td>
      <td>C₂-2Se<sub>vac</sub></td>
    </tr>
    <tr>
      <td>E<sub>f1</sub></td>
      <td>6.26<br>(-1.82)</td>
      <td>3.49<br>(-4.59)</td>
      <td>3.07</td>
      <td>4.97</td>
      <td>6.52</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>5.93</td>
    </tr>
    <tr>
      <td>E<sub>f2</sub></td>
      <td>-</td>
      <td>-</td>
      <td>0.15<br>(-7.93)</td>
      <td>1.19<br>(-6.89)</td>
      <td>3.03<br>(-5.05)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>0.84<br>(-15.33)</td>
    </tr>
  </tbody>
</table>

Table III. Effect of different exchange-correlation functionals on the binding energy of O₂ at
Seᵥₐc, and the binding energy between O atoms in gas phase O₂. All energies are given in eV.

<table>
  <thead>
    <tr>
      <th>Exchange-<br>Correlation<br>Functional</th>
      <th>Bond dissociation<br>energy in gas phase<br>O₂ (experiment:<br>5.169 eV)</th>
      <th>Binding energy<br>between O₂ and<br>Seᵥₐc, relative to<br>energy of O₂ (BE1)</th>
      <th>Binding energy<br>between O₂ and<br>Seᵥₐc, relative to<br>energy of two O<br>atoms (BE2)</th>
      <th>Binding energy<br>between O₂ and<br>Seᵥₐc, relative to<br>energy of two O<br>atoms, computed<br>from BE1 and<br>using the<br>experimental O₂<br>bond dissociation<br>energy of 5.169 eV<br>(BE3)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PBE-D2</td>
      <td>6.04</td>
      <td>2.80</td>
      <td>8.84</td>
      <td>7.97</td>
    </tr>
    <tr>
      <td>RPBE</td>
      <td>5.65</td>
      <td>1.95</td>
      <td>7.60</td>
      <td>7.11</td>
    </tr>
    <tr>
      <td>RPBE-D3</td>
      <td>5.65</td>
      <td>2.20</td>
      <td>7.85</td>
      <td>7.37</td>
    </tr>
    <tr>
      <td>BEEF-vdW</td>
      <td>5.32</td>
      <td>1.90</td>
      <td>7.22</td>
      <td>7.07</td>
    </tr>
  </tbody>
</table>

![](./images/867762514702631331_6.jpg)

FIG. 6. Top and side view of the atomic structure of O-related defects in WSe₂. Blue: W,
Green: Se, Red: O.

![](./images/867762514702631331_7.jpg)

FIG. 7. Top and side view of the atomic structure of H-related defects in WSe₂. Blue: W,
Green: Se, Orange: H.

![](./images/867762514702631331_8.jpg)

FIG. 8. Top and side view of the atomic structure of C-related defects in WSe₂. Blue: W,
Green: Se, Gray: C.

![](./images/867762514702631331_9.jpg)

FIG. 9. Spin polarized DOS of O-related defects in WSe₂.

![](./images/867762514702631331_10.jpg)

FIG. 10. Spin-polarized DOS of H-related defects in WSe₂.

![](./images/867762514702631331_11.jpg)

FIG. 11. Spin-polarized DOS of C-related defects in WSe₂.

![](./images/867762514702631331_12.jpg)

FIG. 12. Isosurface contour plot of the difference between spin up and spin down charge densities, for (a) Hₛₑ, (b), H_W and (c), H-Se_W. Yellow: positive: Blue: negative. Contour values taken to be 2% of the maximum magnitude. H atoms are colored red for clarity. Blue and green circles represent W and Se atoms, respectively.

![](./images/867762514702631331_13.jpg)

FIG. 13. Schematic depiction of charge transition levels and ionization energies (IE) of defects.

(a) Isolated ML. In this paper, the formation energies of the defect in different charged states are computed using the isolated ML. $\varepsilon(+/0)$ and $\varepsilon(0/-)$ are transition levels where the most stable charge state of the defect changes from one charge to another. $\varepsilon(+/0)$ with respect to CBM defines a donor IE (IEₙ), while $\varepsilon(0/-)$ with respect to VBM defines an acceptor IE (IEₐ). (b) ML on substrate. When the substrate is included, the Fermi level is determined by the interaction of the ML with the substrate, and this position of the Fermi level in turn dictates the stable charge state of the defect. For example, the defect is in charge state +1, 0 and -1 for E<sub>Fermi</sub> at E1, E2 and E3, respectively.

![](./images/867762514702631331_14.jpg)

FIG. 14. Plots for computing the ionization energies (IE) of $Se_{\text{vac}}$ in WSe₂ ML using Method 1

(a), (c) $IE(S,L_z)$ is a linear function of $L_z$ (23.34, 33.34, 43.34 $\mathring{A}$) in different lateral dimensions ($S$: 7 × 7, 8 × 8, and 9 × 9) for (+) and (-) charged states, respectively. (b), (d) $IE$ for $L_z=0$ (vertical intercept in (a,c)) as a function of $\frac{1}{\sqrt{S}}$ for (+) and (-) charged states, respectively. The points fit well to a straight line, and the vertical intercepts in (b) and (d) give the converged IE. The excellent linear fits show that equation 5 (see Section II) holds for $Se_{\text{vac}}$.

Table IV. Ionization energies (IE) in eV for the defects obtained using Methods 1 (M1) and 2 (M2) (9×9 supercell with vacuum height of 30 Å).

<table>
  <thead>
    <tr>
      <th>IE (eV)</th>
      <th>Se<sub>vac</sub></th>
      <th>W<sub>vac</sub></th>
      <th>Se<sub>W</sub></th>
      <th>O<sub>Se</sub></th>
      <th>O<sub>ins</sub></th>
      <th>O<sub>ad</sub></th>
      <th>O<sub>2-</sub><br>2Se<sub>vac</sub></th>
      <th>H<sub>Se</sub></th>
      <th>H<sub>ins</sub></th>
      <th>H<sub>W</sub></th>
      <th>H-Se<sub>W</sub></th>
      <th>H<sub>2-</sub><br>Se<sub>vac</sub></th>
      <th>H<sub>2-</sub><br>2Se<sub>vac</sub></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>donor (M1)</td>
      <td>1.54</td>
      <td>1.59</td>
      <td>1.53</td>
      <td>1.60</td>
      <td>1.58</td>
      <td>1.53</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>donor (M2)</td>
      <td>1.69</td>
      <td>1.50</td>
      <td>1.47</td>
      <td>1.69</td>
      <td>1.69</td>
      <td>1.68</td>
      <td>1.69</td>
      <td>0.97</td>
      <td>0.29</td>
      <td>1.31</td>
      <td>1.04</td>
      <td>1.68</td>
      <td>1.21</td>
    </tr>
    <tr>
      <td>acceptor (M1)</td>
      <td>1.46</td>
      <td>0.80</td>
      <td>-</td>
      <td>1.58</td>
      <td>1.58</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>acceptor (M2)</td>
      <td>1.41</td>
      <td>0.78</td>
      <td>0.88</td>
      <td>1.71</td>
      <td>1.69</td>
      <td>1.68</td>
      <td>1.67</td>
      <td>1.20</td>
      <td>1.66</td>
      <td>0.71</td>
      <td>1.01</td>
      <td>1.40</td>
      <td>1.36</td>
    </tr>
  </tbody>
</table>

Table V. Bader charge analysis. Difference between number of electrons centered on the impurity atom, and the number of valence electrons in the neutral impurity atom. A positive number indicates that the impurity atom takes electrons. The numbers in brackets are given for substitutional defects, where the charge normally associated with the missing Se or W atom is subtracted away. For example, O takes 0.98 e⁻ at the Oₛₑ site. Compared with what Se would normally take (0.445e⁻), the O takes an extra 0.535 e⁻.

<table>
  <tr>
    <td></td>
    <th>O<sub>ad</sub></th>
    <th>O<sub>ins</sub></th>
    <th>O<sub>Se</sub></th>
    <th>O<sub>W</sub></th>
    <th>O-Se<sub>W</sub></th>
    <th>O₂-Se<sub>vac</sub></th>
    <th>O₂-W<sub>vac</sub></th>
    <th>O₂-Se<sub>W</sub></th>
    <th>O₂-2Se<sub>vac</sub></th>
  </tr>
  <tr>
    <td>#e⁻</td>
    <td>0.90</td>
    <td>1.05</td>
    <td>0.98<br>(0.54)</td>
    <td>0.84<br>(1.73)</td>
    <td>0.83</td>
    <td>0.62, 0.52</td>
    <td>0.18, 0.35</td>
    <td>0.26, 0.05</td>
    <td>0.97x2<br>(0.53x2)</td>
  </tr>
  <tr>
    <td></td>
    <th>H<sub>ad</sub></th>
    <th>H<sub>ins</sub></th>
    <th>H<sub>Se</sub></th>
    <th>H<sub>W</sub></th>
    <th>H-Se<sub>W</sub></th>
    <th>H₂-Se<sub>vac</sub></th>
    <th>H₂-W<sub>vac</sub></th>
    <th>H₂-Se<sub>W</sub></th>
    <th>H₂-2Se<sub>vac</sub></th>
  </tr>
  <tr>
    <td>#e⁻</td>
    <td>0.09</td>
    <td>0.33</td>
    <td>0.36<br>(-0.09)</td>
    <td>-0.01<br>(0.88)</td>
    <td>0.05</td>
    <td>0.32, 0.24</td>
    <td>-0.01, 0.08</td>
    <td>0.01, 0.00</td>
    <td>0.34x2<br>(-0.10x2)</td>
  </tr>
</table>

![](./images/867762514702631331_15.jpg)

FIG. 15. Bader charge analysis. Charge difference distribution around the defects sites for (a) Oₛₑ, (b) O<sub>ins</sub>, (c) O<sub>ad</sub>. The charge difference $\Delta \rho$ between the WSe₂ units (total Bader charge on one W and 6 nearest neighbor Se atoms (each weighted by 0.5) minus the 18 valence electrons of the perfect WSe₂ primitive cell), plotted against r, the distance of the WSe₂ units from the defect site. The points for r very close to 0 (where $|\Delta \rho|$ is very large) are absent from the plot.