from django import forms
from django.contrib.auth.forms import UserCreationForm

STOR_TYPE=(
    ('N','Stor type'),
    ('S','Starter'),
    ('B','Basic'),
    ('P','Premium'),
    ('A','Anchor'),
    ('E','Enterprise'),
)
LISTING_TYPE=(
    ('F','Fixed Price'),
    ('A','Auction '),
)
PRODUCTS_TYPE=(
    ('AL','All others categories')  ,
    ('BM','Books, DBDs & Movies, Music') , # 12% (maximum fee $750)
    ('CF','Camera & Photo Accessories, Cell Phone Accessories and more') ,
    ('CS','Clothings, Shoes & Accessories') ,
    ('CP','Coins & Paper Money, Stamps') ,
    ('CA','Collectibles , Art Pottery & Glass, and Antiques' ),
    ('CT','Computers/Tablets, Cameras & Photo and more') ,
    ('MP','Motors Parts & Accessoties') ,
    ('MI','Musical Instruments & Gear') , 
    ('GB','Guitars & Basses') , #3.5% (maximum fee $350)
    ('HE','Heavy Equipments, Commercial Printings Presses, Foof Trucks, Trailers & carts '), #2% + 20 (maximum fee $300)
    )
PAYPAL_RATE=(
    ('DM','Domestic | 2.9% + $0.30'), # 2.9 + 0.3
    ('IN','International | 4.4% + $0.30'), # 4.4 + 0.3
    ('NP','None profit | 2.2% + $0.30'), # 2.2 + 0.3
    ('MP','Micropayment | 5% + $5'), # 5 + 0.05

)
class mainFieldsForm(forms.Form):
    net_profit = forms.FloatField(required=False, widget=forms.NumberInput(attrs={
        'class':'input',
        'placeholder':'HM profit you want'
    }))
    listing_type = forms.ChoiceField( choices=LISTING_TYPE  ,initial='F', widget=forms.RadioSelect(attrs={
          'class':'form-check-input',          
    }))
    top_rated = forms.BooleanField(required=False)
    buying_cost= forms.FloatField(widget=forms.NumberInput(attrs={
        'class':'input',
        'placeholder':'Product cost'
    }))
    silling_price = forms.FloatField( widget=forms.NumberInput(attrs={
        'class':'input',
        'placeholder':'Product price'
    }))
    quantity = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class':'input',
        'placeholder':'Quantity'
    }))
    Shipping_cost = forms.FloatField(required=False, widget=forms.NumberInput(attrs={
        'class':'input',
        'placeholder':'Shipping cost'
    }))
    Shipping_price = forms.FloatField(required=False, widget=forms.NumberInput(attrs={
        'class':'input',
        'placeholder':'Shipping price'
    }))
    stor_type = forms.ChoiceField( choices=STOR_TYPE, required=False ,widget=forms.Select(attrs={'class': 'custom-select d-block w-100 mt-3',}))
    product_category = forms.ChoiceField( choices=PRODUCTS_TYPE, required=False ,widget=forms.Select(attrs={'class': 'custom-select d-block w-100 mt-3',}))
    Paypal_rate = forms.ChoiceField(choices=PAYPAL_RATE, required=False ,widget=forms.Select(attrs={'class': 'custom-select d-block w-100 ',}))

class signup_form(UserCreationForm):
 
    fields = ['username','email','password1','password2']

class login_form(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)