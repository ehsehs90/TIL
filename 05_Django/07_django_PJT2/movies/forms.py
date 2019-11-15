from django import forms
from .models import Movie

# class UploadFileForm(forms.ModelForm):
#     class Meta:
#         model = Movie
#         fields = ('title', 'file')

#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['file'].required = False

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'title',
                'placeholder': '제목을 입력하시오',
            }
        )
    )
    description  = forms.CharField(
        label='내용 입력 하세요',
        widget=forms.Textarea(
            attrs={
                'class':'content',
                'placeholder':'내용입력해',
                'rows':5,
                'cols':30,
            }
        )
    )
   
    

    #메타데이터 : 데이터의 데이터
    #ex) 사진 한장 ( 촬영장비이름, 촬영환경 등 )
    class Meta:
        model = Movie
        fields = ('title','description','poster', )     #원하는것만 필드에 나타나게 할 수 있다 ( 'title','content',)

