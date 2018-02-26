#!/bin/usr/python
#-*- coding: utf8 -*-
import os, getpass, re, time

os.system("clear")
print ("Bem Vindo!")

def nome():
    Nome = raw_input("Informe o seu nome: ")
    match = re.match ('^[a-zA-Z ]+$', Nome)
    if match:
        print 'Nome Válido!'
        time.sleep(1)
        os.system("clear")
    else:
        print 'Nome Inválido!'
        time.sleep(2)
        os.system("clear")
        print 'Digite Novamente: '
        nome()
nome()

def email():
    Email = raw_input("Informe seu e-mail: ")
    match = re.match ('^[a-z]+([._-]?[0-9a-z]+|[0-9])*@[a-z]+([._-]?[0-9a-z]+|[0-9])*(\.com|\.br|.\com\.br)$' , Email)
    if match:
        print 'E-mail Válido!'
        time.sleep(1)
        os.system("clear")
    else:
        print 'E-mail Inválido!'
        time.sleep(2)
        os.system("clear")
        print 'Digite novamente: '
        email()
email()

def cell():
        print 'Formato do número: (DDD) 9xxxx-xxxx'
        CELL = raw_input("Informe o número do seu celular: ")
        match = re.match ('^[(][0-9]{2}[)][ ][9][0-9]{4}[-][0-9]{4}$', CELL)
        if match:
            print 'Número de telefone válido!'
            time.sleep(1)
            os.system("clear")
        else:
            print 'Número de telefone inválido!'
            time.sleep(2)
            os.system("clear")
            print 'Digite novamente: '
            cell()
cell()

def fixo():
        print 'Formato do número de telefone: (DDD) xxxx-xxxx'
        Fixo = raw_input("Informe o número de telefone: ")
        match = re.match ('^[(][0-9]{2}[)][ ][0-9]{4}[-][0-9]{4}$' , Fixo)
        if match:
             print 'Número de telefone válido!'
             time.sleep(1)
             os.system("clear")
        else:
             print 'Número de telefone inválido!'
             time.sleep(2)
             os.system("clear")
             print 'Digite novamente: '
             fixo()
fixo()

def rg():
        RG = raw_input("Informe o número do seu RG: ")
        match = re.match ('^[0-9]{2}\.[0-9]{3}\.[0-9]{3}[-][a-z0-9]$' , RG)
        if match:
            print 'Número do RG válido!'
            time.sleep(1)
            os.system("clear")
        else:
            print 'Número do RG inválido!'
            time.sleep(2)
            os.system("clear")
            print 'Digite novamente: '
            rg()
rg()

def cpf():
        CPF = raw_input("Informe o número do seu CPF: ")
        match = re.match ('^[0-9]{3}\.[0-9]{3}\.[0-9]{3}[-][0-9]{2}$' , CPF)
        if match:
            print 'Número de CPF válido!'
            time.sleep(1)
            os.system("clear")
        else:
            print 'Número de CPf inválido!'
            time.sleep(1)
            os.system("clear")
            print 'Digite novamente: '
            cpf()
cpf()

def data():
        print 'Formato da data: dd/mm/aaaa'
        DATA = raw_input("Informe a sua data de nascimento: ")
        match = re.match ('^(0[1-9]|[12][0-9]|3[0-1])/?(0[1-9]|1[0-2])/?(200[0-9]|201[0-8]|19[0-9]{2})$' , DATA)
        if match:
            print  'Data de nascimeto válida!'
            time.sleep(1)
            os.system("clear")
        else:
            print 'Data de nascimento inválida!'
            time.sleep(2)
            os.system("clear")
            print 'Digite novamente: '
            data()
data()

def ip():
        IP = raw_input("Informe o seu IP: ")
        match = re.match ('^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}$', IP)
        if match:
            print 'Ip válido!'
            time.sleep(1)
            os.system("clear")
        else:
            print 'IP inválido!'
            time.sleep(2)
            os.system("clear")
            print 'Digite Novamente: '
            ip()
ip()

def mascara():
        Mascara = raw_input("Informe sua Mascara: ")
        match = re.search(r'^(254|252|248|240|224|192|128)(.0){3}$|^255(.255|.254|.252|.248|.240|.224|.192|.128|.0){3}$', Mascara)
        if match:
            print 'Mascara válida'
            time.sleep(1)
            os.system("clear")
        else:
            print 'Mascara inválida'
            time.sleep(2)
            os.system("clear")
            print 'Digite novamente: '
            mascara()
mascara()
