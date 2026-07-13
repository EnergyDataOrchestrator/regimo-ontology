from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin, RecommendedSlotsPlugin

validator = Validator(
    schema="test-definition.linkML",
    validation_plugins=[
        JsonschemaValidationPlugin(closed=False),
        RecommendedSlotsPlugin()
    ]
)
json = {
   "a1": "test",
   "a2": "optional",
   "unspecified": 12
}

report = validator.validate(json, "Demo")

if not report.results:
    print('The instance is valid!')
else:
    for result in report.results:
        print(result.message)