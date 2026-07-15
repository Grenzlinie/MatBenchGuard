# Monte Carlo Simulation of the Effects of X6 and X7 Intervalley Scattering on the Ultrafast Relaxation of Photoexcited Carriers in GaAs

Mohamed A.Osman
School of Electrical Engineering and Computer Science
Washington State University
Pullman, WA 99164-2752,USA

## Abstract
The effects of X6 and X7 intervalley scattering on the energy relaxation of electrons in GaAs were investigated in GaAs for excitation energy of 4.3eV. An initial build up of electron population in the upper valleys (X6 and X7) following the excitation leads to non-equilibrium LO phonon. The initial LO phonon spectrums in different valleys show maximum build up at different q vectors and then relax to similar distributions at longer times. The Heating of the LO phonons leads to slower transfer of electrons back to the central valleys.

## 1. Introduction
The energy relaxation dynamics of high density carriers photoexcited by femtosecond laser pulses in GaAs have been examined by several groups to understand the role of X6-X7 intervalley scattering and the slowing of the relaxation rate at very high densities [1]-[2]. For example, Cavicchia and Alfano [2] using a 500 femtosecond UV pulse (293 nm) examined intervalley scattering between upper satellite valley X7 and central valley and reported energy band renormalization of the X6 and X7 valleys. Additionally, using infra red absorption techniques, they examined interband and free carrier absorption at different intensities and measured deformation potential for scattering into the X7-valley.

Because of the very high densities of photoexcited carriers used in [2], both the energy relaxation rates and the band structure of GaAs are strongly affected. These effects include energy gap renormalization, slowing of the cooling rates, and strong screening. Additionally, the large excitation energy results in exciting electrons and holes to very high energy regions of the conduction and valence bands, respectively. Under these conditions the details of the band structure strongly influence the cooling rates. The very high initial energy of the electrons excited by 293 nm laser pulse in [2] reduces the effectivness of the screening process at early stages of relaxation. This makes the role of hot phonon population build up as electrons cascade down the upper valleys very important factor in slowing down of the energy relaxation process. Consequently, the intervalley transfer rates will be affected by the presence of hot phonons. In this investigation, we have examined the energy relaxation and population transfer between the first and the second bands in the conduction band for excitation densities of $10^{17}cm^{-3}$ and $10^{18}cm^{-3}$ using ensemble Monte Carlo approach. Additionally, the buildup of non-equilibrium LO phonon distribution in each valley was examined under the ideal assumption of independent nonequilibrium LO phonon distribution in each valley. This assumption, although, not realistic provides insight on the inter-relationship between hot phonon build up and intervalley transfer between different valleys. The details of the model are discussed next followed by discussion of the results of the simulation.

## 2. Simulation Model
We have examined the ultrafast relaxation of photoexcited carriers in GaAs using ensemble Monte Carlo approach (EMC). The EMC model includes four non-parabolic valleys (central, L-, X6-, and X7-valleys), screened carrier-carrier scattering, hot LO phonon, acoustic, intra-valley, and intervalley phonon scattering [3]-[4]. The valence band model includes three parabolic and spherically symmetric bands. In this model both intra-valley and intervalley e-e scattering are included which allows energy exchange between electrons in different valleys [5]. The details of the scattering processes and the implementation of carrier-carrier scattering has been discussed elsewhere and will not be repeated here [3]. The light hole band consists of two piece-wise continuous sections defined by a cutoff wave vector $k_c=5×10^8 cm^{-1}$ such that :


$$
E(k)=
\begin{cases}
\frac{\hbar^2 k^2}{2 m_{l}^{*}} & k \leq k_{c} \\
\frac{\hbar^2 k^2}{2 m_{h}^{*}} & k > k_{c}
\end{cases}
\tag{1}
$$

where $m_{l}^{*}=0.085$ and $m_{h}^{*}=0.45$ are the light and heavy hole effectives masses, respectively. This is a simplified versions of the model used by Collet[6], however, it gives similar results at low and high values of k. To examine energy relaxation process at high excitation energies a laser pulse centered at 293 nm and 500 femtosecond duration was assumed. A spread of 60 meV was assumed in the energy spectrum of the laser. The energies of the electrons excited from the heavy, light, and split-off bands were around, 2200, 2100, and 1700 meV. During the simulation, carriers are added while the laser pulse is on with final electron ensemble of 5000. In this contribution we report only on the effects of the hot phonons on intervalley transfer rates. Because of the long pulse duration (compared to momentum coherence times) and the initial dominance of the momentum randomizing intervalley scattering to upper satellite valleys, the coherence effects are ignored in this investigation. We have also neglected screening of the LO phonons because of the high initial energies of the electrons. However, even though this assumption is realistic at the early stages of relaxation, it leads to more LO scattering events at longer times after the electrons cascade to the bottom of the respective valleys. Even though holes will accelerate the energy relaxation of the electrons through electron-hole interaction as was shown earlier[3], the simulation is limited to electrons only. This assumption leads to overestimating the role of intervalley and LO phonon scattering in the energy relaxation of electrons. However, the present model provides an insight on the heating of the LO phonons under high energy excitation and how the non-equilibrium phonon distributions develop in each of the valleys.

The LO phonon spectrum of the emitted phonons depends on the effective mass of electrons in each valley because for same amount of phonon energy different values of change in electron wave vector is involved. Therefore, one can expect that each spectrum will peak at different values of q. For example, since the electron effective masses in the four conduction band valleys satisfy the following relationship:

$$
m_{\Gamma}^{*}<m_{L}^{*}<m_{X 7}^{*}<m_{X 6}^{*}
\tag{2}
$$

One can expect the corresponding q-vectors of the majority of emitted LO phonons in each valleys will satisfy the following:

$$
q_{\Gamma}<q_{L}<q_{X 7}<q_{X 6}
\tag{3}
$$

Although, initially the maxima of LO phonon distributions in each valley develop at different values of q wave vector q, at longer times due to the phonon interactions the distributions will tend to be similar. Additionally, because LO phonons are emitted over a range of q vectors, the LO distributions tend to overlap each other at longer times. Thus, the LO phonon build up in upper X6 and X7 valleys will influence the energy relaxation in central and L-valleys. The strong carrier-carrier scattering at very high densities accelerates filling of lower energy states in all valleys which while generating electrons at the high energy tails.

### 3. Results and discussion
The time evolution of electron population in all four valleys is shown in Figs. 1-a and Fig. 1-b at excitation level of $10^{17} cm^{-3}$ with and without including hot phonon effects, respectively. There is a very rapid transfer of electrons to both X6 and X7 valleys while the pulse is on resulting in depletion of the central valley population. Including hot phonons leads to very small reduction in the intervalley transfer back to the central valley (about 5%). The effect on the intervalley transfer out of the X6 and X7 valleys is quite negligible because of the strong energy loss through deformation potential scattering. At $10^{18} cm^{-3}$ excitation level, Fig. 2 shows rapid increase in the population of X6 and X7 valleys to close to 80% and 15%, respectively. When hot phonons are neglected, the X6 valley population drops to less than 5% after 2ps, while the L-valley population drops to 17% after 5 picoseconds. On the other hand, when hot phonons are included, a long tail persists in the population of the X6 valley with a slower rise in the population of the

L-valley. At 5 picoseconds after the excitation, the L-valley population drops to about 25% compared to 17% when hot phonons were neglected. This is due to the reduction in energy loss through LO phonon emission which keeps electrons at higher energy states where they can transfer to the L-valley.

The net energy loss through LO phonons and non-polar phonons are shown in Figs. 3 and 4. Introducing hot phonons leads to a slight reduction in energy loss through LO phonons due to enhanced LO phonon absorption rates. This also leads to reduction in the total energy lost by the elctrons. These effects are gen- erally stronger at the higher excitation level of $10^{18} cm^{-3}$. The hot phonon distributions in all four valleys are shown in Fig. 5 at times 2.0 ps and 2.5 ps after excitation for concentration of $10^{17} cm^{-3}$. Note that in Fig. 5-a, each valley distribution exhibits distinct maxima but there is a great deal of overlap at longer q waver vectors. Additionally, the distribution in the L-valley lies almost totally within the LO distribution of the X6 valley which points to fact that a more realistic approach would use the same LO phonon distri- bution for both valleys. Under these circumstances, LO phonon absorption by the L-valley electrons will be significantly enchanced leading to lower energy loss through LO phonon emission. Fig. 5-b shows a rapid and significance build up of LO phonons in the central valley with a larger portion under the X6 distribution which also indicates the weakness of the assumption used in the investigation. However, the distributions show that significant build up of the LO phonons occur mainly in the X6-, L-, and central valleys. The contribution of X7 valley is negligible.

The LO phonon energy loss in all valleys are shown in Fig. 6 at exciation level of $10^{18} cm^{-3}$. When LO phonons are included (Fig. 6-b), the energy loss in the central- and L-valley drops by 30% and 20%, respectively. On the other hand the energy loss in the X6 valley is not significantly affected by including hot phonons because its population drops down quickly through intervalley transfer of electrons to lower valleys. In essence, X6 valley electrons contribute to the build up of LO phonon distribution but do not stick around long enough to re-absorb some of these LO phonons. However, there is a slower bulid up of energy compared to the situation where hot phonons are neglected. Similary, the small energy loss by X7 valley electrons is not affected by including hot phonons.

## 4. Conclusion
The intervally transfer of electrons to the X7 valleys have small effect on the energy relaxation of electrons for the excitation levels used in this investigation. Introducing hot phonons reduces intervalley transfer back to central valley at higher excitation levels and leads to reduction in the effectiveness of LO phonon as an energy loss channel for electrons in the central and L-valleys. However, the energy losses by X6 and X7 valley electrons are not significantly affected by hot phonons. The assumption of different LO phonon distribution leads to overestimating of the energy Loss through LO phonons.

## 5. Acknowledgment
We acknowledge the use of the computing facility at the solid state device animation laboratory funded by NSF's Division of Undergraduate Education through grant DUE # 9651416.

## REFERENCES
[1] W.B. Wang,N. Ockman, M. Yan, and R.R. Alfano, *Solid State Electronics*, **32**, 1337, 1989.
[2] R. Gavicchia and R.R. Alfano, *Phs. Rev*, **B47**, 5337, 1993.
[3] M.A. Osman and D.K. Ferry, *Phys. Rev.*, **B36**, 6018, 1987.
[4] O. Mouton, J.L. Thobel, and R. Fauquembergue, *J. Appl. Phys.*, **81**, 3160, 1997.
[5] M.A. Osman, N. Nintunze, and M.A. Imam, *Semicond. Sci. Technol.*, **7**, 340, 1992.
[6] J.H. Collet, *Phys. Rev.*, **B47**, 3160, 1993.

![](./images/812376802403024896_1.jpg)

Fig. 1: Time evolution of valley population of photoexcited carriers: (a) without hot phonons, (b) with hot phonons $(N_x = 10^{17} cm^{-3})$.

![](./images/812376802403024896_2.jpg)

Fig. 2: Time evolution of valley population of photoexcited carriers: (a) without hot phonons, (b) with hot phonons $(N_x = 10^{18} cm^{-3})$.

![](./images/812376802403024896_3.jpg)

Fig. 3: Accummulative energy loss as a function of time through deformation potential and LO phonons.
(a) without hot phonons, (b) with hot phonons $(N_x=10^{17}cm^{-3})$.

![](./images/812376802403024896_4.jpg)

Fig. 4: Accummulative energy loss as a function of time through deformation potential and LO phonons.
(a) without hot phonons, (b) with hot phonons $(N_x=10^{18}cm^{-3})$.

![](./images/812376802403024896_5.jpg)

Fig. 5: Non-equilibrium phonon population in different valleys: (a) $t=2.0ps$, (b) $t=2.5ps$
$(N_x=10^{17}cm^{-3})$.

![](./images/812376802403024896_6.jpg)

Fig. 6: Accummulative energy loss as a function of time through LO phonon emission in individual valleys.
(a) without hot phonons, (b) with hot phonons $(N_x=10^{18}cm^{-3})$.