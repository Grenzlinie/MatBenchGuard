# Electrostrictive counterforce on fluid microdroplet in short laser pulse

S. Å. Ellingsen* and I. Brevik

Department of Energy and Process Engineering, Norwegian University of Science and Technology, N-7491 Trondheim, Norway
*Corresponding author: simen.a.ellingsen@ntnu.no

Received February 10, 2012; revised March 22, 2012; accepted March 22, 2012;
posted March 22, 2012 (Doc. ID 162891); published May 24, 2012

When a micrometer-sized fluid droplet is illuminated by a laser pulse, there is a fundamental distinction between two cases. If the pulse is short in comparison with the transit time for sound across the droplet, the disruptive optical Abraham–Minkowski radiation force is countered by electrostriction, and the net stress is compressive. In contrast, if the pulse is long on this scale, electrostriction is cancelled by elastic pressure and the surviving term of the electromagnetic force, the Abraham–Minkowski force, is disruptive and deforms the droplet. Ultrashort laser pulses are routinely used in modern experiments, and impressive progress has moreover been made on laser manipulation of liquid surfaces in recent times, making a theory for combining the two pertinent. We analyze the electrostrictive contribution analytically and numerically for a spherical droplet. © 2012 Optical Society of America

OCIS codes: 260.2110, 240.0240, 350.4855, 240.3990.

Consider a laser pulse impinging on a microdroplet of a homogeneous fluid, whose radius is $a$ and density is $\rho$, situated at the origin. Assume the pulse to be short (defined below), but long enough to be treated as a plane monochromatic wave. The refractive index of the droplet is $n$, its permeability $\mu = 1$, and we assume it is surrounded by vacuum for simplicity. The fluid is then acted upon by two different kinds of optical forces: a volume force in the interior due to electrostriction (ES) acting towards regions of higher electromagnetic energy density, and a surface force acting on the surface $r = a$ due to the difference in permittivity between fluid and vacuum.

When the pulse length is sufficiently long, the ES volume force is compensated by mechanical fluid pressure, and the fluid motion becomes entirely dictated by the surface force and fluid mechanical equations of motion. This was the case in the classical experiment by Zhang and Chang [1], and to our knowledge only this case has been considered in the theoretical literature [2–5]. The time it takes for the electrostrictive compressive force to be compensated depends on the compressibility of the fluid; it is approximately the time it takes for a sound wave to traverse the droplet, $\tau_c = 2a/u$, where $u$ is the speed of sound.

The effect has become accentuated in recent years because of the frequent use of short laser pulses. Moreover, in some modern applications, one works with very small surface tensions, typically in a two-fluid system such as used by Delville’s group (c.f. [6] and references therein), in which surface tension is reduced to a millionth of that of an air-water surface. The surface is thus sensitive to even small stresses.

The electromagnetic force density in a fluid is [7]
$$
\mathbf{f} = -\frac{1}{2}\epsilon_0\langle\mathcal{E}^2\rangle\nabla\epsilon + \frac{1}{2}\nabla\left[\langle\mathcal{E}^2\rangle\rho\left(\frac{\partial\epsilon}{\partial\rho}\right)_T\right], \tag{1}
$$
where $\langle\cdots\rangle$ denotes average over an optical period. According to our conventions, the constitutive relations are $\mathcal{D} = \epsilon_0\epsilon\mathcal{E}$, $\mathcal{B} = \mu_0\mathcal{H}$; thus $\epsilon$ is nondimensional, and we assume it to be real and positive. We neglect an additional Abraham term (whose existence is subject to debate), which is much smaller than the other in all typical parameter ranges [7]. Calligraphic typeface denotes real field quantities, so $\mathcal{E} = \text{Re}\{Ee^{i\omega t}\}$, etc. Note $\langle\mathcal{E}^2\rangle = \frac{1}{2}|E|^2$ and so on.

Consider first the second term in Eq. (1), the ES term, called $\mathbf{f}^{\text{ES}}$. We draw on the Lorentz–Lorenz relation to evaluate the derivative of the permittivity, whereby
$$
\mathbf{f}^{\text{ES}} = \frac{1}{6}\epsilon_0\nabla[\langle\mathcal{E}^2\rangle(n^2 - 1)(n^2 + 2)]. \tag{2}
$$

One sees that the effect from this force on the droplet is compressive, as it points towards higher optical intensity. The striction force, when taken alone, accelerates the fluid inward until an elastic counter pressure is established, on a time scale $\tau_c$. We recently considered pressure waves set in motion by a laser beam in a homogeneous fluid [8].

Secondly, there is the first term in Eq. (1), which may be called the Abraham-Minkowski (AM) term $\mathbf{f}^{AM}$, as it is common for the Abraham and Minkowski energy-momentum tensors [7]. This term is the only one to survive after the elastic response time as discussed above. Thus it is sufficient to describe the laser-induced surface deformations observed in quasistatic or long pulse experiments; see, for example, [1,6,9].

By integrating the force density [Eq. (2)] across the boundary, we obtain the ES surface pressure $\mathbf{P}^{\text{ES}}$,
$$
\mathbf{P}^{\text{ES}} = -\frac{1}{6}\epsilon_0(n^2 - 1)(n^2 + 2)\langle\mathcal{E}^2(a^-)\rangle\hat{\mathbf{n}} \equiv \sigma^{\text{ES}}\hat{\mathbf{n}}, \tag{3}
$$
where $\hat{\mathbf{n}}$ is the outward normal and $\sigma^{\text{ES}}$ is the scalar pressure, a negative quantity. In the following, we shall assume circularly polarized plane wave illumination, drawing on the Mie scattering formulation of Barton *et al.* [10]; the circularly polarized fields are given in full in [5].

According to Eq. (2), the ES force also has a volume contribution from the interior of the sphere proportional to $\nabla\mathcal{E}^2$. One could calculate this force in detail, yet for our purposes it is physically more instructive to consider

some overall properties of the ES volume force, which allows simple comparison to the AM surface force.

First, note that the net ES force on the whole sphere is zero. This is easily seen: the force (2) is a gradient, and when integrated over any volume $\mathcal{V}$, it can be written as an integral over surface area. For any control volume outside the sphere, $\partial \epsilon/\partial \rho$ is zero, hence zero total force.

Secondly, a physically instructive quantity to calculate is the full ES force (surface and volume contributions) acting on the front and back hemispheres. Choosing a control volume bisecting the sphere at $z=0$ and closed outside the sphere for $z<0$, the force may be written as an integral over the circular section only,

$$
F_{z,<}^{\mathrm{ES}}=\frac{\pi}{3} \epsilon_{0}\left(n^{2}-1\right)\left(n^{2}+2\right) \int_{0}^{a} r \mathrm{~d} r\left\langle\mathcal{E}^{2}(r)\right\rangle\left.\right|_{\theta=\frac{\pi}{2}}, \quad(4)
$$

$r$ being the radius in cylindrical coordinates. $<$ ($>$) denotes front (back) as seen by light propagating from $z=-\infty$. Exactly the same argument gives $F_{z,>}^{\mathrm{ES}}=-F_{z,<}^{\mathrm{ES}}$, which accords with zero total force.

Consider next the AM force $\mathbf{f}^{\mathrm{AM}}$, which according to Eq. (1) acts in the dielectric boundary layer only, where $\nabla \epsilon \neq 0$. The corresponding surface pressure $\mathbf{P}^{\mathrm{AM}}$ is

$$
\mathbf{P}^{\mathrm{AM}}=\frac{\epsilon_{0}}{2}\left(n^{2}-1\right)\left\langle\mathcal{E}_{t}^{2}\left(\alpha^{-}\right)+n^{2} \mathcal{E}_{r}^{2}\left(\alpha^{-}\right)\right\rangle \hat{\mathbf{n}} \equiv \sigma^{\mathrm{AM}} \hat{\mathbf{n}}. \quad(5)
$$

Here $\mathcal{E}_{t}=\mathcal{E}_{\theta} \hat{\boldsymbol{\theta}}+\mathcal{E}_{\phi} \hat{\boldsymbol{\phi}}$ is the field component parallel to the surface, and $\mathcal{E}_{r}$ the component normal to it. The expression (5) is positive, in accordance with the general property of the dielectric gradient force that it always acts in the direction of the optically thinner medium.

For comparison, we calculate the AM force on the front ($<$) and back ($>$) hemispheres,

$$
F_{z,<}^{\mathrm{AM}}=2 \pi a^{2} \int_{\pi / 2}^{\pi} \mathrm{d} \theta \sin \theta \cos \theta \sigma^{\mathrm{AM}}(\theta) \quad(6)
$$

and similarly for the back upon replacing the integral with $\int_{0}^{\pi / 2}$. Unlike for ES, the two are of unequal magnitude and the net force is a push in the direction of light propagation; the sphere acts as a lens concentrating the electromagnetic energy near the rear surface.

The field equations for circularly polarized light are straightforward to work out in the formalism of [10], and are quoted, e.g., in Appendix C of [5]. We let $\alpha=2 \pi a / \lambda_{-}=n \omega a / c$ be the number of circumferences per wavelength at frequency $\omega$. With field components $E_{r}$, $E_{\theta}$, and $E_{\phi}$ written out, the front and back hemisphere AM forces can be calculated numerically, as shown in Fig. 1, where we plot dimensionless force $Q_{\gtrless}^{\mathrm{AM}}=F_{z, \gtrless}^{\mathrm{AM}} /\left(\pi a^{2} \epsilon_{0} E_{0}^{2}\right)$, where $E_{0}^{2}$ is the rms value of the (real) electric field.

We are able to calculate the hemisphere total ES forces analytically, since at $\theta=\frac{\pi}{2}$ Legendre polynomials simplify through $P_{n}^{1}(0)=-\delta_{n 1}, P_{n}^{1 \prime}(0)=\delta_{n 0}$, and $\psi_{1}(x)=x^{-1} \sin x-\cos x$. After some straightforward calculation, we find $F_{z, \gtrless}^{\mathrm{ES}}= \pm \pi a^{2} \epsilon_{0} E_{0}^{2} Q^{\mathrm{ES}}$ with

$$
\begin{aligned}
Q^{\mathrm{ES}}= & 2\left(n^{2}-1\right)\left(n^{2}+2\right)\left\{\left|c_{1}\right|^{2}\left[4 I_{1}(n \alpha)+I_{2}(n \alpha)\right]\right. \\
& \left.+\left|d_{1}\right|^{2} I_{3}(n \alpha)\right\} /\left(8 \alpha^{2}\right),
\end{aligned} \quad(7a)
$$

$$
I_{1}(x)=\left(2 x^{4}-2 x^{2}-1+\cos 2 x+2 x \sin 2 x\right) /\left(8 x^{4}\right), \quad(7b)
$$

$$
\begin{aligned}
I_{2}(x)= & \frac{1}{2}[\gamma-1-\operatorname{Ci}(2 x)+\log 2 x \\
& \left.+x^{-2}(2 x \cos x-\sin x) \sin x\right],
\end{aligned} \quad(7c)
$$

$$
I_{3}(x)=I_{1}(x)+I_{2}(x)-\frac{x^{2}-3 \sin ^{2} x+x \sin 2 x}{2 x^{2}}. \quad(7d)
$$

Here $I_{1,2,3}$ are the radial integrals $\int_{0}^{n \alpha} \mathrm{d} \chi$ over $\psi_{1}^{2}(\chi) / \chi^{3}$, $\psi_{1}^{2}(\chi) / \chi$, and $\psi_{1}^{\prime 2}(\chi) / \chi$, respectively, resulting from insertion of $\mathcal{E}^{2}$ into Eq. (4). Ci is the cosine integral.

In Fig. 1, we compare the hemisphere forces on the front and back hemispheres due to ES and electromagnetic forces. In all figures $n=1.33$. The total AM force, dictating the center of mass motion of the droplet, is positive (pushed by the laser), whereas the total surface force is much smaller and of opposite sign, and the total surface force slightly is compressive near the focal points at the droplet's rear. ES volume forces balance the corresponding surface forces in sum since also the droplet's interior liquid is attracted to the areas of large field strength near, but not at, the droplet's rear surface. According to Eq. (2), $\left\langle\mathcal{E}^{2}\right\rangle$ acts as a potential for the electrostrictive force density, and is shown in Fig. 2 for four values of $\alpha$. The higher $\alpha$, the more electrostrictive compression is localized in small areas near the rear droplet boundary.

In Fig. 3, we show how optical surface forces are distributed over polar angles $\theta$, plotting $\sigma^{A M}(\theta), \sigma^{E S}(\sigma)$ and the sum of these, $\sigma^{\text {tot }}$. The net surface force is compressive, which serves to counteract the disruptive AM force: The AM surface force is nearly cancelled by the ES compressive force, leaving a much smaller $\sigma^{\text {tot }}$, which is compressive on average but can take small repulsive values in certain areas. The cancellation is exact for $n \rightarrow 1$, while the net surface force density becomes more strongly compressive for increasing $n$. Note correspondence with the first two panels of Fig. 2.

![](./images/813309606305464321_1.jpg)

Fig. 1. (Color online) Force components on front and rear hemispheres. Disruptive force corresponds to positive (negative) value of $Q$ for rear (front) half.

![](./images/813309606305464321_2.jpg)

Fig. 2. (Color online) Electrostriction potential $\langle\mathcal{E}^{2}\rangle/E_{0}^{2}$ inside droplet for four values of $\alpha$. Laser beam incident from left.

We have calculated the effect of ES for the optical force on a liquid droplet. The resulting behavior depends crucially on the laser pulse duration compared to the sonic transit time across the dimensions of the sphere. For example, in water at room temperature, $u \approx 1500$ m/s, so that if $a = 50$ $\mu$m, the pulse is short in this sense when $\tau \leq 70$ ns, which is well achievable in practice (current ultrashort pulses have femtosecond duration). For the purpose of optical pulling [11] of microdroplets, pulses of a few ns at intervals of about $1$ $\mu$s were found to be appropriate [5]. Laser pulses used in droplet manipulation experiments have conventionally been longer than this, allowing the elastic counter pressure time to build, cancelling the contribution from ES. Only the AM force remains, and the force is repulsive, as Fig. [1] shows. This is sufficient to explain experiments conducted to date, e.g., [1,6]. At times much earlier than $t \ll 2a/u$, however, the liquid responds both to the electrostrictive and AM forces as there is no appreciable counterforce met by elastic pressures (there is in this sense an analogy with the classic nonequilibrium pressure experiment of Goetz and Zahn from around 1960 [12,13]). Inclusion of ES is now crucial to describing the behavior of the droplet.

In order to describe droplet hydrodynamics at short times, we have shown that a fully compressible theory is required, whereas previous theoretical treatments were incompressible [2–5]. What the effect on the droplet's motion from ES will be is still an open question of great interest. No experiments exist to our knowledge in which this has been probed. It is clear that the initial deformation is to compress the droplet. If viscosity is low, overcompensation by the elastic pressure buildup would be expected to give rise after a while to surface deformations similar to those for a longer pulse, whereas with higher viscosity we expect surface oscillations to be significantly smaller due to the counteraction of ES. It seems to us that the development of a fully compressible theoretical framework for this geometry is a natural goal for the near future.

![](./images/813309606305464321_3.jpg)

Fig. 3. (Color online) Surface force densities $\bar{\sigma} = \sigma/(\epsilon_{0}E_{0}^{2})$ for AM and ES as functions of polar angle $\theta$. Polar plot of $r = \bar{\sigma}(\theta) + 20$ for illustration (20 is an arbitrary number for visualization).

## References
1. J.-Z. Zhang and R. K. Chang, Opt. Lett. **13**, 916 (1988).
2. H. M. Lai, P. T. Leung, K. L. Poon, and K. Young, J. Opt. Soc. Am. B **6**, 2430 (1989).
3. I. Brevik and R. Kluge, J. Opt. Soc. Am. B **16**, 976 (1999).
4. H. Chraïbi, D. Lasseux, E. Arquis, R. Wunenburger, and J.-P. Delville, Phys. Rev. E **77**, 066706 (2008).
5. S. Å. Ellingsen, Phys. Fluids **24**, 022002 (2012).
6. R. Wunenburger, B. Issenmann, E. Brasselet, C. Loussert, V. Hourtane, and J.-P. Delville, J. Fluid Mech. **666**, 273 (2011).
7. I. Brevik, Phys. Rep. **52**, 133 (1979).
8. S. Å. Ellingsen and I. Brevik, Phys. Fluids **23**, 096101 (2011).
9. A. Ashkin and J. M. Dziedzic, Phys. Rev. Lett. **30**, 139 (1973).
10. J. P. Barton, D. R. Alexander, and S. A. Schaub, J. Appl. Phys. **66**, 4594 (1989).
11. J. Chen, J. Ng, Z. Lin, and C. T. Chan, Nat. Photon. **5**, 531 (2011).
12. H. Goetz and W. Zahn, Z. Phys. **151**, 202 (1958).
13. W. Zahn, Z. Phys. **166**, 275 (1962).