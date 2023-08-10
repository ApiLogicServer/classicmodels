#!/bin/bash

# typically run from ?
# sh ./devops/docker-compose/docker-compose-dev-deploy.sh

# ref: https://learn.microsoft.com/en-us/azure/app-service/tutorial-multi-container-app
# eg: https://github.com/Azure-Samples/multicontainerwordpress

# login to portal

mkdir classicmodels
cd classicmodels

git clone https://github.com/ApiLogicServer/classicmodels.git

cd classicmodels

# create container group
az group create --name myResourceGroup --location "westus"

# create service plan
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku S1 --is-linux

# create docker compose app
# pg ref:
az container create --resource-group <resource group name> \
   --name <container name> \
   --image <docker hub registry name>/<repository name>:<version> \
   --dns-name-label <container name> \
   --ports 5656 5002 \
   --environment-variables SECURITY_ENABLED=True PYTHONPATH=/app/ApiLogicProject APILOGICPROJECT_SQLALCHEMY_DATABASE_URI=postgresql://postgres:p@postgresql-container.centralus.azurecontainer.io:5432/postgres APILOGICPROJECT_SQLALCHEMY_DATABASE_URI_AUTHENTICATION=postgresql://postgres:p@postgresql-container.centralus.azurecontainer.io:5432/authdb APILOGICPROJECT_SECURITY_ENABLED=True
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name classicmodels --multicontainer-config-type compose --multicontainer-config-file devops/docker-compose-dev/docker-compose-dev.yml

az container show --resource-group myResourceGroup --name <container name> 
az container list -g myResourceGroup # is empty

# browse to the app (failed - :( Application Error)
# https://classicmodels.azurewebsites.net