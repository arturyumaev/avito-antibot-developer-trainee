if [ $# -eq 1 ]
then
  echo $1 >> unlimAccessNetworks.ini
  echo "Success!"
else
  echo "Something went wrong"
fi