#!/bin/bash

exit(1)

DISK_NUM = $1

diskutil list

diskutil unmountDisk /dev/disk$DISK_NUM

sudo dd bs=1m if=image.img of=/dev/rdisk$DISK_NUM conv=sync

