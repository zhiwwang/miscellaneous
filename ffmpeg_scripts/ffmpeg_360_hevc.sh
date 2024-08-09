IFS=$'\n'
for f in `find . -iname '*.mp4'`
do 
    echo "$f"
    ffmpeg6 -c:v h264_qsv -i "$f" -movflags use_metadata_tags -map_metadata 0 -c:v hevc_qsv -b:v 20000k -c:a copy -c:s copy -preset veryslow "coverted/$f"
done