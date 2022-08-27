from django import forms

from .models import News

###------ModeleForm,Form

# class NewsForm(forms.Form):
# 	#####------------------------ widget=forms.TextInput(attrs={"class":"form-control"})
# 	###### Bu qolda kiritiladi...
# 	title=forms.CharField(max_length=150,label='Nomi', widget=forms.TextInput(attrs = {"class":"form-control"},))

# 	##### required --- belgilangan qatorga kiritish shart emas False bolsa
	
# 	content=forms.CharField(label="Tekst", required=False,widget=forms.Textarea(attrs=
# 		{
# 			"class":"form-control",
# 			"rows":5,

# 		}
# 	))
# 	#####-------------initial funktsiya kalochka qoyiladi hamma vaqt------
# 	is_published=forms.BooleanField(label="Tanlash",initial=True)	
# 	### queryset parametri
# 	category=forms.ModelChoiceField(empty_label="Kategoriyalarni birini tanlang",queryset=Category.objects.all(),label="Kategoriya",widget=forms.Select(attrs={"class":"form-control",}))


class NewsForm(forms.ModelForm):
	class Meta:
		model=News
		fields=['title','content','is_published','category']
		widgets={
			'title':forms.TextInput(attrs={"class":"form-control"}),
			'content':forms.Textarea(attrs={"class":"form-control","rows":5}),
			'category':forms.Select(attrs={"class":"form-control"}),
		}
