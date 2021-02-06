#!/bin/bash

# Variables
CHROME_DRIVER=chromedriver_linux64.zip

echo "Downloading Chromedriver"
wget -O $CHROME_DRIVER https://chromedriver.storage.googleapis.com/88.0.4324.96/$CHROME_DRIVER
echo "Unziping driver"
unzip $CHROME_DRIVER
echo "Removing zip file"
rm $CHROME_DRIVER
echo "All done!"