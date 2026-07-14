#!/bin/bash
# Unset proxy environment variables
unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY all_proxy ALL_PROXY
exec python3 /mnt/f/aitoptools/.hermes/scripts/scrape_tools.py
