# programa para generar un mail

mail_nombre = "Ubaldo Acosta Soto"
mail_empresa = "Global Mentoring"
mail_dominio = "com.mx"

# el resultado tiene que ser:
# email: ubaldo.acosta.soto@globalmentoring.com.mx
mail_empresa = mail_empresa.replace(" ", "")
email = mail_nombre +  "@"  + mail_empresa + "." + mail_dominio
email = email.lower()
email = email.replace(" ",".")

print(f'El mail es: {email}')