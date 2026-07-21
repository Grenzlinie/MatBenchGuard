Journal of the Physical Society of Japan
Vol. 59, No. 6, June, 1990, pp. 2285-2286
Short Notes

# Temperature Dependence of Spin Wave Energies in the 2D Classical Heisenberg Model with an Easy-Plane Anisotropy

Takayuki SHIRAKURA, Fumitaka MATSUBARA and Sakari INAWASHIRO

Department of Applied Physics, Tohoku University, Sendai 980
(Received December 26, 1989)

Recently some well-characterized quasi 2D easy-plane magnetic materials have been found and many experiments have been performed. $^{1-3)}$ In one of these materials, stage-2 $CoCl_{2}$-GIC, Wiesler et al. $^{3)}$ investigated the temperature dependence of spin wave energies and compared it with "the stiffness" defined on the 2D $XY$ model theoretically $^{4-6)}$ which is, for example in ref. 6, given by $\rho_{s}=$  $\langle\cos (\varphi_{i+\rho}-\varphi_{i})\rangle_{eff }$ , where $\langle\cdots\rangle_{eff } \equiv tr \cdots \exp$  $(-\beta H_{eff }) / tr \exp (-\beta H_{eff }), \ H_{eff } \equiv \frac{1}{2} \rho_{s}|J| \sum_{i, \rho}$  $(\varphi_{i+\rho}-\varphi_{i})^{2}, \beta=1 / k_{B} T$ and $i+\rho$ labels the nearest neighbor site of $i$.

A new method of a computer simulation using Langevin equations has been presented by the authers. $^{7)}$ Using the method, we investigate the temperature dependence of spin wave enrgies in the 2D classical Heisenberg model with an easy-plane anisotropy. Our results strongly suggest that the temperature dependence of spin wave energies is quite similar to that of a square root of the nearest neighbor in-plane correlation, $\langle\sigma_{i x} \sigma_{i+\rho x}$ +σ_σ_1/2 which corresponds to a square root of "the stiffness". Here $\langle\cdots\rangle$ represents the thermal average with the correct Hamiltonian, and $\sigma_{i}=(\sigma_{i x}, \sigma_{i y}, \sigma_{i z})$ a classical spin at $i$ site.

The method of the computer simulation is described in detail in ref. 7 and refered to it. All of the notations used in this note are also the same as used there. However, we use the next equation

$$\left(1 / \Gamma_{0}\right)(\mathrm{d} r / \mathrm{d} t)=\left(\frac{1}{N} \sum_{i}\left|\sigma_{i}\right|^{2}-1\right) / C, \quad (1)$$

instead of the eq. (8) in ref. 7, and we must choose $C<1 / J$ to hasten the relaxation of $r$ when $\Gamma_{0} \Delta t$ is taken to be small enough. In this note we use $C=0.1 / J$.

We perform the simulation in a ferromagnetwith anisotropic interactions $(J_{i j}^{\perp}=J>J_{i j}^{\prime \prime}$ =ηJ>0 for the nearest neighbor (n.n.) pairs) on the square lattice $(16 ×16,20 ×20)$ with the periodic boundary condition. The cases of $\eta=0,0.6$ and 0.9 are considered. We fix other parameters as $u=80 ~J$ and $\gamma / \Gamma_{0}=20$. In orderto determine the value of $\Gamma_{0} \Delta t$ , the $SRO=$ <σ_σ_+σ_σ_>1/2,s in the cases of(Γ_0Δt)^-1=160, 200 and 400 are calculated andcompared with one in the Monte Carlo (MC) method in Fig. 1(a) when $\eta=0.6$ and N=16×16 (we also performed the MC simula- tion following the standard method $^{8)}$ ). When(Γ_0Δt)^-1=160, we see that the SRO saturates to a value less than one in the limit $T \to 0$ , showing a clear difference from the MC results. This comes from the smallness of $(\Gamma_{0} \Delta t)^{-1}$ , and is more remarkable in $\eta=0.9$ than in $\eta=0.6$ . On the contrary, the SRO inη=0 behaves well at all temperatures even when $(\Gamma_{0} \Delta t)^{-1}=160$ . Because of this and thefinancial reasons, we choose $(\Gamma_{0} \Delta t)^{-1}=400$  for all $\eta$ 's, and partly $(\Gamma_{0} \Delta t)^{-1}=200$ for $\eta=0$ . The SRO's in these parameters are shown in Fig. 1(b).

We investigate the spin wave energies in a method in which we measure the response of asystem asgainst an external oscilating field. $^{7)}$  We input an oscilating field only in one direc-tion, instead of the rotational field in ref. 7(the eq. (15) in ref. 7). We applied the externalfield along two directions: $h_{i}(t)=$  $(\delta h cos (k \cdot r_{i}-\omega t), 0,0)$ and $h_{i}(t)=(0,0$ , $\delta h cos (k \cdot r_{i}-\omega t))$ for all $i$ . We could not obtain well-behaved results in the former case due to a large fluctuation of the magnetization in the $XY$ plane. Hence we concentrate on the behaviors of a $z$ -component of the response in the latter case, i.e., $Re G_{z z}(k, \omega)$ and $Im G_{z z}(k$ , $\omega)$ . The spin wave energies were investigated $^{7)}$  for some wave vectors allowed by the periodic boundary condition when $\eta=0,0.6$ and 0.9 in the temperature range $0.8 J \geq T \geq 0.1 J$ . (Wecould not obtain clear results for $T \geq 0.9 ~J$  within the same computational time as for T≤0.8J). We see that in the low temperature limit $(T \to 0)$ these approach to the valuesobtained by the Bloch eqs., $^{1,9)}(\omega_{c k}(T=0) / \gamma)^{2}$  $=(4 J)^{2}[1-\hat{\gamma}(k)][1-\eta \hat{\gamma}(k)] ;$ where $\hat{\gamma}(k)=$  $(cos (k_{x} a)+cos (k_{y} a)) / 2$ and $a$ is a lattice con

![](./images/812270510976008193_1.jpg)

Fig. 1. The SRO's against $T/J$ (a) for different $(\Gamma_0\Delta t)^{-1}$ when $\eta=0.6$; $(\Gamma_0\Delta t)^{-1}=160$ ($\nabla$), 200 ($\square$) and 400 ($\bigcirc$) compared with the MC results ($\times$), and (b) for different $\eta$ when $(\Gamma_0\Delta t)^{-1}=400$; $\eta=0$ ($\square$), 0.6 ($\bigcirc$) and 0.9 ($\nabla$). Other parameters are fixed as $N=16\times16$, $u=80$, $\gamma/\Gamma_0=20$, $n_{\text{i}}=1500$ and $n_{\text{f}}=3000$ for $(\Gamma_0\Delta t)^{-1}=160$ and 200 (and for the MC simulation), and $n_{\text{i}}=3000$ and $n_{\text{f}}=6000$ for $(\Gamma_0\Delta t)^{-1}=400$. See ref. 7 for the notations.

stant. The normalized spin wave energies, $\omega_{ck}(T)/\omega_{ck}(0)$'s, are shown in Fig. 2. Two notable resuls are seen. One is that $\omega_{ck}(T)/\omega_{ck}(0)$ for each $\eta$ depnds little on $\boldsymbol{k}$, contrary to the case of the easy-axis anisotropy. $^{7)}$ The other is the temperature dependence of these. Comparing Fig. 2 with Fig. 1(b), we find a similarity in each case of $\eta=0$, 0.6 and 0.9. In this numerical simulation, the temperature dependence of $\omega_{ck}(T)/\omega_{ck}(0)$ coincides with (or is very close to) that of the square root of the nearest neighbor in-plane correlation $\langle\sigma_{ix}\sigma_{i+px}+\sigma_{iy}\sigma_{i+py}\rangle^{1/2}$ in the low temperature phase. (Kawabata and Bishop $^{10)}$ showed by the MC method that the critical temperatures in the systems considered here are about $0.8\ J$.) These properties are roughly consistent with the Lines' suggestion $^{7)}$ and the very long correlation length in the KT phase. The detailed analysis for these properties is under consideration.

![](./images/812270510976008193_2.jpg)

Fig. 2. The temperature dependence of the normalized spin wave frequencies: $\omega_{ck}(T)/\omega_{ck}(0)$'s for $\boldsymbol{k}=(\pi/4a,\pi/4a)$ when $\eta=0$ ($\times$), 0.6 ($\bigcirc$) and 0.9 ($\nabla$), and for $\boldsymbol{k}=(3\pi/5a,0)$ when $\eta=0$ ($\square$). (Though only two results with different wave vectors at $\eta=0$ are shown for the clearness, we also investigated them for two more $\boldsymbol{k}$'s $((\pi/5a,0)$ and $(2\pi/5a,0))$ at $\eta=0$ and for another $\boldsymbol{k}((\pi/4a,0))$ at $\eta=0.6$ and these results confirm our statement about the $\boldsymbol{k}$-dependence.)

### References

1) K. Hirakawa, H. Yoshizawa and K. Ubukoshi: J. Phys. Soc. Jpn. **51** (1982) 2151.
2) M. T. Hutchings, P. Day, E. Janke and R. Pynn: J. Magn. & Magn. Mater **54-57** (1986) 673.
3) D. G. Wiesler, H. Zabel and S. M. Shapiro: The Meeting of the Physical Society of Japan, 1989, Kagoshima.
4) T. Ohta and D. Jasnow: Phys. Rev. **B20** (1979) 139.
5) D. R. Nelson and J. M. Kosterlitz: Phys. Rev. Lett. **39**(1977) 1201.
6) V. L. Pokrovskii and G. V. Uimin: Sov. Phys.-JETP **38** (1974) 847.
7) T. Shirakura, F. Matsubara and S. Inawashiro: J. Phys.: Condens. Matter **2** (1990) 2231.
8) K. Binder: *Monte Carlo Methods in Statistical Physics* (2nd ed., Springer Verlag, 1986).
9) F. G. Mertens, A. R. Bishop, G. M. Wysin and C. Kawabata: Phys. Rev. **B39** (1989) 591.
10) C. Kawabata and A. R. Bishop: Solid State Commun. **60** (1986) 169.