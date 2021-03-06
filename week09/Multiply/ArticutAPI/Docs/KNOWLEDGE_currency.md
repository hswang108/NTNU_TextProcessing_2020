# Articut: KNOWLEDGE_currency 標記說明
------------------
## 支援表示格式
### 金額+貨幣 (含全形、大小寫中文數字及混用數字)
* 費用共為**`150 元`**
* 多花了他**`五塊錢`**才買到
* 標價為**`149.99 法郎`**呢！
* 只要**`99.99 先令`**就能買一組哦！
* 每杯**`三百六十盧布`**很划算的。
* 欠下**`兩佰億歐元`**的債務。
* 每季收入**`200萬日幣`**的銷售額。(半形數字+國字數字)

### 貨幣名稱+金額+貨幣單位 (含全形數字。若貨幣名稱在數字以前，則優先向後擷取至貨幣單位。)
* 日幣**`10,000.33 元`**的漲幅。(美式千元符「,」，「元」前有空格。)
* 韓元**`50'000 元`**只有一點點。(歐式千元符「\'」，「元」前有空格。)
* 美金**`99.99 元`**就能買三包。(小數點「.」，「元」前有空格。)
* 美金**`伍仟參佰捌拾塊錢`**的金額。(大寫中文數字。)
* 歐元**`９９０元`**(全型數字，元前不加空格)
* 新台幣**`一百零五萬元`**
* 英鎊**`二十五萬元`**
* 印尼**`三百卅盾`**(大寫中文數字「卅」)
* 新加坡幣**`廿萬元`**(大寫中文數字「廿」)
* 加幣**`壹仟參佰陸拾萬 元`**(大寫中文數字，「元」前有空格。)

## 注意！！！
### 貨幣名稱+數字+「非」貨幣單位
#### 為避免產生誤判，如果數字後並「非」貨幣單位，則不會往後擷取。雖然「美金30」看起來是貨幣，但也可能會是：
* 美金*`30`*天內跌了 5%… (此時「100」不會被標為**KNOWLEDGE_currency**)
* 日幣*`2`*度大漲… (此時的「2」不會被標為 **KNOWLEDGE_currency**)

------------------
## 支援貨幣單位
元、塊錢
## 支援貨幣列表
### 亞洲地區
* 新台幣、新臺幣、台幣、臺幣
* 日幣、日圓、日元
* 韓圜、韓幣、韓元
* 泰銖、泰幣
* 人民幣
* 港幣
* 新加坡幣、新幣
* 菲律賓披索、菲律賓比索、菲國披索、菲國比索
* 越南盾
* 印尼幣
* 馬來幣
* 緬元

### 美洲地區
* 美金、美元
* 加拿大幣、加幣
* 墨西哥披索、墨西哥比索

### 歐洲地區
* 歐元
* 法郎、瑞士法郎
* 英鎊、先令
* 盧布、盧比 

### 大洋洲地區
* 澳幣

### 非洲地區
* 南非幣