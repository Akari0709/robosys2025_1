#!/bin/bash

# テスト1: 「あ → い」
out=$(echo あ | ./gojyuon)
status=$?

if [ "$out" = "い" ] && [ $status -eq 0 ]; then
    echo "test1 OK"
else
    echo "test1 NG (out='$out', status=$status)"
    exit 1
fi

# テスト2: 「ん → あ」
out=$(echo ん | ./gojyuon)
status=$?

if [ "$out" = "あ" ] && [ $status -eq 0 ]; then
    echo "test2 OK"
else
    echo "test2 NG (out='$out', status=$status)"
    exit 1
fi

# テスト3: 五十音以外
out=$(echo A | ./gojyuon)
status=$?

if [ -z "$out" ] && [ $status -eq 0 ]; then
    echo "test3 OK"
else
    echo "test3 NG (out='$out', status=$status)"
    exit 1
fi

echo "ALL OK"
exit 0
