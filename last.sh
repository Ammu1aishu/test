del_file()
for entry in `ls $test`
do
    echo $entry
    var=$entry
    find $var -mmin +3 -type f -delete
done
echo 'enter a value'
read val
if [ "$val" -ge "3" ]
then
    del_file
fi
