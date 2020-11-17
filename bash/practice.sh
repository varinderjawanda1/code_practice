#!/bin/bash
# URL to spin online linux server for practice
# https://cocalc.com/projects/54203051-a3aa-4187-a482-afaf46f348fb/files/Welcome%20to%20CoCalc.term?session=default
#
x=Tom
host=$(hostname -i)
PID=$(echo $$)

# processVerifier function verifies user and return process information

processVerifier () {

if [ $x = "Tom" ] ; then
    echo """ Hello ${x}, This shell is running from ${host} and process ID is : ${PID}"""

else
    echo """Owner is not Tom"""

fi
}
processVerifier