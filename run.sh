export FLASK_APP=main.py
export FLASK_ENV=development

CONF=conf.ini
NETS=unlimAccessNetworks.ini
rHost=redisHost.ini
rm $CONF $NETS $rHost
touch $CONF $NETS $rHost 

if [ $# -eq 4 ]
then
  echo $1 > $rHost
  echo NREQ=$2 > $CONF 
  echo TIME_RANGE_SEC=$3 >> $CONF 
  echo TIME_LOCK_SEC=$4 >> $CONF
else
  echo $1 > $rHost
  echo NREQ=100 > $CONF 
  echo TIME_RANGE_SEC=60 >> $CONF 
  echo TIME_LOCK_SEC=120 >> $CONF 
fi

flask run
