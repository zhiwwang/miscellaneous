IFS=$'\n'
for file in `find . -iname 'DJI_0*.mp4'`
do 
   echo $file
   cp --parents $file /volumeUSB1/usbshare/EU_Journey/
done