#!/usr/bin/env bash

uwsgi --http-socket :9090 --plugin python --wsgi-file middleware.py
