#!/usr/bin/env python3
#SPDX-FileCopyrightText: 2025 Akari Sunagawa
#SPDX-License-Indentifier: BSD-3-Clause

import sys
import string
from collections import Counter
import subprocess

def main():
    print("文字を入力してください（Ctrl+D で終了）：")

    # 標準入力から全文読み込み
    try:
        text = sys.stdin.read()
    except KeyboardInterrupt:
        return 0

    # アルファベットのみカウント
    freq = Counter(ch.lower() for ch in text if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'))

    # freq.txt に書き出し
    try:
        with open("freq.txt", "w", encoding="utf-8") as fout:
            for ch in string.ascii_lowercase:  # a～z
                if freq[ch] > 0:
                    fout.write(f"{ch} {freq[ch]}\n")
    except OSError:
        print("出力ファイルを開けません")
        return 1

    print("\n文字頻度を freq.txt に出力しました。")
    print("頻度の高い上位26件を表示します：\n")

    # sort と head を使う（Cと同じ）
    try:
        result = subprocess.run(
            "sort -k2 -nr freq.txt | head -n 26",
            shell=True, text=True, capture_output=True
        )
        print(result.stdout)
    except Exception as e:
        print("sort / head 実行時にエラー:", e)

    return 0

if __name__ == "__main__":
    sys.exit(main())
