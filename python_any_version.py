a
n 2.7.10
#Make sure you aren't already in a VM if you aren't sure
deactivate
#The following steps create a hidden directory from your root
 
cd ~/
mkdir .localpython
cd ~/.localpython
#Download the Python 2.7.10 installation package from python.org into the newly created .localpython directory
wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
tar -xvzf Python-2.7.10.tgz
#In case required later, increase scope of permissions for the .localpython directory
chmod -R +x ~/.localpython
#Install Python 2.7.10 into the .localpython directory
cd Python-2.7.10
./configure --prefix=$HOME/.localpython
make
make install
 
#Installing the latest Virtualenv
#Make a directory for installation files for apps
cd ~/
mkdir src
cd ~/src
#Download the Virtualenv installation package from https://pypi.python.org/pypi/virtualenv/15.0.2
wget https://pypi.python.org/packages/5c/79/5dae7494b9f5ed061cff9a8ab8d6e1f02db352f3facf907d9eb614fb80e9/virtualenv-15.0.2.tar.gz#md5=0ed59863994daf1292827ffdbba80a63
tar -xzf virtualenv-15.0.2.tar.gz
cd virtualenv-15.0.2/
#Install Virtualenv using Python 2.7.10 by pointing to which Python interpreter to be used
~/.localpython/bin/python setup.py install
#Create a VM that uses Python 2.7.10
cd ~/
virtualenv env2710 -p $HOME/.localpython/bin/python2.7
source env2710/bin/activate
#Check that everything worked properly and that the VM you just created is indeed in Python 2.7.10
which python
#Result should be...
/home/yourusername/env2710/bin/python
. env2710/bin/activate
python --version
#Result should be...
Python 2.7.10
 
#(OPTIONAL) Let's set up .bashrc and .pip/pip.conf to ensure that when we install pip packages we install them inside/outside the VM
#Files to be created/updated:
      .bashrc
      .pip/pip.conf
 
#Start from your root directory
cd ~/
cd .pip
#If the above command yields an error, create the directory with the below command
mkdir .pip
ls
#If you don't see a pip.conf, use the below command to create the file
touch pip.conf
vi pip.conf
 
#Add the following lines into the ~/.pip/pip.conf file:
[global]
require-virtualenv = true
 
ESC
:wq
 
#The above lines make it such that you will get an error whenever you try to install a pip package when a VM is not activated
 
#After saving the changes you will need to source your changed file
source pip.conf
 
#You will of course need to install some packages globally (usually ones that you use across different projects consistently) and this can be accomplished by adding the following to your ~/.bashrc file:
 
cd ~/
vi .bashrc
#If the above command yields an error indicating that the .bashrc file does not exist, simply create it
touch .bashrc
vi .bashrc
 
#Add the following lines into the ~/.bashrc file:
#Functions
gpip () {
    PIP_REQUIRE_VIRTUALENV="" pip "$@"
}
 
ESC
:wq
 
#After saving the changes you will need to source your changed file
source .bashrc
 
#Once you source your ~/.bashrc file you can now install packages globally by running gpip install. You can change the name of the function to anything you like, just keep in mind that you will have to use that name when trying to install packages globally with pip
 
#Now to make sure that you have an up-to-date version of pip for installing packages
pip --version
#The below result indicates that pip is out of date and won't work (pip 1.1 specifically)
pip 1.1 from /home/yourusername/env2710/lib/python2.7/site-packages/pip-1.1-py2.7.egg (python 2.7)
 
#If you don't have a newer version of pip, you will need to remove the obsolete pip files and get an updated version of pip
#Running pip install commands with pip 1.1 will yield errors saying that the module does not exist, etc.
 
#First we need to remove obsolete pip-1.1 files
cd ~/env2710/lib/python2.7/site-packages/
rm -rf pip-1.1-py2.7.egg
rm -rf distribute-0.6.24-py2.7.egg
 
cd ~/env2710
rm -rf build
 
#Now we can install a newer version of pip
cd ~/
easy_install pip==9.0.1
#Check the version again
pip --version
pip 9.0.1 from /home/myamaguchi/env2710/lib/python2.7/site-packages/pip-9.0.1-py2.7.egg (python 2.7)
 
#Final check that you have the correct pip and python versions and locations
which pip
/home/yourusername/env2710/bin/pip
which python
/home/yourusername/env2710/bin/python
pip --version
pip 9.0.1 from /home/yourusername/env2710/lib/python2.7/site-packages/pip-9.0.1-py2.7.egg (python 2.7)
python --version
Python 2.7.10
 
#If all of the above is what you get, you're ready to install the pip packages
 
#The crontab repository in Bitbucket contains the latest requirements in requirements.txt
cd ~/crontab
cd ~/crontab
git pull origin master
#If the above commands yield errors, use the commands below to clone the crontab repository
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
(Enter your password)
git clone ssh://git@source.fitbit.com/ca/crontab.git
cd ~/crontab
pip install -r requirements.txt
 
#Check that all the pips installed with the command below
pip freeze
 
#USE BELOW IF PIP INSTALLS MISSING
pip install --index=https://artifacts.site-ops.fitbit.com/artifactory/api/pypi/pypi-virtual/simple fitbit-snowflake-connector
pip install --upgrade snowflake-connector-python
pip install -U pyasn1==0.2.3 pyasn1-modules==0.0.9
pip install fitbit-snowflake-connector
