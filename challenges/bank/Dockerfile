FROM php:7.4-apache

# Install the mysqli extension
RUN docker-php-ext-install mysqli

# Copy the PHP code to the container
COPY login.php /var/www/html/

# Set the working directory to the web server root
WORKDIR /var/www/html

# Expose port 80 for web traffic
EXPOSE 80
