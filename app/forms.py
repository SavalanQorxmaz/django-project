from django import forms
from .models import Logo,Slider,Contacts,Photos
import base64


class BinaryFileInput(forms.ClearableFileInput):

    def is_initial(self, value):
        """
        Return whether value is considered to be initial value.
        """
        return bool(value)

    def format_value(self, value):
        """Format the size of the value in the db.

        We can't render it's name or url, but we'd like to give some information
        as to wether this file is not empty/corrupt.
        """
        if self.is_initial(value):
            return f'{len(value)} bytes'


    def value_from_datadict(self, data, files, name):
        """Return the file contents so they can be put in the db."""
        upload = super().value_from_datadict(data, files, name)
        if upload:
            return upload.read()  
        


class LogoForm(forms.ModelForm):
    logoImage = forms.ImageField(required=True)
    
    model = Logo
    temporaryData = b''
    class Meta:
        fields = [
            'logo_title'
        ]

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            
            self.temporaryData =  instance.logo 
        super().__init__(*args, **kwargs )
    def save(self, commit=True):
        if self.cleaned_data.get('logoImage') is not None:
            
            data = self.cleaned_data['logoImage'].file.read()
            if base64.b64encode(data) != self.temporaryData:
                self.instance.logo = data
        else: self.instance.logo = self.temporaryData
        self.temporaryData = b''
        return self.instance

    def save_m2m(self):
        # FIXME: this function is required by ModelAdmin, otherwise save process will fail
        pass

class SliderForm(forms.ModelForm):
    slideImage = forms.ImageField(required=True)
    
    model = Slider
    temporaryData = b''
    class Meta:
        fields = [
        ]

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        
        if instance:
            
            self.temporaryData =  instance.slide
          
        super().__init__(*args, **kwargs )
   

    def save(self, commit=True):
        if self.cleaned_data.get('slideImage') is not None:
            
            data = self.cleaned_data['slideImage'].file.read()
            if base64.b64encode(data) != self.temporaryData:
                self.instance.slide = data
        else: self.instance.slide = self.temporaryData
        self.temporaryData = b''
        return self.instance

    def save_m2m(self):
        # FIXME: this function is required by ModelAdmin, otherwise save process will fail
        pass
   

class ContactForm(forms.ModelForm):
    contactImage = forms.ImageField(required=True)
    
    model = Contacts
    temporaryData = b''
    class Meta:
        fields = [
            'contact_title',
            'contact_link'
        ]

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        
        if instance:
            
            self.temporaryData =  instance.contact_logo
          
        super().__init__(*args, **kwargs )
   

    def save(self, commit=True):
        if self.cleaned_data.get('contactImage') is not None:
            
            data = self.cleaned_data['contactImage'].file.read()
            if base64.b64encode(data) != self.temporaryData:
                self.instance.contact_logo = data
        else: self.instance.contact_logo = self.temporaryData
        self.temporaryData = b''
        return self.instance

    def save_m2m(self):
        # FIXME: this function is required by ModelAdmin, otherwise save process will fail
        pass
   
    
class PhotoForm(forms.ModelForm):
    photoField = forms.ImageField(required=True)

    model = Photos
    temporaryData = b''
    class Meta:
        fields = [
            'photo_name',
            'project'
        ]

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        initial = {}
        
        if instance:
            
            self.temporaryData =  instance.photo
        super().__init__(*args, **kwargs )
        
    def save(self, commit=True):
        if self.cleaned_data.get('photoField') is not None:
            
            data = self.cleaned_data['photoField'].file.read()
            # print('data:  ',base64.b64encode(data))
            if base64.b64encode(data) != self.temporaryData:
                self.instance.photo = data
        else: self.instance.photo = self.temporaryData
        self.temporaryData = b''
        return self.instance       
            

    

    def save_m2m(self):
        # FIXME: this function is required by ModelAdmin, otherwise save process will fail
        pass
 
