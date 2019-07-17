# Setup SMTP Email Server 

**1.** **Installing Apache2 and PHP7**

``` sudo apt-get install apache2 php ```

**2.** **Installing Postfix Mail Server**
Postfix is a mail transfer agent (MTA) which is the responsible software for delivering & receiving emails, it’s essential in order to create a complete mail server

``` sudo apt-get install postfix ```

  -Select: Internet Site
  -Insert domain: example.com

``` sudo service postfix restart ```

**3.** **Installing Dovecot**
Dovecot is a mail delivery agent (MDA), it delivers the emails from/to the mail server, to install it, run the following command.

``` sudo apt-get install dovecot-imapd dovecot-pop3d ```

``` sudo service dovecot restart ```

**4.** **Installing SquirrelMail in Ubuntu**
SquirrelMail is the email server that you’ll be using to manage emails on your server, it has a simple web interface to do the job, it can be customized by installing more modules & themes.

``` wget https://sourceforge.net/projects/squirrelmail/files/stable/1.4.22/squirrelmail-webmail-1.4.22.zip ```

    unzip squirrelmail-webmail-1.4.22.zip
    sudo mv squirrelmail-webmail-1.4.22 /var/www/html/ 
    sudo chown -R www-data:www-data /var/www/html/squirrelmail-webmail-1.4.22/ 
    sudo chmod 755 -R /var/www/html/squirrelmail-webmail-1.4.22/  
    sudo mv /var/www/html/squirrelmail-webmail-1.4.22/ /var/www/html/mail

``` sudo perl /var/www/html/mail/config/conf.pl ```

Follow the next options:

    -Option 2: Server Settings
    -Option 1: Domain
    -Go back: R
    -Option 4: General Options
    -Option 11: Allow server-side sorting
    -Click y
    -Go back: R
    -Save: S
    -Quit: Q

**5.** **Creating Mail Users**

``` sudo useradd myusername ```

``` sudo passwd myusername ```

``` sudo mkdir -p /var/www/html/myusername ```

``` sudo usermod -m -d /var/www/html/myusername myusername ```

``` sudo chown -R myusername:myusername /var/www/html/myusername ```

``` sudo mkdir -p /var/www/html/myusername ```

``` sudo usermod -m -d /var/www/html/myusername myusername ```

    sudo mkdir -p /var/local/squirrelmail/data
    sudo mkdir -p /var/local/squirrelmail/attach
    sudo mkdir -p /var/local/squirrelmail/mail
    sudo chown -R www-data:www-data /var/local/squirrelmail/data
    sudo chown -R www-data:www-data /var/local/squirrelmail/attach
    sudo chown -R www-data:www-data /var/local/squirrelmail/mail
    sudo chmod 777 /var/mail/

**6.** **Error Log**

``` tail -F /var/log/mail.err ```

## References
https://www.tecmint.com/setup-postfix-mail-server-in-ubuntu-debian/

