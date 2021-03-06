#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#讀取 json 的程式
import json

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,'r',encoding="utf-8") as f:
        content=json.load(f)
    return content
#將字串轉為「句子」列表的程式

def text2Sentence(inputSTR):
    for item in ("、","，","。"):
        inputSTR = inputSTR.replace(item,'<cutting mark>')
    for item in ("...","…"):
        inputSTR = inputSTR.replace(item,'')
    for i in range(len(inputSTR)):
        if inputSTR[i] == "," and inputSTR[i-1]not in ['0','1','2','3','4','5','6','7','8','9']:
           inputSTR=inputSTR[:i]+"<cutting mark>"+inputSTR[i+1:]
    inputList=inputSTR.split('<cutting mark>')[:-1]
    return(inputList)

if __name__== "__main__":
    #設定要讀取的 news.json 路徑

    #將 news.json 利用 [讀取 json] 的程式打開

    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST

    #設定要讀取的 test.json 路徑

    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIS

    #測試是否達到作業需求

    jsonFilePath = "./example/news.json"

    newsSTR = jsonTextReader(jsonFilePath)["text"]

    newsLIST = text2Sentence(newsSTR)

    jsonFilePath2 = "./example/test.json"

    testLIST = jsonTextReader(jsonFilePath2)["sentence"]

    if newsLIST == testLIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")