#!/bin/bash

# Give permission before run:
# chmod +x setup.sh
# To run : ./setup.sh


GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;36m'

NC='\033[0m'

chmod +x subsync
mv subsync /usr/local/bin/
mv subsync_packages /usr/local/bin/

printf "\n ${GREEN}SUCCESS! ${NC} ${YELLOW} subsync package processed!${NC}\n"
printf "\n ${BLUE}subsync is ready to use! ${NC} :) \n\n"

