# BaSyx Architecture

## Digital Twins with Asset Administration Shells

````{sidebar}
![](./images/digital-twins_with_aaset-administration-shell.png)
````

Eclipse BaSyx uses the Asset Administration Shell (AAS) as base technology for digital twins. The AAS is the digital identity of an asset and links to AAS submodels that provide asset specific information, simulation models, and services. Eclipse BaSyx supports three kinds of submodels. The same AAS may link to any number of each kind:

- Static submodels provide access to data that only changes seldomly, such as documents, electronic certificates, data sheets, and digital nameplates. Static submodel data may be serialized into files and sent to suppliers or customers, for example when the physical asset is sold or received. Static submodels are created for example with the AASX package explorer and saved as files.
- Dynamic submodels enable unified access to live asset data. This kind of submodel represents for example raw data, i.e. the state of a device, or higher-level data, such as the location of a product in the process. Dynamic submodels also support behavior (using program code) that implements data preprocessing and analysis. Dynamic submodels are created with the Eclipse BaSyx Software Development Kits (SDKs.)
- Control component submodels enable unified access to asset operation modes, services, and capabilities. They are one foundation for the service-oriented architecture of Eclipse BaSyx.

