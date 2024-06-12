from django import forms

from . models import SendFromModel, SendToModel, ServiceModel, DeliveryService, myDetailsModel, myParcelDetailsModel, UserAttrModel, usersBookingData, returnDetailsModel, deliveryDetailsModel, deliveryGuaranteeOptions

# import datetime

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = ServiceModel
        fields = ("sendFrom", "sendTo", "weight",)
        labels = {
            'sendFrom': 'Send From',
            'sendTo': 'Send To',
            'weight': 'Weight',
        }

    # sendFrom = forms.DateField( 
    #     widget=forms.DateInput(attrs={'class': 'form-control w-full py-4 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'placeholder': 'Send From',}),
    # )

    sendFrom = forms.ModelChoiceField(
        queryset=SendFromModel.objects.all(),
        # empty_label='Select Category Flight',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control w-full py-4 px-6 text-black border-2 border-gray-300 rounded-xl my-2', 'id': 'category_input'}),
        label='Send From',
        initial=3, 
    )

    sendTo = forms.ModelChoiceField(
        queryset=SendToModel.objects.all(),
        # empty_label='Select Category Flight',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control w-full py-4 px-6 text-black border-2 border-gray-300 rounded-xl my-2', 'id': 'category_input'}),
        label='Send To',
        initial=3, 
    )

    weight = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'w-full py-4 px-6 text-black border-2 border-gray-300 rounded-xl my-2', 'placeholder': 'Enter the weight', 'id': 'travelers_input'}),
        label='Weight:',
        initial=1,
        min_value=1, 
    )

    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['sendFrom'].label = 'Send From'

class DeliveryServiceForm(forms.ModelForm):
    class Meta:
        model = DeliveryService
        fields = ['name', 'speed', 'speed_unit',  'price', 'rating', 'image',]


class MyDetailsModelForm(forms.ModelForm):
    class Meta:
        model = myDetailsModel
        fields = ['user_attr', 'name', 'surname', 'email']


    user_attr = forms.ModelChoiceField(
        queryset=UserAttrModel.objects.all(),
        # empty_label='Select Category Flight this is not actulaky a gil',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control w-full py-2 px-6 text-black border-2 border-gray-300 rounded-xl my-2', 'id': 'category_input'}),
        label='Title',
        # initial=3, 
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'w-full px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors', 'placeholder': 'Name'}
        )
    )

    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'w-full px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors', 'placeholder': 'Surname'}
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'w-full px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors', 'placeholder': 'Email'}
        )
    )


class ParcelDetailsModelForm(forms.ModelForm):
    class Meta:
        model = myParcelDetailsModel
        fields = ['parcel_contents', 'length', 'height', 'width']


    parcel_contents = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'w-full px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors', 'placeholder': 'Parcel Content'}
        )
    )

    length = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'flightCost w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'placeholder': 'Length', 'id': 'length'}),
        label='Length',
        # initial=49.0,
        min_value=1, 
    )

    width = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'flightCost w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'placeholder': 'Width', 'id': 'width'}),
        label='Width',
        # initial=49.0,
        min_value=1, 
    )

    height = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'flightCost w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'placeholder': 'Height', 'id': 'height'}),
        label='Height',
        # initial=49.0,
        min_value=1, 
    )


class usersBookingDataForm(forms.ModelForm):
    class Meta:
        model = usersBookingData
        fields = ['terms_and_conditions',]
    

    def __init__(self, *args, **kwargs):
        # Access form instances passed as initial data
        form1_instance = kwargs.pop('form1', None)
        form2_instance = kwargs.pop('form2', None)

        super(usersBookingDataForm, self).__init__(*args, **kwargs)

        # Populate fields from form1 (MyDetailsModelForm)
        if form1_instance:
            self.fields['user_details_data'].initial = form1_instance.cleaned_data.get('name')

        # Populate fields from form2 (ParcelDetailsModelForm)
        if form2_instance:
            self.fields['parcels_details_data'].initial = form2_instance.cleaned_data.get('length')


class returnDetailsForm(forms.ModelForm):
    class Meta:
        model = returnDetailsModel
        fields = ['return_full_name', 'return_address', 'return_postal_code',]

    
    return_full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'w-full px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors', 'placeholder': 'Name'}
        )
    )

    return_address = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'w-full px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors', 'placeholder': 'Address'}
        )
    )

    return_postal_code = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'w-full px-3 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors', 'placeholder': 'Postal Code'}
        )
    )

class deliveryDetailsForm(forms.ModelForm):
    class Meta:
        model = deliveryDetailsModel
        fields = ['delivery_full_name', 'delivery_address', 'delivery_postal_code',]


    delivery_full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'w-full px-12 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors', 'placeholder': 'Name'}
        )
    )

    delivery_address = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'w-full px-12 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors', 'placeholder': 'Address'}
        )
    )

    delivery_postal_code = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'w-full px-12 py-2 mb-1 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors', 'placeholder': 'Postal code'}
        )
    )


class deliveryGuaranteeForm(forms.ModelForm):
    class Meta:
        model = deliveryGuaranteeOptions
        fields = ['deliver_guarantee', 'text_message',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['deliver_guarantee'].widget.attrs['class'] = 'scale-150'
        self.fields['text_message'].widget.attrs['class'] = 'scale-150'