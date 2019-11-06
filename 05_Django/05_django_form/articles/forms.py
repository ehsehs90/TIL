from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=30,
#         #HTML Tag 와 동일
#         label = '제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class':'title',
#                 'placeholder':'제목을 입력하세요',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class' : 'content',
#                 'placeholder' : '내용을 입력해',
#                 'rows' : 5,
#                 'cols' :30,
#             }
#         )
#     )
# 메타데이터 사용하려면 모델  import필요

class ArticleForm(forms.ModelForm):

    #메타데이터 : 데이터의 데이터
    #ex) 사진 한장 ( 촬영장비이름, 촬영환경 등 )
    class Meta:
        model = Article
        fields = '__all__'
