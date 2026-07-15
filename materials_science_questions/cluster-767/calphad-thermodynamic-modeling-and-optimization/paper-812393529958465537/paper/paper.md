![](./images/812393529958465537_1.jpg)

Computers & Geosciences Vol. 20, No. 2, pp. 105-119, 1994
Copyright © 1994 Elsevier Science Ltd
Printed in Great Britain. All rights reserved
0098-3004/94 $7.00 + 0.00
0098-3004(93)E0002-W

# TEREQUIL: A PROGRAM TO CALCULATE EQUILIBRIUM COMPOSITION PAIRS IN TERNARY SYSTEMS

PIERRE-YVES F. ROBIN and DAVID G. A. BALL*

Department of Geology and Erindale Campus, University of Toronto, Mississauga, Ontario,
Canada L5L 1C6

(Received 15 June 1992; accepted 26 May 1993)

**Abstract**--TEREQUIL is a computer program to calculate 2-phase equilibria within ternary systems. Written in ANSI standard C, it can run on any micro-, mini-, or mainframe computer with an available C-compiler. TEREQUIL only requires knowing the two equations of state for the two phases examined, or one equation of state if a solvus. The algorithm minimizes the Gibbs Free Energy of the 2-phase assemblage and imposes no restriction on the form(s) of the equations of state. The equations of state, and, if convenient, some coordinate conversion formulae, need to be inserted in the listing of the program prior to compilation: thus using TEREQUIL requires some program writing.

**Key Words**: Ternary solutions, Phase equilibrium, Solvus, Equation of state.

## INTRODUCTION

Geologists and mineralogists usually are concerned with solid or liquid solutions described by more than two chemical components and in equilibrium with each other. It can be useful in particular to calculate coexisting compositions in a ternary system, or, if the compositions are described by more than three com- ponents, in some ternary subsystem.

The present program, TEREQUIL, determines the compositions, $\mathbf{X}_{a}$ and $\mathbf{X}_{b}$, of two phases, $A$ and $B$, which are in equilibrium with each other; it does this from their respective equations of state expressed as *Gibbs Free Energy* as a function of composition at fixed temperature and pressure, $G_{a}(\mathbf{X}_{a})$ and $G_{b}(\mathbf{X}_{b})$. If the two phases are described by a single equation of state, as for a solvus calculation, TEREQUIL only needs that one equation of state.

Programs to calculate coexisting pairs on a ternary solvus are available for mainframe computers. They seem to rely on particular expressions of the Gibbs Free Energy, $G$: regular solutions (e.g. Olson and Toop, 1969; Kaufman and Bernstein, 1970), sub- regular or Margules-type solutions (e.g. Turpin and Saxena, 1973), or Kohler solutions (Barron, 1978). The algorithms used by these programs to search for compositions coexisting at equilibrium calculate ac- tivities of end-member components using explicit formulae for the derivatives of $G$ with respect to compositions. Thus the search is reduced to determin- ing the compositions for which these activities are matched. Such *activity matching algorithms*, relying on specific forms of $G$ and on explicit expressions of its derivatives, also are used in the in-house programs of Nekvasil and Burnham (1987) and of Lindsley and coworkers, referred to for example in Fuhrman and Lindsley (1988) or Nekvasil and Lindsley (1990). Recently, Hanna Nekvasil and Shaoxiong Wen (SUNY at Stonybrook) have distributed a microcom- puter program, SOLVCALC, which calculates co- existing compositions for ternary feldspars using an activity matching algorithm for several equations of state.

In contrast to the programs mentioned, TERE- QUIL does not assume any specific form for $G$: it only requires entering expressions of $G$, but not of their derivatives. Instead of an activity matching algorithm, TEREQUIL iteratively searches for two coexisting compositions which directly minimize the total $G$ (see Gibbs 1875, eq. 117), subject to the constraint that the mean of the two compositions remains approximately constant (see later). Although the method used by TEREQUIL is more general than activity matching algorithms, it is correspondingly not as fast.

TEREQUIL is not a plotting program. Users are expected to plot the results with a variety of programs and output devices which we did not try to anticipate. The output therefore is strictly in the form of tables of numbers.

## SYSTEM REQUIREMENTS AND AVAILABILITY

TEREQUIL is written in ANSI standard C; in principle, it should work on any system (microcom- puter or mainframe) without modification. Several

*Present address: Department of Geological Sciences, Queen's University, Kingston, Ontario, Canada K7L 3N6.

CAGEO 20/2-B

good, and cheap, compilers exist for the IBM PC and the Apple Macintosh microcomputer systems, whereas most mainframe and minicomputers have C compilers already installed. TEREQUIL is available from the authors*.

# CALCULATING COEXISTING PAIRS

Mathematically, the problem of determining a coexisting pair amounts to minimizing the Gibbs Free Energy for a mixture of two coexisting phases, $A$ and $B$, at a given $P$ and $T$.
$$
G_{o}=f_{a} G_{a}\left(\mathbf{X}_{a}\right)_{T, P}+f_{b} G\left(\mathbf{X}_{b}\right)_{T, P} \tag{1}
$$
where $\mathbf{X}_{a}=(x_{a}, y_{a})$ and $\mathbf{X}_{b}=(x_{b}, y_{b})$ are composition vectors for the two phases, and $f_{a}$ and $f_{b}$ are fractions of $A$ and $B$, with
$$
f_{a}+f_{b}=1. \tag{2}
$$

Thus minimization is achieved for variations in $x_{a}$, $y_{a}$, $x_{b}$, and $y_{b}$, these variations being constrained by the composition of the system, $\mathbf{X}_{o}$,
$$
\mathbf{X}_{o}=f_{a} \mathbf{X}_{a}+f_{b} \mathbf{X}_{b}. \tag{3}
$$

In this implementation, $\mathbf{X}_{o}$ is the mean composition, that is $f_{a}=f_{b}=0.5$.

# ALGORITHM

The algorithm employed by TEREQUIL to calculate one coexisting pair consists of several steps.

## Initial guess of a pair of points

Before any calculation, an initial guess, in the form of a pair of compositions, must be provided. This initial guess serves two purposes: (1) it provides a mean composition, $\mathbf{X}_{o}=0.5\mathbf{X}_{a}+0.5\mathbf{X}_{b}$, approximately constraining the variations of $\mathbf{X}_{a}$ and $\mathbf{X}_{b}$ explored; (2) it should be a reasonable guess of the eventual solution, that is a guess from which successive iterations by the algorithm can converge toward that solution. As discussed in a later section, most failures to determine an answer result from a poor initial guess.

When calculating many coexisting pairs, for example to calculate complete curves, the operator only needs to specify a guess for the first pair. The program then can use the solution determined for a given $P$, $T$, and a given bulk composition as first guess for the next calculation, shifting either the bulk composition or the temperature.

In the situation of a solvus, the first pair given can be replaced by spinodal points which can be calculated readily along a 'binary' section defined by that first pair. Spinodal points are the two inflexion points of the $G(\mathbf{X})$ curve along the 'binary' section; they are determined by monitoring the value of the slope of that curve calculated by finite difference at small intervals. Near critical conditions, spinodal points may be a more reliable starting guess than that which would be obtained by a shift from a previous calculation.

## Main loop

The main loop varies the compositions, $\mathbf{X}_{a}$ and $\mathbf{X}_{b}$, until two successive calculations do not differ by more than $0.1\%$ in any one component of $\mathbf{X}_{a}$ and $\mathbf{X}_{b}$. The minimization is accomplished by searching alternately (1) along a 'binary' section, and then (2) along 'perpendiculars'† to that 'binary' section. In this context, a 'binary' section only indicates the set of compositions along the tieline defined by the current

![](./images/812393529958465537_2.jpg)

Figure 1. Schematic illustration of successive operations to search for coexisting composition $\mathbf{X}_{a}$ and $\mathbf{X}_{b}$ in ternary system. Each passage through main loop of TEREQUIL starts with pairs $\mathbf{X}_{a}^{\mathrm{s}}$ and $\mathbf{X}_{b}^{\mathrm{s}}$. 'Binary' search yields $\mathbf{X}_{b}^{\mathrm{b}}$ and $\mathbf{X}_{a}^{\mathrm{b}}$; perpendicular search yields $\mathbf{X}_{o}^{\mathrm{p}}$ and $\mathbf{X}_{a}^{\mathrm{p}}$. If $\mathbf{X}_{o}^{\mathrm{p}}$ and $\mathbf{X}_{l}^{\mathrm{p}}$ differ from $\mathbf{X}_{o}^{\mathrm{s}}$ and $\mathbf{X}_{b}^{\mathrm{s}}$ by more than set value in any one of their components, loop iterates, using $\mathbf{X}_{a}^{\mathrm{p}}$ and $\mathbf{X}_{b}^{\mathrm{p}}$ as new values for $\mathbf{X}_{a}^{\mathrm{s}}$ and $\mathbf{X}_{b}^{\mathrm{s}}$.

---
*Send a cheque or money order for CDN$50, payable to U. of Toronto, to P.-Y. Robin, to cover the costs of the diskette and of its production, postage, and administrative handling. The administrative costs of handling purchase orders is significantly higher, and the charge is then CDN$100. Please specify IBM or Macintosh disk format. Alternately, and preferably, you may download the program, using FTP, from Site 130.15.110.8 (log on as guest; the password also is guest; download the file TEREQUIL.C). For an additional fee, we are willing to enter an equation of state for those users intimidated by the C-language. Contact either author. The fee, to be negotiated case-by-case, would depend on the complexity of the equation(s) of state.
†The directions explored in the composition space are strictly perpendicular to the tieline only when the composition coordinates form a Cartesian coordinate system. See the later discussion of coordinate systems.

pair of compositions. The current pair is updated during the iteration; as explained next (Search along perpendiculars), there may result a small drift of the constraining mean composition as the calculation proceeds. The sequence is illustrated by Figure 1. The main loop starts from the current pair, $\mathbf{X}_{a}^{\mathrm{s}}$ and $\mathbf{X}_{b}^{\mathrm{s}}$, which may be either the initial guess as discussed or the result of a previous passage through the main loop.

‘Binary’ search: the exploration along a ‘binary’ section is itself an iterative process, done within an inner loop. A mean composition, $\mathbf{X}_{o}$, is calculated from the ‘binary’ pair by taking $f_{a}=f_{b}=0.5$, and then change successively $\mathbf{X}_{a}$ and $\mathbf{X}_{b}$ (and, accordingly, $f_{a}$ and $f_{b}$) to minimize $G_{o}$. The process is iterated in the inner loop until two successive pairs differ by less than a selected test value (0.1%). The result of the ‘binary’ search is a revised current pair, $\mathbf{X}_{a}^{\mathrm{b}}$ and $\mathbf{X}_{b}^{\mathrm{b}}$ (Fig. 1). Note that the new mean composition, $\mathbf{X}_{o}^{\mathrm{b}}$, should not exactly coincide with the starting mean composition, $\mathbf{X}_{o}^{\mathrm{s}}$.

Search along perpendiculars searches the minimum of $G_{o}=0.5 G_{a}+0.5 G_{b}$ when $\mathbf{X}_{a}$ and $\mathbf{X}_{b}$ are migrated from $\mathbf{X}_{a}^{\mathrm{b}}$ and $\mathbf{X}_{b}^{\mathrm{b}}$ by equal amounts, but opposite directions, along directions perpendicular* to the ‘binary’ section (Fig. 1). The compositions explored are constrained to rotate around the midpoint (or mean), $\mathbf{X}_{o}^{\mathrm{b}}$, between the two compositions, $\mathbf{X}_{a}^{\mathrm{b}}$ and $\mathbf{X}_{b}^{\mathrm{b}}$, determined by the ‘binary’ search. As pointed out, and illustrated in Figure 1, $\mathbf{X}_{o}^{\mathrm{b}}$ should generally differ from $\mathbf{X}_{o}^{\mathrm{s}}$; therefore there is the possibility of a drift in the constraining mean composition. Although such drift has not been significant in our calculations, it could become so in other situations. This search yields a new current pair, $\mathbf{X}_{a}^{\mathrm{p}}$ and $\mathbf{X}_{b}^{\mathrm{p}}$ (Fig. 1).

Differences between components of the result $\mathbf{X}_{a}^{\mathrm{p}}$ and $\mathbf{X}_{b}^{\mathrm{p}}$ obtained and those of the starting points, $\mathbf{X}_{a}^{\mathrm{s}}$ and $\mathbf{X}_{b}^{\mathrm{s}}$ are calculated. If any such difference exceeds a certain predetermined value, the latest values, $\mathbf{X}_{a}^{\mathrm{p}}$ and $\mathbf{X}_{b}^{\mathrm{p}}$, then are used as $\mathbf{X}_{a}^{\mathrm{s}}$ and $\mathbf{X}_{b}^{\mathrm{s}}$ in the main loop.

## REQUIRED INPUT

The user must supply to TEREQUIL either two distinct equations of state, $G_{a}(\mathbf{X})$ and $G_{b}(\mathbf{X})$, or, when calculating a solvus, one equation of state, $G(\mathbf{X})$, and a flag to alert the program that it is calculating a solvus. The example supplied in the shipped version is the equation of state of Elkins and Groves (1990) for high-temperature ternary Ca-Na-K feldspars. To explore a different system, the user must replace the feldspar example in the source code by one or two new equations and recompile the program. The parts of the program that require alteration for a new equation of state are marked clearly by comments in the source code.

## PROPER COORDINATES

The algorithm used is valid only if the composition parameters are ‘proper’ vector coordinates in a composition space. Proper vector coordinates are such that the colinearity of three compositions and the lever rule are respected. Ternary Ca-Mg-Fe pyroxenes provide an example for which a set of composition parameters may be convenient but not ‘proper’. It is convenient to describe ternary clinopyroxenes, and to express their equations of state, with ‘user coordinates’ such as

$$
x_{u}=\frac{N_{\mathrm{Fe}}}{N_{\mathrm{Fe}}+N_{\mathrm{Mg}}}, \quad y_{u}=\frac{2 N_{\mathrm{Ca}}}{N_{\mathrm{Ca}}+N_{\mathrm{Fe}}+N_{\mathrm{Mg}}} \tag{4}
$$

where the $N$’s are numbers of gram-formula-weights of each component in a given amount of solution. But these user coordinates, illustrated in Figure 2A, are not proper coordinates. This point can be demonstrated simply. Using the given parameters, the composition of diopside is $x_{u}=0, y_{u}=1$, whereas the composition of ferrosilite is $x_{u}=1$, $y_{u}=0$. An equal gram-formula-weight mixture of ferrosilite and diopside, shown as a solid circle in Figure 2A, is $x_{u}=2 / 3, y_{u}=0.5$; it is not $x_{u}=0.5$, $y_{u}=0.5$ (open circle), the mean value of the improper composition parameters used to describe the two phases. Similarly, in other ternary systems, improper composition parameters may be conventional descriptions of phase compositions, and be good parameters to use in equations of state for its phases.

On the other hand, any description of a ternary solution of components J, K, and L by parameters such as $x=N_{\mathrm{J}} /\left(N_{\mathrm{J}}+N_{\mathrm{K}}+N_{\mathrm{L}}\right)$ and $y=N_{\mathrm{K}} /$ $\left(N_{\mathrm{J}}+N_{\mathrm{K}}+N_{\mathrm{L}}\right)$ is proper, in that it satisfies the requirements of colinearity and lever rule. In the shipped feldspar example, the program uses $x=N_{\mathrm{Or}} /$ $\left(N_{\mathrm{Or}}+N_{\mathrm{Ab}}+N_{\mathrm{An}}\right)$ and $y=N_{\mathrm{Ab}} /\left(N_{\mathrm{Or}}+N_{\mathrm{Ab}}+N_{\mathrm{An}}\right)$. As a guide, composition parameters are proper when lines corresponding to fixed, equally spaced values of one parameter are represented by parallel, equally spaced straightlines in a usual triangular plot (e.g. Figs. 2B and 2C). (It should be noted that these requirements are sufficient but not necessary: proper coordinates may satisfy this parallel, equally spaced criterion in some geometric projection of the usual triangular plot whereas not satisfying it on the triangular plot itself.)

It therefore is essential to convert any convenient but improper composition parameters to proper ones. The user must enter a formula in USERTO PROG to convert from the convenient but improper parameters, $x_{u}$ and $y_{u}$, to proper coordinates, x and y. The Gibbs Free Energy equations are assumed to be in terms of the convenient parameters $x_{u}$ and $y_{u}$, and therefore USERTOPROG is called before any calculation of $G$. The user also must write the opposite transformation formula, from x and y to $x_{u}$ and $y_{u}$, in PROGTOUSER in order to receive the

*See second footnote on p. 106.

![](./images/812393529958465537_3.jpg)

Figure 2. Examples of 'improper' and 'proper' compositional coordinates in ternary system. A-Shows 'improper' coordinates which do not satisfy colinearity and lever rules but may be convenient to express equation of state and results; B and C are two examples of 'proper' coordinates. In 'proper' coordinates, composition coordinates are components of composition vectors in composition space. It follows that equal mixture of two compositions has components equal to average values of end-member components.

results in convenient coordinates. If the user parameters already are proper, as in the shipped feldspar example, the user can simply enter
$$x = xu; \quad y = yu \text{ in USERTOPROG},$$
and
$$xu = x; \quad yu = y \text{ in PROGTOUSER}.$$

![](./images/812393529958465537_4.jpg)

Figure 3. Comparison of Elkins and Grove's (1990) experimental data on ternary feldspars for 1 kbar, with model composition pairs determined by TEREQUIL using their equation of state. Round symbols and solid tielines are "adjusted compositions" determined by Elkins and Grove (1990) from actual experimental data. Square symbols and dotted tielines give model pairs determined by TEREQUIL.

## DISCUSSION

Figure 3 compares the experimental tielines of Elkins and Grove (1990) with those determined by the program for their equation of state, and it shows a good correlation. Figure 4 shows the 1 kbar solvus for the ternary feldspars as calculated by TEREQUIL. If a given equation of state predicts equilibrium pairs which differ appreciably from the experimental ones, the program can be used empirically to modify the parameters to improve the fit and thus improve the equation of state.

## PROBLEMS AND ADVICE ON HOW TO MINIMIZE THEM

(1) Wandering of mean composition: in the course of a search, the mean composition can drift away

![](./images/812393529958465537_5.jpg)

Figure 4. Ternary feldspar solvus as defined by six pairs of equilibrium compositions, calculated by TEREQUIL at each of 700,800 , and $900^{\circ} \mathrm{C}$, using equation of state of Elkins and Grove (1990). Dotted lines are six tielines for $900^{\circ} \mathrm{C}$.

Calculating equilibrium composition pairs in ternary systems

from the initial tieline, as shown in Figure 1 and as discussed; this may become a problem when trying to model specific experimental data. This drift can be minimized by selecting starting points which are as close as possible to the final model pair.

(2) The program fails when:
(a) it leads to 'out-of-bounds' compositions; users are advised to follow the example given in the example program by programming a detailed list of checks on composition valuesbefore calculating $G$;
(b) in the situation of a solvus, it returns the same composition for both points.

(3) Such failure may occur if the initial guess is poor, either
(a) because of a wrong orientation of the guessed 'binary' section, or,
(b) in the situation of a solvus, two guess com- positions which are outside of, and on the same side of, the 'binary' spinodal.

Clearly, a preliminary knowledge of the general features of the solution should make the search easier.

(4) When exploring a solvus near the critical con- ditions, change $T$ or $X$ by small steps. Of course, if the program insists on returning $X_{a}=X_{b}$, you may be above the critical conditions!

(5) The program may go 'out-of-bounds' in nor- mal, operating conditions. The program explores compositions by discrete steps: thus, guess compo- sitions which are too close to a bound, or that coincide with it, may yield out-of-bound compo- sitions. To avoid this problem, make initial guesses which differ from the bounds by more than $\sim 0.2 \%$.

(6) The Gibbs Free Energy function must be defined carefully so as not to require the program to calculate functions such as $\ln 0$.

Acknowledgments-The authors are grateful to D. H. Lind- sley for his insightful comments and suggestions, which helped in greatly improving the manuscript. This research was supported by grants to P.-Y. Robin from the National Science and Engineering Research Council and Erindale College, University of Toronto.

REFERENCES

Barron, L. M., 1978, A simple method of estimating the binodal surface: Geochemical Jour., v. 12, p.101-105.

Elkins, L. T., and Grove, T. L., 1990, Ternary feldspar experiments and thermodynaic models: Am. Mineralo- gist, v. 75, no. 3, p. 544-559.

Fuhrman, M. L., and Lindsley, D. H., 1988, Ternary- feldspar modeling and thermometry: Am. Mineralogist, v. 73, no. 2, p. 201-215.

Gibbs, J. W., 1875, On the equilibrium of heterogeneous substances: Trans. Connecticut Academy, III, Reprinted in: The scientific papers of J. Willard Gibbs, Vol. 1, Thermodynamics: Dover Publications, Inc., 1961, New York, p.91.

Kaufman, L., and Bernstein, H., 1970, Computer calculation of phase diagrams with special reference to refractory metals: Academic Press Inc., New York,334 p.

Nekvasil, H., and Burnham, C. W., 1987. The calculated individual effects of pressure and water content of phase equilibria in the granite system, in Mysen, B. O., ed., Magmatic processes: physicochemical principles-a vol- ume in honor of Hatten S. Yoder, Jr.: The Geochemical Society Spec. Publ. 1, p. 433-445.

Nekvasil, H., and Lindsley, D. H., 1990, Termination of the2 feldspar + liquid curve in the system $Ab-Or-An-H_{2} O$  at low $H_{2} O$ contents: Am. Mineralogist, v. 75, no. 5, p.1071-1079.

Olson, N. J., and Toop, G. W., 1969, Predicting ternary phase diagrams and quaternary excess free-energy using binary data: Trans. Metallurgical Society of AIME, v.245, p. 905-910.

Turpin, F., and Saxena, S. K., 1973, program TERNGAP, in Saxena, S. K., ed., Thermodynamics of rock-forming crystalline solutions: Springer-Verlag, New York, p.174-178.

# TEREQUIL.C

## Program to Calculate Equilibrium Compositions in Ternary Systems

```c
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>

/************************************************************************/
/*                            FUNCTION DEFINITIONS                     */
/************************************************************************/

void USERTOPROG();
void PROGTOUSER();
double GIBBS(int A_or_B);
double Calc_Wg(double Wh, double Ws, double Wv);
double Calc_Ge(double X1, double X2, double X3, double W23, double W32, double W31,
double W13, double W21, double W12, double W123);

void MAINPROG();

int MENU();
void TEMPINPUT();
void TEMPDEC();
void COMPINPUT();
```

```c
void SETMIGRATIONMAGNITUDE();
void COMPINCR(int forwards);
void COMPOSITION_ERROR();
void COMPRINT();
void VALPRINT();
void FVALPRINT();
void SEARCHALONG(int A_or_B);
void BINSPIN();
void SPINSEARCH();

double GETVALUE(char *prompt);
void CLS();
void WAITFORKEY();

/******************************************************************************/
/*                            VARIABLES AND CONSTANTS                         */
/******************************************************************************/

double tst1 = .001;
double tst2 = .001;

double stp1 = .0005;    /* step sizes */
double stp2 = .0002;

/* ====================== important global variables ====================== */

double r = 8.31434;  /* gas constant */
double t = 890;      /* temperature */
double rt;           /* temperature x gas constant */

double x, y;          /* general program coordinates */
double xu, yu;        /* general user coordinates */
double xa, ya, btr, ctr;  /* general triangular coordinates */

double xa, ya;        /* coexisting pair a */
double xb, yb;        /* coexisting pair b */

double dx, dy;       /* Delta x and Delta y */
double dex, dey;
double del;
double Migration = 0.05;  /* magnitude of tieline migration */

double dg;               /* Delta g (Gibbs Energy) */
double lastg;

double stp;
int ipf = 0;        /* flags */
int spn;
int FirstGuessEntered = 0;
char *OnOff[2];

FILE *fp;           /* file handle for output file */

int counter;
char ms[50];

/* ======================================================================= */

/******************************************************************************/
/*                                  CODE                                     */
/******************************************************************************/

/*    COORDINATE TRANSFORMATIONS and GIBBS FUNCTION(S) are specific to each problem and
    must be entered by the user.  The example supplied here is the equation of state
    for ternary feldpars proposed by Elkins and Grove (American Mineralogist, Vol. 75,
    pp. 544-559, 1990)*/

/* ======================================================================= */
/*                        COORDINATE TRANSFORMATIONS                         */
/* ======================================================================= */

double Xor, Xab, Xan;    /*  Composition parameters used in equation of state */

void USERTOPROG()

/* calculates x, y from Xab, Xor (note: we do not need Xan here)
    x,y - proper composition coordinates used by terequil   */

{   y = yu; Xab = yu;
```

```c
    x = xu; Xor = xu;
}

/* ====================================================================== */

void PROGTOUSER()

/* calculates Xab, Xor and Xan from x, y
   Xab, Xor, Xan - composition parameters used in equation of state */

{
    Xor = x; xu = x;
    Xab = y; yu = y;
    Xan = 1 - Xor - Xab;
}
/* ====================================================================== */
/*                            GIBBS ENERGY FUNCTION                       */
/* ====================================================================== */

int Two_Functions = 0;

/*    Two_Functions:
    if two Gibbs functions are defined, set the value of this flag to 1;
    if only one Gibbs function is defined, set the value of this flag to 0  */

char *GIBBS_DESC = "Feldspars"; /* name of system under investigation */

/* introductory statements output with data */

char *Intro1 = "SOLVUS IN THE Ab, Or, An TRIANGLE";
char *Intro2 = "based on the equation of state of Elkins and Grove (1990)";

double GIBBS(int A_or_B)

/* This function calculates the Gibbs energies for a specified composition */

{
/* ========================== variables ============================= */

    double g;                /* final calculated value of g */

    double Lan;              /* Xan*ln(Xan) */
    double Lab;              /* Xab*ln(Xab) */
    double Lor;              /* Xor*ln(Xor) */
    /* Margules parameters */
    double Wabor, Worab, Waban, Wanab;
    double Woran, Wanor, Waboran;
    double Ge_an, Ge_ab, Ge_or;

/* ========================== code ================================== */

    /* define Wg (note: values for Wh, Ws and Wv from Elkins and
       Grove (1990); table 4)  */

    Wabor   = Calc_Wg(18810.0, 10.3,  0.4602);
    Worab   = Calc_Wg(27320.0, 10.3,  0.3264);
    Waban   = Calc_Wg( 7924.0,  0.0,  0.0);
    Wanab   = Calc_Wg(    0.0,  0.0,  0.0);
    Woran   = Calc_Wg(40317.0,  0.0,  0.0);
    Wanor   = Calc_Wg(38974.0,  0.0, -0.1037);
    Waboran = Calc_Wg(12545.0,  0.0, -1.095);

    PROGTOUSER();
    if (A_or_B == 'A' || !Two_Functions)    /* do calculations with first Gibbs
                                               function */
    {
      if (Xan < 0)  { printf("\n\n\rERROR: Xan = %.3f, negative!!", Xan); exit(0);}
      if (Xan > 1)  { printf("\n\n\rERROR: Xan = %.3f, > 1 !!", Xan); exit(0); }
      if (Xan == 0) Lan = 0; else Lan = Xan * log(Xan);
      if (Xab < 0)  { printf("\n\n\rERROR: Xab = %.3f, negative!!", Xab); exit(0); }
      if (Xab > 1)  { printf("\n\n\rERROR: Xab = %.3f, > 1 !!", Xab); exit(0); }
      if (Xab == 0) Lab = 0; else Lab = Xab * log(Xab);
      if (Xor < 0)  { printf("\n\n\rERROR: Xor = %.3f, negative!!", Xor); exit(0); }
      if (Xor > 1)  { printf("\n\n\rERROR: Xor = %.3f, > 1 !!", Xor); exit(0); }
      if (Xor == 0) Lor = 0; else Lor = Xor * log(Xor);

      /* excess free energy terms */

      Ge_an = Calc_Ge(Xan,Xor,Xab,Worab,Wabor,Waban,Wanab,Woran,Wanor,Waboran);
      Ge_ab = Calc_Ge(Xab,Xan,Xor,Wanor,Woran,Worab,Wabor,Wanab,Waban,Waboran);
      Ge_or = Calc_Ge(Xor,Xab,Xan,Waban,Wanab,Wanor,Woran,Wabor,Worab,Waboran);
```

```c
/* calculation of Gibbs free energy */
  g  = rt * (Lab + Lan + Lor) + Xab * Ge_ab + Xan * Ge_an + Xor * Ge_or;
}

else  /* do calculations with second Gibbs function */

{
  /* Enter second Gibbs function here if it is required */
}

  return(g);
}

/* ====================================================================== */

double Calc_Wg(double Wh, double Ws, double Wv)

/* calculates Wg (Excess free energy terms) from for each given T and P
   from Wh, Ws, Wv (passed on numerically; ie. data from Elkins and Grove's
   table 4)  */

{
    double Wg;
    Wg = Wh - (t + 273.15) * Ws + 1000 * Wv;  /* note: 1000 = pressure in bars */
    return(Wg);
}

/* ====================================================================== */

double Calc_Ge(double X1, double X2, double X3, double W23, double W32, double W31,
double W13, double W21, double W12, double W123)

/* calculates excess free energy of mixing for a given end member */

{
    double Ge, Tmp;

    Tmp = X3 * X2 * (0.5 - X1);
    Ge = W123 * (X2 * X3 * (1.0 - 2 * X1));
    Ge += W23 * (X3 * X2 * (0.5 - X1 - 2 * X3));
    Ge += W32 * (X3 * X2 * (0.5 - X1 - 2 * X2));
    Ge += W31 * (2 * X3 * X1 * (1.0 - X1) + Tmp);
    Ge += W21 * (2 * X2 * X1 * (1.0 - X1) + Tmp);
    Ge += W13 * (X3 * X3 * (1.0 - 2.0 * X1) + Tmp);
    Ge += W12 * (X2 * X2 * (1.0 - 2.0 * X1) + Tmp);
    return(Ge);
}

/* ====================================================================== */
/*                            end of user-supplied code                   */
/* ====================================================================== */

void main()

{
    char FileName[100];
    int m;

    CLS();
    spn = (!Two_Functions);
    OnOff[0] = "OFF"; OnOff[1] = "ON ";
    rt = r * (t + 273.15);

    printf("                        *******************************\n\r");
    printf("                            TEREQUIL                   *\n\r");
    printf("                        *******************************\n\n\r");
    printf("                            TERNARY SOLVER\n\n\r");
    printf("                            by Pierre-Yves Robin\n\n\r");
    printf("                        Translated to C by David G.A. Ball\n\r");
    printf("                                1990\n\n\r");
    printf("A program to calculate coexisting equilibrium compositions from the\n\r");
    printf("equation(s) of state given as GIBBS free energies as a function of\n\r");
    printf("composition.\n\n\n\n");

    WAITFORKEY();

    CLS();
    printf("Enter the name of the file for program output.\n\r");
    printf("ON THE IBM PC: Enter 'LPT1' for printer output,\n\r");
    printf("                    or 'NUL' for output to the screen only\n\n\r");
    printf("Enter name: "); scanf("%s", FileName);
    if ((fp = fopen(FileName, "w")) == NULL)
    {
      printf("ERROR: Error opening file!!");
```

```c
    exit(0);
  }
  fprintf(fp, Introl); fprintf(fp, "\n");
  fprintf(fp, Intro2); fprintf(fp, "\n");
  for (;;)
  {
    m = MENU();
    switch (m)
    {
  case 1:
    TEMPINPUT();
    break;
  case 2:
    TEMPDEC();
    break;
  case 3:
    COMPINPUT();
    break;
  case 4:
    SETMIGRATIONMAGNITUDE();
    break;
  case 5:
  case 6:
    if (!FirstGuessEntered)
    {
      printf("\n\nERROR: Enter first guess first!!");
      WAITFORKEY();
    }
    else
      COMPINCR(m - 6);
    break;
  case 7:
    if (!FirstGuessEntered)
    {
      printf("\n\nERROR: Enter first guess first!!");
      WAITFORKEY();
    }
    else
      MAINPROG();
    break;
  case 8:
    if (!Two_Functions)
      spn = 1 - spn;
    else
    {
      printf("\n\nERROR: There are no spinodal points for two Gibbs functions!!");
      WAITFORKEY();
    }
    break;
  case 9:
    ipf = 1 - ipf;
    break;
  case 10:
    CLS();
    printf("                GoodBye from TEREQUIL\n\n\n\n\n\n\n\n\n\n\n\n\n\n\r");
    exit(0);
  default:
    break;
    }
  }
}

/* ================================================================ */

int MENU()     /* Main menu */
{
    int selection;

    CLS();
    printf("                        TEREQUIL:  MAIN MENU\n\n\r");
    printf("  Current system: %s\n\n\r", GIBBS_DESC);
    printf("  1: Choose a new temperature. Current temperature: %.2f Celsius\n\r", t)
    printf("  2: Decrease temperature by Delta T = 50 Celsius\n\r");
    printf("  3: Choose first/new guesses, A and B\n\r");
    printf("  4: Set magnitude of tieline migration. Current value: %.3f\n\r",
Migration);
    printf("  5: Forward migration of A & B compositions perpendicular to current
tieline\n\r");
    printf("  6: Backward migration of A & B compositions perpendicular to current
tieline\n\r");
    printf("  7: Go....\n\r");
```

```c
printf("  8: Find spinodal points before first binary pair (toggle): ");
printf(OnOff[spn]); printf("\n\r");
printf("  9: Display intermediate results (toggle): "); printf(OnOff[ipf]);
printf("\n\r");
printf(" 10: Exit\n\n\r");
printf(" 11: Reprint Menu\n\n");

x = xa; y = ya; PROGTOUSER();
printf("    Current compositions:  Xa = %2.3f       Ya = %2.3f\n\r", xu, yu);
x = xb; y = yb; PROGTOUSER();
printf("                          Xb = %2.3f       Yb = %2.3f\n\n\r", xu, yu)
if (Two_Functions)
  printf("    Note: Two Gibbs functions defined\n\n");
else
  printf("    Note: One Gibbs function defined\n\n");
do
{
  fflush(stdin);
  printf("    Enter Selection: "); scanf("%d", &selection); printf("\n\r");
}
while (selection < 1 || selection > 11);
return(selection);
}

/* =============================================================== */

void TEMPINPUT()

/* enter a new temperature from the keyboard */
{
    CLS();
    printf("Old temperature: %.2f degrees Celsius\n\r", t);
    t = GETVALUE("Temperature (in degrees Celsius): ");
    rt = r * (t + 273.15);
}

/* =============================================================== */

void TEMPDEC()

/* decrease current temperature by 50 degrees Celsius */
{
    t = t - 50;
    rt = r * (t + 273.15);
}

/* =============================================================== */

void COMPINPUT()

/* Enter initial guess at a composition */
{
    CLS();
    printf("                        ENTER INITIAL/NEW COMPOSITION\n\n\n\r");
    xu = GETVALUE("Guess composition of A, user coordinates - Xa: ");
    yu = GETVALUE("                                                Ya: ");
    USERTOPROG(); xa = x; ya = y;
    printf("\n\n\r");
    xu = GETVALUE("Guess composition of B, user coordinates - Xb: ");
    yu = GETVALUE("                                                Yb: ");
    USERTOPROG(); xb = x; yb = y;
    FirstGuessEntered = -1;
}

/* =============================================================== */

void SETMIGRATIONMAGNITUDE()

{
    printf("\n\n\rCurrent magnitude of migration step (program coordinates):
%.3f\n\r", Migration);
    Migration = GETVALUE("Enter new step: ");
}

/* =============================================================== */

void COMPINCR(int forwards)

/* drift tie line perpendicular to current tieline */
/* note: movement occurs in program (i.e. 'proper') coordinates */

{   /* find values dx, dy */
```

```c
dex = xb - xa;
dey = yb - ya;
del = sqrt(dex * dex + dey * dey);
dx = Migration * dex / del; dy = Migration * dey / del;

/* move points inward first */

xa += dx; ya += dy;
xb -= dx; yb -= dy;

/* check for direction of movement */

if (!forwards) { dx = -dx; dy = -dy; }

/* move POINTS A and B by dx and dy */

xa += dy; ya -= dx;
xb += dy; yb -= dx;
}

/* ============================================================= */

void COMPOSITION_ERROR()
{
    printf("\n\n\rERROR: Compositional value out of range!!");
    WAITFORKEY();
}

/* ============================================================= */

void COMPRINT()

/* printing results */
{
    printf("%3d %8s A:", counter, ms);
    x = xa; y = ya; VALPRINT();
    printf("\n\r           B:");
    x = xb; y = yb; VALPRINT();
    printf("\n\n\r");

    fprintf(fp, "%3d %8s A:", counter, ms);
    x = xa; y = ya; FVALPRINT();
    fprintf(fp, "\n           B:");
    x = xb; y = yb; FVALPRINT();
    fprintf(fp, "\n\n");
}

/* ============================================================= */

void VALPRINT()

/* called by COMPRINT */
{
    PROGTOUSER();
    ctr = 100 * y;
    btr = 100 * x;
    atr = 100 - btr - ctr;
    printf(" %7.4f %7.4f", xu, yu);
    printf("   %6.1f   %6.1f   %6.1f", atr, btr, ctr);
    printf("   %7.4f %7.4f", x, y);
}

/* ============================================================= */

void FVALPRINT()

/* called by COMPRINT */
{
    PROGTOUSER();
    ctr = 100 * y;
    btr = 100 * x;
    atr = 100 - btr - ctr;
    fprintf(fp, " %7.4f %7.4f", xu, yu);
    fprintf(fp, "   %6.1f   %6.1f   %6.1f", atr, btr, ctr);
    fprintf(fp, "   %7.4f %7.4f", x, y);
}

/* ============================================================= */

void MAINPROG()
```

```c
{
    double lxa, lya, lxb, lyb, del, sumg, dela, delb;
    double fa, fb, ga, gb, g0, last_g0, xat, xbt, yat, ybt;
    int side;
    struct tm *now;
    time_t tme;

    CLS();

    stp = stp1;

    printf("TEMPERATURE: %-7.2f Celsius", t);
    time(&tme); now = localtime(&tme); printf("        Time: %s\n\n\r", asctime(now));
    printf("COMPOSITIONS:        User                Triangular");
    printf("            Cartesian\n\r");
    printf("                      xu    yu        A        B        C");
    printf("        x        y\n\n\r");

    fprintf(fp, "\n\nTEMPERATURE: %.2f Celsius", t);
    fprintf(fp, "        Time: %s\n\n", asctime(now));
    fprintf(fp, "COMPOSITIONS:        User                Triangular");
    fprintf(fp, "            Cartesian\n\r");
    fprintf(fp, "                      xu    yu        A        B        C");
    fprintf(fp, "        x        y\n\n");

    counter = 0; strcpy(ms, "Start"); COMPRINT();
if (spn) BINSPIN();

/* main loop searching for values of coordinate pairs which minimize the Gibbs
energy of the mixture */

do
{
    counter++;

    if (last_g0 > g0) stp = stp2;

    lxa = xa; lya = ya;
    lxb = xb; lyb = yb;
    dex = xb - xa; dey = yb - ya;
    del = sqrt(dex * dex + dey * dey);
    dx = stp * dex / del; dy = stp * dey / del;

    /* BINARY SEARCH: Find minimum of G on binary section */

    /* Calculate starting values for Ga and Gb */
    x = xa; y = ya; ga = GIBBS('A');
    x = xb; y = yb; gb = GIBBS('B');

    do
    {
        xat = xa; yat = ya; /* STORE VALUES FOR A AND B TO CHECK FOR  */
        xbt = xb; ybt = yb; /* STABLE VALUES IN BINARY SEARCH */

        dela = delb = 0.5 * del;
        last_g0 = 0.5 * (ga + gb);

    /*  SEARCH FOR Xa */
    /*  SEARCH FOR PROPER DIRECTION OF MIGRATION */
        xa += dx; ya += dy;
        del -= stp; dela -= stp;
        fa = delb/del; fb = dela/del; /* LEVER RULE */
        x = xa; y = ya ; ga = GIBBS('A');
        g0 = fa*ga + fb*gb;
        if (g0 > last_g0) { dx = -dx; dy = -dy; stp = -stp; }

        for(;;)
        {
            xa += dx; ya += dy;
            del -= stp; dela -= stp;
            fa = delb/del; fb = dela/del;
            if (fa < 0) break;
            x = xa; y = ya; ga = GIBBS('A');
            g0 = fa*ga + fb*gb;
            if (g0 > last_g0)
            {
            xa -= dx; ya -= dy; /*  OOPS!  WENT TOO FAR!  GOT TO GO BACK */
            x = xa; y = ya; ga = GIBBS('A');
            del += stp; dela += stp;
            break; /* EXIT LOOP IF g0 INCREASES INSTEAD OF DECREASES*/
            }
        last_g0 = g0;
```

```c
)

dela = delb = 0.5 * del;
last_g0 = 0.5 * (ga + gb);
/* SEARCH FOR Xb */
/* SEARCH FOR PROPER DIRECTION OF MIGRATION */
xb += dx; yb += dy;
del += stp; delb += stp;
fa = delb/del; fb = dela/del;
x = xb; y = yb ; gb = GIBBS('B');
g0 = fa*ga + fb*gb;
if (g0 > last_g0) { dx = -dx; dy = -dy; stp = -stp; }

for(;;)
{
  xb += dx; yb += dy;
  del += stp; delb += stp;
  fa = delb/del; fb = dela/del;
  if ( fb < 0 ) break;
  x = xb; y = yb ; gb = GIBBS('B');
  g0 = fa*ga + fb*gb;
  if (g0 > last_g0)
    {
      xb -= dx; yb -= dy; /* OOPS! WENT TOO FAR! GOT TO GO BACK */
      x = xb; y = yb; gb = GIBBS('B');
      del -= stp; delb -= stp;
      break; /* EXIT LOOP IF g0 INCREASES INSTEAD OF DECREASES*/
    }
  last_g0 = g0;
}
}
while (fabs(xa - xat) > tst1 || fabs(ya - yat) > tst1 ||
     fabs(xb - xbt) > tst1 ||  fabs(yb - ybt) > tst1);

if (ipf) { strcpy(ms, "Binary"); COMPRINT(); }

/* SEARCH ALONG PERPENDICULARS to section for minimum of (GA + GB) */

last_g0 = (ga + gb) * 0.5;

/* CHECK FOR SENSE */
xa += dy; ya -= dx;
x = xa; y = ya; ga = GIBBS('A');
xb -= dy; yb += dx;
x = xb; y = yb; gb = GIBBS('B');
g0 = (ga + gb) * 0.5;
if (g0 > last_g0) { dx = - dx; dy = -dy; } /* reverse sense */

do
{
last_g0 = g0;

xa += dy; ya -= dx;
x = xa; y = ya; ga = GIBBS('A');

xb -= dy; yb += dx;
x = xb; y = yb; gb = GIBBS('B');

g0 = (ga + gb) * 0.5;
}
while (g0 < last_g0);

xa -= dy; ya += dx;  /* recover last values */
xb += dy; yb -= dx;

if (ipf) { strcpy(ms, "Across"); COMPRINT(); }

}

    while (fabs(xa - lxa) > tst2 || fabs(ya - lya) > tst2 ||
         fabs(xb - lxb) > tst2 || fabs(yb - lyb) > tst2);

    if (!ipf) { strcpy(ms, ""); COMPRINT(); }
    printf("\n\rSEARCH OVER");
    time(&tme); now = localtime(&tme);
    printf("                    Time: %s\n\n\r", asctime(now));
    fprintf(fp, "SEARCH OVER");
    fprintf(fp, "                    Time: %s\n\n", asctime(now));
    fflush(fp);
    WAITFORKEY();
}
```

```c
void BINSPIN()
/* find pair of spinodal points, then cotangent pair */
{    double ga, gb;

    dex = (xb - xa) / 20; dey = (yb - ya) / 20;

    x = xa; y = ya;
    dx = dex; dy = dey;
    SPINSEARCH();
    xa = x - dx; ya = y - dy;

    x = xb; y = yb;
    dx = -dex; dy = -dey;
    SPINSEARCH();
    xb = x - dx; yb = y - dy;

    counter = 1;
    if (ipf) { strcpy(ms, "Fr.spn"); COMPRINT(); }
}

void SPINSEARCH()
/* find a spinodal point */
{    double g, oldg;

    oldg = GIBBS('A');
    x += dx; y += dy; lastg = GIBBS('A');
    x += dx; y += dy; g = GIBBS('A');

    if (g + oldg < 2 * lastg) /* search for spinodal point from inside
               the spinodal  */
    {
      x -= 2 * dx; y -= 2 * dy;
      g = oldg;
      dx = -dx; dy = -dy;

      while (g + oldg < 2 * lastg) /* find where curvature becomes > 0 */
      {
    oldg = lastg; lastg = g;
    x += dx; y += dy; g = GIBBS('A');
      }
    }
    else /* search for point from outside the spinodal */
    {
      while (g + oldg > 2 * lastg)
      {
    oldg = lastg; lastg = g;
    x += dx; y += dy; g = GIBBS('A');
      }
    }
}


                    Miscellaneous Functions

double GETVALUE(char *prompt)
/* enter a double precision value from the keyboard */
{    double x;

    fflush(stdin);
    printf(prompt); scanf("%lf", &x);
    return(x);
}

void CLS()
/* clear the screen */
```

```c
{
    printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\r");
}

/* ============================================================== */

void WAITFORKEY()

/* wait for user to press return */
{
    int ch;

    printf("\n\n\n\n\rEnter 'c' to continue...");
    do
    {
        ch = getchar();
    }
    while (ch != 'C' && ch != 'c');
}
```