import web
from web import form

render = web.template.render('templates/', base = 'base')

urls = ('/', 'index' )
app = web.application(urls, globals())

myform = form.Form( 
    form.Textbox("Nombre"), 
    form.Textbox("Telefono", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        form.Validator('Must be more than 5', lambda x:int(x)>5)), 
    form.Textbox("Nacimiento", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        form.Validator('No puede ser mayor a 2016', lambda x:int(x)<2016) ),   
    form.Textarea('Email'),
    form.Checkbox('INE', value='INE'),  
    form.Dropdown('Genero', ['Macho Alfa','Mujer' ])) 

class index: 
    def GET(self): 
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtest(form)

    def POST(self): 
        form = myform() 
        if not form.validates(): 
            return render.formtest(form)
        else: 
            age = 2016 - int(form.d.Nacimiento) 
            if age >= 18 and form.d.INE == True: 
                return "Felicidades puedes votar" 
            else:
                return "No puedes votar"    
              

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()