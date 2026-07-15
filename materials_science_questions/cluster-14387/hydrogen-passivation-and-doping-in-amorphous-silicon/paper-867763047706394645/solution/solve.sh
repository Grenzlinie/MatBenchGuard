#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: nc_formulas_values.csv ===
_csv=/app/outputs/nc_formulas_values.csv
{
  printf 'shape,subclass,i,N_NC,N_bnd,N_IF\n'
  for i in 1 2 3 4 5 6 7; do
    # cube
    n_nc=$((8*i*i*i))
    n_bnd=$((i*((4*i-2)*(4*i-1)+1)))
    n_if=$((6*((2*i-1)*(2*i-1)+3*i-1)))
    printf 'cube,,%d,%d,%d,%d\n' $i $n_nc $n_bnd $n_if

    # octahedron
    n_nc=$(((i+1)*(4*(i+1)*(i+1)-1)/3))
    n_bnd=$((2*i*(i+1) + 4*i*(i+1)*(2*i+1)/3))
    n_if=$((4*(i+1)*(i+1)))
    printf 'octahedron,,%d,%d,%d,%d\n' $i $n_nc $n_bnd $n_if

    # dodecahedron odd
    n_nc=$((16*i*((i+1)*(24*i+9) - 8*(i+1)*(2*i+1)) + 10*(4*i+1)))
    n_bnd=$((16*i*(3*(16*i+5)*(i+1) - 16*(i+1)*(2*i+1)) + 4*(23*i+3)))
    n_if=$((128*i*(i+1) - 184*i + 112))
    printf 'dodecahedron,odd,%d,%d,%d,%d\n' $i $n_nc $n_bnd $n_if

    # dodecahedron even
    n_nc=$((16*i*((24*i+21)*(i+1) - 8*(i+1)*(2*i+1)) + 88*(i+1)))
    n_bnd=$((16*i*(3*(16*i+13)*(i+1) - 16*(i+1)*(2*i+1)) + 140*(i+1)))
    n_if=$((128*i*(i+1) - 56*i + 136))
    printf 'dodecahedron,even,%d,%d,%d,%d\n' $i $n_nc $n_bnd $n_if

    # pyramid
    n_nc=$((i*(i+1)*(2*(2*i+1)+9)/6 + i + 1))
    n_bnd=$((2*i*(i+1)*(2*i+1)/3 + i*(i+1)))
    n_if=$((4*(i+1)*(i+1)))
    printf 'pyramid,,%d,%d,%d,%d\n' $i $n_nc $n_bnd $n_if

    # tetrahedron
    n_nc=$((i*(i+1)*(2*i+1)/6 + (i+1)*(i+1)))
    n_bnd=$((i*(i+1)*(2*i+1)/3 + i*(i+1)))
    n_if=$((2*(i+1)*(i+2)))
    printf 'tetrahedron,,%d,%d,%d,%d\n' $i $n_nc $n_bnd $n_if

    # quatro_111
    n_nc=$((9*i*(2*i+1)*(2*i+1) + (2*i+1) - i*(4*i+5)*(i+1)))
    n_bnd=$((2*i*(3*i+1)*(12*i+5) - (4*i*(i+1)*(2*i+1) + 6*i*(i+1))))
    n_if=$(((6*i+2)*(6*i+2)))
    printf 'quatro_111,,%d,%d,%d,%d\n' $i $n_nc $n_bnd $n_if

    # quatro_001
    termA=$((3*(2*i+7)*(i+4)*(i+4)))
    termB=$(((2*i+7)*(i+3)*(2*i+5)))
    termC=$((6*(i+3)*((i+4)*(i+4)+i)))
    termD=$((4*(i+1)*(i+2)*(i+3)))
    numerator=$((termA + termB + termC + termD))
    n_nc=$((numerator / 3))
    term1=$((6*(i+3)*(i+3)))
    term2_num=$(((i+1)*(20*i*i + 49*i + 30)))
    term2=$((term2_num / 6))
    term3=$((7*(2*i+3)*(i+2)))
    n_bnd=$((4 * (term1 + term2 + term3)))
    n_if=$((4*(2*i+7)*(2*i+7)))
    printf 'quatro_001,,%d,%d,%d,%d\n' $i $n_nc $n_bnd $n_if
  done
} > "$_csv"
