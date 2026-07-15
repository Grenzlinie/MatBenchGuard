# Monte Carlo studies of nonequilibrium phonon effects in polar semiconductors and quantum wells. II. Non-Ohmic transport in $n$-type gallium arsenide

M. Rieger and P. Kocevar
Institut für Theoretische Physik, Universität Graz, Universitätsplatz 5, A-8010 Graz, Austria

P. Lugli
Dipartimento di Ingegneria Meccanica, Seconda Università degli Studi di Roma, Tor Vergata, via Orazio Raimondo, I-00173 Roma, Italy

P. Bordone and L. Reggiani
Dipartimento di Fisica e Centro Interuniversitario di Struttura della Materia dell'Università degli Studi di Modena, via Campi 213/A, I-41100 Modena, Italy

S. M. Goodnick
Center for Advanced Materials Research, Oregon State University, Corvallis, Oregon 97331

(Received 11 October 1988)

Effects of LO-phonon disturbances on the transient and steady-state high-dc-field response of $n$-type gallium arsenide are studied by implementing the simulation of nonequilibrium phonon distributions into the conventional Monte Carlo algorithms for hot-carrier transport in semiconductors. Strong LO-phonon amplification is found for the whole range of fields, carrier densities, and temperatures of interest. At room temperature the phonon disturbances lead to enhancements of up to 20% of the steady-state velocity at low fields and to reductions of up to 10% for fields around and above the maximum of the velocity-field characteristics. However, detailed phase-space restrictions for LO-phonon reabsorption prevent a noticeable interference of the phonon buildup with the transient velocity overshoot.

## I. INTRODUCTION

Since the early days of modern solid-state theory, phonon disturbances have been discussed in connection with fundamental aspects of charge transport. Peierls $^{1}$ and later Klemens $^{2}$ recognized their importance and, in particular, the essential role of nonelectronic relaxation processes of the nonequilibrium phonons for the establishment of a steady state of the coupled carrier-phonon system in the presence of a dc electric field. Contributions of mutual drag effects between carriers and phonons to the electrical and thermal conductivity and to the thermopower of semiconductors were first estimated by Sondheimer $^{3}$ and Parrot, $^{4}$ who also pointed out that the neglect of phonon disturbances in the calculation of electronic transport coefficients leads to a violation of the Kelvin relations. It is interesting to note that even in the Ohmic case any drag effect of nonequilibrium phonons on the electrons introduces nonlinear current-field characteristics. This non-Ohmic behavior arises from the fact that the phonon distributions, and therefore the rates for carrier-phonon scattering, become field dependent, in contrast to the linear-response concept of field-independent electronic mobilities. But the most practical aspects of phonon disturbances concern the nonlinear-response phenomena connected with high-field transport and laser-pulse excitation of semiconductors.

Because of the weak carrier-phonon couplings and of the rapid increase of the thermalization rate of acoustic modes with temperature, possible mobility effects of acoustic-phonon disturbances are restricted to the lattice temperatures of at most a few degrees kelvin. At these temperatures, the great difficulties in the treatment of the dominant ionized-impurity scattering overshadow the question of possible nonequilibrium phonon effects on the theoretical carrier mobilities, but phonon-drag-induced increases of the mobility by more than 20% have been found in simple $^{5}$ as well as more refined $^{6}$ model calculations.

In contrast to the acoustic case, the dependence (i.e., increase) of the thermalization rates of optical phonons with temperature is only weak. Although these rates are very fast, of the order of inverse picoseconds, the strong polar-optical-carrier-LO-phonon coupling in polar materials can lead to even faster emission rates of phonons by the carriers, and therefore to substantial LO-phonon amplification even at room temperature. A first theoretical estimate of such effects was made for $n$-type InSb, predicting small transient modifications of the carrier mobility due to the LO-phonon amplification. $^{7}$

Practically the most interesting candidate among the standard semiconductors for noticeable mobility effects of nonequilibrium LO phonons is $n$-type GaAs, where the time constants for valley transfer and for the generally expected ensuing velocity overshoot are again in the picosecond range and, therefore, comparable to the above-discussed time constants for the development of phonon disturbances. Since the phonon amplification acts back


on the carrier distribution and modifies the carrier popu- lations of the different valleys, the question arises wheth- er there might be interference effects between the phonon buildup and the performance of high-speed GaAs devices designed to work in the velocity-overshoot regime.

A recently reported calculation $^{8}$ provided a first step towards a quantitative estimate of such transient none- quilibrium phonon effects in GaAs by implementing pho- non disturbances into the conventional heated-displaced- Maxwellian (HDM) carrier models of nonlinear trans- port.

The physical model used in this preceding study as well as in the present study consists of electrons in isotropic and parabolic $\Gamma$ and $L$ conduction-band minima with the standard electron-phonon couplings: polar optical, ine- quivalent and equivalent intervalley, acoustic deforma- tion potential, optical deformation potential (in the $L$ val leys), and ionized-impurity scattering. The model as- sumes spatial homogeneity, but, due to the negligible LO-phonon diffusion, it would allow later applications to a coarse-grained and therefore locally homogeneous description of space-dependent carrier transport in de- vices.

The results of the HDM study can be summarized as follows.

When the upper $L$ valleys are neglected, the nonequili brium phonons induce a collective breakdown within the typical field and time range of the overshoot effect in the actual many-valley band structure. The breakdown is caused by a LO-phonon avalanche through a "phononČerenkov" mechanism (i.e., the mean carrier drift veloci- ty must exceed the phase velocity of the phonons) and re- quires a sufficiently high carrier concentration of strongly drifting carriers. $^{9}$ As the mathematical resonance condi tion is a consequence of the HDM distribution of the car-riers, the model dependence of this prediction is obvious; however, a Čerenkov-like phonon amplification should be expected whenever the actual carrier distribution is of the form of a sufficiently drifted HDM.

For the realistic many-valley band structure it turns out that the loss of fast-drifting $\Gamma$ electrons through transfer into the "slow" $L$ valleys suffices to stop the above-mentioned single-valley breakdown and to ensure the establishment of an asymptotic steady state at arbi- trary fields. Carrier drag by the initially amplified for- ward phonons dominates at fields below the onset of val- ley transfer and increases the mean steady-state drift ve- locity $v$. For higher fields $v$ is reduced, because the re duced cooling efficiency of the "hot" LO phonons leads to a higher $\Gamma$-valley temperature and therefore to a higher population of the $L$ valleys of lower mobility. Moreover, with increasing fields the higher number of carrier interactions with randomly oriented LO phonons soon outweighs the drag effect of the forward modes and acts to reduce even the $\Gamma$-valley mobility (for a similar effect with acoustic-phonon disturbances in low- temperature transport, see Ref. 5). Both the drag- and heating-induced corrections amount to more than $20 \%$ at the highest investigated carrier concentrations (several $10^{17} \mathrm{~cm}^{-3}$).

In these calculations, the integration of the time- dependent Boltzmann equation for the phonon distribu- tion functions was performed in parallel to the number, energy, and momentum balance for the HDM electrons in the $\Gamma$ and $L$ valleys for the momentary phonon distri bution, implying an instantaneous adaptation of the car- riers to any change in the phonon population. However, besides the well-known HDM requirement of an extreme- ly fast internal carrier thermalization, such a complete enslavement of the carriers by the LO phonons would only be justified if the energy and momentum relaxation rates of the carrier system as a whole were much larger than the rate of change of the LO-phonon distribution. The condition is well fulfilled for the dominant polar- optical-electron-LO-phonon coupling and was therefore sufficient for the investigation of the eventual approach to a steady state and corresponding stabilization of the carrier-phonon system, in agreement with the experimen- tal evidence against a collective electrical breakdown in n-type GaAs. But the model did not allow a detailed esti- mate of the initial transient, and especially of the overshoot phenomenon, where the comparable time scales for the $\Gamma-L$ valley transfer and the LO-phonon buildup require a treatment of the time evolution of both carriers and phonons on the same footing.

So three questions remained.

(i) Would a rapid initial phonon heating and the ensu- ing rise of the mean energy of the $\Gamma$ electrons lead to an accelerated $\Gamma-L$ transfer, and thereby to a reduction of the overshoot through the earlier bend down of the mean carrier velocity?

(ii) Would this earlier onset of the transfer very soon reduce the number of fast-drifting $\Gamma$ electrons below its threshold value for strong LO-phonon amplification? In this case the phonon avalanche would be automatically quenched in its initial stages and nonequilibrium phonon effects kept low.

(iii) What is the role the model-distribution functions for the carriers play in describing a coupled electron- phonon system?

The present study was set up to clarify these points within the model-free approach of implementing none- quilibrium phonon distributions into a conventional en- semble Monte Carlo simulation of electron transport and to apply the novel code to a fully-time-dependent calcula- tion of the hot-carrier response in $n$-type GaAs in the transient overshoot regime at room temperature and at77 K. Preliminary results have been presented in Ref. 10.

## II. THE TRANSPORT MODEL

### A. The Monte Carlo algorithm

To incorporate phonon disturbances into Monte Carlo simulations of time-dependent non-Ohmic dc transport, we extend our previous work on the simpler case of iso- tropic phonon amplification during the energy relaxation of highly photoexcited carriers. $^{11}$ To this end the (spa tially homogeneous) Boltzmann equation for each pho- non branch of interest (like the LO-phonon branch in our applications)

$$
\frac{\partial N(\mathbf{q}, t)}{\partial t}=\left.\frac{\partial N(\mathbf{q}, t)}{\partial t}\right|_{\mathrm{ph}-e}+\left.\frac{\partial N(\mathbf{q}, t)}{\partial t}\right|_{\mathrm{ph}-\mathrm{ph}}
\tag{1}
$$
is discretized in both the phonon wave vector $\mathbf{q}$ and in time by introducing appropriately chosen q-space cells $\Delta \Omega_{\mathbf{q}}$ and time intervals $\Delta t$.

The resulting time evolution of the phonon distribution function $N$ during the $j$ th time interval $(\Delta t)_{j}$ of the Monte Carlo simulation is
$$
\begin{aligned}
N(\mathbf{q}, j \Delta t)= & N(\mathbf{q},(j-1) \Delta t)+\left.\delta N\left(\mathbf{q},(\Delta t)_{j}\right)\right|_{\mathrm{ph}-e} \\
& +\left.\delta N\left(\mathbf{q},(\Delta t)_{j}\right)\right|_{\mathrm{ph}-\mathrm{ph}}, \quad j=1,2,3, \ldots
\end{aligned}
\tag{2}
$$
and contains the contributions of phonon-electron (ph-e) and phonon-phonon (ph-ph) processes.

The $\mathbf{q}$ cells are obtained by discretizing $q(\equiv|\mathbf{q}|)$ and $\cos \theta$, with $\theta$ the angle between $\mathbf{q}$ and the electrical field $\mathbf{F}$. The corresponding cylindrical symmetry about $\mathbf{F}$ requires carriers in isotropic band minima, a reasonable assumption for the polar materials of our present concern.

Equally spaced intervals were chosen for $\cos \theta$ between -1 and +1 , and for $|\mathbf{q}|$ between $q_{\min }(=0)$ and $q_{\max }$. As the polar-optical-electron-LO-phonon coupling favors small $q$ values, it is easy to find an upper limit $q_{\max }$, which is very seldomly surpassed during the simulations. In our calculations $q_{\max }$ was chosen between $1.5 \times 10^{7}$ and $3.0 \times 10^{7} \mathrm{~cm}^{-1}$. The number of $q$ intervals was typically of the order of 100 and the number of $\cos \theta$ intervals of the order of 10.

The implementation of the nonequilibrium phonon distributions into a conventional ensemble Monte Carlo algorithm $^{12}$ now proceeds in three steps [(i)-(iii)].

(i) ph- $e$ scattering. To follow the time evolution of the phonon population, a mesh $N\left(\mathbf{q}_{i}, t\right)$ and a histogram $H\left(\mathbf{q}_{i}, t\right)$ are set up within the $(q, \cos \theta)$ grid, with $i$ the cell index. The simulation is started for a still-vanishing field with $H\left(\mathbf{q}_{i}, 0\right)=0$ and $N\left(\mathbf{q}_{i}, 0\right)=N_{\mathrm{LO}}$ in each cell. Under the reasonble assumption of dispersionless LO phonons the thermal equilibrium Planck distribution, $N_{\mathrm{LO}}$ is a $\mathbf{q}$ independent constant. During the simulation each emission or absorption of a phonon, whose wave vector falls into cell $i$, changes the histogram by $\Delta H\left(\mathbf{q}_{i}, t_{c}\right)= \pm 1$, with $t_{c}$ the time instant of the collision process. The few events with $q>q_{\max }$ are, without noticeable effect on the scattering statistics, either added to the highest cell (for $q_{\max }$ ) or neglected.

Any change $\Delta H$ is transferred to the phonon distribution function by scaling the histogram with respect to the actual (fine-grained) number of $\mathbf{q}$ points in each cell and with respect to the ratio of the actual number and the simulated number $N_{\text {sim }}$ of carriers:
$$
\left.\Delta N\left(\mathbf{q}, t_{c}\right)\right|_{\mathrm{ph}-e}=\frac{(2 \pi)^{3}}{\Delta \Omega_{\mathbf{q}}} \frac{n_{e}}{N_{\text {sim }}} \Delta H\left(\mathbf{q}, t_{c}\right),
\tag{3}
$$
where $n_{e}$ is the actual electron density. In terms of its upper and lower limits in the $(q, \cos \theta)$ grid, the volume of the $\mathbf{q}$ cell is given by
$$
\Delta \Omega_{\mathbf{q}}=\frac{2 \pi}{3}\left(q_{u}^{3}-q_{l}^{3}\right)\left(\cos \theta_{u}-\cos \theta_{l}\right).
\tag{4}
$$

So the electronic contribution to Eq. (2) is obtained by summing Eq. (3) over all scattering events within the time interval $(\Delta t)_{j}$ :
$$
\left.\delta N\left(\mathbf{q},(\Delta t)_{j}\right)\right|_{\mathrm{ph}-e}=\sum_{t_{c} \in(\Delta t)_{j}}\left.\Delta N\left(\mathbf{q}, t_{c}\right)\right|_{\mathrm{ph}-e}.
\tag{5}
$$

As for each "subhistory" $\Delta t$, the ensemble Monte Carlo technique requires the sequential simulation of one carrier after the other; our prescription of updating $N(\mathbf{q}, t)$ after each $e$-ph scattering event in the numerical procedure does not preserve the actual time sequence of the phonon processes in the ensemble. However, by choosing $\Delta t$ to be much shorter (of the order of a few $10^{-14} \mathrm{~s}$ ) than the mean $e$-ph scattering time, one can guarantee that during each subhistory all carriers find nearly the same phonon distribution and, therefore, practically identical phonon scattering probabilities.

(ii) Nonelectronic phonon losses. To account for the nonelectronic phonon processes, the simulated $N(\mathbf{q}, t)$ is being updated at the end of each subhistory $\Delta t$ by $\left.\partial N / \partial t\right|_{\text {ph-ph }} \Delta t$ and, using the relaxation-time ansatz, implemented into Eq. (2) through
$$
\left.\delta N\left(\mathbf{q},(\Delta t)_{j}\right)\right|_{\mathrm{ph}-\mathrm{ph}}=-\frac{N(\mathbf{q},(j-1) \Delta t)+\left.\delta N\left(\mathbf{q},(\Delta t)_{j}\right)\right|_{\mathrm{ph}-e} N_{\mathrm{LO}}}{\tau_{\mathrm{LO}}}(\Delta t)_{j}.
\tag{6}
$$

Here the experimentally determined LO-phonon lifetime $\tau_{\mathrm{LO}}$ is extrapolated to the high lattice temperatures of our study through the spectroscopically fitted two-channel-decay formula $^{13,14}$
$$
\tau_{\mathrm{LO}}\left(T_{L}\right)=\frac{\tau_{\mathrm{LO}}^{0}}{1+\left[\exp \left(\frac{0.65 \hbar \omega_{\mathrm{LO}}}{k_{B} T_{L}}\right)-1\right]^{-1}+\left[\exp \left(\frac{0.35 \hbar \omega_{\mathrm{LO}}}{k_{B} T_{L}}\right)-1\right]^{-1}},
\tag{7}
$$
where $\tau_{\mathrm{LO}}^{0}=\lim _{T_{L} \rightarrow 0} \tau_{\mathrm{LO}}\left(T_{L}\right)$. The use of such a "singlemode" relaxation towards the thermal equilibrium distribution is well justified, because the thermalization of long-wavelength optical phonons is dominated by decays into pairs of zone-boundary phonons with negligible coupling to the carriers. As this second phonon generation in turn rapidly decays into the thermal reservoir of the low-lying acoustic lattice modes, the whole phonon cascade acts as a perfect sink of energy and momentum for the coupled carrier-LO-phonon system, at least for the picosecond time scale of our study for which any latticeheating effects are completely negligible. $^{8}$

As typical LO-phonon lifetimes $\tau_{\text{LO}}$ are of the order of several ps, our above choice of much shorter subhistories $\Delta t$ again ensures that the actual time change of $N(\mathbf{q}, t)$ due to lattice losses is well approximated by our updating procedure.

(iii) Selection of the final state. To make the novel algorithm computationally tractable, the total carrier- LO-phonon scattering probabilities are analytically calculated for an artificially high $\mathbf{q}$-independent $N_{\max }$ in place of the actual $N(\mathbf{q}, t)$ obtained from (i) and (ii). If a scattering has in this way been selected, its final state is determined as usual, $^{15}$ except for a rejection technique which compares the maximized differential scattering rate for $N_{\max }$ with the rate for $N(\mathbf{q}, t)$. The scatterings induced by the difference $N_{\max }-N(\mathbf{q}, t)$ are treated as self-scatterings. This method works for arbitrary time variations of $N(\mathbf{q}, t)$, as long as $N_{\max }$ remains an upper limit.

The implementation [(i)-(iii)] of time-varying phonon distributions within the conventional ensemble Monte Carlo technique provides a novel algorithm which is free of adjustable parameters. The method is easily extendable to more refined numerical treatment-such as the use of interpolation schemes with respect to the discretization in $\mathbf{q}$ and $t$-and to nonequilibrium carrier-phonon systems other than the electron-LO-phonon system of the present work.

### B. Physical parameters

To allow a better comparison of our results with earlier work for phonon equilibrium, the material parameters for this analysis were taken from the standard Monte Carlo study of $n$-type GaAs by Littlejohn $e t$ al. $^{16}$ Two types of conduction-band valleys ( $\Gamma$ and $L$ ) were considered. Besides the polar-optical-electron-LO-phonon interaction, ionized-impurity $(i-i)$ scattering and the deformation potential couplings of the electrons to intervalley, acoustic, and (for $L$ electrons) optical phonons were taken into account. As mentioned already, acoustic-phonon disturbances are negligible at the high temperatures of our present concern. The intervalley phonons were also assumed to be in equilibrium, since their disturbance is partitioned over large regions of $\mathbf{q}$ space. $^{17}$ The LO phonons and the ionized-impurity potentials were statically free-carrier screened. Because of its dependence on the time-changing concentrations and mean energies of the electrons in the different types of valleys, the corresponding Debye-screening parameter was simultaneously updated with the LO-phonon distributions at the end of each subhistory $\Delta t .^{18}$

Since several choices of $\Gamma-L$ intervalley deformation potentials were tried in Ref. 16, we finally used $0.85 \times 10^{9}$ $\mathrm{eV} / \mathrm{cm}$ instead of Littlejohn's favorite value of $1 \times 10^{9}$ $\mathrm{eV} / \mathrm{cm}$, in better agreement with more recent estimates. $^{19}$

All calculations were performed for lattice temperatures of 77 and $300 \mathrm{~K}$. As suggested by the earlier HDM analysis and confirmed by the present study, substantial LO-phonon disturbances require sufficiently high carrier densities, typically above $n_{e}=10^{16} \mathrm{~cm}^{-3}$. However, for noticeable nonequilibrium phonon effects on the carrier mobility, one has to expect some upper limit to $n_{e}$, above which the polar-optical couplings would be effectively screened out by the free carriers. In recent calculations of hot-phonon effects in highly photoexcited GaAs, $^{9}$ such an upper limit was found around a carrier density of $10^{20}$ $\mathrm{cm}^{-3}$. Moreover, for high doping, typically above $n_{i}=10^{19} \mathrm{~cm}^{-3}$, the carrier mobility becomes so strongly dominated and reduced by $i-i$ scattering that nonequilibrium phonon effects become negligible. For these reasons our following studies of uncompensated material were restricted to carrier and impurity concentrations between $10^{16}$ and $10^{19} \mathrm{~cm}^{-3}$, with the main emphasis on the technologically interesting range of moderately high doping between $1 \times 10^{17}$ and $5 \times 10^{17} \mathrm{~cm}^{-3}$.

As of particular interest for future device applications in GaAs-based heterojunction or superlattice structures, the case of "remote ionized-impurity scattering" $^{20}$ was approximated in our bulk model by simulation of a high carrier density $\left(n_{e}=3 \times 10^{17} \mathrm{~cm}^{-3}\right)$ in the presence of a negligible (residual) impurity concentration of $n_{i}=3$ $\times 10^{12} \mathrm{~cm}^{-3}$.

---

## III. RESULTS AND DISCUSSION

### A. Single-valley effects

To study the consequences of perturbed LO phonons for the mobility and mean carrier energy $E_{\Gamma}$ of the $\Gamma$-valley electrons without the interference of intervalley scattering, one has to keep the electrical field $F$ below the threshold (of $3-4 \mathrm{kV} / \mathrm{cm}$ for noticeable electron transfer to the higher $L$ minima. Figures $1-3$, showing the results of a simulation for $F=2 \mathrm{kV} / \mathrm{cm}, n_{e}=n_{i}=2 \times 10^{17}$ $\mathrm{cm}^{-3}$, and $T_{L}=300 \mathrm{~K}$, contain all the essential single-valley effects of the phonon disturbances. Starting from a (Maxwellian) thermal equilibrium distribution of elec-

![](./images/812741332278706176_1.jpg)

FIG. 1. Mean electron drift velocity as function of time with $(\tau_{\text{LO}}^{0}=9$ ps) and without $(\tau_{\text{LO}}^{0}=0)$ LO-phonon disturbances.

![](./images/812741332278706176_2.jpg)

FIG. 2. Mean electron energy in the $\Gamma$ valley as function of time with $(\tau_{\mathrm{LO}}^{0}=9 \mathrm{ps})$ and without $(\tau_{\mathrm{LO}}^{0}=0)$ LO-phonon disturbances.

trons (all in the $\Gamma$ valley), $10^{4}$ electrons were simulated over a time span of 40 ps after the onset of the field pulse; in fact, 10 ps were sufficient for the establishment of a steady state, at least within our numerical standard devia- tions. The length of the subhistories $\Delta t$ was $2.5 \times 10^{-14} \mathrm{~s}$. The onset of the electrical field $F$ was taken as linear within $5 \times 10^{-14} \mathrm{~s}$ and accordingly taken as $1 \mathrm{kV} / \mathrm{cm}$ dur ing the first subhistory. Variation of the detailed shape of $F(t)$ during such a short risetime was found to have no noticeable influence on the later time evolution of the en- semble, in accord with the general assumption of an abrupt field step in most transport studies of transient carrier response in bulk material. $^{21}$

Dividing the ensemble into ten subensembles of $10^{3}$ carriers gave standard deviations of $4-6 \%$ for the mean drift velocity and $2-5 \%$ for the mean carrier energy per valley, as long as the relative valley population exceeded30%.

Figures 1 and 2 show the time evolution of the mean drift velocity $v$ and of the mean electron energy $E_{\Gamma}$ in the $\Gamma$ valley as obtained for phonon equilibrium $(\tau_{LO}^{0}=0$ , solid lines) and disturbed phonons $(\tau_{LO}^{0}=9 ps$ , dashed lines), respectively. The two major effects of the phonon disturbances are clearly displayed: a significant increase in $v$ and $E_{\Gamma}$ , showing, the drag of the carriers by the most strongly amplified (i.e., forward) pho- nons and the reduced cooling of the carriers by the hot phonons.

The time evolution of the forward distribution $N$ (q,cos =-1) is shown separately in Fig. 3. The distribu- tion, which quite generally is found to have its most pro- nounced amplification along this forward direction $(\| v)$ , is seen to approach a final steady-state peak value of 1.4, a substantial increase over the thermal equilibrium value of 0.34. The decrease of the magnitude $q_{p}$ of the wave vector for maximum phonon amplification with time is in agreement with the increase of $E_{\Gamma}$ and the concomitant population of higher (i.e., steeper) band regions. In this way a pronounced low- $q$ peak develops in $N(q)$ , with a cutoff of the phonon amplification at the lowest $q$ values due to energy and momentum conservation per electron-LO-phonon process and due to the (static) free- carrier screening of the polar-optical couplings. Especial- ly at higher fields this low- $q$ peak is further accentuated by the accumulation of $\Gamma$ -valley electrons at energies just below the valley-transfer threshold $\Delta_{\Gamma L}$ .

Although qualitatively we can ascribe the higher car- rier energies in the presence of nonequilibrium phonon distributions to the reduced cooling efficiency of a hot- phonon system, a more-detailed phase-space analysis is necessary to see why the effects of the LO-phonon distur- bances in the present low-field case are more pronounced than in the high-field cases of Sec. III B. For this purpose we combine a q-space analysis of the amplified phonons with the information about the carrier distribution func- tion $f(E)$ obtained from our simulation. Figure 4 shows

![](./images/812741332278706176_3.jpg)

FIG. 3. Forward LO-phonon distribution function at two different times.

![](./images/812741332278706176_4.jpg)

FIG. 4. Phase-space diagram for LO-phonon emission and absorption by $\Gamma$ -valley electrons in gallium arsenide.

the magnitude of the minimal phonon wave vectors $q_{emab}^{min}$ allowed by energy and momentum conservation for emis- sion and absorption of a LO phonon by $\Gamma$-valley electron of energy $E$. As polar-optical scatterings are dominated by small $q$ values, the dominant $q$ ranges for emissions and absorptions lie just above these $q^{min}$ curves.

In contrast to thermal equilibrium, with equal rates for phonon emission and absorption, the presence of a dc field causes a relative increase of emissions over absorp- tions to provide the net flow of energy from the external field through the carrier system into the lattice. In the presence of phonon disturbances, the statistical factors for induced emission and for absorption processes in- crease in the same proportion $N_{LO}/N_{LO}^{(0)}$. Therefore, no change in the net energy transfer can be expected from the increased phonon occupancy alone. However, the re- sulting relative increase of the electronic absorption rates is higher, whenever the differential band occupation bythe carriers (the number of electrons per unit energy) $N(E) \propto E^{1 / 2} f(E)$ is peaked below the threshold $E=\hbar \omega_{LO}$  for phonon emission and near the favorable reabsorption range. In this way the relative statistical weight of the absorptions is enhanced and the difference between emis- sion and absorption rates reduced, so that the carriers are "hotter" than in the case of phonon equilibrium. In the following we shall refer to this situation as the net pho- non reabsorption.

Note that most of the reabsorbing electrons will have the (very low) energies picked out by the dominant- coupling regime in Fig. 4 near that part of the $q_{ab}^{min}$ curve which covers the $q$ range $(q_{dist})$ of the phonon disturbance. In our specific case we find from Fig. 3 that $(q_{dist})$  extends from $0.5 \times 10^{6}$ to roughly $10 \times 10^{6} ~cm^{-1}$ and peaks between $0.8 \times 10^{6}$ and $1.5 \times 10^{6} ~cm^{-1}$ . The corre sponding range $(E_{ab})$ of dominant carrier energies forreabsorptions is $0.01-0.07 eV$ , as found from the $q_{ab}^{min}$  curve of Fig. 4. In Fig. 5 the simulated $\Gamma$ -valley occupa tions $N_{\Gamma}(E)$ are plotted for 2 and 10 ps. Indeed, $(E_{ab})$ is centered around the peak region of $N_{\Gamma}$ , with the max imum of $N_{\Gamma}$ at energies below the LO-phonon emission threshold, as required for marked phonon-reabsorption effects.

An interesting question concerns the contribution of ionized-impurity scattering to the nonequilibrium pho- non effects in Figs. 1 and 2. At first site one might expect a reduction of the $i-i$ scattering rate during the reheating of the carriers by the perturbed phonons. However, the general notion of the decrease of the number of scatter- ings with increasing carrier energy only holds for a fixed screening parameter $q_{D}$ . In our cases the quite pro nounced decrease of $q_{D}$ during the phonon buildup even outweighs the decrease of the unscreened scattering cross section, resulting in a slow increase of the number of $i$ -i scatterings (roughly $\propto E_{\Gamma}^{1 / 2}$ ) for high carrier densities. This effect is also well documented in the scattering statistics of our simulations. However, the final effect on the carrier mobility is difficult to estimate, because a de- creased screening induces a stronger forward tendency of each individual $i$ - $i$ scattering, which counteracts the effect of the increased scattering frequency. We have therefore kept track of the partial momentum relaxation rates for phonon and $i$ - $i$ scattering during the simulations and indeed found a slight $(\approx 7 \%)$ increase of the $i$ - $i$  momentum-relaxation rate due to the nonequilibrium phonon-induced reheating of the carriers.

A related question concerns the influence of the screen-ing model. Figures 6 and 7 show our results for $T_{L}=77$  K, as obtained for Debye-screened and -unscreened polar-optical couplings. They confirm the old findings of the carrier-temperature models that screening plays a negligible role in the presence of strong phonon distur- bances. As the use of static screening corresponds to as- suming the maximum possible screening efficiency of the

![](./images/812741332278706176_5.jpg)
FIG. 5. Differential band occupation of $\Gamma$ -valley at two different times.

![](./images/812741332278706176_6.jpg)
FIG. 6. Mean electron drift velocity as function of time with LO-phonon disturbances (dashed line) for both screened and un- screened polar-optical interaction and without LO-phonon dis- turbances for screened and unscreened polar-optical interactionand without LO-phonon disturbances for screened (solid line) and unscreened (dashed-dotted line) polar-optical interaction.

![](./images/812741332278706176_7.jpg)

FIG. 7. Mean electron energy in the $\Gamma$ valley as function of time with LO-phonon disturbances for screened (dashed line) and unscreened (dotted line) polar-optical interaction and without LO-phonon disturbances for screened (solid line) and unscreened (dashed-dotted line) polar-optical interaction.

free carriers, any more detailed dynamic screening model should give results intermediate between the two limiting cases of Debye-screened and -unscreened polar-optical coupling in Figs. 6 and 7. The only exception would be the case of antiscreening $^{22}$ where the results should be expected to extrapolate beyond the no-screening limit in proportion to the increased polar-optical coupling, but again with negligible modifications of $v$.

### B. Many-valley effects: Velocity overshoot
To illustrate the situations where a substantial fraction of electrons has enough energy to be scattered into an $L$ valley we choose a simulation for $F=8$ kV/cm, $n_e=n_i=3\times 10^{17}\ \mathrm{cm}^{-3}$, and $T_L=300$ K. An ensemble of $10^4$ electrons was simulated over a time interval of 20 ps after a stepwise onset of the field pulse, with the same discretization in $\mathfrak{q}$ and $t$ as in the previous examples.

The important difference to the single-valley situation of the preceding subsection is seen in Fig. 8, which shows the relative carrier concentration $n_{\Gamma}/n_e$ in the $\Gamma$ valley (dashed and solid lines) and the mean $\Gamma$-valley energy of the carriers (dotted and dashed-dotted lines), with and without inclusion of phonon disturbances, as functions of time. The higher field results in a sufficient heating of the $\Gamma$ electrons to allow a very rapid onset of intervalley scattering, causing a decrease of the $\Gamma$-valley mobility and a substantial $\Gamma$-$L$ transfer. The consequences of this transfer for the total mean drift velocity are seen in Fig. 9. Here $v(t)$ (dashed and dotted lines) and the mean kinetic energy $E_L$ of the carriers in the $L$ valleys (dotted and dashed-dotted lines) are plotted as function of time, again for disturbed and undisturbed phonons, respectively. Quite generally, it turned out that the phonons took much longer times to reach a steady state than the carriers, whose mean values remained constant after typically 5 ps. The most remarkable feature of the $v(t)$ curves, the velocity overshoot with a peak of $3.7\times 10^7\ \mathrm{cm\ s^{-1}}$ within the first 0.6 ps, is seen to be practically identical for both simulations. After the finding of the strong nonequilibrium-phonon-induced $\Gamma$-valley heating in the preceding example of Sec. III A this result is rather surprising.

![](./images/812741332278706176_8.jpg)

FIG. 8. Mean energy and relative valley population of $\Gamma$-valley electrons as functions of time with $(\tau_{LO}^0=9$ ps) and without $(\tau_{LO}^0=0)$ LO-phonon disturbances.

![](./images/812741332278706176_9.jpg)

FIG. 9. Mean electronic drift velocity and mean energy of $L$-valley electrons with $(\tau_{LO}^0=9$ ps) and without $(\tau_{LO}^0=0)$ LO-phonon disturbances.

Again, it is helpful to follow the time evolution of the LO-phonon disturbances and of the carrier occupation $N(E)$ of the bands. Figure 10 shows the forward phonon distribution obtained at time instants corresponding to the velocity peak (at 0.5 ps), to the maximum amplification of the electronically most active, i.e., the reabsorbable, modes (around 1.3 ps), and to the onset of the steady state (at 20 ps). The error bars are included to demonstrate the increasing statistical fluctuations with decreasing size of the q cells, resulting in substantial numerical uncertainties at the smallest $|q|$ values. However, as seen in the following discussion, the net reabsorption of such long-wavelength LO phonons is of negligible importance for the electronic response, so that these uncertainties have no practical consequences. Most noteworthy, it is seen that the maximum forward $N_{\text{LO}}(\mathbf{q})$ at $t=0.5$ ps is 2.0 and, therefore, already higher than the maximum (steady-state) value in the previous example in Sec. III A (Fig. 3). In spite of this strong and rapid phonon amplification, the mean $\Gamma$-valley energy $E_{\Gamma}$ is still the same as for phonon equilibrium. Therefore, the $\Gamma$- valley population and velocity overshoot remain practically unchanged.

Repeating the phase-space analysis of Sec. III A for the present situation at 0.5 ps, we find a phonon-excitation spectrum similar to the steady-state case in Fig. 3, and therefore nearly the same range $(E_{\text{ab}})$ of favorable carrier energies for net phonon reabsorption. However, the carrier occupation of the $\Gamma$ valley is now much broader, peaking near the threshold for valley transfer and leaving only a small fraction of electrons to the dominant net reabsorption region below $E=\hbar\omega_{\text{LO}}$. As a consequence, the phonon-reabsorption effects for the $\Gamma$ electrons are much less pronounced than in the low-field case, resulting in practically unchanged carrier distributions and explaining the general failure of LO-phonon disturbances to interfere with the valley-transfer dynamics and the ensuing velocity overshoot. The other consequence of the phase-space restrictions for electron-phonon scattering follows from Fig. 4: the low-$q$ peak of $N_{\text{LO}}(\mathbf{q})$ does not contribute to the net phonon-reabsorption effects which are restricted to $q$ values above $1\times 10^{6}\ \text{cm}^{-1}$. This leaves a substantial fraction of the amplified modes with negligible influence on the carrier response.

The decisive difference between the low-field and high-field cases is demonstrated in Fig. 11, where a comparison is made between the final steady-state $\Gamma$-valley occupations with and without phonon disturbances for our two examples of 2 and 8 kV/cm. While at 2 kV/cm a noticeable nonequilibrium phonon-induced depletion of the low-energy part of $N_{\Gamma}(E)$ and a corresponding enhancement of the high-energy part is clearly visible, the high-field distributions are practically identical within the statistical fluctuations of the carrier distributions in spite of the much higher phonon amplification (Fig. 10). As can be seen from the asymptotic range of Figs. 8 and 9, this strong phonon buildup finally results in a slightly increased $E_{\Gamma}$, a corresponding slight reduction of the steady-state $\Gamma$-valley population, and a reduction of the total mean steady-state velocity $v$ of about $6\%$.

A separate analysis of the mean drift velocities $v_{\Gamma}$ and $v_{L}$ in the two types of valleys reveals very small

![](./images/812741332278706176_10.jpg)

FIG. 10. Forward LO-phonon distribution function at three different times.

![](./images/812741332278706176_11.jpg)

FIG. 11. Steady-state differential band occupation of $\Gamma$ valley with $(\tau_{\text{LO}}^{0}=9$ ps) and without $(\tau_{\text{LO}}^{0}=0)$ LO-phonon disturbances for (a) 2 and (b) 8 kV/cm, respectively.

nonequilibrium-phonon effects on $v_{L}$ and a noticeable effect on $v_{\Gamma}$. In contrast to the low-field case, however, $v_{\Gamma}$ is reduced. This change, from a dominant phonon-drag effect at low fields to an increased momentum relaxation through the increased intervalley scattering rate and a frictional hot-phonon effect at high fields, confirms the earlier HDM results $^{8}$ described in Sec. I, despite the very different shape of a HDM band occupation as compared to $N_{\Gamma}(E)$ in Fig. 11(b).

An additional point connected with the effects of phonon drag and heating comes out of the present analysis. Since the majority of carriers is populating the $L$ valleys, most of the phonons are distributed over a larger range of $q$ values with small forward drift, thus destroying the overall drag phenomenon. To further illustrate this transition, we refer to Figs. 12 and 13. Figure 12 shows, besides the results for the steady-state $v$-$F$ characteristics of our uncompensated standard material, the characteristics obtained for "remote $i$-$i$ scattering." In this way it is possible to demonstrate the pure drag or heating regimes without the additional $i$-$i$ effects discussed in Sec. III A. For the still higher mobilities and lower nonelectronic phonon losses of the undoped sample at the lattice temperature of 77 K, the drag regime was not detectable by our simulation, as seen in Fig. 13. The reduction of the drag regime for this case of higher mobility can be ascribed to a more dominant "phonon heating," implying a stronger frictional action of the phonon disturbances.

As a final example for the unexpectedly small interplay of LO-phonon disturbances with the overshoot phenomenon, Fig. 14 shows the time-resolved results for a rather spectacular case of extremely strong LO-phonon amplification, namely again the remote $i$-$i$ scattering case of Fig. 13, but for the higher field of 16 kV/cm.

![](./images/812741332278706176_12.jpg)

FIG. 12. Steady-state velocity-field characteristics with ($\tau_{LO}^{0}$=9 ps) and without ($\tau_{LO}^{0}$=0) LO-phonon disturbances for uncompensated material and for a case of remote ionized-impurity scattering.

![](./images/812741332278706176_13.jpg)

FIG. 13. Steady-state velocity-field characteristics with ($\tau_{LO}^{0}$=9 ps) and without ($\tau_{LO}^{0}$=0) LO-phonon disturbances for a case of remote ionized-impurity scattering.

## IV. SUMMARY AND CONCLUSIONS

The theoretical prediction and strong experimental indication of pronounced effects of LO-phonon disturbances on the energy relaxation of highly laser-excited

![](./images/812741332278706176_14.jpg)

FIG. 14. Mean electronic drift velocity and forward LO-phonon distribution as functions of time with ($\tau_{LO}^{0}$=9 ps) and without ($\tau_{LO}^{0}$=0) LO-phonon disturbances for a case of remote ionized-impurity scattering.

carriers in polar semiconductors has raised the question of whether or not similar hot-phonon effects could also influence the high-dc-field response of these materials. In particular, it has been argued that LO-phonon amplification with its typical picosecond timescale might interfere with the velocity overshoot in $n$-type GaAs pre- dicted by conventional electron-transport calculations for phonon equilibrium.

We have performed a systematic theoretical analysis of this question by developing a very general Monte Carlo code, which includes a full Monte Carlo treatment of the phonon distribution and provides the first model- independent dc transport theory of nonequilibrium carrier-phonon systems.

The interplay of the mutual energy transfer and drag between the electron and phonon systems with the $\Gamma-L$ valley transfer was studied for a wide range of carrier densities and fields and for lattice temperatures of 300 and 77 K. Proportionality of the phonon disturbances to the electron density on the one hand, and the reduction of the relative contribution of nonequilibrium phonon effects for strongly dominant ionized-impurity scattering on the other hand, were found to restrict marked hot- phonon effects to uncompensated doping levels around $10^{17}-10^{18} \mathrm{~cm}^{-3}$.

Noticeable corrections of the room-temperature steady-state mean carrier velocity were found, from a drag-induced increase of up to $20 \%$ at fields below the threshold for $\Gamma-L$ electron transfer to a reduction at higher fields of up to $10 \%$ due to the reduced cooling efficiency of the hot phonons and the resulting higher in- tervalley scattering rates. In contrast to these steady- state effects, the influence of the LO-phonon disturbances on the velocity overshoot was found to be negligible, in spite of a strong phonon buildup already before and dur- ing the onset of the valley transfer. This inefficiency of the initially amplified LO phonons in reducing the overshoot was shown to be a consequence of the phase- space restrictions for their net reabsorption. This situa- tion is analogous to the case of time-resolved Raman spectroscopy of hot-carrier-induced LO-phonon distur-bances. $^{11}$

We found modifications of the saturation velocity of up to $20 \%$ for the case of high carrier densities and negligi ble doping, resembling the situation of remote ionized im- purities in modulation-doped heterostructures, but again we found only negligible corrections to the velocity overshoot.

The general outcome of the Monte Carlo analysis, and particularly the results for the steady-state velocity-field characteristics, confirm previous calculations using a heated and displaced Maxwellian carrier distribution. In this way the general findings, for phonon equilibrium, of a weak sensitivity of the mean carrier velocity to the de- tailed shape of the carrier distribution function are ex- tended to the present case of strong phonon disturbances. As intercarrier scattering was not included in the present Monte Carlo simulation, while it strongly dominates a heated and displaced Maxwellian, the similarity of the two results indicates a minor influence of intercarrier scattering on the hot-carrier response studied in this work.

## ACKNOWLEDGMENTS
This research was supported by the European Research Office and the Italian National Research Coun- cil. We are also grateful to Dr. C. Jacoboni, Dr. M. Fadel, and Dr. J. C. Vaissière for helpful discussions. The Computer Centers of the Universities of Graz and Modena are acknowledged for providing computer facili- ties.

$^{1}$ R. Peierls, Ann. Phys. (Leipzig) 4, 121 (1930); 5, 244 (1930); 12,154 (1932).
$^{2}$ P. G. Klemens, Proc. Phys. Soc. (London) A 64, 1030 (1951).
$^{3}$ E. H. Sondheimer, Proc. R. Soc. London, Ser. A 234, 391(1956).
$^{4}$ J. E. Parrott, Proc. Phys. Soc. London, 70, 590 (1957).
$^{5}$ P. Kocevar, Phys. Status Solidi B 84, 681 (1977); P. Kocevar and E. Fitz, ibid. 89, 225 (1978).
$^{6}$ P. Bordone, C. Jacoboni, P. Lugli, L. Reggiani, and P. Ko cevar, J. Appl. Phys. 61, 1460 (1987).
$^{7}$ P. Kocevar, J. Phys. C 5, 3349 (1972); Acta Phys. Austriaca 37,259 (1973).
$^{8}$ P. Kocevar, Festkörperprobleme (Advances in Solid State Phys- ics), edited by P. Grosse (Pergamon, Braunschweig, 1987), Vol. 27, p. 197.
$^{9}$ P. Kocevar, Physica B+C 134B, 155 (1985).
$^{10}$ M. Rieger, P. Kocevar, P. Bordone, P. Lugli, and L. Reggiani, Solid State Electron. 31, 687 (1988).
$^{11}$ P. Lugli, C. Jacoboni, L. Reggiani, and P. Kocevar, Appl. Phys. Lett. 50, 1251 (1987); see also P. Lugli, C. Jacoboni, L. Reggiani, and P. Kocevar, Proc. SPIE 793, 102 (1987).
$^{12}$ C. Jacoboni and L. Reggiani, Rev. Mod. Phys. 55, 645 (1983).
$^{13}$ J. Menéndez and M. Cardona, Phys. Rev. B 29, 2051 (1984).
$^{14}$ E. Göbel (private communication).
$^{15}$ W. Fawcett, A. D. Boardman, and S. Swain, J. Phys. Chem. Solids 31, 1963 (1970).
$^{16}$ M. A. Littlejohn, J. R. Hauser, and T. H. Glisson, J. Appl. Phys. 48, 4587 (1977).
$^{17}$ K. Kim, K. Hess, and F. Capasso, Appl. Phys. Lett. 52, 1167(1988).
$^{18}$ S. Goodnick and P. Lugli, Appl. Phys. Lett. 51, 584 (1987).
$^{19}$ J. Shah, B. Deveaud, T. C. Damen, W. T. Tsang, A. C. Gos sard, and P. Lugli, Phys. Rev. Lett. 59, 2222 (1987).
$^{20}$ R. Dingle, H. L. Störmer, A. C. Gossard, and W. Wiegmann, Appl. Phys. Lett. 3, 665 (1978).
$^{21}$ For the different case of longer risetimes, see H. L. Grubin, D.K. Ferry, G. J. Iafrate, and J. R. Barker, in VLSI Electron.: Microstruct. Sci. 3, 197 (1982); E. Constant, in Hot Electron Transport in Semiconductors, edited by L. Reggiani(Springer-Verlag, Berlin, 1985), p. 227; R. Castagné, in High Speed Electronics, edited by B. Källbäck and H. Beneking(Springer-Verlag, Berlin, 1986), p. 2.
$^{22}$ S. Doniach, Proc. Phys. Soc. (London) 73, 849 (1959).