import requests
from django.shortcuts import render, redirect
from .forms import NumeroTelefoneForm

def cadastro_numero(request):
    if request.method == "POST":
        form = NumeroTelefoneForm(request.POST)
        if form.is_valid():
            numero_obj = form.save()  # salva no banco
            numero = numero_obj.numero

            # Chamada para WhatsApp API para enviar template
            enviar_template_whatsapp(numero)

            return redirect('cadastro_sucesso')
    else:
        form = NumeroTelefoneForm()
    return render(request, 'cadastro/cadastro.html', {'form': form})

def enviar_template_whatsapp(numero):
    access_token = "EAAorZCvhCOzMBPB0PO9VG1ON9CeH87ZCPRZC1XdoJEN1xlYe6mCh06ZCDWb2hzAq5zdNWd2wtWtZAkC2ev9xNnlCdHiNmodqAYmAeuZAhH4eMUdUCTW1XHzh2S0uctL0NjB28kEqcheDoAb0juZBvqWOVKPKmRHmdBCsleWRQASwTzZCwoAWyNQ7gr5GQUx9EpCd7vcOZAS4ztP3BSFUP4fZACb6aXNaGVISoBZAtdztrB485NTfwZDZD"
    phone_number_id = "726355323897338"
    url = f"https://graph.facebook.com/v15.0/{phone_number_id}/messages"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": numero,  # número no formato "5511999999999"
        "type": "template",
        "template": {
            "name": "nome_do_template_aprovado", 
            "language": {
                "code": "pt_BR"
            },

        }
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code, response.json())


def cadastro_sucesso(request):
    return render(request, 'cadastro/sucesso.html')
