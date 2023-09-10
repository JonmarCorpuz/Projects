# Project Context

As part of the continued development of its architecture, the IT department of Collège de Rosemont would like to improve the services provided by its IT asset management software (GLPI).

Our mandate for this project iwas to carry out an analysis of the needs and the impact of adding the different functionalities that were requested.

Depending on the result of the analysis, you will be called upon to configure a GLPI server in a test environment (your own environment) in such a way as to meet the needs of the department, represented by Bertrand Xayasane ("Project Owners").

To complete this project, we used the SCRUM project management approach.

# Project Objectives

## Documentation Objectives

- Create a **project charter**
- Create a **product backlog**
- Provide the **SCRUM master schedule** from the start of the project to the end of the project

## Product Objectives

- The software should be able to inventory at minimum the following elements:
  -  All types of network equipment in the IT department using the SNMP (Simple Network Management Protocol) protocol
  -  All type 1 hypervisors using GLPI
  -  All Windows and Linux computers using agents in client-server relationship mode
 
- A ticketing system that resembles a service catalog that has a functional email notification system

- An equipment reservation system

- Integrated APIs

# Project Procedures

## Installing GLPI

```Bash
#!/bin/bash

# Step 1: Update Ubuntu 
sudo apt update

# Step 2: Upgrade the installed packages 
sudo apt -y upgrade

# Step 3: Downloaded the 
sudo apt-get -y install wget curl

# Step 4:
sudo apt install mousepad

# Step 5: Install MariaDB  
sudo apt install mariadb-server

# Step 6:
sudo mysql_secure_installation

# Step 7: Create a database and user for GLPI
sudo mysql -u root -p
CREATE DATABASE glpi;
CREATE USER 'user'@'localhost' IDENTIFIED BY 'crosemont';
GRANT ALL PRIVILEGES ON glpi.* TO 'user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# Step 8: Install PHP 
sudo apt -y install php php-{curl,zip,bz2,gd,imagick,intl,apcu,memcache,imap,mysql,cas,ldap,tidy,pear,xmlrpc,pspell,mbstring,json,iconv,xml,gd,xsl}

# Step 9: Install Apache2
sudo apt -y install apache2 libapache2-mod-php

# Step 10:
sudo mousepad /etc/php/*/apache2/php.ini
session.cookie_httponly = on

# Step 11: 
VER=$(curl -s https://api.github.com/repos/glpi-project/glpi/releases/latest|grep tag_name|cut -d '"' -f 4)
wget https://github.com/glpi-project/glpi/releases/download/$VER/glpi-$VER.tgz

# Step 12: Uncompress the downloaded archive
tar xvf glpi-$VER.tgz

# Step 13: Move the created GLPI folder to the /var/www/html directory
sudo mv glpi /var/www/html/

# Step 14: Give the Apach user ownership of the directory
sudo chown -R www-data:www-data /var/www/html/

# Step 15: 
ifconfig
firefox "<IP>/glpi"
```

## Configuring Our DNS Server

# Sources

## Installing GLPI

- https://computingforgeeks.com/how-to-install-glpi-on-ubuntu-linux/?expand_article=1
- https://www.youtube.com/watch?v=oU1ZJ5uHTkw
- https://glpi-project.org/

## DNS Server Configuration

- https://ubuntu.com/server/docs/service-domain-name-service-dns

## Active Directory (AD) Implementation

- https://rdr-it.com/en/glpi-link-with-an-active-directory/
- https://glpi-install.readthedocs.io/en/latest/command-line.html#ldap-synchonization
- https://glpi-user-documentation.readthedocs.io/fr/latest/modules/configuration/authentication/ldap.html
