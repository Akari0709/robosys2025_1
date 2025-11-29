#!/bin/bash -xv 
#SPDX-FileCopyrightText: 2025 Akari Sunagawa
#SPDX-License-Indentifier: BSD-3-Clause
ng () {
	echo ${1}行目が違うよ
	res=1
}

res=0

out=$(seq 5 | ./sysk1.py)
[ "${out}" = 15 ] || ng "$LINENO"

[ "${res}" = 0 ] && echo OK
exit $res
