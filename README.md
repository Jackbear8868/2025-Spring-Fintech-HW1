# 金融科技作業 1

### 0.說明:

繳交作業前請詳細閱讀以下部分：
整個學期的作業主軸是希望大家透過學會使用 python 用來畫圖跟進行網路爬蟲，並實際體驗發幣跟幣流追蹤的部分，對於整個金融科技的犯罪過程更加理解，也同時學會如何使用程式語言來加快整個案件蒐集證據的過程。

第一個作業的設計初衷是希望大家學會使用大型語言模型(LLM)來學習撰寫程式，如：ChatGPT, Claude, Gemini...等等。我們會這樣出的原因是，因為以前學習程式的方法就是得觀看 document，或是找到其他人撰寫的範例，然而完成一個專案可能要需要花費 3 個禮拜，而現在的大型語言模型能力非常厲害，能夠提供使用者，許多方便快速的函數跟演算法，大幅度的提升程式語言的撰寫跟學習速率，透過大型語言模型幫我們撰寫出整個框架，再小幅度的修改，就可以在 3 天內完成相同的事情。於是我們希望大家能夠透過學習如何大型語言模型幫助自己學習如何撰寫程式，培養撰寫程式的基礎思維。

### 1. 基礎設置 與 繳交方式：

網路上有相當多的資源在教學如何撰寫 python ，這裡推薦大家依照以下的影片去建立運行程式所需的基礎設置，大家請依照自己的作業系統，來設置運行環境：
Windows：https://youtu.be/jtsBrJyElHg?si=1qT1GeHHBdLyPt5T
MacOS:https://www.youtube.com/watch?v=NirAuEAblvo

詳情請參考這篇：[HW1 步驟](/Nn8EarddQeiB-9sK24qdug)

作業 1~4，輸出答案時都只需將結果`print` 即可，請注意題目的範例答案，若與題目中條件不同，可能導致成績與預期不一樣。

注意：請勿更動檔案位置，這有可能會導致成績與預期不同，後果自負。

### 2. 題目：

#### 1.讀寫檔案 and 字串操作(20%)：

讀寫檔案是完成作業的基本需求，為了檢測各位同學是否能夠完成作業，各位同學需要讀取 `1.txt` 的內容(一行文字)後，請幫我把所有的空格移除(換行不用)，然後將這個內容 `print` 100 次。

假設原本的文件裡只有一個 `Hello, World!` ，那請同學輸出 100 個 `Hello,World!` 。
範例

```
Hello,World! #100行
Hello,World!
Hello,World!
.
.
.
Hello,World!
```

推薦大家觀看下列影片對於此整個 python 觀念更加了解：
基本資料型態、變數：https://youtu.be/rU4I1NQLteo?si=8WC44lUZh59OwJ6d
如何使用字串、字串的用法：https://youtu.be/dNFI2c007Sw?si=C3XOQd6dlEiXw7Qe
如何使用數字、數字的用法：https://youtu.be/eRnRi3n0gIM?si=YOgJ1yOA__48dPT4
檔案的讀取、寫入：https://youtu.be/uHV4V-z5c8E?si=Y1LIjkDOQQALgwuz

#### 2. 陣列、字典、迴圈 (20%)：

各位大學生都是貼心善良的好孩子，今天長輩寫了一張紙條請你去買水果，這張紙條上的內容寫著各種水果的名稱，例如：`apple`, `banana` 等等，長輩把所有水果都寫在 `2.txt` 的檔案中，每一行都是一種水果，請厲害的各位使用剛學習到的 python ，找出需要購買的水果的名稱，並且幫我把水果的名稱進行字典序的排序，並且統計出每個水果相對應的數量 `print` 出來。

答案請依照以下格式：

```
//水果名稱:數量，不同的水果請幫我換行
//水果的順序請按照abc的順序，也注意不要有多餘的空格
apple:100
banana:200
pear:300
```

推薦大家觀看下列影片對於此整個 python 觀念更加了解：
列表介紹、列表的用法：https://youtu.be/orCsnSHc8Mo?si=ft-zZ5HOE-FzYL2v
字典介紹、字典用法：https://youtu.be/DOWswV0CASg?si=o_Hcnwudnarm2stl
for 迴圈：https://youtu.be/4KkK-8CrEz4?si=3dj-O5nJDfviQIWE
while 迴圈：https://youtu.be/cZnp_HtZStg?si=gJHow-pBwmrOtXNG

#### 3. if else 判斷、函式、ASCII Code(20%)：

ASCII Code，是一種以數字表示文字的編碼方式。每個字元，如字母、數字或符號，都有唯一的編碼，範圍從 0 到 127。這是一種廣泛應用於電腦中的一種編碼，C/C++中的字元就是以基於 ASCII 編碼。這裡基於 ASCII 編碼我們可以設計一種相當簡單的加密跟解密算法。
已知可顯示字元的編號範圍是 32~126，總共 95 個字元，所以當我們把字元轉換成 ASCII 編碼後，只要不改變字元的相對順序，把編碼的範圍做一個平移的動作，也就是可顯示字元的編號範圍改成 32 + k ~ 126 + k，然後把每個字元改成 (原本的 ASCII 編碼 - 32 + k) % 95+32，只要想傳遞暗號的兩人彼此知道 k 是什麼就可以順利溝通，而其他不知道 k 的人則只能不斷嘗試找出正確的 k 值。
如今，已知 `3.txt` 使用 k = 78 經過加密，請各位聰明的大學生幫助我解密後，`print` 原本的文稿。

範例答案：

```
An apple a day keeps doctor away.
```

推薦大家觀看下列影片對於此整個 python 觀念更加了解：
if 判斷句：https://youtu.be/z3cUEOyiQIw?si=bda6YdeCjj-UiVIF
函式介紹、函式用法：https://youtu.be/4dZBM3vyxfk?si=vzbX0jWXy3jbqP1B
ASCII code:https://zh.wikipedia.org/zh-tw/ASCII

#### 4. 巢狀迴圈、2 維陣列(20%)：

有些時候，一個迴圈無法完全做到我們想做的事情，這個時候我們可能會在迴圈中再次使用迴圈，形成巢狀迴圈，if else 也會有類似的情況產生，
陣列的話則是 2 維陣列。當然可以使用迴圈中的迴圈中的迴圈中的...，很多個迴圈或是陣列，但是這樣不僅會造成程式很難理解，也會增加許多的負擔，
通常兩層的迴圈已經足夠應付大多數的問題。

以下助教提供一個 50 X 50 的數字表在 `4.txt`中，數字的範圍是 1 ~ 10000 ，每個數字之後都會有一個空格已分開不同數字，每 50 個數字後會有一個換行符號。請各位聰明的大學生使用巢狀迴圈以及 2 陣列讀取並儲存這個數字表，請幫我找出整個數字表中最小的數字，並且幫我抓出每一橫排中最大的數字，進行升序排列，`print` 每個數字。

推薦大家觀看下列影片對於此整個 python 觀念更加了解：
2 維列表、巢狀迴圈：https://youtu.be/pEPlcN7gOVs?si=VwPNFcV7fyduKWw_
常見的排序演算法——氣泡排序(Bubble Sort)：https://youtu.be/XSw6Knd3dcg?si=HWlNm_pgXc7Xp4dn

舉 3 X 3 的數字表為例子：

```
3 2 1
6 5 4
9 8 7
```

答案應該要是:

```
1
3
6
9
```

#### 5. 模組 module(20%)：

大家經過前 4 題的摧殘，應該很累了吧? 最後一題我們來一點簡單的題目，只需要學會安裝模組 `mpmath` ，並且運行以下程式，依照結果回答此 [表單](https://forms.gle/JZXqQcGaHSYVNqyG7) 。

注意：若擅自修改程式可能會導致答案出錯。

推薦大家觀看下列影片對於此整個 python 觀念更加了解：
模組 module 的使用：https://youtu.be/SV5OqR46kEM?si=VZBhLkj0obH2UEx2

```
import math
from mpmath import mp
mp.dps = 100  # 設定小數點後 100 位精度

print(f'math.pi = {math.pi}' )
print(f'mp.pi = {mp.pi}' )
```

以下推薦一些常用的模組提供大家自行學習：`matplotlib`, `math`, `os`, `time`, `random`, `numpy`, `pandas`.
