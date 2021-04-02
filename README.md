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
    'test_title': 
        [
            {"type": "integer", "name": "test_int", "value": 6},
            {"type": "string", "name": "test_str", "placeholder": "put text here", "required": true},
            {"type": "text", "name": "test_text"},
            {"type": "tel", "name": "test_tel", "value": "800-000-000", "required": true},
            {"type": "range", "name": "test_range", "min": 5, "max": 10},
            {"type": "search", "name": "test_search", "placeholder": "Search here"},
            {"type": "checkbox", "name": "test_checkbox", "value": False},
            {
                "type": "select",
                "name": "test_select",
                "option": 
                    [
                        {"text": "test_option_1", "value": 1, "selected": false},
                        {"text": "test_option_2", "value": 2}
                    ]
             }
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
- `pip install phonenumbers`

