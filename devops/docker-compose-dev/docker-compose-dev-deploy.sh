#!/bin/bash

# these are just notes for copy/paste into portal - not to be run as script.

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
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name classicmodels --multicontainer-config-type compose --multicontainer-config-file devops/docker-compose-dev/docker-compose-dev.yml

az container show --resource-group myResourceGroup --name <container name> 
az container list -g myResourceGroup # is empty

# browse to the app (failed - :( Application Error)
# https://classicmodels.azurewebsites.net