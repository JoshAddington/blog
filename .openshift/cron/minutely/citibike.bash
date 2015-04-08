#!/bin/bash

minute=$(date +%M)
if [ $((10#$minute % 5)) -eq 0 ]; then
        echo 'hello'
        python "$OPENSHIFT_REPO_DIR"wsgi/update_bike_table.py
fi
