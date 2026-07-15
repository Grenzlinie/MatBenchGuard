![](./images/812117233420468225_1.jpg)

Available online at www.sciencedirect.com

![](./images/812117233420468225_2.jpg)

Engineering Fracture Mechanics 73 (2006) 1086-1114

# Engineering
## Fracture
### Mechanics

www.elsevier.com/locate/engfracmech

# A technique for studying interacting cracks of complex geometry in 2D

S.C. TerMaath $^{a,*}$, S.L. Phoenix $^{b}$, C.-Y. Hui $^{b}$

$^{a}$ Exponent Failure Analysis Associates, 149 Commonwealth Drive, Menlo Park, CA 94025, USA
$^{b}$ Department of Theoretical and Applied Mechanics, Cornell University, Ithaca, NY 14853, USA

Received 5 December 2003; received in revised form 17 September 2004; accepted 19 September 2004
Available online 3 February 2006

## Abstract
A method for studying brittle fracture in an infinite plate containing interacting cracks of complex shape under general loading conditions is developed and studied for accuracy and potential applications. This technique is based on superposition and dislocation theory and can be used to determine the full stress and displacement fields in a cracked body. In addition, stress intensity factors at both crack tips and wedges, created by crack kinking and branching, are calculated so that crack growth and initiation can be analyzed at these locations of possible crack propagation. Such information can then be used to study damage accumulation in structures containing a large number of interacting cracks.

© 2004 Published by Elsevier Ltd.

Keywords: Superposition; Dislocation distribution; Interacting cracks; Stress intensity factor; Brittle fracture

## 1. Introduction
Cracks may change direction or branch as they grow due to many factors including fatigue loading conditions, preferred crack paths such as grain boundaries, material imperfections, or environmental effects (i.e., corrosion). Damage zones containing many of these randomly shaped cracks of varying size are common in aging structures. During early formation, these crack arrays, as illustrated in Fig. 1, typically consist of small cracks that may not adversely affect structural performance. However, subsequent loading could cause these cracks to propagate and coalesce into a larger failure-inducing crack. Components plagued by crack arrays include a broad range of materials and applications, and staggering replacement costs often

* Corresponding author. Tel.: +1 817 737 3131.
E-mail address: stermaath@ara.com (S.C. TerMaath).

0013-7944/$ - see front matter © 2004 Published by Elsevier Ltd.
doi:10.1016/j.engfracmech.2004.09.009

![](./images/812117233420468225_3.jpg)

Fig. 1. Random array of cracks of complex shape.

dictate life extension over part replacement. To ensure public safety and preserve structural integrity when exercising a life extension option, it is imperative to accurately predict the behavior of existing crack arrays to assess structural reliability, safety, and performance.

Evaluating such damage zones poses a challenging problem. To predict damage propagation and structural failure in cracked regions, the stress state in the material and stress intensity factors must be determined at all locations and in all directions of possible crack growth. The stress state and stress intensity factors must be calculated at crack tips, wedges formed by crack kinking (or turning), and small-scale material flaws (which may be justifiably ignored in initial modeling, but may grow and become important if located in an area with a high stress state). Limiting the scope of this problem to two-dimensional components modeled with isotropic, linear elastic material properties still leaves complex mathematical barriers to overcome.

To study interacting crack behavior under the aforementioned conditions, an analytical weighted superposition technique based on the dislocation distribution method [1] is further developed. This method is applicable to arrays of cracks of virtually any configuration with an arbitrarily selected number of straight segment lengths. Cracks need not be symmetric, periodically placed, nor limited to a certain number of crack tips or growth directions. Furthermore, loading is not restricted by type and can be any combination of shear and normal loading modes. With this technique, key equations are solved analytically, and, only minimal numerical approximations are necessary when evaluating opening displacements of cracks and stress singularities at wedge locations. Since both approximations have a negligible effect on final results, continued development of this method is a solid step forward towards accurately predicting the evolution of crack arrays.

Applications for three different types of crack shapes, V-shaped, multiply kinked, and branched, are presented. Convergence and parameter studies provide insight into efficient implementation of the method, while verification cases are included to assess accuracy. In addition, a propagation example demonstrates the use of this method to study growth of damage zones and the link-up of small cracks into a possible failure-inducing crack.

### 1.1. Literature review

Brittle rock fracture, cracking in composites, and fatigue cracking in aging aircraft are a few of the many fracture examples that may consist of crack arrays or distributed fractures. Attention in the literature has focused on many diverse solution methods for widespread applications involving this type of damage. For

example, dislocation-based analytical and hybrid-analytical methods to analyze arrays of multiple cracks are abundant in the literature (e.g. [2–11] as a representative sampling). To solve the singular integral equations involved in these methods, many researchers follow the numerical solution schemes of Erdogan et al. [12], or others [13–16]. An overview of applications and developments of the dislocation approach is provided by Hills et al. [17]. Unfortunately, few exact solutions are available for interacting cracks and cracks of complex shape; therefore, accuracy comparisons for new approaches are limited to specific crack configurations [18–22]. To evaluate cracks of complex shape, singularities occurring at kinks and branches must be considered. Williams [23,24] performed some of the first work on the classical elasticity problem of singularities at material wedges. Timoshenko and Goodier [25] and Barber [26] both included review chapters on wedge theory. Meanwhile, multiple authors have studied kinked and branched cracks [27–36]. A more comprehensive literature review can be found in TerMaath [37].

Since most researchers evaluate stress singularities and crack propagation only at crack tips, the possibility of crack development and growth is neglected elsewhere in the material. When included at wedge locations, these singularities are usually approximated, and most methods utilize numerical techniques for integration, leading to additional approximations and inaccuracies. Moreover, the application of many methods is restricted to straight cracks, and often only a small number of cracks can be evaluated in a reasonable amount of time due to computational requirements. To overcome these limitations, the following technique was developed for determining stress fields and stress intensity factors in a cracked, two-dimensional, isotropic, linearly elastic material under conditions of brittle fracture.

## 2. Mathematical formulation and concepts

The mathematical formulation is based on the dislocation distribution method, coupled to the principle of superposition applied at both the global and local levels. Additional reviews of dislocation theory and the dislocation distribution method are available [17,26,38,39].

### 2.1. Global superposition

At the global level, the cracked plate solution is the sum of two separate solutions, trivial and auxiliary (Fig. 2). The trivial problem is the given plate under the specified far field loading but without the cracks. The auxiliary problem is the given cracked plate without the far field loading, but instead, prescribed tractions applied to the crack faces. To fulfill the original boundary condition of traction-free crack faces, these tractions are equal and opposite to those induced by the stresses in the uncracked material at the location of the crack faces. Obtaining the solution to the auxiliary problem comprises the bulk of the analytical effort. Satisfying the prescribed tractions necessitates the calculation of the corresponding opening displacement profile (shape of the deformed crack) for every crack in the array.

### 2.2. Local superposition

Solving the auxiliary problem for the stress field and stress intensity factors [40] requires the development and superposition of detailed crack geometric features. To determine the opening displacements, cracks are subdivided into a series of straight segments. Each crack segment is treated as though it alone is open in an infinite plate but with an opening displacement form in terms of certain shapes that anticipate those needed to model the full crack system. A local coordinate system $(x_{i}, y_{i})$ is aligned along each crack segment $i$. For example, each arm of a V-shaped crack represents a crack segment of length $a_{i}, i=1,2$, with a unique local coordinate system (Fig. 3). To simplify notation in equations, the arbitrary parameter $t$ is aligned with $x_{i}$. For the V-shaped crack case, each segment is closed at one end (a crack tip at $t=a_{i}$). The other end $(t=0)$

![](./images/812117233420468225_4.jpg)

![](./images/812117233420468225_5.jpg)

is open, since it must connect to the opposite segment and satisfy continuity. Superposition of the local solutions for all crack segments yields the full solution to the auxiliary problem.

### 2.3. The distributed dislocation approach

Dislocations are utilized to create the prescribed crack face tractions of the auxiliary problem. Glide dislocations will produce relative tangential sliding between opposing crack faces, while climb dislocations will induce relative normal displacements. For crack segments of finite length, opening displacements are generally not equal at both ends, and the displacement between crack faces along the crack segment is not constant. Therefore, a single climb or glide dislocation is insufficient, and an array of dislocations must be applied. For crack segment, $i$, these dislocation distributions are $(\mu_{1i}(t), \mu_{2i}(t))$ for the tangential and normal directions respectively.

In local coordinate system $(x_i, y_i)$ the stress induced at an arbitrary point $(x,y)$ caused by crack segment $i$ acting alone (as though all other crack segments are closed) is written as

$$
\begin{aligned}
s_{x y}^{(i)}(x, y) & =-\frac{2 G}{\pi(1+\kappa)} \int_{0}^{a_{i}} \frac{1}{w^{4}}\left[\left((x-t)^{2}-y^{2}\right) y \mu_{2 i}+\left((x-t)^{2}-y^{2}\right)(x-t) \mu_{1 i}\right] \mathrm{d} t \\
s_{y y}^{(i)}(x, y) & =-\frac{2 G}{\pi(1+\kappa)} \int_{0}^{a_{i}} \frac{1}{w^{4}}\left[\left((x-t)^{2}+3 y^{2}\right)(x-t) \mu_{2 i}+\left((x-t)^{2}-y^{2}\right) y \mu_{1 i}\right] \mathrm{d} t \\
s_{x x}^{(i)}(x, y) & =-\frac{2 G}{\pi(1+\kappa)} \int_{0}^{a_{i}} \frac{1}{w^{4}}\left[\left((x-t)^{2}-y^{2}\right)(x-t) \mu_{2 i}+\left(3(x-t)^{2}-y^{2}\right) y \mu_{1 i}\right] \mathrm{d} t
\end{aligned}
\tag{1}
$$

where $w=\sqrt{(x-t)^{2}+y^{2}}$. The shear modulus of the material is $G$, and $v$ is Poisson's ratio. Kosolov's constant is denoted by $\kappa$ ($(3-4v)$, for plane strain, and $(3-v)/(1+v)$, for plane stress). These equations can be recast with a complex variable formulation, $z=x+\mathrm{i}y$ (Eqs. (2)).

$$
\begin{aligned}
s_{x y}^{(i)}(z) & =-\frac{2 G}{\pi(1+\kappa)}\left\{y \operatorname{Re}\left(Z_{2 i}^{2}\right)+\operatorname{Re}\left(Z_{1 i}^{1}\right)+y \operatorname{Im}\left(Z_{2 i}^{1}\right)\right\} \\
s_{y y}^{(i)}(z) & =-\frac{2 G}{\pi(1+\kappa)}\left\{\operatorname{Re}\left(Z_{1 i}^{2}\right)-y \operatorname{Im}\left(Z_{2 i}^{2}\right)+y \operatorname{Re}\left(Z_{2 i}^{1}\right)\right\} \\
s_{x x}^{(i)}(z) & =-\frac{2 G}{\pi(1+\kappa)}\left\{\operatorname{Re}\left(Z_{1 i}^{2}\right)+y \operatorname{Im}\left(Z_{2 i}^{2}\right)+2 \operatorname{Im}\left(Z_{1 i}^{2}\right)-y \operatorname{Re}\left(Z_{2 i}^{1}\right)\right\}
\end{aligned}
\tag{2}
$$

$Z_{1i}^{\eta}$ and $Z_{2i}^{\eta}$, are Cauchy singular integrals to be evaluated in closed form in terms of the dislocation distributions (Eqs. (3)). When the point $(x,y)$ falls on a crack segment, these integrals are solved for the Cauchy principal value.

$$
\begin{aligned}
Z_{1 i}^{\eta} & =\int_{0}^{a_{i}} \frac{\mu_{\eta i}(t) \mathrm{d} t}{z-t} \\
Z_{2 i}^{\eta} & =\int_{0}^{a_{i}} \frac{\mu_{\eta i}(t) \mathrm{d} t}{(z-t)^{2}}=-\frac{\mathrm{d}}{\mathrm{d} z} Z_{1 i}^{\eta}
\end{aligned}
\tag{3}
$$

The total stress at a given point in the auxiliary problem, $\sigma$, is the sum of the contributions, $s$ (Eqs. (2)), from all crack segments after they are converted to the global coordinate system (identified by capital letters). With $c$ as the number of crack segments,

$$
\sigma_{X Y}=\sum_{i=1}^{c} s_{X Y}^{(i)} \quad \sigma_{Y Y}=\sum_{i=1}^{c} s_{Y Y}^{(i)} \quad \sigma_{X X}=\sum_{i=1}^{c} s_{X X}^{(i)}
\tag{4}
$$

### 2.4. Enforcing the traction-free condition

To obtain traction-free crack faces in the full problem, series of equations in both the tangential and normal directions are enforced simultaneously at a given set of points along each crack segment. At point $(X, Y)$ in the global coordinate system, these equations take the form

$$
\begin{aligned}
\sigma_{X Y}^{\infty} n_{Y}+\sigma_{X X}^{\infty} n_{X} &=-n_{Y} \sigma_{X Y}-n_{X} \sigma_{X X} \\
\sigma_{Y Y}^{\infty} n_{Y}+\sigma_{X Y}^{\infty} n_{X} &=-n_{Y} \sigma_{Y Y}-n_{X} \sigma_{X Y}
\end{aligned}
\tag{5}
$$

The left sides of Eqs. (5) are the prescribed tractions induced at the crack faces by the loading conditions, while the right sides represent the tractions caused by the opening displacements (dislocation distributions) of the crack segments (Eqs. (4)). Also, $n_{X}$ and $n_{Y}$ are the normals to the bottom crack face. The $\sigma^{\infty}$ are the far field stresses applied to the plate in the directions denoted by their subscripts. Dislocation distributions, $\mu_{1 i}$ and $\mu_{2 i}$, must be determined that satisfy these equations for every crack segment.

### 2.5. Solving for dislocation distributions

Enforcing the prescribed tractions (Eqs. (5)) at a sufficient number of points along each crack segment in an array of cracks results in a large system of equations. Furthermore, constraints applied to adjoining crack segments (required to enforce displacement continuity and to eliminate mathematically induced but non-physical singularities) produce additional algebraic equations that must be satisfied explicitly. For a single crack with a complex geometry (or an array of cracks with complex geometries, where the crack face tractions are influenced by the opening displacements of the other cracks), exact solutions for the dislocation distributions typically cannot be obtained and must be approximated.

A library of dislocation distributions, as described shortly, was created for the standard crack segment shapes required to analyze V-shaped, multiply kinked, and branched cracks. Dislocation distributions will be calculated as the derivatives of certain opening displacement profiles (opening shapes of the crack segments). Development of these opening displacement profiles is based on solid and fracture mechanics fundamentals, resulting in different types of series, each representing a specific characteristic of crack segment behavior. Every individual term in a series is multiplied by a weighting coefficient (or degree of freedom) whose value is determined by the solution of Eqs. (5), and each type of series is used independently in both the tangential and normal modes of deformation.

To maximize computational efficiency, points where the traction conditions are enforced are allocated along crack segments according to the leverage effects of an equal and opposite opening point force pair on stress intensities (i.e., at tips, kinks, and branches). This scheme (presented in Appendix A) allows for a greater density of points to be allocated near the ends of crack segments, where accuracy is more difficult to achieve and traction errors more significantly affect results. Points must be assigned in sufficient numbers to fully capture crack behavior, and increasing the number of points is computationally less demanding than adding additional degrees of freedom. Thus, the minimum number of degrees of freedom (columns in the matrix), necessary for convergence and accuracy will be included in an analysis, while adequate points (rows in the matrix) will be assigned to capture traction behavior. This selection of points and number of terms produces an over-determined matrix that is solved by a least squares fit. This solution method has the advantage of yielding an error estimate based on the fit of the tractions induced by the computed opening displacement profile, as compared to the prescribed tractions.

### 3. Opening displacement series

Different types of series (wedge, polynomial, and tip) comprise the library of opening displacement profiles (or dislocation distributions). Poor convergence and increased computation time arise when terms of different series compete to represent similar behavior, as demonstrated by near cancellation of extremely large equal and opposite weighting coefficients. To prevent this difficulty and to minimize computation time through efficient use of degrees of freedom, each term from each type of series must independently represent a specific physical characteristic. And, to prevent non-physical singularities, series are constrained for zero

![](./images/812117233420468225_6.jpg)

Fig. 4. Multiply kinked crack.

opening displacement and zero slope (first derivative) at their end points. In exploratory work, additional constraints applied to the third and fourth derivatives were found to impede convergence [37]. Therefore, while series must be prohibited from non-physical singular behavior, they must retain enough ability to per- form minor shaping adjustments. Details for evaluating the Cauchy singular integrals for each type of term are presented in Appendix B. Crack segments are defined as interior or exterior depending on whether they include a crack tip (i.e. Fig. 4 for a multiply kinked crack).

### 3.1. Wedge series

A power series based on Williams' [23] displacement equation (Eq. (6)) for a traction free wedge (Fig. 3) is developed to include the effects of wedge distortions at kinks and material singularities and has the form

$$
\mathrm{OD}(r, \theta) \approx \sum_{\rho} c_{\rho}(\theta) r^{\rho}
\tag{6}
$$

where the $\rho$ are eigenvalues that satisfy either of the two boundary conditions (for the mating wedges)

$$
\begin{aligned}
\sin (\rho \omega) & = \pm \rho \sin (\omega) \\
\sin (\rho(2 \pi-\omega)) & = \pm \rho \sin (\omega)
\end{aligned}
\tag{7}
$$

Only eigenvalues greater than zero automatically satisfy the opening displacement continuity condition across kinks, and only an eigenvalue whose real part is less than one will cause a stress singularity. At wedge locations, there is always a dominant $\rho_{1}$ eigenvalue less than unity representing a circumferentially symmet- ric, singular stress field in the lower wedge, Mode I. There is a second singular eigenvalue, $\rho_{2}$, when the lower wedge angle is greater than $257.4^{\circ}$, accounting for a circumferentially anti-symmetric singular stress field, Mode II. Eigenvalues that do not cause singularities are not explicitly included in the analysis, since their effects are approximated by the higher order terms of the series. In addition, the eigenvalues $\rho=0$ and1 that model relative translation and rotation of upper and lower wedges also satisfy Eqs. (7) but are in- cluded in the polynomial series considered shortly.

Though a wedge may be flanked by crack segments of different lengths, $a_{1}$ and $a_{2}$, the generic symbol $a$ is used when writing series equations to simplify notation. The general form of a wedge series, $W(t)$, for a crack segment emanating from a kink is given by

$$
W(t)=c_{\rho 0}\left(\frac{t}{a}\right)^{\rho}+c_{\rho 1}\left(\frac{t}{a}\right)^{\rho+1}+c_{\rho 2}\left(\frac{t}{a}\right)^{\rho+2}+\cdots+c_{\rho n}\left(\frac{t}{a}\right)^{\rho+n}
\tag{8}
$$

where $n$ is fixed, depending on the desired accuracy, and $\rho$ is either $\rho_{1}$ or $\rho_{2}$. The $c_{\rho j}$ are the weighting coef ficients. Applying conditions to prohibit (from this series) a displacement jump and non-zero slope of the opening profile at the opposite end of the crack segment reduces the number of weighting coefficients to $n-1$ resulting in the final form of the wedge series (Eq. (9)).

![](./images/812117233420468225_7.jpg)

Fig. 5. Wedge opening displacement shapes for $n=3$ and $\rho=0.7$.

$$
W(t)=\sum_{j=0}^{n-2} c_{\rho j}\left(\left(\frac{t}{a}\right)^{\rho+j}-(n-j)\left(\frac{t}{a}\right)^{\rho+n-1}+(n-j-1)\left(\frac{t}{a}\right)^{\rho+n}\right), \quad n \geqslant 2
\tag{9}
$$

When both $\rho_{1}$ and $\rho_{2}$ apply to a wedge angle, a separate wedge series must be included for each eigenvalue, and both series must be assigned separately to all adjoining crack segments to the wedge. Therefore, an interior crack segment with a kink at each end could conceivably be assigned four wedge series, as two eigenvalues could exist for the wedge at each kink. In this case, two series, $W(t)$, originate from the local segment coordinate origin, and two additional series written as $W(a-t)$, would represent the wedge at the opposite end of the crack segment. If a crack is branched, wedge terms are included only when the junction contains a wedge angle greater than $180^{\circ}$, the limit to produce singular eigenvalues.

Shapes for individual components of Eq. (9) follow the two general forms depicted in Fig. 5. When $j=0$, the shape has an infinite slope at the kink end, since $\rho+j<1$ (representing the singularity as $t$ approaches 0 ). Therefore, wedge series for each crack segment emanating from a kink, and thus sharing the same $\rho$ value, require constraints relating their $c_{\rho 0}$ coefficients to eliminate unwanted non-physical singularities in the tractions at the kink. The final form of the constraints is given in Appendix C, and a detailed derivation is contained in [37]. The shapes for $j \geqslant 1$ (e.g., right example for $\rho+j=1.7$ ) approximate the influence of higher order eigenvalues and do not generate a singularity at either end.

### 3.2. Polynomial series

Polynomial series account for the $\rho=0$ and 1 eigenvalue effects (opening and rotation) and also perform the task of manipulating the overall shape of the crack segment opening displacement profile by allowing greater flexibility in midspan deformations. A polynomial series of degree $n$ is simply a wedge series with $\rho=0$; therefore, the constrained polynomial series, $P(t)$, is written as

$$
P(t)=\sum_{j=0}^{n-2} c_{0 j}\left(\left(\frac{t}{a}\right)^{j}-(n-j)\left(\frac{t}{a}\right)^{n-1}+(n-j-1)\left(\frac{t}{a}\right)^{n}\right), \quad n \geqslant 2
\tag{10}
$$

As with the wedge series, polynomial series can also be applied as $P(a-t)$ depending on local coordinate system orientation relative to the crack segment. When applied to interior crack segments, however, one end should be restricted to $n=3$ (two degrees of freedom, $c_{00}$ and $c_{01}$ ), controlling only the slope and opening displacement at that end. This restriction avoids redundant higher order terms emanating across a single crack segment from both ends (resulting in a rank deficiency in the matrix inversions) but retains the necessary shaping for the opening displacements and slopes at both ends.

Fig. 6 shows the shapes of components associated with $c_{00}, c_{01}$ and $c_{02}$ for $n=5$. The $j=0$ shape has a jump opening, associated with $(t / a)^{0}=1$, that allows translation of an upper wedge relative to its lower counterpart. The non-physical singularity induced by this shape is removed by applying constraints to enforce continuity of opening displacements between adjoining crack segments (Appendix C). For $j=1$,

![](./images/812117233420468225_8.jpg)

Fig. 6. Polynomial opening displacement shapes for $n=5$.

the slope discontinuity, $(t/a)^1$, is another source of a non-physical singularity that is eliminated once constraints on adjoining crack segments are applied. This shape allows for relative rotation of upper and lower wedges in addition to other possible linear distortions in shear. The shapes for the higher order terms (e.g., $j=2$) manipulate the overall shape of opening displacement profiles. These terms have zero displacement and slope at both ends and require no additional constraints.

### 3.3. Tip series

Tip series incorporate crack tip behavior including the square-root singularity and higher order behavior [41]. Therefore, they are only included in opening displacement profiles of exterior crack segments. Tip series are constructed as series of powers to the order $(2j+1)/2$ to exclude redundant integer terms that are already included in the polynomial series. Tip series are subject to the constraints of zero slope and displacement at the kink or branch end of a crack segment, since they always originate from crack tips (Eq. (11)).

$$
T(t)=2 \sum_{j=0}^{n-2} c_{(1 / 2), j}\left(\left(\frac{a-t}{a}\right)^{\frac{2 j+1}{2}}-(n-j)\left(\frac{a-t}{a}\right)^{\frac{2(n-1)+1}{2}}+(n-j-1)\left(\frac{a-t}{a}\right)^{\frac{2 n+1}{2}}\right), \quad n \geqslant 2
\tag{11}
$$

Eq. (11) applies to an origin located at the kink or branch end of an exterior crack segment. The factor 2 in front of the series provides coefficient consistency with the wedge series, since a crack tip is a wedge with a collapsed mating wedge $(\omega \rightarrow 0)$. No additional constraints are required, since non-physical singularities are not induced by these terms. The shape for $j=0$ represents the square-root singularity (Fig. 7). The shape of the $j=1$ term with leading exponent 1.5 is similar to the shape depicted in Fig. 5 for the leading exponent 1.7.

![](./images/812117233420468225_9.jpg)

Fig. 7. Tip opening displacement shape for $n=2$, $j=0$.

## 4. Calculation of stress intensity factors

Stress intensity factors are calculated at both crack tip and wedge locations using the weighting coefficients corresponding to the terms inducing singular behavior. At the crack tips, the equations for the Mode I and Mode II stress intensity factors, $K_{\text{I}}$ and $K_{\text{II}}$ respectively, are

$$
\left(\begin{array}{l}
K_{\text{I}} \\
K_{\text{II}}
\end{array}\right)=\frac{2 G}{1+\kappa} \sqrt{\frac{2 \pi}{a}}\left(\begin{array}{l}
c_{(1 / 2) 0}^{[2]} \\
c_{(1 / 2) 0}^{[1]}
\end{array}\right) \tag{12}
$$

where $c_{(1 / 2) 0}^{[1]}$ and $c_{(1 / 2) 0}^{[2]}$ are the weighting coefficients for the $j=0$ tip terms representing the square-root singularity. The superscript notations, [1] and [2], denote the tangential and normal directions respectively. At the kink, generalized stress intensity factor equations are

$$
\begin{aligned}
K_{\mathrm{I}} & =-\frac{2 G}{1+\kappa}(2 \pi)^{\left(1-\rho_{1}\right)} \rho_{1}\left(\rho_{1}+1\right)\left(1-\frac{\cos \left[\left(\rho_{1}-1\right) \omega^{\prime} / 2\right]}{\cos \left[\left(\rho_{1}+1\right) \omega^{\prime} / 2\right]}\right) \frac{c_{\rho_{1} 0}^{[2]} / a^{\rho_{1}}}{\sin \left[\left(\rho_{1}-1\right) \omega^{\prime} / 2\right]} \\
K_{\mathrm{II}} & =-\frac{2 G}{1+\kappa}(2 \pi)^{\left(1-\rho_{2}\right)} \rho_{2}\left(\rho_{2}+1\right)\left(\frac{\sin \left[\left(\rho_{2}-1\right) \omega^{\prime} / 2\right]}{\sin \left[\left(\rho_{2}+1\right) \omega^{\prime} / 2\right]}-\frac{\rho_{2}-1}{\rho_{2}+1}\right) \frac{c_{\rho_{2} 0}^{[1]} / a^{\rho_{2}}}{\sin \left[\left(\rho_{2}-1\right) \omega^{\prime} / 2\right]}
\end{aligned} \tag{13}
$$

where $\omega^{\prime}=360^{\circ}-\omega$. When $\rho_{2}<1$ does not exist for certain wedge angles, $K_{\text{II}}$ at the kink is irrelevant. A detailed derivation of Eqs. (13) is provided in Appendix D. For $\omega=0$ and $\rho=1 / 2$, these equations collapse to those for a crack tip, Eq. (12).

## 5. V-shaped cracks

Two crack segments forming the shape of a V with angle $\omega$ define a V-shaped crack (Fig. 8). In addition to verifying the accuracy of the method, this configuration was used to investigate convergence, point allocation, and the effects of eigenvalue approximation. Eigenvalues and their rational number approximations, $\alpha / \beta$, corresponding to various values of $\theta$ ($\omega=180^{\circ}-\theta$) are listed in Table 1. These values will be used in all subsequent calculations unless specified otherwise.

To verify accuracy, results from this method were compared with results from other methods [37]. Since crack tip stress intensity factors are typically the only values specified in the literature, this parameter formed the basis for comparison. However, for all examples addressed in this paper, tractions on all crack segments were evaluated and matched those prescribed in the auxiliary problem with high accuracy, and generalized stress intensity factors computed at wedges displayed rapid convergence. First, a straight crack ($\theta=0$) divided into two crack segments with varying segment lengths and loading conditions was studied, and the results from all cases matched Irwin's [42] exact results. And, multiple configurations of a single V-shaped crack were analyzed, including varying crack segment lengths, loading conditions (tension, shear,

![](./images/812117233420468225_10.jpg)

Fig. 8. V-Shaped crack in an infinite plate.

<table>
<caption>Table 1 Wedge eigenvalues for varying values of $\theta=180^{\circ}-\omega$</caption>
<thead>
<tr>
<th>$\theta$</th>
<th>$\rho$</th>
<th>$\rho_{\text{approx}}=\alpha/\beta$</th>
<th>Relative error (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$30^{\circ}$</td>
<td>0.7519745</td>
<td>70/93</td>
<td>0.095</td>
</tr>
<tr>
<td>$45^{\circ}$</td>
<td>0.6735834</td>
<td>31/46</td>
<td>0.049</td>
</tr>
<tr>
<td>$60^{\circ}$</td>
<td>0.6157311</td>
<td>8/13</td>
<td>0.056</td>
</tr>
<tr>
<td>$90^{\circ}$</td>
<td>0.5444837</td>
<td>43/79</td>
<td>0.033</td>
</tr>
<tr>
<td></td>
<td>0.9085292</td>
<td>10/11</td>
<td>0.062</td>
</tr>
<tr>
<td>$120^{\circ}$</td>
<td>0.5122214</td>
<td>21/41</td>
<td>0.005</td>
</tr>
<tr>
<td></td>
<td>0.7309007</td>
<td>19/26</td>
<td>0.018</td>
</tr>
</tbody>
</table>

and biaxial), and deviation angles. Results agreed with those of other researchers who utilized a variety of methods [31,43-46].

### 5.1. Effect of point allocation on convergence

Enforcing tractions at only a few points will lead to nearly exact correlation in those regions, but accu- racy will be compromised elsewhere. Therefore, a sufficient number of points must be assigned along crack faces to sufficiently capture traction behavior. Since computation time is proportional to the number of points, it is imperative to optimize point allocation.

An error estimate is quantified through the fit of the tractions induced by the computed opening dis- placement profiles as compared to the prescribed tractions. This error estimate (relative root mean square

<table>
<caption>Table 2
Convergence results for varying number of points for $120^\circ$ V-shaped crack with unit crack segment lengths loaded in unit tension</caption>
<thead>
<tr>
<th>Number of points</th>
<th>$K_{\text{I}}$</th>
<th>$K_{\text{II}}$</th>
<th>$K_{\text{I,kink}}$</th>
<th colspan="2">RRMS error</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th>Normal</th>
<th>Shear</th>
</tr>
</thead>
<tbody>
<tr>
<td>25</td>
<td>1.2548</td>
<td>0.8456</td>
<td>$-0.4494$</td>
<td>$1.50 \times 10^{-5}$</td>
<td>$1.46 \times 10^{-5}$</td>
</tr>
<tr>
<td>30</td>
<td>1.2548</td>
<td>0.8456</td>
<td>$-0.4494$</td>
<td>$1.52 \times 10^{-5}$</td>
<td>$2.52 \times 10^{-5}$</td>
</tr>
<tr>
<td>40</td>
<td>1.2548</td>
<td>0.8456</td>
<td>$-0.4493$</td>
<td>$1.44 \times 10^{-5}$</td>
<td>$4.46 \times 10^{-5}$</td>
</tr>
<tr>
<td>50</td>
<td>1.2548</td>
<td>0.8456</td>
<td>$-0.4492$</td>
<td>$1.34 \times 10^{-5}$</td>
<td>$6.08 \times 10^{-5}$</td>
</tr>
<tr>
<td>100</td>
<td>1.2548</td>
<td>0.8456</td>
<td>$-0.4490$</td>
<td>$9.74 \times 10^{-6}$</td>
<td>$1.10 \times 10^{-4}$</td>
</tr>
</tbody>
</table>

error, RRMS) is calculated by dividing the sum of the squared errors of the fit at each point by the sum of the squared applied tractions, dividing by the number of points, and then taking the square root of this quantity.

Table 2 lists results obtained for varying number of points for a V-shaped crack (Fig. 8) with unit crack segment lengths $(a_1 = a_2 = 1)$ under far field unit tension $(\sigma_y^\infty = 1, \sigma_x^\infty = 0, \text{ and } \tau_{xy}^\infty = 0)$ and $\omega = 120^\circ$. The eigenvalue required for the solution corresponds to $\theta = 60^\circ$ from Table 1, and the number of degrees of freedom (DOF) included in the analysis was 48. This number was chosen in order to compare this point allocation scheme to that of previous work [47]. This scheme achieves adequate convergence with 25 points. For 48 DOF, no less than 24 points can be placed along each crack segment, since the use of fewer points generates an under-determined matrix with more columns than rows. (Both normal and tangential tractions are calculated, resulting in a doubling factor.) To reach a compromise between time efficiency and fully capturing behavior at crack segment ends, 50 points will be used along crack segments for all subsequent examples.

### 5.2. Effect of number of degrees of freedom on convergence

Table 3 lists results for a V-shaped crack (Fig. 8) with unit crack segment lengths under far field unit tension and shear $(\sigma_y^\infty = 1, \sigma_x^\infty = 0, \text{ and } \tau_{xy}^\infty = 1)$ and $\omega = 60^\circ$. The two eigenvalues required for the solution correspond to wedge angle $\theta = 120^\circ$ from Table 1. Fig. 9 shows normal traction plots along crack segment 1 as representative examples of the tractions calculated along each crack segment. The value of the prescribed traction for this case is $-0.6160254$. Reasonable results were obtained with only 9 DOF when only the basic crack behaviors (tip and wedge singularities and jump opening at the kink) are included with no fine-tuning. As more DOFs (up to series order $n = 5$ or 53 DOF) are added to allow greater flexibility in shaping the crack opening displacement profiles, convergence occurs rapidly with extremely low errors, as noted in the dramatic change of scale for the normal tractions axis. Based on these results, all subsequent analyses will use series of order $n = 5$ per crack segment, in both normal and tangential modes.

<table>
<caption>Table 3
Convergence results for $60^\circ$ V-shaped crack with unit crack segment lengths loaded in unit tension and shear</caption>
<thead>
<tr>
<th rowspan="2">DOF</th>
<th colspan="2">$K_{\text{I}}$</th>
<th colspan="2">$K_{\text{II}}$</th>
<th rowspan="2">$K_{\text{I,kink}}$</th>
<th rowspan="2">$K_{\text{II,kink}}$</th>
<th colspan="2">RRMS error</th>
</tr>
<tr>
<th>Segment 1</th>
<th>Segment 2</th>
<th>Segment 1</th>
<th>Segment 2</th>
<th>Normal</th>
<th>Shear</th>
</tr>
</thead>
<tbody>
<tr>
<td>9</td>
<td>$-1.1652$</td>
<td>1.7196</td>
<td>0.9087</td>
<td>$-0.6459$</td>
<td>$-0.0146$</td>
<td>$-2.2846$</td>
<td>0.0317</td>
<td>0.0472</td>
</tr>
<tr>
<td>21</td>
<td>$-1.1549$</td>
<td>1.8208</td>
<td>0.9033</td>
<td>$-0.7567$</td>
<td>$-0.0561$</td>
<td>$-2.4146$</td>
<td>$1.98 \times 10^{-3}$</td>
<td>$1.41 \times 10^{-3}$</td>
</tr>
<tr>
<td>37</td>
<td>$-1.1554$</td>
<td>1.8206</td>
<td>0.9037</td>
<td>$-0.7554$</td>
<td>$-0.0565$</td>
<td>$-2.4062$</td>
<td>$5.26 \times 10^{-5}$</td>
<td>$2.50 \times 10^{-5}$</td>
</tr>
<tr>
<td>53</td>
<td>$-1.1554$</td>
<td>1.8206</td>
<td>0.9037</td>
<td>$-0.7554$</td>
<td>$-0.0564$</td>
<td>$-2.4051$</td>
<td>$1.16 \times 10^{-6}$</td>
<td>$2.25 \times 10^{-6}$</td>
</tr>
</tbody>
</table>

![](./images/812117233420468225_11.jpg)

Fig. 9. Plots of normal tractions for varying numbers of degrees of freedom along crack segment 1 for a $60^{\circ}$ V-shaped crack with unit crack segment lengths loaded in unit tension and shear.

### 5.3. Effects of wedge eigenvalue approximation

While most methods in the literature fix the singular exponent at kinks as $\rho=1 / 2$, this method closely approximates the exact singular eigenvalues calculated from a wedge analysis. To more fully understand the effects of approximation on solution accuracy and convergence, two examples are studied. The first example is the $\omega=120^{\circ}$, V-shaped crack in an infinite plate loaded in far field unit tension from the point allocation study. This problem is symmetric with only one singular eigenvalue, $\rho_{1}$; therefore, the effects of independently varying eigenvalue approximations, $\alpha / \beta$, can be isolated. The commonly used value of $1 / 2$

is compared to the values 8/13 (which closely approximates the exact value, 0.61573, with a relative error of 0.06%) and 274/445 (with a relative error of only $5.5 \times 10^{-5}\%$).

As shown in Table 4 and Fig. 10, substantial error results from using $\rho = 1/2$ in place of a more accurate approximation. Large deviations occur in the tractions, particularly at the kink, and the generalized Mode I stress intensity factor computed at the kink is inaccurate. However, crack tip stress intensity factors appear unaffected. At the other extreme, the traction plots for 8/13 and 274/445 are nearly identical, and the results with 8/13 exhibit sufficient convergence. Therefore, the additional accuracy is not worth the substantially increased computation time. (Since a sum is performed over the denominator integer value of the approximation when integrating the corresponding dislocation distribution term, the large values associated with more accurate approximations dramatically increase computation time.)

The second eigenvalue study was performed using the previously described $\omega = 60^\circ$, V-shaped crack loaded in unit tension and shear from the DOF convergence study. Since this angle has two singular eigenvalues, as seen in Table 1, $(\rho_1 = 0.5122, \rho_2 = 0.7309)$, the effects of inaccurately approximating, as well as ignoring, the second eigenvalue can be evaluated. Results from three cases are studied: Case 1 (as presented in the DOF study, Table 3) correctly accounts for both singular eigenvalues; Case 2 approximates both eigenvalues as $\rho_1 = \rho_2 = 1/2$; and Case 3 correctly includes the first singular eigenvalue but ignores the second.

As shown in Table 5, relatively small errors occur in the Modes I and II stress intensity factors at the crack tips when the analysis is performed with incorrect eigenvalues. However, the effects on the Modes I and II generalized stress intensity factors at the kink are more noticeable. For Case 2, since the correct value of $\rho_1$ is close to the value of 1/2, little deviation occurred in the Mode I generalized stress intensity factor. However, the Mode II generalized stress intensity factor is inaccurate, and the traction plots show large error at the kink (Fig. 11). When only $\rho_1$ was included in the analysis (Case 3), even the $K_\text{I}$ value at the kink was affected. In addition, no Mode II generalized stress intensity factor can be computed, and the tractions at the kink deviate to an even greater extent. It is therefore concluded that all singular eigenvalues are required in an analysis and must be close approximations of their true values. Moreover, these results further substantiate the need to analytically evaluate the Cauchy singular integrals to obtain accurate stress fields at wedges, since it is clear that results are sensitive to large approximations such as those that can occur from numerical integration.

### 5.4. Interacting V-shaped cracks

Before attempting the case of two interacting V-shaped cracks (Fig. 12), two collinear straight cracks were analyzed for varying separation distances. The results [37] agreed with Erdogan's exact solution [20]. Having verified accuracy for two straight cracks, two interacting V-shaped cracks with angles $\theta = 60^\circ$ were analyzed under unit tension loading. The crack segment lengths of $a_1 = a_4 = 2$ and $a_2 = a_3 = 1$ were held constant while the value of $d$ (the distance between the cracks) was varied.

<table>
<caption>Table 4<br>Convergence results for varying eigenvalue of $\omega = 120^\circ$ V-shaped crack with unit crack segment lengths loaded in unit tension</caption>
<thead>
<tr>
<th>$\rho$</th>
<th>$K_\text{I}$</th>
<th>$K_\text{II}$</th>
<th>$K_\text{I,kink}$</th>
<th colspan="2">RRMS error</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th>Normal</th>
<th>Shear</th>
</tr>
</thead>
<tbody>
<tr>
<td>1/2</td>
<td>1.2550</td>
<td>0.8452</td>
<td>$-0.2505$</td>
<td>$1.03 \times 10^{-4}$</td>
<td>$2.19 \times 10^{-3}$</td>
</tr>
<tr>
<td>8/13</td>
<td>1.2548</td>
<td>0.8456</td>
<td>$-0.4492$</td>
<td>$9.08 \times 10^{-6}$</td>
<td>$5.77 \times 10^{-5}$</td>
</tr>
<tr>
<td>274/445</td>
<td>1.2548</td>
<td>0.8456</td>
<td>$-0.4498$</td>
<td>$1.06 \times 10^{-5}$</td>
<td>$8.71 \times 10^{-6}$</td>
</tr>
</tbody>
</table>

![](./images/812117233420468225_12.jpg)

Fig. 10. Effects of varying eigenvalue on normal tractions of crack segment 1 for a $120^{\circ}$ V-shaped crack with unit crack segment lengths loaded in unit tension.

Niu and Wu [36] studied interacting kinked and branched cracks by modeling deviations from main cracks as dislocation distributions. The interpolations of their graphically presented results are listed in Table 6 and may suffer inaccuracy in the second decimal place; however, the results from the present method match within this tolerance. As will be demonstrated in the coalescence example, convergence can be achieved for much smaller distances between the cracks than those presented in this example. Moreover, this method is not limited to collinear main cracks nor to equal deviations of the two cracks or segment lengths.

<table>
<caption>Table 5
Convergence results for varying eigenvalue of $\omega=60^\circ$ V-shaped crack with unit crack segment lengths loaded in unit tension and shear</caption>
<thead>
<tr>
<th rowspan="2">Case</th>
<th colspan="2">$K_{\text{I}}$</th>
<th colspan="2">$K_{\text{II}}$</th>
<th rowspan="2">$K_{\text{I,kink}}$</th>
<th rowspan="2">$K_{\text{II,kink}}$</th>
<th colspan="2">RRMS Error</th>
</tr>
<tr>
<th>Segment 1</th>
<th>Segment 2</th>
<th>Segment 1</th>
<th>Segment 2</th>
<th>Normal</th>
<th>Shear</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>−1.1554</td>
<td>1.8206</td>
<td>0.9037</td>
<td>−0.7554</td>
<td>−0.0564</td>
<td>−2.4051</td>
<td>$1.16\times10^{-6}$</td>
<td>$2.25\times10^{-6}$</td>
</tr>
<tr>
<td>2</td>
<td>−1.1495</td>
<td>1.8147</td>
<td>0.9134</td>
<td>−0.7457</td>
<td>−0.0556</td>
<td>−3.4794</td>
<td>0.0147</td>
<td>0.0264</td>
</tr>
<tr>
<td>3</td>
<td>−1.1519</td>
<td>1.8171</td>
<td>0.9591</td>
<td>−0.6999</td>
<td>−0.0565</td>
<td>N/A</td>
<td>0.0344</td>
<td>0.0392</td>
</tr>
</tbody>
</table>

![](./images/812117233420468225_13.jpg)

Fig. 11. Effects of varying eigenvalue on normal tractions of crack segment 1 for a $60^\circ$ V-shaped crack with unit crack segment lengths loaded in unit tension and shear.

![](./images/812117233420468225_14.jpg)

Fig. 12. Two interacting V-shaped cracks.

Table 6
Results comparison of stress intensity factors at crack tip 2 for varying separation distance of two interacting V-shaped cracks (Fig. 12)
under unit tension ($a_1=a_4=2$, $a_2=a_3=1$ and $\theta=60^\circ$)

<table>
<thead>
<tr>
<th>$d/a_2$</th>
<th colspan="2">$K_\text{I}$</th>
<th colspan="2">$K_\text{II}$</th>
</tr>
<tr>
<th></th>
<th>[36]</th>
<th>Present work</th>
<th>[36]</th>
<th>Present work</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.05</td>
<td>2.48</td>
<td>2.49</td>
<td>1.19</td>
<td>1.19</td>
</tr>
<tr>
<td>1.10</td>
<td>2.30</td>
<td>2.34</td>
<td>1.14</td>
<td>1.16</td>
</tr>
<tr>
<td>1.25</td>
<td>2.13</td>
<td>2.10</td>
<td>1.10</td>
<td>1.11</td>
</tr>
<tr>
<td>1.50</td>
<td>1.86</td>
<td>1.93</td>
<td>1.06</td>
<td>1.07</td>
</tr>
</tbody>
</table>

## 6. Multiply kinked and branched cracks

Using the same general principles successfully applied to V-shaped cracks, the method is now applied to cracks with more than one kink and branched cracks.

### 6.1. Examples for multiply kinked cracks

To demonstrate the accuracy of the method for multiply kinked cracks, an antisymmetric crack with two kinks (Fig. 13) was analyzed, and the results compared with accepted results from Kitagawa and Yuuki [46] and Vitek [33]. As with previous comparisons, stress intensity factors at crack tips form the basis of the comparisons, although crack face tractions matched those prescribed and wedge singularities demonstrated convergence. The loading was unit tension ($\phi=90^\circ$), and the central crack segment length was $a_2=2$. Table 7 presents results for two values of $a_1=a_3$ while $\theta$ is varied. Next, the same configuration was analyzed under pure shear loading, ($\phi=0^\circ$). For comparison, the central crack segment is again $a_2=2$, but the kink angle is now held constant at $\theta=60^\circ$. Results showing agreement are given in Table 8.

### 6.2. Examples for branched cracks

Though not presented here, results were obtained for a single branched crack and compared to those from other researchers [16,46,48], including experimental results [49]. Again, only stress intensity factors at crack tips were available. As with previous examples, tractions matched those prescribed, and when applicable, generalized wedge stress intensity factors exhibited rapid convergence. Details appear in TerMaath [37], where agreement is seen between the results of the above researchers and the present method.

Next, the problem of two interacting branched cracks was studied. Comparisons were made with the results of Niu and Wu [36] under unit tension loading (Fig. 14). The first example was a symmetric case where all lengths and branch angles were held fixed ($a_1=a_4=2$, $a_2=a_3=a_5=a_6=1$, and $\beta_1=\beta_2=30^\circ$) while the separation distance, $d$, was varied. Stress intensity factor results shown in Table 9 for the interacting crack tips are in agreement. The second example was non-symmetric. Lengths were equal to the previous values with the exception that now $a_5=a_6=0.1$. One branch angle was fixed at

![](./images/812117233420468225_15.jpg)

Fig. 13. Multiply kinked crack in an infinite plate (two kinks).

Table 7
Comparison of crack tip stress intensity factors for a crack with two kinks (Fig. 13) under unit tension

<table>
<thead>
<tr>
<th>$a_{1}/a_{2}$</th>
<th>$\theta$</th>
<th colspan="3">$K_{\mathrm{I}}$</th>
<th colspan="3">$K_{\mathrm{II}}$</th>
</tr>
<tr>
<th></th>
<th></th>
<th>[33]</th>
<th>[46]</th>
<th>Present work</th>
<th>[33]</th>
<th>[46]</th>
<th>Present work</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.1</td>
<td>$30^{\circ}$</td>
<td>1.570</td>
<td>1.605</td>
<td>1.604</td>
<td>0.705</td>
<td>0.714</td>
<td>0.716</td>
</tr>
<tr>
<td></td>
<td>$45^{\circ}$</td>
<td>1.208</td>
<td>1.237</td>
<td>1.237</td>
<td>0.909</td>
<td>0.926</td>
<td>0.926</td>
</tr>
<tr>
<td></td>
<td>$60^{\circ}$</td>
<td>N/A</td>
<td>0.800</td>
<td>0.810</td>
<td>0.972</td>
<td>0.995</td>
<td>0.995</td>
</tr>
<tr>
<td>0.2</td>
<td>$30^{\circ}$</td>
<td>1.686</td>
<td>1.720</td>
<td>1.695</td>
<td>0.829</td>
<td>0.839</td>
<td>0.827</td>
</tr>
<tr>
<td></td>
<td>$45^{\circ}$</td>
<td>1.283</td>
<td>1.311</td>
<td>1.260</td>
<td>1.085</td>
<td>1.102</td>
<td>1.061</td>
</tr>
<tr>
<td></td>
<td>$60^{\circ}$</td>
<td>0.806</td>
<td>0.763</td>
<td>0.762</td>
<td>1.099</td>
<td>1.124</td>
<td>1.126</td>
</tr>
</tbody>
</table>

Table 8
Comparison of crack tip stress intensity factors for a crack with two kinks (Fig. 13) under unit shear

<table>
<thead>
<tr>
<th>$a_{3}$</th>
<th colspan="2">$K_{\mathrm{I}}$</th>
<th colspan="2">$K_{\mathrm{II}}$</th>
</tr>
<tr>
<th></th>
<th>[46]</th>
<th>Present work</th>
<th>[46]</th>
<th>Present work</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.10</td>
<td>0.3972</td>
<td>0.3991</td>
<td>−0.2465</td>
<td>−0.2464</td>
</tr>
<tr>
<td>0.20</td>
<td>0.5681</td>
<td>0.5687</td>
<td>−0.3497</td>
<td>−0.3498</td>
</tr>
<tr>
<td>0.60</td>
<td>1.0111</td>
<td>1.0120</td>
<td>−0.6123</td>
<td>−0.6127</td>
</tr>
<tr>
<td>1.0</td>
<td>1.3212</td>
<td>1.3223</td>
<td>−0.7954</td>
<td>−0.7959</td>
</tr>
</tbody>
</table>

$\beta_{1}=30^{\circ}$, and the separation distance was constant at $d=0.3$. The other angle, $\beta_{2}$, was varied. The stress intensity results at the interacting crack tips are again in agreement (Table 10).

![](./images/812117233420468225_16.jpg)

Fig. 14. Two interacting branched cracks in an infinite plate.

<table>
<caption>Table 9 Stress intensity factor comparison for two symmetric interacting branched cracks</caption>
<thead>
<tr>
<th rowspan="2">$d$</th>
<th colspan="2">$K_{\text{I}}$</th>
<th colspan="2">$K_{\text{II}}$</th>
</tr>
<tr>
<th>[36]</th>
<th>Present work</th>
<th>[36]</th>
<th>Present work</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.05</td>
<td>2.04</td>
<td>2.00</td>
<td>0.94</td>
<td>0.94</td>
</tr>
<tr>
<td>1.10</td>
<td>1.95</td>
<td>1.93</td>
<td>0.89</td>
<td>0.89</td>
</tr>
<tr>
<td>1.25</td>
<td>1.84</td>
<td>1.81</td>
<td>0.78</td>
<td>0.78</td>
</tr>
<tr>
<td>1.50</td>
<td>1.68</td>
<td>1.68</td>
<td>0.69</td>
<td>0.70</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 10 Stress intensity factor comparison for two interacting branched cracks</caption>
<thead>
<tr>
<th rowspan="2">$\beta_{2}$</th>
<th colspan="2">$K_{\text{I}}^{2}$</th>
<th colspan="2">$K_{\text{II}}^{2}$</th>
<th colspan="2">$K_{\text{I}}^{6}$</th>
<th colspan="2">$K_{\text{II}}^{6}$</th>
</tr>
<tr>
<th>[36]</th>
<th>Present work</th>
<th>[36]</th>
<th>Present work</th>
<th>[36]</th>
<th>Present work</th>
<th>[36]</th>
<th>Present work</th>
</tr>
</thead>
<tbody>
<tr>
<td>$30^{\circ}$</td>
<td>0.53</td>
<td>0.53</td>
<td>1.12</td>
<td>1.12</td>
<td>1.65</td>
<td>1.66</td>
<td>$-0.34$</td>
<td>$-0.31$</td>
</tr>
<tr>
<td>$60^{\circ}$</td>
<td>0.62</td>
<td>0.61</td>
<td>1.15</td>
<td>1.15</td>
<td>1.10</td>
<td>1.10</td>
<td>$-0.96$</td>
<td>$-0.95$</td>
</tr>
</tbody>
</table>

## 7. Crack propagation and coalescence

To demonstrate the ability of the method to treat local behavior of interacting cracks, an example problem is presented that propagates and joins two initially straight cracks (Fig. 15) in an infinite plate. The loading is unit tension applied perpendicular to the cracks. To solve for the stress intensity factors, the two straight cracks are divided into two crack segments each of unit length and solved in the same manner

![](./images/812117233420468225_17.jpg)

Fig. 15. Localized coalescence of two interacting cracks.

as V-shaped cracks. For this particular problem, the cracks are forced to propagate along the shortest path between the cracks, and possible growth at the extremes is not considered, so that the local joining growth is isolated. As the cracks begin to grow towards each other, they become V-shaped cracks. Convergence is achieved for very small ligaments (as short as 0.0774) between the two V-shaped cracks. (The main cracks are now modeled as entire crack segments, while the deviations are also modeled as individual crack segments.) Note, that for crack tip 1 (and tip 3 by symmetry arguments), $K_{\text{II}}$ grows faster than $K_{\text{I}}$, so in reality, the crack paths may curve as the two cracks tips attempt to avoid each other.

When the two V-shaped cracks coalesce, they form a multiply kinked crack. The shear stress intensity factor, $K_{\text{II}}$, at the ends of the main cracks, represented by crack tip 2, is negligible, and therefore not tabulated. As this example demonstrates, the method is capable of providing converged values of stress intensity factors and opening displacement shapes for propagating cracks with very small ligaments of material between them. With this information, growth of larger crack arrays can be studied.

### 8. Future work

A straightforward extension of this research is to study cracks in a finite plate. This problem would be modeled as a polygon-shaped plate created by crack segments embedded in an infinite plate. For example, a rectangular plate would be modeled as four connected crack segments with four wedges of $90^\circ$. In addition, interpenetration of crack surfaces is not currently prevented and should be eliminated, and friction laws governing crack face sliding could be implemented through traction criteria. Also, small-scale yielding at crack tips could be readily incorporated providing a more realistic model of crack behavior for materials exhibiting limited ductile behavior. Moreover, this method is conducive to programming in a parallel environment, and if transferred to a supercomputer, large arrays of cracks could be processed in a feasible amount of time, allowing for Monte Carlo simulation of fracture processes. For varying probabilistic characteristics (for example, crack orientations, growth properties, or material defects), statistical properties could be determined by investigating randomly assigned crack patterns.

This method could be applied to curved cracks by modeling the crack as a series of straight crack segments and using the solution method for a multiply kinked crack. For propagating cracks where there is a substantial mode II component, crack growth will not be linear. This case could be handled by modeling the curved crack growth as a new crack segment attached to the initial crack with a newly formed kink.

By assuming a brittle matrix material, this method could be applied to cases of cracking in composite materials. The problem of crack-bridging by fibers could be studied by modeling the effects of the fibers as point forces acting on the crack faces. T- and H-shaped cracks, that induce debond between the fiber and the matrix, could be investigated once this method is modified for bimaterial interfaces.

### 9. Conclusions

Superposition methods based on a dislocation distribution approach require the determination of crack opening displacement profiles that satisfy the traction-free condition on crack faces. Even for single cracks of complex shape, this solution approach is mathematically cumbersome creating a barrier to the development and application of methods to analyze large arrays of interacting cracks. To overcome this difficulty, the method presented in this paper creates these displacement profiles from sets of series, each representing a physically realistic behavior of the cracks. Such an approach proves accurate and efficient. Solutions exhibited rapid convergence (with respect to prescribed tractions and stress intensity factors) using few degrees of freedom, and stability of the weighting coefficients was achieved regardless of loading conditions or crack configuration. This research shows promising applicability to a wide variety of important problems of practical interest and begins to fill the need for a means to efficiently evaluate general configurations of interacting cracks under arbitrary loading conditions.

### Acknowledgement

S.L.P. and C.Y.H. acknowledge support under the Institute for Future Space Transport (IFST), a NASA University Institute that is monitored through NASA Glenn Research Center. The authors would also like to thank Dr. Brun Hilbert for his time in reviewing this paper.

### Appendix A. Point allocation scheme

For exterior crack segments, the effects of an opening point force pair on the stress intensity factors at kinks and tips are assumed to be proportional to $1/x_j^{\rho_1}$ and $1/(1 - x_j)^{1/2}$ respectively. ($x_j$ is the distance mea-

sured from the kink or branch point when the crack segment length is normalized by $a$ to unit length.) These relationships are multiplied by constants and integrated from the origin of the crack segment to the point $x_j$. Enforcing continuity across the crack segment leads to the solution for the constants. The final point allocation equations are

$$
\begin{aligned}
x_j & = \left( \frac{(3-2\rho_1)}{2(1/2)^{\rho_1}} \frac{j}{n} \right)^{\frac{1}{1-\rho_1}}, & 0 < x_j \leqslant \frac{1}{2} \\
x_j & = 1 - \left( \sqrt{1/2} - \frac{(3-2\rho_1)(j/n)-1}{2\sqrt{2}(1-\rho_1)} \right)^2, & \frac{1}{2} \leqslant x_j < 1
\end{aligned} \tag{A.1}
$$

For interior crack segments, both ends are bounded by kinks so the effects of a point force pair on wedge stress intensities at both ends must be included and are assumed proportional to $1/x_j^{\rho_{1,1}}$ and $1/(1-x_j)^{\rho_{1,2}}$. The second subscripts on the eigenvalues designate the origin, 1, or the end of the crack segment, 2. Fol- lowing the previous derivation, final equations for point allocation along interior crack segments are

$$
\begin{aligned}
x_j & = \left( \frac{2-\rho_{1,1}-\rho_{1,2}}{(1/2)^{\rho_{1,1}-1}(1-\rho_{1,2})} \frac{j}{n} \right)^{\frac{1}{1-\rho_{1,1}}}, & 0 \leqslant x_j \leqslant \frac{1}{2} \\
x_j & = 1 - \frac{1}{2} \left( 1 - \frac{(2-\rho_{1,1}-\rho_{1,2})\frac{j}{n}+(\rho_{1,2}-1)}{(1-\rho_{1,1})} \right)^{\frac{1}{1-\rho_{1,2}}}, & \frac{1}{2} \leqslant x_j \leqslant 1
\end{aligned} \tag{A.2}
$$

## Appendix B. Integration of dislocation distributions

Dislocation distributions, $\mu$, derived from the terms of the various series (Eqs. (9)-(11)), are analytically integrated according to Eqs. (3). All terms have the form $(t/a)^{\lambda}$, where the exponent $\lambda \geqslant 0$ is a real number. One of five different solutions applies for $Z_1$ and $Z_2$ depending on the particular value of $\lambda$.

### B.1. Solution 1: $\lambda = \rho$ where $0 < \rho < 1$

For this case, opening displacement terms of the form $(t/a)^{\rho}$ are evaluated. These terms are first con- verted to dislocation distribution terms by taking the derivative as

$$
\mu(t) = \frac{\mathrm{d}}{\mathrm{d}t} \left[ \left( \frac{t}{a} \right)^{\rho} (H(t)-H(t-a)) \right] = \frac{\rho}{a} \left( \frac{t}{a} \right)^{\rho-1} (H(t)-H(t-a)) - \delta(t-a) \tag{B.1}
$$

where $H(t)$ is the Heaviside unit step function, and $\delta(t)$ is the Dirac delta function. Use of these functions allows crack opening displacements to be turned on and off at the beginning and end of each crack segment. Eqs. (3) can be solved exactly if $\rho$ is a rational number, if not, $\rho$ can be approximated to any desired degree of accuracy by choosing integers $\alpha$ and $\beta$ such that $\rho \approx \alpha/\beta$. In terms of this approximation, the final forms of the integral solutions are

$$
\begin{aligned}
Z_1 & = -\frac{\rho}{a} \left( \frac{z}{a} \right)^{\alpha/\beta-1} \sum_{k=0}^{\beta-1} \mathrm{e}^{2\pi\mathrm{i}k\alpha/\beta} \ln \left( \frac{(z/a)^{1/\beta} \mathrm{e}^{2\pi\mathrm{i}k/\beta}-1}{(z/a)^{1/\beta} \mathrm{e}^{2\pi\mathrm{i}k/\beta}} \right) - \frac{1}{z-a} \\
Z_2 & = \frac{\rho}{z(z-a)} - \frac{(1-\rho)}{z} \frac{\rho}{a} \left( \frac{z}{a} \right)^{\alpha/\beta-1} \sum_{k=0}^{\beta-1} \mathrm{e}^{2\pi\mathrm{i}k\alpha/\beta} \ln \left( \frac{(z/a)^{1/\beta} \mathrm{e}^{2\pi\mathrm{i}k/\beta}-1}{(z/a)^{1/\beta} \mathrm{e}^{2\pi\mathrm{i}k/\beta}} \right) - \frac{1}{(z-a)^2}
\end{aligned} \tag{B.2}
$$

### B.2. Solution 2: $\lambda = \rho + j$ where $\rho + j > 1$ and $\rho + j$ is not an integer

In this case, $\rho$ is again approximated as a rational number $\alpha/\beta$. A recursive procedure using the identity $(t/a)^{(\rho+j)-1} = -((z - t)/a)(t/a)^{(\rho+j)-2} + (z/a)(t/a)^{(\rho+j)-2}$ is applied successively until the results from Eqs. (B.2) are applicable.

### B.3. Solution 3: $\lambda = \rho = 0$

For this exponent, the corresponding dislocation distribution term is

$$
\mu(t) = \delta(t) - \delta(t - a) \tag{B.3}
$$

Using Eqs. (3), it is trivial to evaluate $Z_1$, and $Z_2$ as

$$
\begin{aligned}
Z_1 &= \frac{1}{z} - \frac{1}{z - a} \\
Z_2 &= \frac{1}{z^2} - \frac{1}{(z - a)^2}
\end{aligned} \tag{B.4}
$$

### B.4. Solution 4: $\lambda = \rho = 1$

The dislocation distribution term for this exponent is

$$
\mu(t) = \left(\frac{1}{a}\right)(H(t) - H(t - a)) - \delta(t - a) \tag{B.5}
$$

The integration is again trivial and results in the solution

$$
\begin{aligned}
Z_1 &= \frac{1}{a}(\ln(-z) - \ln(a - z)) - \frac{1}{z - a} = \frac{1}{a}\left(\ln\left(\frac{z}{a - z}\right)\right) - \frac{1}{z - a} \\
Z_2 &= \frac{1}{z(z - a)} - \frac{1}{(z - a)^2}
\end{aligned} \tag{B.6}
$$

### B.5. Solution 5: $\lambda = N$ where $N > 1$ is an integer

For the final case, the dislocation distribution is

$$
\mu(t) = \frac{N}{a}\left(\frac{t}{a}\right)^{N-1}(H(t) - H(t - a)) - \delta(t - a) \tag{B.7}
$$

yielding the following integral solutions

$$
\begin{aligned}
Z_1 &= -\frac{N}{a}\left(\sum_{j=1}^{N-1} \frac{1}{j}\left(\frac{z}{a}\right)^{N-j-1} + \left(\frac{z}{a}\right)^{N-1}\left(\ln\left(\frac{z - a}{z}\right)\right)\right) - \frac{1}{z - a} \\
Z_2 &= \frac{N}{a^2}\left(\sum_{j=1}^{N-1} \frac{N - j - 1}{j}\left(\frac{z}{a}\right)^{N-j-2} + m\left(\frac{z}{a}\right)^{N-2}\left(\ln\left(\frac{z - a}{z}\right)\right) - \left(\frac{z}{a}\right)^{N-1}\left(\frac{a^2}{z(a - z)}\right)\right) - \frac{1}{(z - a)^2}
\end{aligned} \tag{B.8}
$$

## Appendix C. Coefficient constraints

To develop the constraints on coefficients at kinks, the notation, $c_{\rho j, k}^{[1]}$ and $c_{\rho j, k}^{[2]}$ is used to represent the tangential and normal opening displacement coefficients, respectively, where $k=1,2$ refers to the two adjoining crack segments (Fig. 8). These constraints eliminate mathematically possible but physically inadmissible singularities in the crack face tractions and enforce continuity where two or more crack segments join.

### C.1. Constraints for the jump openings induced by $(t l a)^{0}$ polynomial terms for V-shapes

To ensure the continuity in crack opening at a kink, coefficient constraints are

$$
\left[\begin{array}{l}
c_{00,2}^{[1]} \\
c_{00,2}^{[2]}
\end{array}\right]=-\left[\begin{array}{cc}
\cos \omega & \sin \omega \\
-\sin \omega & \cos \omega
\end{array}\right]\left[\begin{array}{l}
c_{00,1}^{[1]} \\
c_{00,1}^{[2]}
\end{array}\right] \tag{C.1}
$$

### C.2. Constraints for the slope discontinuity associated with $(t l a)^{1}$ polynomial terms for V-shapes

The linear opening terms allow one wedge to rotate relative to another as well as providing for possible Poisson effects in connection with the superimposed trivial problem. The constraints for these terms are

$$
\begin{aligned}
& c_{01,2}^{[1]}=-\left(\frac{a_{2}}{a_{1}}\right) c_{01,1}^{[1]}, \quad c_{01,2}^{[2]}=-\left(\frac{a_{2}}{a_{1}}\right) c_{01,1}^{[2]}, \quad \omega=\pi \\
& c_{01,2}^{[1]}=\left(\frac{a_{2}}{a_{1}}\right) c_{01,1}^{[1]}, \quad c_{01,2}^{[2]}=-\left(\frac{a_{2}}{a_{1}}\right) c_{01,1}^{[2]}, \quad \omega=\frac{\pi}{2} \\
& c_{01,2}^{[1]}=c_{01,1}^{[1]}=0, \quad c_{01,2}^{[2]}=-\left(\frac{a_{2}}{a_{1}}\right) c_{01,1}^{[2]}, \quad \omega \neq \frac{\pi}{2}, \pi
\end{aligned} \tag{C.2}
$$

### C.3. Constraints for traction singularities associated with $(t l a)^{\rho}$ polynomial terms for V-shapes

For the terms based on the wedge eigenvalue, $\rho_{1}$, the coefficients must satisfy

$$
c_{\rho_{1} 0,2}^{[2]}=\left(\frac{a_{2}}{a_{1}}\right)^{\rho_{1}} c_{\rho_{1} 0,1}^{[2]}, \quad c_{\rho_{1} 0,2}^{[1]}=-\left(\frac{a_{2}}{a_{1}}\right)^{\rho_{1}} c_{\rho_{1} 0,1}^{[1]}=\left(\frac{1+B}{A}\right)\left(\frac{a_{2}}{a_{1}}\right)^{\rho_{1}} c_{\rho_{1} 0,1}^{[2]} \tag{C.3}
$$

For the terms based on the wedge eigenvalue, $\rho_{2}$, the coefficients must follow

$$
c_{\rho_{2} 0,2}^{[2]}=-\left(\frac{a_{2}}{a_{1}}\right)^{\rho_{2}} c_{\rho_{2} 0,1}^{[2]}, \quad c_{\rho_{2} 0,2}^{[1]}=\left(\frac{a_{2}}{a_{1}}\right)^{\rho_{2}} c_{\rho_{2} 0,1}^{[1]}=\left(\frac{1-B}{A}\right)\left(\frac{a_{2}}{a_{1}}\right)^{\rho_{2}} c_{\rho_{2} 0,1}^{[2]} \tag{C.4}
$$

where

$$
\begin{aligned}
A & =-\frac{(1+\rho) \sin \omega \cos (\rho(\omega-\pi))}{\cos (\pi \rho)} \\
B & =\frac{\cos \omega \cos (\rho(\omega-\pi))+\rho \sin \omega \sin (\rho(\omega-\pi))}{\cos (\pi \rho)}
\end{aligned} \tag{C.5}
$$

### C.4. Constraints for branched cracks

If a branch junction includes a wedge angle greater than $180^{\circ}$, constraints will be applied to the two crack segments adjacent to the wedge on the corresponding $(t / a)^{\rho}$ terms using the equations developed

![](./images/812117233420468225_18.jpg)

Fig. 16. Branched crack configuration for constraint equations.

for V-shaped cracks. However, constraint equations for the two singular polynomial terms must be mod- ified to include additional crack segments; therefore, the subscript $i$ now denotes crack segment 1,2 or 3 (Fig. 16). Constraint equations for branches consisting of more than three crack segments follow the same form. For the $(t / a)^{0}$ terms, the jumps must all be compatible in assembling the three wedges leading to

$$
\begin{aligned}
& c_{00,1}^{[1]}=-\cos \omega_{1} c_{00,2}^{[1]}+\sin \omega_{1} c_{00,2}^{[2]}-\cos \omega_{2} c_{00,3}^{[1]}+\sin \omega_{2} c_{00,3}^{[2]} \\
& c_{00,1}^{[2]}=-\sin \omega_{1} c_{00,2}^{[1]}-\cos \omega_{1} c_{00,2}^{[2]}-\sin \omega_{2} c_{00,3}^{[1]}-\cos \omega_{2} c_{00,3}^{[2]}
\end{aligned} \tag{C.6}
$$

If the branch has no right angle wedges or angles equal to $\pi$ (collinear segments), the constraint equations on the $(t / a)^{1}$ terms are

$$
\begin{aligned}
& c_{01,1}^{[1]}=c_{01,2}^{[1]}=c_{01,3}^{[1]}=0 \\
& \frac{c_{01,1}^{[2]}}{a_{1}}=-\frac{c_{01,2}^{[2]}}{a_{2}}-\frac{c_{01,3}^{[2]}}{a_{3}}
\end{aligned} \tag{C.7}
$$

Physically, these constraints specify that the angles must be preserved and that tangential stretching or com- pression cannot occur. Tangential behavior (associated with Poisson effects) is only allowed at right angles $(\pi / 2)$ or angles equal to $\pi$, as will be seen by non-zero tangential coefficients. Constraints for configurations containing such angles are summarized in Table 11.

<table>
<caption>Table 11<br>Constraints on $t^{1}$ for branched crack configurations</caption>
<tr>
<td>Two right angles</td>
<td>One right angle</td>
<td>One right angle</td>
<td>Branch off a main crack</td>
</tr>
<tr>
<td>![](./images/812117233420468225_19.jpg)</td>
<td>![](./images/812117233420468225_20.jpg)</td>
<td>![](./images/812117233420468225_21.jpg)</td>
<td>![](./images/812117233420468225_22.jpg)</td>
</tr>
<tr>
<td>$\displaystyle\frac{c_{01,1}^{[1]}}{a_{1}}=\frac{c_{01,2}^{[1]}}{a_{2}}-\frac{c_{01,3}^{[1]}}{a_{3}}$</td>
<td>$\displaystyle\frac{c_{01,1}^{[1]}}{a_{1}}=\frac{c_{01,2}^{[1]}}{a_{2}}$</td>
<td>$\displaystyle\frac{c_{01,1}^{[1]}}{a_{1}}=\frac{c_{01,3}^{[1]}}{a_{3}}$</td>
<td>$\displaystyle\frac{c_{01,1}^{[1]}}{a_{1}}=-\frac{c_{01,3}^{[1]}}{a_{3}}$</td>
</tr>
<tr>
<td>$\displaystyle\frac{c_{01,1}^{[2]}}{a_{1}}=-\frac{c_{01,2}^{[2]}}{a_{2}}-\frac{c_{01,3}^{[2]}}{a_{3}}$</td>
<td>$c_{01,3}^{[1]}=0$</td>
<td>$c_{01,2}^{[1]}=0$</td>
<td>$c_{01,2}^{[1]}=0$</td>
</tr>
<tr>
<td></td>
<td>$\displaystyle\frac{c_{01,1}^{[2]}}{a_{1}}=-\frac{c_{01,2}^{[2]}}{a_{2}}-\frac{c_{01,3}^{[2]}}{a_{3}}$</td>
<td>$\displaystyle\frac{c_{01,1}^{[2]}}{a_{1}}=-\frac{c_{01,2}^{[2]}}{a_{2}}-\frac{c_{01,3}^{[2]}}{a_{3}}$</td>
<td>$\displaystyle\frac{c_{01,1}^{[2]}}{a_{1}}=-\frac{c_{01,2}^{[2]}}{a_{2}}-\frac{c_{01,3}^{[2]}}{a_{3}}$</td>
</tr>
</table>

### Appendix D. Generalized stress intensity factors derivation

Based on Williams [23], generalized stress intensity factors at wedges greater than $180^\circ$ are formulated using polar coordinates (Fig. 3). For simplicity this derivation neglects rigid body motion. Final expressions are functions of the eigenvalues and corresponding weighting coefficients. From Williams, the stress equations (for a given $\rho$) are expressed as

$$
\sigma_{\theta \theta}(r, \theta)=\rho(\rho+1) r^{\rho-1} F(\theta) \quad \tau_{r \theta}(r, \theta)=-\rho r^{\rho-1} F^{\prime}(\theta)
\tag{D.1}
$$

where the prime denotes differentiation with respect to $\theta$. From Eqs. (D.1), it is clear that values $0<\rho<1$ will cause singular stress behavior as $r \rightarrow 0$. The displacement equations are

$$
\begin{aligned}
&2 G u_{r}=r^{\rho}\left(-(\rho+1) F(\theta)+\frac{1}{1+v} N^{\prime}(\theta)\right) \\
&2 G u_{\theta}=r^{\rho}\left(-F^{\prime}(\theta)+\frac{1}{1+v}(\rho-1) N(\theta)\right)
\end{aligned}
\tag{D.2}
$$

### D.1. Symmetric $\sigma_{\theta \theta}$ case (Mode I)

The biharmonic and harmonic functions of the stress and displacement equations are

$$
\begin{aligned}
&F(\theta)=b_{2} \cos \left(\left(\rho_{1}+1\right) \theta\right)+b_{4} \cos \left(\left(\rho_{1}-1\right) \theta\right) \\
&N(\theta)=\frac{4}{\rho_{1}-1} b_{4} \sin \left(\left(\rho_{1}-1\right) \theta\right)
\end{aligned}
\tag{D.3}
$$

where

$$
b_{2}=\Gamma b_{4}, \quad \Gamma=-\frac{\cos \left(\left(\rho_{1}-1\right) \alpha\right)}{\cos \left(\left(\rho_{1}+1\right) \alpha\right)}
\tag{D.4}
$$

and $\alpha=(2 \pi-\omega) / 2$. The normal stress along the wedge bisector, $\theta=0$ is

$$
\left.\sigma_{\theta \theta}\right|_{\theta=0}=\rho_{1}\left(\rho_{1}+1\right) r^{\rho_{1}-1}(1+\Gamma) b_{4}
\tag{D.5}
$$

To obtain the relationship between $b_{4}$ and the coefficient corresponding to the singular wedge term, set $t=r$ in the opening displacement profile. The equation for the normal displacement along the wedge boundary $\theta=\alpha$ can then be written as

$$
\left.u_{\theta}\right|_{\theta=\alpha}=-c_{\rho_{1} 0}^{[2]}(r / a)^{\rho_{1}}
\tag{D.6}
$$

An important subtlety is that setting the displacement along a wedge boundary equal to this term causes this boundary to absorb all of the displacement. From the wedge theory formulation (and generalizing to plane stress or plane strain), the displacement equation is

$$
\left.2 G u_{\theta}\right|_{\theta=\alpha}=r^{\rho_{1}}(1+\kappa) b_{4} \sin \left(\left(\rho_{1}-1\right) \alpha\right)
\tag{D.7}
$$

Equating Eqs. (D.6) and (D.7), yields

$$
b_{4}=-\frac{c_{\rho_{1} 0}^{[2]}}{a^{\rho_{1}}}\left(\frac{2 G}{1+\kappa}\right) \frac{1}{\sin \left(\left(\rho_{1}-1\right) \alpha\right)}
\tag{D.8}
$$

Finally, the stress intensity factor for symmetric behavior is

$$
K_{\mathrm{I}}=\lim _{r \rightarrow 0}\left.\sigma_{\theta \theta}\right|_{\theta=0}(2 \pi r)^{1-\rho_{1}}
\tag{D.9}
$$

and by substitution of the above relations, the final form is

$$
K_{\mathrm{I}}=(2 \pi)^{1-\rho_{1}} \rho_{1}\left(\rho_{1}+1\right)(1+\Gamma)\left(-\frac{c_{\rho_{1} 0}^{[2]}}{a^{\rho_{1}}}\left(\frac{2 G}{1+\kappa}\right) \frac{1}{\sin \left(\left(\rho_{1}-1\right) \alpha\right)}\right) \tag{D.10}
$$

### D.2. Anti-symmetric $\sigma_{r\theta}$ case (Mode II)

In a similar manner, the generalized stress intensity factor for anti-symmetric, Mode II, behavior is obtained. The biharmonic and harmonic functions are

$$
\begin{aligned}
&F(\theta)=b_{1} \sin \left(\left(\rho_{2}+1\right) \theta\right)+b_{3} \sin \left(\left(\rho_{2}-1\right) \theta\right) \\
&N(\theta)=\frac{-4}{\rho_{2}-1} b_{3} \cos \left(\left(\rho_{2}-1\right) \theta\right)
\end{aligned} \tag{D.11}
$$

where

$$
b_{1}=\Omega b_{3}, \quad \Omega=-\frac{\sin \left(\left(\rho_{2}-1\right) \alpha\right)}{\sin \left(\left(\rho_{2}+1\right) \alpha\right)} \tag{D.12}
$$

so that the shear stress along $\theta=0$ is

$$
\left.\tau_{r \theta}\right|_{\theta=0}=-\rho_{2} r^{\rho_{2}-1}\left(\Omega\left(\rho_{2}+1\right)+\left(\rho_{2}-1\right)\right) b_{3} \tag{D.13}
$$

To obtain the relationship between $b_{3}$ and the coefficient for the singular wedge term for tangential deformation, begin with the tangential displacement along $\theta=\alpha$ and $t=r$, which is

$$
\left.u_{r}\right|_{\theta=\alpha}=-c_{\rho_{2} 0}^{[1]}(r / a)^{\rho_{2}} \tag{D.14}
$$

From the wedge theory formulation and generalizing to plane stress or plane strain,

$$
\left.2 G u_{r}\right|_{\theta=\alpha}=r^{\rho_{2}}(1+\kappa) b_{3} \sin \left(\left(\rho_{2}-1\right) \alpha\right) \tag{D.15}
$$

From these two equations,

$$
b_{3}=-\frac{c_{\rho_{2} 0}^{[1]}}{a^{\rho_{2}}}\left(\frac{2 G}{1+\kappa}\right) \frac{1}{\sin \left(\left(\rho_{2}-1\right) \alpha\right)} \tag{D.16}
$$

Finally the stress intensity factor for anti-symmetric behavior is

$$
K_{\mathrm{II}}=\lim _{r \rightarrow 0}\left.\tau_{r \theta}\right|_{\theta=0}(2 \pi r)^{1-\rho_{2}} \tag{D.17}
$$

and the final form is obtained by substitution as

$$
K_{\mathrm{II}}=(2 \pi)^{1-\rho_{2}} \rho_{2}\left(\left(\rho_{2}+1\right) \Omega+\left(\rho_{2}-1\right)\right)\left(\frac{c_{\rho_{2} 0}^{[1]}}{a^{\rho_{2}}}\left(\frac{2 G}{1+\kappa}\right) \frac{1}{\sin \left(\left(\rho_{2}-1\right) \alpha\right)}\right) \tag{D.18}
$$

## References

[1] Burton Jr JK, Phoenix SL. Superposition method for calculating singular stress fields at kinks, branches and tips in multiple crack arrays. Int J Fract 2000;102:99-139.

[2] Bilby B, Eshelby J. Dislocations and the theory of fracture. In: Liebowitz H, editor. Fracture, an advanced treatise, vol. I. New York: Academic Press; 1968. p. 99-182.

[3] Lam K, Phua S. Multiple crack interaction and its effect on stress intensity factor. Engng Fract Mech 1991;40(3):585-92.

[4] Melin S. Why do cracks avoid each other? Int J Fract 1983;23:37-45.

[5] Gol'dstein R, Salganik R. Brittle fracture of solids with arbitrary cracks. Int J Fract 1974;10:507-23.

[6] Han X, Wang T. Interacting multiple cracks with complicated crack surface conditions. Int J Fract 1996;82:R53-7.

[7] Li S, Mear M. Singularity-reduced integral equations for displacement discontinuities in three-dimensional linear elastic media. Int J Fract 1998;93:87-114.

[8] Hu K, Chandra A. Interactions among cracks and rigid lines near a free surface. Int J Solids Struct 1993;30(14):1919-37.

[9] Hu K, Chandra A. Interactions among general systems of cracks and anticracks: an integral equation approach. J Appl Mech 1993;60:920-8.

[10] Benveniste Y, Dvorak G, Zarzour J, Wung E. On interacting cracks and complex crack configurations in linear elastic media. Int J Solids Struct 1989;25(11):1279-93.

[11] Kachanov M, Montagut E. A simple analysis of interacting cracks and cracks intersecting a hole. Int J Fract 1989;40(3):R61-5.

[12] Erdogan F, Gupta G, Cook T. Numerical solution of singular integral equations. In: Sih G, editor. Methods of analysis and solutions of crack problems. Leyden: Noordhoff; 1973. p. 368-425.

[13] Theocaris P, Ioakimidis N. Numerical integration methods for the solution of singular integral equations. Q Appl Math 1977;35:173-83.

[14] Gerasoulis A. The use of quadratic polynomials for the solution of singular integrals of Cauchy type. Comput Math Appl 1982;8:15-22.

[15] Melin S. On singular integral equations for kinked cracks. Int J Fract 1986;30:57-65.

[16] Chen Y, Hasebe N. New integration scheme for the branch crack problem. Engng Fract Mech 1995;52(5):791-801.

[17] Hills D, Kelly P, Dai D, Korsunsky A. Solution of crack problems: the distributed dislocation technique. Dordrecht: Kluwer Academic Publishers; 1996.

[18] Westergaard H. Bearing pressures and cracks. J Appl Mech 1939;6:49-53.

[19] Koiter W. An infinite row of collinear cracks in an infinite elastic sheet. Ing Arch 1959;28:168-72.

[20] Erdogan F. On the stress distribution in plates with collinear cuts under arbitrary loads. In: Proceedings, fourth US national congress of applied mechanics, 1962. p. 547-53.

[21] Sih G. Stress distribution near internal crack tips for longitudinal shear problems. J Appl Mech 1965;32:51-8.

[22] Murakami Y, editorStress intensity factors handbook. 1st ed. New York: Pergamon; 1987.

[23] Williams M. Stress singularities resulting from various boundary conditions in angular corners of plates in extension. J Appl Mech 1952;19:526-8.

[24] Williams M. On the stress distribution at the base of a stationary crack. J Appl Mech 1957;24:109-14.

[25] Timoshenko S, Goodier J. Theory of elasticity. 3rd ed. New York: McGraw-Hill; 1970.

[26] Barber J. Elasticity. Boston: Kluwer Academic Publishers; 1992.

[27] Cotterell B, Rice J. Slightly curved or kinked cracks. Int J Fract 1980;16(2):155-69.

[28] Karihaloo B, Keer L, Nemat-Nasser S. Crack kinking under nonsymmetric loading. Engng Fract Mech 1980;13:879-88.

[29] Karihaloo B, Keer L, Nemat-Nasser S, Oranratnachai A. Approximate description of crack kinking and curving. J Appl Mech 1981;48:515-9.

[30] Bilby B, Cardew G. The crack with a kinked tip. Int J Fract 1975;11:708-12.

[31] Chatterjee S. The stress field in the neighborhood of a branched crack in an infinite sheet. Int J Solids Struct 1975;11:521-38.

[32] Lo K. Analysis of branched cracks. J Appl Mech 1978;45:797-802.

[33] Vitek V. Plane strain stress intensity factors for branched cracks. Int J Fract 1977;13(4):481-501.

[34] Hayashi K, Nemat-Nasser S. Energy release rate and crack kinking under combined loading. J Appl Mech 1981;48:520-4.

[35] Blanco C, Martinez-Esnaola J, Atkinson C. Kinked cracks in anisotropic elastic materials. Int J Fract 1998;93:387-407.

[36] Niu J, Wu M. Strong interactions of morphologically complex cracks. Engng Fract Mech 1997;57:665-87.

[37] TerMaath S. A two-dimensional analytical technique for studying fracture in brittle materials containing interacting kinked and branched cracks. Dissertation, Cornell University, 2000.

[38] Lardner R. Mathematical theory of dislocations and fracture. Great Britain: University of Toronto Press; 1974.

[39] Hirth J, Lothe J. Theory of dislocations. New York: John Wiley & Sons; 1982.

[40] Bueckner H. A novel principle for the computation of stress intensity factors. Z Angew Math Mech 1970;50:529-46.

[41] Hui C-Y, Ruina A. Why K? High order singularities and small scale yielding. Int J Fract 1995;72:97-120.

[42] Irwin G. Analysis of stresses and strains near the end of a crack transversing in a plate. J Appl Mech 1957;24:361-4.

[43] Abe H, Hayashi K, Yamamoto T. Growth path of a crack in earth's crust. Trans Jpn Soc Mech Engrs 1985;51-465:1359-66.

[44] Isida M. Analysis of stress intensity factors of plate with arbitrary array cracks and bent cracks. Trans Jpn Soc Mech Engrs 1978;44-380:1122-33.

[45] Isida M, Nishino T. Formulae of stress intensity factors of bent cracks in plane problems. Trans Jpn Soc Mech Engrs 1982;48-430:729-38.

[46] Kitagawa H, Yuuki R. Stress intensity factors for branched cracks in a two-dimensional stress state. Trans Jpn Soc Mech Engrs 1975;41-346:1641-9.

[47] TerMaath S, Phoenix SL. Investigation of a new analytical method for treating kinked cracks in a plate. In: Fatigue and fracture mechanics. ASTM STP 1389, vol. 31. 2000. p. 331-47.

[48] Isida M, Noguchi H. Formulae of stress intensity factors of branched cracks in plane problems. Trans Jpn Soc Mech Engrs 1983;49-440:469-79.

[49] Theocaris P. Complex stress-intensity factors at bifurcated cracks. J Mech Phys Solids 1972;20:265-79.