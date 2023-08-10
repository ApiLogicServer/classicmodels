#!/bin/bash

# typically run from ?
# sh ./devops/docker-compose/docker-compose-dev-deploy.sh

# ref: https://learn.microsoft.com/en-us/azure/app-service/tutorial-multi-container-app

# login to portal

mkdir classicmodels
cd classicmodels

git clone https://github.com/Azure-Samples/multicontainerclassicmodels

cd multicontainerclassicmodels

# create container group
az group create --name myResourceGroup --location "Western US"

# create service plan
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku S1 --is-linux

# create docker compose app
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name <app-name> --multicontainer-config-type compose --multicontainer-config-file docker-compose-wordpress.yml

# browse to the app
# http://<app-name>.azurewebsites.net
