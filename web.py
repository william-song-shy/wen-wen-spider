from flask import Flask,render_template,flash,request,redirect,url_for
from flask_wtf import Form
import os
app=Flask (__name__)
app.secret_key = os.environ.get('wen-wen-secretkey')
@app.route ("/",methods=['GET','POST'])
def main ():
    return '咕咕咕'
