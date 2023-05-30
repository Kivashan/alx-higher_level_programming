#!/bin/bash
echo "Enter filename"
read file_name
touch $file_name
sed -i.bak 's/"\t"/"    "/g' $file_name
