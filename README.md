Brent Janski - Form Creator API
========

- The idea is to store html forms and their inputs for easy JSON representation
- Use with a front end to create custom form templates to be used for any reason
- forms can have fully filled default values or be empty templates
- values can be specified as required

Work primarily done on models, serializers, api views, and validation

## An example json form:
```buildoutcfg
{
    "formtitle":
        [
            {"type": "integer", "name":"my int", "value": 0},
            {"type": "range", "name":"my range", "min":0, "max":5, "value":2},
            {"type": "select", "name":"my select",
                "option": [
                    {"value":4, "text":"my option", "selected":true},
                    {"value":5, "text":"five"}
                ]
            },
            {"type":"string", "name":"my string", "placeholder":"write here"}
        ]
}
```
- The top level key is the form title, and the top level value in the list of fields, in the order that they should appear in a UI
- field types correspond to model tables, and attributes correspond to columns

## POST `/api/form/`
- A json which represents the desired new form entry

## GET `/api/form/<title>`
+ view a json of an existing form

## DELETE `/api/form/<title>`
+ delete an existing form entry

## PUT `/api/form/`
- A json which will update an existing form to the submitted json


### requires:
postgres db exists: `lofty`
`pip install phonenumbers`

