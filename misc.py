#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Encoding: UTF-8

import os, configparser

config = configparser.ConfigParser()  # define config file
config.read("%s/config.ini" % os.path.dirname(os.path.realpath(__file__)))  # read config file

videoTypes = (config.get('video', 'videoTypes')).split(',')  # allowed file types