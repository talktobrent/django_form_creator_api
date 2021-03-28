from rest_framework import serializers
import phonenumbers

from .models import *

class CommonSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['id', 'form']

    def to_representation(self, obj):
        obj_dict = super().to_representation(obj)
        obj_dict['type'] = obj._meta.object_name.lower()
        return obj_dict

class TelSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Tel

    def validate_value(self, phone):
        if not phonenumbers.is_valid_number(phonenumbers.parse(phone, None)):
            raise serializers.ValidationError("Not a phone number!")
        return phone

class RangeSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Range

    def validate(self, data):
        if data.get('min') >= data.get('max'):
            raise serializers.ValidationError("Min must be less than max!")
        return data

class SearchSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Search

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['value', 'selected', 'text']

class IntegerSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Integer

class StringSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = String

class TextSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Text

class CheckboxSerializer(CommonSerializer):
    class Meta(CommonSerializer.Meta):
        model = Checkbox

class SelectSerializer(CommonSerializer):

    option = OptionSerializer(many=True)

    class Meta(CommonSerializer.Meta):
        model = Select

    def to_representation(self, obj):
        obj_dict = super().to_representation(obj)
        obj_dict['type'] = obj._meta.object_name.lower()
        return obj_dict

    def validate_option(self, options):
        selected = False
        texts = []
        for option in options:
            if option.get('selected', None) and not selected:
                selected = True
            elif option.get('selected', None):
                raise serializers.ValidationError("Max of ONE option selection!")
            if option.get('text', None) in texts:
                raise serializers.ValidationError("Duplicate option!")
            else:
                texts.append(option.get('text'))
        return options

    def create(self, validated_data):
        options_data = validated_data.pop('option')
        select = Select.objects.create(**validated_data)
        options = []
        for option in options_data:
            options.append(Option.objects.create(select_field=select, **option))
        select.option.set(options)
        select.save()
        return select

    def update(self, instance, validated_data):
        options_data = validated_data.pop('option')
        for key, value in validated_data.items():
            setattr(instance, key, value)
        options = []
        for option in options_data:
            options.append(Option.objects.create(select_field=instance, **option))
        instance.option.set(options)
        instance.save()
        return instance

class FormSerializer(serializers.ModelSerializer):

    integer = IntegerSerializer(many=True, required=False)
    string = StringSerializer(many=True, required=False)
    text = TextSerializer(many=True, required=False)
    search = SearchSerializer(many=True, required=False)
    range = RangeSerializer(many=True, required=False)
    tel = TelSerializer(many=True, required=False)
    checkbox = CheckboxSerializer(many=True, required=False)
    select = SelectSerializer(many=True, required=False)

    class Meta:
        model = Form
        fields = 'title', 'integer', 'string', 'text', 'search', 'range', 'tel', 'checkbox', 'select'
        depth = 2

    def to_representation(self, form):
        form = super().to_representation(form)
        title = form.pop('title')
        fields = []
        for field_list in form.values():
            fields.extend(field_list)
        fields = sorted(fields, key=lambda x: x['order'])
        return {title: fields}

    def create(self, validated_data):
        title = validated_data.pop('title')
        form = Form.objects.create(title=title)
        for key, obj_list in validated_data.items():
            for obj_dict in obj_list:
                serial = eval(key.capitalize() + 'Serializer')(data=obj_dict)
                serial.is_valid(raise_exception=True)
                serial.save(form=form)
        form.save()
        return form

    def update(self, instance, validated_data):
        title = validated_data.pop('title', None)
        instance.title = title or instance.title
        for key, obj_list in validated_data.items():
            for obj_dict in obj_list:
                serial = eval(key.capitalize() + 'Serializer')(getattr(instance, key), data=obj_dict)
                serial.is_valid(raise_exception=True)
                serial.save()
        instance.save()
        return instance



