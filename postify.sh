#!/bin/bash

for i in "$@"; do
    meta="$(grep -m 1 -E '.* [[:digit:]]+.{2}, [[:digit:]]{4}, by:.*' "$i" | cut -d '*' -f 3 | sed -r 's/([[:digit:]])(th|st|rd|nd)/\1/')"
    postdate="$(echo $meta | cut -d ',' -f 1-2)"
    # february 2nd, year
    postdate="$(date -d "$postdate" '+%F')"
    author="$(echo $meta | cut -d ',' -f 3 | sed 's/ by: //')"
    # echo -e "$postdate\t$author"
    # echo -e "$postdate-$i"
    sed -i "s/author: TODO/author: $author/;6,8d" "$i"
    mv "$i" "$postdate-$i"
done
