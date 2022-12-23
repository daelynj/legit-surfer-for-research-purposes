#!/usr/bin/env bash

diff $1 $2 | grep '^<' > search_terms.txt
sed -i 's/^< //' search_terms.txt
