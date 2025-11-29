#/bin/bash -xv 
#SPDX-FileCopyrightText: 2025 Akari Sunagawa
#SPDX-License-Indentifier: BSD-3-Clause

ng() {
    echo "${1}行目が違うよ"
    res=1
}

res=0

INPUT="aabccde"

echo "$INPUT" | python3 ./sysk1.py


EXPECTED=$(cat <<EOF
o 4
e 3
t 2
l 2
n 1
m 1
i 1
h 1
c 1
EOF
)

# 実際の出力を読み込み
OUTPUT=$(cat freq.txt)

# 比較
if [ "$OUTPUT" != "$EXPECTED" ]; then
    ng "$LINENO"
fi

# 結果
[ "${res}" = 0 ] && echo "OK"

exit $res
