# split-to-excel

> 대용량의 엑셀 데이터를 나누는데 힘들어하는 직원들을 위해 간단하게 만들었다
>> Main.exe 파일과 같은 폴더에 input.txt 을 위치시킨다<br>
>> 첫번째 줄은 몇개의 데이터씩 분할할지 숫자를 입력<br>
>> 두번째 줄부터는 데이터를 엑셀 파일로부터 복사/붙여넣기한다. (메모장에 붙여넣기할 경우, 각 열을 탭(\t)으로 분리된다)
>> <br>실행 파일(.exe)을 실행하면 output1 ... outputN.xlsx 파일을 생성한다

## 모듈 설치
```
pip install openpyxl
pip install pyinstaller
```

## 실행 파일(.exe) 생성
```
pyinstaller Main.py
```
