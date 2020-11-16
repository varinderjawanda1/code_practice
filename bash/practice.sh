#!/bin/bash
owner=Rob
host=$(hostname -i)
PID=$(echo $$)

processVerifier () {
if [[ ${owner}=Tom ]] ;

    then echo """ Hello ${owner}, This shell is running from ${host} and process ID is : ${PID}"""
else
    echo """Owner is not Tom"""
fi
}
processVerifier