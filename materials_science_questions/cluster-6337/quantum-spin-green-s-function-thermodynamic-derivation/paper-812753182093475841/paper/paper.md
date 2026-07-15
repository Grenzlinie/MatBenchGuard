LETTER TO THE EDITOR

# A proposal to include damping effects in the spectral density approach

L S Campana†, A Caramico D'Auria†, M D'Ambrosio†, L De Cesare‡
and U Esposito§
† Istituto di Fisica della Facoltà di Ingegneria, Napoli, Italy; and Gruppo Nazionale di
Struttura della Materia, Napoli, Italy
‡ Istituto di Fisica, Università di Salerno, Salerno, Italy; and Gruppo Nazionale di
Struttura della Materia, Salerno, Italy
§ Istituto di Cibernetica del CNR, ARCO FELICE (NA), Italy; Istituto di Fisica della
Facoltà di Ingegneria, Napoli, Italy; and Gruppo Nazionale di Struttura della Materia,
Napoli, Italy

Received 23 February 1983

Abstract. Recently there has been proposed a modification of the spectral density method
(SDM) to take into account damping effects for Fermi systems. There are in any case some
difficulties concerning Bose and classical systems. We suggest a simple way of avoiding such
difficulties and preserving the earliest idea for discussing damping effects. A classical ferro-
magnetic linear chain in external magnetic field is studied.

Recent investigations (Nolting 1979, Campana *et al* 1979) suggest that the spectral
density method (SDM) (Kalashnikov and Fradkin 1969) can be successfully applied in
situations where the usual perturbation theory fails, for instance when phase transitions
are present (Kalashnikov and Fradkin 1973, Campana *et al* 1981). It has been widely
used for quantum systems and only recently extended to treat classical systems as well
(Caramico *et al* 1981).

The method is based on the introduction of the 'spectral density'

$$
\Lambda_{A B}(\omega)=\int_{-\infty}^{+\infty} \mathrm{d} t \exp (\mathrm{i} \omega t)\left\{\begin{array}{cc}
\eta\langle[A, B(t)]_{\eta}\rangle & \text { (quantum systems) } \\
-\mathrm{i}\langle\{A, B(t)\}\rangle & \text { (classical systems) }
\end{array}\right. \tag{1}
$$

where $A$ and $B$ are two arbitrary operators or dynamical variables. In equation (1),
$\langle\ldots\rangle$ stands for the usual ensemble average, $[A, B]_{\eta}=A B+\eta B A$ ($\eta=+1\ (-1)$ for
Fermi (Bose) operators), $\{A, B\}$ is the Poisson brackets, $A(t)=\exp (\mathrm{i}\mathcal{H}t) A \exp (-\mathrm{i}\mathcal{H}t)$
($\hbar=1$) in the quantum case and $A(t)=\exp (\mathrm{i}\mathcal{L}t) A(0)$ in the classical one, where $\mathcal{L}=$
$\mathrm{i}\{\mathcal{H}, \ldots\}$ is the Liouville operator and $\mathcal{H}$ is the Hamiltonian.

According to the (quantum or classical) nature of the system one finds the following
exact 'spectral decompositions' for $\Lambda_{AB}(\omega)$:

$$
\begin{aligned}
\Lambda_{A B}(\omega)=2 \pi \mathcal{L}^{-1} & \\
& \times\left\{\begin{array}{l}
\left(\mathrm{e}^{\omega / T}+\eta\right) \sum_{m, n}\langle m|A| n\rangle\langle n|B| m\rangle \exp \left(-E_{m} / T\right) \delta\left(\omega-E_{m}+E_{n}\right) \\
(\omega / T) \sum_{n}\left\langle\psi_{n}|A\rangle\left\langle\psi_{n}^{*}|B\right\rangle \delta\left(\omega-\omega_{n}\right)
\end{array}\right. \tag{2}
\end{aligned}
$$

© 1983 The Institute of Physics
L549

L550
Letter to the Editor

where $T$ is the temperature, $\mathcal{Z}$ is the (canonical or grand canonical) partition function, $\{|n\rangle\}$ ($\{\psi_n\}$) is a complete set of orthonormal $\mathcal{H}$ eigenvectors ($\mathcal{Z}$ eigenfunctions), $E_n$ ($\omega_n$) is defined by $\mathcal{H}|n\rangle = E_n|n\rangle$ ($\mathcal{Z}\psi_n = \omega_n\psi_n$) and

$$
\langle\psi|\varphi\rangle = \int \mathrm{d}p\,\mathrm{d}q\,\exp(-\mathcal{H}/T)\,\psi^*(p,q)\,\varphi(p,q).
$$

Due to the representation (2), the standard SDM assumes for $\Lambda_{AB}(\omega)$ the 'polar ansatz (PA)':

$$
\Lambda_{AB}(\omega) = 2\pi \sum_{i=1}^{\nu} \lambda_{i}^{(A,B)} \delta(\omega - \omega_{i}^{(A,B)}) \qquad (\nu = 1,2,\dots) \tag{3}
$$

containing some free parameters to be determined in a 'self-consistent' manner by using a truncated system of spectral moment equations. Unfortunately, in this scheme, information about the damping effect of the elementary excitations are completely dropped from the beginning. It is therefore of 'practical' and 'methodological' interest to modify the method in order to take into account damping effects without any loss of its systematic and handy nature.

A modification of the SDM in this sense has been recently proposed by Nolting and Olés (1980) for Fermi systems. It is simply based on the substitution of the PA (3) with the 'gaussian ansatz (GA)':

$$
\Lambda_{AB}(\omega) = 2\pi \sum_{i=1}^{\nu} \lambda_{i}^{(A,B)} \frac{\exp\left[-(\omega - \omega_{i}^{(A,B)})^2/\Gamma_{i}^{(A,B)}\right]}{(\pi\Gamma_{i}^{(A,B)})^{1/2}} \qquad (\nu = 1,2,\dots) \tag{4}
$$

with the basic presumption $(\omega_{i}^{(A,B)})^2/\Gamma_{i}^{(A,B)} \gg 1$ in order to preserve the quasi-particle concept itself. Of course, the GA reduces to the PA for $\Gamma_{i}^{(A,B)} \to 0$. The parameters $\Gamma_{i}^{(A,B)}$, which describe the broadening of the $\delta$ poles due to the finite lifetime of elementary excitations, give a measure of the damping effects.

Unfortunately, except for Fermi systems at $T = 0$ (Nolting and Olés 1980), the use of the GA shows some limitations which reduce sensibly the effectiveness and the general character of the original SDM. Indeed, apart from difficulties of calculation which arise also for Fermi systems at $T \neq 0$, its extension to Bose and classical systems makes it problematic to preserve the physical nature of the spectral densities (not definite positive) and, simultaneously, to avoid divergence problems connected with the appearance of the factor $[\exp(\omega/T)-1]^{-1}$ or $\omega^{-1}$ in some integrals in the truncated moment equations. A detailed discussion about these points, based on more fundamental principles, is not the purpose of the present short communication and will be presented elsewhere. Here we only suggest a simple way to avoid the mentioned difficulties which preserves the idea by Nolting and Olés for discussing damping effects and does not break the generality of the SDM.

By inspection of the exact structure of the spectral decompositions (2), it becomes clear that the peculiarity, which distinguishes the Bose and classical systems from the Fermi ones, is connected with the presence of the not-everywhere-positive factors $[\exp(\omega/T)-1]$ and $\omega$ respectively. In order to include this crucial aspect of the spectral densities, together with the possibility of investigating damping effects systematically, we propose to use for $\Lambda_{AB}(\omega)$ the modified GA (MGA):

$$
\Lambda_{AB}(\omega) = 2\pi F(\omega) \sum_{i=1}^{\nu} \lambda_{i}^{(A,B)} \frac{\exp\left[-(\omega - \omega_{i}^{(A,B)})^2/\Gamma_{i}^{(A,B)}\right]}{(\pi\Gamma_{i}^{(A,B)})^{1/2}} \qquad \frac{(\omega_{i}^{(A,B)})^2}{\Gamma_{i}^{(A,B)}} \ll 1 \tag{5}
$$

$$
F(\omega)=
\begin{cases}
\exp(\omega/T)+\eta & \text{(quantum systems)} \\
\omega & \text{(classical systems)}.
\end{cases}
\tag{6}
$$

As a preliminary test of the practical utility and of the general character of the MGA, we now investigate, to the lowest approximation, damping effects in a classical isotropic spin-S ferromagnetic linear chain in an external magnetic field, very recently (Caramico et al 1981) discussed only within the polar ansatz. A detailed study, also including Bose systems, will be presented in a future paper.

We consider the classical spin-S model defined by the Hamiltonian (Caramico et al 1981, Blume et al 1975):

$$
\mathcal{H}=-I \sum_{i=1}^{N} S_{i} \cdot S_{i+1}-h \sum_{i=1}^{N} S_{i}^{z}
\tag{7}
$$

where $S_{i}$ is the angular momentum of the $i$ th particle and $I$ and $h$ are quantities proportional to the positive exchange integral and to the applied magnetic field respectively. It is convenient for us to describe the model in terms of the $2N$ canonical variables $\{\varphi_{i}, S_{i}^{z}\}$, where $\varphi_{i}$ is the angle between the projection of $S_{i}$ on the $x-y$ plane and the $x$ axis.

We introduce the spectral density

$$
\Lambda_{k}(\omega)=-\mathrm{i} \int_{-\infty}^{+\infty} \mathrm{d} t \exp (\mathrm{i} \omega t)\langle\{S_{-k}^{-}, S_{k}^{+}(t)\}\rangle
\tag{8}
$$

where $S_{k}^{\pm}=S_{k}^{x} \pm \mathrm{i} S_{k}^{y}, S_{k}^{\mu}(\mu=x, y)$ is the Fourier transform of $S_{i}^{\mu}$ and $K=0,2\pi/N \dots$ $2\pi(N-1)/N$.

We assume, according to equations (5)-(6),

$$
\Lambda_{k}(\omega)=2\pi \omega \lambda_{k} \frac{\exp \left[-(\omega-\omega_{k})^{2}/\Gamma_{k}\right]}{(\pi \Gamma_{k})^{1/2}}
\tag{9}
$$

with the basic condition $\omega_{k}^{2}/\Gamma_{k} \gg 1$. The unknown parameters $\lambda_{k}, \omega_{k}, \Gamma_{k}$ can be obtained from the moment equations (Caramico et al 1981):

$$
\int_{-\infty}^{+\infty} \frac{\mathrm{d}\omega}{2\pi} \Lambda_{k}(\omega)=2Nm
$$

$$
\int_{-\infty}^{+\infty} \frac{\mathrm{d}\omega}{2\pi} \omega \Lambda_{k}(\omega)=2I(1-\cos k) \frac{1}{N} \sum_{p} \cos p\left[\langle S_{p}^{-}S_{-p}^{-}\rangle+2\langle S_{p}^{z}S_{-p}^{z}\rangle\right]+2hNm
$$

$$
\begin{aligned}
\int_{-\infty}^{+\infty} \frac{\mathrm{d}\omega}{2\pi} \omega^{2} \Lambda_{k}(\omega)&=4I(1-\cos k)[2Im(1-\cos k)+h] \frac{1}{N} \sum_{p} \cos p\langle S_{p}^{+}S_{-p}^{-}\rangle \\
&+8I(1-\cos k)[Im(1-\cos k)+h] \frac{1}{N} \sum_{p} \cos p\langle S_{p}^{z}S_{-p}^{z}\rangle+2h^{2}Nm
\end{aligned}
\tag{10}
$$

where $m=\langle S_{i}^{z}\rangle$ and the decouplings $\langle S_{k}^{z}S_{p}^{+}S_{q}^{-}\rangle \to \langle S_{k}^{z}\rangle\langle S_{p}^{+}S_{q}^{-}\rangle$ and $\langle S_{k}^{z}S_{p}^{z}S_{q}^{z}\rangle \to$ $\langle S_{k}^{z}\rangle\langle S_{p}^{z}S_{q}^{z}\rangle$ for the higher-order correlation functions have been used.

Now it is (Caramico et al 1981):

$$
\langle S_{p}^{+}S_{-p}^{-}\rangle=T \int_{-\infty}^{+\infty} \frac{\mathrm{d}\omega}{2\pi} \frac{\Lambda_{p}(\omega)}{\omega}.
\tag{11}
$$

Furthermore, if we limit ourselves to the $\{h, T\}$ region in which $S_{i}^{z} \approx S$ so that the

approximation $S_{i}^{z} \approx S-S_{i}^{+} S_{i}^{-} / 2 S$ is valid (Blume et al 1975), we can write in equation (10)

$$
\begin{aligned}
\frac{1}{N} \sum_{p} \cos p\left\langle S_{p}^{z} S_{-p}^{z}\right\rangle \simeq & N S^{2}-\frac{1}{N} \sum_{p}\left\langle S_{p}^{+} S_{-p}^{-}\right\rangle \\
& +\frac{T}{4 S^{2}} \frac{1}{N^{3}} \sum_{k_{3} k_{4}} \exp \left[\mathrm{i}\left(k_{3}+k_{4}\right)\right] \int_{-\infty}^{+\infty} \frac{\mathrm{d} \omega}{2 \pi} \frac{\Lambda_{k_{3} k_{4}}(\omega)}{\omega}
\end{aligned}
$$

where we have introduced the higher-order spectral density:

$$
\Lambda_{k_{3} k_{4}}(\omega)=-\mathrm{i} \sum_{k_{1} k_{2}} \delta_{k_{1}+k_{2},-k_{3}-k_{4}} \int_{-\infty}^{+\infty} \mathrm{d} t \exp (\mathrm{i} \omega t)\left\langle\left\{S_{k_{1}}^{+} S_{k_{2}}^{-} S_{k_{3}}^{+}, S_{k_{4}}^{-}(t)\right\}\right\rangle. \quad(13)
$$

Then, if we use, as in the quantum case (Kalashnikov and Fradkin 1969), the decoupling procedure

$$
\Lambda_{k_{3} k_{4}}(\omega)=-\left[\delta_{k_{3},-k_{4}} \sum_{k_{1}}\left\langle S_{k_{1}}^{+} S_{-k_{1}}^{-}\right\rangle+\left\langle S_{k_{3}}^{+} S_{-k_{3}}^{-}\right\rangle\right] \Lambda_{k_{4}}(\omega)
$$

with equation (11), the moment system (10) becomes closed and we have for $\lambda_{k}, \omega_{k}, \Gamma_{k}$ the self-consistent equations

$$
\begin{aligned}
\lambda_{k}= & 2 N M / \omega_{k} \\
\omega_{k}+\Gamma_{k} / 2 \omega_{k}= & h+2 I(1-\cos k)\left[T\left(\alpha_{1}-\alpha_{2}\right)+S-\left(m T^{2} / S^{2}\right)\left(\alpha_{1}^{2}+\alpha_{2}^{2}\right)\right] \\
\omega_{k}^{2}+\frac{3}{2} \Gamma_{k}= & h^{2}+8 I^{2}(1-\cos k)^{2} m\left\{T\left(\alpha_{1}-\alpha_{2} / 2\right)+\frac{1}{2}\left[S-\left(m T^{2} / S^{2}\right)\left(\alpha_{1}^{2}+\alpha_{2}^{2}\right)\right]\right\} \\
& +4 I h(1-\cos k)\left[T\left(\alpha_{1}-\alpha_{2}\right)+S-\left(m T^{2} / S^{2}\right)\left(\alpha_{1}^{2}+\alpha_{2}^{2}\right)\right]
\end{aligned}
$$

where

$$
\begin{aligned}
m & \simeq S-T \alpha_{2} /\left(1-T \alpha_{2} / S\right) \\
\alpha_{1}(T) & =\frac{1}{\pi} \int_{0}^{\pi} \mathrm{d} p \frac{\cos p}{\omega_{p}} \\
\alpha_{2}(T) & =\frac{1}{\pi} \int_{0}^{\pi} \mathrm{d} p \frac{1}{\omega_{p}}.
\end{aligned}
$$

Under condition $\omega_{k}^{2} / \Gamma_{k} \gg 1$, equations (15) can be analytically solved in the lowtemperature limit and we have, to leading order in $T$ :

$$
\begin{aligned}
\omega_{k} & \simeq h+4 I S \sin ^{2} \frac{k}{2}\left\{1-\frac{1}{2} \frac{T}{I S^{2}}\left[1-\left(\frac{h}{h+4 I S}\right)\right]\right\}^{1 / 2} \\
\Gamma_{k} & \simeq \frac{8 I^{2}}{h(h+4 I S)} T^{2}(1-\cos k)^{2} \\
m & \simeq S-\frac{T}{[h(h+4 I S)]^{1 / 2}} .
\end{aligned}
$$

Note that, due to the approximation used for $S_{i}^{z}$, the results (17) break down at any given low temperature where the field becomes sufficiently small. They have a fully physical meaning only when $T \ll 2\left[\left(I S^{2}\right)(S h)\right]^{1 / 2}$ for low external fields.

The physical meaning of the parameter $\lambda_{k}=2 N m / \omega_{k}$ which enter the ansatz (9) for the spectral density is immediate. It is directly connected with the correlation function

$\langle S_{k}^{+} S_{-k}^{-}\rangle$. From equations (11) and (9) we have in fact

$$
\frac{1}{N S^{2}}\left\langle S_{k}^{+} S_{-k}^{-}\right\rangle=T \frac{\lambda_{k}}{N S^{2}}=\frac{2\left(m / S^{2}\right)}{\omega_{k}} T. \tag{18}
$$

In particular, in the low-temperature limit we find

$$
\frac{1}{N S^{2}}\left\langle S_{k}^{+} S_{-k}^{-}\right\rangle=\frac{2}{S}[h+2 I S(1-\cos k)]^{-1} T \tag{19}
$$

which is consistent with the exact result (Manson 1975) obtained for $h=0$.

For what concerns the frequency spectrum $\omega_{k}$ and the damping factor $\Gamma_{k}$ some remarks are in order. Firstly, our result for $\omega_{k}$ is consistent with the corresponding exact ones obtained by Reiter and Sjolander (Reiter and Sjolander 1980) in zero field. Furthermore, the gaussian peak width $\Gamma_{k}^{1 / 2}$ exhibits the correct low-temperature behaviour found for $k<\pi$ by other authors (Reiter and Sjolander 1980, Balucani *et al* 1982).

In conclusion, we wish to observe that, with the use of the MGA proposed in this communication, reasonable results have been obtained for the classical spin-$S$ model already in the previous simple approximation. However, we think that, within the spirit of the SDM, these results may be systematically improved and useful investigations about the damping effects for the Bose and Fermi systems can be also made.

### References

Balucani U, Pini M G and Tognetti V 1982 *Phys. Rev.* **B26** 4974
Blume M, Heller P and Lurie N A 1975 *Phys. Rev.* **B11** 4483
Campana L S, Caramico D'Auria A, De Cesare L and Esposito U 1979 *Physica* **95A** 417
Campana L S, D'Ambrosio M, De Cesare L 1981 *Lett. Nuovo Cimento* **32** 39
Caramico D'Auria A, De Cesare L, Esposito F and Esposito U 1980 *Nuovo Cim.* **59A** 351
Caramico D'Auria A, De Cesare L and Esposito U 1981 *Phys. Lett.* **85A** 197
Kalashnikov O K and Fradkin E S 1969 *Sov. Phys.-JETP* **28** 317
—— 1973 *Phys. Status Solidi* **b59** 9
Manson M 1975 *Phys. Rev.* **B12** 400
Nolting W 1979 *Phys. Status Solidi* **b96** 11
Nolting W and Olés A M 1980 *J. Phys. C: Solid State Phys.* **13** 2295
Reiter G and Sjolander A 1980 *J. Phys. C: Solid State Phys.* **13** 3027