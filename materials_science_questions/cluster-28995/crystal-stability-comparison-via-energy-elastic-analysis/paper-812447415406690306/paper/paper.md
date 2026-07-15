# THE ELECTRON-LATTICE INTERACTION ENERGY OF STRONGLY COMPRESSED MATTER

I.I. GOLDMAN and C. YANG
Yerevan Physics Institute, USSR

Received 11 July 1972

A crystal structure dependent term of the energy of strongly compressed matter is calculated. The correction is of the same order of magnitude as the terms calculated allready on an assumption of a uniformly distributed background of positive charge.

Calculations of the energy of various lattice types of strongly compressed matter lead to the conclusion that there is very small difference between the Coulomb energies of the most symmetrical lattices (b.c.c., f.c.c., and h.c.p.) and this necessitates the consideration of the next order approximation in an expansion into powers of a small parameter $\rho=r_{0} / a$, where $a=h^{2} / m e^{2}$, $r_{0}^{-3}$ is the atomic density. A lattice type independent part of terms of this order was calculated [1,2] on a model assumption of a uniformly distributed background of positive charge. In a more realistic model (the nuclei form a periodic structure) lattice type dependent terms of the same order may arise due to the electron-nuclei interaction (for example [3]).

In this paper we shall calculate these terms. The difficulties of such calculation consist in taking into account the intersection of Fermi surface with Brillouin zone boundaries (and the corresponding deformation of the Fermi surface). We have calculated this effect for periodic structures of one, two and three dimensions. It was found that essential correction of this kind may arise only in the one-dimension model. In three-dimension case the Fermi surface intersection leads to corrections only in the next terms of the expansion $(\sim \rho \ln \rho)$. Namely, it leads to the electron-lattice interaction energy acquiring a factor of the kind $1+c\left(U_{\mathrm{f}} / E_{\mathrm{f}}^{0}\right) \ln \left(E_{\mathrm{f}}^{0} / U_{\mathrm{f}}\right)$, where $U_{\mathrm{f}}$ is the matrix element of the electron-lattice interaction potential, $E_{\mathrm{f}}^{0}$ is the unperturbed single-electron energy, $c$ is a numerical factor.

The sums over the reciprocal lattice may be calculated by a method of reduction to integrals [4]. In a three-dimensional case the electron-lattice interaction energy (per one atom) in the second order of perturbation theory has the form

$$
E_{\mathrm{e}-l}=-\frac{Z e^{4} m}{\nu^{2} 6 \pi^{2} h^{2}} \sum_{b \neq 0} g f\left(\frac{\pi b}{p_{\mathrm{F}}}\right)
\tag{1}
$$

where

$$
f(x)=\frac{1}{x^{4}}\left(1+\frac{1-x^{2}}{2 x} \ln \left|\frac{x+1}{x-1}\right|\right)
\tag{2}
$$

$$
g=\left|\sum_{r^{\prime}} \exp \left(2 \pi \mathrm{i} b r^{\prime}\right)\right|^{2}.
\tag{3}
$$

Here $Z$ is the atomic number, $\nu$ is the number of atoms in one unit cell, $r^{\prime}$ is the position of atom within a unit cell, $b$ is the reciprocal lattice vector, $p_{\mathrm{F}}=\pi(3 Z \nu / \pi v)^{1 / 3}$, $v$ is the unit cell volume.

To calculate (1) one may consider it as an energy of pair interaction in reciprocal space with an "interaction potential" of a form $g f\left(\pi b / p_{\mathrm{F}}\right)$ and transform the function $f(x)$ into an integral

$$
f(x)=\int_{0}^{\infty} \psi(t) \exp \left(-x^{2} t\right) \mathrm{d} t.
\tag{4}
$$

The function $f(x)$ is analytic for $|x|>1$. So the integral transformation (4) (which is a modified version of Laplace transformation) exists only for $|x|>1$. Representing $f(x)$ as an expansion into powers of $x$ and taking integral transformation (4) for every term one gets

$$
\psi(t)=\frac{2}{3}\left[3 t-1+F\left(-\frac{3}{2}, \frac{1}{2} ; t\right)\right]
\tag{5}
$$

where $F(\alpha, \beta ; t)$ is the confluent hypergeometric function.

Thus the considered sum may be represented in form


<table>
<caption>Table 1 The values of $-E_{\mathrm{e}-l}$ for three most symmetric lattices of various $Z$ (in units of $Z^{2} e^{4} m / h^{2}$)</caption>
<thead>
  <tr>
    <th></th>
    <th>b.c.c.</th>
    <th>f.c.c.</th>
    <th>h.c.p.</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Hydrogen</td>
    <td>0.0903860</td>
    <td>0.0913073</td>
    <td>0.0661690</td>
  </tr>
  <tr>
    <td>Helium</td>
    <td>0.224488</td>
    <td>0.219672</td>
    <td>0.189904</td>
  </tr>
  <tr>
    <td>Carbon</td>
    <td>0.473481</td>
    <td>0.474871</td>
    <td>0.435366</td>
  </tr>
  <tr>
    <td>Iron</td>
    <td>1.034330</td>
    <td>1.036611</td>
    <td>0.989050</td>
  </tr>
</tbody>
</table>

$$
\begin{aligned}
\sum_{x \neq 0} g f(x)= & \sum_{x \neq 0} \sum_{1} g f(x)+\int_{0}^{\infty}\left(\sum g \exp \left(-x^{2} t\right)-\right. \\
& \left.\sum_{1} g \exp \left(-x^{2} t\right)\right) \psi(t) \mathrm{d} t
\end{aligned}
$$

where $x=\pi b / p_{\mathrm{F}}$, and $\sum_{1}$ means a summation over some region 1 containing the origin $x=0$ which is determined from the requirement of convergence of the integral (6) (for this purpose the region 1 must at least contain the region $|x| \leqslant 1$ as a whole).

The sum over reciprocal lattice may be represented by combinations of elliptic functions of Jacobi by analogy with ref. [4].

The calculation of electron-lattice interaction energy by formulae (6) and (1) for various lattice types shows that this energy is maximum when the lattice is sufficiently symmetric. The main contribution into the dependence of total energy of strongly compressed matter on its structure is known to be given by the Coulomb energy of the nuclei which is minimum for most symmetric lattices (b.c.c. and f.c.c.). Thus, the electron-lattice energy in general somewhat "smooths" out the mentioned dependence of total energy on the structure.

It can be seen from table 1 of the results of the calculations for b.c.c., f.c.c. and h.c.p. lattices that in most cases (except helium) the calculated energy for b.c.c. lattice is larger than that for f.c.c., and for the h.c.p. lattice the energy is larger in every case. The difference in the energy between b.c.c. and f.c.c. lattices is about $10^{-3} Z^{2}$ (in units of $e^{4} m / h^{2}$ ). Since the difference in Coulomb energy of nuclei between f.c.c. and b.c.c. lattices is of order of $10^{-4} Z^{2} / \rho$ [4]; so at $\rho \sim 10^{-1}$, these two differences in energies may compensate each other and the problem of the stable structure of compressed matter must be solved by considering the higher terms of the expansion over $\rho$.

### References
[1] M. Gell-Mann and K. Brueckner, Phys. Rev. 106 (1957) 364.
[2] K. Sawada, Phys. Rev. 106 (1957) 72.
[3] T. Schneider, Helv. Phys. Acta 42 (1969) 957; see also D. Pines and Ph. Nozieres, The theory of quantum liquids (1966).
[4] I.I. Goldman, Phys. Lett. 34A (1971) 339.