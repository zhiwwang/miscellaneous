find . -type d > filelist.txt
cat filelist.txt | xargs -I{} mkdir -p coverted/{}