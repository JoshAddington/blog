#!/bin/bash

minute=$(date +%M)
if [ $(($minute % 5)) -eq 0 ]; then
        python "$OPENSHIFT_REPO_DIR"wsgi/update_bike_table.py
