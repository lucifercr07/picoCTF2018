#!/bin/bash

strings myname.pcap | grep -oE "picoCTF{.*}" --color=none
