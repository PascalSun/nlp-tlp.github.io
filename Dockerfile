# Use a lightweight base image
FROM nginx:alpine

# TODO: Install eleventy and build site

# Copy the static website files to the Nginx document root
COPY _site/ /usr/share/nginx/html