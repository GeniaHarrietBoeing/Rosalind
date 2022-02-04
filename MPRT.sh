#!/bin/bash

input="Data/rosalind_mprt.txt"
data_dir="Data/Uniprot"
mkdir $data_dir


url="https://www.uniprot.org/uniprot/"
filetype=".fasta"
while IFS= read -r line
do 
    wget -P Data/Uniprot "$url$line$filetype"
    echo "$url$line$filetype"
done <"$input"

python3 MPRT.py $input $data_dir
