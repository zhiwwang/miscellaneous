IFS=$'\n'
for file in `find . -iname 'PRO_VID_*.mp4'`
do 
   echo $file
   cp --parents $file /volumeUSB1/usbshare/EU_Journey_360/
done