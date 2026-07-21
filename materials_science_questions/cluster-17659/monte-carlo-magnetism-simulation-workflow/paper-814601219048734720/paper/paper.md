# Edwards' Measures for Powders and Glasses
Alain Barrat, $^{1}$ Jorge Kurchan, $^{2}$ Vittorio Loreto, $^{3}$ and Mauro Sellitto $^{4}$ 
$^{1}$ Laboratoire de Physique Théorique, $^{*}$ Bâtiment 210, Université de Paris-Sud, 91405 Orsay Cedex, France
$^{2}$ P.M.M.H. Ecole Supérieure de Physique et Chimie Industrielles, 10 rue Vauquelin, 75231 Paris, France
$^{3}$ Università degli Studi di Roma "La Sapienza," Dipartimento di Fisica, Piazzale Aldo Moro 5, 00185 Rome, Italy and INFM, Unità di Roma 1, Rome, Italy
$^{4}$ Laboratoire de Physique de l'École Normale Supérieure de Lyon, 46 Allée d'Italie, 69007 Lyon, France
(Received 8 June 2000)

Can one construct a thermodynamics for compact, slowly moving powders and grains? A few years ago, Edwards proposed a possible step in this direction, raising the fascinating perspective that such systems have a statistical mechanics of their own, different from that of Maxwell, Boltzmann, and Gibbs, allowing us to have some information while still ignoring dynamic details. Recent developments in the theory of glasses have come to confirm these ideas within mean field. In order to go beyond, we explicitly generate Edwards' measure in a 3D model. Comparison of the results with the irreversible compaction data shows very good agreement. The present framework immediately suggests new experimental checks.

PACS numbers: 05.70.Ln, 05.20.-y, 45.70.Cc, 64.70.Pf

The classical way to go from the microscopic dynamics to statistical mechanics proceeds in two steps: one first identifies a distribution that is left invariant by the dynamics (e.g., the microcanonical ensemble), and then assumes that this distribution will be reached by the system, under suitable conditions of "ergodicity." For granular systems this approach seems doomed from the outset: because energy is lost through internal friction, and gained by a non-thermal source such as tapping or shearing, the dynamical equations do not leave the microcanonical or any other known ensemble invariant. Moreover, the compaction dynamics is extremely slow and does not approach any stationary state on experimental time scales. This raises the question of characterizing the typical configurations or the region of phase space visited dynamically.

The proposal of Edwards and collaborators [1-3] is to use an alternative distribution for very gently vibrated or sheared granular systems, with the static situation as a limiting case. It may be summarized as follows: given a certain situation attained dynamically, physical observables are obtained by averaging over the usual equilibrium distribution at the corresponding volume, energy, etc., but restricting the sum to the "blocked" configurations defined as those in which every grain is unable to move. This definition leads immediately to an entropy (in the glass literature a "complexity") $S_{\text{edw}}$, given by the logarithm of the number of blocked configurations of given volume, energy, etc., and its corresponding density $s_{\text{edw}} \equiv S_{\text{edw}}/N$. Associated with this entropy are the state variables such as "compactivity" $X_{\text{edw}}^{-1}=\frac{\partial}{\partial V}S_{\text{edw}}(V)$ and "temperature" $T_{\text{edw}}^{-1}=\frac{\partial}{\partial E}S_{\text{edw}}(E)$.

That configurations with low mobility should be relevant in a jammed situation is rather obvious; the strong assumption here is that, apart from the usual statistical weights, all blocked configurations are treated as equivalent-any extra weight of dynamical origin that might distinguish them is disregarded. The purpose of this Letter is to argue that this "flatness" assumption characterizing Edwards' distributions is neither capricious (it leads to correct predictions for the compaction dynamics of a given class of systems) nor obvious (it does not apply to other classes of systems). To do this we devise a method to count the blocked configurations and compute averages over them.

Let us briefly summarize the state of the art. A first clue comes from exploiting the analogy between the settling of grains and powders, as when we gently tap a jar with flour to make space for more, and the aging of glassy systems [4-6]: in both cases, the system remains out of equilibrium on all accessible time scales, and displays very slow relaxations.

In the late 1980s, Kirkpatrick *et al.* [7,8] recognized that a class of mean-field models contains, although in a rather schematic way, the essentials of glassy phenomena. When the aging dynamics of these systems was solved analytically, a feature that emerged was the existence of a temperature $T_{\text{dyn}}$ for all the slow modes (corresponding to structural rearrangements) [9,10]. For our purposes here, $T_{\text{dyn}}$ can be defined by comparing the random diffusion and the mobility between two widely separated times $t$ and $t_w$ of any particle or tracer in the aging glass. Surprisingly, one finds in all cases an Einstein relation $\langle(r(t)-r(t_w))^2\rangle=T_{\text{dyn}}\frac{\delta\langle r(t)-r(t_w)\rangle}{\delta f}$, where $r$ is the position of the particle and $f$ is a constant perturbing field. While in an equilibrium system the fluctuation-dissipation theorem guarantees that the role of $T_{\text{dyn}}$ is played by the thermodynamic temperature, the appearance of such a quantity out of equilibrium is by no means obvious. $T_{\text{dyn}}$ is different from the external temperature, but it can be shown to have all other properties defining a true temperature [10].

As it turned out, despite its very different origin, this temperature matches exactly Edwards' ideas: $T_{\text{edw}}$ and $T_{\text{dyn}}$ happen to coincide for mean-field glass models aging in contact with an almost zero temperature bath [11-15].

In fact, given the energy $E(t)$ at long times, the value of any other macroscopic observable is also given by the flat average over all blocked configurations of energy $E(t)$. Within the same approximation, one can also treat systems that, like granulars, present a nonlinear friction and different kinds of energy input, and the conclusions remain the same [16].

A first partial conclusion is then that Edwards' scenario is at the very least correct within mean-field schemes and for very weak vibration or forcing. The problem that remains is to what extent it carries through to more realistic models.

In this direction, there have recently been studies [17] of Lennard-Jones glass formers from the perspective of the so-called "inherent structures" (a partition of the phase space in terms of the blocked configurations [18]). In this context a "flat weight" assumption-similar in spirit but not quite equivalent to Edwards'-also comes into question and is tested in various ways. Though there are caveats [19,20], the results are encouraging.

The path we follow instead is to construct the Edwards' measure explicitly in the case of representative (non-mean-field) systems, together with the corresponding entropy and expectation values of observables. We thus obtain results that are distinctly different from the equilibrium ones, and we can compare both sets with those of the irreversible compaction dynamics.

The first model we consider is the so-called Kob-Andersen (KA) model [21] that, though very schematic, reproduces rather well several aspects of glasses [22] and of granular compaction [23]; most important, this model is non mean field. A particle can move to a neighboring empty site, on a three dimensional lattice, only if it has less than four neighbors in the initial and in the final position. (In these "hard particle" models the temperature is irrelevant, and we set it to one.) The dynamic rule guarantees that the equilibrium distribution is trivially simple since all the configurations of a given density are equally probable. However, at densities close to $\rho_{\mathrm{g}}(\simeq 0.88)$, the particle diffusion becomes extremely slow due to the kinetic constraints. In order to mimic a compaction (or aging) process without gravity, we simulate a "piston" by freely creating and destroying particles only on the topmost layer with a chemical potential $\mu$ [22].

(i) The dynamic measurements are taken as follows: starting from low density, we perform a slow compression by raising the chemical potential up to a high value $\mu=3$. Since the equilibrium density at $\mu=3$ is much larger than the jamming density $\rho_{g}$, the system falls out of equilibrium and very slow compaction ensues. We record the density $\rho(t)$ and the spatial structure function $g_{\mathrm{dyn}}(r, t)$ defined as the probability that two sites at distance $r$ are occupied. We also compute the dynamic temperature $T_{\text {dyn }}$ by comparing induced and spontaneous displacements. This is the set of observables we use for testing the different measures, which are obtained independently.

(ii) In the equilibrium measure all configurations (whether they are blocked or not) have equal weight. It is easy to obtain the exact equilibrium entropy density per particle $s_{\text {equil }}(\rho)=-\rho \ln \rho-(1-\rho) \ln (1-\rho)$. Since $T=1$ as mentioned above, $\frac{d s_{\text {equil }}(\rho)}{d \rho}=-\mu$. The equilibrium structure factor is easily seen to be a constant $g_{\text {equil }}(r)=\rho^{2}$ : indeed, one main advantage of this model is that it is particularly easy to compare small deviations from $g_{\text {equil }}(r)$, a notoriously difficult task in glassy systems.

(iii) Finally, we obtain Edwards' measure results as follows: we introduce an "auxiliary model" in which particles have energy equal to one if the dynamic rule of the original model would allow them to move, and to zero otherwise. Performing simulated annealing of the auxiliary model at a fixed number of particles is an efficient way to sample over the configurations with vanishing fraction of moving particles the Edwards' ensemble structure function $g_{\mathrm{edw}}(r)$, and to obtain (Fig. 1) $S_{\mathrm{edw}}(\rho)$ as the logarithm of the number of such configurations by thermodynamic integration of the energy of the auxiliary model with respect to its temperature. We then compute $T_{\mathrm{edw}}^{-1}=-\frac{1}{\mu} \frac{d s_{\mathrm{edw}}(\rho)}{d \rho}$.

We are now in a position to compare the long-time results of the out of equilibrium dynamics (i) with those obtained with measures (ii) and (iii). Figure 2 shows a plot of the mobility $\chi\left(t, t_{w}\right)=\frac{1}{3 N} \sum_{a=1}^{3} \sum_{k=1}^{N} \times \frac{\delta\left\langle\left(r_{k}^{a}(t)-r_{k}^{a}\left(t_{w}\right)\right)\right\rangle}{\delta f}$ vs the mean square displacement $B\left(t, t_{w}\right)=\frac{1}{3 N} \sum_{a=1}^{3} \sum_{k=1}^{N}\left\langle\left(r_{k}^{a}(t)-r_{k}^{a}\left(t_{w}\right)\right)^{2}\right\rangle$, testing in the compaction data the existence of a dynamical temperature $T_{\text {dyn }}$ [24]. ( $N$ is the number of particles and $a$ runs over the spatial dimensions.)

The agreement between $T_{\text {dyn }}$ and the Edwards' temperature $T_{\text {edw }}$, obtained from the blocked configurations as in Fig. 1, is clearly excellent.

![](./images/814601219048734720_1.jpg)

FIG. 1. Gibbs' and Edwards' entropies per particle of the Kob-Andersen model vs density. At high enough density the curves are indistinguishable, and join exactly only at $\rho=1$. The slope of the tangent to $s_{\mathrm{edw}}(\rho)$ for a generic $\rho$ allows one to extract $T_{\mathrm{edw}}(\rho)$ from the relation $\frac{d s_{\mathrm{edw}}}{d \rho}=\frac{1}{T_{\mathrm{edw}}(\rho)} \frac{d s_{\text {equil }}}{d \rho}$.

![](./images/814601219048734720_2.jpg)

FIG. 2. Einstein relation in the Kob-Andersen model: plot of the mobility $\chi(t,t_w)$ vs the mean-square displacement $B(t,t_w)$. The slope of the full straight line corresponds to the equilibrium temperature ($T=1$), and the slope of the dashed one to Edwards' prescription obtained from Fig. 1 at $\rho(t_w)=0.848$.

In Fig. 3 we plot (i) the long-time dynamic $g_{\text{dyn}}(r,t)$, (ii) the equilibrium $g_{\text{equil}}(r)=\rho^2$, and (iii) the Edwards' $g_{\text{edw}}(r)$ structure factors. The agreement between (i) and (iii) is good.

From the results shown so far, a picture emerges where the Edwards' measure is able to correctly reproduce the sampling of the phase space generated by the out of equilibrium dynamics of this non-mean-field model. We have found, however, that at short times or for excessively fast compressions, the quality of the agreement becomes worse, possibly due to heterogeneities. We refer to a longer, more technical paper for a discussion of these issues, as well as a study of other models (in particular the so-called Tetris model [25] for which one recovers the same conclusions as for the KA model) and more technical details on our numerical methods [26].

As already mentioned, Edwards' construction can be inappropriate for certain models, even though they may have a logarithmically slow dynamics. As a representative example of this we consider the low temperature domain growth dynamics of a 3D Ising model in a weak random magnetic field, a model relevant to many physical problems [27]. At large times the domain walls are pinned by the field, and the dynamics proceeds by thermal activation. The mean energy decreases slowly towards the ground state energy. In a large system, the long-time configurations are made of domains of "up" and "down" spins having similar volumes, the global magnetization being zero. This is quite different from the equilibrium configurations at the same energy, which are instead magnetized (since the energy is near the ground state energy).

The question in the present context is therefore whether a long-time configuration of (low) energy $E_0$ is well reproduced by the typical "blocked" configuration of the same energy. By simulating the corresponding "auxiliary" model (with auxiliary energy equal to the number of spins not aligned with their local field, i.e., the number of "mobile" spins), we have checked that this is not the case: the blocked configurations constituting Edwards' distribution at energy $E_0$ are also magnetized. Therefore, neither Gibbs' nor Edwards' distributions describe the typical configurations obtained dynamically.

When is, then, the flatness assumption characterizing Edwards' argument justified? A natural criterion, suggested by glass theory [14,28-30], consists of studying how a system explores its phase space, i.e., its "chaoticity" properties. After aging for a time $t_w$, two copies (clones) are made of the system, and allowed to evolve subsequently with different realizations of the randomness in the updating procedure. We have checked that in the KA model the two clones always diverge (the slower the larger $t_w$: see Fig. 4), while for the 3D random field Ising model they do not. It is thus tempting to conjecture that this form of chaoticity is a necessary condition to have flat statistical weights for the blocked configurations. Note that for this criterion to make sense, it should always be applied at nonzero (though weak) tapping or shearing. The condition of chaoticity is, however, not sufficient: Bouchaud's "trap model" [9] is chaotic, but its fluctuation-dissipation properties are not directly related to the density of states.

To summarize, our study suggests that the proposal made by Edwards does indeed make sense and opens a door towards a statistical (thermodynamic) description of compact granular matter under very weak driving. In order to generalize these ideas to stronger forcing, lower

![](./images/814601219048734720_3.jpg)

FIG. 3. Structure functions $g(r)-\rho^2$ at density $\rho\simeq0.87$ computed with the equilibrium, Edwards' and dynamical measure of the Kob-Andersen model. The three sets of data come from independent Monte Carlo simulations. The dynamic structure function (circles) is obtained after slow compression raising the chemical potential continuously from $\mu=1$ to $\mu=3$ in $10^6$ Monte Carlo sweeps. The Edwards' structure function (open squares) is obtained from the auxiliary model. Although the equilibrium value of $g(r)-\rho^2$ is exactly 0, we also obtain it by a Monte Carlo simulation (full squares) in order to show that the difference in the short distance behavior is not an artifact of the numerical simulation. The size of the typical error bar on dynamical data is shown at $r=3$.

![](./images/814601219048734720_4.jpg)

FIG. 4. Mean overlap $Q_{t_w}(t)$ between two clones in the KA model: the two clones are separated at $t_w$ and evolve subsequently with different noises. $Q_{t_w}(t)$ always decreases to zero (the slower the larger $t_w$), showing that the clones always diverge.

chemical potential, or higher temperatures (as required to analyze the experiments in [31]), one has to learn how to go from the concept of "blocked configuration" to that of "metastable state," and this requires other tools [32]. The inherent structure construction could provide a practical shortcut.

The present setting of the problem immediately sug- gests experiments to check these ideas, e.g., by study- ing diffusion and mobility of tracer particles within driven granular media.

Finally, let us note that even in the simplest cases the correspondence between Edwards' distribution and long- time dynamics is at best checked but does not follow from any principle. The situation is thus as if one would have checked that the microcanonical distribution gives good results for gases, without knowing Liouville's theorem that proves that such a distribution is indeed left invariant by the equations of motion. Such more refined arguments would be very welcome.

M. S. is supported by the European Commission (Con- tract No. ERBFMBICT983561). This work has also been partially supported from the European Network-Fractals under Contract No. FMRXCT980183.

*Unité Mixte de Recherche UMR 8627.

[1] S. F. Edwards, in Granular Matter: An Interdisciplinary Approach, edited by A. Mehta (Springer-Verlag, New York, 1994), and references therein.

[2] A. Mehta, R.J. Needs, and S. Dattagupta, J. Stat. Phys. 68, 1131 (1992).

[3] R. Monasson and O. Pouliquen, Physica (Amsterdam) 236A, 395 (1997).

[4] See, for example, L. C. E. Struik, Physical Aging in Amor- phous Polymers and Other Materials (Elsevier, Houston, 1978), Chap. 7.

[5] H. M. Jaeger and S. R. Nagel, Science 255, 1523 (1992).

[6] H. M. Jaeger, S. R. Nagel, and R. P. Behringer, Rev. Mod. Phys. 68, 1259 (1996).

[7] T. R. Kirkpatrick and D. Thirumalai, Phys. Rev. B 36, 5388 (1987).

[8] T. R. Kirkpatrick and P. Wolynes, Phys. Rev. A 35, 3072 (1987).

[9] J.-P. Bouchaud, L. F. Cugliandolo, J. Kurchan, and M. Mézard, in Spin Glasses and Random Fields, edited by A. P. Young (World Scientific, Singapore, 1997).

[10] L. F. Cugliandolo, J. Kurchan, and L. Peliti, Phys. Rev. E 55, 3898 (1997).

[11] R. Monasson, Phys. Rev. Lett. 75, 2847 (1995).

[12] J. Kurchan, in Proceedings of the Conference on Jamming and Rheology: Constrained Dynamics on Microscopic and Macroscopic Scales, 1997, edited by S. F. Edwards, A. Liu, and S. R. Nagel (cond-mat/9812347, to be pub-lished); http://www.itp.ucsb.edu/online/jamming2/

[13] Th. M. Nieuwenhuizen, Phys. Rev. E 61, 267 (2000).

[14] S. Franz and M. A. Virasoro, J. Phys. A 33, 891 (2000).

[15] A. Crisanti and F. Ritort, cond-mat/9911226.

[16] J. Kurchan, J. Phys. Condens. Matter 12, 6611 (2000).

[17] W. Kob, F. Sciortino, and P. Tartaglia, Europhys. Lett. 49, 590 (2000).

[18] P. H. Stillinger and T. A. Weber, Science 225, 983 (1984).

[19] G. Biroli and R. Monasson, Europhys. Lett. 50, 155 (2000).

[20] A. Crisanti, F. Ritort, A Rocco, and M. Sellitto, cond-mat/0006045.

[21] W. Kob and H. C. Andersen, Phys. Rev. E 48, 4364 (1993).

[22] J. Kurchan, L. Peliti, and M. Sellitto, Europhys. Lett. 39, 365 (1997).

[23] M. Sellitto and J.J. Arenzon, cond-mat/0006146 (to be published).

[24] M. Sellitto, Eur. J. Phys. B 4, 135 (1998).

[25] E. Caglioti, V. Loreto, H. J. Herrmann, and M. Nicodemi, Phys. Rev. Lett. 79, 1575 (1997).

[26] A. Barrat, J. Kurchan, V. Loreto, and M. Sellitto (to be published).

[27] T. Nattermann, in Spin-Glasses and Random Fields, edited by A. P. Young (World Scientific, Singapore, 1997).

[28] A. Baldassarri, Tesi di Laurea, Università degli Studi di Roma "La Sapienza," 1995.

[29] L. F. Cugliandolo and D. S. Dean, J. Phys. A 28, 4213 (1995).

[30] A. Barrat, R. Burioni, and M. Mézard, J. Phys. A 29, 1311 (1996).

[31] E. Nowak, J. Knight, E. Ben-Naim, H. Jaeger, and S. R. Nagel, Phys. Rev. E 57, 1971 (1998).

[32] G. Biroli and J. Kurchan, cond-mat/0005499.