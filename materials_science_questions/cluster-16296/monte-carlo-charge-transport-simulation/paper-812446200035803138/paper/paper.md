# A NEW MONTE CARLO SIMULATION OF HOT ELECTRON TRANSPORT WITH ELECTRON-ELECTRON SCATTERING

A. Hasegawa, K. Miyatsuji, K. Taniguchi and C. Hamaguchi

Department of Electronics, Osaka University,
Suita City, Osaka 565, Japan

## ABSTRACT

A new, simple and more accurate method of Monte Carlo simulation is proposed to take into account the electron-electron scattering. The method is based on two particle simulation which simplifies the Monte Carlo procedure. Present work reveals that the electron-electron scattering introduces no noticeable effect on the transport properties at high electric fields.

## KEYWORDS

Electron-electron scattering; hot electron; drift velocity overshoot; Monte Carlo simulation
Ensemble Monte Carlo simulation, two electrons' states Monte Carlo simulation

## INTRODUCTION

It is well established that Monte Carlo simulation gives a good information of the hot electron transport in semiconductors, such as distribution function, drift velocity saturation, negative differential mobility, drift velocity overshoot effect and so on (Fawcett et al., 1970; Ruch, 1972; Littlejohn et al., 1977; Jacoboni and Regiani, 1983; Hamaguchi, 1985). Accuracy of the simulation depends on how the scattering processes of electrons are adequately taken into account. It is known that dominant scattering processes in n-GaAs are acoustic deformation potential scattering, polar optic phonon scattering, piezoelectric phonon scattering and intervalley phonon scattering. Importance of electron-electron (e-e) interaction has been pointed out by several workers (Matulionis et al., 1975; Takenaka et al., 1979; Jacoboni and Regiani, 1983; Lugli and Ferry, 1983, 1985a, 1985b; Brunetti and Jacoboni, 1985). The treatment of the e-e scattering is different from the other scattering processes such as ionized impurity scattering, phonon scattering and so on in the sense that the e-e scattering is the interaction between two electrons whereas the other scatterings are interactions with one electron. This indicates that the e-e scattering is very complicated and Monte Carlo simulation of e-e scattering seems to be impossible. This is because computer simulation is serial (sequential in time) and we cannot simulate many electrons at the same time (in one sequential time). In this paper we will present a new and simple method to take into account the e-e scattering, where we deal with the short range interaction only and neglect the long range interaction (electron-plasmon interaction). Our method is based on simulation of two-electrons' states and therefore energy and momentum conservation equations are exactly taken into account (Hasegawa et al., 1987). We will investigate the drift velocity overshoot effect in n-GaAs and compare the results with and without e-e scattering.

## ELECTRON-ELECTRON SCATTERING

We follow the treatment of Ziman (1963) where the e-e scattering is divided into two parts corresponding to the collective motion (electron-plasmon interaction) and the individual motion (short range electron-electron scattering). In this paper we take into account the short range e-e scattering and disregard the electron-plasmon interaction. The e-e scattering rate due to the individual mode of Coulomb interaction potential is given by for electron of wave vector $\mathbf{k}_1$

$$
\lambda_{\mathrm{ee}}\left(\mathbf{k}_{1}\right)=\frac{4 \mathrm{n} \mathrm{m}^{*} \mathrm{e}^{4}}{\pi \hbar^{3} \varepsilon^{2} \beta^{2}} \int \mathrm{f}\left(\mathbf{k}_{2}\right) \frac{\mathrm{g}}{\beta^{2}+\mathrm{g}^{2}} \mathrm{~d} \mathbf{k}_{2} \qquad(1)
$$

where $g=|\mathbf{k}_{1}-\mathbf{k}_{2}|$, $\beta=1/\lambda_{\mathrm{d}}$, $\lambda_{\mathrm{d}}$ is the Debye length, $\varepsilon$ is the dielectric constant, n is the electron density, $f(\mathbf{k}_{2})$ is the distribution function of $\mathbf{k}_{2}$ electron and $\mathrm{m}^{*}$ is the electron effective mass (Matulionis et al., 1975; Takenaka et al., 1979).

It is evident from eq. (1) that the knowledge of the electron distribution function is needed in order to evaluate the scattering rate. Matulionis et al. (1975) and Takenaka et al. (1979) reported Monte Carlo simulation including the e-e scattering where they used a priori assumption for the electron distribution function. A more sophisticated technique was recently proposed by


Lugli and Ferry (1983) who employed Ensemble Monte Carlo (EMC) method which allowed inclusion of the e-e scattering without any a priori assumption on the electron distribution function. This technique is based on computation of Monte Carlo histories of N particles in parallel and allows to evaluate an ensemble distribution function at every time step. In the EMC eq. (1) reduces to a sum over all the N electrons of the ensemble

$$
\lambda_{\mathrm{ee}}\left(\mathbf{k}_{1}\right)=\frac{4 \mathrm{n} \mathrm{m}^{*} \mathrm{e}^{4}}{\pi \hbar \varepsilon^{2} \beta^{2} \mathrm{~N}} \sum_{\substack{\text { all } \\ \text { particles }}} \frac{g}{\beta^{2}+g^{2}} \quad(2)
$$

It is very important to point out that in the former method the conservation of momentum and energy cannot be taken into account. In the latter method, EMC method, it seems to be possible to include the conservation but it cannot be done exactly. This is because the EMC isn't carried out in parallel but in the serial form in actual time. The procedure of the EMC calculations is shown schematically in Fig. 1(a). First we simulate one electron out of the ensemble and assume the electron is encountered in the e-e scattering. The second electron involved in the e-e scattering is picked at random from the ensemble. It is evident from Fig. 1(a) that the second electron is spending its free flight and thus we have to stop the second electron during the free flight. This process introduces extra scattering to the counterpart electron. Therefore we cannot expect exact calculation of the e-e scattering. This difficulty can be solved by our new Monte Carlo simulation shown below.

We propose a new EMC method to include the momentum and energy conservation of the two electrons exactly without introducing any extra scattering. This is done by simulating the multiple states of electrons simultaneously. For simplicity we show a case of two electrons' states. In this case we pick up two states of electrons, $\mathbf{k}_{1}$ and $\mathbf{k}_{2}$, and simulate simultaneously. The total scattering rate of the two states of electrons is defined as

$$
\lambda\left(\mathbf{k}_{1}, \mathbf{k}_{2}\right)=\sum_{i} \lambda_{i}\left(\mathbf{k}_{1}, \mathbf{k}_{2}\right) \quad(3)
$$

where the scattering rate includes three types of processes, (i) only one electron $\mathbf{k}_{1}$ is scattered, (ii) only the other electron $\mathbf{k}_{2}$ is scattered, and (iii) both of the electrons, $\mathbf{k}_{1}$ and $\mathbf{k}_{2}$, are scattered at the same time. The subscript i denotes the different scattering processes, such as acoustic phonon scattering, polar LO phonon scattering, e-e scattering and so on. In addition we neglect the process in which both electrons are scattered at the same time by single electron process, for example $\mathbf{k}_{1}$ scattered by acoustic phonon and $\mathbf{k}_{2}$ scattered by polar LO phonon at the same time. In the case of acoustic phonon scattering, the electron with the wave vector $\mathbf{k}_{1}$ changes to $\mathbf{k}_{1}^{\prime}$, and the state $\mathbf{k}_{2}$ remains unchanged, and viceversa. Under this approximation, the total scattering rate of the two-electron state $(\mathbf{k}_{1}, \mathbf{k}_{2})$ is given by

$$
\begin{aligned}
\lambda\left(\mathbf{k}_{1}, \mathbf{k}_{2}\right)= & \lambda_{\text {ion }}\left(\mathbf{k}_{1}\right)+\lambda_{\text {op }}\left(\mathbf{k}_{1}\right)+\lambda_{\text {ac }}\left(\mathbf{k}_{1}\right)+\ldots \ldots \\
& +\lambda_{\text {ion }}\left(\mathbf{k}_{2}\right)+\lambda_{\text {op }}\left(\mathbf{k}_{2}\right)+\lambda_{\text {ac }}\left(\mathbf{k}_{2}\right)+\ldots \ldots+\sum_{i} \lambda_{\text {ee }}\left(\mathbf{k}_{1}, \mathbf{k}_{i}\right)+\sum_{j} \lambda_{\text {ee }}\left(\mathbf{k}_{2}, \mathbf{k}_{j}\right)
\end{aligned}
\tag{4}
$$

where $\lambda_{\text {ion }}(\mathbf{k}), \lambda_{\text {op }}(\mathbf{k})$, and $\lambda_{\text {ac }}(\mathbf{k})$ are ionized impurity, optic phonon, and acoustic phonon scattering rate with wave vector $\mathbf{k}$, respectively. In eq. (4) the e-e scattering is expressed, for example, by $\lambda_{\mathrm{ee}}\left(\mathbf{k}_{1}, \mathbf{k}_{\mathrm{i}}\right)$ with the two states of electrons $\mathbf{k}_{1}$ and $\mathbf{k}_{i}$. In a semiconductor we are interested in, there exist many electrons, n electrons in unit volume. In EMC calculations we simulate finite electrons, N electrons, of which number depends on a computer and on time required. We assume that half of the electrons, N/2, have wave vector $\mathbf{k}_{1}$ and the other half electrons, N/2, have $\mathbf{k}_{2}$. In other words, we assume that

$$
\sum_{i} \lambda_{\mathrm{ee}}\left(\mathbf{k}_{1}, \mathbf{k}_{i}\right)+\sum_{j} \lambda_{\mathrm{ee}}\left(\mathbf{k}_{2}, \mathbf{k}_{j}\right) \cong \mathrm{N} \lambda_{\mathrm{ee}}\left(\mathbf{k}_{1}, \mathbf{k}_{2}\right) \quad(5)
$$

where $\lambda_{\mathrm{ee}}\left(\mathbf{k}_{1}, \mathbf{k}_{2}\right)$ is the e-e scattering rate between the two electrons $\mathbf{k}_{1}$ and $\mathbf{k}_{2}$ and given by

$$
\lambda_{\mathrm{ee}}\left(\mathbf{k}_{1}, \mathbf{k}_{2}\right)=\frac{4 \mathrm{n} \mathrm{m}^{*} \mathrm{e}^{4}}{\pi \hbar^{3} \varepsilon^{2} \beta^{2} \mathrm{~N}} \frac{g}{\beta^{2}+g^{2}} \quad(6)
$$

![](./images/812446200035803138_1.jpg)

Fig. 1 Schematic illustrations of Ensemble Monte Carlo simulation. (a) Conventional method of 1 electron state, and (b) new EMC of 2 electrons' states. Scattering is shown by x and dotted circle is e-e scattering.

Figure 2 illustrates schematic diagram of the scattering rates in the scheme of the two electrons' states, where we find a difference in the scattering between single electron process and two electron process. When we use these approximations, the procedures of the EMC are very simple as shown in Fig. 1(b), where pairs of two electrons' states are simulated in parallel. Comparing the present EMC method of pair states with the conventional EMC method of Lugli and and Ferry (1983), we find a similarity except the e-e scattering. Therefore the transient

dynamical response of electrons is easily investigated in the presence of the e-e scattering. It is very important to point out that the energy and momentum conservation are exactly taken into account. In addition we need no knowledge of the electron distribution function and therefore the calculations become very simple, resulting in saving time of computation.

We have to note that although the e-e scattering rate approximated by eq. (4) is not exact, these electrons experience many different pair states and ensemble average gives an approximate information. If we increase the number of the electrons which are simulated simultaneously, $\mathbf{k}_1$, $\mathbf{k}_2$, $\mathbf{k}_3$,..., the simulation gives more reliable results.

# RESULTS OF SIMULATION

In the present simulation we used 5,000 pairs of particles of which initial conditions were generated by assuming Maxwellian distribution under zero electric field. We apply a uniform electric field at time t=0 ps and these pairs are accelerated and scattered. Noting that the scattering probabilities change time by time depending on the electron temperature, we have to deduce average values of transport parameters, for example electron temperature, step by step and to update the scattering rate at definite times. This is done by calculating ensemble averages during progressive time interval. We set the time interval $\Delta t = 0.01ps$ which is comparable with the mean scattering time. We present here only the results for T=300 K, E=5 kV/cm and $n=1.0X10^{18} cm^{-3}$. The lattice temperature is assumed to be constant. We included screening effect of polar optic phonon field by electrons (Hamaguchi, 1985; Hasegawa et al., 1987). The parameters used in the present calculations are the same as those of Littlejohn et al. (1977) except the effective masses which are $m_t(L)=0.08m$, $m_l(L)=1.58m$, $m_t(X)=0.19m$, and $m_l(X)=0.98m$, where subscript t and l mean the transverse and longitudinal component of the effective mass, L and X are the valley index, and m is the free electron mass.

The present simulation was made as follows. The first pair of electrons is accelerated in the electric field and is subjected to scatterings during the first time interval $\Delta t$. Next, we simulate the second pair of electrons during the first period $\Delta t$. We continue this process until the final electron pair, 5000th electron pair, spends the time interval $\Delta t$. In this way, we get the information of the 5000 electron pairs at time t= $\Delta t$. Using the results, we set new condition for the next period $\Delta t < t \leq 2 \Delta t$ and continue the calculations of the 5000 electron pairs. These procedures give us the information about the transient dynamics of electrons. In order to confirm our new EMC, we carried out the conventional EMC calculations (single electron state) and our new EMC calculations (two electrons' states), both without the e-e scattering, and found that these two methods give exactly the same results as expected.

![](./images/812446200035803138_2.jpg)

Fig. 2 Scattering rates of 2 electrons' states, $\mathbf{k}_1$ and $\mathbf{k}_2$. Overlapping part is e-e scattering.

Figure 3 shows the drift velocity as a function of time after the application of a uniform electric field 5kV/cm, where the solid curve is calculated by our new EMC method (two electrons' states) with e-e scattering which is almost the same as the curve calculated by the conventional EMC method (single electron's state) without the e-e scattering. This indicates that the e-e scattering induces a negligible contribution to the electron transport at high electric field. The dashed curve in Fig. 3 is calculated by the conventional EMC with the e-e scattering, which shows a noticeable difference from the new EMC calculations. This difference may be ascribed to the incorrect assumption of the e-e scattering in the conventional EMC. A weak overshoot of drift velocity is seen in Fig. 3. When we increase the electric field, we obtain a pronounced overshoot effect as reported ealier.

![](./images/812446200035803138_3.jpg)

Fig. 3 Drift velocity of electrons in n- GaAs with $n=1.0X10^{18}cm^{-3}$ at T=300K and E=5kV/cm. Solid curve is calculated by the new EMC with e-e scattering which is the same as the result of conventional EMC without e-e scattering. Dashed curve is obtained by the conventional EMC with e-e scattering.

![](./images/812446200035803138_4.jpg)

Fig. 4 Electron temperature as a function of time in n-GaAs with $n=1.0 \times 10^{18} \mathrm{~cm}^{-3}$ at T = 300K and E = 5kV/cm. Solid curve: two electrons' states EMC with e-e scattering which is almost the same as the results calculated by the conventional EMC without e-e scattering. Dashed curve: conventional EMC (single state) calculations with e-e scattering.

![](./images/812446200035803138_5.jpg)

Fig. 5 Electron populations in the $\Gamma$ and $L$ valleys as a function of time in n-GaAs with $n=1.0 \times 10^{18} \mathrm{~cm}^{-3}$ at $\mathrm{T}=300 \mathrm{~K}$ and $\mathrm{E}=5 \mathrm{kV} / \mathrm{cm}$. Solid curves: two electrons' state EMC with e-e scattering which are the same as the results calculated by the conventional EMC of single state without e-e scattering.
Dashed curves: conventional EMC (single state) calculations with e-e scattering.

Figure 4 shows the calculated electron temperature as a function of time after the application of a uniform electric field 5 kV/cm. We find in Fig. 4 that the electron temperature increases with time and reaches a steady state value. It should be noted that inclusion of the e-e scattering in the conventional EMC results in an increase in the electron temperature. Figure 5 shows a plot of the calculated results of the valley occupations as a function of time, where we find that after the overshoot, time $t>1.0$ ps, electrons are transferred from the $\Gamma$ valley into the L valleys. It is pointed out by several authors that the most significant influence of the e-e scattering is the change in the electron distribution function. The valley occupation reflects the distribution function, because the electrons in the tail of the distribution (the high energy electrons) can be transferred into the different higher valleys. Therefore the difference between the solid and dashed curves in Fig. 5 is explained in terms of the difference in the electron temperature shown in Fig. 4. Since the drift velocity of electrons in the L valleys is quite low compared with that in the $\Gamma$ valley, the difference of the drift velocitiesin Fig. 3 may be explained in the same way. (Electron temperature is averaged over the valleys.)

From the present work we find that the e-e scattering introduces no noticeable change in the transport properties at high electric fields. The difference between the new EMC method utilizing two electrons' states and the conventional EMC method utilizing series of single electron state comes from improper treatment of the e-e scattering in the latter method in which only the k state of one of the two electrons is taken into account and the counterpart is disregarded or, in other words, the energy and momentum conservation is not taken into account exactly.

## REFERENCES

Brunetti, R, C. Jacoboni, A. Matulionis, and V. Dienys (1985). Physica, 134B, 369-373.
Fawcett, W, A. D. Boardman, and S. Swain (1970). J. Phys. Chem. Solids, 63, 1963-1990.
Hamaguchi, C (1985). Physica, 134B, 87-96.
Hasegawa, A, K. Miyatsuji, and C. Hamaguchi (1987). Technol. Repts. Osaka Univ., 37, 117125.
Jacoboni, C, and L. Regiani (1983). Rev. Mod. Phys., 55, 645-705.
Littlejohn, M. A., J. R. Hauser, and T. H. Glisson (1977). J. Appl. Phys., 48, 4587-4590.
Lugli, P., and D. K. Ferry (1983). Physica, 117B & 118B, 251-253.
Lugli, P., and D. K. Ferry (1985). Appl. Phys. Lett., 46, 594-596.
Lugli, P., and D. K. Ferry (1985). Physica, 134B, 364-368.
Matulionis, A, J. Pozela, and A. Reklaitis (1975). Solid State Commun., 16, 1133-1137.
Ruch, J. G. (1972). IEEE Trans. Electron Device, ED-19, 652-654.
Takenaka, N, M. Inoue, and Y. Inuishi (1979). J. Phys. Soc. Jpn., 47, 861-868.
Ziman, J. M. (1963)."Electrons and Phonons," Clarendon Press (Oxford), Chapt. IX (9.14), 412-418.