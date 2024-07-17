# 데이터 전처리
# 양성은 1, 음성은 0으로 통일
# 모름, 응답거부 제거
def get_preprocessed(df):

    # _MICHD
    # 심장질환 음성: 2 -> 0 
    df['_MICHD'] = df['_MICHD'].replace({2: 0})


    # _RFHYPE6, 고혈압 여부
    # 음성: 1 -> 0
    # 양성: 2 -> 1
    df['_RFHYPE6'] = df['_RFHYPE6'].replace({1:0, 2:1})
    df = df[df._RFHYPE6 != 9]


    # TOLDHI3, 고콜레스테롤 여부
    # No: 2 -> 0 
    # 모름: 7 제거
    # 응답거부: 9 제거
    df['TOLDHI3'] = df['TOLDHI3'].replace({2:0})
    df = df[df.TOLDHI3 != 7]
    df = df[df.TOLDHI3 != 9]


    # CHOLCHK3, 최근 콜레스테롤 수치 검사 여부
    # 지난 5년간 검사한 적 없음: 1 -> 0, 8 -> 0 
    # 모름: 7 제거
    # 응답거부: 9 제거
    df['CHOLCHK3'] = df['CHOLCHK3'].replace({1:0,2:1,3:1,4:1,5:1,6:1,8:0})
    df = df[df.CHOLCHK3 != 7]
    df = df[df.CHOLCHK3 != 9]


    # _BMI5, 체질량지수(BMI)
    # 네 자리 숫자로 기록되어 있으므로 100을 곱한 후 정수 변환
    df['_BMI5'] = df['_BMI5'].div(100).round(0)


    # SMOKE100, 흡연 여부
    # No: 2 -> 0 
    # 모름: 7 제거
    # 응답거부: 9 제거
    df['SMOKE100'] = df['SMOKE100'].replace({2:0})
    df = df[df.SMOKE100 != 7]
    df = df[df.SMOKE100 != 9]


    #6 CVDSTRK3, 뇌졸중 여부
    # No: 2 -> 0
    # 모름: 7 제거
    # 응답거부: 9 제거
    df['CVDSTRK3'] = df['CVDSTRK3'].replace({2:0})
    df = df[df.CVDSTRK3 != 7]
    df = df[df.CVDSTRK3 != 9]


    # DIABETE4, 당뇨병 여부
    # 당뇨병 음성이거나 임신시에만 걸렸던 경우: 0 
    # 당뇨병 양성, 당뇨 전 단계, borderline diabetes: 1 
    # 모름: 7 제거
    # 응답거부: 9 제거
    df['DIABETE4'] = df['DIABETE4'].replace({2:0, 3:0, 4:1})
    df = df[df.DIABETE4 != 7]
    df = df[df.DIABETE4 != 9]


    # _TOTINDA, 신체활동 수준
    # 신체활동 함: 1
    # 신체활동 안함: 2 -> 0 
    # 모름/응답거부: 9 제거
    df['_TOTINDA'] = df['_TOTINDA'].replace({2:0})
    df = df[df._TOTINDA != 9]


    # _FRTLT1A, 과일 섭취 수준
    # 일일 과일 섭취 없음: 2 -> 0
    # 모름/결측치: 9 제거
    df['_FRTLT1A'] = df['_FRTLT1A'].replace({2:0})
    df = df[df._FRTLT1A != 9]


    # _VEGLT1A, 채소 섭취 수준
    # 일일 채소 섭취 없음: 2 -> 0
    # 모름/결측치: 9 제거
    df['_VEGLT1A'] = df['_VEGLT1A'].replace({2:0})
    df = df[df._VEGLT1A != 9]


    # _RFDRHV7, 과도한 음주 여부
    # Yes: 2 -> 1
    # No: 1 -> 0
    # 모름/결측치: 9 제거
    df['_RFDRHV7'] = df['_RFDRHV7'].replace({1:0, 2:1})
    df = df[df._RFDRHV7 != 9]


    # _HLTHPLN, 의료보험 가입 여부
    # No: 2 -> 0
    # 모름/응답거부: 9 제거
    df['_HLTHPLN'] = df['_HLTHPLN'].replace({2:0})
    df = df[df._HLTHPLN != 9]


    # MEDCOST1, 의료비 부담 여부
    # No: 2 -> 0
    # 모름: 7 제거
    # 응답거부: 9 제거
    df['MEDCOST1'] = df['MEDCOST1'].replace({2:0})
    df = df[df.MEDCOST1 != 7]
    df = df[df.MEDCOST1 != 9]


    # GENHLTH, 전반적인 건강 상태
    # 모름: 7 제거
    # 응답거부: 9 제거
    df = df[df.GENHLTH != 7]
    df = df[df.GENHLTH != 9]


    # MENTHLTH, 정신건강 상태
    # no bad mental health days: 88 -> 0
    # 모름: 77 제거
    # 응답거부: 99 제거
    df['MENTHLTH'] = df['MENTHLTH'].replace({88:0})
    df = df[df.MENTHLTH != 77]
    df = df[df.MENTHLTH != 99]


    # PHYSHLTH, 신체건강 상태
    # no bad physical health days: 88 -> 0
    # 모름: 77 제거
    # 응답거부: 99 제거
    df['PHYSHLTH'] = df['PHYSHLTH'].replace({88:0})
    df = df[df.PHYSHLTH != 77]
    df = df[df.PHYSHLTH != 99]


    # DIFFWALK, 걷기 어려움 여부
    # No: 2 -> 0
    # 모름: 7 제거
    # 응답거부: 9 제거
    df['DIFFWALK'] = df['DIFFWALK'].replace({2:0})
    df = df[df.DIFFWALK != 7]
    df = df[df.DIFFWALK != 9]


    # _SEX, 성별
    # Female: 2 -> 0
    df['_SEX'] = df['_SEX'].replace({2:0})


    # _AGEG5YR, 연령대
    # 모름/결측치: 14 제거
    df = df[df._AGEG5YR != 14]


    # EDUCA, 교육 수준
    # 응답거부: 9 제거
    df = df[df.EDUCA != 9]


    # INCOME3, 가구 소득 수준
    # 모름: 77 제거
    # 응답거부: 99 제거
    df = df[df.INCOME3 != 77]
    df = df[df.INCOME3 != 99]

    return df
