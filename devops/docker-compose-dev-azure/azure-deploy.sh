#!/bin/bash

# intended for use in portal cli - not to be run on your local machine.

# modeled after: https://learn.microsoft.com/en-us/azure/app-service/tutorial-multi-container-app
# which uses: https://github.com/Azure-Samples/multicontainerwordpress

# login to portal

# To build container for your ApiLogicProject:
#    create / customize your project as you normally would
#    edit this file: change your_account/your_repository as appropriate
#    be sure to add security (already done for demo)

#    in terminal (not in VSCode docker - docker is not installed there)
#    $ cd <your project>
#    $ sh devops/docker-image/build_image.sh .

projectname="classicmodels"  # lower case, only
resourcegroup="classicmodels_rg"
dockerrepositoryname="apilogicserver"  # change this to your DockerHub Repository
githubaccount="apilogicserver"         # change this to your GitHub account
version="1.0.0"

debug() {
  debug="disabled"
  # echo "$1"
}

echo " "
if [ "$1" = "." ]; then
  debug "..using defaults"
else
  debug "using arg overrides"
  projectname="$1"
  githubaccount="$2"
  dockerrepositoryname="$3"
  resourcegroup="$4"
fi

debug "\n"
debug "Azure Deploy here, 1.0"
if [ $# -eq 0 ]; then
  echo "\nAzure Portal CLI commands to deploy project\n"
  echo " "
  echo "Prereqs"
  echo "  1. You have published your project to GitHub: https://github.com/$githubaccount/$projectname.git
  echo "  2. You have built your project image, and pushed it to DockerHub: ${dockerrepositoryname}/${projectname}"
  echo " "
  echo "  cd classicmodels"
  echo "  sh devops/docker/docker-compose-dev-azure/azure-deploy.sh [ . | args ]"
  echo "    . means use defaults:"
  echo "        ${dockerrepositoryname}/${projectname}:${version}"
  echo "    <args> = projectname githubaccount dockerrepositoryname resourcegroupname
  echo " "
  exit 0
fi

read -p "Verify settings above, then press ENTER to proceed> "

# we really only need the docker compose file
git clone https://github.com/$githubaccount/$projectname.git

cd classicmodels

# create container group
az group create --name $resourcegroup --location "westus"

# create service plan
az appservice plan create --name myAppServicePlan --resource-group $resourcegroup g --sku S1 --is-linux

# create docker compose app
az webapp create --resource-group $resourcegroup --plan myAppServicePlan --name classicmodels --multicontainer-config-type compose --multicontainer-config-file devops/docker-compose-dev-azure/docker-compose-dev-azure.yml

# enable logging: https://learn.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs#enable-application-logging-linuxcontainer

#    To enable web server logging for Windows apps in the Azure portal, navigate to your app and select App Service logs.
#    For Web server logging, select Storage to store logs on blob storage, or File System to store logs on the App Service file system.

echo "\n Completed.  Browse to the app:" 
echo "https://$projectname.azurewebsites.net"
echo " "

