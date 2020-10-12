# Update the server:
    $ sudo apt-get update

# Install Lampserver :

    $ sudo apt-get install lamp-server^

## Note: Above command will install apache web server, php and Mysql

# Visit default page: 

## Here copy and paste the public DNS of the instance in the address bar of the browser and click enter

# Uploading Web Pages to WWW Folder: 

## After the webserver has been installed you have to upload your web pages or project to the/var/www/html/of apache web server.

# Locate the folder using the following command
 
    $ cd /var/www/html

# Create the working directory:(change mode to 777)

    $ chmod 777 /var/www/html/

# Step 3 — (Optional) Adjusting User Authentication and Privileges

    $ sudo mysql

### Next, check which authentication method each of your MySQL user accounts use with the following command:

    SELECT user,authentication_string,plugin,host FROM mysql.user;

### In this example, you can see that the root user does in fact authenticate using the auth_socket plugin. To configure the root account to authenticate with a password, run the following ALTER USER command. Be sure to change password to a strong password of your choosing, and note that this command will change the root password you set in Step 2:

    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

### Then, run FLUSH PRIVILEGES which tells the server to reload the grant tables and put your new changes into effect:

    FLUSH PRIVILEGES;

### Check the authentication methods employed by each of your users again to confirm that root no longer authenticates using the auth_socket plugin:

    SELECT user,authentication_string,plugin,host FROM mysql.user;

### You can see in this example output that the root MySQL user now authenticates using a password. Once you confirm this on your own server, you can exit the MySQL shell:

    exit

### Alternatively, some may find that it better suits their workflow to connect to MySQL with a dedicated user. To create such a user, open up the MySQL shell once again:

    $ sudo mysql

### Note: If you have password authentication enabled for root, as described in the preceding paragraphs, you will need to use a different command to access the MySQL shell. The following will run your MySQL client with regular user privileges, and you will only gain administrator privileges within the database by authenticating:

    $ mysql -u root -p

### Following this, exit the MySQL shell:

    exit

# Testing MySQL

### Regardless of how you installed it, MySQL should have started running automatically. To test this, check its status.

    $ sudo systemctl status mysql.service

# Connecting files for the php application

    <?php
        /* Database credentials. Assuming you are running MySQL
        server with default setting (user 'root' with no password) */
        define('DB_SERVER', 'localhost');
        define('DB_USERNAME', 'admin');
        define('DB_PASSWORD', 'adminadmin');
        define('DB_NAME', 'demo');
 
        /* Attempt to connect to MySQL database */
        $mysqli = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
 
        // Check connection
        if($mysqli === false){
            die("ERROR: Could not connect. " . $mysqli->connect_error);
        }
    ?>

## Please Note, for deployment in Iaas endpoint of RDS is required in the place of local host. 



