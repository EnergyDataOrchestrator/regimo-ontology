# Integration of linkml to EDO

These scripts demonstrate, how the output of RDMO (json list) can be used to generate a Linkml class definition and transform the 
RDMO json output to a yaml file, conform to the generated linkML class definition.


## Requirements:

php interpreter (no special modules needed)

## Generation of a linkML definition file 

The script takes all ``question`` properties from the [../01_Data\ Capture \(RDMO\)/metadata_analysis_01.json](https://github.com/EnergyDataOrchestrator/regimo-ontology/blob/demo-victory/demo_victory/01_Data%20Capture%20(RDMO)/metadata_analysis_01.json) 
file and makes linkml attributes out of them. Additionally it adds the header information from [rdmo_header.linkML](templates/rdmo_header.linkML) to the output (at the beginning).

To build linkml properties out of the questions, we do a number of transformtions:
- replace one or more consequtive spaces with a single underline character  (_).
- remove everthing after the first questionmark (?). The rest of the query is explanation on how to answer the question, so we can ignore it.
- remove everything that is not inside A-Z, a-z, 0-9, _
- transform to lowercase characters

```` 
php rdmo2linkML-definition.php "../01_Data Capture (RDMO)/metadata_analysis_01.json" > RDMO-definition.linkML
````

## Generation of a yaml file, containing the same information as ``../01_Data Capture (RDMO)/metadata_analysis_01.json``. 

The script catches all ``question`` and ``values`` properties from the [metadata_analysis_01.json](https://github.com/EnergyDataOrchestrator/regimo-ontology/blob/demo-victory/demo_victory/01_Data%20Capture%20(RDMO)/metadata_analysis_01.json) file, 
and builds a yaml file from this information (properties are handled as described above).

````
php rdmo2yaml.php "../01_Data Capture (RDMO)/metadata_analysis_01.json" > metadata_analysis_01.yaml
````

## Check that ``metadata_analysis_01.yaml`` conforms to ``RDMO-definition.linkML``.

````
linkml-validate  -s RDMO-definition.linkML metadata_analysis_01.yaml
````

At this point we have a yaml version of the json regimo output, as well as a linkml class definition file, describing the yaml  version of the regimo output.

## Next steps:

Develop a linkml description of the target format (internal EDO format). After that, linkml-map transformation can be applied to transform the generated yaml file to EDO's 
internal representation.

Additionally a linkml class defintion must be created for SMS  as well as for the knowledge graph, which both act as an input to EDO and must also be 
transformed to the internal EDO format (see above) using linkml.



