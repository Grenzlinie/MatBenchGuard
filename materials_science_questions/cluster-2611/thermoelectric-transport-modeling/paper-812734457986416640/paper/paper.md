A EUROPEAN JOURNAL

CHEMPHYSCHEM

OF CHEMICAL PHYSICS AND PHYSICAL CHEMISTRY

Accepted Article

Title: Thermal properties of ordered and disordered DNA chains:
Efficient energy conversion

Authors: Judith Helena Ojeda Silva and Santanu K. Maiti

This manuscript has been accepted after peer review and appears as an
Accepted Article online prior to editing, proofing, and formal publication
of the final Version of Record (VoR). This work is currently citable by
using the Digital Object Identifier (DOI) given below. The VoR will be
published online in Early View as soon as possible and may be different
to this Accepted Article as a result of editing. Readers should obtain
the VoR from the journal website shown below when it is published
to ensure accuracy of information. The authors are responsible for the
content of this Accepted Article.

To be cited as: ChemPhysChem 10.1002/cphc.201900699

Link to VoR: http://dx.doi.org/10.1002/cphc.201900699

WILEY-VCH
www.chemphyschem.org
![](./images/812734457986416640_1.jpg)

![](./images/812734457986416640_2.jpg)

# Thermal properties of ordered and disordered DNA chains: Efficient energy conversion

Judith Helena Ojeda Silva $^{1,2}$ and Santanu K. Maiti $^{3, *}$

$^{1}$ Grupo de Física de Materiales, Universidad Pedagógica y Tecnológica de Colombia, Tunja, Colombia
$^{2}$Laboratorio de Química Teórica y Computacional,
Grupo de Investigación Química-Física Molecular y Modelamiento Computacional (QUIMOL),
Facultad de Ciencias, Universidad Pedagógica y Tecnológica de Colombia, Tunja, Boyacá, Colombia
$^{3}$Physics and Applied Mathematics Unit, Indian Statistical Institute,
203 Barrackpore Trunk Road, Kolkata-700 108, India

Considering the numerous possibilities of having suitable thermoelectric energy conversion at nano-scale level, especially for molecular systems, in the present work we put forward a new proposal along this using a flat DNA segment as a functional element. It is modeled by coupling two chains to a form a two-stranded ladder like geometry, with interactions to first neighbors, within the tight-binding prescription. We critically investigate electrical and thermal properties of DNA molecule depending on the length of the system, temperature, molecule-to-lead coupling and the degree of (correlated) disorder. Our analysis might be helpful in analyzing thermoelectric signatures of correlated and uncorrelated disordered systems, and can be verified in laboratory.

**Keywords:** Thermoelectricity; DNA molecule; Transfer matrix; Correlated disorder; Lyapunov exponent.

## I. INTRODUCTION

The electron transport is a feature that has been analyzed deeply to materials, where properties of symmetry and translational invariance have valid applying concepts such as: Bloch theorem, unit cell, number of wave, Brillouin zone, among others [1–5]. Generally, in these cases we speak of long-range order where the quantum states are representations of Bloch type and are spatially delocalized, with wave vector $k$. However, such symmetry arguments are not fully applicable, since there is no strictly ordered crystals. All material, in fact, is always disturbed by distortions presenting, dislocations, impurities, vacancies or other defects simply either by external fields or by the same interactions of the elements that compose it. These materials, also known as disordered systems, are amorphous semiconductors, glass, liquid metals, polymers, molecules, DNA molecules, among others.

In recent times there has been growing interest and development of mesoscopic and nanometric systems using DNA molecules as a prototype quantum wire with the desire to use it in molecular electronic devices, and especially, the studies of quantum transport through DNA molecules have been extensively performed in the past few years [6–18], due to their unique and diverse characteristic features. A wealth of literature knowledge has already been developed in investigating electronic transport through DNA molecules under different physical conditions and several interesting features have been explored. But, too limited progress has been done so far in the context of energy conversion viz, the conversion of waste heat into usable electrical energy. A fruitful energy conversion is undoubtedly required to overcome the energy crisis and to address the present global energy issues. It has already been recommended that low-dimensional quantum systems will be the suitable functional elements, and among them DNA molecule can be the role model for proper energy conversion due to its non-trivial electronic properties. Now, whenever we talk about the thermoelectric energy conversion, we need to focus on the conversion efficiency which is measured by the quantity *figure of merit*, usually referred as $ZT$. To make the device competitive with present thermoelectric devices, $ZT$ should be at least comparable to unity [19, 22], and, higher value of $ZT$ ($ZT > 1$) is thus always favorable.

Utilizing the atypical electrical transport characteristics, in the present work we focus on thermoelectric properties of flat DNA segments that may provide some interesting behavior and can lead to a higher $ZT$. The factor

![](./images/812734457986416640_3.jpg)

FIG. 1: Flat segment of DNA molecule, having base pairs A (A-T) and B (G-C) composed with different bases, is directly connected to the left and right electrodes. The electrodes are taken in the form of a two-stranded ladder, and they are considered as perfect and semi-infinite.

$ZT$ involves electrical conductance ($G$), Seebeck coefficient ($S$), and thermal conductance ($\kappa$). Thus, to have a complete idea about $ZT$, we need to explore all these different thermoelectric quantities. We model the DNA molecule using the standard tight-binding (TB) framework within a nearest-neighbor approximation, and calculate the electronic transmission using the transfer ma-

*Electronic address: santanu.maiti@isical.ac.in

trix formalism [23-30], while the thermoelectric quanti- ties are evaluated based on the Ladauer prescription [31-36]. Depending on the arrangements of two base pairs A and B (see Fig. 1), we can have ordered and disordered DNAs, and, we will concentrate on both these two cases to make the present communication a self contained one.

It is important to note that, in the present work we consider artificial DNAs instead of real ones, since a real DNA involves more cumbersome arrangements of differ- ent nucleobases which is very difficult to simulate prop- erly. On the other hand, with the advanced nanotech- nologies it is now possible to fabricate artificial DNAs quite easily with any desired configuration. Moreover these artificial DNAs are suitable enough to mimic the characteristic features of real DNAs, and several such propositions have been made in different contemporary works [18, 37-39]. In addition, we also make another valid approximation by considering a 'flat' DNA, whereas the common wisdom suggests that real DNAs are helical in nature. But the fact is that, for DNA molecules the in- teraction is restricted almost within the nearest-neighbor sites, which has been verified by several groups in their works [40, 41]. As the interaction is limited to the neigh- boring sites only, we can safely consider the flat structure of DNA rather than considering the helical one. These assumptions will make the model relatively simpler one, and with these choices no physical picture will be ham- pered that we are going to investigate in the present work. As a side note, we would like to state that longer range interactions are important especially for other biological molecules like $\alpha$- and $\beta$-helical proteins, nucleic acids and to name a few [40, 41]. These systems are not considered here.

The rest part of our work is organized as follows. In Section II, we introduce the DNA model based on a TB Hamiltonian. In Section III, we describe the method uti- lized for the calculations of different thermoelectric quan- tities. The results are thoroughly analyzed in Section IV. Finally, we summarize our essential findings in Section V.

## II. MODEL

Let us start with the junction set up shown in Fig. 1, where a double-stranded DNA molecule is directly cou- pled to the contact electrodes (namely, left and right electrodes). The DNA is modeled by coupling two one- dimensional chains laterally to form a ladder.

The full system is described by a tight-binding Hamil-tonian, given by:

$$
\begin{aligned}
H= & \sum_{i, j} v_{i, j}\left(c_{i, j}^{\dagger} c_{(i+1), j}+c_{(i+1), j}^{\dagger} c_{i, j}\right) \\
& +\sum_{i, j, l} v_{i, j}^{l}\left(c_{i, j}^{\dagger} d_{(i+1), j}+c_{(i+1), j}^{\dagger} d_{i, j}\right) \\
& +\lambda \sum_{\alpha, \beta}\left(c_{\alpha}^{\dagger} c_{\beta}+c_{\beta}^{\dagger} c_{\alpha}\right)+\sum_{i, j} E_{i, j} c_{i, j}^{\dagger} c_{i, j} \\
& +\sum_{i, j, l} E_{i, j}^{l} d_{i, j}^{\dagger} d_{i, j},
\end{aligned}
$$

where $c_{i, j}^{\dagger}$ is the creation operator of an electron at site $i$ of the DNA chain $j$ ($j=\alpha,\beta$), $\lambda$ is the intra-chain hopping integral, $E_{i,j}$ is the energy of atomic sites in the DNA molecule, $d_{i,j}^{\dagger}$ is the creation operator of an electron at site $i$ of the left (L) or right (R) leads, $v_{i,j}^l$ is molecule- lead hopping (where $l=L,R$) and $E_{i,j}^l$ is the energy of atomic site of leads. On-site energies are chosen as bivalued sites given by $E_A$ or $E_B$, where $E_A$ contains the base pairs Adenine and Thymine ($A-T$) and $E_B$ contains the base pairs Cytosine and Guanine ($C-G$).

Both the ordered and disordered DNA molecules are taken into account to analyze thermoelectric properties. For the ordered DNA, the base pairs $A$ and $B$ are ar- ranged in a regular pattern, while we adopt a minimal model to study disordered system with diagonal disor- der and without off-diagonal disorder. This model is perhaps the simplest generalization of Anderson model where, when the concentration of one type of sites, say $B$, the probability for two nearby sites to have the same on-site energy $E_B$ is null (correlated disorder) and the probability of that the $i$ site will be busy for $B$ is $P_B$ and the probability of that the $i$ site will be busy for $A$ is $1-P_B$. In this case the system behaves as the "Repul- sive binary alloy" model. However, if the system presents bonding between first neighbors type $B$ bases, we speak of a disordered system uncorrelated [23, 25, 26, 30]. For the ordered case the probability $P_B=1$.

## III. METHOD

In order to investigate thermoelectric properties of the DNA molecule, the primary quantity that we need to evaluate is the transmission probability through this molecular system. Here we do it by using transfer ma- trix (TM) formalism [25-30], though one can also usesome other prescriptions like wave-guide theory [42, 43] or Green's function technique [3, 44-48]. The prescrip- tion for calculating transmission probability using TM method is briefly described as follows, considering a sim- ple $N$-site chain, which can easily be generalized for our ladder system or even other complicated geometri- cal shaped conductor. The TM method permits us to find the local projection, related to the coefficients at each end of the chain formed by $N$ sites given by

$$
\left(\begin{array}{l}
C_{0} \\
C_{1}
\end{array}\right)=Q_{N}\left(\begin{array}{l}
C_{N} \\
C_{N+1}
\end{array}\right),\qquad(2)
$$

where, each coefficient $C_i$ becomes

$$
C_{i}=\left(\begin{array}{l}
C_{i, \alpha} \\
C_{i, \beta}
\end{array}\right).\qquad(3)
$$

$Q_N$ represents the evolution of a state, which can be written as the product of transfer matrices $M_i$, such that

$$
Q_{N}=\prod_{i=1}^{N} M_{i}\qquad(4)
$$

and

$$
M_{i}=\left(\begin{array}{cc}
\left(V^{i, i-1}\right)^{-1} \epsilon_{i} & \left(V^{i, i-1}\right)^{-1} V^{i, i+1} \\
1 & 0
\end{array}\right)\qquad(5)
$$

$$
V^{i, i \pm 1}=\left(\begin{array}{cc}
v_{\alpha}^{i, i \pm 1} & \lambda^{i} \\
\lambda^{i} & v_{\beta}^{i, i \pm 1}
\end{array}\right)
\tag{6}
$$

$$
\epsilon_{i}=\left(\begin{array}{cc}
E-E_{i, \alpha} & 0 \\
0 & E-E_{i, \beta}
\end{array}\right)
\tag{7}
$$

If the determinant of each matrix $M_{i}$ is finite and different from zero, then these matrices can meet *Oseledec theorem* [25, 26, 30] i.e., there exists a matrix $\Gamma$ which satisfies the condition

$$
\Gamma=\lim _{N \rightarrow \infty}\left(Q_{N}^{\dagger} Q_{N}\right)^{1 / 2 N}.
\tag{8}
$$

This $\Gamma$ matrix has eigenvalues given by $e^{\gamma_{j}}$ where $\gamma_{j}$ are the Lyapunov Characteristic Exponents (LCE's) of $Q_{N}$.

The *LCE's* are associated with the exponential decay of the wave function, and thus the localization length, $\Lambda$, of the system, which is taken as the inverse of the lowest of *LCE's*. Oseledec theorem guarantees us the existence of the $\Gamma$ matrix that contains the necessary and relevant information of the system, and it circumvents the use of statistical averages.

Given the definition of the localization length $\Lambda(E)=$ $-2 N / \ln (T(E))$, we can calculate the transmission probability $T(E)$ associated with the lowest of the *LCE's* by the relation

$$
T(E)=e^{-\frac{2 N}{\Lambda(E)}},
\tag{9}
$$

where $\Lambda(E)=\left[\min \left\{\gamma_{j}\right\}\right]^{-1}$. We can define the normalized localization length as the ratio between the localization length and the length of the chain, giving us the information whether there exists localized and/or delocalized states.

Once the transmission function $T(E)$ is determined based on transfer matrix formalism which can meet Oseledec theorem, we can do all the theoretical calculations to study thermoelectric properties, which is the standard formalism for these calculations. For complete analysis we need to calculate electrical conductance $G$, Seebeck coefficient $S$, thermal conductance $k$ and the figure of merit $Z T$ [19, 20, 33]. We evaluate these quantities by using Landauer integrals through the following relations:

$$
G=\frac{2 e^{2}}{h} L_{0}
\tag{10a}
$$

$$
S=-\frac{1}{e T} \frac{L_{1}}{L_{0}}
\tag{10b}
$$

$$
\kappa=\frac{2}{h T}\left(L_{2}-\frac{L_{1}^{2}}{L_{0}}\right)
\tag{10c}
$$

$$
Z T=\frac{G S^{2} T}{\kappa}=\frac{1}{\frac{L_{0} L_{2}}{L_{1}^{2}}-1}
\tag{10d}
$$

where $T$ being the equilibrium temperature, $e$ is the electronic charge and $h$ represents the Plank's constant. The Landauer integrals $L_{n}$ used in Eq. 10 have the form

$$
L_{n}=-\int T(E)(E-E f)^{n}\left(\frac{\partial f(E)}{\partial E}\right) d E,
\tag{11}
$$

where $E f$ describes the equilibrium Fermi energy of the system under zero biased condition, and $f(E)$ gives the Fermi-Dirac distribution function.

## IV. NUMERICAL RESULTS AND DISCUSSION

Based on the above theoretical prescription we compute transmission probability along with all the required thermoelectric quantities for both the ordered and disordered flat DNA molecules, and the results are critically analyzed one by one in this section. Before presenting the results let us mention the parameter values those are common in our calculations.

Throughout the paper, the thermal properties through the base-pairs poly(A)-poly(T) and poly(G)-poly(C) DNA molecule are addressed with the following on-site energies: $E_{A}=0.26 \mathrm{eV}$ (Adenine energy), $E_{T}=$ $-0.93 \mathrm{eV}$ (Thymine energy), $E_{G}=1.14 \mathrm{eV}$ (Guanine energy) and $E_{C}=-1.06 \mathrm{eV}$ (Cytosine energy) [10, 11].

For simplicity and in order to reduce the number of model parameters we adopt a simple parametrization taking a homogeneous hopping along both the strands between adjacent nucleotides i.e., the interaction of $\pi$ $\pi$ stacking between base pairs given by $v_{G G}=v_{C C}=$ $v_{A A}=v_{T T}=v_{G A}=v_{C T}=\lambda=2.8 \mathrm{eV}$. At the same time, to minimize the contact effects, we assume a strong coupling between the electrodes and the DNA molecule and set $v_{M L}=2.8 \mathrm{eV}$, unless stated otherwise.

The results are classified in two parts (Part-A and Part-B), associated with the orderness of the DNA molecule. In the first part (Part-A) we focus on the ordered DNA, while in the other part (Part-B) the results of disordered DNA molecule are presented.

### A. Ordered DNA

We start by establishing the configuration within the ladder model of the DNA molecule taking into account the distribution with parameters $A$ and $B$ shaped as shown in Fig. 1. We fix a probability $P_{B}=1$ which corresponds to an ordered distribution of the base pairs $A$ and $B$, and the sequence reads as $A B A B A B A B A B A \ldots$ i.e., alternate arrangements of $A$ and $B$.

Figure 2 shows the variation of electrical conductance $G$ as a function of the Fermi energy for an ordered DNA having 50 base pairs at three typical temperatures (T=200K, T=300K and T=400K). In the calculation of the conductance $G$, the pair of bases $E_{B}$ acts as a simple potential barrier for the charges that migrate between the bases $E_{A}$ at the ends of the molecule and as we know, the linear conductance $(G=G_{0} T(E))$ is proportional to the transmission probability (which is not plotted here), we can deduce that the transmission is much smaller than unity. The transport channels can appear near the energies of the eigenvalues of the molecule where the resonances occur, resulting peaks in the conductance spectrum as we can see in Fig. 2.

We also observe an anti-resonance that originates from the destructive interference between the non-localized

![](./images/812734457986416640_4.jpg)

FIG. 2: Conductance ($G$) for an ordered DNA with 50 base pairs ($N=50$), varying the temperature with T=200K, T=300K and T=400K.

states in the base pairs along the two main conducting channels (inter-site coupling of the bases) and the localized states that are generated from the intra-site coupling of the bases [49].

On the other hand, we can observe that as the temperature increases, the conductance amplitude gets decreased. It means that the resistivity through the DNA molecule grows up with increasing the system temperature, and it happens due the enhancement of the vibrating amplitude of the atoms associated with the bases around their equilibrium positions, which hinders the movement of the large amount of free electrons that the molecule possesses.

![](./images/812734457986416640_5.jpg)

FIG. 3: Seebeck co-efficient ($S$) for an ordered DNA having 50 base pairs, varying the temperature with T=200K, T=300K and T=400K.

In order to show the temperature dependence, in our theoretical calculations we set these three typical temperature values. Now, one may think that at such a high temperature there is a possibility to have denaturation of DNA which involves the decoupling of the two strands. This morphological change actually depends on the specific arrangements of the base pairs. Depending on the arrangements of the bases one can design an (artificial) DNA that can persists even at much higher temperature. So this is one aspect. The other thing is that here we are working with small scale DNA samples, and thus, the average energy level spacing is reasonably large compared to the thermal energy. Therefore, the denaturing effect of DNA can safely be avoided. For actual and longer DNA molecules, we need to restrict the temperature accordingly such that it is not denatured. Here it is relevant to note that, few years back a breakthrough experiment has been done on a double-stranded DNA molecule at room temperature to explore spin selectivity [50]. It gives a strong confidence that our analysis can also be verified in a wide range of temperature.

Figure 3 shows the variation of thermopower, viz, the Seebeck coefficient $S$ as a function of Fermi energy for the same set of physical parameters as presented in Fig. 2.

![](./images/812734457986416640_6.jpg)

FIG. 4: Thermal conductance ($\kappa$) for an ordered DNA with 50 base pairs, varying the temperature with T=200K, T=300K and T=400K.

![](./images/812734457986416640_7.jpg)

FIG. 5: $ZT$ for an ordered DNA with 50 base pairs, varying the temperature with T=200K, T=300K and T=400K.

An interesting pattern is observed especially towards the central part of the transmitting zones. From Fig. 2 it is shown that the conductance spectrum gets splitted into two zones associated with the energy eigenvalues of the DNA molecule. Towards the inner sides of these zones, the conductance, and hence the transmission function, becomes more asymmetric which results a high degree of thermopower $S$ as clearly reflected from the results given in Fig. 3. The thermopower actually depends on the 'asymmetric' nature of transmission function. More asymmetry means more thermopower, and higher thermopower leads to higher $ZT$ as the factor $S$ is in the numerator of $ZT$ (see Eq. 10(d)). Thus, our primary goal will be to achieve large $S$ to have better thermoelectric performance, and it can be obtained for a system that exhibits high degree of asymmetric transmission. On the other hand, when the transmission function becomes less asymmetric, $S$ gets reduced, and it is clearly noticed if we

look into the energy regions well inside the bands. The other interesting observation is that at the inner parts of
the energy bands, $S$ increases with temperature, while opposite signature appears for other energy regions. The sign reversal in $S$ is associated with the change in slope of the transmission function [51].

In Fig. 4 we show the dependence of another ther- moelectric quantity, the thermal conductance ($\kappa$), as a function of the Fermi energy for the same set of system parameters as described above. The first impression is that, the thermal conductances increases with the rise of temperature, and this is usually expected. But the no- table thing is that for the entire allowed energy window $\kappa$ is reasonably small ($\kappa < 50$ pW/K). The lower value of $\kappa$ is always desirable as it will help to enhance the thermo- electric performance $ZT$, since the efficiency is inversely proportional to the thermal conductance.

With the results of electrical conductance (Fig. 2), thermopower (Fig. 3) and thermal conductance (Fig. 4), now we can easily explain the dependence of $ZT$ as a function of Fermi energy. The dependence is shown in Fig. 5 for the identical set of parameter values as taken above. Several significant features are noticed. At a first glance it is observed that the $ZT$ is greater than unity almost for the entire energy region, which is undoubtedly a good signature as we can set Fermi energy anywhere to find a reasonable $ZT$. But the most important behavior is seen when the Fermi energy is fixed around the inner edges of the allowed bands. A high degree of $ZT$ appears, which may even reach to more than 20 at T=400K. The essential mechanism of getting such a large $ZT$ depends solely on the asymmetric nature of the transmission func- tion at these zone edges. Well inside the energy bands, since the transmission function is more symmetric, $ZT$ becomes quite less as clearly visible from the curves given in the inset of Fig. 5. As the Fermi energy $E_F$ can be ad- justed selectively by applying external gate voltage [52], we can thus set $E_F$ in a suitable way to achieve favorable $ZT$ using this functional element, viz flat DNA.

![](./images/812734457986416640_8.jpg)

FIG. 6: Maximum conductance (Gmax), maximum Seebeck co- efficient (Smax), maximum thermal conductance ($\kappa$max) and max- imum of $ZT$ (ZTmax) of an ordered DNA as a function of temper- ature. Here we set $N = 50$.

From the above analysis it is reflected that all the ther- moelectric quantities are significantly influenced by the temperature difference between the hot and cold ends. So now, to have a more clear idea about the dependence of all the thermoelectric quantities on temperature, in Fig. 6 we show the results by varying the temperature in a wide range (180K to 420K). We plot the maximum of each of these quantities, and we compute it by tak- ing the maximum within the full allowed energy window. What we see that the electrical conductance smoothly de- creases, while the thermopower and thermal conductance gradually increase with the rise of temperature. The re- sultant of all these three yields an increasing nature of $ZT$ with temperature. The $ZT$-$T$ spectrum (Fig. 6(d)) will provide an important information about the choice of temperature for better performance.

![](./images/812734457986416640_9.jpg)

FIG. 7: ZTmax for an ordered DNA having $N = 50$ as a function of the the molecule-lead coupling ($v_{ML} = \Gamma$).

As the thermoelectric performance is directly related to the electron transfer across the junction, it is expected that molecule-to-lead coupling will have a significant im- pact on it. To justify this fact, in Fig. 7 we show the variation of $ZT_{max}$ as a function of molecular coupling. The efficiency changes drastically with this coupling, and thus, it can be manifested that molecule-to-lead coupling can be utilized as a suitable tuning parameter for efficient energy conversion.

### B. Disordered DNA

The results studied so far are worked out for the perfect DNA systems. Now we concentrate on disordered DNAs, and look forward the role of disorder on $ZT$.

The disorder is introduced by changing the probabil- ity $P_B$ of getting B pair in the ladder string from unity ($P_B = 1$ indicates perfect DNA). For instance if we set $P_B = 0.9$, it corresponds to 45% of all the parameters (A + B) and for this case, the sequence of the bases can have the form $ABAABABAA....$

In the same way we can find configurations where the probabilities are $P_B = 0.8,0.7,...$, and these distribu- tions lose the sequence more frequently with respect to the parameter B. In placing B, we impose a restriction

![](./images/812734457986416640_10.jpg)

FIG. 8: Electrical conductance (G), Seebeck co-efficient (S), thermal conductance ($\kappa$) and $ZT$ for a flat DNA with $N = 100$ base pairs varying the degree of disorder $P_b = 1.0$ (black line), $P_b = 0.9$ (red line) and $P_b = 0.8$ (blue line). Here we choose T=250K.

that at no moment the two B bases can sit together. Under this situation, we can call it as a correlated disordered system, instead of a random one. In the rest of our analysis we focus on correlated disordered DNA molecules.

Here it is worth clarifying that the distributions mentioned above that contain disorder are not the only ones, on the contrary, for each value of $P_B$ where $P_B \neq 1.0$, we can have several distinct configurations, and therefore, we determine all the quantities taking the average over a large number of such configurations.

Figure 8 shows the characteristics of electrical conductance (G), Seebeck co-efficient (S), thermal conductance ($\kappa$) and $ZT$ as a function of Fermi energy for a molecular system with $N = 100$ base pairs varying the degree of disorder $P_b = 1.0$ (black line), $P_b = 0.9$ (red line) and $P_b = 0.8$ (blue line). Here we choose T=250K.

Disorder has significant impact on all the thermoelectric quantities. A careful inspection reveals that in the absence of disorder ($P_B = 1$), there is a finite energy gap in the electrical conductance spectrum (black line of Fig. 8(a)) which denotes a semiconducting nature. This semiconducting gap decreases with the inclusion of impurities in the system and can eventually vanish for a large degree of disorder (see red and blues lines of Fig. 8(a)), which yields a semiconducting-to-conducting transition. This closing of energy gap is solely associated with the disorderness of the system. For $P_B = 1$, the bases A and B are arranged in order which generates a two-band spectrum, whereas increasing the degree of disorderness the correlation between the bases gradually decreases, and thus, the gap closes. This is the well known phenomenon and can be utilized in designing suitable DNA based electronic devices.

As the energy levels, and hence, finite transmission occurs at the band center, where zero transmission probability was obtained in the case of perfect DNA, the thermopower $S$ decreases around the band center (red and blue lines of Fig. 8(b)) compared to the impurity free DNA molecule (black line of Fig. 8(b)). As already discussed that the asymmetric nature of transmission function is the most desirable one for achieving better thermopower and hence thermoelectric performance. And it is usually obtained by placing the Fermi energy at the edges of the energy bands, since sharp at the edge, one side is allowed for transmission while the other side is forbidden. Thus, it can clearly be manifested that the semiconducting material is more superior than the metallic one for efficient energy conversion.

![](./images/812734457986416640_11.jpg)

FIG. 9: Maximum electrical conductance (Gmax), maximum Seebeck co-efficient (Smax), maximum thermal conductance ($\kappa$max) and ZTmax as a function of temperature of a disordered DNA ($P_b = 0.85$) for different disordered configurations. Here we take $N = 100$.

It is a good sign that the thermal conductance gets reduced with increasing disorder (Fig. 8(c)) which indicates that the efficiency might increase, but the final response (viz, $ZT$) depends on all the factors $G$, $S$ and $\kappa$. In Fig. 8(d) the variation of $ZT$ is shown, which provides much reduced value compared to the perfect DNA molecule. The more reduction of both $G$ and $S$ with disorder does not compensated by the lowering of $\kappa$ which results a lower value of $ZT$. Even though it decreases, still $ZT$ is quite comparable to 1, which is not too bad compared to the reported values for molecular systems.

Finally, let us concentrate on the spectra shown in Fig. 9 where $G_{max}$, $S_{max}$, $\kappa_{max}$ and $ZT_{max}$ are plotted as a function of temperature. The results are computed for a disordered DNA considering $P_B = 0.85$ and $N = 100$. The black line without points in each of the spectra denotes the average of the curves obtained for four distinct disordered configurations. Like ordered DNA molecule, here the electrical conductance decreases and thermal conductance increases with temperature. But, contrary to the perfect DNA molecule, the thermopower decreases with temperature in presence of disorder. The incorporation of disorder with spatial correlation into the diagonal sector of the molecular Hamiltonian reduces the trans-

port energy, and thus, the Seebeck coefficient. It is in agreement with the previous results of disordered systems as reported by Meddels and Tessler [53]. Combining all these effects, we eventually get the variation of $ZT_{max}$ which shows a slower increment with temperature.

## V. CLOSING REMARKS

In the present work we have investigated thermoelectric properties considering a flat DNA segment and established that the DNA molecule can be utilized as an efficient functional element for energy conversion. Both the ordered and disordered counterparts have been taken into account to address the thermoelectric behavior. From our analysis it emerges that the semi-conducting material is more superior than a conducting one for better thermoelectric performance, as for the previous material more asymmetric transmission function can be obtained by selectively choosing the Fermi energy which leads to an important role in enhancing $ZT$.

We have used a standard theoretical prescription for evaluating all the physical quantities, and described the model within a tight-binding framework which is extremely suitable for analyzing transport properties especially in molecular junctions. Our study can be useful in describing thermoelectric signatures in different simple and complex molecular geometries.

## VI. ACKNOWLEDGMENTS

JHOS acknowledges the financial support from el Patrimonio Autónomo Fondo Nacional de Financiamiento para la Ciencia, la Tecnología y la Innovación Francisco José de Caldas (project 80740-173-2019). SKM deeply acknowledges the financial support of the Science and Engineering Research Board, Department of Science and Technology, Government of India (Project File Number: EMR/2017/000504).

### Conflict of interest

The authors declare no conflict of interest.

[1] M. Brandbyge, J. L. Mozos, P. Ordejón, J. Taylor, K. Stokbro, *Phys. Rev. B* **2002**, 65, 165401.
[2] M. Razeghi, *Fundamentals of Solid State Engineering*, Kluwer Academic Publishers **2002**.
[3] S. Datta, *Electronic Transport in Mesoscopic Systems*, Cambridge University Press, Cambridge **1997**.
[4] X. G. Zhang, K. Varga, S. T. Pantelides, *Phys. Rev. B* **2007**, 76, 035108.
[5] A. Alase, E. Cobanera, G. Ortiz, L. Viola, *Phys. Rev. B* **2017**, 96, 195133.
[6] D. Porath, A. Bezryadin, S. de Vries, C. Dekker, *Nature* **2000**, 403, 635.
[7] A. Yu. Kasumov, M. Kociak, S. Guron, B. Reulet, V. T. Volkov, D. V. Klinov, H. Bouchiat, *Science* **2001**, 280, 291.
[8] H. Cohen, C. Nogues, R. Naaman, D. Porath, *Proc. Natl. Acad. Sci. USA* **2005**, 102, 11589.
[9] O. Legrand, D. Côte, U. Bockelmann, *Phys. Rev. E* **2006**, 73, 031925.
[10] R. Gutiérrez, S. Mohapatra, H. Cohen, D. Porath, G. Cuniberti, *Phys. Rev. B* **2006**, 74, 235105.
[11] A. V. Malyshev, *Phys. Rev. Lett.* **2007**, 98, 096801.
[12] J. H. Ojeda, R. P. A. Lima, F. Domíguez-Adame, P. A. Orellana, *J. Phys.: Condens. Matter* **2009**, 21, 285105.
[13] J. H. Ojeda , M. Pacheco, L. Rosales, P. A. Orellana, *Org. Electron.* **2012**, 13, 1420.
[14] L. A. Agapito, J. Gayles, C. Wolowiec, N. Kioussis, *Nanotechnology* **2012**, 23, 135202.
[15] J. C. Genereux, J. K. Barton, *Nature Chem.* **2009**, 1, 106.
[16] M. D. Ventra, Y. V. Pershin, *Nature Nanotech.* **2011**, 6, 198.
[17] G. I. Livshits *et al.*, *Nature Nanotech.* **2014**, 9, 1040.
[18] A. Guo, Q.-F. Sun, *Phys. Rev. B* **2012**, 86, 115441.
[19] K. A. Chao, M. Larsson, *Thermoelectric phenomena from macro-systems to nano-systems*, Ed. by S. N. Karmakar *et al.*, Physics of Zero- and One-Dimensional Nanoscopic Systems, Springer, UK **2007**.

[20] N. A. Zimbovskaya, *J. Phys.: Condens. Matter* **2016**, 28, 183002.
[21] S. Chakraborty, S. K. Maiti, *ChemPhysChem* **2019**, 20, 848.
[22] M. Dey, S. F. Aman, S. K. Maiti, *Europhys. Lett.* **2019**, 126, 27003.
[23] R. Rey-Gonzalez, P. A. Schulz, *Phys. Rev. B* **1996**, 54, 7113.
[24] P. Carpena, P. Bernaola-Galván, P. Ch. Ivanov, H. F. Stanley, *Nature* **2002**, 418, 955.
[25] J. H. Ojeda-Silva, R. R. Rey-González, *Revista Colombiana de Física* **2004**, 36, 335.
[26] J. H. Ojeda-Silva, R. R. Rey-González, *Revista Colombiana de Física* **2006**, 38, 109.
[27] R. G. Sarmento, G. A. Mendes, E. L. Albuquerque, U. L. Fulco, M. S. Vasconcelos, O. Ujsághyd, V. N. Freire, E. W. S. Caetano, *Phys. Lett. A* **2012**, 376, 2413.
[28] M. Mardaani, A. A. Shokri, K. Esfarjani, *Physica E* **2005**, 28, 150.
[29] M. Dey, S. K. Maiti, S. N. Karmakar, *Eur. Phys. J. B* **2011**, 80, 105.
[30] C. A. Plazas, K. M. Fonseca-Romero, R. R. Rey-González, *J. Nanosci. Nanotechnol.* **2018**, 18, 5042.
[31] E. Macià, *Phys. Rev. B* **2010**, 82, 045431.
[32] K. Biswas, J. He, I. D. Blum, C.-I. Wu, T. P. Hogan, D. N. Seidman, V. P. Dravid, M. G. Kanatzidis, *Nature* **2012**, 489, 414.
[33] E. Zerah-Harush, Y. Dubi, *Phys. Rev. App.* **2015**, 3, 064017.
[34] L. Simine, W. J. Chen, D. Segal, *J. Phys. Chem. C* **2015**, 119, 12097.
[35] S. K. Maiti, M. Dey, *Chem. Phys. Lett.* **2019**, 731, 136601.
[36] D. K. Suhendro, E. Yudiarsah, R. Saleh, *AIP Conference Proceedings* **2016**, 1719, 030033.
[37] A. M. Guo, *Phys. Rev. E* **2007**, 75, 061915.
[38] H. Lei, J. Chen, G. Nouet, S. Feng, Q. Gong, X. Jiang, *Phys. Rev. B* **2007**, 75, 205109.

[39] S. Sil, S. K. Maiti, A. Chakrabarti, *Phys. Rev. B* **2008**, 78, 113103.

[40] R. G. Endres, D. L. Cox, R. R. P. Singh, Colloquium: The quest for high conductance DNA, *Rev. Mod. Phys.* **2004**, 76, 195.

[41] A.-M. Guo, Q.-F. Sun, *Proc. Natl. Acad. Sci. U.S.A.* **2014**, 111, 11658.

[42] Y. Shi, H. Chen, *Phys. Rev. B* **1999**, 60, 10949.

[43] M. Patra, S. K. Maiti, *Sci. Rep.* **2017**, 7, 14313.

[44] D. S. Fisher, P. A. Lee, *Phys. Rev. B* **1981**, 23, 6851.

[45] S. Sil, S. K. Maiti, A. Chakrabarti, *Phys. Rev. Lett.* **2008**, 101, 076803.

[46] M. Dey, S. K. Maiti, S. N. Karmakar, *Org. Electron.* **2011**, 12, 1017.

[47] S. K. Maiti, S. Sil, A. Chakrabarti, *Ann. Phys. (N. Y.)* **2017**, 382, 150.

[48] S. K. Maiti, *Phys. Lett. A* **2015**, 379, 361.

[49] H. -H. Fu, L. Gu, D. -D. Wu, Z. -Q. Zhang, *Phys. Chem. Chem. Phys.* **2015**, 17, 11077.

[50] B. Göhler, V. Hamelbeck, T. Z. Markus, M. Kettner, G. F. Hanne, Z. Vager, R. Naaman, H. Zacharias, *Science* **2011**, 331, 894.

[51] Y. -J. Dong, X. -F. Wang, Y. -S. Liu, X. -M. Wu, *Org. Electron.* **2015**, 26, 176.

[52] M. L. Perrin, E. Galán, R. Eelkema, J. M. Thijssen, F. Grozema, H. S. J. van der Zant, *Nanoscale* **2016**, 8, 8919.

[53] D. Mendels, N. Tessler, *J. Phys. Chem. Lett.* **2014**, 5, 3247.

This article is protected by copyright. All rights reserved.