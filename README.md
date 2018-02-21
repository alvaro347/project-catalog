***Project: Linux Server***

information:

1. IP adress: 35.177.44.39

2. URL: http://ec2-35-177-44-39.eu-west-2.compute.amazonaws.com

3. Software installed:

  - Apache2
  - WGSI library
  - Flask
  - Postgrsql
  - Finger
  - Requests
  - virtualenve
  - psycopg2
  - oauth2client
  - Sqlalchemy

4. Summery of configurations:

  - Configure firewall to be opened for ports 2200, 80 and 123.
  - Add port 2200 for SSH connection.
  - Add user 'grader' with password
  - Generate and store SSH key in /.ssh/linuxserverproject and add passprahre
  - Allow SSH connections only
  - Create and configure 'project-catalog.conf' from 'sites-enabled'
  - Create git repository and clone it inside /var/www/ as 'project-catalog'
  - Create and configure 'project-catalog.wsgi'
  - Create Postgrsql user
  - Implement
  - Add write permission to 'static' folder for uploads

5. Third party resources to complete this project:

  - Udacity Forum
  - StackOverflow
  - Flask documentation
  - Google APIs
  - Amazon LightSail
  - Github
  - Digitalocean.com
  - Sqlalchemy documentation
