#!/usr/bin/env python3
#SPDX-FileCopyrightText: 2025 Akari Sunagawa
#SPDX-License-Indentifier: BSD-3-Clause

gojuon = [
    'あ','い','う','え','お',
    'か','き','く','け','こ',
    'さ','し','す','せ','そ',
    'た','ち','つ','て','と',
    'な','に','ぬ','ね','の',
    'は','ひ','ふ','へ','ほ',
    'ま','み','む','め','も',
    'や','ゆ','よ',
    'ら','り','る','れ','ろ',
    'わ','を','ん'
]

# 入力ループ
while True:
    try:
        char = input("文字を入力してください（終了は Ctrl+C）: ").strip()
        if char == "":
            continue
        if char not in gojuon:
            print("五十音以外です")
            continue
        idx = gojuon.index(char)
        next_idx = (idx + 1) % len(gojuon)
        print(gojuon[next_idx])
    except KeyboardInterrupt:
        print("\n終了します")
        break
