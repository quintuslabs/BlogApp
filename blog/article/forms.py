from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image"]
        
     # this function will be used for the validation 
    def clean(self):   
        # data from the form is fetched using super function 
        super(ArticleForm, self).clean() 
          
        # extract the username and text field from the data 
        title = self.cleaned_data.get('title') 
        content = self.cleaned_data.get('content') 
  
        # conditions to be met for the username length 
        if (title and len(title) < 5): 
            self._errors['title'] = self.error_class([ 
                'Minimum 5 characters required']) 
        if (content and len(content) <10): 
            self._errors['content'] = self.error_class([ 
                'Post Should Contain minimum 10 characters']) 
  
        # return any errors if found 
        return self.cleaned_data 