#!/bin/sh
set -e

echo "--- Debugging Entrypoint ---"
echo "API_URL is: '${API_URL}'"

if [ -z "${API_URL}" ]; then
  echo "Error: API_URL environment variable is not set." >&2
  exit 1
fi

# Use sed to replace the placeholder with the environment variable
# The delimiter for sed is changed to '|' to avoid conflicts with '/' in the URL
sed -i "s|__API_URL__|${API_URL}|g" /etc/nginx/conf.d/default.conf

echo "--- Nginx Conf After Substitution ---"
cat /etc/nginx/conf.d/default.conf
echo "-------------------------------------"

# Execute the original Nginx command
exec nginx -g 'daemon off;'