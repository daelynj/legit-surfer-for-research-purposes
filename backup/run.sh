#!/usr/bin/env bash

sudo mkdir /mnt/z
sudo mount -t drvfs Z: /mnt/z

./create_backup.sh backups/$(date +%F_%T).txt
