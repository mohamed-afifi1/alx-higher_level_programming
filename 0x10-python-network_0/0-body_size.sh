#!/bin/bash
# size of the body
curl -s "$1" | wc -c
