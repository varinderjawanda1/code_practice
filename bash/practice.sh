#!/bin/bash
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