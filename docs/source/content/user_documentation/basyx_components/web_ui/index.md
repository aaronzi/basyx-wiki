# AAS Web UI

The AAS Web UI is a vue.js 3 based web application and can be used to visualize and interact with Asset Administration Shells. It is intended to work in conjunction with the BaSyx Registry and the BaSyx AAS Environment.

```{figure} ./images/1800px-AAS_Web_UI.png
---
width: 100%
alt: AAS Web UI
name: web_ui
---
```

## Download

```{note}
:class: margin
The AAS Web UI is now only compatible with the components of BaSyx V2 and the Asset Administration Shell V3.
If you still wish to use BaSyx V1, please use the following release of the UI:

```bash
docker pull eclipsebasyx/aas-gui:v230703
```
```

The AAS Web UI can be downloaded from [Docker Hub](https://hub.docker.com/r/eclipsebasyx/aas-gui) as off-the-shelf component.
Yuo can pull it by executing the following command:

```bash
docker pull eclipsebasyx/aas-gui
```

## Quick Start

```{note}
:class: margin
Docker must be installed on your system to run the AAS Web UI.
Dockers official documentation provides a [detailed installation guide](https://docs.docker.com/get-docker/) for Windows, Mac and Linux.
```

The container for the AAS Web UI can be started by executing the following command:

```bash
docker run -p 3000:3000 --name=aas-web-ui eclipsebasyx/aas-gui
```

When the container is running, you can access the AAS Web UI by navigating to [http://localhost:3000](http://localhost:3000) in your browser.

There you will be able to connect to the BaSyx Registry and the AAS Environment (AAS Repository, Submodel Repository, Concept Description Repository) from the main menu.

```{figure} ./images/connect_to_basyx.png
---
width: 80%
alt: Connect to BaSyx Components
name: connect_basyx
---
```

## Introductory Example

You can find a complete example on how to setup a BaSyx environment with the AAS Web UI, Registry and AAS Environment in the [Quick Start](../../../introduction/quickstart) section.

## Interacting with AAS

## Features

```{toctree}
:caption: Features
:maxdepth: 1

features/statuscheck
```