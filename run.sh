CONF=conf.ini
NETS=unlimAccessNetworks.ini
rm $CONF
rm $NETS
touch $CONF
touch $NETS

if [ $# -eq 3 ]
then
  echo NREQ=$1 > $CONF 
  echo TIME_RANGE_SEC=$2 >> $CONF 
  echo TIME_LOCK_SEC=$3 >> $CONF
else
  echo NREQ=100 > $CONF 
  echo TIME_RANGE_SEC=60 >> $CONF 
  echo TIME_LOCK_SEC=120 >> $CONF 
fi

flask run
