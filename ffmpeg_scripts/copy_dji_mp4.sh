for file in `find . -iname 'DJI_0*.mp4'`
do 
    cp --parents $file /volumeUSB1/usbshare/EU_Journey/
done