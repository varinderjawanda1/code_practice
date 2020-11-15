#!/bin/bash
owner=Tom
host="hostname -i"
PID="ps -ef |grep bash"
echo """ Hello ${owner}, This shell is running from ${host} and process ID is : ${PID}"""
