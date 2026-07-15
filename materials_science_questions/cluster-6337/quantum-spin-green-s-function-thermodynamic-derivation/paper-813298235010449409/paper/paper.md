# Correlations equalities and some upper bounds for the critical temperature for spin one systems

F.C. Sá Barreto $^{a,b}$, A.L. Mota $^{a,*}$

$^{a}$ Departamento de Ciências Naturais, Universidade Federal de São João del Rei, C.P. 110, CEP 36301-160, São João del Rei, Brazil
$^{b}$ (Emeritus Professor) Departamento de Física, Universidade Federal de Minas Gerais, 31270-901, Belo Horizonte, MG, Brazil

---

## ARTICLE INFO

**Article history:**
Received 5 April 2012
Received in revised form 31 May 2012
Available online 13 July 2012

**Keywords:**
Blume-Capel model
Correlation equalities
Critical temperature upper bounds

---

## ABSTRACT

Starting from correlation identities for the Blume-Capel spin 1 systems and using correlation inequalities, we obtain rigorous upper bounds for the critical temperature. The obtained results improve over effective field type results.

© 2012 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Correlation inequalities combined with exact identities are useful in obtaining rigorous results in statistical mechanics. Among the various questions that are resolved by them one is the decay of the correlation functions. The decay of the correlation functions give information about the critical couplings of statistical mechanics models. In this work, the method will be applied to study systems described by the spin one Blume-Capel model [1,2]. Firstly, we present the derivation of an exact relation for the two spin correlation function, valid in any dimension, which is an extension of Callen's identity for the spin 1/2 Ising model [3]. Starting from these identities we will then make use of the first and second Griffiths inequalities and Newman's inequalities to obtain the exponential decay of the two spin correlation functions. The coupling constant which are the upper bounds for the critical temperature are obtained for $d=2$ and $d=3$ dimensions. In this study the coupling parameters obtained improve effective field results. Upper bounds for the critical temperature $T_c$ for Ising and multi-component spin systems have been obtained by showing (for $T>T_c$) the exponential decay of the two-point function [4-6]. Spin correlation inequalities and their iteration are used by Brydges et al. [6], Lieb [7] and Simon [5].

The aim of the present work is to obtain rigorous upper bounds for the critical couplings of the spin one Blume-Capel model in two- and three-dimensional lattices. The method we will employ is based on an exact two-point correlation function identity and rigorous inequalities for the correlation functions. Thus, our results are rigorous upper bounds for the critical temperature of the model. The results improve mean field ones, and are comparable to others obtained by effective field theory, with the advantage of representing rigorous limits for the true critical temperature.

The procedure to improve the bound for the critical temperature over the effective field result for the classical $S=1$ model is as follows: starting from a two-point correlation function identity, a generalization of Callen's identity [3] for this model [8] and using Griffith's 1st and 2nd inequalities (Griffith I, II) (see Refs. [9-15]) and Newman's inequalities [11,16] we establish the inequality for the two-point function, $\langle S_0S_l\rangle$, as

$$
\langle S_0S_l\rangle \leq \sum_j a_j\langle S_jS_l\rangle, \quad 0 \leq a_j \leq 1 \tag{1}
$$

---

* Corresponding author. Tel.: +55 32 3379 2483; fax: +55 32 3379 2483.
E-mail addresses: fcsabarreto@gmail.com (F.C. Sá Barreto), motaal@ufsj.edu.br (A.L. Mota).

0378-4371/$ - see front matter © 2012 Elsevier B.V. All rights reserved.
doi:10.1016/j.physa.2012.07.026

which when iterated (see Ref. [5]) implies exponential decay for $T > T_c$. In Section 2 we present the derivation of the correlation identities for the Blume-Capel model [8]. In Section 3, we apply these identities to the $d=2$ and $d=3$ lattices. Next, in Section 4, we apply the correlation inequalities to obtain the upper bounds for $T_c$. Numerical results can be found in Section 5, and in Section 6 we present our concluding remarks.

We write the Hamiltonian for the classical spin one system, known as the Blume-Capel model, as

$$
H=-J \sum_{i, j} S_{i} S_{j}-D \sum_{i} S_{i}^{2},
\tag{2}
$$

where $J>0$, $D$ is the single ion anisotropy and the first sum is over the nearest neighbors spins on the lattice. We define the thermal average $\langle\cdots\rangle$ by

$$
\langle\cdots\rangle=Z^{-1} \sum_{\left\{S_{i}\right\}}(\ldots) \mathrm{e}^{-\beta H}, \quad Z=\sum_{\left\{S_{i}\right\}} \mathrm{e}^{-\beta H}
\tag{3}
$$

where each $S_{i}$ is restricted by $S_{i}=-1,0,+1$.

## 2. Correlation identity for the spin one model

We reproduce the generalization of Callen's identity for the spin 1 Blume-Capel model which has been obtained previously by Siqueira and Fittipaldi [8], derived in a manner analogous to the ones for the spin 1/2 Ising model [17], the transverse Ising model [18] and $Z_2$ gauge model [19]. Let

$$
\left\langle F(S) S_{i}\right\rangle=\frac{\operatorname{Tr}\left(F(S) S_{i} \mathrm{e}^{-\beta H}\right)}{\operatorname{Tr}\left(\mathrm{e}^{-\beta H}\right)},
\tag{4}
$$

where $F(S)$ is any function of $S$ different from $S_i$. We can write $H=H_i+H'$, where

$$
H_{i}=-\left(\sum_{|j|=1} J_{i j} S_{j}\right) S_{i}-D S_{i}^{2},
\tag{5}
$$

is the Hamiltonian describing site $i$ and its neighbors, and $H'$ corresponds to the Hamiltonian of the rest of the lattice. Consequently $\left[H_i, H'\right]=0$. From Eqs. (2) and (3), we get,

$$
\left\langle F(S) S_{i}\right\rangle=\frac{\operatorname{Tr} F(S) \mathrm{e}^{-\beta\left(H_{i}+H^{\prime}\right)} S_{i}}{\operatorname{Tr} \mathrm{e}^{-\beta\left(H_{i}+H^{\prime}\right)}}=\frac{\operatorname{Tr}^{\prime} \operatorname{Tr}_{i} F(S) \mathrm{e}^{-\beta H_{i}} S_{i} \mathrm{e}^{-\beta H^{\prime}}}{\operatorname{Tr}^{\prime} \operatorname{Tr}_{i} \mathrm{e}^{-\beta H_{i}} \mathrm{e}^{-\beta H^{\prime}}}
\tag{6}
$$

or

$$
\left\langle F(S) S_{i}\right\rangle=\frac{\operatorname{Tr}^{\prime} \operatorname{Tr}_{i} F(S) \mathrm{e}^{-\beta H_{i}} \mathrm{e}^{-\beta H^{\prime}} \frac{\operatorname{Tr}_{i} \mathrm{e}^{-\beta H_{i}} S_{i}}{\operatorname{Tr}_{i} \mathrm{e}^{-\beta H_{i}}}}{\operatorname{Tr}^{\prime} \operatorname{Tr}_{i} \mathrm{e}^{-\beta H_{i}} \mathrm{e}^{-\beta H^{\prime}}}
\tag{7}
$$

where $\operatorname{Tr}' \operatorname{Tr}_i=\operatorname{Tr}$. Finally, we obtain,

$$
\left\langle F(S) S_{i}\right\rangle=\left\langle F(S) \frac{\operatorname{Tr}_{i} \mathrm{e}^{-\beta H_{i}} S_{i}}{\operatorname{Tr}_{i} \mathrm{e}^{-\beta H_{i}}}\right\rangle.
\tag{8}
$$

Explicitly operating the trace $\operatorname{Tr}_i$, we get,

$$
\begin{aligned}
\left\langle F(S) S_{i}\right\rangle & =\left\langle F(S) \frac{2 \mathrm{e}^{\beta D} \sinh \left(\sum_{j} \beta J_{i j} S_{j}\right)}{2 \mathrm{e}^{\beta D} \cosh \left(\sum_{j} \beta J_{i j} S_{j}\right)+1}\right\rangle \\
& =\left\langle\left. F(S) \prod_{|j|=1} \mathrm{e}^{\beta J_{i j} S_{j} \nabla}\right|_{x=0}, f(x)\right|_{x=0},
\end{aligned}
\tag{9}
$$

with $\nabla \equiv \frac{\partial}{\partial x}$, such that $\mathrm{e}^{\alpha \nabla} f(x)=f(x+\alpha)$, and

$$
f(x)=\frac{2 \mathrm{e}^{\beta D} \sinh (x)}{2 \mathrm{e}^{\beta D} \cosh (x)+1}.
\tag{10}
$$

As $S_{j}^{2 n}=S_{j}^{2}$ and $S_{j}^{2 n+1}=S_{j}$ for $n=0,1,2,3, \ldots$, we obtain,

$$
\mathrm{e}^{S_{j} A}=S_{j}^{2} \cosh (A)+S_{j} \sinh (A)+1-S_{j}^{2},
\tag{11}
$$

and, applying Eqs. (10) and (11) in Eq. (9), we get

$$
\left\langle F(S) S_{i}\right\rangle=\left\langle F(S) \prod_{j \neq i,|j|=1}\left(S_{j}^{2} \cosh \left(\beta J_{i j} \nabla\right)+S_{j} \sinh \left(\beta J_{i j} \nabla\right)+1-S_{j}^{2}\right)\right\rangle\left.f(x)\right|_{x=0}. \tag{12}
$$

Similarly for the correlation function involving the square of the spin function $S_{i}^{2}$, we obtain,

$$
\left\langle G(S) S_{i}^{2}\right\rangle=\left\langle G(S) \prod_{j \neq i,|j|=1} \mathrm{e}^{\beta J_{i j} S_{j} \nabla}\right\rangle\left.g(x)\right|_{x=0}, \tag{13}
$$

with,

$$
g(x)=\frac{2 \mathrm{e}^{\beta D} \cosh (x)}{2 \mathrm{e}^{\beta D} \cosh (x)+1}, \tag{14}
$$

resulting in,

$$
\left\langle G(S) S_{i}^{2}\right\rangle=\left\langle G(S) \prod_{j \neq i,|j|=1}\left(S_{j}^{2} \cosh \left(\beta J_{i j} \nabla\right)+S_{j} \sinh \left(\beta J_{i j} \nabla\right)+1-S_{j}^{2}\right)\right\rangle\left.g(x)\right|_{x=0}. \tag{15}
$$

The function $G(S)$ is any function of $S$, except $S_{i}^{2}$. Eqs. (12) and (15) are exact and generalize Callen's identity which was obtained for the $S=1 / 2$ Ising model [3].

### 3. Exact correlation identities applied to the $d=2$ and $d=3$ lattices

Let us apply the previous results for $\left\langle F(S) S_{i}\right\rangle$ and $\left\langle G(S) S_{i}^{2}\right\rangle$ given by Eqs. (12) and (15) for specific lattices in two- and three-dimensions. The two spin correlation functions, $\left\langle S_{0} S_{l}\right\rangle$, are obtained from Eqs. (12) and (15) by defining $F(S)=S_{l}$.

#### 3.1. For the $d=2$ and $z=3$, the honeycomb lattice

We obtain from Eq. (12)

$$
\left\langle S_{0} S_{l}\right\rangle=A_{1} \sum_{i}\left\langle S_{i} S_{l}\right\rangle+A_{2} \sum_{i<j}\left\langle S_{i} S_{j}^{2} S_{l}\right\rangle+A_{3} \sum_{i<j<k}\left\langle S_{i} S_{j} S_{k} S_{l}\right\rangle+A_{4} \sum_{i<j<k}\left\langle S_{i} S_{j}^{2} S_{k}^{2} S_{l}\right\rangle, \tag{16}
$$

where the A coefficients are given in Appendix A.1. We also obtain, from Eq. (15),

$$
\left\langle S_{0}^{2} S_{l}\right\rangle=B_{0}+B_{1} \sum_{i}\left\langle S_{i}^{2} S_{l}\right\rangle+B_{2} \sum_{i<j}\left\langle S_{i} S_{j} S_{l}\right\rangle+B_{3} \sum_{i<j}\left\langle S_{i}^{2} S_{j}^{2} S_{l}\right\rangle+B_{4} \sum_{i<j<k}\left\langle S_{i} S_{j} S_{k}^{2} S_{l}\right\rangle+B_{5} \sum_{i<j<k}\left\langle S_{i}^{2} S_{j}^{2} S_{k}^{2} S_{l}\right\rangle, \tag{17}
$$

where the B coefficients are given in Appendix A.1.

#### 3.2. For $d=2$ and $z=4$, the square lattice

We obtain from Eq. (12) for the two spin correlation functions $\left\langle S_{0} S_{l}\right\rangle$ the expression,

$$
\begin{aligned}
\left\langle S_{0} S_{l}\right\rangle= & A_{1} \sum_{i}\left\langle S_{i} S_{l}\right\rangle+A_{2} \sum_{i<j}\left\langle S_{i} S_{j}^{2} S_{l}\right\rangle+A_{3} \sum_{i<j<k}\left\langle S_{i} S_{j} S_{k} S_{l}\right\rangle \\
& +A_{4} \sum_{i<j<k}\left\langle S_{i} S_{j}^{2} S_{k}^{2} S_{l}\right\rangle+A_{5} \sum_{i<j<k<m}\left\langle S_{i} S_{j} S_{k} S_{m}^{2} S_{l}\right\rangle+A_{6} \sum_{i<j<k<m}\left\langle S_{i} S_{j}^{2} S_{k}^{2} S_{m}^{2} S_{l}\right\rangle,
\end{aligned} \tag{18}
$$

where the A coefficients are given in Appendix A.2. We also obtain, for the function $\left\langle S_{0}^{2} S_{l}\right\rangle$,

$$
\begin{aligned}
\left\langle S_{0}^{2} S_{l}\right\rangle= & B_{0}+B_{1} \sum_{i}\left\langle S_{i}^{2} S_{l}\right\rangle+B_{2} \sum_{i<j}\left\langle S_{i} S_{j} S_{l}\right\rangle+B_{3} \sum_{i<j}\left\langle S_{i}^{2} S_{j}^{2} S_{l}\right\rangle+B_{4} \sum_{i<j<k}\left\langle S_{i} S_{j} S_{k}^{2} S_{l}\right\rangle \\
& +B_{5} \sum_{i<j<k}\left\langle S_{i}^{2} S_{j}^{2} S_{k}^{2} S_{l}\right\rangle+B_{6} \sum_{i<j<k<m}\left\langle S_{i} S_{i} S_{k} S_{m}\right\rangle+B_{7} \sum_{i<j<k<m}\left\langle S_{i} S_{j} S_{k}^{2} S_{m}^{2}\right\rangle+B_{8} \sum_{i<j<k<m}\left\langle S_{i}^{2} S_{j}^{2} S_{k}^{2} S_{m}^{2} S_{l}\right\rangle,
\end{aligned} \tag{19}
$$

where the B coefficients are given in Appendix A.2.

### 3.3. For $d=3$ and $z=6$, the cubic lattice

We obtain from Eq. (12)

$$
\begin{aligned}
\left\langle S_{0} S_{l}\right\rangle &=A_{1} \sum_{i}\left\langle S_{i} S_{l}\right\rangle+A_{2} \sum_{i<j}\left\langle S_{i} S_{j}^{2} S_{l}\right\rangle+A_{3} \sum_{i<j<k}\left\langle S_{i} S_{j} S_{k} S_{l}\right\rangle+A_{4} \sum_{i<j<k}\left\langle S_{i} S_{j}^{2} S_{k}^{2} S_{l}\right\rangle+A_{5} \sum_{i<j<k<m}\left\langle S_{i} S_{j} S_{k} S_{m}^{2} S_{l}\right\rangle \\
&+A_{6} \sum_{i<j<k<m}\left\langle S_{i} S_{j}^{2} S_{k}^{2} S_{m}^{2} S_{l}\right\rangle+A_{7} \sum_{i<j<k<m<n}\left\langle S_{i} S_{j} S_{k} S_{m} S_{n} S_{l}\right\rangle \\
&+A_{8} \sum_{i<j<k<m<n}\left\langle S_{i} S_{j} S_{k} S_{m}^{2} S_{n}^{2} S_{l}\right\rangle+A_{9} \sum_{i<j<k<m<n<p}\left\langle S_{i} S_{j} S_{k} S_{m} S_{n} S_{p}^{2} S_{l}\right\rangle \\
&+A_{10} \sum_{i<j<k<m<n}\left\langle S_{i} S_{j}^{2} S_{k}^{2} S_{m}^{2} S_{n}^{2} S_{l}\right\rangle+A_{11} \sum_{i<j<k<m<n<p}\left\langle S_{i} S_{j} S_{k} S_{m}^{2} S_{n}^{2} S_{p}^{2} S_{l}\right\rangle,
\end{aligned}
\tag{20}
$$

where the A coefficients are given in Appendix A.3. We also obtain, for the function $\langle S_{0}^{2} S_{l}\rangle$,

$$
\begin{aligned}
\left\langle S_{0}^{2} S_{l}\right\rangle &=B_{0}+B_{1} \sum_{i}\left\langle S_{i}^{2} S_{l}\right\rangle+B_{2} \sum_{i<j}\left\langle S_{i} S_{j} S_{l}\right\rangle+B_{3} \sum_{i<j}\left\langle S_{i}^{2} S_{j}^{2} S_{l}\right\rangle \\
&+B_{4} \sum_{i<j<k}\left\langle S_{i} S_{j} S_{k}^{2} S_{l}\right\rangle+B_{5} \sum_{i<j<k}\left\langle S_{i}^{2} S_{j}^{2} S_{k}^{2} S_{l}\right\rangle+B_{6} \sum_{i<j<k<m}\left\langle S_{i} S_{i} S_{k} S_{m}\right\rangle+B_{7} \sum_{i<j<k<m}\left\langle S_{i} S_{j} S_{k}^{2} S_{m}^{2}\right\rangle \\
&+B_{8} \sum_{i<j<k<m}\left\langle S_{i}^{2} S_{j}^{2} S_{k}^{2} S_{m}^{2} S_{l}\right\rangle+B_{9} \sum_{i<j<k<m<n<p}\left\langle S_{i} S_{j} S_{k} S_{m} S_{n} S_{p} S_{l}\right\rangle \\
&+B_{10} \sum_{i<j<k<m<n}\left\langle S_{i}^{2} S_{j}^{2} S_{k}^{2} S_{m}^{2} S_{n}^{2} S_{l}\right\rangle+B_{11} \sum_{i<j<k<m<n<p}\left\langle S_{i}^{2} S_{j}^{2} S_{k}^{2} S_{m}^{2} S_{n}^{2} S_{p}^{2} S_{l}\right\rangle \\
&+B_{12} \sum_{i<j<k<m<n}\left\langle S_{i}^{2} S_{j}^{2} S_{k}^{2} S_{m} S_{n} S_{l}\right\rangle+B_{13} \sum_{i<j<k<m<n<p}\left\langle S_{i}^{2} S_{j}^{2} S_{k}^{2} S_{m}^{2} S_{n} S_{p} S_{l}\right\rangle \\
&+B_{14} \sum_{i<j<k<m<n}\left\langle S_{i}^{2} S_{j} S_{k} S_{m} S_{n} S_{l}\right\rangle+B_{15} \sum_{i<j<k<m<n<p}\left\langle S_{i}^{2} S_{j}^{2} S_{k} S_{m} S_{n} S_{p} S_{l}\right\rangle,
\end{aligned}
\tag{21}
$$

where the B coefficients are given in Appendix A.3.

The sums over $i, j, k, m, n$ and $p$ are over the nearest neighbors of 0 to which we have given a numerical ordering. The proof of results (16) for the case Section 3.1, the honeycomb lattice, is presented in Appendix B, as an example for the other cases.

### 4. Application of the correlation inequalities

In the following results we will make use of the following inequalities: $\langle S_{A}\rangle \geq 0$ (Griffiths I), $\langle S_{A} S_{B}\rangle-\langle S_{A}\rangle\langle S_{B}\rangle \geq 0$ (Griffiths II) (see Refs. [9,11,12,15]), $\langle S_{i} F\rangle \leq \sum_{j}\langle S_{i} S_{j}\rangle\langle\mathrm{d} F / \mathrm{d} S_{j}\rangle$ (Newman's) [11,16] and $\langle S_{i}^{2} S_{A}\rangle \leq\langle S_{A}\rangle$ [13,14], where $\langle S_{A}\rangle=\prod_{i} S_{i}$, $\langle S_{B}\rangle=\prod_{i} S_{i}$ and $F$ is a polynomial function of variables $S$.

From the equations for the two spin correlation functions obtained in Sections 3.1-3.3 and applying the Griffithith's and Newman's inequalities we obtain an inequality of the form

$$
\left\langle S_{0} S_{l}\right\rangle \leq \sum_{|i|=1} a_{i}\left\langle S_{i} S_{l}\right\rangle,
\tag{22}
$$

where $a_{i}$ is a sum of products of two-point functions.

### 4.1. Case $d=2$, $z=3$, honeycomb lattice

Using

$$
\left\langle S_{j}^{2} S_{i} S_{l}\right\rangle \leq\left\langle S_{i} S_{l}\right\rangle
\tag{23}
$$

in Eq. (19), in the $A_{2}$ term and Griffiths II, i.e.,

$$
\left\langle S_{i} S_{j} S_{k} S_{l}\right\rangle \geq\left\langle S_{i} S_{j}\right\rangle\left\langle S_{k} S_{l}\right\rangle
\tag{24}
$$

in the $A_3$ term, and noticing that $A_2$ and $A_3$ are negative, we get for $d=2$, $z=3$,

$$
\langle S_{0}S_{l}\rangle\leq\left(A_{1}-\left|A_{2}\right|-\left|A_{3}\right|\langle S_{0}S_{1}\rangle_{1D}+A_{4}\right)\sum_{|i=1|}\langle S_{i}S_{l}\rangle. \tag{25}
$$

### 4.2. Case $d=2$, $z=4$, square lattice

Using inequality (23) in Eq. (20), in the $A_2$ term ($A_2<0$) term, Griffiths II in the $A_3$ term ($A_3<0$), the inequalities

$$
\langle S_{j}^{2}S_{k}^{2}S_{i}S_{l}\rangle\leq\langle S_{i}S_{l}\rangle \tag{26}
$$

in the $A_4$ term ($A_4>0$) and

$$
\langle S_{j}^{2}S_{k}^{2}S_{m}^{2}S_{i}S_{l}\rangle\leq\langle S_{i}S_{l}\rangle \tag{27}
$$

in the $A_6$ term ($A_6>0$) and in the $A_5$ term using Griffiths II, we get for $d=2$, $z=4$,

$$
\langle S_{0}S_{l}\rangle\leq\left(A_{1}-\left|A_{2}\right|-\langle S_{1}S_{2}\rangle_{1D}|A_{3}|+A_{4}+\langle S_{1}S_{2}\rangle_{1D}A_{5}+A_{6}\right)\sum_{|i=1|}\langle S_{i}S_{l}\rangle. \tag{28}
$$

### 4.3. Case $d=3$, $z=6$, cubic lattice

As before, we use in Eq. (20), inequality (23) in the $A_2$ term ($A_2<0$) term, Griffiths II in the $A_3$ term ($A_3<0$), the inequalities (26) in the $A_4$ term ($A_4>0$), inequality (24) in the $A_6$ term ($A_6>0$), and Griffiths II in the $A_5$ term. For the term $A_7(>0)$ we use Newman's inequality and for the terms $A_8(>0)$, $A_9(>0)$, $A_{10}(>0)$ and $A_{11}(>0)$, we use inequality (22). Then, we get for $d=3$, $z=6$,

$$
\langle S_{0}S_{l}\rangle\leq\left(A_{1}-\left|A_{2}\right|-\langle S_{1}S_{2}\rangle_{1D}|A_{3}|+A_{4}+\langle S_{1}S_{2}\rangle_{1D}A_{5}+A_{6}+A_{7}+A_{8}+A_{9}+A_{10}+A_{11}\right)\sum_{|i=1|}\langle S_{i}S_{l}\rangle. \tag{29}
$$

The two-spin correlation function $\langle S_{1}S_{2}\rangle_{1D}$ is the one-dimension model two spin correlation separated by a distance of two lattice sites. By bounding the resulting two-point function occurring in the previous results from below with the two-point function of the one-dimensional infinite chain (see Appendix B), we get:

$$
\langle S_{0}S_{l}\rangle\leq\sum_{|i=1|}a_{i}\langle S_{i}S_{l}\rangle, \tag{30}
$$

where, for $d=2$, $z=3$, honeycomb lattice,

$$
a_{j}=A_{1}-\left|A_{2}\right|-\left|A_{3}\right|\langle S_{0}S_{1}\rangle_{1D}+A_{4}; \tag{31}
$$

for $d=2$, $z=4$, square lattice,

$$
a_{j}=A_{1}-\left|A_{2}\right|-\langle S_{1}S_{2}\rangle_{1D}|A_{3}|+A_{4}+\langle S_{1}S_{2}\rangle_{1D}A_{5}+A_{6}; \tag{32}
$$

and for $d=3$, $z=6$, cubic lattice,

$$
a_{j}=A_{1}-\left|A_{2}\right|-\langle S_{1}S_{2}\rangle_{1D}|A_{3}|+A_{4}+\langle S_{1}S_{2}\rangle_{1D}A_{5}+A_{6}+A_{7}+A_{8}+A_{9}+A_{10}+A_{11}. \tag{33}
$$

The one-dimensional correlation function is given by (see Appendix C):

$$
\langle S_{1}S_{2}\rangle_{1D}=\frac{1+\sqrt{1-2f(2\beta J)}}{f(2\beta J)} \tag{34}
$$

and $f(2\beta J)$ is given by (10).

## 5. Numerical results

Evaluating numerically the value of $T$ such that $\sum a_{j}\leq1$, $a_{j}>0$, we obtain, by sufficient condition, upper bounds for $T_c$, which are shown in Tables 1 and 2, for $D=0$ and $D=\infty$, in comparison with results obtained by other methods. Although we have obtained the upper bounds for $T_c$ for $D=0$ and $D=\infty$, we can as well obtain the bounds for the critical temperature of the model as a function of the anisotropy $D$. The spin one model has been extensively studied by many authors applying different techniques, such as, molecular field approximation (MFA) [1,2], effective field approximation(EFT) [8,20], series expansion methods [21,22], renormalization group(RG) [23-27], Monte-Carlo methods(MC) [28-31], the Wang-Landau technique [32-34] and cluster variation methods(CVM) [35]. We will restrict our comparisons to some values of the critical temperatures obtained by these works mentioned above.

For the evaluation of the self-correlation terms ($\langle S_{i}^{2}\rangle$) that emerge from the application of the Griffith's and Newman's inequalities, we use, for the $D=0$ case, $\langle S_{i}^{2}\rangle\leq2/3$, correct for a spin 1 ferromagnetic system, and, for the $D=\infty$ case, $\langle S_{i}^{2}\rangle=1$, since in this limit the $S_i=0$ spin value is suppressed. In other words, the $D=\infty$ case is the two state Ising model.

<table><caption>Table 1 Estimates for $kT_c/J$ for $D=0$ in previous and in the present work.</caption>
<thead>
<tr>
<th>
</th>
<th>
$d=2,z=3$
</th>
<th>
$d=2,z=4$
</th>
<th>
$d=3,z=6$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
MFA
</td>
<td>
2
</td>
<td>
2.667
</td>
<td>
4
</td>
</tr>
<tr>
<td>
EFT [8]
</td>
<td>
1.518
</td>
<td>
2.188
</td>
<td>
3.516
</td>
</tr>
<tr>
<td>
EFT [20]
</td>
<td>
–
</td>
<td>
1.964
</td>
<td>
–
</td>
</tr>
<tr>
<td>
CVM [35]
</td>
<td>
–
</td>
<td>
–
</td>
<td>
2.886
</td>
</tr>
<tr>
<td>
Series [21,22]
</td>
<td>
–
</td>
<td>
1.688
</td>
<td>
3.192
</td>
</tr>
<tr>
<td>
RG [27]
</td>
<td>
–
</td>
<td>
2.128
</td>
<td>
3.474
</td>
</tr>
<tr>
<td>
Monte Carlo [29]
</td>
<td>
–
</td>
<td>
1.695
</td>
<td>
–
</td>
</tr>
<tr>
<td>
Monte Carlo [31]
</td>
<td>
–
</td>
<td>
1.681
</td>
<td>
–
</td>
</tr>
<tr>
<td>
Wang Landau [32]
</td>
<td>
–
</td>
<td>
1.714
</td>
<td>
–
</td>
</tr>
<tr>
<td>
Wang Landau [33,34]
</td>
<td>
–
</td>
<td>
1.693
</td>
<td>
–
</td>
</tr>
<tr>
<td>
Present work
</td>
<td>
1.591
</td>
<td>
2.322
</td>
<td>
3.678
</td>
</tr>
</tbody>
</table>

<table><caption>Table 2 Estimatives for $kT_c/J$ for $D=\infty$ in previous and in the present work.</caption>
<thead>
<tr>
<th>
</th>
<th>
$d=2,z=3$
</th>
<th>
$d=2,z=4$
</th>
<th>
$d=3,z=6$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
MFA
</td>
<td>
3
</td>
<td>
4
</td>
<td>
6
</td>
</tr>
<tr>
<td>
EFT [8]
</td>
<td>
2.103
</td>
<td>
3.088
</td>
<td>
5.076
</td>
</tr>
<tr>
<td>
CVM [35]
</td>
<td>
–
</td>
<td>
–
</td>
<td>
3.876
</td>
</tr>
<tr>
<td>
Series [21,22]
</td>
<td>
–
</td>
<td>
–
</td>
<td>
4.482
</td>
</tr>
<tr>
<td>
RG [27]
</td>
<td>
–
</td>
<td>
2.884
</td>
<td>
4.932
</td>
</tr>
<tr>
<td>
Monte Carlo [30]
</td>
<td>
–
</td>
<td>
–
</td>
<td>
4.504
</td>
</tr>
<tr>
<td>
Exact [36]
</td>
<td>
–
</td>
<td>
2.269
</td>
<td>
–
</td>
</tr>
<tr>
<td>
Present work
</td>
<td>
1.999
</td>
<td>
3.070
</td>
<td>
5.084
</td>
</tr>
</tbody>
</table>

For the honeycomb lattice our result has to be compared with the mean field and the effective field calculations. Those results are not rigorous, as ours, and the numerical values we obtain improve those mean field type results and therefore represent the upper bounds. In particular, for $D=\infty$ our result is lower than all other estimative, so it is a better (more precise) result. For $D=0$ the result we obtain here is of the same order (coincides in the second decimal figure) of the effective field one. For the square and cubic lattices besides the mean field calculation there are other results, better than mean field, obtained by series and renormalization group methods, which can be used as a comparison. As before, our results agree with the effective field ones (with a better estimative for the $D=\infty$ square lattice), with the advantage of being rigorous upper bounds, as already emphasized. In all the cases, our results are also close to those obtained by renormalization group methods.

The importance of the present numerical results lies in the fact that they were obtained using an identity and rigorous inequalities for the two-spin correlation function. For this reason they represent rigorous upper bounds for the critical temperature. In summary, the numerical results for the critical coupling obtained by the present method, which represent the rigorous bounds, are quite good when compared to other results obtained by approximated methods (MFA, CVM, EFT). Some of the other methods (MC, RG, Series) give better numerical results for the critical coupling, i.e. more precise results, although not based on rigorous procedures.

## 6. Final comments

We have presented the derivation of correlation identities for the Blume–Capel spin 1 model which are exact in all dimensions, and we have made use of correlation inequalities to obtain the upper bounds for the transition temperature. The coupling constants obtained for those bounds are calculated for $d=2$ (honeycomb and square lattices) and $d=3$ (cubic lattice). We obtain rigorous results that improve mean field type calculations. This was achieved by the use of an identity for the two-spin correlation function for the model, which is an exact result, and is derived explicitly in the paper, combined with correlation inequalities, which are rigorous and have been obtained, for the model, by various authors. This is the main advantage of the method—it is rigorous. The numerical results for the critical coupling, which represent the upper bounds, are quite good when compared to other results obtained by approximated methods. Other methods give better numerical results for the critical coupling (more precise results) although not based on rigorous procedures.

## Acknowledgments

FCSB is grateful to CAPES/Brazil for the financial support that made possible his visit to the UFSJ/Brazil. ALM acknowledges financial support from CNPq-Brazil and FAPEMIG-Brazil.

### Appendix A. Coefficients of the spin correlation identities for $d=2$, $z=3$ and $z=4$

With $k=\beta J$ and $f(x)$ given by relation (10), we have for

#### A.1. $d=2$, $z=3$

$$A_1=3f(k)>0, \tag{A.1}$$

$$A_2=(3f(2k)-6f(k))<0, \tag{A.2}$$

$$A_3=\frac{1}{4}\bigl(f(3k)-3f(k)\bigr)<0 \tag{A.3}$$

$$A_4=\frac{3}{4}\bigl(5f(k)+f(3k)-4f(2k)\bigr)>0 \tag{A.4}$$

and

$$B_0=g(0), \tag{A.5}$$

$$B_1=3(g(k)-g(0)), \tag{A.6}$$

$$B_2=\frac{3}{2}(g(2k)-g(0)), \tag{A.7}$$

$$B_3=\frac{3}{2}g(2k)+-6g(k)+\frac{9}{2}g(0), \tag{A.8}$$

$$B_4=\frac{3}{4}\bigl(g(3k)-g(k)-2g(2k)+2g(0)\bigr), \tag{A.9}$$

$$B_5=\frac{1}{4}g(3k)-\frac{3}{2}g(2k)+\frac{15}{4}g(k)-\frac{5}{2}g(0). \tag{A.10}$$

#### A.2. $d=2$, $z=4$

$$A_1=4f(k)>0, \tag{A.11}$$

$$A_2=6f(2k)-12f(k)<0, \tag{A.12}$$

$$A_3=f(3k)-3f(k)<0, \tag{A.13}$$

$$A_4=15f(k)-12f(2k)+3f(3k)>0, \tag{A.14}$$

$$A_5=\frac{1}{2}f(4k)-f(3k)-f(2k)+3f(k)>0 \tag{A.15}$$

$$A_6=\frac{1}{2}f(4k)-3f(3k)+7f(2k)-7f(k)<0 \tag{A.16}$$

and

$$B_0=g(0), \tag{A.17}$$

$$B_1=4(g(k)-g(0)), \tag{A.18}$$

$$B_2=3(g(2k)-g(0)), \tag{A.19}$$

$$B_3=3(g(2k)-4g(k)+3g(0)), \tag{A.20}$$

$$B_4=3(g(3k)-2g(2k)-g(k)+2g(0)), \tag{A.21}$$

$$B_5=g(3k)-6g(2k)+15g(k)-10g(0), \tag{A.22}$$

$$B_6=\frac{1}{8}\bigl(g(4k)-4g(2k)+3g(0)\bigr), \tag{A.23}$$

$$B_7=\frac{3}{4}g(4k)-3g(3k)+3g(2k)+3g(k)-\frac{15}{4}g(0), \tag{A.24}$$

$$B_8=\frac{1}{8}g(4k)-g(3k)+\frac{7}{2}g(2k)-7g(k)+\frac{35}{8}g(0). \tag{A.25}$$

#### A.3. $d=3$, $z=6$

$$A_1=6f(k)>0, \tag{A.26}$$

$$
A_{2}=-30 f(k)+15 f(2 k)<0, \tag{A.27}
$$

$$
A_{3}=5 f(3 k)-15 f(k)<0, \tag{A.28}
$$

$$
A_{4}=75 f(k)+15 f(3 k)-60 f(2 k)>0, \tag{A.29}
$$

$$
A_{5}=-15 f(3 k)+45 f(k)+\frac{15}{2} f(4 k)-15 f(2 k)>0, \tag{A.30}
$$

$$
A_{6}=-45 f(3 k)-105(f(k)-f(2 k))+\frac{15}{2} f(4 k)<0, \tag{A.31}
$$

$$
A_{7}=\frac{3}{8} f(5 k)-\frac{15}{8} f(3 k)+\frac{15}{4} f(k)>0, \tag{A.32}
$$

$$
A_{8}=\frac{45}{4} f(3 k)-\frac{105}{2} f(k)+\frac{15}{4} f(5 k)-15 f(4 k)+30 f(2 k)<0, \tag{A.33}
$$

$$
A_{9}=-\frac{3}{8} f(5 k)+\frac{15}{8} f(3 k)-\frac{15}{4} f(k)+\frac{3}{16} f(6 k)-\frac{3}{4} f(4 k)+\frac{15}{16} f(2 k)<0, \tag{A.34}
$$

$$
A_{10}=\frac{405}{8} f(3 k)+\frac{315}{4} f(k)+\frac{15}{8} f(5 k)-15 f(4 k)-90 f(2 k)>0, \tag{A.35}
$$

$$
A_{11}=-\frac{5}{4} f(3 k)+\frac{45}{2} f(k)+\frac{15}{2} f(4 k)-\frac{135}{8} f(2 k)-\frac{15}{4} f(5 k)+\frac{5}{8} f(6 k)>0 \tag{A.36}
$$

and

$$
B_{0}=g(0), \tag{A.37}
$$

$$
B_{1}=6(g(k)-g(0)), \tag{A.38}
$$

$$
B_{2}=\frac{15}{2}(g(2 k)-g(0)), \tag{A.39}
$$

$$
B_{3}=\frac{15}{2}(g(2 k)-4 g(k)+3 g(0)), \tag{A.40}
$$

$$
B_{4}=15(g(3 k)-2 g(2 k)-g(k)+2 g(0)), \tag{A.41}
$$

$$
B_{5}=5(g(3 k)-6 g(2 k)+15 g(k)-10 g(0)), \tag{A.42}
$$

$$
B_{6}=\frac{15}{8}(g(4 k)-4 g(2 k)+3 g(0)), \tag{A.43}
$$

$$
B_{7}=45\left(\frac{1}{4} g(4 k)-g(3 k)+g(2 k)+g(k)-\frac{5}{4} g(0)\right), \tag{A.44}
$$

$$
B_{8}=15\left(\frac{1}{8} g(4 k)-g(3 k)+\frac{7}{2} g(2 k)-7 g(k)+\frac{35}{8} g(0)\right), \tag{A.45}
$$

$$
B_{9}=\frac{1}{32}(g(6 k)-6 g(4 k)+15 g(2 k)-10 g(0)), \tag{A.46}
$$

$$
B_{10}=\frac{3}{8}(-126 g(0)+45 g(3 k)+210 g(k)-120 g(2 k)-10 g(4 k)+g(5 k)), \tag{A.47}
$$

$$
B_{11}=\frac{3}{8}\left(-\frac{55}{3} g(3 k)-66 g(k)+\frac{165}{4} g(2 k)+\frac{77}{2} g(0)+\frac{1}{12} g(6 k)+\frac{11}{2} g(4 k)-g(5 k)\right), \tag{A.48}
$$

$$
B_{12}=\frac{15}{4}(-8 g(2 k)+14 g(0)+g(5 k)-14 g(k)+13 g(3 k)-6 g(4 k)), \tag{A.49}
$$

$$
B_{13}=\frac{15}{32}(-40 g(3 k)+48 g(k)+15 g(2 k)-42 g(0)+26 g(4 k)+g(6 k)-8 g(5 k)), \tag{A.50}
$$

$$
B_{14}=\frac{15}{8}(-2 g(4 k)+8 g(2 k)-6 g(0)+g(5 k)-3 g(3 k)+2 g(k)), \tag{A.51}
$$

$$
B_{15}=\frac{15}{32}(2 g(4 k)-17 g(2 k)+14 g(0)-4 g(5 k)+12 g(3 k)-8 g(k)+g(6 k)). \tag{A.52}
$$

### Appendix B. Proof of the correlation identity for the honeycomb lattice

From Eq. (12)
$$
\left\langle F(S) S_{i}\right\rangle=\left\langle F(S) \prod_{j \neq i}\left(S_{j}^{2} \cosh \left(\beta J_{i j} \nabla\right)+S_{j} \sinh \left(\beta J_{i j} \nabla\right)+1-S_{j}^{2}\right)\right\rangle\left.f(x)\right|_{x=0}
\tag{B.1}
$$
where,
$$
f(x)=\frac{2 \mathrm{e}^{\beta D} \sinh (x)}{2 \mathrm{e}^{\beta D} \cosh (x)+1},
\tag{B.2}
$$
we obtain $\langle S_0S_l\rangle$, for the honeycomb lattice,
$$
\begin{aligned}
\left\langle S_{0} S_{l}\right\rangle= & \left\langle S_{l}\left(1+S_{1} \sinh J \nabla+S_{1}^{2}[\cosh J \nabla-1]\right) \times\left(1+S_{2} \sinh J \nabla+S_{2}^{2}[\cosh J \nabla-1]\right)\right. \\
& \left.\times\left(1+S_{3} \sinh J \nabla+S_{3}^{2}[\cosh J \nabla-1]\right)\right\rangle
\end{aligned}
\tag{B.3}
$$
where $S_1$, $S_2$ and $S_3$ are the neighbors of $S_0$.

Or,
$$
\left\langle S_{0} S_{l}\right\rangle=3 a_{1}\left\langle S_{1} S_{l}\right\rangle+6\left(a_{2}-a_{1}\right)\left\langle S_{1} S_{2}^{2}\right\rangle+a_{3}\left\langle S_{1} S_{2} S_{3}\right\rangle+\left(a_{1}-2 a_{2}+a_{4}\right)\left\langle S_{1} S_{2}^{2} S_{3}^{2}\right\rangle,
\tag{B.4}
$$
where,
$$
\begin{aligned}
& a_{1}=\left.\sinh J \nabla \cdot f(x)\right|_{x=0}=f(\beta J) \\
& a_{2}=\left.\sinh J \nabla \cosh J \nabla \cdot f(x)\right|_{x=0}=1 / 2 f(2 \beta J) \\
& a_{3}=\left.\sinh J^{3} \nabla \cdot f(x)\right|_{x=0}=1 / 4[f(3 \beta J)-3 f(\beta J)] \\
& a_{4}=\left.\sinh J \nabla \cosh ^{2} J \nabla \cdot f(x)\right|_{x=0}=1 / 4[f(3 \beta J)+f(\beta J)].
\end{aligned}
\tag{B.5}
$$

From those results we obtain Eqs. (16) and (17) of Section 3.1.

### Appendix C. Spin correlation for the one-dimensional $S=1$ Blume-Capel model

For the linear chain, we have,
$$
\left\langle S_{0}\right\rangle=\left\langle\left(1+S_{1} \sinh J \nabla+S_{1}^{2}[\cosh J \nabla-1]\right)\left(1+S_{-1} \sinh J \nabla+S_{-1}^{2}[\cosh J \nabla-1]\right)\right\rangle \cdot\left.f(x)\right|_{x=0}
\tag{C.1}
$$
with $f(x)$ given by expression (10) and $S_1$ and $S_{-1}$ are neighbors of $S_0$. We obtain for the two-spin correlation function
$$
\left\langle S_{0} S_{R}\right\rangle=\left\langle\left(S_{1} S_{R}+S_{-1} S_{R}\right)\right\rangle f(k)+\left\langle\left(S_{1} S_{-1} S_{1} S_{R}+S_{1} S_{-1} S_{-1} S_{R}\right)\right\rangle\left(\frac{1}{2} f(2 k)-f(k)\right)
\tag{C.2}
$$
where $k=\beta J$. Applying the inequalities [13,14]
$$
\begin{aligned}
& \left\langle S_{1}^{2} S_{-1} S_{R}\right\rangle \leq\left\langle S_{-1} S_{R}\right\rangle \\
& \left\langle S_{-1}^{2} S_{1} S_{R}\right\rangle \leq\left\langle S_{1} S_{R}\right\rangle
\end{aligned}
\tag{C.3}
$$
we get,
$$
\left\langle S_{0} S_{R}\right\rangle \leq\left(\left\langle S_{1} S_{R}\right\rangle+\left\langle S_{-1} S_{R}\right\rangle\right) f(k)+\left(\left\langle S_{-1} S_{R}\right\rangle+\left\langle S_{1} S_{R}\right\rangle\right)[1 / 2 f(2 k)-f(k)].
\tag{C.4}
$$

Defining $C(R)=\langle S_0S_R\rangle$ we get
$$
C(R)=A(k)(C(R+1)+C(R-1)),
\tag{C.5}
$$
where $A(k)=f(2k)/2$.

If $\gamma(R)=C(R+1)/C(R)$ is inserted in the previous equation we get
$$
1=A(k)\left(\gamma(R)+\gamma(R)^{-1}\right).
\tag{C.6}
$$

So, $C(R)=\gamma^R$ and
$$
\gamma=\frac{1+\sqrt{1-2 f(2 \beta J)}}{f(2 \beta J)}.
\tag{C.7}
$$

### References

[1] H.W. Capel, Physica 32 (1966) 966.
[2] M. Blume, Phys. Rev. 141 (1966) 517.
[3] H.B. Callen, Phys. Lett. 4 (1963) 161.
[4] M. Fisher, Phys. Rev. 162 (1967) 480.
[5] B. Simon, Commun. Math. Phys. 77 (1980) 111.
[6] D. Brydges, J. Fröhlich, T. Spencer, Commun. Math. Phys. 83 (1982) 123.
[7] E. Lieb, Commun. Math. Phys. 77 (1980) 127.
[8] A.F. Siqueira, I.P. Fittipaldi, Physica A 138 (1986) 592.
[9] R.B. Griffiths, J. Math. Phys. 10 (1969) 1559.
[10] J. Ginibre, Phys. Rev. Lett. 23 (1969) 828.
[11] G.S. Sylvester, J. Stat. Phys. 15 (1976) 327.
[12] R. Fernandez, J. Fröhlich, A.D. Sokal, Random Walks, Critical Phenomena and Triviality in Quantum Field Theory, Springer-Verlag, Berlin, 1992.
[13] G.A. Braga, S.J. Ferreira, F.C. Sa Barreto, Braz. J. Phys. 23 (1993) 343.
[14] G.A. Braga, S.J. Ferreira, F.C. Sa Barreto, J. Stat. Phys. 76 (1994) 819.
[15] D. Szàsz, J. Stat. Phys. 19 (1978) 453.
[16] C. Newman, Z. Wahrscheinlichkeitstheor. Verwandte Geb. 33 (1975) 75.
[17] F.C. Sá Barreto, M.L. O'Carroll, J. Phys. A 16 (1983) L431.
[18] F.C. Sá Barreto, A.L. Mota, J. Stat. Mech. (2012) P05006.
[19] F.C. Sá Barreto, M.L. O'Carroll, J. Phys. A 16 (1983) 1035.
[20] Y. Yüksel, Ü. Akinci, H. Polat, Phys. Scr. 79 (2009) 045009.
[21] J.G. Brankov, J. Pryzstawa, E. Praveczki, J. Phys. C 5 (1972) 3387.
[22] D.M. Saul, M. Wortis, D. Stauffer, Phys. Rev. B 9 (1974) 4964.
[23] A.N. Berker, M. Wortis, Phys. Rev. B 14 (1976) 4946.
[24] T.W. Buckhardt, Phys. Rev. B 14 (1976) 1186.
[25] T.W. Buckhardt, H.J.P. Knops, Phys. Rev. B 15 (1977) 1602.
[26] S. Moss de Oliveira, P.M.C. Oliveira, F.C. Sá Barreto, J. Stat. Phys. 78 (1995) 1619.
[27] O.F. Alcantara Bonfim, Physica A 130 (1985) 367.
[28] B.L. Arora, D.P. Landau, AIP Conf. Proc. 5 (1972) 352.
[29] P.D. Beale, Phys. Rev. B 33 (1986) 1717.
[30] A.M. Ferrenberg, D.P. Landau, Phys. Rev. B 44 (1991) 5081.
[31] J.C. Xavier, F.C. Alcaraz, D. Pena Lara, J.A. Plascak, Phys. Rev. B 57 (1998) 11575.
[32] C.J. Silva, A.A. Caparica, J.A. Plascak, Phys. Rev. E 73 (2006) 36702.
[33] A. Malakis, A.N. Berker, I.A. Hadjiagapiou, N.G. Fytas, Phys. Rev. E 79 (2009) 011125.
[34] A. Malakis, A.N. Berker, I.A. Hadjiagapiou, N.G. Fytas, T. Papakonstantinou, Phys. Rev. E 81 (2009) 041113.
[35] R. Michnas, Physica A 98 (1979) 403.
[36] L. Onsager, Phys. Rev. 65 (1944) 117.