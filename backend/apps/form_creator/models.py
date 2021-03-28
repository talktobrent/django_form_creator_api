from django.db import models

# a form, which may have many fields
class Form(models.Model):
    title = models.CharField(max_length=100, primary_key=True)

# base field class
class CommonInfo(models.Model):
    name = models.CharField(max_length=100, null=False)
    required = models.BooleanField(default=False)
    order = models.IntegerField(null=False)

    class Meta:
        abstract = True

# tel input fields, each belongs to one form
class Tel(CommonInfo):
    value = models.CharField(max_length=100, null=True)
    form = models.ForeignKey(Form, related_name='tel', on_delete=models.CASCADE)
    pattern = models.CharField(max_length=100, null=True)
    placeholder = models.CharField(max_length=100, null=True)

# range input fields, each belongs to one form
class Range(CommonInfo):
    value = models.IntegerField(default=0)
    form = models.ForeignKey(Form, related_name='range', on_delete=models.CASCADE)
    min = models.IntegerField()
    max = models.IntegerField()

# integer input fields, each belongs to one form
class Integer(CommonInfo):
    value = models.IntegerField(default=0)
    form = models.ForeignKey(Form, related_name='integer', on_delete=models.CASCADE)

# checkbox fields, each belongs to one form
class Checkbox(CommonInfo):
    value = models.BooleanField(default=False)
    form = models.ForeignKey(Form, related_name='checkbox', on_delete=models.CASCADE)

# search input fields, each belongs to one form
class Search(CommonInfo):
    value = models.CharField(max_length=300, null=True)
    form = models.ForeignKey(Form, related_name='search', on_delete=models.CASCADE)
    placeholder = models.CharField(max_length=100, null=True)

# string input fields, each belongs to one form
class String(CommonInfo):
    value = models.CharField(max_length=100, null=True)
    form = models.ForeignKey(Form, related_name='string', on_delete=models.CASCADE)
    placeholder = models.CharField(max_length=100, null=True)

# textarea fields, each belongs to one form
class Text(CommonInfo):
    value = models.TextField(null=True)
    form = models.ForeignKey(Form, related_name='text', on_delete=models.CASCADE)
    placeholder = models.TextField(null=True)

# select fields, each belongs to one form
class Select(CommonInfo):
    form = models.ForeignKey(Form, related_name='select', on_delete=models.CASCADE)

# options of select fields, each belongs to one select field
class Option(models.Model):
    text = models.CharField(max_length=100)
    value = models.CharField(max_length=100, default=1)
    select_field = models.ForeignKey(Select, related_name='option', on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)



