![](./images/811159340860833792_1.jpg)

Mechanics of Materials 26 (1997) 81-92

# Inelastic deformation of fiber composites containing bridged cracks

## F.W. Zok $^{a, *}$, M.R. Begley $^{b}$, T.E. Steyer $^{a}$, D.P. Walls $^{c}$
$^{a}$ Materials Department, University of California, Santa Barbara, CA 93106, USA
$^{b}$ Division of Applied Sciences, Harvard University, Cambridge, MA 02138, USA
$^{c}$ United Technologies, Pratt and Whitney, West Palm Beach, FL 33410, USA

Received 5 April 1996; received in revised form 25 February 1997

---

### Abstract
An analysis of the inelastic tensile deformation of a fiber composite containing multiple bridged cracks of finite length is presented. Composite strains are predicted by using crack opening areas to account for the additional inelastic strain due to the cracks. The analysis is based upon a line-spring representation of the crack surface tractions associated with bridging fibers, accounting for frictional sliding along the fiber-matrix interface with a constant shear stress. Approximate analytical solutions are derived based on the assumption that the near tip behavior of the crack dominates either the entire crack profile (for short cracks) or only a small portion of it (for long cracks). These results are compared to more detailed numerical solutions. The analysis is extended to the case of cyclic loading, incorporating the hysteresis that occurs as a result of reverse slip along the interfaces. © 1997 Elsevier Science Ltd.

---

### 1. Introduction
Fiber-reinforced titanium matrix composites (TMC) undergo multiple matrix cracking during cyclic tensile loading parallel to the fiber axis (Harmon and Saff, 1989; Walls et al., 1996). In uniform (unnotched) panels, the cracks usually initiate at the edges and propagate both through the thickness and across the width of the panel. Provided the applied stress is sufficiently low, the cracks grow past the fibers, leaving the fibers intact in the crack wake. This process is accommodated by debonding and sliding along the fiber-matrix interface.

Fig. 1 shows a typical sequence of crack patterns obtained from surface replicas taken at various stages of a fatigue test on a unidirectional Ti-6Al-4V/SCS-6 SiC composite (Steyer et al., 1997). As the cracks develop, the tensile response of the composite exhibits several changes, including: (i) a reduction in the longitudinal Young's modulus, $E$, (ii) the development of inelastic strain, manifested in a progressive broadening of the hysteresis loop and a reduction in the hysteresis modulus, $E_{\text{H}}$, and (iii) an increasing permanent strain, $\varepsilon_{\text{p}}$. Some typical measured loops illustrating these changes are shown in Fig. 2.

The objective of the present article is to present an analysis of the inelastic deformation of multiply cracked TMCs, incorporating the effects of crack length and fiber bridging. The analysis is conducted

---

* Corresponding author. Tel.: +1-805-8938699; fax: +1-805-8938486; e-mail: zok@engineering.ucsb.ecu.

0167-6636/97/$17.00 © 1997 Elsevier Science Ltd. All rights reserved.
PII S0167-6636(97)00021-5

![](./images/811159340860833792_2.jpg)

Fig. 1. Crack patterns obtained from surface replicas of a Ti-6Al-4V/SCS-6 SiC composite, following cyclic loading at a stress amplitude, $\Delta\sigma=800$, and stress ratio, $R=0$, for various numbers of cycles, $N$. The specimen width is 6.3 mm.

within the context of continuum fracture mechanics wherein the bridging fibers are treated as a distribution of tractions acting on the faces of the matrix crack, the magnitude of the tractions being governed by a characteristic bridging law. Comparisons between the analytical results and experimental measurements (of the type shown in Fig. 2) are presented also.

There is a vast body of literature on the use of line spring models to describe the effect of fibers bridging a matrix crack, for a variety of materials and bridging laws. Previous calculations have focused on the reduction in the crack tip stress intensity factor due to fiber bridging, which can be used to address questions about crack stability, toughening behavior, cyclic crack growth and fiber failure. A few notable examples of such work include Marshall et al., 1985; Nemat-Nasser and Hori, 1987; McMeeking and Evans, 1990; Cox and Lo, 1992a,b; Ghosn et al., 1992; Bakuckus and Johnson, 1993; Bao and McMeeking, 1994, 1995; and Begley and McMeeking, 1995. Since bridging traction profiles can be directly related to crack opening profiles via the bridging law, the governing equations outlined in the previous studies provide the background for the work presented here, which focuses on predicting remote displacements via crack opening areas.

Rather than recalculating complete solutions to the integral equations governing fiber bridging, use is made of the asymptotic behavior of these equations in the limit that cracks are very short or very long. The asymptotic behavior of the singular integral equations has been rigorously treated in Willis

![](./images/811159340860833792_3.jpg)

Fig. 2. Changes in the hysteresis loops associated with matrix cracking. (Data correspond to surface replicas shown in Fig. 1). Note the development of inelastic (permanent) strain and the reduction in the hysteresis modulus, $E_{\text{H}}$, with increasing cycles.

and Nemat-Nasser, 1990 and Hori and Nemat-Nasser,
1990. Such work provides the foundation for the
solutions presented here. Relevant asymptotic solu-
tions are presented in terms of the engineering quan-
tities governing crack bridging in TMCs (e.g. mod-
uli, interface sliding stress, fiber diameter, fiber vol-
ume fraction, etc.) and explained in terms of how
much the near tip behavior dominates the crack
opening profile along the crack. Full numerical solu-
tions for a limited number of cases are used to
illustrate the error associated with the asymptotic
solutions when they are not strictly applicable.

The present results are also applicable to some
CMCs: specifically, those that exhibit bridged cracks
of finite length. The response of composites contain-
ing cracks that propagate across the entire composite
section have been analyzed extensively in the past
(see, for example, Aveston et al., 1971; Hutchinson
and Jensen, 1990; Evans et al., 1994).

## 2. Preliminaries

### 2.1. General

The problem of interest is shown schematically in
Fig. 3. A unidirectionally-reinforced fiber composite
panel containing a fully bridged through-thickness
crack of length, $2a$, is subjected to an applied tensile
stress, $\sigma_{\mathrm{a}}$, parallel to the fiber axis. The additional
remote displacement, $\delta$, associated with the crack is
(Tada et al., 1985)
$$
\delta_{\mathrm{c}}=A / 2 W, \tag{1}
$$
where $2W$ is the specimen width and $A$ is the crack
area, defined by
$$
A=2 \int_{0}^{a} u(x) \mathrm{d} x \tag{2}
$$
with $u(x)$ being the effective crack opening dis-
placement (COD) $^{1}$ and $x$ the distance from the
crack center.

![](./images/811159340860833792_4.jpg)

Fig. 3. Schematic diagram showing the crack and specimen geometry.

The governing equation for the crack opening
profile for a bridged crack can be written as (Marshall
et al., 1985; McMeeking and Evans, 1990).

$$
\begin{aligned}
u(x)=f\left[\sigma_{\mathrm{b}}(x)\right]= & \frac{4 \sigma_{\mathrm{a}} a}{\overline{E}}\left(1-\left(\frac{x}{a}\right)^{2}\right)^{1 / 2} \\
& -\frac{4}{\overline{E}} \int_{0}^{a} \sigma_{\mathrm{b}}(t) H(t, x, a) \mathrm{d} t,
\end{aligned}
\tag{3}
$$

where $\sigma_{\mathrm{a}}$ is the applied stress; $H(t, x, a)$ is the
Green's function for the specimen geometry (Tada et
al., 1985); $f[\sigma_{\mathrm{b}}(x)]$ is the bridging law, usually
obtained from a cell model; and $\overline{E}$ is a composite
modulus which accounts for plane stress or strain,
and possibly orthotropy (Bao and McMeeking, 1994).
($\overline{E}$ is hereafter taken to be equal to the longitudinal
composite Young's modulus, $E$, which is obtained
from the rule of mixtures. This assumption is justi-
fied on the basis that the degree of orthotropy in
TMCs is small. Indeed, calculations by Bao and
McMeeking (1994) indicate that the difference be-
tween $\overline{E}$ and $E$ is typically only $\sim 4\%$.). The first
term on the right side of Eq. (3) is the crack opening
profile of an unbridged crack, whereas the second
term represents the reduction in the crack opening
due to bridging. In general, this equation must be

$^{1}$ For cracks bridged by fibers, $u(x)$ represents the additional
extension of the fibers associated with fiber-matrix sliding. This
differs from the actual crack opening displacement by a factor
$E_{\mathrm{m}}(1-f)/E$ (Hutchinson and Jensen, 1990).

solved numerically because of the dependence on $\sigma_{\mathrm{b}}$ of both the opening, $u$, (on the left side) and the argument of the integral (on the right side). Once the solution for $u$ is obtained at each position, $x$, it is integrated according to Eq. (2) and the result combined with Eq. (1) to obtain the additional displacement due to the crack.

For a dilute array of cracks with a number density per unit area of $\rho_{\mathrm{c}}$, the additional strain, $\varepsilon_{\mathrm{c}}$, associated with the cracks is obtained by summing the displacements from each individual crack and dividing by the appropriate length. The result is

$$
\varepsilon_{\mathrm{c}}=\delta_{\mathrm{c}} \rho_{\mathrm{c}}^{1 / 2}
$$

For the remainder of this article, attention is focused on the crack area, though its connection with the remote displacement for a single crack and the strain for a dilute array of cracks is implied through Eqs. (1) and (4).

### 2.2. Unbridged cracks
In the absence of fiber bridging (or, equivalently, when the bridging tractions are very small) the COD profile in Eq. (3) reduces to the usual elliptical form which can be integrated to get

$$
A_{\mathrm{c}}=2 \pi \sigma_{\mathrm{a}} a^{2} / E
$$

Note that, in this case, $A$ scales linearly with the applied stress, $\sigma_{\mathrm{a}}$.

### 2.3. Bridging law for TMCs
The simplest form of bridging law appropriate for TMCs is obtained by assuming that the interface sliding stress, $\tau$, is constant and subsequently performing a shear lag analysis of a single bridging fiber. Under monotonic loading, the resulting law is (Marshall et al., 1985; Hutchinson and Jensen, 1990; McMeeking and Evans, 1990)

$$
u=\lambda \sigma_{\mathrm{b}}^{2}, \quad \text { (6a) }
$$

where

$$
\lambda=D(1-f)^{2} E_{\mathrm{m}}^{2} / 4 f^{2} \tau E_{\mathrm{f}} E^{2} \quad \text { (6b) }
$$

with $D$ being the fiber diameter, $f$ the fiber volume fraction, $E_{\mathrm{m}}$ and $E_{\mathrm{f}}$ the matrix and fiber Young's modulus, respectively, and $E$ the longitudinal composite Young's modulus. Under cyclic loading, an analogous relationship exists between the COD range, $\Delta u$, during a loading-unloading cycle and the associated stress range, $\Delta \sigma_{\mathrm{b}}$, given by (McMeeking and Evans, 1990)

$$
\Delta u=\frac{1}{2} \lambda\left(\Delta \sigma_{\mathrm{b}}\right)^{2}
$$

## 3. Bridged crack under monotonic loading
For monotonic tensile loading, the displacement $\delta_{\mathrm{c}}$ is obtained by first combining the traction law of Eqs. (6a) and (6b) with Eq. (3), solving numerically for u, and then integrating u over the length of the crack. Details of the method used to solve for u are outlined in Begley and McMeeking (1995).

The COD profiles obtained in this manner exhibit two characteristic shapes (Fig. 4). When cracks are

![](./images/811159340860833792_5.jpg)

Fig. 4. COD profiles obtained for (a) $\Sigma_{\mathrm{a}}=10$ (short crack) and (b) $\Sigma_{\mathrm{a}}=0.1$ (long crack).

short and applied loads are high, the near tip behav- ior of the crack dominates the COD profile along its entire length. The result is a nearly elliptical crack opening. For longer cracks, the near tip behavior influences only a small portion of the crack, and the crack opening is constant over a large portion of its length. This can also be understood from the view- point of bridging tractions; far from the crack tip, the bridging stresses must be equal to the applied load due to equilibrium considerations. This leads imme- diately via the bridging law to constant crack open- ings. This scenario is often referred to as a steady state, since the crack tip has no effect on the majority of cracked material and vice versa. Thus, when the crack length is large or the applied stress is small, the profile is comprised of (i) an approximately elliptical region near the crack tip and (ii) a region away from the crack tip in which the opening is essentially constant. It has previously been shown that a steady-state is approached when (Cox and Lo, 1992a,b; Bao and McMeeking, 1994; Begley and McMeeking, 1995)

$$
\Sigma_{\mathrm{a}} \equiv \lambda E \sigma_{\mathrm{a}} / a<1, \quad(8)
$$

where $\Sigma_{\mathrm{a}}$ can be considered as a nondimensional measure of either the applied stress or the inverse of the crack length.

Rather than resorting to numerical methods for evaluating the COD profile exactly, an approximate analytical solution can be obtained by assuming that at least part of the crack is dominated by near tip behavior and is therefore nearly elliptical. In this case, the form of the solution depends on whether steady state conditions have been obtained. The solu- tions are developed below. The two cases (short cracks vs. long cracks) are considered separately.

### 3.1. Short cracks $(\Sigma_{a}>1)$

In this regime, the entire COD profile is assumed to be elliptical. The profile is of the general form

$$
u=u_{\mathrm{o}}\left(1-(x / a)^{2}\right)^{1 / 2}=u_{\mathrm{o}}\left(2 r / a-(r / a)^{2}\right)^{1 / 2},
$$

where $u_{\mathrm{o}}$ is the COD at the crack center $(x=0)$ and $r$ is the distance measured from the crack tip $(r=a$ $-x)$. The corresponding stress distribution (from Eqs. (6a), (6b) and (9)) is

$$
\sigma_{\mathrm{b}}=\sigma_{\mathrm{o}}\left(1-(x / a)^{2}\right)^{1 / 4}, \quad(10)
$$

where $\sigma_{\mathrm{o}}$ is the bridging stress at $x=0$. The near-tip shape must be consistent with the square root profile, given by

$$
u=\frac{8 K_{\mathrm{t}}}{E} \sqrt{\frac{r}{2 \pi}}, \quad(11)
$$

where $K_{\mathrm{t}}$ is the crack tip stress intensity factor. $K_{\mathrm{t}}$ is obtained by summing the contributions from the applied stress and from the crack bridging tractions in the standard manner (Tada et al., 1985). Using the assumed bridging stress distribution (Eq. (10)) with the appropriate weight function yields

$$
K_{\mathrm{t}}=I_{0} \sigma_{\mathrm{a}} \sqrt{\pi a}-2 I_{1} \sigma_{\mathrm{o}} \sqrt{a / \pi}
$$

with $I_{0}=1$ and $I_{1}=1.2{ }^{2}$. The near-tip profile must also be consistent with the traction law (Eqs. (6a) and (6b)), such that

$$
u=\lambda(\sigma(r))^{2} \approx \lambda \sigma_{\mathrm{o}}^{2} \sqrt{2 r / a}
$$

Combining Eqs. (11)-(13) yields

$$
\Sigma_{\mathrm{o}}^{2}+\frac{8 I_{1}}{\pi} \Sigma_{\mathrm{o}}-4 I_{0} \Sigma_{\mathrm{a}}=0, \quad(14)
$$

where $\Sigma_{\mathrm{o}}$ is a nondimensional parameter that charac- terizes the maximum bridging stress, defined by

$$
\Sigma_{\mathrm{o}} \equiv \lambda E \sigma_{\mathrm{o}} / a \quad(15)
$$

Note the first term in Eq. (14) reflects the total COD via the bridging law, the second the reduction due to bridging and the third the opening for an unbridged crack. Solving Eq. (14) for $\Sigma_{\mathrm{o}}$ yields

$$
\Sigma_{\mathrm{o}}=\frac{4 I_{1}}{\pi}\left\{\left[1+\left(\frac{\pi}{2 I_{1}}\right)^{2} I_{0} \Sigma_{\mathrm{a}}\right]^{1 / 2}-1\right\}
$$

Note that Eq. (16) is general in the sense that it applies to any crack configuration coupled with a square root bridging law. Other crack geometries will influence this expression only through the con-

---
$^{2}$ For an edge crack in an infinite body, the same result applies, with constants $I_{0}=1.12$ and $I_{1}=1.35$.

stants $I_{0}$ and $I_{1}$, which are obtained via integration of the appropriate Green's function.

The COD profile can be written in the nondimensional form
$$
\lambda E u / a^{2}=\Sigma_{\mathrm{o}}^{2}\left(1-(x / a)^{2}\right)^{1 / 2}
\qquad(17)
$$

A comparison of the approximate profile with the one calculated numerically for $\Sigma_{\mathrm{a}}=10$ is shown in Fig. 4(a). The correlation between the two is quite good, though the analytical result generally overesti- mates the COD, particularly near the crack center. The corresponding crack area is obtained by integrat- ing this profile according to Eq. (12), resulting in
$$
\lambda E^{2} A / 2 a^{3}=\frac{4 I^{2}}{\pi}\left\{\left[1+\left(\frac{\pi}{2 I_{1}}\right)^{2} I_{0} \Sigma_{\mathrm{a}}\right]^{1 / 2}-1\right\}^{2}
\qquad(18)
$$

In the limit of very short cracks $(\Sigma_{\mathrm{a}} \gg 1)$, Eq. (18) reduces to
$$
\lambda E^{2} A / 2 a^{3}=\pi \Sigma_{\mathrm{a}}
\qquad(19)
$$

It can be readily shown that this result is identical to the solution for an unbridged crack (Eq. (5)). Note, again, the linear dependence of crack area on the applied stress in this limit.

### 3.2. Steady state cracks $(\Sigma_{a} \lesssim 1)$

In this regime, the crack profile is assumed to consist of two regions: (i) a near-tip region of length $a_{*}$ where the profile is elliptical (due to the domi- nance of the tip), and (ii) a steady-state region of length $a-a_{*}$ where the COD is constant (since it is far removed from the tip).

In the near-tip region $(x<a_{*})$, the crack opening and bridging stress profiles are given by Eqs. (9) and (10), except that $\sigma_{\mathrm{o}}$ is replaced by $\sigma_{\mathrm{a}}$ and a is replaced by $a_{*}$. This represents the limiting case where the maximum bridging stress equals the ap- plied stress. The very near-tip region is again re- quired to be consistent with the square root profile (Eq. (11)) with $K_{\mathrm{t}}$ given by (Tada et al., 1985)
$$
K_{\mathrm{t}}=\sqrt{\frac{2}{\pi}} \int_{o}^{a_{*}} \frac{\sigma_{\mathrm{a}}-\sigma_{\mathrm{b}}(r)}{\sqrt{r}} \mathrm{~d} r=I_{2} \sigma_{\mathrm{a}} \sqrt{2 a_{*} / \pi},
\qquad(20)
$$
where $I_{2}=0.513$. (Note that the crack tip is assumed to be far removed from external influences; hence, the weight function of a semi-infinite geometry is used.) Combining this result with Eq. (11) gives
$$
u=8 I_{2} \sigma_{\mathrm{a}} \sqrt{a_{*} r} / E \pi
\qquad(21)
$$

As before, the near-tip profile must also be consis- tent with the traction law (Eqs. (6a) and (6b)). The critical length, $a_{*}$, is obtained by setting the expres- sions for u in Eqs. (21) and (13) equal to one another (wherein $\sigma_{\mathrm{o}} \to \sigma_{\mathrm{a}}$ ); the result is
$$
a_{*}=\lambda E \sigma_{\mathrm{a}}\left(\frac{\sqrt{2} \pi}{8 I_{2}}\right)=\gamma \lambda E \sigma_{\mathrm{a}},
\qquad(22)
$$
where $\gamma=1.08 \approx 1$. Comparison of this result with the definition of $\Sigma_{a}$ reveals that the critical length is adequately described by the condition $\Sigma_{a} \approx 1$. That is, for a given crack length $a$, the critical load at which the near tip zone encompasses the entire crack is given by $\Sigma_{a}=1$. Below this load or for crack lengths greater than $\lambda E \sigma_{a}$, the near tip zone does not dominate the entire crack length and hence a steady state region is obtained.

The crack area in the near-tip portion of the crack is
$$
\begin{aligned}
A_{1} & =2 \lambda \sigma_{\mathrm{a}}^{2} a_{*} \int_{o}^{1}\left[\frac{2 r}{a_{*}}-\left(\frac{r}{a_{*}}\right)^{2}\right]^{1 / 2} \mathrm{~d}\left(r / a_{*}\right) \\
& =I_{3} \lambda^{2} \sigma_{\mathrm{a}}^{3} E
\end{aligned}
\qquad(23)
$$
where $I_{3}=1.710$. In the steady state region, $r>a_{*}$, the crack area is simply
$$
A_{2}=\lambda \sigma_{\mathrm{a}}^{2}\left(a-a_{*}\right)=\lambda \sigma_{\mathrm{a}}^{2} a\left(1-\gamma \lambda \sigma_{\mathrm{a}} E / a\right) \quad(24)
$$

The total crack area is the sum of $A_{2}$ and $A_{1}$ which can be written in the nondimensional form
$$
\lambda E^{2} A / 2 a^{3}=\Sigma_{\mathrm{a}}^{2}-0.225 \Sigma_{\mathrm{a}}^{3}
\qquad(25)
$$

In the limit of very long cracks $(\Sigma_{a} \ll 1)$, the first term on the right side becomes dominant and the area reduces to
$$
\lambda E^{2} A / 2 a^{3}=\Sigma_{\mathrm{a}}^{2}
\qquad(26)
$$

In this limit, the crack area scales with the square of the stress. This result is equivalent to the one ob-

![](./images/811159340860833792_6.jpg)

Fig. 5. (a) Variation in crack area ($A$ or $\Delta A/2$) with applied stress ($\Sigma_{\mathrm{a}}$ or $\Delta \Sigma_{\mathrm{a}} / 2$). The solid symbols are the exact numerical results. The solid line is the approximate analytical result. (b) Differences between the numerical and analytical results.

tained from a shear lag analysis of a single bridging fiber (done originally by Aveston et al., 1971).

A comparison of the approximate COD profile with the one obtained numerically for $\Sigma_{\mathrm{a}}=0.1$ is shown in Fig. 5(b). Once again, the correlation between the two is good, though the analytic result slightly overestimates the numerical one.

Comparisons of the crack areas over a wide range of $\Sigma_{\mathrm{a}}$ (both in the short crack and the long crack regimes) are presented in Fig. 5(a); the relative differences between the two are plotted in Fig. 5(b). In general, the agreement is good for $\Sigma_{\mathrm{a}} \gg 1$ and $\Sigma_{\mathrm{a}} \ll 1$. The difference is at a maximum $(\sim 30 \%)$ at the transition between the short and long crack regimes (at $\Sigma_{\mathrm{a}}=1$ ) and diminishes as $\Sigma_{\mathrm{a}}$ either increases above or decreases below unity.

## 4. Bridged crack under cyclic loading

The integral equation that describes the crack profile under cyclic loading is obtained by replacing $u, \sigma_{\mathrm{a}}$ and $\sigma_{\mathrm{b}}$ in Eq. (3) with the corresponding changes in these parameters, $\Delta u, \Delta \sigma_{\mathrm{a}}$ and $\Delta \sigma_{\mathrm{b}}$, respectively, such that

$$
\begin{aligned}
\Delta u\left(\Delta \sigma_{\mathrm{b}}, x\right)= & \frac{4 \Delta \sigma_{\mathrm{a}}}{E}\left(1-\left(\frac{x}{a}\right)^{2}\right)^{1 / 2} \\
& -\frac{4}{E} \int_{o}^{a} \Delta \sigma_{\mathrm{b}}(t) H(t, x, a) \mathrm{d} t
\end{aligned}
$$

For the traction law of interest, the crack opening range, $\Delta u$, under cyclic loading is related to the peak crack opening under monotonic loading through the relation

$$
\Delta u=2 u\left(\Delta \sigma_{\mathrm{b}} / 2\right)
$$

Notably, the COD range is twice the value of the peak COD evaluated at a bridging stress equal to half of the bridging stress range. Upon inspection of Eq. (27), it is further recognized that the integral equation for cyclic loading can be made equivalent to the one for monotonic loading by replacing $\sigma_{\mathrm{a}}$ with $\Delta \sigma_{\mathrm{a}} / 2$ and $\sigma_{\mathrm{b}}$ with $\Delta \sigma_{\mathrm{b}} / 2$. (This connection between monotonic and cyclic loading was first identified by McMeeking and Evans (1990), and is extensively detailed by Begley and McMeeking (1995).) Consequently, $\sigma_{\mathrm{b}}$ and $\Delta \sigma_{\mathrm{b}}$ are related through

$$
\Delta \sigma_{\mathrm{b}}\left(\Delta \sigma_{\mathrm{a}}, x\right)=2 \sigma_{b}\left(\Delta \sigma_{\mathrm{a}} / 2, x\right)
$$

Recognizing these connections, the approximate analytical solutions for crack openings developed in the preceding sections can be re-interpreted for cyclic loading. It can be readily shown that the peak normalized bridging stress, $\Sigma_{0}$, is related to the bridging stress range, $\Delta \Sigma_{0}$, through a relation analogous to Eq. (29), specifically

$$
\Delta \Sigma_{o}\left(\Delta \Sigma_{\mathrm{a}}\right)=2 \Sigma_{\mathrm{o}}\left(\Delta \Sigma_{\mathrm{a}} / 2\right)
$$

Similarly, the peak crack area is related to the range in crack area, $\Delta A$, through

$$
\Delta A\left(\Delta \Sigma_{\mathrm{a}}\right)=2 A\left(\Delta \Sigma_{\mathrm{a}} / 2\right)
$$

Consequently, the results in Fig. 5(a) can be re-interpreted for cyclic loading by replacing $A$ on the ordinate with $\Delta A / 2$ and $\Sigma_{\mathrm{a}}$ on the abscissa with $\Delta \Sigma_{\mathrm{a}} / 2$.

These results can also be used to obtain the crack area, $A_{\mathrm{m}}=A-\Delta A$, at the minimum stress, $\sigma_{\mathrm{a}}-\Delta \sigma$. For short cracks $\left(\Sigma_{\mathrm{a}}>1\right)$, the minimum crack area is
$$
\lambda E^{2} A_{\mathrm{m}} / 2 a^{3}=\frac{\pi}{4}\left[\Sigma_{\mathrm{o}}^{2}-\frac{1}{2}\left(\Delta \Sigma_{\mathrm{o}}\right)^{2}\right],\quad(32)
$$
where $\Sigma_{\mathrm{o}}$ and $\Delta \Sigma_{\mathrm{o}}$ are given by Eqs. (16) and (30); for long cracks $\left(\Sigma_{\mathrm{a}}<1\right)$, it is
$$
\begin{aligned}
\lambda E^{2} A_{\mathrm{m}} / 2 a^{3}= & {\left[\Sigma_{\mathrm{a}}^{2}-0.225 \Sigma_{\mathrm{a}}^{3}\right]-2\left[\left(\Delta \Sigma_{\mathrm{a}} / 2\right)^{2}\right.} \\
& \left.-0.225\left(\Delta \Sigma_{\mathrm{a}} / 2\right)^{3}\right]
\end{aligned}\quad(33)
$$

## 5. Slip zone lengths and crack interactions

At sufficiently high stress levels, the slip zones of adjacent cracks begin to overlap. Once this occurs, the average matrix stress within the slip zone reaches a saturation value, independent of additional crack opening. Upon further opening, only the fibers support additional stress and the bridging traction law becomes linear (rather than quadratic). Consequently, the solutions presented in the preceding sections no longer apply. For a periodic array of cracks, the interactions can begin when the maximum slip length, $d_{\mathrm{s}}$, (at the crack center) reaches one half of the crack spacing, $\ell$, measured normal to the crack plane (Zok and Spearing, 1992) $^{3}$. The slip length is given by
$$
d_{\mathrm{s}}=\sigma_{\mathrm{b}} D E_{\mathrm{m}}(1-f) / 2 \tau E f,\quad(34)
$$
where $\sigma_{\mathrm{b}}$ is the maximum bridging stress.

---

$^{3}$ The onset of slip zone overlap depends on the relative offset of neighboring cracks, i.e. the relative locations of the crack centers. The present analysis considers only the case where the crack centers are directly above one another. This assumption yields a lower bound to the stress required for the onset of slip zone overlap.

![](./images/811159340860833792_7.jpg)

Fig. 6. Effect of applied stress on the critical crack spacing at which overlap occurs between slip zones of neighboring cracks.

In the short crack regime $\left(\Sigma_{\mathrm{a}} \geq 1\right)$, the maximum slip length occurs at $\sigma_{\mathrm{b}}=\sigma_{\mathrm{o}}$. The result, in nondimensional form, is
$$
\alpha d_{\mathrm{s}} / a=\Sigma_{\mathrm{o}},\quad(35a)
$$
where
$$
\alpha \equiv(1-f) E_{\mathrm{m}} / f E_{\mathrm{f}}\quad(35b)
$$
and $\Sigma_{\mathrm{o}}$ is related to $\Sigma_{\mathrm{a}}$ through Eq. (16). In the limit where $\Sigma_{\mathrm{a}} \gg 1$, Eqs. (35a) and (35b) reduces to
$$
\alpha d_{\mathrm{s}} / a=2 \sqrt{\Sigma_{\mathrm{a}}}\quad(36)
$$

The corresponding result in the long crack regime $\left(\Sigma_{\mathrm{a}} \lesssim 1\right)$ is obtained by setting $\sigma_{\mathrm{o}}=\sigma_{\mathrm{a}}$ whereupon
$$
\alpha d_{\mathrm{s}} / a=\Sigma_{\mathrm{a}}\quad(37)
$$

Trends in the critical crack spacing (obtained by setting $d_{\mathrm{s}}=\ell / 2$ ) with applied stress, $\Sigma_{\mathrm{a}}$, are plotted in Fig. 6. Below the critical value, the slip zones overlap; above it, the solutions presented in the preceding sections are expected to apply.

When the slip zones overlap and the cracks are within the steady state regime $\left(\Sigma_{\mathrm{a}}<1\right)$, a simple limiting solution for the crack area can be obtained in the following way. If $\Sigma_{\mathrm{a}} \ll 1$, then the majority of the crack has a uniform opening. In this limit, the crack area scales with $\Sigma_{\mathrm{a}}^{2}$ up to the critical stress at which the slip zones begin to overlap $\left(\Sigma_{\mathrm{a}}=\alpha \ell / 2 a\right)$.

Beyond this stress, the bridging traction law is linear, such that the crack area follows the relation

$$
A=A_{\mathrm{c}}+2 a \ell\left(\sigma-\sigma_{\mathrm{c}}\right) / f E_{\mathrm{f}}, \tag{38}
$$

where $A_{\mathrm{c}}$ and $\sigma_{\mathrm{c}}$ represent the critical values of $A$ and $\sigma$ at which the slip zones just begin to overlap. Evaluating $A_{\mathrm{c}}$ and $\sigma_{\mathrm{c}}$ (by setting $\Sigma_{\mathrm{a}}=\alpha \ell / 2 a$) and substituting the results into Eq. (38) gives the variation in the nondimensional crack area with applied stress as

$$
\lambda E^{2} A / 2 a^{3}=\left(\frac{\alpha \ell}{2 a}\right)^{2}+\frac{2 \ell E}{a f E_{\mathrm{f}}}\left(\Sigma_{\mathrm{a}}-\frac{\alpha \ell}{2 a}\right) \tag{39}
$$

The corresponding remote strain in a composite specimen containing a uniform array of cracks stacked directly above one another (such as those shown in Fig. 1) can be calculated by considering the specimen to be comprised of two parallel slabs (one containing cracks and the other uncracked), and assuming that the total tensile strain in each is the same. The inelastic strain within the cracked regions is taken as $A / \ell$, where $A$ is given by either Eq. (26) or Eq. (39), as appropriate. An additional elastic strain also arises within the cracked material; it is $\sigma / E_{*}$, where $E_{*}$ is the elastic modulus of the cracked composite (He et al., 1994). The total strain in this region is the sum of the elastic and inelastic components. In contrast, the response of the uncracked region remains elastic, with a modulus, $E$. The composite stress is then given by the weighted average of the two strength levels at a prescribed macroscopic strain, with the weighting factors being $a / W$ and $1-a / W$ for the cracked and uncracked sections, respectively.

## 6. Comparisons with experiments

A preliminary comparison between the predicted inelastic response and that measured experimentally has been performed. The tested material was a Ti-6Al-4V alloy reinforced unidirectionally with $34 \%$ by volume of SCS-6 SiC fibers. Cyclic loading experiments were performed on dog-bone shaped tensile coupons with a gauge length of $50 \mathrm{~mm}$ and width of $6.4 \mathrm{~mm}$. The strain was measured using a clip-on extensometer with a $10 \mathrm{~mm}$ gauge length.

![](./images/811159340860833792_8.jpg)

Fig. 7. Scanning electron micrograph showing periodic cracks following fatigue fracture. The specimen width is $6.3 \mathrm{~mm}$.

The test results reported here were obtained at a stress range $\Delta \sigma=800 \mathrm{MPa}$, a stress ratio $R=0$, and cycling frequency of $10 \mathrm{~Hz}$. The test was interrupted periodically and the hysteresis response measured and recorded over the stress range of 0-800 MPa. Typical hysteresis loops are shown on Fig. 2. In addition, the broad surface of the specimen was replicated using cellulose acetate tape and the replica then examined in an optical microscope. Measurements were made of both the average crack length and the average crack spacing normal to the loading direction. The cracks typically initiated at the specimen corners and propagated stably across the broad face until they linked with cracks emanating from the opposite side. Once the cracks linked, they formed a periodic array with a fixed mean spacing, as shown in Fig. 7. At this point, the crack pattern resembled that seen in unidirectional fiber-reinforced ceramic composites.

In order to assess the model predictions, the values of numerous constituent properties are needed. Most of these are well known (e.g. fiber diameter, fiber volume fraction, matrix modulus and fiber modulus) and are given in Table 1. The property which is subject to the most uncertainty is the inter-

<table><caption>Table 1 Summary of constituent properties of Ti-6Al-4V/SCS-6 fiber composite</caption>
<tbody><tr>
<td>Fiber volume fraction $f$</td>
<td>0.34</td>
</tr>
<tr>
<td>Fiber diameter $D$ ($\mu$m)</td>
<td>140</td>
</tr>
<tr>
<td>Fiber modulus $E_{\text{f}}$ (GPa)</td>
<td>410</td>
</tr>
<tr>
<td>Matrix modulus $E_{\text{m}}$ (GPa)</td>
<td>110</td>
</tr>
<tr>
<td>Interface sliding stress $\tau$ (MPa)</td>
<td>23</td>
</tr>
</tbody></table>

face sliding stress, $\tau$. It was evaluated from the hysteresis loops following complete saturation and linkage of cracks. In this regime, the cracks can be treated as being infinitely long and, provided the slip zones of adjacent cracks do not overlap, the axial response is given by (Aveston et al., 1971; Walls et al., 1996)

$$
\bar{\varepsilon}=\frac{\bar{\sigma}}{E_{*}}+\frac{(1-f)^{2} E_{\mathrm{m}}^{2} D \bar{\sigma}^{2}}{8 \tau E_{\mathrm{f}} f^{2} \ell E^{2}}, \quad(40)
$$

where $\bar{\varepsilon}$ and $\bar{\sigma}$ represent the differences in the strain and the stress from those measured at the previous load reversal, $l$ is the mean crack spacing and $E_{*}$ is the modulus of the cracked material. (Note that Eq. (40) represents the sum of the elastic and inelastic strains, the latter being obtained from Fig. 5(a) in the 'infinite crack' regime.) Once the slip zones overlap, the response is linear and given by Eq. (39). In this case, the tangent modulus is simply $f E_{\mathrm{f}}$ because only the fibers support additional stress.

To obtain $\tau$, it is convenient to differentiate Eq. (40) to get

$$
\frac{\mathrm{d} \bar{\varepsilon}}{\mathrm{d} \bar{\sigma}}=\frac{1}{E_{*}}+\frac{(1-f)^{2} E_{\mathrm{m}}^{2} D \bar{\sigma}}{4 \tau E_{\mathrm{f}} f^{2} \ell E^{2}} \quad(41)
$$

A plot of $\mathrm{d} \bar{\varepsilon} / \mathrm{d} \bar{\sigma}$ vs. $\bar{\sigma}$ is thus predicted to be linear at sufficiently low stresses, with a slope governed by $\tau$ (along with the other constituent properties) and an intercept given by $1 / E_{*}$. Fig. 8 shows such a plot. In this case, $\mathrm{d} \bar{\varepsilon} / \mathrm{d} \bar{\sigma}$ varies linearly with $\bar{\sigma}$ over the stress range 0-300 MPa. The slope of this plot along with the constituent properties in Table 1 and the measured mean crack spacing $(\ell=$ 0.69 mm) yields a sliding stress of ~ 23 MPa, and a modulus $E^{*}=182 \mathrm{GPa}$ (slightly lower than the modulus of the uncracked TMC $E_{\mathrm{o}}=203 \mathrm{GPa}$ ). At higher stress levels, the tangent modulus reaches a saturation value approximately equal to $1 / f E_{\mathrm{f}}=7.2$ $\times 10^{-6} \mathrm{MPa}^{-1}$.

![](./images/811159340860833792_9.jpg)

Fig. 8. Variation in $d \bar{\varepsilon} / d \bar{\sigma}$ with stress, $\sigma$ , for a fully-cracked specimen.

In simulating the hysteresis loops, the effects of crack spacing on the elastic modulus, $E_{*}$ , were taken into account by interpolating between the initial (uncracked) modulus, $E_{\mathrm{o}}=203 \mathrm{GPa}$ , and the one for the fully cracked panel with a crack spacing of 0.69 mm, in accordance with (He et al., 1994; Walls et al., 1996)

$$
E_{\mathrm{o}} / E_{*}=1+\phi D / \ell \quad(42)
$$

Here $\phi$ is a nondimensional parameter, determined from the experiments to be $\phi \approx 0.57$ . Moreover, the

<table><caption>Table 2 Summary of measurements ( $\Delta \sigma=800 MPa, R=0$ )</caption>
<tbody><tr>
<td>Cycle number</td>
<td>Average crack length $a$ (mm)</td>
<td>Normalized crack length $a / W$</td>
<td>Average crack spacing $\ell$ *</td>
<td>Measured hysteresis strain $\Delta \varepsilon(\%)^{a}$</td>
<td>Simulated hysteresis strain $\Delta \varepsilon(\%)^{a}$</td>
</tr>
<tr>
<td>$1 ×10^{5}$</td>
<td>0.81</td>
<td>0.25</td>
<td>0.98</td>
<td>0.414</td>
<td>0.422</td>
</tr>
<tr>
<td>$2 ×10^{5}$</td>
<td>2.66</td>
<td>0.84</td>
<td>0.84</td>
<td>0.476</td>
<td>0.513</td>
</tr>
<tr>
<td>$3.5 ×10^{5}$</td>
<td>3.97</td>
<td>~1</td>
<td>0.69</td>
<td>0.543</td>
<td>0.555</td>
</tr>
</tbody></table>

$^{a}$ Maximum-minimum.

![](./images/811159340860833792_10.jpg)

Fig. 9. Comparison of simulated and measured stress-strain curves ($\Delta\sigma=800$ MPa, $R=0$, $N=3\times10^{5}$).

cracks were treated as being in steady-state, wherein the crack opening profile is uniform along its entire length. This assumption is justified on the basis of the calculated range of $a_{\ast}$ using the constituent properties in Table 1. The maximum value of $a_{\ast}$ (evaluated at the peak stress, $\sigma=800$ MPa) is $\sim0.5$ mm, which is roughly equal to two fiber spacings. Considering that $a_{\ast}$ is proportional to $\sigma$ and hence, on average, is only $\sim0.25$ mm, and that the perti- nent crack and specimen dimensions are typically more than an order of magnitude greater than $a_{\ast}$, the variation in crack opening near the crack tip can be safely neglected. A summary of the measured crack lengths and crack spacings are presented in Table 2.

The simulated curves are shown on Fig. 9, along with the ones measured experimentally. For clarity, only the change in strains within each loop for the loading portion are presented here. The agreement between experiment and theory appears encouraging, with the maximum difference in the hysteresis strains being $\sim0.03\%$. The discrepancy is believed to be due to a crack morphology (characterized by its size and spatial distributions) which is somewhat more complex than the idealization. This issue is the sub- ject of current investigations.

## 7. Concluding remarks

The analysis presented in this paper provides approximate solutions for the area of bridged cracks in terms of the applied stress, the crack length and the various constituent properties that govern the bridging law. These solutions are based on asymptot- ically correct solutions to the governing equations which are available in the literature. They are identi- cal to the exact (numerical) results in the limiting cases of very short and very long cracks, and are overestimates near crack lengths at which steady state conditions are obtained. The results can be applied to cyclic loading through a transformation of the relevant parameters. For sufficiently low crack densities, the crack areas can be readily converted to inelastic strains. For higher densities, the conversion is more complicated; an approach for this conversion in the long crack regime has been proposed and compared with experimental results. The results are expected to find utility in modeling the development of permanent (inelastic) strain and the reduction in hysteresis modulus associated with matrix cracks during fatigue of TMCs.

## Acknowledgements

Funding for this work was provided by the ARPA University Research Initiative Program at UCSB un- der ONR contract No. N00014-92-J-1808.

## References

Aveston, J., Cooper, G.A., Kelly, A., 1971. Single and multiple fracture. In: The Properties of Fiber Composites. National Physical Laboratory, IPC Science and Technology Press, pp. 15-26.

Bakuckus, J.W., Johnson, W.S., 1993. Application of fiber bridg- ing models to fatigue crack growth in unidirectional titanium matrix composites. J. Comp. Tech. Res. 15, 242-255.

Bao, G., McMeeking, R.M., 1994. Fatigue crack growth in fiber- reinforced metal matrix composites. Acta Metall. Mater. 42, 2415-2425.

Bao, G., McMeeking, R.M., 1995. Thermomechanical fatigue cracking in fiber reinforced metal-matrix composites. J. Mech. Phys. Solids 43, 1433-1460.

Begley, M.R., McMeeking, R.M., 1995. Fatigue crack growth with fiber failure in metal-matrix composites. Comp. Sci. Tech. 53, 365-382.

Cox, B.N., Lo, C., 1992a. Load ratio, notch and scale effects for bridged cracks in fibrous composites. Acta Metall. Mater. 40, 69-80.

Cox, B.N., Lo, C., 1992b. Simple approximations for bridged cracks in fibrous composites. Acta Metall. Mater. 40, 1487-1496.

Evans, A.G., Domergue, J.M., Vaggagini, E., 1994. Methodology for relating the tensile constitutive behavior of ceramic-matrix composites to constituent properties. J. Am. Ceram. Soc. 77, 1425-1435.

Ghosn, L.J., Kantzos, P., Telesman, J., 1992. Modeling of crack bridging in a unidirectional metal matrix composite. Int. J. Fract. 54, 345-357.

Harmon, D.M., Saff, C.R., 1989. Damage initiation and growth in fiber reinforced metal matrix composites. In: Johnson, W.S. (ed.), Metal Matrix Composites Testing, Analysis and Failure Modes. ASTM STP 1032, ASTM, Philadelphia, pp. 237-250.

He, M.Y., Wu, B.X., Evans, A.G., Hutchinson, J.W., 1994. Inelastic strains due to matrix cracking in unidirectional fiber- reinforced composites. Mech. Mater. 18, 213-229.

Hori, M., Nemat-Nasser, S., 1990. Asymptotic solution of a class of strongly singular integral equations. SIAM J. Appl. Math. 50, 716-725.

Hutchinson, J.W., Jensen, H., 1990. Models of fiber debonding and pullout in brittle composites with friction. Mech. Mater. 9, 139-163.

Marshall, D.B., Cox, B.N., Evans, A.G., 1985. The mechanics of matrix cracking in brittle-matrix fiber composites. Acta Met- all. 32, 2013-2021.

McMeeking, R.M., Evans, A.G., 1990. Fatigue crack growth in fiber-reinforced metal-matrix composites. Mech. Mat. 9, 217-227.

Nemat-Nasser, S., Hori, M., 1987. Toughening by partial or full bridging of cracks in ceramics and fiber reinforced compos- ites. Mech. Mater. 6, 245-269.

Steyer, T.E., Zok, F.W., Walls, D.P., 1997. Experimental assess- ment of fatigue life and failure modes in a SiC/Ti composite. Comp. Sci. Tech., submitted.

Tada, H., Paris, P.C., Irwin, G.R., 1985. The Stress Analysis of Cracks Handbook. Del Research, St. Louis, MO.

Walls, D.P., McNulty, J.C., Zok, F.W., 1996. Multiple matrix cracking in a fiber-reinforced titanium matrix composite under high-cycle fatigue. Metall. Mater. Trans. A 27, 1899-1907.

Willis, J.R., Nemat-Nasser, S., 1990. Singular perturbation solu- tion of a class of singular integral equations. Q. Appl. Math 48, 741-753.

Zok, F.W., Spearing, S.M., 1992. Matrix crack spacing in brittle matrix composites. Acta Metall. Mater. 40, 2033-2043.