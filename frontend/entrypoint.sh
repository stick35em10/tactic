#!/bin/sh
set -e

# Use sed to replace the placeholder with the environment variable
sed -i "s|__API_URL__|${API_URL}|g" /etc/nginx/conf.d/default.conf

# Execute the original Nginx command
exec nginx -g 'daemon off;'
