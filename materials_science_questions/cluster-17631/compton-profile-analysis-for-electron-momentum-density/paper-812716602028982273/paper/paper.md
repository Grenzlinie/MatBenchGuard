# Atomic K- and L-shell Compton defects for the study of electronic structures

F. Gasser and C. Tavard
Laboratoire Rayonnements et Structures, Faculté des Sciences, Ile du Saulcy,
57045 Metz Cedex, France
(Received 12 April 1982)

An accurate treatment is developed for the calculation of Compton defects and their physical interpretation. The case of atomic $K$ and $L$-shells analyzed here exhibits the strong dependency of Compton defects with overlapping properties of individual orbitals. For given azimuthal $l$ and magnetic $m$ quantum numbers, a simple generalization allows one to predict the sign of the Compton defect from the parity of $l+m$.

## I. INTRODUCTION

During the last few years very accurate experimental Compton profiles for gaseous targets have been found to disagree$^{1,2}$ with impulse approximation (IA) calculations. The observed discrepancies or Compton defects primarily result from an asymmetry of the profile leading to a shift $\delta q$ of the peak maximum with respect to the position predicted by the IA. In the framework of the first Born approximation, various attempts to explain these observations have been formulated.$^{3,4}$ They include effects of binding in the final-state representation of the ejected electron.

A different approach had been proposed previously.$^{5,6}$ It consists of a drastic expansion of the Born propagator and yields corrective terms to the profile $J^{0}(q)$ in the IA:
$$J(q, k)=J^{0}(q)+J^{\prime}(q, k)+J^{\prime \prime}(q, k)+....$$

These corrections only imply a knowledge of the target in its initial state. The first two corrective terms $J'$ and $J''$ are, respectively, antisymmetric and symmetric in $q$. For hydrogenic ions in $1s$ initial state, their behavior has been investigated in a previous work$^{7}$ for a complete set of momentum transfers. Very satisfactory results were obtained even for those small values of momentum transfer where IA is failing. The proposed treatment is presented here under an improved approach making use of space properties for individual orbitals (and for the ground-state wave function in a general case.) A number of applications here concern the $2s$, $2p_{x,y}$, and $2p_{z}$ hydrogenic orbitals, with aim towards a future extension to atomic systems.

$$J^{0}(q)=k \sum_{\mu=1}^{N} \frac{1}{2 \pi} \int_{-\infty}^{+\infty} d t \exp (-i t q k)\left\langle\phi_{a}\left|\exp \left(i t C_{\mu}\right)\right| \phi_{a}\right\rangle.\tag{4}$$

## II. THEORY

When relativistic and exchange corrections are omitted$^{8}$ and the Born approximation is used for the scattering of an electron by an $N$-electron target system, the differential cross section can be defined in terms of the Compton profile:
$$J(q, \overrightarrow{\mathrm{k}})=k \sum_{\mu=1}^{N} \frac{1}{2 \pi} \int_{-\infty}^{+\infty} d t \exp (-i t q k) F_{\mu}(t, \overrightarrow{\mathrm{k}})\tag{1}$$
with
$$F_{\mu}(t, \overrightarrow{\mathrm{k}})=\left\langle\phi_{a}\left|\exp \left[i t\left(X+C_{\mu}\right)\right]\right| \phi_{a}\right\rangle.\tag{2}$$

$X$ and $C_{\mu}$ are two operators given by
$$\begin{aligned}
& X\left|\phi_{a}\right\rangle=\left(H-E_{a}\right)\left|\phi_{a}\right\rangle=0, \\
& C_{\mu}=-i \overrightarrow{\mathrm{k}} \cdot \vec{\nabla}_{\mu}.
\end{aligned}\tag{3}$$

$H$ represents the target Hamiltonian and $\phi_{a}$ the electronic wave function describing the initial state of energy $E_{a}$. The Compton parameter $q$ corresponds to
$$q=(E-k^{2}/2)/k,$$
where $E$ and $k$ represent, respectively, the energy and momentum transferred from the incident particle to the target. All the expressions are written in Hartree atomic units. A similar result holds for high-energy photon scattering (x ray or gamma ray).

For large $k$, the expressions (1) and (2) are simply evaluated by assuming a commutation of $X$ and $C_{\mu}$. This assumption yields the IA result

However, the Born operator $\exp[it(X+C_{\mu})]$ can be expressed using the exact relationship,
$$
\exp \left[i t\left(X+C_{\mu}\right)\right]=\exp \left(i t C_{\mu}\right)\left[1+i \int_{0}^{t} d t^{\prime} \exp \left(-i t^{\prime} C_{\mu}\right) X \exp \left[i t^{\prime}\left(X+C_{\mu}\right)\right]\right],\qquad(5)
$$
which allows a series expansion of this operator. The translation operator $\exp (i t C_{\mu})$ clearly brings the IA result from the first term. The alternately antisymmetric and symmetric successive terms give rise to corrections to the IA. A leading contribution to the Compton defect thus comes from the first antisymmetric correction which will be examined here.

This antisymmetric correction can be rewritten as
$$
J^{\prime}(q, \overrightarrow{\mathrm{k}})=k \sum_{\mu=1}^{N} \frac{1}{2 \pi} \int_{-\infty}^{+\infty} d t \exp (-i t q k) F_{\mu}^{\prime}(t, \overrightarrow{\mathrm{k}})\qquad(6)
$$
with
$$
F_{\mu}^{\prime}(t, \overrightarrow{\mathrm{k}})=i\left\langle\phi_{a}\left|\exp \left(i t C_{\mu}\right) \int_{0}^{t} d t^{\prime} X\left(t^{\prime}\right)\right| \phi_{a}\right\rangle.\qquad(7)
$$

In this expression
$$
\begin{aligned}
\left.X\left(t^{\prime}\right) | \phi_{a}\right\rangle & =\exp \left(-i t^{\prime} C_{\mu}\right)\left(H-E_{a}\right) \exp \left(i t^{\prime} C_{\mu}\right) | \phi_{a}\right\rangle \\
& =\left[U\left(\overrightarrow{\mathrm{r}}_{1}, \ldots, \overrightarrow{\mathrm{r}}_{\mu}-\overrightarrow{\mathrm{k}} t^{\prime}, \ldots, \overrightarrow{\mathrm{r}}_{N}\right)-U\left(\overrightarrow{\mathrm{r}}_{1}, \ldots, \overrightarrow{\mathrm{r}}_{\mu}, \ldots, \overrightarrow{\mathrm{r}}_{N}\right)\right] | \phi_{a}\rangle
\end{aligned}\qquad(8)
$$
corresponds to the variation of the potential energy $U$ in the target, due to the uniform translation $\overrightarrow{k} t^{\prime}$ being found for the $\mu$ th bound electron under impulse assumptions. The next step consists in performing the integration in Eq. (7). This integration was approximated previously $^{6,9}$ by a three-point method of Simpson.

An exact calculation may now be carried out. With $\overrightarrow{R}=\overrightarrow{k} t$, a one-dimensional Fourier inversion transforms the Compton profile Eq. (1) in a sum of terms $F_{\mu}(R, \overrightarrow{k})$ depending on space properties of the orbitals, some of which are of current use in molecular physics. $^{10}$ IA Compton profile (4) is simply the Fourier transform of self-overlap functions $S_{\mu}(R)$ for the wave function,
$$
F_{\mu}^{0}(t, \overrightarrow{\mathrm{k}})=S_{\mu}(R)=\left\langle\phi_{a}\left|\exp \left(i t C_{\mu}\right)\right| \phi_{a}\right\rangle=\left\langle\phi_{a}\left(\ldots, \overrightarrow{\mathrm{r}}_{\mu}, \ldots\right)\left|\phi_{a}\left(\ldots, \overrightarrow{\mathrm{r}}_{\mu}+\overrightarrow{\mathrm{R}}, \ldots\right)\right\rangle,\right.\qquad(9)
$$
which may consist in a sum of overlap functions for individual orbitals. In the IA scheme and after collision, each electron undergoes a translation $\overrightarrow{R}=\overrightarrow{k} t$ or, in an equivalent way, the center $A$ of its orbital suffers a recoil $\overrightarrow{A} A^{\prime}=-\overrightarrow{R}$ (Fig. 1). For one-electron problems, overlap integrals or autocorrelation functions $^{11} S(R)$ have been evaluated for different orbitals $^{10}$ and have been used in the interpretation of Compton profiles in solid materials. $^{12}$

A similar approach can be employed for the corrective terms to the IA. The antisymmetric correction $J^{\prime}(q, \overrightarrow{k})$ thus corresponds to a pure imaginary function $F_{\mu}^{\prime}(R, \overrightarrow{k})$,
$$
F_{\mu}^{\prime}(R, \overrightarrow{\mathrm{k}})=i\left[V_{\mu}^{\prime}(R, \overrightarrow{\mathrm{k}})-V_{\mu}(R, \overrightarrow{\mathrm{k}})\right]=i \Delta V_{\mu}(R, \overrightarrow{\mathrm{k}})\qquad(10)
$$
with
$$
\begin{aligned}
V_{\mu}(R, \overrightarrow{\mathrm{k}}) & =\int_{0}^{t} d t^{\prime}\left\langle\phi_{a}\left|U\left(\ldots, \overrightarrow{\mathrm{r}}_{\mu}, \ldots\right) \exp \left(i t C_{\mu}\right)\right| \phi_{a}\right\rangle \\
& =\frac{R}{k}\left\langle\phi_{a}\left(\ldots, \overrightarrow{\mathrm{r}}_{\mu}, \ldots\right)\left|U\left(\ldots, \overrightarrow{\mathrm{r}}_{\mu}, \ldots\right)\right| \phi_{a}\left(\ldots, \overrightarrow{\mathrm{r}}_{\mu}+\overrightarrow{\mathrm{R}}, \ldots\right)\right\rangle
\end{aligned}\qquad(11)
$$
and
$$
V_{\mu}^{\prime}(R, \overrightarrow{\mathrm{k}})=\int_{0}^{t} d t^{\prime}\left\langle\phi_{a}\left|\exp \left[i\left(t-t^{\prime}\right) C_{\mu}\right] U\left(\ldots, \overrightarrow{\mathrm{r}}_{\mu}, \ldots\right) \exp \left[-i\left(t-t^{\prime}\right) C_{\mu}\right]\right| \exp \left(i t C_{\mu}\right) \phi_{a}\right\rangle.\qquad(12)
$$

The two-center potential energy functions $V_{\mu}(R, \overrightarrow{k})$ have also been tabulated $^{10}$ for different orbitals. Since $V_{\mu}^{\prime}(R, \overrightarrow{k})$ appears to depend on three distinct centers $A, A^{\prime}$, and $A^{\prime \prime}$ (Fig. 2), its explicit calculation should be performed by rewriting Eq. (12) as, with $\overrightarrow{R}^{\prime}=\overrightarrow{k} t^{\prime}$,
$$
V_{\mu}^{\prime}(R, \overrightarrow{\mathrm{k}})=\int_{0}^{R} \frac{d R^{\prime}}{k}\left\langle\phi_{a}\left(\ldots, \overrightarrow{\mathrm{r}}_{\mu}, \ldots\right)\left|U\left(\ldots, \overrightarrow{\mathrm{r}}_{\mu}+\overrightarrow{\mathrm{R}}^{\prime}, \ldots\right)\right| \phi_{a}\left(\ldots, \overrightarrow{\mathrm{r}}_{\mu}+\overrightarrow{\mathrm{R}}, \ldots\right)\right\rangle.\qquad(13)
$$

For hydrogenic ions, the $V^{\prime}(R, k)$ functions reduce to the nuclear attractive integral

$$
\begin{aligned}
V^{\prime}(R, k)= & \left\langle\phi_{a}(\vec{r})\left|\int_{0}^{R} \frac{d R^{\prime}}{k}\left(-\frac{Z}{\left|\vec{r}+\overrightarrow{\mathrm{R}}^{\prime}\right|}\right)\right| \phi_{a}(\vec{r}+\overrightarrow{\mathrm{R}})\right\rangle \\
= & -\frac{Z}{k}\left\langle\phi_{a}(\vec{r})\left|\int_{0}^{R} d R^{\prime}\left[\frac{R^{2}}{4}(\xi-\eta)^{2}+R^{\prime 2}-R R^{\prime}(1-\xi \eta)\right]^{-1 / 2}\right| \phi_{a}(\vec{r}+\overrightarrow{\mathrm{R}})\right\rangle,
\end{aligned}
$$

rewritten here in terms of elliptical coordinates $^{13}$
$\xi=(r+r') / R$ and $\eta=(r'-r) / R$.

After integration over $R'$, the following expressions are obtained:
$$
\int_{0}^{R} \frac{d R^{\prime}}{k}\left(-\frac{Z}{\left|\vec{r}+\overrightarrow{\mathbf{R}}^{\prime}\right|}\right)=-\frac{Z}{k} \ln \left(\frac{\xi+1}{\xi-1}\right), \quad(15)
$$

$$
\int_{0}^{R} \frac{d R^{\prime}}{k}\left(-\frac{Z}{r}\right)=-\frac{Z}{k}\left(\frac{2}{\xi-\eta}\right), \quad(16)
$$
and, by difference,
$$
\Delta U(k, \vec{r})=-\frac{Z}{k}\left[\ln \left(\frac{\xi+1}{\xi-1}\right)-\frac{2}{\xi-\eta}\right]. \quad(17)
$$

This last expression proportional to $Z / k$ is independent of $R$. The binding effects acting upon the ejected electron are taken into account through $\Delta U$, an estimate of the variation in potential energy during the impulse motion (linear trajectory) of this electron. $\cdot \Delta U$ vanishes for short time interactions $^{14}$ (large $k$). Quantum mechanics occurs finally, with an average of $\Delta U$ performed upon the overlap:
$$
\Delta V(R, k)=\left\langle\phi_{a}(\vec{r})|\Delta U| \phi_{a}(\vec{r}+\overrightarrow{\mathrm{R}})\right\rangle. \quad(18)
$$

In the case of more complicated atomic or molecular systems, the electronic repulsive terms may be carried out in a similar manner.

![](./images/812716602028982273_1.jpg)

FIG. 1. Geometrical representation of parameters used in $S$ 's integration of Eq. (9): $\vec{r}_{\mu}^{\prime}=\vec{r}_{\mu}+\overrightarrow{\mathrm{R}}$.

The behavior of Eq. (18) explains finally all observed defects. The first-order antisymmetric correction $J'$ is found to possess, for $q=0$, the following slope:
$$
\Delta^{\prime}=\left.\frac{d J^{\prime}(q, k)}{d q}\right|_{q=0}=\frac{1}{\pi} \int_{0}^{\infty} d R R \Delta V(R, k). \quad(19)
$$

Since $\Delta V$ appears to have a constant sign over all $R$ values, $\Delta'$ and hence $\delta q$ are found with the sign of $\Delta V$.

The antisymmetric correction $J'(q, k)$ is then simply obtained by performing an analytical Fourier transform of $\Delta V$. For hydrogenic ions in $1s$, $2s$, $2p_{x,y}$, and $2p_{z}$ electronic states, the results are presented in Figs. 3 and 4. With $K=k/\zeta$, the functions $S$ and $K\Delta V$ (Fig. 3) are shown under universal coordinates with abscissas $z=\zeta R$. In the reciprocal space and with $Q=q/\zeta$ (Fig. 4), the $KZJ'(Q)$ functions are found to correspond to the $K\Delta V$ functions. They are compared here at $K=3$ (a typical intermediate case) to the antisymmetric part available from the exact hydrogenic calculations of Bloch and Mendelsohn.⁴

![](./images/812716602028982273_2.jpg)

FIG. 2. Geometrical representation of parameters used in $\Delta V$ 's integration of Eq. (13):
$$
\vec{r}_{\mu}^{\prime}=\vec{r}_{\mu}+\overrightarrow{\mathrm{R}}
$$
and
$$
\vec{r}_{\mu}^{\prime \prime}=\vec{r}_{\mu}+\overrightarrow{\mathrm{R}}^{\prime}
$$
$\left(\overrightarrow{\mathrm{AA}}^{\prime}=-\overrightarrow{\mathrm{R}}, \overrightarrow{\mathrm{AA}}^{\prime \prime}=-\overrightarrow{\mathrm{R}}^{\prime}\right)$.

![](./images/812716602028982273_3.jpg)

FIG. 3. The solid line denotes the self-overlap function $S(z)$ and the dashed line denotes the $K[\Delta V(x)]$ function. Both curves are given in a universal representation.

![](./images/812716602028982273_4.jpg)

FIG. 4. The dashed line denotes the hydrogenic antisymmetric Compton defects (universal representation). Curves are independent of $K$ and $Z$. The solid line denotes Bloch and Mendelsohn (Ref. 4) at $K=3$.

### III. RESULTS

#### A. 1s orbital Compton defect

The following results are found for $\Delta V$ and $J'$, respectively:

$$
\Delta V(z, K)=\frac{e^{-z}}{K}\left[z^{2}+2 z+(C+\ln 2 z)\left(-z^{2} / 3-z-1\right)-e^{2 z} E_{i}(-2 z)\left(-z^{2} / 3+z-1\right)\right],
\tag{20}
$$

where $C$ represents the Euler constant$^{13}$ and $E_{i}$ the exponential integral function$^{13}$ and

$$
J^{\prime}(Q, k)=\frac{16}{3 \pi K Z} \frac{Q}{\left(1+Q^{2}\right)^{3}}\left\lceil\frac{3}{4}-\frac{\arctan Q}{Q}\right\rceil.
\tag{21}
$$

$S$ is positive and $\Delta V$ always negative leading to a negative shift $\delta q$. An excellent agreement is found for Eq. (21) with the exact result over all physically allowed $Q$ values.

#### B. 2s (hydrogenic) Compton defect

New results are in this case

$$
\begin{aligned}
\Delta V(z, K)=\frac{e^{-z}}{K} \Bigg[ & z^{4} / 3+2 z^{2}+4 z+2(C+\ln 2 z)\left(-\frac{z^{4}}{15}-\frac{z^{2}}{3}-z-1\right) \\
& \left.-2 e^{2 z} E_{i}(-2 z)\left(-\frac{z^{4}}{15}-\frac{z^{2}}{3}+z-1\right)\right],
\end{aligned}
\tag{22}
$$

$$
J^{\prime}(Q, k)=\frac{32}{\pi K Z} \frac{Q}{\left(1+Q^{2}\right)^{5}}\left\lceil\frac{1}{3}-4 Q+Q^{4}+\frac{8}{3} \frac{\arctan Q}{Q}\left(-\frac{2}{5}+Q^{2}-Q^{4}\right)\right\rceil.
\tag{23}
$$

The situation is found quite similar to the case of a 1s orbital. However, both $S$ and $\Delta V$ have larger spatial extension, giving rise to a larger Compton defect.

#### C. $2p_{x,y}$ Compton defect

When the momentum transfer $\vec{k}$ is used for 0z, these $2p$ orbitals have their axis perpendicular to the direction of $\vec{k}$. The following expressions are found for $\Delta V$ and $J'$:

$$
\Delta V(z, K)=\frac{e^{-z}}{K}\left\lceil\frac{7}{15} z^{3}+2 z^{2}+4 z+2(C+\ln 2 z)\left(\frac{z^{4}}{15}-z^{2}-3 z-3\right)-2 e^{2 z} E_{i}(-2 z)\left(\frac{z^{4}}{15}-z^{2}+3 z-3\right)\right\rceil,
\tag{24}
$$

$$
J^{\prime}(Q, K)=\frac{64}{15 \pi K Z} \frac{Q}{\left(1+Q^{2}\right)^{4}}\left\lceil 5-6 \frac{\arctan Q}{Q}\right\rceil.
\tag{25}
$$

The curves still correspond to those of a 1s orbital although the defect $J'$ is slightly more important. Excellent agreement is found with the exact calculation referred to above.

### D. $2p_z$ orbital case

In this situation the orbital axis is parallel to the $\vec{k}$ direction. A completely different behavior of the different function is found, due to the following expressions:

$$
\begin{aligned}
\Delta V(z, K)= & \frac{e^{-z}}{K}\left[-\frac{z^{4}}{3}-4 \frac{z^{3}}{15}+2 z^{2}+4 z+2(C+\ln 2 z)\left(\frac{z^{4}}{15}+2 \frac{z^{3}}{15}-\frac{z^{2}}{5}-z-1\right)\right. \\
& \left.-2 e^{2 z} E_{i}(-2 z)\left(\frac{z^{4}}{15}-\frac{2 z^{3}}{15}-\frac{z^{2}}{5}+z-1\right)\right],
\end{aligned}
\tag{26}
$$

$$
J^{\prime}(Q, K)=\frac{128}{15 \pi K Z} \frac{Q}{\left(1+Q^{2}\right)^{5}}\left(5+10 Q^{2}-24 Q \arctan Q\right).
\tag{27}
$$

A node exists in a widely spread self-overlap function $S$, and $\Delta V$ exhibits large positive values giving rise to a positive $\delta q$ and the most important defect.

### IV. FINAL DISCUSSION

Table I reports the calculations of $K Z \Delta^{\prime}$ [Eq. (19)] as were performed for these various orbitals from Eqs. (21), (23), (25), and (27). These slopes exactly correspond to those derived from Bloch and Mendelsohn's exact calculations at the limit of high momentum transfers. When discussing the behavior of calculated $J^{\prime}$ Compton defects for a given set of orbitals, the average energy loss $k^{2} / 2$ should be referred to their binding energy $Z^{2} / 2 n^{2}$. In order to obtain energetically similar situations, all curves $J^{\prime} K Z$ have been represented for a constant value of

$$
K=k /(Z / n)=3,
$$

which corresponds to an average energy loss equal here to 4.5 times the binding energy whatever the orbital may be. The differences observed here (Fig. 4) no longer result from the energetic features of the binding but only from geometric properties of the orbitals.

Under the previous conditions, Table I and Figs. 3 and 4 show that the magnitude of the defect is related to the overlap $S(z)$ extent. Likewise, discrepancies between the proposed treatment [Eqs. (6) and (7)] and Bloch and Mendelsohn's calculations stand out with large overlap extents $(2 s$ and $2 p_{z})$. An explanation holds in the close correspondence between $S(z)$ and $\Delta V(z, K)$ in their spatial extent. Similar features are well known $^{15}$ in molecular physics. Here, important overlaps allow for a prediction of large discrepancies between the impulse path and the real Born trajectory, resulting in a deflection due to the electrostatic fields acting upon the ejected electron. Moreover, these spatial extent effects are transferred to the intensity of the antisymmetric correction by a Fourier transform. The treatment proposed will certainly have a slower convergence for such orbitals with a wide spatial extent [and hence a wide $S(R)$ function] in the momentumtransfer direction.

Equations (6) and (7) establish a link between the antisymmetric $J^{\prime}$ Compton defect and some potential energy integrals specific of the target system. Average values of this new operator may then be (and have already been $^{16}$ ) determined experimentally. Their calculation is simple for atomic systems and a detailed study has been performed in the case of $\mathrm{He} .^{9}$ With molecular targets the defect also depends on the orientation of molecular orbitals in relation to the $\vec{k}$ direction.

The Compton defect has been shown to depend primarily on the $Z / k$ factor as caused by binding energy effects [Eq. (17)]. Furthermore, it strongly

<table>
<caption>TABLE I. $J'(KZ)$ slopes at $Q=0$ for different orbitals.</caption>
<thead>
<tr>
<th>$1s$</th>
<th>$2s$</th>
<th>$2p_{x,y}$</th>
<th>$2p_{z}$</th>
<th>$2p$ (average)</th>
<th>$L$ shell (average)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$- \dfrac{4}{3\pi}$</td>
<td>$- \dfrac{4}{3\pi}\left(\dfrac{88}{5}\right)$</td>
<td>$- \dfrac{4}{3\pi}\left(\dfrac{16}{5}\right)$</td>
<td>$\dfrac{4}{3\pi}(32)$</td>
<td>$\dfrac{4}{3\pi}\left(\dfrac{128}{15}\right)$</td>
<td>$\dfrac{4}{3\pi}(8)$</td>
</tr>
</tbody>
</table>


depends on the spatial properties of individual orbitals and their orientation in relation to the $\vec{k}$ momentum-transfer direction. The situations summarized in Table I lead to a strong positive Compton defect for a $2p_z$ orbital, while negative defects occur for $2p_{x,y}$ and $2s$ orbitals. Some simple considerations relative to the shape of $d$ and $f$ orbitals allow one to generalize the results in Table I, with the following rule: For a given orbital with azimuthal $l$ and magnetic $m$ quantum numbers, the Compton defect (just like $\Delta'$) has a positive sign for an odd $l + m$ value and a negative one for an even $l + m$ value. Compton defects for the first-row atomic elements will be discussed in a further article.

$^1$A. D. Barlas, W. Rueckner, and H. F. Wellenstein, Philos. Mag. $\underline{36}$, 201 (1977).

$^2$A. Lahmam-Bennani and A. Duguet, Chem. Phys. Lett. $\underline{74}$, 85 (1980).

$^3$R. Currat, P. D. DeCicco, and R. J. Weiss, Phys. Rev. B $\underline{4}$, 4256 (1971).

$^4$B. J. Bloch and L. B. Mendelsohn, Phys. Rev. A $\underline{9}$, 129 (1974).

$^5$C. Tavard and F. Gasser, presented at Metz, France, 1978 (unpublished); F. Gasser, Thése de 3éme Cycle, Strasbourg, 1980 (unpublished).

$^6$F. Gasser and C. Tavard, J. Chim. Phys. $\underline{78}$, 341 (1981).

$^7$F. Gasser and C. Tavard, J. Chim. Phys. $\underline{78}$, 487 (1981).

$^8$C. Tavard and R. A. Bonham, J. Chem. Phys. $\underline{50}$, 1736 (1969).

$^9$C. Tavard, M. C. Dal Cappello, F. Gasser, C. Dal Cappello, and H. Wellenstein, Phys. Rev. A (in press).

$^{10}$C.C.J. Roothaan, J. Chem. Phys. $\underline{19}$, 1445 (1951).

$^{11}$L. Van Hove, Phys. Rev. $\underline{95}$, 249 (1954).

$^{12}$W. Weyrich, P. Pattison, and B. G. Williams, Chem. Phys. $\underline{41}$, 271 (1979); A. J. Thakkar, A. Simas, and V. H. Smith, Chem. Phys. $\underline{63}$, 175 (1981).

$^{13}$M. Abarmowitz, I. A. Stegun, *Handbook of Mathematical Functions* (Dover, New York, 1965), pp. 752 and 228.

$^{14}$P. Eisenberger and P. M. Platzman, Phys. Rev. A $\underline{2}$, 415 (1970).

$^{15}$R. S. Mulliken, J. Chim. Phys. $\underline{46}$, 675 (1949).

$^{16}$A. Lahmam-Bennani, A. Duguet, and M. Rouault, J. Chem. Phys. (in press); T. C. Wong, L. B. Mendelsohn, H. Grossman, and H. F. Wellenstein, Phys. Rev. A $\underline{26}$, 181 (1982).