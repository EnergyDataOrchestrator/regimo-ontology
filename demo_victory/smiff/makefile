default: generated/metadata_analysis_01.json

generated/RDMO-definition.linkML: 
	@echo "create linkml class definition"
	php rdmo2linkML-definition.php "../01_Data Capture (RDMO)/metadata_analysis_01.json" > generated/RDMO-definition.linkML

generated/metadata_analysis_01.yaml: generated/RDMO-definition.linkML
	@echo "transform RDMO output to previously linkml class format"
	php rdmo2yaml.php "../01_Data Capture (RDMO)/metadata_analysis_01.json" > generated/metadata_analysis_01.yaml
	@echo "validate generated RDMO datafile against creted linkml schema"
	linkml-validate  -s generated/RDMO-definition.linkML generated/metadata_analysis_01.yaml

generated/metadata_analysis_01.json: generated/RDMO-definition.linkML generated/metadata_analysis_01.yaml
	@echo "transform RDMO data file from yaml format into json format"
	linkml-convert -s generated/RDMO-definition.linkML generated/metadata_analysis_01.yaml -t json > generated/metadata_analysis_01.json
	ls generated/metadata_analysis_01.json

clean:
	rm -f generated/*
