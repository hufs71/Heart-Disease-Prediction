import requests

def download_file(url, save_path):
    # 요청을 보내어 데이터를 받아옴
    response = requests.get(url)
    response.raise_for_status()  # 오류가 발생하면 예외를 발생시킵니다.

    # 바이너리 모드로 파일을 열고 데이터를 저장
    with open(save_path, 'wb') as f:
        f.write(response.content)

# 파일 URL
# 2021년 BRFSS dataset
url = 'https://www.cdc.gov/brfss/annual_data/2021/files/LLCP2021XPT.zip'
# 파일 저장 경로
save_path = 'LLCP2021XPT.zip'

# 파일 다운로드 함수 호출
download_file(url, save_path)


import zipfile
import pyreadstat

# 파일 압축 해제
with zipfile.ZipFile('LLCP2021XPT.zip', 'r') as zip_ref:
    zip_ref.extractall('.')

# 원 데이터 경로
xpt_file_path = './LLCP2021.XPT'

# XPT 파일 로드
df, meta = pyreadstat.read_xport(xpt_file_path)

# 데이터 프레임과 메타데이터 출력
print(df.head())
print(meta.variable_value_labels)
