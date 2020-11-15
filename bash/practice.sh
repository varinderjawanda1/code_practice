#!/bin/bash
owner=Tom
host=$(hostname -i)
PID=$(echo $$)
echo """ Hello ${owner}, This shell is running from ${host} and process ID is : ${PID}"""

file_organizer ()
{
pwd && ls -lrt
fileName=$(ls -lrt |test.txt)
If ${fileName}==test.txt
  then chmod 777 ${fileName} && ls -lrt
 else echo """ text.txt doesn't exit"""
}
file_organizer ()

