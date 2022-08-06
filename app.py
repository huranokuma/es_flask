from flask import Flask, render_template,request
from function import catch_sentence
import asyncio
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/donation")
def donation():
    return render_template('donation.html')

@app.route("/app1",methods=['GET','POST'])
async def app1():
    if request.method == 'GET': #普通にurlでぺージに来た場合
        result={
    'sentence':'',
    'elapsed_time':''
} 
        #値がないとエラーが出るので空の値を渡しておく
        return render_template('app1.html',result=result)
    if request.method == 'POST':
        print('POSTデータ受け取ったので処理します。')
        if request.form['prompt_text']!=None:
          prompt_text = request.form['prompt_text']
          print(prompt_text)
        else:
          prompt_text = '私'
        
        if request.form['max_length']!=None:
            max_length = int(request.form['max_length'])
            print(max_length)
        else:
            max_length=100
        start = time.time()

        sentence,elapsed_time= await catch_sentence(prompt_text=prompt_text,max_length=max_length)

        result={
            'sentence':sentence,
            'elapsed_time':elapsed_time
        }
        print('文章を生成しました')
            
        print('経過時間:'+str(round(time.time()-start,2)))    
        return render_template('app1.html',result=result)
